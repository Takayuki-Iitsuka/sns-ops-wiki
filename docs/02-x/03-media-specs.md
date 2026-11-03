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

## 動画(🟡 二次資料と docs.x.com の検索要約。#18)

| 項目 | 値 | 確度 |
|---|---|---|
| 形式 | MP4 / MOV(H.264 映像+AAC 音声が一般的) | 🟡 |
| 長さ | 通常アカウント 約2分20秒。Premium は拡張(時間・容量は資料により不一致) | 🟡 |
| 容量 | 通常 512MB(API では `amplify_video` で 512MB) | 🟡 |
| 比率 | 1:3〜3:1(1:1、9:16、16:9 を含む) | 🟡 |
| 推奨解像度 | 1280×720(横)/ 720×1280(縦)/ 720×720(正方形)。1920×1080 まで可とする資料 | 🟡 |
| フレームレート | 60fps 以下(30 または 60) | 🟡 |
| ビットレート目安 | 5〜8Mbps(⚪ 設計値) | ⚪ |

## ヘッダー

| 項目 | 値 | 確度 |
|---|---|---|
| 推奨 | 1500×500(3:1)。左下にプロフィール画像が重なる | 🟡 |
| 容量 | 2MB または 5MB と資料により不一致 | 🟡 |

## API 経由の投稿

画像 5MB・GIF 15MB・動画 512MB(公式文書の要約)。詳細と移行は [20-api/02-x-api](../20-api/02-x-api.md)。

## 書き出し

[export-presets](../01-common/export-presets.md)、比較は [image](../01-common/image-specs-comparison.md) / [video](../01-common/video-specs-comparison.md)。

