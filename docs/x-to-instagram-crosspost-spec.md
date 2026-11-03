# X → Instagram クロスポスト 変換仕様書

作成時点: 2026年(皇紀2686年・令和8年)11月

> **信頼度に関する注意**
> 本書の数値(サイズ・長さ・上限)は筆者の知識に基づく。Meta・X の仕様は頻繁に変わるため、実装前に必ず一次資料で再確認すること。確度が低い項目は「⚠要確認」と明記した。
>
> 一次資料(確認先):
> - Instagram Platform / Content Publishing: https://developers.facebook.com/docs/instagram-platform/content-publishing
> - Instagram Reels 仕様: 同上(`media_type=REELS` の節)
> - X API v2 Media / Posts: https://docs.x.com/
> - X メディアベストプラクティス: https://developer.x.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices

---

## 1. 概要

### 1.1 目的
X に投稿した本文・画像・動画を、同一内容で Instagram に自動展開する。両 SNS でメディア規格・文字数・リンク挙動が異なるため、**メディア変換(トランスコード/リサイズ/クロップ)**と**本文変換**を行う中間パイプラインを実装する。

### 1.2 前提・制約
| 項目 | 内容 |
|---|---|
| Instagram アカウント | プロアカウント(Business または Creator)必須。個人アカウントは API 投稿不可 |
| 投稿手段 | Instagram Graph API(Content Publishing)。Facebook ページ連携 or Instagram ログイン |
| メディア渡し方 | 画像は**公開 HTTPS URL**必須。動画は公開 URL またはリジューマブルアップロード |
| X 側の取得 | 自アカウントの投稿のみ対象。X API v2(要有料プラン⚠要確認)。スクレイピングは規約違反のため不採用 |
| 権利 | 他者の投稿のリポスト/引用は対象外。自作コンテンツのみ |

### 1.3 スコープ
- 対象: テキスト、画像(1〜4枚)、動画(1本)、GIF
- 対象外(初版): スレッド全体の展開、投票(Poll)、引用ポスト、Spaces、Stories、Instagram→X の逆方向

---

## 2. 全体アーキテクチャ

```
[X 投稿検知] → [取得/正規化] → [判定ルーター] → [メディア変換] → [公開用ストレージ] → [IG コンテナ作成] → [ステータス待機] → [media_publish] → [記録/通知]
 Webhook/Poll    X API v2         投稿種別      sharp/ffmpeg     S3/R2 等(署名なし公開)   POST /media        GET status_code     POST /media_publish   DB・Slack
```

### 2.1 コンポーネント
| コンポーネント | 責務 | 推奨実装 |
|---|---|---|
| Watcher | X の新規投稿検知 | Account Activity API(Webhook)または `GET /2/users/:id/tweets` ポーリング(1〜5分) |
| Normalizer | 投稿を内部モデルへ変換 | 下記 §3 のスキーマ |
| Router | 投稿種別の判定 | 画像/動画/GIF/テキストのみ |
| Image Processor | 画像の比率・サイズ・形式変換 | sharp(libvips)または ImageMagick |
| Video Processor | 動画のトランスコード | ffmpeg |
| Storage | IG に渡す公開 URL を発行 | S3/Cloudflare R2、公開後にライフサイクルで削除 |
| IG Publisher | コンテナ作成〜公開 | Graph API クライアント(リトライ・ポーリング込み) |
| State Store | 冪等性・履歴 | DB(下記テーブル) |
| Notifier | 失敗・要確認の通知 | Slack/メール |

### 2.2 処理フロー(状態遷移)
`DETECTED → FETCHED → CONVERTING → UPLOADED → IG_CONTAINER_CREATED → IG_PROCESSING → PUBLISHED`
失敗時: `FAILED(reason)` / 人手確認: `NEEDS_REVIEW`

---

## 3. データモデル

### 3.1 内部投稿モデル
```json
{
  "x_post_id": "string",
  "text": "string",
  "entities": { "urls": [], "mentions": [], "hashtags": [] },
  "media": [
    { "type": "image|video|animated_gif", "url": "string", "width": 0, "height": 0,
      "duration_ms": 0, "alt_text": "string|null", "variants": [] }
  ],
  "is_reply": false, "is_retweet": false, "is_quote": false,
  "created_at": "ISO8601"
}
```

### 3.2 管理テーブル `crosspost_jobs`
| カラム | 型 | 説明 |
|---|---|---|
| id | uuid | PK |
| x_post_id | text UNIQUE | **冪等性キー**(二重投稿防止) |
| ig_creation_ids | jsonb | 子コンテナ+親の creation_id |
| ig_media_id | text | 公開後の media id |
| status | text | 上記状態遷移 |
| error | text | 失敗理由 |
| converted_assets | jsonb | 変換後ファイルの URL・寸法・ハッシュ |
| created_at / updated_at | timestamptz | |

