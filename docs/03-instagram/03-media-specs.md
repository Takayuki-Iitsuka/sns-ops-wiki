---
title: Instagram 画像・動画仕様
platform: instagram
topic: media
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://help.instagram.com/1631821640426723
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
---

# Instagram 画像・動画仕様

> **このページで分かること**: フィード写真・カルーセル・リール・ストーリーズ・プロフィール画像のサイズと比率、切れない画像の作り方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [image-specs-comparison](../01-common/image-specs-comparison.md)

## 概要

Instagram では、決められた**比率(縦横比)**の範囲外の画像は自動で切り抜かれます。初心者は次の3つを覚えておけば十分です(詳細は下の表)。

1. **フィードは 4:5(1080×1350)** の縦長が基本(1:1 も可)
2. **リール・ストーリーズは 9:16(1080×1920)**
3. 文字や顔は**中央**に置く(プロフィール一覧やボタンで端が隠れるため)

なお、**アプリで投稿する場合**と **API(外部ツール)で投稿する場合**で条件が違うことがあります。このページでは両者を分けて書いています。

## 用語

| 用語 | 意味 |
|---|---|
| aspect ratio(アスペクト比、縦横比) | 横:縦 の比。4:5 は縦長、1.91:1 は横長 |
| resolution(解像度) | 画像の縦横のピクセル数(例: 1080×1350) |
| sRGB(エスアールジービー) | Web で標準的な色の範囲。ほかの色空間は変換される |
| safe area(安全領域) | 切り抜きやボタンで隠れない中央部分 |
| FPS(フレームレート) | 1秒あたりのコマ数 |
| codec(コーデック) | 動画・音声の圧縮方式(H.264、HEVC、AAC など) |

## 手順 / 仕様

### フィード写真

| 項目 | 値 | 確度 |
|---|---|---|
| 幅 | 320〜1080px は元解像度を維持。**幅1080px以上のアップロードを推奨** | 🟡(公式ヘルプの検索要約) |
| 許容比率 | **1.91:1(横長)〜 4:5(縦長)**。範囲外は自動トリミング | 🟡(公式ヘルプの検索要約) |
| 3:4(1080×1440) | 2025年(皇紀2685年・令和7年)に追加されたとの二次情報あり。**未確認** | 🟡 #4 |
| 形式 | JPEG / PNG が一般的に挙げられる | ⚪ #9 |
| 容量 | 8MB〜30MB と資料により不一致 | ⚪ #9 |

### サイズ早見

| 用途 | サイズ | 比率 | 確度 |
|---|---|---|---|
| 正方形 | 1080×1080 | 1:1 | 🟡 |
| 縦長(推奨の1つ) | 1080×1350 | 4:5 | 🟡 |
| 横長 | 1080×566 | 1.91:1 | 🟡 |
| リール / ストーリーズ | 1080×1920 | 9:16 | ⚪(比率 9:16 推奨は API ✅) |
| プロフィール画像 | 320×320 以上、1:1 | 1:1 | ⚪ |

### カルーセル

