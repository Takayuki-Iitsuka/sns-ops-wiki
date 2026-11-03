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
  - https://help.x.com/en/managing-your-account/how-to-customize-your-profile
  - https://docs.x.com/x-api/media/introduction.md
  - https://docs.x.com/x-api/media/quickstart/best-practices.md
  - https://docs.x.com/x-api/fundamentals/metrics.md
---

# X 画像・動画仕様

> **このページで分かること**: X に載せる画像・動画の形式・容量・比率と、失敗しない書き出し方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [02-posting](02-posting.md)

> 出典ページは **検索要約**のみ取得で、一部は約3年前の更新。公式で再確認してください (#7)。

## 概要

画像や動画は、仕様に合わないと **アップロードできない・一部が切れる・画質が落ちる** といった問題が起きます。このページでは次の順に整理します。

1. 通常ポストの画像(🟡 公式ヘルプの検索要約)
2. プロフィール画像・ヘッダー(🟡)
3. 動画(✅ 公式の開発者文書)
4. 実務のおすすめサイズ(⚪ 経験則)

数値の確度が違うのは、`help.x.com` が自動取得できず、`docs.x.com`(開発者向け)は取得できるためです。API の上限(✅)と、アプリで投稿するときの上限が同じとは限りません。

## 用語

| 用語 | 意味 |
|---|---|
| aspect ratio(アスペクト比、縦横比) | 横:縦の比率。16:9 は横長、1:1 は正方形、3:4 は縦長 |
| resolution(解像度) | 画像の縦横のピクセル数。例: 1600×900 |
| file size(容量) | ファイルの大きさ。MB(メガバイト)、GB(ギガバイト) |
| crop(トリミング) | 画像の一部を切り取って表示すること |
| codec(コーデック) | 動画・音声の圧縮方式。例: H.264、AAC |
| bitrate(ビットレート) | 1秒あたりのデータ量。高いほど高画質だが容量が増える |
| fps(frames per second、フレームレート) | 1秒あたりのコマ数 |

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
| ヘッダー画像 | 推奨 1500×500(下の「ヘッダー」節) | 🟡 |
| アニメーション GIF | プロフィール画像・ヘッダーには使えない | 🟡 |

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
| 推奨 | 1500×500(3:1)。左下にプロフィール画像が重なる | 🟡(help.x.com のプロフィール設定ページの検索要約でも 1500×500) |
| 容量 | 2MB または 5MB と資料により不一致 | 🟡 |

## API 経由の投稿

メディア上限と移行は [20-api/02-x-api](../20-api/02-x-api.md)(✅)。

## 書き出し

[export-presets](../01-common/export-presets.md)、比較は [image](../01-common/image-specs-comparison.md) / [video](../01-common/video-specs-comparison.md)。

## 手順: 画像を用意して投稿する

1. **目的を決める**: 1枚で見せるか、4枚で順に見せるか。
2. **比率を決める**: 迷ったら 16:9(1600×900)か 1:1(1200×1200)(⚪)。
3. **文字の大きさを確認**: スマホで縮小表示したときに読めるか、実機で確認する([mobile-viewing-optimization](../01-common/mobile-viewing-optimization.md))。
4. **書き出す**: JPEG(写真)か PNG(文字・図)。5MB 以下に収める(🟡)。
5. **個人情報を消す**: 写り込み・位置情報(Exif)を確認する([privacy](../01-common/privacy-and-personal-info.md))。
6. **投稿画面で確認**: プレビューで切れていないかを見る。
7. **ALT を付ける**([05-alt-text](05-alt-text.md))。

## 手順: 動画を用意して投稿する

1. 比率は 16:9(横)か 1:1、縦動画なら 9:16(1:3〜3:1 の範囲内 ✅)。
2. MP4、H.264 + AAC-LC で書き出す(✅)。
3. 30fps または 60fps にする(✅)。
4. 長さが **20分**(通常アカウント)を超えないか確認する(✅ API)。
5. 冒頭の数秒で内容が分かるようにする(⚪)。音なしで見る人向けに字幕を入れる(⚪)。
6. 投稿後、[08-analytics](08-analytics.md) で再生の到達率(25%・50%・75%・100%)を確認する(✅ API の指標)。

## 具体例

| 用途 | 設定例 | 確度 |
|---|---|---|
| 料理の完成写真 | 1200×1200、JPEG、品質80%程度 | ⚪ |
| 手順の図解4枚 | 4枚とも 1200×1500(4:5)に揃える。3:4 より縦長にしない | ⚪ |
| 店の告知画像 | 1600×900、PNG。文字は中央寄せ | ⚪ |
| 縦の短い動画 | 720×1280(9:16)、30fps、MP4 | ✅ 推奨解像度 |

## よくある失敗と対処

| 失敗 | 原因 | 対処 |
|---|---|---|
| 画像の上下が切れた | 3:4 より縦長、2:1 より横長(🟡) | 比率を範囲内にする |
| 文字がつぶれて読めない | 文字が小さい・画像が大きく圧縮された | 文字を大きくし、情報を減らす |
| 動画がアップロードできない | 形式・コーデック・長さが範囲外 | MP4/H.264/AAC-LC で書き出し直す |
| 4枚の並びがバラバラ | 比率が揃っていない | 同じ比率で書き出す |
| プロフィール画像の GIF が動かない | アニメーション GIF は非対応(🟡) | 静止画にする |
| 長い動画で 403 エラー | 通常アカウントの上限超え(✅) | 分割するか、契約を確認 |

## 注意点

- 他人が撮った写真・イラストの無断使用は削除や凍結の原因になります([image-sources-and-copyright](../01-common/image-sources-and-copyright.md))。
- 公式の数値は変わります。重要な制作物は、本番前にテスト投稿(非公開アカウントなど)で確認すると安全です。

## チェックリスト

- [ ] 比率が範囲内(画像は 2:1〜3:4、動画は 1:3〜3:1)
- [ ] 画像 5MB 以下 / GIF 15MB 以下
- [ ] スマホで文字が読める
- [ ] 個人情報・位置情報を消した
- [ ] ALT を付けた
- [ ] 動画は MP4・H.264・AAC-LC、60fps 以下

## 関連ページ / 次に読む

- [共通の画像比較](../01-common/image-specs-comparison.md)、[動画の基本](../01-common/video-basics.md)
- [画像制作の流れ](../01-common/image-production-workflow.md)、[画像チェックリスト](../../templates/image-checklist.md)
- 次に読む: [04-text-hashtags](04-text-hashtags.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://help.x.com/en/using-x/posting-gifs-and-pictures | 2026-11-03 | 検索要約のみ(🟡) |
| https://help.x.com/en/business-and-advertising/creative-ad-specifications | 2026-11-03 | 広告仕様。検索要約のみ(🟡) |
| https://help.x.com/en/managing-your-account/common-issues-when-uploading-profile-photo | 2026-11-03 | プロフィール画像。検索要約のみ(🟡) |
| https://help.x.com/en/managing-your-account/how-to-customize-your-profile | 2026-11-03 | ヘッダー 1500×500、GIF 非対応(🟡) |
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | メディア上限(✅ API) |
| https://docs.x.com/x-api/media/quickstart/best-practices.md | 2026-11-03 | 動画の推奨(✅ API) |
| https://docs.x.com/x-api/fundamentals/metrics.md | 2026-11-03 | 動画の再生指標(✅ API) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、画像・動画の準備手順、具体例、よくある失敗、チェックリスト、出典表)。プロフィール表のヘッダーを「未確認」から 🟡 1500×500 に更新(help.x.com の検索要約で確認) |
