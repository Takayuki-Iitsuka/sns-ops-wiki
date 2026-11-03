---
title: API 活用ガイド(索引)
platform: common
topic: api
last_verified: 2026-11-03
confidence: 🟡
---

# API 活用ガイド

SNS の **API(Application Programming Interface、プログラムから操作する公式の窓口)** を使った、投稿の予約・自動化、分析データの取得、複数サービスへの同時配信の設計をまとめます。

> 公式の開発者文書(docs.x.com、developers.facebook.com、developers.google.com、developers.line.biz、atproto.com など)の**本文は取得できていません**。検索要約と二次資料に基づくため、価格・上限・エンドポイントは必ず公式で確認してください(#36〜#40)。

## ページ一覧

| ページ | 内容 |
|---|---|
| [01-concepts-and-security](01-concepts-and-security.md) | 認証、スコープ、トークン管理、レート制限、リトライ |
| [02-x-api](02-x-api.md) | **X API: v1.1 から v2 への移行**、料金、メディア投稿 |
| [03-instagram-graph-api](03-instagram-graph-api.md) | Instagram の公開 API |
| [04-threads-api](04-threads-api.md) | Threads の公開 API |
| [05-youtube-data-api](05-youtube-data-api.md) | YouTube Data API(アップロード、クォータ、監査) |
| [06-tiktok-api](06-tiktok-api.md) | TikTok の API |
| [07-other-apis](07-other-apis.md) | Facebook、LINE、Bluesky、Twitch、note |
| [08-automation-and-tools](08-automation-and-tools.md) | 自動化の方針・ツール・規約 |
| [09-architecture-patterns](09-architecture-patterns.md) | 投稿パイプラインの設計 |

## 横断比較(🟡)

| サービス | 投稿 API | 認証 | 主な制約 |
|---|---|---|---|
| X | あり(v2 `POST /2/tweets`) | OAuth 2.0 PKCE / OAuth 1.0a / Bearer | **従量課金(pay-per-use)**、メディアは別エンドポイント |
| Instagram | あり(Content Publishing) | Meta アプリ+アクセストークン | **JPEG のみ**、50件/24時間、公開 URL の素材が必要 |
| Threads | あり | Meta アプリ | 250件/24時間 |
| YouTube | あり(`videos.insert`) | OAuth 2.0 | **未監査プロジェクトは非公開に固定**、クォータ |
| TikTok | あり(Content Posting API) | OAuth | 監査まで制限あり ⚪ |
| Facebook ページ | あり(Graph API) | Meta アプリ | 権限審査 |
| LINE | あり(Messaging API) | チャネルアクセストークン | メッセージ数の課金 |
| Bluesky | あり(AT Protocol) | アプリパスワード/OAuth | 画像・動画の上限 |
| note | 公式の公開 API は未確認 | — | 非公式 API は規約確認 |

## 使う前の判断

1. **自動化が必要か**: 公式の予約機能(Meta Business Suite、YouTube Studio、各サービスの予約投稿)で足りるなら、API は不要。
2. **規約**: 自動化の規約と、アカウント凍結のリスクを確認([08-automation-and-tools](08-automation-and-tools.md))。
3. **コスト**: X の API は従量課金。投稿数・読み取り数で見積もる。
4. **セキュリティ**: 認証情報は**この public リポジトリに書かない**([01-concepts-and-security](01-concepts-and-security.md))。
