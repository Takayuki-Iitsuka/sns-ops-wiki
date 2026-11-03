---
title: 書き出しプリセット(サービス別)
platform: common
topic: media
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/x-api/media/best-practices.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://support.google.com/youtube/answer/72431
  - https://support.google.com/youtube/answer/1722171
  - https://support.google.com/youtube/answer/10059070
  - https://support.google.com/youtube/answer/10456525?hl=ja
---

# 書き出しプリセット

> **このページで分かること**: 各サービスに画像・動画を投稿するとき、そのまま使える「書き出しの設定値」(サイズ・形式・容量・ビットレート)と、書き出しの手順。
>
> **対象**: 初心者(何 px で保存すればよいか分からない人)〜中級者  **先に読むページ**: [image-specs-comparison](image-specs-comparison.md)(上限の一覧)

[画像](image-specs-comparison.md)・[動画](video-specs-comparison.md)の上限値(✅ 公式で確認できたものと 🟡 を含む)の**範囲内に収まるよう設計した、推奨の書き出し値**です。値そのものは設計案(⚪)です。上限ぎりぎりを避けるため、容量は上限の約半分を目標にしています。

## 概要

「書き出し(export)」とは、編集アプリで作った画像・動画を、投稿用のファイル(JPEG、PNG、MP4 など)として保存することです。サービスごとに**受け付けるサイズ・比率・容量**が違うため、合わない設定だと次のことが起きます。

- 自動で縮小・再圧縮され、文字がにじむ・画質が落ちる。
- 比率が合わず、端が切れる。
- 容量オーバーでアップロードできない。

このページの表は「**上限(公式の仕様)**」ではなく「**この値で書き出せば安全**」という推奨値です。上限そのものは [image-specs-comparison](image-specs-comparison.md) と [video-specs-comparison](video-specs-comparison.md) を見てください。

## 用語

| 用語 | 意味 |
|---|---|
| px / pixel(ピクセル) | 画像を作る点の数。1080×1350 は横1080点・縦1350点 |
| aspect ratio(アスペクト比、縦横比) | 横:縦の比。4:5 は縦長、16:9 は横長 |
| JPEG / PNG | 写真向けの形式(容量が小さい)/ 文字・図向けの形式(にじまない) |
| codec(コーデック) | 動画・音声の圧縮方式。H.264(映像)と AAC(音声)が最も広く使える |
| bitrate(ビットレート) | 1秒あたりのデータ量。Mbps(メガビット毎秒)。大きいほど高画質・大容量 |
| fps / frames per second(フレームレート) | 1秒あたりのコマ数。30fps が一般的 |
| sRGB | Web 表示の標準の色空間 |
| Exif(撮影情報) | 写真に埋め込まれる撮影日時・機種・位置情報 |
| `moov` atom / faststart | 動画の目次情報。ファイルの先頭に置くと読み込みが速い |
| closed GOP / progressive | 動画の圧縮の区切り方 / 1コマを一度に描く方式(インターレースでない) |
| safe area(安全領域) | UI の重なりや切り抜きがあっても欠けない範囲 |

## 画像

| サービス | 用途 | サイズ(px) | 比率 | 形式 | 容量目標 | 備考 |
|---|---|---|---|---|---|---|
| X | 1枚(横) | 1600×900 | 16:9 | JPEG/PNG | 〜2.5MB | 2:1〜3:4 の範囲内 |
| X | 1枚(正方) | 1200×1200 | 1:1 | JPEG/PNG | 〜2.5MB | |
| X | 縦長 | 1200×1600 | 3:4 | JPEG/PNG | 〜2.5MB | 範囲の端。上下を欠けさせない |
| X | ヘッダー | 1500×500 | 3:1 | JPEG/PNG | 〜1MB | 左下はアイコンが重なる |
| X | プロフィール | 400×400 | 1:1 | JPEG/PNG | 〜500KB | 2MB 以下 |
| Instagram | フィード縦長 | 1080×1350 | 4:5 | **JPEG**(API 投稿は JPEG のみ ✅) | 〜3MB(API は 8MB 以下) | 比率範囲 4:5〜1.91:1 内、幅 1440px 以内 ✅ |
| Instagram | フィード正方 | 1080×1080 | 1:1 | JPEG | 〜3MB | |
| Instagram | フィード横長 | 1080×566 | 1.91:1 | JPEG | 〜2MB | |
| Instagram | ストーリーズ | 1080×1920 | 9:16 | JPEG/PNG | 〜3MB | 上下の安全領域を空ける |
| Threads | フィード | 1080×1350 | 4:5 | JPEG / PNG(8MB 以下 ✅) | 〜3MB | 比率 10:1 以内、幅 1440px 以内 ✅ |
| note | 見出し | 1280×670 | 約1.91:1 | JPEG/PNG | 〜2MB | 10MB 以下。文字は中央 |
| note | 本文内図解 | 幅1280 | 任意 | PNG/JPEG | 〜2MB | |
| YouTube | サムネイル(動画) | 1920×1080(公式の推奨は 3840×2160) | 16:9 | JPEG/PNG | 〜1.5MB(**モバイルからは 2MB 以下**、パソコンは 50MB 以下 ✅) | 右下に再生時間が重なる。幅 640px 以上 |
| YouTube | サムネイル(ショート) | 1080×1920(公式の推奨は 2160×3840) | 9:16 | JPEG/PNG | 〜1.5MB(パソコンは 50MB 以下 ✅) | 幅 640px 以上 |
| YouTube | バナー | 2560×1440(最小 2048×1152 ✅) | 16:9 | JPEG/PNG | 〜4MB(6MB 以下 ✅) | **文字・ロゴは中央 1235×338 に** ✅(旧記載 1546×423 は 🟡 の古い値) |
| YouTube | プロフィール | 800×800 | 1:1 | JPEG/PNG | 〜1MB(15MB 以下 ✅) | 円形切り抜き。98×98px で表示される ✅ |
| Facebook | リンク/共有 | 1200×630 | 1.91:1 | JPEG | 〜1MB | ⚪ |
| Bluesky | 投稿 | 長辺 〜1600 | 任意 | JPEG | 〜900KB(1MB 想定) | 従来上限 1MB に合わせる |
| LINE | リッチメニュー | 2500×1686 / 2500×843 | — | JPEG/PNG | — | ⚪ 要確認 |
| KDP | 表紙 | 2560×1600 | 1.6:1 | JPEG/TIFF | — | ⚪ 要確認 |

