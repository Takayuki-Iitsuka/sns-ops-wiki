---
title: X 画像・動画仕様
platform: x
topic: media
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://help.x.com/en/using-x/posting-gifs-and-pictures
  - https://help.x.com/en/business-and-advertising/creative-ad-specifications
  - https://help.x.com/en/managing-your-account/common-issues-when-uploading-profile-photo
---

# X 画像・動画仕様

> 出典ページは **検索要約**のみ取得で、一部は約3年前の更新。公式で再確認してください (#7)。

## 通常ポスト

| 項目 | 値 | 確度 |
|---|---|---|
| 形式 | JPEG, PNG, GIF(BMP, TIFF は不可) | 🟡 |
| 写真容量 | 最大5MB | 🟡 |
| GIF 容量 | 5MB(モバイル) / 15MB(Web) | 🟡 |
| 枚数 | 最大4枚。GIF と複数画像は併用不可 | 🟡 |
| 単一画像の比率 | 2:1〜3:4 は全体表示、それ以外はトリミング | 🟡 |

## プロフィール

| 項目 | 値 | 確度 |
|---|---|---|
| プロフィール画像 | 推奨 400×400px、最大2MB、JPEG/PNG/GIF | 🟡 |
| ヘッダー画像 | 未確認(→ 要検証) | ⚪ |

## 広告(参考)

| 項目 | 値 | 確度 |
|---|---|---|
| 画像容量 | 5MB、GIF 15MB | 🟡 |
| 推奨比率 | 1:1(1080×1080)、16:9(1920×1080) | 🟡 |

## 実務のおすすめ（⚪）

| 目的 | サイズ例 |
|---|---|
| 1枚で見せる | 1600×900(16:9) または 1200×1200(1:1) |
| 縦長を見せたい | 3:4 以内に収める(1200×1600)。上下のトリミングに注意 |
| 4枚並べ | 各画像は同じ比率で揃える |

## Media Studio

別ツール上の仕様(JPG/PNG 20MB と報告)はあるが、通常ポストと別の可能性あり。🟡 未確認。

## 関連

[共通の画像比較](../01-common/image-specs-comparison.md)

## 動画(✅ docs.x.com の公式文書。API の仕様)

| 項目 | 値 |
|---|---|
| 形式 | MP4 / MOV。H.264 High Profile + AAC-LC |
| **長さ・容量(Post)** | **通常アカウント 20分・8GB / Premium・認証済み 125分・16GB**(0.5秒以上) |
| 長さ・容量(DM) | 通常 140秒・512MB / Premium 10分・1GB |
| 比率 | **1:3〜3:1**(推奨は 16:9 か 1:1)、ピクセル比 1:1 |
| 解像度 | 推奨 1280×720(横)/ 720×1280(縦)/ 720×720。**Premium は 1080p** をアップロード・再生可。範囲 32×32〜1280×1024 |
| フレームレート | 30 または 60fps(60fps 以下) |
| ビットレート | 映像 最低 5,000kbps、音声 最低 128kbps |
| 画像 | JPG・PNG・GIF・**WEBP**、5MB 以下。GIF は 15MB 以下 |
| 添付数 | 写真4枚、または GIF 1つ、または動画 1つ |

- 制限は**投稿するユーザーの Premium/認証済みの有無**で決まり、API プランでは決まらない。超えると投稿時に 403。
- アプリ(Web・モバイル)で投稿する場合の上限は、同じとは限らない(アプリでの長さ・容量の公式ページは未取得 #18)。
- 詳細は [20-api/02-x-api](../20-api/02-x-api.md)。

## ヘッダー

| 項目 | 値 | 確度 |
|---|---|---|
| 推奨 | 1500×500(3:1)。左下にプロフィール画像が重なる | 🟡 |
| 容量 | 2MB または 5MB と資料により不一致 | 🟡 |

## API 経由の投稿

メディア上限と移行は [20-api/02-x-api](../20-api/02-x-api.md)(✅)。

## 書き出し

[export-presets](../01-common/export-presets.md)、比較は [image](../01-common/image-specs-comparison.md) / [video](../01-common/video-specs-comparison.md)。

