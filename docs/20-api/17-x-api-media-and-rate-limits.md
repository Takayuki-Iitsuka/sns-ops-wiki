---
title: X API のメディア投稿とレート制限
platform: x
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/x-api/media/introduction.md
  - https://docs.x.com/x-api/media/quickstart/best-practices.md
  - https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md
  - https://docs.x.com/x-api/fundamentals/rate-limits.md
  - https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md
  - https://docs.x.com/changelog.md
---

# X API のメディア投稿とレート制限

> **このページで分かること**: X API で画像・動画を付けて投稿する流れ、ファイルの上限、動画の推奨設定、レート制限(回数の上限)の読み方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [02-x-api](02-x-api.md)、[16-x-api-getting-started](16-x-api-getting-started.md)

> 2026年(皇紀2686年・令和8年)11月3日に docs.x.com の公式 Markdown を取得して確認した内容です(✅)。もとは [02-x-api](02-x-api.md) の §6・§7 にあった内容を、初心者向けの説明を加えてこのページに移しました。

## 概要

X API で画像や動画を付けて投稿するときは、**2段階**になります。

1. まずファイルを X に**アップロード**し、`media_id`(メディアの番号)を受け取る。
2. 次に投稿(`POST /2/tweets`)の中で、その `media_id` を指定する。

動画のような大きなファイルは、**チャンク**(chunk、小分け)に分けて送ります。2026年9月1日に v2 の新しいアップロード方式に統一されました(✅ changelog)。

また、API には**レート制限**(15分あたり何回まで、など)があります。超えると 429 エラーになります。

## 用語

| 用語 | 意味 |
|---|---|
| media_id(メディア ID) | アップロードしたファイルに付く番号。投稿で指定する |
| chunked upload(分割アップロード) | 大きなファイルを小分けにして送る方式 |
| `initialize` / `append` / `finalize` | 分割アップロードの「開始 / 追加 / 完了」の3段階 |
| `media_category`(メディアの種類) | `tweet_image`(画像)、`tweet_gif`(GIF)、`tweet_video`(動画)など |
| codec(コーデック) | 動画・音声の圧縮方式。H.264、AAC など |
| rate limit window(制限の時間枠) | X では主に15分または24時間 |
| App あたり / User あたり | アプリ全体の上限 / 利用者1人ごとの上限 |

## メディアを含む投稿(✅)

### フロー

1. `POST /2/media/upload/initialize`(JSON ボディ: `media_type`、`total_bytes`、`media_category`)
2. `POST /2/media/upload/{id}/append`(チャンクごと)
3. `POST /2/media/upload/{id}/finalize`
4. 必要なら `GET /2/media/upload`(`command=STATUS`)で処理待ち
5. `POST /2/tweets` の `media.media_ids` に ID を渡す

- 以前の **`command=INIT/APPEND/FINALIZE` 方式は旧プロトコル**で使わない(9月1日に切替 ✅)。
- 単純アップロード `POST /2/media/upload` は**画像と小さなファイルのみ**。動画は必ずチャンク方式。
- 必要なスコープ: `media.write`、`tweet.write`、`tweet.read`、`users.read`(`offline.access` はリフレッシュ用)。

### 制限(✅)

**制限は「認証したユーザーの X Premium/認証済みか」と `media_category` で決まり、API プランでは決まらない**。アップロードと投稿作成で**別々に**検査される(アップロードが成功しても、投稿で 403 になりうる)。

| 種別 | `media_category` | 上限 |
|---|---|---|
| 画像(JPG・PNG・GIF・**WEBP**) | `tweet_image` | **5MB** |
| アニメーション GIF | `tweet_gif` | **15MB**(解像度 1280×1080 以下、350フレーム以下、総画素 3億以下が成功率の目安) |
| 動画(Post)・通常アカウント | `tweet_video` / `amplify_video` | **20分、8GB** |
| 動画(Post)・Premium/認証済み | 同上 | **125分、16GB** |
| 動画(DM)・通常 | `dm_video` | 140秒、512MB |
| 動画(DM)・Premium | `dm_video` | 10分、1GB |

- 動画の最短は 0.5 秒。`initialize` の `total_bytes` は 16GB まで。
- 投稿には**写真4枚まで、または GIF 1つ、または動画 1つ**。
- 通常アカウントの上限を超える動画を投稿すると **403** `This user is not allowed to post a video longer than N minutes.`。

### 動画の推奨・要件(✅)

| 項目 | 推奨 | 必須条件 |
|---|---|---|
| コーデック | H.264 High Profile | — |
| フレームレート | 30 または 60fps | 60fps 以下 |
| 解像度 | 1280×720(横)/ 720×1280(縦)/ 720×720(正方形)。Premium は 1080p のアップロード・再生が可 | 32×32 〜 1280×1024 |
| 比率 | 16:9 または 1:1 | **1:3 〜 3:1**、ピクセル比 1:1 |
| ビットレート | 映像 最低 5,000kbps(推奨表では 720p で 2,048K)、音声 最低 128kbps | — |
| 音声 | AAC-LC(HE-AAC 不可)、モノラルまたはステレオ | 5.1以上は不可 |
| その他 | — | YUV 4:2:0、progressive scan、open GOP 不可 |

