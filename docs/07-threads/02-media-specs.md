---
title: Threads 画像・動画・文字数
platform: threads
topic: media
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md
  - https://developers.facebook.com/documentation/threads/reference/publishing.md
---

# Threads の画像・動画・文字数

> **このページで分かること**: Threads に載せる画像・動画の形式・容量・比率、文字数やリンクの上限、書き出しの手順。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [01-setup-and-posting](01-setup-and-posting.md)

> Meta の公式開発者文書(Threads API の概要)を 2026年(皇紀2686年・令和8年)11月3日に直接取得して確認しました(✅)。アプリの UI から投稿する場合の上限は、API の上限と異なる可能性があります。

## 概要

Threads の画像・動画の仕様は、Meta の開発者文書で公開されています(✅)。この数値を守って書き出せば、API でもアプリでも失敗しにくくなります。

初心者がまず覚えるのは次の3つです。

1. 画像は **JPEG か PNG、8MB まで**
2. 動画は **MP4(または MOV)、5分・1GB まで**、縦の **9:16 が推奨**
3. 本文は **500字まで**

## 用語

| 用語 | 意味 |
|---|---|
| aspect ratio(アスペクト比) | 横:縦の比率。9:16 は縦長、4:5 はやや縦長 |
| sRGB(エスアールジービー) | 標準的な色の範囲。Web 用の画像はこれで書き出す |
| codec(コーデック) | 動画・音声の圧縮方式。H.264、HEVC、AAC など |
| VBR(Variable Bit Rate、可変ビットレート) | 場面に応じてデータ量を変える方式 |
| progressive / closed GOP | 動画の記録方式。一般的な書き出し設定の既定値で満たされることが多い(⚪) |
| carousel(カルーセル) | 複数の画像・動画をまとめた投稿 |

## 文字数・構成

| 項目 | 値 | 確度 |
|---|---|---|
| テキスト投稿 | **500字まで** | ✅ |
| カルーセル | **2〜20件** | ✅ |
| ハッシュタグ(トピック) | 1つとする二次資料あり。公式の本文では未確認 | 🟡 |
| トピックタグ(API の文書) | **1投稿に1つ**、**1〜50字**。ピリオド(.)とアンパサンド(&)は使えない | ✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md) |
| テキスト添付(長文) | **10,000字まで**。テキストのみの投稿に限る | ✅ [Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md) |
| リンク | **1投稿5つまで**(2025年(皇紀2685年・令和7年)12月22日から、超えると API で投稿エラー) | ✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md) |
| リンクのプレビュー | テキストのみの投稿で、最初の URL がプレビューカードになる | ✅ 同上 |
| 絵文字の数え方(API) | UTF-8 のバイト数で数える | ✅ 同上 |
| 代替テキスト | **1,000字まで** | ✅ [Publishing reference](https://developers.facebook.com/documentation/threads/reference/publishing.md) |

> 上の「ハッシュタグ(トピック)1つとする二次資料」の行は、開発者文書で「1投稿に1つ」と確認できたため、その下の行(✅)が最新です。アプリで同じ制限かは 🟡 のままです。

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

## 手順: 画像を書き出す

1. 比率を決める。迷ったら 4:5(1080×1350)(⚪)。
2. 幅は 1440px 以下にする(それより大きいと縮小される ✅)。
3. 形式は写真なら JPEG、文字や図なら PNG。
4. 色空間を sRGB にする(✅)。
5. 8MB 以下か確認する(✅)。
6. 写り込み・位置情報(Exif)を消す([privacy](../01-common/privacy-and-personal-info.md))。

## 手順: 動画を書き出す

1. 縦 9:16(例 1080×1920)で作る(✅ 推奨比率。横幅は 1920px 以下)。
2. MP4、H.264、AAC で書き出す(✅)。
3. フレームレートは 30fps など 23〜60 の範囲にする(✅)。
4. 5分以内・1GB 以下か確認する(✅)。
5. 音なしでも分かるよう字幕を入れる(⚪ [video-basics](../01-common/video-basics.md))。

## 具体例

| 用途 | 設定例 | 確度 |
|---|---|---|
| 料理の写真1枚 | 1080×1350、JPEG、sRGB | ⚪(範囲は ✅) |
| 作り方の手順を5枚で | 5枚とも 1080×1350 に揃えたカルーセル | ⚪(2〜20件は ✅) |
| 制作過程の短い動画 | 1080×1920、30fps、MP4(H.264 + AAC)、60秒 | ⚪(範囲は ✅) |

## よくある失敗と対処

| 失敗 | 原因 | 対処 |
|---|---|---|
| 画像がぼやけた | 幅 320px 未満で拡大された(✅) | 元画像を大きくする |
| 動画が投稿できない | 5分超・1GB 超・形式違い | 分割、または書き出し直す |
| リンクをたくさん貼ったら投稿できない | 5つ超(✅) | リンクを5つ以内にする |
| カルーセルが作れない | 1件だけ | カルーセルは2件以上(✅) |
| 色がくすんだ | sRGB 以外で書き出した | sRGB で書き出し直す |

## 注意点

- 数値は API の公式文書(✅)です。アプリで投稿するときの上限は異なる可能性があります(#18)。
- 他人の写真・音楽を使うときは権利を確認してください([image-sources-and-copyright](../01-common/image-sources-and-copyright.md)、[music-and-licensing](../01-common/music-and-licensing.md))。

## チェックリスト

- [ ] 画像は JPEG/PNG、8MB 以下、幅 1440px 以下、sRGB
- [ ] 動画は MP4/MOV、5分以内、1GB 以下、9:16 推奨
- [ ] 本文は500字以内、リンクは5つ以内
- [ ] カルーセルは2〜20件
- [ ] 代替テキストを付けた([03-text-hashtags-alt](03-text-hashtags-alt.md))

## 関連ページ / 次に読む

- 次に読む: [03-text-hashtags-alt](03-text-hashtags-alt.md)
- [image-specs-comparison](../01-common/image-specs-comparison.md)、[video-specs-comparison](../01-common/video-specs-comparison.md)、[export-presets](../01-common/export-presets.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | 画像・動画・文字数・上限(✅) |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | トピックタグ・リンク・絵文字の数え方(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md | 2026-11-03 | テキスト添付10,000字(✅) |
| https://developers.facebook.com/documentation/threads/reference/publishing.md | 2026-11-03 | 代替テキスト1,000字(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、書き出し手順、具体例、よくある失敗、チェックリスト、出典表)。トピックタグ「1投稿に1つ・1〜50字」、リンク5つ、テキスト添付10,000字、代替テキスト1,000字を ✅ で追加(開発者文書で確認) |
