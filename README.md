# sns-ops-wiki

X・Instagram・note など SNS の使い方・設定・投稿ノウハウ・収益化条件を、Markdown で体系化したナレッジベースです。運用の題材は**古事記・日本書紀**で、目的は**認知拡大と収益化**です。

- 作成開始: 2026年(皇紀2686年・令和8年)11月3日
- 言語: 日本語(専門用語は英語＋日本語訳)
- 公開範囲: **public** — 認証情報・非公開の運用数値・顧客情報は絶対に書かない(→ [CONTRIBUTING.md](CONTRIBUTING.md))

## 目次

| 区分 | 場所 | 内容 |
|---|---|---|
| メタ情報 | [docs/00-meta/](docs/00-meta/) | 読み方、用語集、出典方針、ページ雛形、**要検証リスト**、ロードマップ、品質レビュー記録 |
| 共通知識 | [docs/01-common/](docs/01-common/) | 画像仕様の横断比較、制作工程、ハッシュタグ、代替テキスト、コメント運用、文章術、動画、検索、AI 方針、著作権、法令、炎上対応、ツール、FAQ |
| X | [docs/02-x/](docs/02-x/) | 旧 Twitter |
| Instagram | [docs/03-instagram/](docs/03-instagram/) | フィード・リール・ストーリーズ |
| note | [docs/04-note/](docs/04-note/) | 記事・マガジン・メンバーシップ |
| テーマ運用 | [docs/05-theme-kojiki/](docs/05-theme-kojiki/) | 古事記・日本書紀の原典、表記、年表、企画、画像、配慮、連載案 |
| 全体戦略 | [docs/06-strategy/](docs/06-strategy/) | 目標・KPI、導線、収益化計画、税務、リスク、調査 |
| 運用アカウント | [docs/07-accounts/](docs/07-accounts/) | 運用方針、プロフィール案 |
| 今後の追加候補 | [docs/99-planned/](docs/99-planned/) | Threads, YouTube, TikTok, Bluesky ほか |
| 雛形 | [templates/](templates/) | 投稿計画、週次レビュー、画像チェックリスト |
| 検査 | [scripts/check_wiki.py](scripts/check_wiki.py) | リンク・front matter・年換算・鮮度・秘密情報の検査 |

## 各サービスのページ構成(共通)

| 番号 | ファイル | 内容 |
|---|---|---|
| — | `README.md` | 概要・特徴・向いている用途 |
| 01 | `01-account-setup.md` | 初期設定 |
| 02 | `02-posting.md` | 投稿ルート(種類・手順・予約) |
| 03 | `03-media-specs.md` | 画像・動画のファイル形式、サイズ、アスペクト比 |
| 04 | `04-text-hashtags.md` | 文字数、ハッシュタグ、メンション、リンク |
| 05 | `05-alt-text.md` | 画像の説明文(alt text) |
| 06 | `06-engagement.md` | コメント・返信・DM・コミュニティ運用 |
| 07 | `07-monetization.md` | 収益化の条件・方法 |
| 08 | `08-analytics.md` | 分析・KPI |
| 09 | `09-tips.md` | ノウハウ・コツ |
| 10 | `10-policies.md` | ガイドライン・禁止事項・法令 |
| 11 | `11-checklist.md` | 運用チェックリスト |
| 12 | `12-theme-application.md` | 古事記・日本書紀テーマへの適用 |

## 情報の信頼度表示

各ページ先頭の front matter と本文の数値に、次の確度ラベルを付けています。詳細は [出典方針](docs/00-meta/source-policy.md)。

| ラベル | 意味 |
|---|---|
| ✅ | 公式(一次資料)で確認済み |
| 🟡 | 二次資料(解説記事等)のみ。公式で要確認 |
| ⚪ | 一般的な知識・経験則。出典未確認 |

> **重要**: 仕様・収益化条件は頻繁に変わります。2026年(皇紀2686年・令和8年)11月3日の作成時点では、実行環境の制約により公式ヘルプの本文を取得できなかったため、**多くの数値が 🟡/⚪ です**。確認待ちの項目は [verification-queue.md](docs/00-meta/verification-queue.md) に集約しています。

## 検査の実行

```bash
python3 -I scripts/check_wiki.py
```