### 迷ったときの3枚(⚪)

| 作るもの | サイズ | 使える先 |
|---|---|---|
| 縦長 | 1080×1350(4:5) | Instagram・Threads のフィード、X(3:4 の範囲内に収まる) |
| 正方形 | 1080×1080(1:1) | ほぼ全サービス |
| 縦型全画面 | 1080×1920(9:16) | ストーリーズ、リール、ショート、TikTok |

## 動画

| サービス | 用途 | 解像度 | 比率 | コーデック | フレーム | ビットレート目安 | 長さ・容量の目標 |
|---|---|---|---|---|---|---|---|
| Instagram | リール | 1080×1920 | 9:16 | H.264+AAC(48kHz 以下) | 30fps(23〜60 ✅) | 8〜12Mbps(最大 25Mbps ✅) | **15分以内、300MB 以内**(API の公式上限 ✅)。アプリは資料不一致のため短めに |
| YouTube | Shorts | 1080×1920 | 9:16 | H.264+AAC | 撮影時と同じ | 8〜12Mbps | **3分以内**(✅ 公式) |
| YouTube | 通常(横) | 1920×1080 | 16:9 | **MP4**(H.264 High、closed GOP、AAC-LC 48kHz) | 撮影時と同じ | **8Mbps(48〜60fps は 12Mbps)** ✅ | 音声 384kbps(ステレオ)。`moov` を先頭に |
| TikTok | 縦型 | 1080×1920 | 9:16 | H.264+AAC | 30fps | 8Mbps | 10分以内、モバイルの容量を考慮し 70MB 以内なら確実 |
| Threads | 縦型 | 1080×1920 | 9:16 | H.264+AAC | 30fps(23〜60 ✅) | 8Mbps(最大 100Mbps ✅) | **5分以内、1GB 以内** ✅ |
| X | 横 | 1280×720(Premium は 1080p 可 ✅) | 16:9 | H.264 High + AAC-LC | 30 または 60fps ✅ | 映像 5〜8Mbps(最低 5,000kbps ✅)、音声 128kbps 以上 | **20分以内・8GB 以内**(通常アカウント)、125分・16GB(Premium) ✅ |
| X | 縦 | 720×1280 | 9:16 | H.264 High + AAC-LC | 30 または 60fps ✅ | 同上 | 同上 |
| Bluesky | 縦/横 | 1080×1920 / 1280×720 | — | H.264+AAC | 30fps | 5Mbps | 3分以内、100MB 以内(従来上限) |

### 縦型の安全領域(⚪)

```
┌─────────────────┐
│ ▒▒ 上 約10% ▒▒  │ ← ユーザー名・UI
│                 │
│   ここに主要     │
│   な要素        │
│                 │
│ ▒▒ 下 約15% ▒▒  │ ← キャプション・ボタン
└─────────────────┘
        右 約15% はボタンが重なる
```

## 書き出しの手順

1. マスター(縦型 1080×1920、横型 1920×1080)を作る。
2. 上の表の用途に合わせて**比率を切り出し**(トリミングでなく再レイアウトを推奨)。
3. 画像は sRGB、Exif の位置情報を削除。動画は **`moov` atom を先頭・編集リストなし・closed GOP・4:2:0・progressive**(X・Instagram・Threads・YouTube の公式要件に共通 ✅)。
4. 実機で表示確認(ダークモード/ライトモード、縮小表示)。
5. 検証結果を [verification-queue](../00-meta/verification-queue.md) に反映。

