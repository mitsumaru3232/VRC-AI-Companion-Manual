# VRC AI Companion マニュアル

> **マイクが認識しない・機能が動作しない・変更が反映されないとき**
>
> マイクが認識しない、機能が動作しない・設定変更や更新が反映されない場合は、画面上部の **「アプリ」→「再起動」** を実施してください。再起動後、もう一度動作を確認してください。
> 改善しない場合は、[困ったとき](troubleshooting.md)をご確認ください。

VRChatでの会話を、AIと一緒に楽しむためのガイドです。
マイクで話しかけると、AIがアプリ内やVRChatのチャットボックスへ文字で返答します。文字入力だけでも使えます。

**対象：0.5.0 ベータ版 / Windows 11 64bit（x64）**

最終更新：2026年9月23日。配布識別「2026-09-21-kat-parakeet」の操作に対応しています。
配布識別は、EXEと同じフォルダの「バージョン.txt」で確認できます。

## はじめて使う方へ

まずは、マイクやVRChatを使わずに「会話」で返答を確認しましょう。

1. [動作環境と必要なもの](getting-started/requirements.md)を確認する。
2. [ダウンロードと初回起動](getting-started/install.md)を進める。
3. [使うAIを選ぶ](ai/README.md)。クラウドAIには、ご自身のAPIキーが必要です。
4. [初回セットアップ](getting-started/setup.md)を終え、文字で会話する。
5. [マイクを設定](audio/microphone.md)し、[VRChatに返答を表示](vrchat/README.md)する。

![会話画面。左側でページを選び、下の入力欄から送信します。](assets/screenshots/chat.png)

*画像は実際のアプリ画面です。説明用の会話例を使い、AI・マイク・VRChatへの接続を停止して撮影しています。モデル名や状態表示は、お使いの環境と異なる場合があります。*

## やりたいことから探す

| やりたいこと | 読むページ |
| --- | --- |
| APIキーを用意したい | [OpenAI](ai/openai.md) / [Anthropic・Claude](ai/anthropic.md) / [Google Gemini](ai/gemini.md) |
| パソコン内のAIで使いたい | [Ollamaの導入](ai/ollama.md) |
| APIキーの入力場所を知りたい | [アプリへの登録・AIの切り替え](ai/register.md) |
| 他の人の声にも反応してほしい | [周囲の音声（ベータ版）](audio/nearby.md) |
| ムチォの文字盤にAIの返答を出したい | [ムチォとの連携](vrchat/mucho.md) |
| 名前・性格・返答の長さを変えたい | [名前と性格](usage/character.md) |
| 覚えたことを確認・修正したい | [記憶と会話履歴](usage/memory.md) |
| 認識しない・返事がない・表示されない | [困ったとき](troubleshooting.md) |
| 新しい版に更新したい | [更新・バックアップ・初期化](maintenance.md) |

## 利用前に

**会話の自然さ・文脈の理解・返答の正確さは、使用するAIサービスやモデルによって大きく異なります。**
同じ設定や話しかけ方でも、話がかみ合わなかったり、意図と異なる返答になることがあります。[AIを選ぶときの注意点](ai/README.md)も確認してください。

アプリの購入代金に、外部AIサービスの利用料は含まれません。[料金とAPIキーの注意点](ai/costs-and-keys.md)を確認してください。
他の人の会話を取り込む場合は、相手への説明と必要な同意、利用場所のルールを確認してください。

[利用規約](legal/terms.md)・[データの取り扱い](legal/privacy.md)・[第三者ライセンス](legal/third-party.md)・[お問い合わせ](support.md)

VRC AI Companionは、VRChatの非公式外部アプリです。
