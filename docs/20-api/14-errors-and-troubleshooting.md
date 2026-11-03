---
title: よくある API エラーと対処(401・403・429 ほか)
platform: common
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md
  - https://docs.x.com/make-your-first-request.md
  - https://developers.facebook.com/docs/graph-api/guides/error-handling
  - https://developers.facebook.com/documentation/threads/troubleshooting.md
  - https://developers.google.com/youtube/v3/determine_quota_cost
  - https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit
  - https://developers.line.biz/ja/reference/messaging-api/
---

# よくある API エラーと対処(401・403・429 ほか)

> **このページで分かること**: エラーの番号(ステータスコード)の意味、サービス別のエラーの読み方、再試行(リトライ)の正しいやり方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

API のエラーは「**誰が悪いか**」で大きく2つに分かれます。

| 種類 | 番号 | 意味 | 再試行してよいか |
|---|---|---|---|
| こちら側の問題 | **4xx**(400 番台) | 書き方・鍵・権限・回数の問題 | **原則しない**(直してから)。ただし 429 は待てば通る |
| 相手側の問題 | **5xx**(500 番台) | サーバーの不調・混雑 | 時間をおいて数回まで |

エラーが出たら、まず**ステータスコード**、次に**エラー本文(JSON)のメッセージ**を読みます。

## 用語

| 用語 | 意味 |
|---|---|
| status code(ステータスコード) | 結果を表す3桁の番号 |
| error body(エラー本文) | エラーの詳しい説明が入った JSON |
| retry(リトライ、再試行) | 失敗した呼び出しをもう一度送ること |
| exponential backoff(指数バックオフ) | 再試行の待ち時間を 2秒→4秒→8秒…と倍に増やす方法 |
| rate limit(レート制限) | 一定時間あたりの回数の上限 |
| quota(クォータ) | 1日などの期間に使える量の上限 |
| idempotency(冪等性、べきとうせい) | 同じ操作を何度送っても結果が1回分になる性質。二重投稿の防止に関係 |

## ステータスコード別の対処(X の公式表をもとに整理)

| コード | 意味 | よくある原因 | 対処 | 確度 |
|---|---|---|---|---|
| **400** | Bad Request | JSON の誤り、必須パラメータの漏れ、値の型の間違い | JSON と必須項目を確認。特殊文字をエスケープ | ✅ |
| **401** | Unauthorized | トークンがない・間違い・期限切れ、**再発行して古い鍵が無効** | 認証方式がエンドポイントに合うか、`Authorization` ヘッダーの形式、再発行の有無を確認 | ✅ |
| **403** | Forbidden | 認証は通ったが権限がない(スコープ不足、アプリの登録・アクセスレベル不足、非公開の対象) | スコープとアプリの権限を確認。**ユーザー認証が必要なエンドポイント**に App-only で呼んでいないか | ✅ |
| **404** | Not Found | 対象が存在しない・削除済み | ID と URL を確認 | ✅ |
| **409** | Conflict | (X のフィルタードストリーム)ルールがない | ルールを1つ以上追加 | ✅ |
| **429** | Too Many Requests | レート制限・利用上限の超過 | `x-rate-limit-reset` を見て待つ。指数バックオフ、キャッシュ、時間分散 | ✅ |
| **500 / 502 / 503** | サーバー側の失敗・過負荷 | 相手側の障害 | 待って再試行。公式のステータスページを確認 | ✅ |

出典: [X response codes](https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md)。他のサービスでも番号の意味はおおむね同じです(HTTP の標準 ⚪)。

## サービス別のエラーの読み方

### X

エラー本文に `title`、`detail`、`type` が入ります(✅)。`type` の末尾で原因が分かります。

| `type` の末尾 | 意味 |
|---|---|
| `invalid-request` | リクエストの形式・パラメータの誤り |
| `resource-not-found` | 投稿・ユーザーなどが存在しない |
| `not-authorized-for-resource` | 非公開・保護された内容へのアクセス |
| `client-forbidden` | アプリが必要な登録・アクセスを持っていない |
| `usage-capped` | 利用上限の超過 |
| `rate-limit-exceeded` | レート制限の超過 |

