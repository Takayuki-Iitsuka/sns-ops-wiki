---
title: 動画仕様の横断比較
platform: common
topic: media
last_verified: 2026-11-03
confidence: 🟡
sources:
  - ../00-meta/sources.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://docs.x.com/x-api/media/introduction.md
  - https://support.google.com/youtube/answer/10059070
  - https://support.google.com/youtube/answer/1722171
  - https://support.google.com/youtube/answer/72431
---

# 動画仕様の横断比較

> **このページで分かること**: 主要サービスの動画の形式・比率・長さ・容量・サムネイルの仕様を一覧で比べる。作り方の考え方は [video-basics](video-basics.md)。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [video-basics](video-basics.md)

## 概要

動画の仕様(長さ・容量・比率)はサービスごとに違い、**アプリから投稿する場合と API(プログラム)から投稿する場合でも違う**ことがあります。このページは、公式資料で確認できた値(✅)と、二次資料の値(🟡)を分けて並べています。

初心者は、まず次の3点だけ押さえれば十分です。

1. 縦型は **9:16・1080×1920**、横型は **16:9・1920×1080** を基準にする。
2. 形式は **MP4(H.264 + AAC)** にしておけば、ほとんどのサービスで受け付けられる。
3. 長さ・容量の上限は変わりやすいので、**投稿前にアプリ内で確認**する。

## 用語

| 用語 | 意味 |
|---|---|
| MP4 / MOV | 動画ファイルの入れ物(コンテナ)の形式 |
| codec(コーデック) | 映像・音声を圧縮する方式。H.264・HEVC(H.265)・AAC など |
| bitrate(ビットレート) | 1秒あたりのデータ量。大きいほど高画質で容量も大きい(Mbps) |
| FPS / frame rate(フレームレート) | 1秒あたりのコマ数 |
| VBR / CBR | 可変ビットレート / 固定ビットレート |
| API | プログラムから投稿する窓口。アプリとは上限が異なる場合がある |
| `moov` atom | MP4 の目次情報。先頭にあると読み込みが速い(faststart) |
| closed GOP / progressive | 圧縮の区切りが独立していること / インターレースでない(順次走査)映像 |

> 確度ラベル: ✅ 公式の本文を直接確認 / 🟡 検索要約・二次資料 / ⚪ 一般知識。資料間で食い違う値は併記し、[要検証リスト](../00-meta/verification-queue.md) に載せています。書き出し値は [export-presets](export-presets.md)、制作の考え方は [video-basics](video-basics.md)。

## 1. 縦型・短尺動画

| サービス | 形式 | 比率・解像度 | 長さ | 容量 | 確度・備考 |
|---|---|---|---|---|---|
| **Instagram リール(API)** | MOV / MP4(H.264 または HEVC + AAC) | 比率 0.01:1〜10:1(**9:16 推奨**)、最大横幅 1920px、23〜60 FPS、映像 VBR 最大 25Mbps | **3秒以上、最大15分** | **最大 300MB** | ✅ 公式リファレンス |
| Instagram リール(アプリ) | — | 9:16、1080×1920 | 資料により 90秒〜20分と不一致 | 約4GB とする資料 | 🟡(アプリ内で確認) |
| **YouTube Shorts** | MP4 など | 縦向き 9:16 | **最大3分** | — | ✅ YouTube ヘルプ(長さ) |
| TikTok | MP4 / MOV(H.264+AAC) | 9:16、1080×1920 | 10分(一部アカウント・Web で60分)とする資料 | モバイル 約72MB(Android)/ 約288MB(iOS)、Web 1GB〜と不一致 | 🟡 |
| **Threads(API)** | MOV / MP4(H.264 または HEVC + AAC) | 比率 0.01:1〜10:1(**9:16 推奨**)、最大横幅 1920px、23〜60 FPS、映像 VBR 最大 100Mbps | **最大5分**(0秒超) | **最大 1GB** | ✅ 公式 |
| **X(API)** | MP4 / MOV(H.264 High Profile + AAC-LC) | 比率 **1:3〜3:1**、32×32〜1280×1024。推奨 1280×720 / 720×1280 / 720×720、30 または 60 fps | **通常: 20分、Premium/認証済み: 125分**(0.5秒以上) | **通常: 8GB、Premium: 16GB** | ✅ docs.x.com(DM 動画は 140秒・512MB / 10分・1GB) |
| Facebook リール | MP4 など | 9:16 | 未確認 | 未確認 | ⚪ |
| Bluesky | MP4 | — | 3分(従来)/ 10分(新)と不一致 | 100MB(従来)/ 300MB(新) | 🟡 |

## 2. 横型・長尺動画

| サービス | 形式 | 比率・解像度 | 長さ・容量 | 確度 |
|---|---|---|---|---|
| **YouTube** | **MP4**(H.264 High Profile、closed GOP、CABAC、4:2:0。音声 AAC-LC 48kHz) | 標準 16:9。縦長・正方形はプレーヤーが調整 | 256GB または 12時間のうち小さい方とする資料 | ✅ エンコード設定 / 🟡 サイズ・長さ |
| Facebook | 未確認 | 16:9 | 未確認 | ⚪ |
| X | 上記(API) | 16:9(1280×720 推奨。Premium は 1080p) | 上記 | ✅ |