- **最初の画像の比率に、全体が合わせて切り抜かれます**(API。既定は 1:1)✅([Content Publishing](https://developers.facebook.com/documentation/instagram-platform/content-publishing.md))。アプリでも同様とされます ⚪。
- そのため**全枚数を同じ比率**で作ります。
- 最大20件 ✅(API)。

### プロフィールのグリッド(一覧)の見え方

- 2025年1月、プロフィールのグリッドが正方形から**縦長の長方形**に変わったと報道されています 🟡([Engadget](https://www.engadget.com/social-media/instagram-swoops-in-with-3-minute-reels-and-rectangular-profile-grids-as-the-tiktok-ban-gets-real-201316339.html))。
- 投稿ごとに「プレビューを調整」(Fit / Fill)で一覧での見え方を変えられるとする報道があります 🟡。
- グリッドの正確な表示比率は公式未確認です(⚪)。**重要要素は中央**に置けば、どの比率で切られても読めます。

### リール・ストーリーズ・動画(🟡 二次資料。#18)

| 項目 | 値 | 確度 |
|---|---|---|
| リールの比率・解像度 | 9:16、1080×1920 | 🟡 |
| リールの長さ(アプリ) | 90秒・3分・15分・20分と資料により不一致(**アプリ内で確認**) | 🟡 |
| **リールの長さ・容量(API 公開)** | **3秒以上〜最大15分、300MB 以下**、23〜60FPS、MOV/MP4、H.264/HEVC、AAC | ✅ 公式リファレンス |
| リールの容量(アプリ) | 約4GB まで | 🟡 |
| ストーリーズ | 9:16、1080×1920。上下の安全領域を空ける | ⚪ |
| **ストーリーズ動画(API)** | **3秒以上〜最大60秒、100MB 以下**、23〜60FPS | ✅ 公式リファレンス |
| **ストーリーズ画像(API)** | JPEG、8MB 以下、sRGB、9:16 推奨 | ✅ 公式リファレンス |
| カバー | **JPEG、8MB 以下、sRGB**(API ✅)。9:16 推奨。プロフィールのグリッド表示の切り抜きに注意 | ✅/⚪ |

リールのカバーは、9:16 でない画像なら**中央の 9:16**、フィードに表示する場合は**中央の 1:1** が使われます ✅([IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md))。

### API 経由の公開

**画像は JPEG のみ・8MB・比率 4:5〜1.91:1・幅 320〜1440px** ✅。公開上限は公式ページ内で 100件/24時間と 50件/24時間が併記(カルーセルは1件)。素材は公開 URL に置く。詳細は [20-api/03-instagram-graph-api](../20-api/03-instagram-graph-api.md)。

- 幅 320px 未満は拡大、1440px 超は縮小されます ✅。
- sRGB 以外の色空間は sRGB に変換されます ✅。色が変わるのを防ぐには、最初から sRGB で書き出します。
- **PNG は API では使えません**。図解を PNG で作った場合は JPEG に変換します ✅。

### 切れない画像の作り方(手順)

1. 制作アプリで **1080×1350(4:5)** のキャンバスを作ります。
2. 上下左右の端から約10% を「余白」と決め、文字・顔・ロゴはその内側(中央約80%)に置きます(⚪ 経験則)。
3. 書き出しは JPEG(sRGB)にします。品質は高め(80〜90% 程度 ⚪)。
4. スマートフォンに送り、**実際の画面で拡大・縮小して**文字が読めるか確認します([mobile-viewing-optimization](../01-common/mobile-viewing-optimization.md))。

## 具体例

| 目的 | おすすめ | 理由(⚪) |
|---|---|---|
| 作品・商品写真 | 4:5 縦長 | 画面を大きく使える |
| 図解・手順のカルーセル | 4:5 で全枚数統一 | 1枚目に全体が合わせられるため |
| 横長の風景写真 | 1.91:1 または 4:5 に切り出し | 横長は表示が小さくなる |
| リール | 9:16、文字は中央 | 下部と右側はボタンで隠れる |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 1枚目を 1:1、2枚目を 4:5 で作り、2枚目が切れた | 全枚数を同じ比率に |
| 文字が端で切れた | 安全領域(中央80%)に収める |
| 外部ツールから PNG を投稿しようとしてエラー | API は JPEG のみ ✅。JPEG に変換 |
| 色がくすんだ | sRGB で書き出す |
| 解像度が低くぼやけた | 幅1080px 以上で書き出す |

## 注意点

- アプリの仕様(容量・長さ)は告知なく変わることがあり、公式本文を取得できていない項目が多いです(#4・#9・#18)。
- 写真の **Exif(撮影情報)** に位置情報が残っていないか確認します([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。

## 関連ページ / 次に読む

- [共通の画像比較](../01-common/image-specs-comparison.md)、[video-specs-comparison](../01-common/video-specs-comparison.md)
- [export-presets](../01-common/export-presets.md)、[image-production-workflow](../01-common/image-production-workflow.md)
- [12-reels](12-reels.md)、[13-stories-and-highlights](13-stories-and-highlights.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://help.instagram.com/1631821640426723 | 2026-11-03 | 🟡 フィード写真の幅・比率(検索要約) |
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | ✅ API の画像・リール・ストーリーズ・カバー仕様 |
| https://developers.facebook.com/documentation/instagram-platform/content-publishing.md | 2026-11-03 | ✅ カルーセルの切り抜き |
| https://www.engadget.com/social-media/instagram-swoops-in-with-3-minute-reels-and-rectangular-profile-grids-as-the-tiktok-ban-gets-real-201316339.html | 2026-11-03 | 🟡 グリッドの長方形化(報道) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(用語、ストーリーズの API 仕様 ✅、カバーの切り抜き ✅、グリッドの変更、切れない画像の作り方、具体例、よくある失敗)。既存の表と ✅ は維持 |
