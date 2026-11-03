---
title: Threads 画像・動画・文字数
platform: threads
topic: media
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
---

# Threads の画像・動画・文字数

> Meta の公式開発者文書(Threads API の概要)を 2026年(皇紀2686年・令和8年)11月3日に直接取得して確認しました(✅)。アプリの UI から投稿する場合の上限は、API の上限と異なる可能性があります。

## 文字数・構成

| 項目 | 値 | 確度 |
|---|---|---|
| テキスト投稿 | **500字まで** | ✅ |
| カルーセル | **2〜20件** | ✅ |
| ハッシュタグ(トピック) | 1つとする二次資料あり。公式の本文では未確認 | 🟡 |

## 画像(✅)

| 項目 | 値 |
|---|---|
| 形式 | **JPEG・PNG** |
| 容量 | 最大 **8MB** |
| 比率 | 上限 **10:1** |
| 幅 | 最小 320px(拡大)、最大 1440px(縮小) |
| 色空間 | sRGB |
| 推奨サイズ(設計値) | 1080×1350(4:5) ⚪ |

## 動画(✅)

| 項目 | 値 |
|---|---|
| コンテナ | MOV または MP4 |
| 映像 | HEVC または H.264、progressive、closed GOP、4:2:0 |
| 音声 | AAC、48kHz 以下、モノラル/ステレオ、128kbps |
| フレームレート | 23〜60 FPS |
| 最大横幅 | 1920px |
| 比率 | 0.01:1 〜 10:1(**9:16 推奨**) |
| ビットレート | VBR、映像 最大 100Mbps |
| 長さ | **最大5分**、0秒超 |
| 容量 | 最大 **1GB** |

## API での公開上限(✅)

| 項目 | 値 |
|---|---|
| 投稿 | 250件/24時間(カルーセルは1件) |
| 返信 | 1,000件/24時間 |
| 削除 | 100件/24時間 |
| 位置情報検索 | 500件/24時間 |

詳細: [20-api/04-threads-api](../20-api/04-threads-api.md)。比較: [image](../01-common/image-specs-comparison.md) / [video](../01-common/video-specs-comparison.md)。書き出し: [export-presets](../01-common/export-presets.md)。
