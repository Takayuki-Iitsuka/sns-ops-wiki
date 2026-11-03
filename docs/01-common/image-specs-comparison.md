---
title: 画像仕様の横断比較
platform: common
topic: media
last_verified: 2026-11-03
confidence: 🟡
sources:
  - ../00-meta/sources.md
  - https://docs.x.com/x-api/media/introduction.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://support.google.com/youtube/answer/72431
  - https://support.google.com/youtube/answer/10456525?hl=ja
  - https://developers.line.biz/ja/docs/messaging-api/using-rich-menus/
---

# 画像仕様の横断比較

> **このページで分かること**: 主要サービスの画像の形式・容量・枚数・比率の上限と、プロフィール・ヘッダー画像のサイズを一覧で比べる。
>
> **対象**: 初心者〜中級者  **先に読むページ**: なし。すぐ使える書き出し値だけ知りたい場合は [export-presets](export-presets.md)

> 確度ラベル: ✅ 公式の本文を直接確認 / 🟡 検索要約・二次資料 / ⚪ 一般知識。一致しない資料は両論併記し、[要検証リスト](../00-meta/verification-queue.md) に載せています。動画は [video-specs-comparison](video-specs-comparison.md)、そのまま使える書き出し値は [export-presets](export-presets.md)。

## 概要

同じ画像でも、サービスによって**受け付ける形式・容量・比率**が違います。範囲外の画像は、アップロードできない・自動で切り抜かれる・強く圧縮される、といったことが起きます。

このページは「**上限(どこまで受け付けるか)**」の一覧です。「何 px で作ればよいか」の推奨値は [export-presets](export-presets.md) にまとめています。

### 表の読み方

- **(API)** と書いた行は、開発者向けの公式文書(予約投稿ツールなどが使う仕組み)の値です。✅ が多いのはこのためです。
- **(アプリ)** の行は、スマホアプリやブラウザから投稿するときの値です。公式ヘルプの本文を取得できないものが多く、🟡 / ⚪ が残っています。
- アプリと API で値が違うことがあります。迷ったら**両方の範囲に収まる値**で作ると安全です。

## 用語

| 用語 | 意味 |
|---|---|
| format(形式) | JPEG・PNG・GIF・WEBP などファイルの種類 |
| file size(容量) | ファイルの大きさ。MB(メガバイト)・KB(キロバイト) |
| resolution(解像度) | 横×縦のピクセル数 |
| aspect ratio(アスペクト比、縦横比) | 横:縦。1.91:1 は横長、4:5 は縦長 |
| carousel(カルーセル) | 1投稿に複数枚の画像を入れて横にめくる形式 |
| crop(トリミング、切り抜き) | 画像の一部を切り取ること。範囲外の比率は自動で切られる |
| sRGB | Web 表示の標準の色空間 |
| API(エーピーアイ) | アプリ同士がデータをやり取りする仕組み。予約投稿ツールなどが使う |

## 1. 投稿画像