---

## 4. 投稿種別の判定(ルーティング)

| X の投稿 | Instagram での展開 | `media_type` |
|---|---|---|
| テキストのみ | **投稿しない**(IG はメディア必須)。設定により「テキスト画像化」オプション | — |
| 画像 1 枚 | 単一画像フィード投稿 | `IMAGE`(省略可) |
| 画像 2〜4 枚 | カルーセル | `CAROUSEL` |
| 動画 1 本 | リール | `REELS` |
| GIF(X では MP4 として配信) | MP4 化してリール | `REELS` |
| リプライ/リポスト/引用 | **既定でスキップ**(設定で変更可) | — |

> フィード動画: 現行 API では動画は原則リール(`REELS`)として公開される。`VIDEO` 単体指定は廃止/非推奨の扱い(⚠要確認)。

---

## 5. メディア変換仕様

### 5.1 規格比較

#### 画像
| 項目 | X | Instagram(API) | 変換要否 |
|---|---|---|---|
| 形式 | JPEG/PNG/GIF/WebP | **JPEG のみ** | PNG/WebP → JPEG 変換必須 |
| 最大容量 | 5MB(画像)/15MB(GIF) | **8MB** | 超過時は品質を下げて再エンコード |
| 枚数 | 最大 4 | カルーセル最大 10 | そのまま可 |
| 縦横比 | 自由(表示は切り詰めあり) | **4:5(0.8)〜1.91:1** | 範囲外は変換必須 |
| 幅 | 最大 4096px 程度⚠ | 最小 320px、**最大 1440px**(超過は縮小される) | 1080〜1440px に正規化 |
| 色空間 | 任意 | sRGB 推奨 | ICC を sRGB へ変換 |
| ALT テキスト | 最大 1000 文字 | 対応(`alt_text` パラメータ)。文字数上限は⚠要確認 | 切り詰め |

#### 動画
| 項目 | X | Instagram リール(API) | 変換要否 |
|---|---|---|---|
| コンテナ | MP4/MOV | **MP4/MOV** | — |
| 映像コーデック | H.264(High)推奨 | **H.264 または HEVC**、プログレッシブ | 非対応なら再エンコード |
| 音声 | AAC | **AAC**、最大 48kHz、モノ/ステレオ | 再エンコード |
| 長さ | 通常 2分20秒(Premium は長尺)⚠ | **3秒〜15分**(上限は改定履歴あり⚠要確認) | 下限未満はループ延長、超過は短縮 or スキップ |
| 容量 | 512MB | リール 最大約 300MB⚠要確認(リジューマブル利用で大容量可) | ビットレート調整 |
| 縦横比 | 1:3〜3:1 | リール推奨 **9:16**、許容 0.01:1〜10:1(ただし表示は 9:16 に収められる) | §5.3 の方式で変換 |
| 解像度 | 最大 1920×1200 など | 推奨 **1080×1920**、最小 720px 幅推奨 | |
| フレームレート | 〜60fps | **23〜60fps** | 範囲外は 30fps に統一 |
| ビットレート | — | 映像 最大 25Mbps、音声 最大 128kbps(目安)⚠ | |

### 5.2 画像変換ルール
入力 `W×H`、比率 `r = W/H`。

| 条件 | 処理 |
|---|---|
| `0.8 ≤ r ≤ 1.91` | 比率維持。縮小・形式変換のみ |
| `r < 0.8`(縦長すぎ) | **戦略 A: 中央クロップで 4:5 に** / **戦略 B: ぼかし背景パディングで 4:5 に** |
| `r > 1.91`(横長すぎ) | 戦略 A: 1.91:1 にクロップ / 戦略 B: 上下に余白を足し 1.91:1 以上に |
| 幅 > 1440 | 1440px に縮小(Lanczos) |
| 幅 < 320 | 拡大しない。`NEEDS_REVIEW` |
| PNG(透過あり) | 白背景に合成して JPEG 化(背景色は設定可) |
| 容量 > 8MB | JPEG 品質 90 → 85 → 80 と段階的に再エンコード |

**カルーセル(画像 2〜4 枚)の特則**
- 最初のアイテムの比率が全アイテムに適用される。→ **全画像を第1画像と同じ比率に揃える**(クロップ/パディング)。
- 揃える比率は既定 `1:1`(全画像の無理が少ない)。設定で 4:5 を選択可。

**戦略の既定値**: 被写体情報の欠落を避けるため **パディング(B)を既定**、設定でスマートクロップ(A)に切替可能。スマートクロップは顔検出/注目領域(sharp の `attention`/`entropy`、または顔検出モデル)を使用。

