"""公開マニュアルのリンク・目次・画像整合性を標準ライブラリで検査する。"""

from __future__ import annotations

import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
EXCLUDED = {".git", ".preview", "__pycache__"}
ALLOWED_SUFFIXES = {".md", ".png", ".json", ".yaml", ".yml"}
ALLOWED_FILES = {".gitignore", ".gitattributes", "scripts/check_docs.py"}


def anchors(text: str) -> set[str]:
    """このリポジトリで使う通常のMarkdown見出しからアンカーを求める。"""
    result: set[str] = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        value, index = base, 0
        while value in result:
            index += 1
            value = f"{base}-{index}"
        result.add(value)
    return result


def main() -> int:
    """ネットワークへ接続せず、公開候補を検査する。"""
    errors: list[str] = []
    files = [p for p in ROOT.rglob("*") if p.is_file()
             and not any(part in EXCLUDED for part in p.relative_to(ROOT).parts)]
    pages = {p: p.read_text(encoding="utf-8") for p in files if p.suffix == ".md"}
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix not in ALLOWED_SUFFIXES and relative not in ALLOWED_FILES:
            errors.append(f"公開対象外のファイル: {relative}")
        if path.suffix != ".png":
            value = path.read_text(encoding="utf-8")
            if re.search(r"(?:sk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}|AIza[A-Za-z0-9_-]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)", value):
                errors.append(f"秘密情報の疑い（内容は非表示）: {relative}")
    for page, content in pages.items():
        if not content.startswith("# "):
            errors.append(f"ページタイトルなし: {page.relative_to(ROOT)}")
        for raw in LINK.findall(content):
            parsed = urlsplit(raw.strip("<>"))
            if parsed.scheme or parsed.netloc:
                continue
            target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append(f"リンク先なし: {page.relative_to(ROOT)} -> {raw}")
            elif parsed.fragment and target.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"見出しなし: {page.relative_to(ROOT)} -> {raw}")
    summary = ROOT / "SUMMARY.md"
    indexed = {(ROOT / urlsplit(raw).path).resolve() for raw in LINK.findall(pages[summary])}
    for page in pages:
        if page.name not in {"SUMMARY.md", "CONTRIBUTING.md"} and page not in indexed:
            errors.append(f"目次に未登録: {page.relative_to(ROOT)}")
    folder = ROOT / "assets" / "screenshots"
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    if not manifest.get("sample_data") or manifest.get("contains_real_credentials") is not False:
        errors.append("撮影データの条件を確認してください")
    recorded: set[str] = set()
    for entry in manifest["images"]:
        name = entry["file"]
        path = (folder / name).resolve()
        if not path.is_relative_to(folder) or not path.is_file():
            errors.append(f"画像なし: {name}")
            continue
        data = path.read_bytes()
        recorded.add(name)
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            errors.append(f"画像ハッシュ不一致: {name}")
        if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != (entry["width"], entry["height"]):
            errors.append(f"画像形式・寸法不一致: {name}")
    if recorded != {p.name for p in folder.glob("*.png")}:
        errors.append("画像一覧とmanifestが一致しません")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(pages)} Markdown files, {len(recorded)} screenshots: {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
