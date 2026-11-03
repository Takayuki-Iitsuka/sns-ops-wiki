---
title: Instagram Platform API(コンテンツ公開)
platform: instagram
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/instagram-platform/overview.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md
  - https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md
  - https://developers.facebook.com/docs/graph-api/guides/error-handling
---

# Instagram Platform API(コンテンツ公開)

> **このページで分かること**: Instagram の API でできること・できないこと、始めるための準備、画像・リールの仕様、公開の流れ、上限、トークン、最小コード、よくあるエラー。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)

> 2026年(皇紀2686年・令和8年)11月3日に Meta の公式開発者文書(Markdown 版)を直接取得して確認しました(✅)。API バージョンは **v26.0** が例に使われています。

## 概要

Instagram の API(Instagram Platform)を使うと、**プロフェッショナルアカウント**(ビジネスまたはクリエイター)に、プログラムから画像・リール・ストーリーズ・カルーセルを公開できます。

投稿は**2段階**です。①「コンテナ」(container、投稿の下書きの入れ物)を作り、②それを公開します。素材(画像・動画)は、**Meta が取りに来られる公開 URL** に置いておく必要があります。

**利用料金**: 本ページで確認した公式文書の範囲では、Instagram API の利用料金の記載はありません。回数の上限で制御されています(⚪ 要確認)。

## 用語

| 用語 | 意味 |
|---|---|
| Instagram Platform(インスタグラム プラットフォーム) | Instagram の公式 API 群の総称 |
| professional account(プロアカウント) | ビジネスまたはクリエイターのアカウント。API の前提 |
| Meta App(Meta アプリ) | Meta for Developers に登録するあなたのプログラム。**Business タイプ**が必要 |
| App Dashboard(アプリダッシュボード) | Meta アプリの管理画面 |
| container(コンテナ) | 公開前の投稿の入れ物。ID が返る |
| `ig-id` / `IG_ID` | Instagram アカウントの ID |
| Standard Access / Advanced Access | 開発・自分用の標準アクセス / 他人のアカウントにも使う高度なアクセス(審査あり) |
| App Review(アプリ審査) | Meta がアプリの用途を審査する手続き |
| Business Verification(ビジネス認証) | 事業者であることの確認 |
| PPA(Page Publishing Authorization) | Facebook ページ側の公開の認可 |

## 準備の手順(✅ 公式の Get Started と Overview。画面名は変わる可能性 ⚪)

1. Instagram アカウントを**プロフェッショナルアカウント**にする([01-account-setup](../03-instagram/01-account-setup.md))。
2. Meta for Developers(developers.facebook.com)に登録し、**アプリを作成**する。種類は **Business** を選ぶ(既存アプリが Business でなければ新規作成 ✅)。
3. ログインの方式を選ぶ(下の §7)。Facebook ページを持たないなら **Instagram ログイン**、ページと連携しているなら **Facebook ログイン**。新規の統合には Unified Login が推奨されています(✅ Overview)。
4. App Dashboard の **Instagram > API setup with Instagram business login** で、対象アカウントの横の **Generate token** を押し、Instagram にログインしてトークンをコピーする(✅)。
5. トークンを `.env` に保存する([13-secrets-management](13-secrets-management.md))。
6. 最初の呼び出しで動作確認する: `GET https://graph.instagram.com/v26.0/me?fields=user_id,username`(✅。コードは [15-python-first-steps](15-python-first-steps.md))。

**アクセスレベル**(✅ Overview):

| レベル | 対象 | 条件 |
|---|---|---|
| Standard Access | アプリに役割を持つ人、開発中・テスト | 既定 |
| Advanced Access | **自分が所有・管理していない**アカウント | **App Review とビジネス認証**が必要 |

→ **自分のアカウントだけを扱うなら Standard Access で始められます**。代理運用ツールのように他人のアカウントを扱う場合は審査が必要です。

## 1. できること / できないこと(✅)

| 項目 | 内容 |
|---|---|
| 公開できる種類 | 画像、動画、**リール**、**ストーリーズ**、**カルーセル**(最大20件の画像・動画の混在) |
| 前提アカウント | Instagram **プロフェッショナル**アカウント。Facebook ページ側で **Page Publishing Authorization(PPA)** が必要になる場合があり、未完了だと公開できない |
| 素材の置き場 | Meta が URL を cURL で取得するため、**公開サーバー上**にあること(リールの再開可能アップロードを除く) |
| 非対応 | **ショッピングタグ、フィルター** |
| リール | **カルーセルには入れられない** |
| カルーセルの切り抜き | **最初の画像の比率**に合わせて全体が切り抜かれる(既定 1:1) |
| 代替テキスト | **`alt_text` フィールド(2025年3月24日追加)**。画像投稿のみ。リールとストーリーズは非対応 |
| AI 生成の自己申告 | **`is_ai_generated=true`**(2026年(皇紀2686年・令和8年)6月22日に追加 ✅ [changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md))。カルーセルでは親コンテナにのみ指定(子に付けるとエラー) |
| 有料パートナーシップ表示 | `is_paid_partnership`、`branded_content_sponsor_ids`(最大2)。**Facebook ログイン経由のみ**。ブランドコンテンツ表示が可能 |
| コラボ | `collaborators`(最大3、フィード画像・リール・カルーセル。ストーリーズ不可) |
| トライアルリール | `trial_params`(非フォロワーにのみ共有し、後で通常のリールに昇格) |