sharp 例:
```js
await sharp(input)
  .rotate()                                   // EXIF 向き補正
  .toColourspace('srgb')
  .resize({ width: 1080, height: 1350, fit: 'cover', position: sharp.strategy.attention })
  .flatten({ background: '#ffffff' })
  .jpeg({ quality: 90, mozjpeg: true })
  .toFile(output);
```

### 5.3 動画変換ルール

**ぼかし背景パディング(縦長 9:16 化)** — 既定:
```bash
ffmpeg -i in.mp4 -filter_complex \
"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5[bg]; \
 [0:v]scale=1080:1920:force_original_aspect_ratio=decrease[fg]; \
 [bg][fg]overlay=(W-w)/2:(H-h)/2,fps=30,format=yuv420p[v]" \
-map "[v]" -map 0:a? \
-c:v libx264 -profile:v high -preset medium -crf 20 -maxrate 20M -bufsize 40M \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart -t 900 out.mp4
```

**センタークロップ(戦略 A)**:
```bash
ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" \
  -c:v libx264 -crf 20 -c:a aac -b:a 128k -movflags +faststart out.mp4
```

**GIF/アニメ GIF(X では MP4)**
- 3 秒未満 → `-stream_loop` で 3 秒以上になるようループ延長。
- 音声なしでも可。無音 AAC トラックを付与すると互換性が上がる場合あり⚠。

**共通ルール**
| 条件 | 処理 |
|---|---|
| コーデック/コンテナ不適合 | 再エンコード |
| 適合しており比率・容量 OK | **再エンコードせず**ストリームコピー(画質劣化回避) |
| 容量超過 | 2-pass で目標ビットレート算出し再エンコード |
| 長さ超過 | 先頭から上限で切る or `NEEDS_REVIEW`(設定) |
| 縦動画 9:16 | パディング不要 |
| 横動画 16:9 | 既定: ぼかしパディングで 9:16。設定で「そのまま(横長リール)」も可 |
| `moov` atom | `+faststart` で先頭へ(Meta 側取得の安定化) |

**サムネイル/カバー**: `cover_url`(画像)または `thumb_offset`(ms)を指定可能。X のポスター画像があれば 9:16 に変換して使用。

---

## 6. 本文(キャプション)変換仕様

| 項目 | X | Instagram | 変換ルール |
|---|---|---|---|
| 文字数 | 280(加重)/ Premium は長文可 | **2,200 文字** | 通常は収まる。超過時は切り詰め+省略記号 |
| ハッシュタグ | 制限緩い | **最大 30 個** | 31 個目以降を削除(通知) |
| メンション | `@x_handle` | `@ig_handle` | **ハンドル名は別物**。対応表(マッピング)で置換、未登録は `@` を除去 or 平文化 |
| 最大メンション数 | — | 20 | 超過分は平文 |
| URL | `t.co` 短縮・クリック可 | **キャプション内リンクはクリック不可** | `t.co` を展開して表示、または「プロフのリンクから」へ置換。UTM 付与は任意 |
| 末尾の メディア URL (`pic.x.com/...`) | 付く | 不要 | **削除** |
| 改行 | あり | あり | 維持(連続空行は最大 2 に正規化) |
| 絵文字・日本語 | 可 | 可 | そのまま。サロゲートペアの切断に注意 |
| 「続きはスレッドで」等 | — | — | 設定で付与可 |
| 固定ハッシュタグ・署名 | — | — | テンプレート `{{text}}\n\n{{fixed_tags}}` を設定可能に |

**文字数の数え方**: X は加重カウント(CJK=2)、IG は Unicode コードポイント数(⚠要確認)。IG 側は `Array.from(text).length` 等で数える。

---

## 7. Instagram 公開フロー(API 仕様)

### 7.1 単一画像
```
POST /{ig-user-id}/media
  image_url=https://cdn.example.com/a.jpg
  caption=...
  alt_text=...
→ { "id": "<creation_id>" }

POST /{ig-user-id}/media_publish
  creation_id=<creation_id>
→ { "id": "<ig_media_id>" }
```

### 7.2 カルーセル
1. 各アイテムにつき `POST /{ig-user-id}/media` を `is_carousel_item=true` で実行(画像は `image_url`、動画は `media_type=VIDEO`+`video_url`)。
2. 親コンテナ: `POST /{ig-user-id}/media` に `media_type=CAROUSEL`、`children=id1,id2,...`、`caption`。
3. `media_publish`。