| サービス | 形式 | 容量上限 | 枚数 | 比率・表示 | 確度・備考 |
|---|---|---|---|---|---|
| X(API) | **JPG・PNG・GIF・WEBP** | 画像 **5MB**、GIF **15MB**(解像度 1280×1080 以下・350フレーム以下が目安) | 写真 **4枚**、または GIF 1つ、または動画 1つ | — | ✅ docs.x.com |
| X(アプリ) | JPEG / PNG / GIF | 写真 5MB、GIF 5MB(モバイル)/ 15MB(Web) | 最大4枚 | 単一画像は 2:1〜3:4 が全体表示、範囲外はトリミング | 🟡 古い公式ページの要約 |
| Instagram(フィード、アプリ) | JPEG / PNG が一般的 | 資料により 8〜30MB と不一致 | カルーセル 最大20 | 1.91:1〜4:5(幅 320〜1080px は元解像度維持)。3:4 追加の報道あり(未確認) | 🟡 |
| Instagram(API 公開) | **JPEG のみ** | **8MB** | カルーセル 最大20(全体が1枚目の比率に切り抜かれる、既定 1:1) | **4:5 〜 1.91:1**、幅 **320〜1440px**、sRGB | ✅ 公式リファレンス |
| Threads(API) | **JPEG・PNG** | **8MB** | カルーセル **2〜20** | 比率上限 **10:1**、幅 320〜1440px、sRGB | ✅ 公式 |
| note | 画像(形式は未確認) | 1枚 最大 **10MB** | — | 見出し **1280×670**(約1.91:1)。異なる比率はトリミング | 🟡 公式ヘルプの要約 |
| YouTube(サムネイル) | JPG・PNG など | **モバイル: 動画 2MB(ポッドキャスト 10MB)/ パソコン: 50MB** | — | **動画 16:9、ショート 9:16**、ポッドキャスト 1:1。推奨解像度 動画 3840×2160、ショート 2160×3840、最小幅 640px | ✅ YouTube ヘルプ |
| Bluesky | JPEG / PNG ほか | 1MB(従来)/ 2MB(新)と不一致 | 最大4枚 | — | 🟡 |
| Facebook | JPEG / PNG | 未確認 | — | リンクプレビューは約1.91:1(1200×630)が一般的 | ⚪ |
| LINE(リッチメニュー) | JPEG / PNG | 未確認 | — | **2500×1686** または **2500×843** | ✅ LINE 開発者文書のサンプル(容量は未確認) |
| KDP(電子書籍の表紙) | JPEG / TIFF | 未確認 | — | 縦横比 1.6:1(2560×1600 相当)が一般的 | ⚪ |

## 2. プロフィール・ヘッダー・カバー

| サービス | 項目 | 推奨 | 確度 |
|---|---|---|---|
| X | プロフィール画像 | 400×400、2MB 以下、JPEG/PNG/GIF | 🟡 |
| X | ヘッダー | 1500×500(3:1)。左下にプロフィール画像が重なる | 🟡 |
| Instagram | プロフィール画像 | 正方形。円形に切り抜かれる | ⚪ |
| note | クリエイターページ/マガジンヘッダー | 比率 1.91:1(1280×670 を用意) | 🟡 |
| YouTube | プロフィール | 800×800(円形表示)🟡。公式: **98×98px で表示**できる画像、JPG・GIF・BMP・PNG(アニメーション GIF 不可)、**15MB 以下** ✅ | 🟡 / ✅ |
| YouTube | チャンネルバナー | 2560×1440 で書き出し(公式の推奨 ✅)。**最小 2048×1152**、文字・ロゴの**安全領域は中央 1235×338**、**6MB 以下** ✅。旧記載の安全領域 1546×423 は古い資料の値(🟡) | ✅ |
| Threads / Facebook / TikTok | プロフィール | 正方形。円形切り抜きに備え中央配置 | ⚪ |

## 3. 比率の早見表

| 比率 | 1080px 幅での高さ | 向き | 主な使い所 |
|---|---|---|---|
| 3:1 | 360 | 横長 | X ヘッダー |
| 1.91:1 | 566 | 横長 | note 見出し、リンクカード、Instagram 横長 |
| 16:9 | 608 | 横長 | YouTube サムネイル、動画 |
| 3:2 | 720 | 横長 | 写真 |
| 1:1 | 1080 | 正方形 | 汎用 |
| 4:5 | 1350 | 縦長 | Instagram・Threads のフィード、YouTube 縦長動画の自動サムネイル |
| 3:4 | 1440 | 縦長 | X の縦長上限付近。Instagram は未確認 |
| 9:16 | 1920 | 縦長 | リール、ショート、ストーリーズ、縦型動画、YouTube ショートのサムネイル |

> 高さの計算: 高さ = 幅 ÷ 横の数 × 縦の数。例: 4:5 で幅 1080 なら 1080 ÷ 4 × 5 = 1350。

## 4. 共通の実務ルール(⚪ 経験則)

