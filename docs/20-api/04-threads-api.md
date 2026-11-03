---
title: Threads API
platform: threads
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.facebook.com/documentation/threads/get-started.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/troubleshooting.md
---

# Threads API

> **このページで分かること**: Threads の API で投稿するための準備、上限、メディアの仕様、公開の流れ、権限、トークン、最小コード、よくある失敗。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)

> 2026年(皇紀2686年・令和8年)11月3日に Meta の公式開発者文書(Markdown 版)を直接取得して確認しました(✅)。

## 概要

Threads API は、Meta のテキスト中心の SNS「Threads」に、プログラムから投稿・返信管理・インサイト取得をするための公式 API です。Instagram と同じく、**①コンテナを作る → ②公開する**の2段階で投稿します。

**利用料金**: 本ページで確認した公式文書の範囲では利用料金の記載はなく、回数の上限で制御されています(⚪ 要確認)。

## 用語

| 用語 | 意味 |
|---|---|
| Threads use case(Threads のユースケース) | Meta アプリ作成時に選ぶ用途。Threads API を使うにはこれを選ぶ |
| Threads app ID / secret | Threads 用のアプリ ID と秘密鍵(アプリには2組の ID と secret があり、**Threads 用の組**を使う ✅) |
| Threads Tester(テスター) | 開発中のアプリを試せる利用者の役割 |
| Authorization Window(許可画面) | 利用者が権限を許可する画面 |
| container(コンテナ) | 公開前の投稿の入れ物 |
| `creation_id` | 公開するときに指定するコンテナの ID |
| topic tag(トピックタグ) | Threads のハッシュタグに当たるもの |

## 準備の手順(✅ [Get Started](https://developers.facebook.com/documentation/threads/get-started.md)。画面名は変わる可能性 ⚪)

1. Meta for Developers で**アプリを作成**し、**Threads のユースケース**を選ぶ。
2. **Threads 用のアプリ ID と secret** を控える(`.env` へ。[13-secrets-management](13-secrets-management.md))。
3. App Dashboard の **App roles > Roles** から、自分のアカウントを **Threads Tester** として招待する。招待された側は Threads の**アカウント設定 > ウェブサイトのアクセス許可**で承認する。
4. 必要な権限を決める(§4)。`threads_basic` は**すべてのエンドポイントで必須**。
5. 許可画面を実装して認可コードを受け取り、**短期トークン**に交換する。
6. 短期トークンを**長期トークン**に交換し、期限前に更新する(下の表)。
7. 投稿用の画像・動画は、**公開サーバー**に置く(Meta が公開時に取得する)。

### トークンの有効期限(✅ 同ページ)

| 種類 | 有効期間 |
|---|---|
| 認可コード | 1時間 |
| 短期アクセストークン | **1時間**(長期に交換できる) |
| 長期アクセストークン | **60日**。期限前に `GET /refresh_access_token` で更新 |
| 許可(公開プロフィールの利用者) | 90日。長期トークンの更新でさらに90日延長。**非公開プロフィールは延長できず再許可が必要** |

## 1. 上限(✅ 公式の概要)

| 項目 | 値 |
|---|---|
| 投稿 | **250件/24時間**(ローリング)。**カルーセルは1件**。`threads_publish` の実行時に判定 |
| 返信 | **1,000件/24時間** |
| 削除 | **100件/24時間** |
| 位置情報検索 | **500件/24時間** |
| 残量確認 | `GET /{threads-user-id}/threads_publishing_limit`(`threads_basic` と `threads_content_publish` 権限が必要) |
| API 呼び出し全体の制限 | `4800 × インプレッション数`/24時間(最小インプレッション 10)。CPU 時間の制限もあり |

## 2. メディアの仕様(✅ 公式)

### 画像

| 項目 | 値 |
|---|---|
| 形式 | **JPEG・PNG**(公式にサポート) |
| 容量 | 最大 **8MB** |
| 比率 | 上限 **10:1** |
| 幅 | 最小 320px(拡大)、最大 1440px(縮小) |
| 色空間 | sRGB |

### 動画

| 項目 | 値 |
|---|---|
| コンテナ | MOV または MP4(編集リストなし、`moov` atom が先頭) |
| 映像 | HEVC または H.264、progressive、closed GOP、4:2:0 |
| 音声 | AAC、48kHz 以下、モノラル/ステレオ、128kbps |
| フレームレート | **23〜60 FPS** |
| 最大横幅 | 1920px |
| 比率 | 0.01:1 〜 10:1(**9:16 を推奨**) |
| ビットレート | VBR、映像 最大 **100Mbps** |
| 長さ | **最大5分(300秒)**、0秒超 |
| 容量 | 最大 **1GB** |

### その他

| 項目 | 値 |
|---|---|
| **テキスト投稿** | **500字まで** |
| カルーセル | **2〜20件** |

