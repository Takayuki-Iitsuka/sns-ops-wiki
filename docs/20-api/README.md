---
title: API 活用ガイド(索引)
platform: common
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.google.com/youtube/v3/determine_quota_cost
  - https://developers.tiktok.com/doc/content-sharing-guidelines
  - https://developers.line.biz/ja/docs/messaging-api/pricing/
---

# API 活用ガイド

> **このページで分かること**: API のページの一覧と、初心者が読む順番、サービス別の比較。
>
> **対象**: すべての人  **最初に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

SNS の **API(Application Programming Interface、プログラムから操作する公式の窓口)** を使った、投稿の予約・自動化、分析データの取得、複数サービスへの同時配信の設計をまとめます。

> 2026年(皇紀2686年・令和8年)11月3日に、**X(docs.x.com)、Instagram・Threads(developers.facebook.com)の公式文書を直接取得して確認**しました(✅)。YouTube Data API、TikTok、LINE の API、Bluesky などは未取得で、🟡/⚪ のままです(#38〜#40)。価格・上限は変わるため、実運用前に公式で再確認してください。
>
> **追記(同日)**: YouTube(developers.google.com)、TikTok(developers.tiktok.com)、LINE(developers.line.biz)、Facebook ページの投稿 API も公式文書を直接取得して ✅ に更新しました。Bluesky は公式文書を取得できず 🟡 のままです。

## 初心者の読む順番

| 順番 | ページ | 内容 |
|---|---|---|
| 1 | [00-api-for-beginners](00-api-for-beginners.md) | **API 入門**: 仕組み、リクエスト/レスポンスの読み方、始める流れ |
| 2 | [13-secrets-management](13-secrets-management.md) | **鍵の安全な保管**: `.env`、`.gitignore`、漏えい時の対応 |
| 3 | [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) | **認証**: OAuth 2.0、アクセストークン、スコープ、有効期限 |
| 4 | [15-python-first-steps](15-python-first-steps.md) | **Python で最初の1回**(読み取り) |
| 5 | [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) | **よくあるエラー**(401・403・429)と再試行 |
| 6 | 使うサービスのページ(下の一覧) | 準備・上限・コード例 |

## ページ一覧

| ページ | 内容 |
|---|---|
| [00-api-for-beginners](00-api-for-beginners.md) | **API 入門(初心者向け)** |
| [01-concepts-and-security](01-concepts-and-security.md) | 認証、スコープ、トークン管理、レート制限、リトライ |
| [02-x-api](02-x-api.md) | **X API: v1.1 から v2 への移行**、料金、メディア投稿 |
| [03-instagram-graph-api](03-instagram-graph-api.md) | Instagram の公開 API |
| [04-threads-api](04-threads-api.md) | Threads の公開 API |
| [05-youtube-data-api](05-youtube-data-api.md) | YouTube Data API(アップロード、クォータ、監査) |
| [06-tiktok-api](06-tiktok-api.md) | TikTok の API |
| [07-other-apis](07-other-apis.md) | Facebook、LINE、Bluesky、Twitch、note |
| [08-automation-and-tools](08-automation-and-tools.md) | 自動化の方針・ツール・規約 |
| [09-architecture-patterns](09-architecture-patterns.md) | 投稿パイプラインの設計 |
| [10-benefits-of-api](10-benefits-of-api.md) | **API のメリット・デメリット・判断基準・ユースケース** |
| [11-tool-integrations](11-tool-integrations.md) | **他のツールとの連携** |
| [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) | **認証の基本**(OAuth 2.0・トークン・スコープ・サービス別の有効期限) |
| [13-secrets-management](13-secrets-management.md) | **API キー・トークンの安全な保管** |
| [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) | **よくあるエラーと対処**(X・Meta・YouTube・TikTok・LINE) |
| [15-python-first-steps](15-python-first-steps.md) | **Python で API を呼ぶ最初の一歩** |
| [16-x-api-getting-started](16-x-api-getting-started.md) | **X API をはじめる**(登録・アプリ作成・費用上限・最初の投稿) |
| [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md) | **X API のメディア投稿とレート制限**(02-x-api §6・§7 の詳細) |

## 用語(このフォルダでよく出るもの)

| 用語 | 意味 |
|---|---|
| endpoint(エンドポイント) | 操作ごとの URL |
| access token(アクセストークン) | API を呼ぶための期限付きの許可証 |
| scope(スコープ) | トークンで許す操作の範囲 |
| rate limit(レート制限) | 一定時間あたりの回数の上限 |
| quota(クォータ) | 1日などに使える量の上限 |
| audit / App Review(監査 / アプリ審査) | サービスがアプリの用途を確認する手続き |

詳しくは [00-api-for-beginners](00-api-for-beginners.md) の用語表と [glossary](../00-meta/glossary.md)。

## 横断比較(🟡)

| サービス | 投稿 API | 認証 | 主な制約 |
|---|---|---|---|
| X | あり(v2 `POST /2/tweets`) | OAuth 2.0 PKCE / OAuth 1.0a / Bearer | ✅ **従量課金**。URL 付き投稿は $0.20。自動いいね・フォロー・引用は API 不可。返信は呼び出された場合のみ |
| Instagram | あり(Content Publishing) | Meta アプリ+アクセストークン | ✅ **JPEG のみ**、公開上限 100 または 50件/24時間(公式内で併記)、公開 URL の素材が必要 |
| Threads | あり | Meta アプリ | ✅ 250件/24時間、テキスト500字 |
| YouTube | あり(`videos.insert`) | OAuth 2.0 | **未監査プロジェクトは非公開に固定**、クォータ(→ ✅ 2026-11-03 確認: `videos.insert` は専用枠で100回/日。非公開制限は公式文書間で記述が不一致 [05](05-youtube-data-api.md)) |
| TikTok | あり(Content Posting API) | OAuth | 監査まで制限あり ⚪(→ ✅ 未監査は本人のみ閲覧・24時間5人まで、投稿はおおむね15件/日 [06](06-tiktok-api.md)) |
| Facebook ページ | あり(Graph API) | Meta アプリ | 権限審査(✅ 予約は10分後〜30日後 [07](07-other-apis.md)) |
| LINE | あり(Messaging API) | チャネルアクセストークン | メッセージ数の課金(✅ reply は通数に数えない [07](07-other-apis.md)) |
| Bluesky | あり(AT Protocol) | アプリパスワード/OAuth | 画像・動画の上限 |
| note | 公式の公開 API は未確認 | — | 非公式 API は規約確認 |

## 使う前の判断

1. **自動化が必要か**: 公式の予約機能(Meta Business Suite、YouTube Studio、各サービスの予約投稿)で足りるなら、API は不要。
2. **規約**: 自動化の規約と、アカウント凍結のリスクを確認([08-automation-and-tools](08-automation-and-tools.md))。
3. **コスト**: X の API は従量課金。投稿数・読み取り数で見積もる。
4. **セキュリティ**: 認証情報は**この public リポジトリに書かない**([01-concepts-and-security](01-concepts-and-security.md)、[13-secrets-management](13-secrets-management.md))。

## 関連ページ

- [beginners-guide](../00-meta/beginners-guide.md) — はじめての SNS 運用
- [40-pricing](../40-pricing/README.md) — 料金プラン
- [verification-queue](../00-meta/verification-queue.md) — 要検証リスト

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | X の料金 |
| https://developers.facebook.com/documentation/instagram-platform/content-publishing.md | 2026-11-03 | Instagram の公開 |
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | Threads の上限 |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | YouTube のクォータ |
| https://developers.tiktok.com/doc/content-sharing-guidelines | 2026-11-03 | TikTok の未監査の制限 |
| https://developers.line.biz/ja/docs/messaging-api/pricing/ | 2026-11-03 | LINE の通数 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | X・Instagram・Threads の公式文書を取得して更新(既存) |
| 2026-11-03 | 初心者向けに加筆(読む順番、用語、関連ページ、出典を追加)。新規ページ 00・12〜17 を追記。横断比較に YouTube・TikTok・Facebook・LINE の公式確認結果を併記(元の記述は残した) |
