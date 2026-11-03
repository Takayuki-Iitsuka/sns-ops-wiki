---
title: Threads API
platform: threads
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/docs/threads/overview
---

# Threads API

> 公式概要の検索要約に基づく 🟡 (#34)。文字数・動画の仕様は Meta の公式リファレンスで確認。

## 上限(公式概要の要約)

| 項目 | 値 | 確度 |
|---|---|---|
| 投稿 | **250件/24時間**(ローリング)。カルーセルは1件。コンテナの公開時に判定 | 🟡 |
| 返信 | 1,000件/24時間 | 🟡 |
| 削除 | 100件/24時間 | 🟡 |
| 位置情報検索 | 500件/24時間 | 🟡 |
| 残量確認 | `threads_publishing_limit` エンドポイント | 🟡 |

## 公開の流れ(⚪ 2段階)

1. コンテナ作成(`POST /{user-id}/threads`)— テキスト、`image_url`/`video_url`、カルーセルの子要素。
2. 公開(`POST /{user-id}/threads_publish`)。動画は処理待ち。

## 主な権限(スコープ ⚪)

`threads_basic`、`threads_content_publish`、`threads_manage_replies`、`threads_read_replies`、`threads_manage_insights`。

## メディアの目安(🟡 二次資料)

| 項目 | 値 |
|---|---|
| 画像 | JPEG/PNG、JPEG 8MB・PNG 3MB。カルーセル 2〜20 |
| 動画 | 5分まで、MP4/MOV |
| 文字数 | 500字 |
| ハッシュタグ | 1つ |

## 運用

- Instagram と同様、公式の予約機能やサードパーティの導入で足りるなら API は不要。
- 返信管理(`threads_manage_replies`)で荒れ対策の自動化が可能だが、**誤判定のリスク**に注意。
- インサイトの取得で、週次レビューを自動化([analytics-kpi](../01-common/analytics-kpi.md))。
