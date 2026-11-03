---
title: Threads API
platform: threads
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
---

# Threads API

> 2026年(皇紀2686年・令和8年)11月3日に Meta の公式開発者文書(Markdown 版)を直接取得して確認しました(✅)。

## 1. 上限(✅ 公式の概要)

| 項目 | 値 |
|---|---|
| 投稿 | **250件/24時間**(ローリング)。**カルーセルは1件**。`threads_publish` の実行時に判定 |
| 返信 | **1,000件/24時間** |
| 削除 | **100件/24時間** |
| 位置情報検索 | **500件/24時間** |
| 残量確認 | `GET /{threads-user-id}/threads_publishing_limit`(`threads_basic` と `threads_content_publish` 権限が必要) |
| API 呼び出し全体の制限 | `4800 × インプレッション数`/24時間(最小インプレッション 10)。CPU 時間の制限もあり |

## 2. メディアの仕様(✅ 公式)

### 画像

| 項目 | 値 |
|---|---|
| 形式 | **JPEG・PNG**(公式にサポート) |
| 容量 | 最大 **8MB** |
| 比率 | 上限 **10:1** |
| 幅 | 最小 320px(拡大)、最大 1440px(縮小) |
| 色空間 | sRGB |

### 動画

| 項目 | 値 |
|---|---|
| コンテナ | MOV または MP4(編集リストなし、`moov` atom が先頭) |
| 映像 | HEVC または H.264、progressive、closed GOP、4:2:0 |
| 音声 | AAC、48kHz 以下、モノラル/ステレオ、128kbps |
| フレームレート | **23〜60 FPS** |
| 最大横幅 | 1920px |
| 比率 | 0.01:1 〜 10:1(**9:16 を推奨**) |
| ビットレート | VBR、映像 最大 **100Mbps** |
| 長さ | **最大5分(300秒)**、0秒超 |
| 容量 | 最大 **1GB** |

### その他

| 項目 | 値 |
|---|---|
| **テキスト投稿** | **500字まで** |
| カルーセル | **2〜20件** |

> 以前、二次資料にあった「PNG 3MB」「動画 500MB」は、公式の概要には**記載がなく**、公式値は上記。個別エンドポイントのリファレンスに追加の制限がある可能性あり(#34)。

## 3. 公開の流れ(⚪ 公式の入門ページ未取得)

1. `POST /{threads-user-id}/threads` — コンテナ作成(テキスト、`image_url`/`video_url`、カルーセルの子要素)。
2. `POST /{threads-user-id}/threads_publish` — 公開。動画は処理待ち。

## 4. 主な権限(⚪)

`threads_basic`、`threads_content_publish`、`threads_manage_replies`、`threads_read_replies`、`threads_manage_insights`。

## 5. 運用

- 公式の予約機能やサードパーティで足りるなら API は不要。
- 返信管理で荒れ対策の自動化が可能だが、**誤判定のリスク**に注意。
- インサイトの取得で週次レビューを自動化([analytics-kpi](../01-common/analytics-kpi.md))。

## 6. 公式で確認できなかった点(#34)

- ハッシュタグ(トピックタグ)の個数の上限(二次資料は1つ)。
- 公開の流れの詳細(上記 ⚪)。
- 収益化プログラムの有無。