## 2. 画像の仕様(✅ 公式リファレンス)

| 項目 | 値 |
|---|---|
| 形式 | **JPEG のみ**(MPO・JPS などの拡張 JPEG は不可) |
| 容量 | 最大 **8MB** |
| 比率 | **4:5 〜 1.91:1** |
| 幅 | 最小 **320px**(小さいと拡大)、最大 **1440px**(大きいと縮小) |
| 色空間 | sRGB(他は変換) |

## 3. リールの仕様(✅ 公式リファレンス)

| 項目 | 値 |
|---|---|
| コンテナ | MOV または MP4(編集リストなし、`moov` atom がファイル先頭) |
| 映像 | HEVC または H.264、progressive、closed GOP、4:2:0 |
| 音声 | AAC、サンプルレート最大 48kHz、モノラルまたはステレオ、128kbps |
| フレームレート | **23〜60 FPS** |
| 最大横幅 | 1920px |
| 比率 | 0.01:1 〜 10:1(**9:16 を推奨**) |
| ビットレート | VBR、映像 最大 **25Mbps** |
| 長さ | **3秒以上、最大15分** |
| 容量 | 最大 **300MB** |
| カバー | JPEG、最大 8MB、sRGB。`cover_url` または `thumb_offset`(ミリ秒)で指定 |

> 以前の資料にあった「リール 100MB」は、公式リファレンス上は **300MB**。

## 4. 文字数・タグ(✅)

| 項目 | 上限 |
|---|---|
| キャプション | **2,200字** |
| ハッシュタグ | **30個** |
| @メンション | **20個** |
| カルーセルの子要素への caption / user_tags | **非対応** |

## 5. 公開の流れ(✅)

1. `POST /{ig-id}/media` — コンテナ作成(`image_url` または `video_url`、`media_type` = `REELS` / `STORIES` / `VIDEO`、`caption`、`alt_text` など)。
2. カルーセル: 子コンテナに `is_carousel_item=true`、親に `media_type=CAROUSEL` と `children`(最大20)。
3. 動画: コンテナの `status_code` を確認(**1分に1回、5分まで**を推奨)。`FINISHED` になったら公開可。`EXPIRED` は24時間以内に公開しなかった場合。
4. `POST /{ig-id}/media_publish` — `creation_id` を渡して公開。
5. 大きな動画は `upload_type=resumable` で `rupload.facebook.com` にアップロード(Facebook ログイン経由)。

## 6. 公開の上限(✅ ただし公式文書内で不一致)

| 記載 | 値 |
|---|---|
| 「Rate Limit」の節 | **100件/24時間**(ローリング)。カルーセルは1件 |
| 「カルーセルの制限」の節 | **50件/24時間** |