> 以前、二次資料にあった「PNG 3MB」「動画 500MB」は、公式の概要には**記載がなく**、公式値は上記。個別エンドポイントのリファレンスに追加の制限がある可能性あり(#34)。

## 3. 公開の流れ(✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md)。2026-11-03 に公式を取得して ⚪ から更新)

1. `POST /{threads-user-id}/threads` — コンテナ作成(テキスト、`image_url`/`video_url`、カルーセルの子要素)。
   - `media_type`(必須): `TEXT` / `IMAGE` / `VIDEO`(単体投稿で `CAROUSEL` は使わない)。
   - `text`: `TEXT` では必須。**500字まで**(絵文字は UTF-8 のバイト数で数えられる ✅)。
   - `image_url` / `video_url`: 公開サーバー上の URL。
2. `POST /{threads-user-id}/threads_publish` — 公開。動画は処理待ち。`creation_id` にコンテナ ID を指定。
   - コンテナ作成から公開まで**平均30秒ほど待つ**ことが推奨されています(✅)。
   - 動画の状態は**1分に1回、5分まで**確認。24時間以内に公開しないと `EXPIRED`(✅ [troubleshooting](https://developers.facebook.com/documentation/threads/troubleshooting.md))。

ベース URL: 公式の Posts ページは `https://graph.threads.com/v1.0/` を使っています(✅)。古い資料の `graph.threads.net` との関係は要確認(⚪)。

**トピックタグとリンク**(✅ Posts):

| 項目 | 値 |
|---|---|
| トピックタグ | **1投稿に1つ**(本文中のタグは最初の有効なものが使われる)。`topic_tag` パラメータは1〜50字、ピリオド・& は不可 |
| リンク | **5個以下**。2025年(皇紀2685年・令和7年)12月22日以降、6個以上は作成時に `THREADS_API__LINK_LIMIT_EXCEEDED` で失敗 |
| `link_attachment` | テキストのみの投稿で使える。本文中の URL と違う場合だけ追加の1個として数える |

## 4. 主な権限(✅ [Get Started](https://developers.facebook.com/documentation/threads/get-started.md)。2026-11-03 に ⚪ から更新)

`threads_basic`、`threads_content_publish`、`threads_manage_replies`、`threads_read_replies`、`threads_manage_insights`。

| 権限 | 用途 |
|---|---|
| `threads_basic` | **全エンドポイントで必須** |
| `threads_content_publish` | 投稿 |
| `threads_manage_replies` | 返信の管理(非表示など ⚪) |
| `threads_read_replies` | 返信の読み取り |
| `threads_manage_insights` | インサイトの取得 |

## 具体例: テキスト投稿(概念。動作は未検証)

```python
import os
import time
import requests

BASE = "https://graph.threads.com/v1.0"
USER_ID = os.environ["THREADS_USER_ID"]
TOKEN = os.environ["THREADS_ACCESS_TOKEN"]

c = requests.post(f"{BASE}/{USER_ID}/threads", data={
    "media_type": "TEXT",
    "text": "今日の営業時間は 11時〜20時です",
    "access_token": TOKEN,
}, timeout=30)
c.raise_for_status()

time.sleep(30)                      # 公式は平均30秒待つことを推奨
p = requests.post(f"{BASE}/{USER_ID}/threads_publish", data={
    "creation_id": c.json()["id"],
    "access_token": TOKEN,
}, timeout=30)
print(p.status_code, p.json())
```

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| どの呼び出しも権限エラー | `threads_basic` がない、テスター未承認 | 権限とテスターの承認を確認 |
| Instagram 用の app ID で失敗 | アプリの2組の ID を取り違えた | **Threads 用**の app ID と secret を使う |
| 公開で失敗(作成直後) | 処理が終わっていない | 30秒ほど待ってから公開 |
| `FAILED_DOWNLOADING_VIDEO` | 動画の URL を取得できない | 公開 URL か確認 |
| `INVALID_DURATION` など | 動画の仕様違反(最大5分) | §2 の仕様で書き出し直す |
| `THREADS_API__LINK_LIMIT_EXCEEDED` | リンクが6個以上 | 5個以下にする |
| 60日後に 401/190 | 長期トークンの期限切れ | 期限前に `refresh_access_token` |

## 5. 運用

- 公式の予約機能やサードパーティで足りるなら API は不要。
- 返信管理で荒れ対策の自動化が可能だが、**誤判定のリスク**に注意。
- インサイトの取得で週次レビューを自動化([analytics-kpi](../01-common/analytics-kpi.md))。

## 6. 公式で確認できなかった点(#34)

- ~~ハッシュタグ(トピックタグ)の個数の上限(二次資料は1つ)~~ → **1投稿に1つ**を公式で確認(✅ 2026-11-03、§3)。
- ~~公開の流れの詳細(上記 ⚪)~~ → 公式で確認(✅ 2026-11-03、§3)。
- 収益化プログラムの有無。
- ベース URL `graph.threads.net` と `graph.threads.com` の関係。

## 関連ページ / 次に読む

- [03-instagram-graph-api](03-instagram-graph-api.md) — 同じ Meta の Instagram
- [01-setup-and-posting](../07-threads/01-setup-and-posting.md) — アプリでの投稿
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | 上限、メディアの仕様 |
| https://developers.facebook.com/documentation/threads/get-started.md | 2026-11-03 | 準備の手順、権限、トークンの有効期限 |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | 公開の流れ、30秒の待機、トピックタグ1つ、リンク5個 |
| https://developers.facebook.com/documentation/threads/troubleshooting.md | 2026-11-03 | コンテナの状態、エラー |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | Meta の公式開発者文書を取得して ✅ に更新(既存) |
| 2026-11-03 | 初心者向けに加筆(概要・用語・準備の手順・トークンの有効期限・コード例・よくある失敗を追加)。§3 公開の流れと §4 権限を公式の Posts / Get Started で確認して ⚪ → ✅。トピックタグ1つ・リンク5個以下を ✅ で追記 |