1. **マスターは大きく**: 長辺 2000px 以上で作り、各サービス向けに書き出す。
2. **安全領域**: 重要な要素は中央 80% に。自動トリミングやUIの重なりに備える。
3. **形式**: 写真は JPEG、図・文字入りは PNG。**Instagram の API 公開を使う予定なら最初から JPEG**(公式は JPEG のみ)。
4. **色空間**: sRGB で書き出す(Instagram・Threads の API は他の色空間を sRGB に変換する ✅)。
5. **容量**: 上限の**半分程度**に収める。
6. **文字**: スマホの縮小表示で読める大きさ。画像内の文字は alt text と本文にも書く([alt-text](alt-text.md))。
7. **Exif**: 公開前に位置情報を削除([image-production-workflow](image-production-workflow.md))。
8. **ファイル名**: `YYYYMMDD_媒体_用途_連番.拡張子`。

## 具体例: 1枚の画像を複数サービスに出す

| やりたいこと | 安全な作り方(⚪) |
|---|---|
| X と Instagram に同じ縦長画像 | 1080×1350(4:5)。X の 3:4 の範囲内、Instagram の範囲内 |
| Instagram の予約投稿ツールでカルーセル | 全枚 JPEG・同じ比率(1枚目の比率に切られるため ✅) |
| note の見出しと X のリンクカード | 1280×670(約1.91:1)で、文字は中央に |

## よくある失敗と対処

| 失敗 | 起きること | 対処 |
|---|---|---|
| カルーセルに縦長と横長を混ぜた | 1枚目の比率に切り抜かれる(Instagram API ✅) | 全枚を同じ比率に |
| PNG で予約投稿ツールから Instagram へ | 公開できない(API は JPEG のみ ✅) | JPEG で書き出す |
| 9:16 の画像を Instagram フィードに | 4:5 に切られて上下が欠ける | フィード用は 4:5 で別に作る |
| YouTube バナーの端に文字 | テレビ・スマホで切れる | 中央 1235×338 に収める(✅) |
| プロフィール画像の四隅に文字 | 円形で欠ける | 中央の円の中に |

## チェックリスト

- [ ] 投稿先の形式(JPEG/PNG)・容量・比率の範囲内
- [ ] アプリと API の両方に収まる値にした(予約投稿ツールを使う場合)
- [ ] カルーセルは全枚同じ比率
- [ ] プロフィール・バナーの文字は安全領域の中
- [ ] 画像内の文字を alt text と本文にも書いた

## 5. 未確認事項

[verification-queue](../00-meta/verification-queue.md) の #4, #7, #9, #12, #17, #31〜#35, #39〜#41 を参照。

## 関連ページ / 次に読む

- [export-presets](export-presets.md)(推奨の書き出し値)
- [video-specs-comparison](video-specs-comparison.md)(動画)
- [mobile-viewing-optimization](mobile-viewing-optimization.md)(スマホでの見え方)
- サービス別: [X](../02-x/03-media-specs.md) / [Instagram](../03-instagram/03-media-specs.md) / [note](../04-note/03-media-specs.md) / [YouTube](../05-youtube/02-media-specs.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| ../00-meta/sources.md | 2026-11-03 | 出典一覧(既存) |
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | X API の画像・GIF の上限 |
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | Instagram API の画像仕様 |
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | Threads API の画像仕様 |
| https://support.google.com/youtube/answer/72431 | 2026-11-03 | YouTube のサムネイル |
| https://support.google.com/youtube/answer/10456525?hl=ja | 2026-11-03 | YouTube のバナー・プロフィール写真(今回本文を確認) |
| https://developers.line.biz/ja/docs/messaging-api/using-rich-menus/ | 2026-11-03 | LINE のリッチメニュー |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成 |
| 2026-11-03 | 初心者向けに加筆(概要、表の読み方、用語、比率の計算、具体例、よくある失敗、チェックリスト、関連ページ、出典)。**YouTube のバナー(最小 2048×1152、安全領域 1235×338、6MB)とプロフィール写真(98×98 表示、15MB)を公式で確認し ✅ を追加**。安全領域の旧値 1546×423(🟡)は古い資料の値として注記 |