### アプリで書き出すときに見る項目(⚪ 名称はアプリで違う)

| 項目 | 画像 | 動画 |
|---|---|---|
| サイズ / 解像度 | 表の px | 1080×1920 など |
| 形式 | 写真は JPEG、文字・図は PNG | MP4(H.264) |
| 品質 | JPEG 品質 80〜90 前後 | ビットレートを表の目安に |
| 色 | sRGB | — |
| フレームレート | — | 撮影時と同じ(30fps が無難) |
| その他 | 位置情報を含めない | 「Web 用に最適化」「ファストスタート」があればオン |

> スマホの編集アプリは「1080p」「30fps」などの選択肢だけのことが多いです。その場合は **1080p・30fps・高画質**を選べば、ほとんどのサービスの範囲に収まります(⚪)。編集アプリの選び方は [video-editing-apps](video-editing-apps.md)。

## 自動化(任意)

Python(Pillow)や ffmpeg でプリセットを一括書き出しできます。大量処理の前に1枚で試し、画像の実ファイルはリポジトリに入れず(ソースのみ)管理します。

### ffmpeg の例(縦型 9:16、⚪ 設計例)

```bash
ffmpeg -i master.mov \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -b:v 8M -maxrate 10M -bufsize 16M \
  -c:a aac -b:a 128k -ar 48000 -movflags +faststart out_9x16.mp4
```

- `-pix_fmt yuv420p` は 4:2:0、`-movflags +faststart` は `moov` を先頭に置く指定です。

### Pillow の例(位置情報を含めずに JPEG 保存、⚪ 設計例)

```python
from PIL import Image
img = Image.open("master.png").convert("RGB")
img.thumbnail((1080, 1350))           # 比率を保って縮小
img.save("out_4x5.jpg", "JPEG", quality=85)  # exif を渡さないので撮影情報は書き込まれない
```

## 文字サイズ・スマートフォンでの見え方

1080px 幅の画像では **本文 44px 以上**、1280px 幅(note)では約 50px 以上、YouTube サムネイル(1280×720)では **100px 以上**が目安。根拠と計算は [mobile-viewing-optimization](mobile-viewing-optimization.md)。

## よくある失敗と対処

| 失敗 | 起きること | 対処 |
|---|---|---|
| 4000px の写真をそのまま投稿 | サービス側で強く再圧縮され、にじむ | 表のサイズに縮小してから投稿 |
| 文字入りの画像を JPEG で保存 | 文字のまわりにノイズ | PNG で保存(Instagram API 用は高品質 JPEG) |
| 容量を上限ぎりぎりにした | 回線や仕様変更で失敗 | 上限の半分程度に |
| 9:16 動画の下端に字幕を置いた | キャプションやボタンに隠れる | 下約15%を空ける |
| 60fps で撮って 30fps に変換 | 動きがカクつく | 撮影時と同じ fps で書き出す |
| 書き出し後に実機で見ていない | 小さすぎて読めない | スマホで実寸確認 |

## チェックリスト

- [ ] 表のサイズ・比率で書き出した
- [ ] 写真は JPEG、文字・図は PNG(Instagram API は JPEG)
- [ ] 容量は上限の半分程度
- [ ] 位置情報(Exif)を削除した
- [ ] 動画は H.264 + AAC、`moov` が先頭(faststart)
- [ ] 縦型は上・下・右の安全領域を空けた
- [ ] スマホの実機で確認した

## 関連ページ / 次に読む

- [image-specs-comparison](image-specs-comparison.md) / [video-specs-comparison](video-specs-comparison.md)(上限の一覧)
- [image-production-workflow](image-production-workflow.md)(制作の流れ)
- [mobile-viewing-optimization](mobile-viewing-optimization.md)(スマホでの見え方)
- [tools](tools.md)(ツール)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/media/best-practices.md | 2026-11-03 | X の動画の推奨(既存の ✅ 値の出典) |
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | Instagram の画像・リールの仕様 |
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | Threads の画像・動画の仕様 |
| https://support.google.com/youtube/answer/72431 | 2026-11-03 | YouTube のサムネイル |
| https://support.google.com/youtube/answer/1722171 | 2026-11-03 | YouTube のエンコード設定 |
| https://support.google.com/youtube/answer/10059070 | 2026-11-03 | YouTube ショート(3分) |
| https://support.google.com/youtube/answer/10456525?hl=ja | 2026-11-03 | バナー(最小 2048×1152、安全領域 1235×338、6MB)、プロフィール写真(98×98 表示、15MB) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成 |
| 2026-11-03 | 初心者向けに加筆(概要、用語、迷ったときの3枚、アプリで見る項目、ffmpeg・Pillow の例、よくある失敗、チェックリスト、出典)。YouTube バナー・プロフィールを公式ヘルプで確認し ✅ を追加。**バナーの安全領域を 1546×423(🟡)→ 1235×338(✅ 公式)に修正** |