### 7.3 リール
```
POST /{ig-user-id}/media
  media_type=REELS
  video_url=https://cdn.example.com/v.mp4     # または upload_type=resumable
  caption=...
  share_to_feed=true
  cover_url=... / thumb_offset=...
```
- `status_code` が `FINISHED` になるまで `GET /{creation_id}?fields=status_code,status` を**ポーリング**(5〜10秒間隔、最大 10〜15分)。`IN_PROGRESS` → `FINISHED` / `ERROR` / `EXPIRED`。
- 大容量動画はリジューマブルアップロード(`rupload.facebook.com`)を推奨。

### 7.4 制限・エラー処理
| 項目 | 内容 |
|---|---|
| 投稿数上限 | **24時間あたり 100 件**(カルーセルは 1 件扱い)。`content_publishing_limit` エンドポイントで残量確認可 |
| コンテナ有効期限 | 作成後 24 時間 |
| 画像 URL | 認証なし・リダイレクトなし・200 応答・正しい `Content-Type` |
| アクセストークン | 長期トークン(約 60 日)。期限前に更新ジョブを実行 |
| 権限 | `instagram_basic`, `instagram_content_publish`(+ ページ連携時 `pages_show_list` 等) |
| リトライ | 429/5xx/一時エラーは指数バックオフ(最大 4 回)。`ERROR` ステータスは原因別に分類し、メディア不適合は再変換して 1 回だけ再試行 |
| アプリレビュー | 他者アカウントで運用する場合は Meta のアプリレビュー(権限審査)が必要。自アカウントのみなら開発モードで可 |

---

## 8. 非機能要件

| 項目 | 要件 |
|---|---|
| 冪等性 | `x_post_id` 一意制約。再実行しても二重投稿しない |
| 遅延 | 画像: 検知から 2 分以内。動画: 変換+IG 処理込みで 15 分以内を目標 |
| 秘密情報 | X/Meta のトークンは Secrets Manager 等に保管。ログに出さない |
| ストレージ | 変換後ファイルは公開 URL 化し、投稿成功/失敗確定後 24〜72 時間で削除 |
| 観測性 | 各状態遷移を構造化ログ化。失敗は通知 |
| 手動介入 | `NEEDS_REVIEW` キュー(承認後に公開)モードを用意。初期運用は**承認制を推奨** |
| テスト | 比率境界値(0.79/0.8/1.91/1.92)、8MB 超、PNG 透過、EXIF 回転、2 秒/16 分動画、30 超ハッシュタグ、`t.co` 展開 |

---

## 9. 設定項目(例)

```yaml
crosspost:
  skip_replies: true
  skip_retweets: true
  skip_quotes: true
  text_only_policy: skip            # skip | render_text_image
  image:
    fit_strategy: pad_blur          # pad_blur | smart_crop
    carousel_ratio: "1:1"           # 1:1 | 4:5
    max_width: 1440
    jpeg_quality: 90
    transparent_bg: "#ffffff"
  video:
    landscape_policy: pad_blur_9x16 # pad_blur_9x16 | keep_landscape | center_crop
    max_duration_sec: 900
    min_duration_sec: 3
    fps: 30
  caption:
    max_chars: 2200
    max_hashtags: 30
    expand_tco: true
    append_template: "{{text}}\n\n#fixed_tag"
    mention_map: { "@x_handle": "@ig_handle" }
  approval_mode: true               # true: 手動承認後に公開
```

---

## 10. 実装ステップ(推奨順)

1. **PoC**: 画像 1 枚のみ。X API 取得 → sharp 変換 → S3 配置 → IG 公開。
2. **画像拡張**: カルーセル、比率戦略、ALT テキスト。
3. **動画**: ffmpeg 変換、ポーリング、リジューマブルアップロード。
4. **本文変換**: ハッシュタグ/メンション/URL 規則、テンプレート。
5. **運用機能**: 承認キュー、通知、トークン更新、レート制限管理。
6. **品質**: テストデータセット作成、変換結果の目視確認 UI。

---

## 11. リスク・未確定事項

| # | 内容 | 対応 |
|---|---|---|
| 1 | X API の提供条件・料金(⚠要確認) | 実装前に最新プランを確認 |
| 2 | リールの長さ・容量上限、`VIDEO` 廃止状況(⚠要確認) | 公式ドキュメントで再確認、設定値化 |
| 3 | IG の `alt_text` 上限、グリッド表示比率(近年 3:4 表示へ変更の報⚠) | 実機検証。重要被写体は中央に配置されるよう変換 |
| 4 | 自動クロスポスト時の見え方がネイティブ投稿より劣る | 承認制+プレビュー確認で品質担保 |
| 5 | ぼかしパディングは好みが分かれる | 設定で切替可能に |
| 6 | Meta/X の規約変更 | 四半期ごとに仕様レビュー |