## レート制限(✅ 公式)

| エンドポイント | App あたり | User あたり |
|---|---|---|
| `POST /2/tweets` | 10,000/24時間 | **100/15分** |
| `DELETE /2/tweets/:id` | — | 50/15分 |
| `GET /2/tweets/search/recent` | 450/15分 | 300/15分(最大100件/回) |
| `POST /2/media/upload`(単純) | 50,000/24時間 | 500/15分 |
| `POST /2/media/upload/initialize`・`append`・`finalize` | 各 180,000/24時間 | 各 1,875/15分 |

- 応答ヘッダー `x-rate-limit-limit` / `remaining` / `reset` を見る。429 は待機して再試行([01-concepts-and-security](01-concepts-and-security.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md))。
- ベアラートークン(アプリ専用)は App あたり、ユーザー認証は User あたりの制限が適用される。

## 具体例: 画像1枚を付けて投稿する(概念。動作は未検証)

小さな画像は単純アップロード `POST /2/media/upload` が使えます(✅ 上記)。パラメータの細かい名前は公式の media upload のリファレンスで確認してください(⚪ 要確認)。

```python
import os
import requests

token = os.environ["X_USER_ACCESS_TOKEN"]   # media.write と tweet.write を含む OAuth 2.0 トークン
headers = {"Authorization": f"Bearer {token}"}

# 1) 画像をアップロードして media_id を得る(形は概念)
with open("image_1200x675.jpg", "rb") as f:
    up = requests.post(
        "https://api.x.com/2/media/upload",
        headers=headers,
        files={"media": f},
        data={"media_category": "tweet_image"},
        timeout=60,
    )
up.raise_for_status()
media_id = up.json()["data"]["id"]          # 返る項目名は公式で確認(⚪)

# 2) 代替テキスト(alt text、最大1,000字 ✅)を付ける場合は Create Media Metadata を使う($0.005)

# 3) media_id を指定して投稿する
r = requests.post(
    "https://api.x.com/2/tweets",
    headers=headers,
    json={"text": "今週のお知らせです", "media": {"media_ids": [media_id]}},
    timeout=30,
)
print(r.status_code, r.json())
```

## レート制限の読み方(初心者向け)

- 応答ヘッダーの `x-rate-limit-remaining` が**残り回数**、`x-rate-limit-reset` が**回復する時刻**(UNIX 時刻 ⚪)です。
- 例: `POST /2/tweets` は**ユーザーあたり 15分に100回**(✅)。通常の運用(1日に数回の投稿)なら届きません。届くのは、ループの誤りで連投しているときです。
- **レート制限の内側でも料金はかかります**。投稿1回 $0.015、URL 付きは $0.200(✅ [02-x-api](02-x-api.md) §2)。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| アップロードは成功したのに投稿で 403 | 投稿時の検査で上限超え(アカウント種別による動画の長さなど) | 上の表で通常アカウントの上限を確認(✅ アップロードと投稿は別々に検査) |
| 動画が「処理中」のまま | `finalize` 後の処理待ち | `GET /2/media/upload`(`command=STATUS`)で完了を待ってから投稿 |
| 旧方式の `command=INIT` で失敗 | 旧プロトコル | `initialize/append/finalize` に置き換える |
| PNG の写真が重い | 5MB 超え | JPEG で書き出す([export-presets](../01-common/export-presets.md)) |
| 429 が続く | ループの誤り、短時間の連続呼び出し | 待機して再試行。原因のループを直す([14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)) |

## 注意点

- 上限は**認証したユーザーのアカウント種別**(X Premium/認証済みか)で変わります。API の料金プランでは変わりません(✅)。
- アプリからの投稿の上限は API と異なる場合があります([03-media-specs](../02-x/03-media-specs.md))。

## 関連ページ / 次に読む

- [02-x-api](02-x-api.md) — 料金・移行の全体
- [16-x-api-getting-started](16-x-api-getting-started.md) — 登録から最初の投稿まで
- [video-specs-comparison](../01-common/video-specs-comparison.md)、[export-presets](../01-common/export-presets.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | メディアの種類と上限 |
| https://docs.x.com/x-api/media/quickstart/best-practices.md | 2026-11-03 | 動画の推奨・要件 |
| https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md | 2026-11-03 | 分割アップロードの流れ |
| https://docs.x.com/x-api/fundamentals/rate-limits.md | 2026-11-03 | レート制限の表 |
| https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md | 2026-11-03 | 429 と `x-rate-limit-reset` |
| https://docs.x.com/changelog.md | 2026-11-03 | 9月1日のメディアパスの統一 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | [02-x-api](02-x-api.md) の §6(メディア)・§7(レート制限)を移設して新規作成。概要・用語・投稿のコード例・レート制限の読み方・失敗例を追加 |
