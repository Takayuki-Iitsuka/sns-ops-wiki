---
title: Instagram Graph API(コンテンツ公開)
platform: instagram
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/docs/instagram-platform/content-publishing
  - https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media
---

# Instagram Graph API(コンテンツ公開)

> 公式文書の検索要約に基づく 🟡 (#37)。API バージョンは v26.0 が参照されていた。

## できること / できないこと

| 項目 | 内容 | 確度 |
|---|---|---|
| 公開できる種類 | 画像、動画(リール)、カルーセル、ストーリーズ(条件あり ⚪) | 🟡/⚪ |
| 前提アカウント | プロフェッショナル(ビジネス/クリエイター)アカウント | ⚪ |
| 利用不可 | **ショッピングタグ、ブランドコンテンツタグ、フィルター** | 🟡 |
| リールをカルーセルに | 不可 | 🟡 |

## 画像の要件(🟡)

| 項目 | 値 |
|---|---|
| 形式 | **JPEG のみ**(MPO、JPS などの拡張形式は不可) |
| 容量 | 8MB |
| 色空間 | sRGB に変換される |
| 比率 | 4:5〜1.91:1 とする資料(公式の表は未確認) |
| 幅 | 320〜1440px とする資料(二次資料) |

→ 画像を API 投稿に回す予定なら、**最初から JPEG・8MB 以内**で作る([export-presets](../01-common/export-presets.md))。PNG の図解は JPEG に変換する。

## リール(動画)

| 項目 | 値 | 確度 |
|---|---|---|
| 指定 | `media_type=REELS`、`video_url` | 🟡 |
| ホスト | アップロードは `rupload.facebook.com`(他の呼び出しは `graph.facebook.com`) | 🟡 |
| 容量 | 300MB とする公式要約、100MB とする別の記述あり(**不一致**) | 🟡 |
| 比率 | 9:16 推奨 | 🟡 |
| カバー | JPEG、8MB 以下 | 🟡 |

## 公開の流れ(2段階)

1. `POST /{ig-user-id}/media` — コンテナ(下書き)を作成(`image_url` または `video_url` ほか)。
2. 動画の場合、コンテナの処理完了(`status_code`)を待つ。
3. `POST /{ig-user-id}/media_publish` — `creation_id` を渡して公開。

## 制約

| 項目 | 値 | 確度 |
|---|---|---|
| 公開上限 | **50件/24時間**(カルーセルは1件)。別資料の25件は古い可能性 | 🟡 |
| 残量確認 | `GET /{ig-user-id}/content_publishing_limit` | 🟡 |
| 素材の置き場 | **公開 URL**にホストされている必要がある(公開時点) | 🟡 |

## 権限と審査(⚪ 要確認)

- Meta アプリの作成、Instagram の API(Instagram ログイン経由か、Facebook ページ経由か)の選択。
- コンテンツ公開の権限(例: `instagram_business_content_publish` / `instagram_content_publish`)。
- 自分のアカウントだけを操作する場合の**開発モード**と、他人のアカウントを扱う場合の**アプリ審査・ビジネス認証**の違い。

## 運用上の注意

1. 公式の予約機能(Meta Business Suite)で足りるなら、API を使わない。
2. 画像・動画の公開 URL は、**公開後に削除/期限切れにしない**(処理が終わるまで)。
3. 自動投稿でも**広告・PR 表記**が必要([legal-compliance](../01-common/legal-compliance.md))。