→ **同じ公式ページ内で 100 と 50 が併記されている**。実際の残量は `GET /{ig-id}/content_publishing_limit` で確認する。安全側として **50件以内**で設計する(通常運用では十分)。(#37)

## 7. ログインの種類と権限(✅)

| 方式 | トークン | ホスト | 権限 |
|---|---|---|---|
| Instagram API with Unified Login | Business Integration System User トークン | `graph.facebook.com`・`rupload.facebook.com` | `instagram_basic`、`instagram_content_publish` |
| Instagram API with **Instagram Login** | Instagram ユーザートークン | `graph.instagram.com` | `instagram_business_basic`、`instagram_business_content_publish` |
| Instagram API with **Facebook Login** | Facebook ページトークン | `graph.facebook.com`・`rupload.facebook.com` | `instagram_basic`、`instagram_content_publish`、`pages_read_engagement`(+ ビジネス権限の場合 `ads_management`・`ads_read`) |

- アクセスレベルは Standard Access / Advanced Access(後者はアプリ審査)。
- **パートナーシップ表示を使うなら Facebook ログイン経由**。

### トークンの有効期限(✅)

| 種類 | 有効期間 | 出典 |
|---|---|---|
| ビジネスログインで得た短期トークン | **1時間** | [Get Started](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md) |
| App Dashboard で発行したトークン | **60日**(長期) | 同上 |
| 長期トークンへの交換 | `GET https://graph.instagram.com/access_token`(`grant_type=ig_exchange_token`、`client_secret`、短期トークン)→ **60日** | [access_token](https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md) |

長期トークンの更新(refresh)の条件は今回の取得範囲では確認できていません(⚪ 要確認)。

### API 呼び出し全体の上限(✅ Overview)

- 一般のエンドポイント: **24時間の呼び出し数 = 4800 × インプレッション数**(インプレッション = 過去24時間にそのアカウントのコンテンツが画面に表示された回数)。
- 公開(publish)の上限は別枠(§6)。

## 具体例: 画像1枚を公開する(概念。動作は未検証)

```python
import os
import time
import requests

BASE = "https://graph.instagram.com/v26.0"     # Instagram ログインの場合
IG_ID = os.environ["IG_USER_ID"]
TOKEN = os.environ["IG_ACCESS_TOKEN"]

# ① コンテナを作る(画像は公開 URL・JPEG・8MB 以内)
c = requests.post(f"{BASE}/{IG_ID}/media", data={
    "image_url": "https://example.com/images/post_4x5.jpg",
    "caption": "今週の新メニューです #料理",
    "alt_text": "白い皿に盛られた野菜のパスタ",
    "access_token": TOKEN,
}, timeout=30)
c.raise_for_status()
creation_id = c.json()["id"]

# ② 公開する(動画なら status_code が FINISHED になるまで 1分に1回・5分まで待つ)
time.sleep(5)
p = requests.post(f"{BASE}/{IG_ID}/media_publish", data={
    "creation_id": creation_id,
    "access_token": TOKEN,
}, timeout=30)
print(p.status_code, p.json())
```

- 公開前に、残りの公開枠を `GET /{ig-id}/content_publishing_limit` で確認できます(✅ §6)。
- 画像の URL は例です。実際には自分の公開サーバーの URL を使います。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| コンテナ作成でエラー(画像) | PNG・8MB 超・比率が 4:5〜1.91:1 の外 | JPEG・8MB 以内・比率内で書き出す(§2) |
| 素材を取得できない | URL が非公開、ログインが必要、期限切れ | 誰でも開ける URL に置く。公開完了まで消さない |
| code 190 | トークンの期限切れ | 新しいトークンを取得([14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)) |
| code 10 / 200〜299 | 権限不足 | `instagram_business_content_publish` などを付けて再認可 |
| 動画が `EXPIRED` | 24時間以内に公開しなかった | コンテナを作り直す |
| 公開上限に達した | 24時間の上限 | `content_publishing_limit` で確認し、翌日に回す |
| カルーセルの子にキャプションを付けてエラー | 子要素は caption 非対応 | 親コンテナにだけ付ける |

## 8. 運用上の注意

1. 公式の予約機能(Meta Business Suite)で足りるなら API は不要。
2. 画像素材は**最初から JPEG・8MB 以内・幅1440px以内**で書き出す([export-presets](../01-common/export-presets.md))。PNG の図解は JPEG に変換する。
3. 自動投稿でも**広告・PR 表記**が必要。`is_paid_partnership` を使う([legal-compliance](../01-common/legal-compliance.md))。
4. **AI 生成画像は `is_ai_generated=true`**([ai-usage-policy](../01-common/ai-usage-policy.md))。
5. 公開 URL の素材は、公開処理が終わるまで消さない。

## 9. 公式で確認できなかった点(#37)

- 公開上限が 100 か 50 か(§6)。
- アプリ審査の具体的な要件と所要日数。
- Instagram の**インサイト取得 API** と、コメント管理 API の詳細(別ページ)。

## 関連ページ / 次に読む

- [04-threads-api](04-threads-api.md) — 同じ Meta の Threads
- [07-other-apis](07-other-apis.md) — Facebook ページの API
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)
- [03-media-specs](../03-instagram/03-media-specs.md) — アプリでの仕様

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/content-publishing.md | 2026-11-03 | 公開の流れ、上限、カルーセル |
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | 画像・リールの仕様、文字数 |
| https://developers.facebook.com/documentation/instagram-platform/overview.md | 2026-11-03 | ログインの種類、アクセスレベル、呼び出し上限 |
| https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md | 2026-11-03 | 準備、トークン発行、最初の呼び出し、有効期限 |
| https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md | 2026-11-03 | 長期トークンへの交換 |
| https://developers.facebook.com/docs/graph-api/guides/error-handling | 2026-11-03 | エラーコード |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | Meta の公式開発者文書を取得して ✅ に更新(既存) |
| 2026-11-03 | 初心者向けに加筆(概要・用語・準備の手順・アクセスレベル・トークンの有効期限・呼び出し上限・公開のコード例・よくある失敗・関連ページ・出典を追加) |
| 2026-11-03 | `is_ai_generated` の追加日を「2025年以降」から公式 changelog の 2026年6月22日に訂正 |
