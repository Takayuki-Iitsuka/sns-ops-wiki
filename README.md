# sns-ops-wiki

SNS の**使い方・設定・投稿ノウハウ・画像と動画の仕様・収益化条件・API 活用**を、Markdown で体系化したナレッジベースです。題材(テーマ)ごとの内容は含まず、**SNS 運用そのもの**に限ります。

- 作成開始: 2026年(皇紀2686年・令和8年)11月3日
- 言語: 日本語(専門用語は英語＋日本語訳)
- 公開範囲: **public** — 認証情報・非公開の運用数値・顧客情報は絶対に書かない(→ [CONTRIBUTING.md](CONTRIBUTING.md))

## 目次

| 区分 | 場所 | 内容 |
|---|---|---|
| メタ情報 | [docs/00-meta/](docs/00-meta/) | 読み方、用語集、出典方針、ページ雛形、**要検証リスト**、ロードマップ、品質レビュー記録 |
| 共通知識 | [docs/01-common/](docs/01-common/) | **画像・動画の仕様比較と書き出しプリセット**、制作工程、ハッシュタグ、代替テキスト、コメント運用、文章術、企画、検索、AI 方針、著作権、法令、炎上対応、FAQ |
| X | [docs/02-x/](docs/02-x/) | 旧 Twitter。**Subscriptions(月額購読)**を含む |
| Instagram | [docs/03-instagram/](docs/03-instagram/) | フィード・リール・ストーリーズ |
| note | [docs/04-note/](docs/04-note/) | 記事・マガジン・メンバーシップ |
| YouTube | [docs/05-youtube/](docs/05-youtube/) | 長尺・Shorts・ライブ・収益化 |
| TikTok | [docs/06-tiktok/](docs/06-tiktok/) | 縦型動画・Creator Rewards |
| Threads | [docs/07-threads/](docs/07-threads/) | Meta のテキスト SNS |
| Facebook | [docs/08-facebook/](docs/08-facebook/) | ページ・グループ・リール |
| その他 | [docs/09-other-services/](docs/09-other-services/) | Bluesky、LINE 公式アカウント、Twitch、**Discord** |
| 収益化サービス | [docs/10-creator-economy/](docs/10-creator-economy/) | FANBOX、Fantia、Patreon、Ko-fi、BOOTH、SUZURI、KDP、アフィリエイト、メンバーシップ設計 |
| **API** | [docs/20-api/](docs/20-api/) | **X API v1.1 → v2 移行**、Instagram/Threads/YouTube/TikTok/LINE/Bluesky、**API のメリット**、**ツール連携**、自動化の方針、パイプライン設計 |
| **料金プラン** | [docs/40-pricing/](docs/40-pricing/) | **X と Grok の関係・料金、Google(AI・YouTube Premium・Gemini API)、Meta One、note、AI・制作・予約ツール、費用の見積り** |
| 全体戦略 | [docs/30-strategy/](docs/30-strategy/) | 目標・KPI、導線、収益化計画、税務、リスク、調査 |
| 運用アカウント | [docs/31-accounts/](docs/31-accounts/) | 運用アカウントの台帳(公開情報のみ) |
| 追加候補 | [docs/99-planned/](docs/99-planned/) | Pinterest ほか(Discord・X Subscriptions は作成済み) |
| 雛形 | [templates/](templates/) | 投稿計画、週次レビュー、画像チェックリスト |
| 検査 | [scripts/check_wiki.py](scripts/check_wiki.py) | リンク・front matter・年換算・鮮度・秘密情報の検査 |

## 最初に見るページ

- 画像のサイズ・比率: [image-specs-comparison](docs/01-common/image-specs-comparison.md)
- 動画の長さ・容量・比率: [video-specs-comparison](docs/01-common/video-specs-comparison.md)
- そのまま使える書き出し値: [export-presets](docs/01-common/export-presets.md)
- X API の移行: [02-x-api](docs/20-api/02-x-api.md)
- スマホで見やすい画像・動画サイズの考察: [mobile-viewing-optimization](docs/01-common/mobile-viewing-optimization.md)
- ALT の詳細: [alt-text](docs/01-common/alt-text.md)
- ハッシュタグの効率的な使い方: [hashtags](docs/01-common/hashtags.md)
- AI 利用のルールと設定: [ai-rules-by-platform](docs/01-common/ai-rules-by-platform.md)
- 料金プラン: [40-pricing](docs/40-pricing/README.md)
- 未整備事項の考察: [gap-analysis](docs/00-meta/gap-analysis.md)
- 収益化の比較: [monetization-comparison](docs/01-common/monetization-comparison.md)

## 情報の信頼度表示

各ページ先頭の front matter と本文の数値に、次の確度ラベルを付けています。詳細は [出典方針](docs/00-meta/source-policy.md)。

| ラベル | 意味 |
|---|---|
| ✅ | 公式(一次資料)で確認済み |
| 🟡 | 二次資料(解説記事・検索要約)のみ。公式で要確認 |
| ⚪ | 一般的な知識・経験則。出典未確認 |

> **重要**: 仕様・収益化条件・API 料金は頻繁に変わります。2026年(皇紀2686年・令和8年)11月3日に、**X(docs.x.com)、Instagram・Threads(developers.facebook.com)、YouTube ヘルプ、LINE 開発者文書、消費者庁の本文を直接取得して ✅ に更新**しました。取得できなかったもの(help.x.com、help-note.com など)は 🟡/⚪ のままです。確認状況は [verification-queue.md](docs/00-meta/verification-queue.md) に集約しています。

## 検査の実行

```bash
python3 -I scripts/check_wiki.py
```