## 3. YouTube の推奨映像ビットレート(✅ 公式「おすすめのエンコード設定」)

| 解像度 | 標準フレームレート(24/25/30) | 高フレームレート(48/50/60) |
|---|---|---|
| 720p | 5 Mbps | 7.5 Mbps |
| **1080p** | **8 Mbps** | **12 Mbps** |
| 1440p | 16 Mbps | 24 Mbps |
| 2160p(4K) | 35〜45 Mbps | 53〜68 Mbps |

音声: ステレオ **384kbps**、モノラル 128kbps、5.1 512kbps。**フレームレートは撮影時と同じで書き出す**。インターレースは解除。

## 4. サムネイル・カバー

| サービス | 用途 | 仕様 | 確度 |
|---|---|---|---|
| **YouTube** | 動画のサムネイル | 16:9、推奨 3840×2160、最小幅 640px、JPG/PNG。**モバイルは 2MB、パソコンは 50MB** まで | ✅ |
| **YouTube** | ショートのサムネイル | **9:16**、推奨 2160×3840、最小幅 640px。パソコンから 50MB まで | ✅ |
| YouTube | 縦向き動画に 16:9 のサムネイルを付けた場合 | ホーム・探索・登録チャンネルでは**自動生成の 4:5 に置き換え** | ✅ |
| Instagram | リールのカバー | **JPEG、8MB 以下、sRGB**。9:16 推奨。`cover_url` または `thumb_offset` で指定 | ✅ |
| TikTok | カバー | 動画の1コマまたは画像 | ⚪ |

## 5. 運用上の注意

1. **長さの上限は変更が頻繁**: 投稿前にアプリ内で確認し、検証結果を [verification-queue](../00-meta/verification-queue.md) に記録する。
2. **API は UI と制限が異なる**(例: Instagram リールの API は最大 15 分・300MB)。API を使う場合は [20-api](../20-api/README.md)。
3. **X の動画上限は API プランではなく、投稿するユーザーの Premium/認証済みの有無で決まる**。上限を超えると 403(アップロードに成功しても投稿で失敗する)。
4. **縦型は安全領域**: 上部・下部にUI(ユーザー名、キャプション、ボタン)が重なる。**上下約10〜15%、右側約15%**を空ける(⚪ 経験則。各アプリで実機確認)。
5. 複数サービスに同じ動画を出すなら、**縦型 1080×1920 の1本を基準**に、透かし(他社ロゴ)を入れない。
6. 書き出しの注意: **`moov` atom を先頭に、編集リストなし、closed GOP、4:2:0、progressive**(X・Instagram・Threads・YouTube の公式要件に共通)。

## 6. ライブ配信(参考)

ライブ配信の推奨設定は録画した動画と異なります。YouTube ライブの推奨ビットレート(例: 1080p・30fps で H.264 推奨 14Mbps ✅)などは [live-streaming](live-streaming.md) を参照してください。

## よくある失敗と対処

| 失敗 | 原因 | 対処 |
|---|---|---|
| アップロードできない・処理が終わらない | 形式・コーデックが非対応、容量超過 | MP4(H.264 + AAC)で書き出し直す。容量は上限の半分程度に |
| 投稿後に画質が大きく落ちる | 低いビットレート、解像度の不一致 | 1080p・8〜12Mbps 程度で書き出す(YouTube の推奨 ✅) |
| 動きがカクカクする | 撮影と書き出しのフレームレートが違う | 撮影時と同じフレームレートで書き出す(✅) |
| 縦動画の上下が切れる | 端末の画面比が 9:16 より縦長 | 重要な要素を中央に置く |
| API で投稿すると失敗する | API とアプリで上限が違う | API の上限(表の ✅ の行)を確認 |

## 関連ページ / 次に読む

- [video-basics](video-basics.md) — 動画の作り方の基本
- [export-presets](export-presets.md) — サービス別の書き出し値
- [video-editing-apps](video-editing-apps.md) — 編集アプリの書き出し設定
- [mobile-viewing-optimization](mobile-viewing-optimization.md) — スマホでの見え方
- [image-specs-comparison](image-specs-comparison.md) — 画像の仕様

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | Instagram リール・カバーの API 仕様 |
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | Threads の動画仕様 |
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | X の動画仕様(API) |
| https://support.google.com/youtube/answer/10059070 | 2026-11-03 | YouTube ショート(最大3分) |
| https://support.google.com/youtube/answer/1722171 | 2026-11-03 | おすすめのエンコード設定 |
| https://support.google.com/youtube/answer/72431 | 2026-11-03 | サムネイル |
| [sources.md](../00-meta/sources.md) | 2026-11-03 | 二次資料(🟡)の一覧 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(このページで分かること、概要の3点、用語表、ライブ配信への案内、よくある失敗、関連ページ、出典・変更履歴を追加。既存の表と ✅ は維持) |
