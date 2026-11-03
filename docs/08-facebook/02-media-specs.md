---
title: Facebook 画像・動画仕様
platform: facebook
topic: media
last_verified: 2026-11-03
confidence: ⚪
---

# Facebook の画像・動画仕様

> **公式の仕様は未取得**です。以下は一般的に知られる設計値(⚪)。公式で確認 (#35)。

## 画像

| 用途 | 推奨 | 確度 |
|---|---|---|
| リンク共有(OGP) | 1200×630(約1.91:1) | ⚪ |
| 投稿画像(正方形/縦長) | 1080×1080 / 1080×1350 | ⚪ |
| プロフィール写真 | 正方形。円形に切り抜き | ⚪ |
| カバー写真 | 横長。端末で切り抜きが変わる。中央に主要要素 | ⚪ |
| 形式 | JPEG / PNG | ⚪ |

## 動画

| 用途 | 推奨 | 確度 |
|---|---|---|
| リール | 9:16、1080×1920 | ⚪ |
| 通常動画 | 16:9、1920×1080、H.264+AAC | ⚪ |
| 長さ・容量 | 未確認 | ⚪ |

## OGP(リンクプレビュー)

note の記事などを共有する際、画像タイトルが表示される。**note の見出し画像 1280×670**は約1.91:1で適合(🟡)。

比較: [image-specs-comparison](../01-common/image-specs-comparison.md) / [video-specs-comparison](../01-common/video-specs-comparison.md)。書き出し: [export-presets](../01-common/export-presets.md)。
