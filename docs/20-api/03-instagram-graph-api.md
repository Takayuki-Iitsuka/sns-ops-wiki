---
title: Instagram Platform API(コンテンツ公開)
platform: instagram
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
---

# Instagram Platform API(コンテンツ公開)

> 2026年(皇紀2686年・令和8年)11月3日に Meta の公式開発者文書(Markdown 版)を直接取得して確認しました(✅)。API バージョンは **v26.0** が例に使われています。

## 1. できること / できないこと(✅)

| 項目 | 内容 |
|---|---|
| 公開できる種類 | 画像、動画、**リール**、**ストーリーズ**、**カルーセル**(最大20件の画像・動画の混在) |
| 前提アカウント | Instagram **プロフェッショナル**アカウント。Facebook ページ側で **Page Publishing Authorization(PPA)** が必要になる場合があり、未完了だと公開できない |
| 素材の置き場 | Meta が URL を cURL で取得するため、**公開サーバー上**にあること(リールの再開可能アップロードを除く) |
| 非対応 | **ショッピングタグ、フィルター** |
| リール | **カルーセルには入れられない** |
| カルーセルの切り抜き | **最初の画像の比率**に合わせて全体が切り抜かれる(既定 1:1) |
| 代替テキスト | **`alt_text` フィールド(2025年3月24日追加)**。画像投稿のみ。リールとストーリーズは非対応 |
| AI 生成の自己申告 | **`is_ai_generated=true`**(2025年以降)。カルーセルでは親コンテナにのみ指定(子に付けるとエラー) |
| 有料パートナーシップ表示 | `is_paid_partnership`、`branded_content_sponsor_ids`(最大2)。**Facebook ログイン経由のみ**。ブランドコンテンツ表示が可能 |
| コラボ | `collaborators`(最大3、フィード画像・リール・カルーセル。ストーリーズ不可) |
| トライアルリール | `trial_params`(非フォロワーにのみ共有し、後で通常のリールに昇格) |

## 2. 画像の仕様(✅ 公式リファレンス)

| 項目 | 値 |
|---|---|
| 形式 | **JPEG のみ**(MPO・JPS などの拡張 JPEG は不可) |
| 容量 | 最大 **8MB** |
| 比率 | **4:5 〜 1.91:1** |
| 幅 | 最小 **320px**(小さいと拡大)、最大 **1440px**(大きいと縮小) |
| 色空間 | sRGB(他は変換) |

## 3. リールの仕様(✅ 公式リファレンス)

| 項目 | 値 |
|---|---|
| コンテナ | MOV または MP4(編集リストなし、`moov` atom がファイル先頭) |
| 映像 | HEVC または H.264、progressive、closed GOP、4:2:0 |
| 音声 | AAC、サンプルレート最大 48kHz、モノラルまたはステレオ、128kbps |
| フレームレート | **23〜60 FPS** |
| 最大横幅 | 1920px |
| 比率 | 0.01:1 〜 10:1(**9:16 を推奨**) |
| ビットレート | VBR、映像 最大 **25Mbps** |
| 長さ | **3秒以上、最大15分** |
| 容量 | 最大 **300MB** |
| カバー | JPEG、最大 8MB、sRGB。`cover_url` または `thumb_offset`(ミリ秒)で指定 |

> 以前の資料にあった「リール 100MB」は、公式リファレンス上は **300MB**。

## 4. 文字数・タグ(✅)

| 項目 | 上限 |
|---|---|
| キャプション | **2,200字** |
| ハッシュタグ | **30個** |
| @メンション | **20個** |
| カルーセルの子要素への caption / user_tags | **非対応** |

## 5. 公開の流れ(✅)

1. `POST /{ig-id}/media` — コンテナ作成(`image_url` または `video_url`、`media_type` = `REELS` / `STORIES` / `VIDEO`、`caption`、`alt_text` など)。
2. カルーセル: 子コンテナに `is_carousel_item=true`、親に `media_type=CAROUSEL` と `children`(最大20)。
3. 動画: コンテナの `status_code` を確認(**1分に1回、5分まで**を推奨)。`FINISHED` になったら公開可。`EXPIRED` は24時間以内に公開しなかった場合。
4. `POST /{ig-id}/media_publish` — `creation_id` を渡して公開。
5. 大きな動画は `upload_type=resumable` で `rupload.facebook.com` にアップロード(Facebook ログイン経由)。

## 6. 公開の上限(✅ ただし公式文書内で不一致)

| 記載 | 値 |
|---|---|
| 「Rate Limit」の節 | **100件/24時間**(ローリング)。カルーセルは1件 |
| 「カルーセルの制限」の節 | **50件/24時間** |

→ **同じ公式ページ内で 100 と 50 が併記されている**。実際の残量は `GET /{ig-id}/content_publishing_limit` で確認する。安全側として **50件以内**で設計する(通常運用では十分)。(#37)

## 7. ログインの種類と権限(✅)

| 方式 | トークン | ホスト | 権限 |
|---|---|---|---|
| Instagram API with Unified Login | Business Integration System User トークン | `graph.facebook.com`・`rupload.facebook.com` | `instagram_basic`、`instagram_content_publish` |
| Instagram API with **Instagram Login** | Instagram ユーザートークン | `graph.instagram.com` | `instagram_business_basic`、`instagram_business_content_publish` |
| Instagram API with **Facebook Login** | Facebook ページトークン | `graph.facebook.com`・`rupload.facebook.com` | `instagram_basic`、`instagram_content_publish`、`pages_read_engagement`(+ ビジネス権限の場合 `ads_management`・`ads_read`) |

- アクセスレベルは Standard Access / Advanced Access(後者はアプリ審査)。
- **パートナーシップ表示を使うなら Facebook ログイン経由**。

## 8. 運用上の注意

1. 公式の予約機能(Meta Business Suite)で足りるなら API は不要。
2. 画像素材は**最初から JPEG・8MB 以内・幅1440px以内**で書き出す([export-presets](../01-common/export-presets.md))。PNG の図解は JPEG に変換する。
3. 自動投稿でも**広告・PR 表記**が必要。`is_paid_partnership` を使う([legal-compliance](../01-common/legal-compliance.md))。
4. **AI 生成画像は `is_ai_generated=true`**([ai-usage-policy](../01-common/ai-usage-policy.md))。
5. 公開 URL の素材は、公開処理が終わるまで消さない。

## 9. 公式で確認できなかった点(#37)

- 公開上限が 100 か 50 か(§6)。
- アプリ審査の具体的な要件と所要日数。
- Instagram の**インサイト取得 API** と、コメント管理 API の詳細(別ページ)。