X 固有の 403 の例: 通常アカウントで上限より長い動画を投稿すると `This user is not allowed to post a video longer than N minutes.`(✅ [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md))。**呼び出されていない投稿への返信**も API では制限されています(✅ [02-x-api](02-x-api.md) §3)。

### Meta(Instagram・Facebook・Threads)

エラーは `error` の中に `message`、`type`(例 `OAuthException`)、`code`、`error_subcode`、`fbtrace_id` が入ります(✅ [Graph API error handling](https://developers.facebook.com/docs/graph-api/guides/error-handling))。問い合わせのときは `fbtrace_id` を伝えます(すぐに期限が切れる ✅)。

| code | 名前 | 対処 |
|---|---|---|
| 190 | アクセストークンの期限切れ | 新しいトークンを取得 |
| 102 | API Session | 新しいトークンを取得(サブコードがあればそれを確認) |
| 4 | API Too Many Calls(アプリ単位) | 待って再試行、呼び出し量を減らす |
| 17 | API User Too Many Calls(ユーザー単位) | 待って再試行、呼び出し量を減らす |
| 341 | Application limit reached | 待って再試行、呼び出し量を減らす |
| 10、200〜299 | 権限の不足 | 不足している権限を申請・再認可 |
| 368 | ポリシー違反による一時的なブロック | 待って再試行(内容も見直す) |
| 506 | 重複投稿 | 内容を変えて再試行 |

認証のサブコードの例: 463(期限切れ)、467(無効なトークン)、460(パスワード変更)、458(アプリがインストールされていない → 再認証)(✅ 同ページ)。

Threads・Instagram の**動画コンテナ**のエラー(✅ [Threads troubleshooting](https://developers.facebook.com/documentation/threads/troubleshooting.md)):

| 状態・エラー | 意味 | 対処 |
|---|---|---|
| `IN_PROGRESS` | まだ処理中 | 1分に1回、5分まで確認 |
| `EXPIRED` | 24時間以内に公開しなかった | コンテナを作り直す |
| `FAILED_DOWNLOADING_VIDEO` | 動画を取得できなかった | URL が公開されているか、期限付き URL が切れていないか |
| `INVALID_ASPEC_RATIO`、`INVALID_DURATION`、`INVALID_FRAME_RATE` など | 仕様違反 | 書き出し設定を直す([export-presets](../01-common/export-presets.md)) |

### YouTube

- 1日のクォータ(既定 10,000 ユニット)を使い切ると、翌日まで使えません。**リセットは太平洋時間(PT)の午前0時**です(✅ [quota](https://developers.google.com/youtube/v3/determine_quota_cost))。日本時間では夏時間の時期で16時、それ以外は17時です(⚪ 換算)。
- **失敗したリクエストもクォータを最低1消費**します(✅ 同ページ)。エラーの再試行ループで枯渇しないようにします。
- アップロード数の上限に達すると `uploadLimitExceeded`(400)が返ります(✅ [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert))。

### TikTok

- レート制限は**1分間のスライディングウィンドウ**で数えられ、超えると HTTP 429 と `rate_limit_exceeded` が返ります(✅ [rate limit](https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit))。
- 投稿前に `creator_info` で「今は投稿できない」と返ったら、投稿を中止して利用者に後で再試行するよう伝えます(✅ [06-tiktok-api](06-tiktok-api.md))。

### LINE

| コード | LINE の説明 | 確度 |
|---|---|---|
| 401 | 有効なチャネルアクセストークンが指定されていない | ✅ |
| 403 | 権限がない。契約中のプランやアカウントの権限を確認 | ✅ |
| 429 | レート制限の超過(トークンバケット方式で徐々に回復) | ✅ |

当月の送信上限を超えた場合もエラーになり、メッセージは送られません(✅ [07-other-apis](07-other-apis.md))。

## 具体例: 安全な再試行(Python)

```python
import time
import requests

RETRY_STATUS = {429, 500, 502, 503}

def call_with_retry(method, url, max_tries=4, **kwargs):
    """429 と 5xx だけを、待ち時間を増やしながら再試行する。"""
    wait = 2
    for attempt in range(1, max_tries + 1):
        r = requests.request(method, url, timeout=30, **kwargs)
        if r.status_code not in RETRY_STATUS:
            return r                       # 成功、または直すべき 4xx
        reset = r.headers.get("x-rate-limit-reset")   # X の場合(UNIX 時刻)
        if r.status_code == 429 and reset:
            wait = max(1, int(reset) - int(time.time()))
        print(f"{r.status_code}: {wait}秒待って再試行({attempt}/{max_tries})")
        time.sleep(wait)
        wait *= 2
    return r
```

- **投稿(POST)の再試行は慎重に**。タイムアウトでも実は投稿されていることがあります(⚪)。再試行の前に、投稿済みかどうかを確認します([09-architecture-patterns](09-architecture-patterns.md) の冪等性)。
- `print` にトークンやヘッダー全体を出さない([13-secrets-management](13-secrets-management.md))。

## トラブルシューティングの手順

1. **ステータスコード**を見る(4xx か 5xx か)。
2. **エラー本文**の `detail` / `message` を読む(英語なら翻訳してよい。ただし**鍵の部分を隠して**から)。
3. 401 → トークンの期限・貼り間違い・再発行の有無。
4. 403 → スコープ、アプリの権限設定、アクセスレベル(審査)、サービスの制限(X の返信制限など)。
5. 429 → ヘッダーで回復時刻を見て待つ。呼び出し回数を減らす設計に。
6. 5xx → 公式のステータスページを確認し、時間をおく。
7. 直らなければ、公式の開発者フォーラムに**鍵を伏せて**質問する。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 429 のたびにすぐ再送して、さらに制限が長引く | 待ち時間を守る。指数バックオフ |
| 400 を何度も再試行してクォータを無駄にした(YouTube) | 4xx は再試行しない。原因を直す |
| タイムアウト後に再送して二重投稿 | 投稿前後で ID を記録し、再送前に確認 |
| エラーの全文を SNS やチャットに貼った | トークンや個人情報が含まれていないか確認してから共有 |

## 注意点

- エラーの文言・コードは変わることがあります。最新は各公式文書で確認してください。
- 上限ぎりぎりで運用しない。目安は**上限の半分以内**([09-architecture-patterns](09-architecture-patterns.md))。

## 関連ページ / 次に読む

- [01-concepts-and-security](01-concepts-and-security.md) — レート制限・リトライの基本
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) — 401・403 の背景にある認証
- [15-python-first-steps](15-python-first-steps.md) — エラー処理を含む最小コード

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md | 2026-11-03 | X のステータスコード表とエラー `type` |
| https://docs.x.com/make-your-first-request.md | 2026-11-03 | 401・403 のトラブルシューティング |
| https://developers.facebook.com/docs/graph-api/guides/error-handling | 2026-11-03 | Meta のエラー形式とコード表 |
| https://developers.facebook.com/documentation/threads/troubleshooting.md | 2026-11-03 | Threads のコンテナ状態・メディアのエラー |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | クォータのリセット時刻、失敗も最低1消費 |
| https://developers.google.com/youtube/v3/docs/videos/insert | 2026-11-03 | `uploadLimitExceeded` |
| https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit | 2026-11-03 | 1分間のスライディングウィンドウ、429 |
| https://developers.line.biz/ja/reference/messaging-api/ | 2026-11-03 | LINE のステータスコード、レート制限の仕組み |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(ステータスコード別の対処、X・Meta・YouTube・TikTok・LINE のエラーの読み方、再試行のコード例) |
