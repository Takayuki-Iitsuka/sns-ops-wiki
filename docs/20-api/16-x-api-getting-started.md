---
title: X API をはじめる(登録から最初の投稿まで)
platform: x
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://docs.x.com/make-your-first-request.md
  - https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://docs.x.com/xdks/python/install.md
  - https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md
---

# X API をはじめる(登録から最初の投稿まで)

> **このページで分かること**: X の開発者登録、アプリの作成、4種類の認証情報の違い、費用の上限設定、最初の読み取りと投稿のコード。
>
> **対象**: 初心者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[13-secrets-management](13-secrets-management.md)。料金・移行の全体は [02-x-api](02-x-api.md)

> 2026年(皇紀2686年・令和8年)11月3日に docs.x.com の公式 Markdown を取得して確認しました(✅)。画面の名称・配置は変わる可能性があります(⚪)。

## 概要

X API を使うには、**Developer Console**(開発者コンソール、https://console.x.com)で登録し、**アプリ**を作り、発行された認証情報で API を呼びます。X API は**従量課金**なので、最初に**支出の上限**を決めてから始めます。

## 用語

| 用語 | 意味 |
|---|---|
| Developer Console(開発者コンソール) | X API の登録・アプリ管理・請求の画面 |
| App(アプリ) | あなたのプログラムの登録単位。認証情報はアプリごとに発行される |
| API Key & Secret | アプリの識別と、OAuth 1.0a の署名・トークン生成に使う |
| Bearer Token | アプリ専用認証(App-only)。公開データの読み取り用 |
| Access Token & Secret | OAuth 1.0a で**自分のアカウントとして**操作するための鍵 |
| Client ID & Secret | OAuth 2.0 でユーザーとして操作するための鍵 |
| credit(クレジット) | 前払いの残高。使った分が引かれる |
| auto-recharge(自動チャージ) | 残高が減ったら自動で補充する設定 |
| spending limit(支出上限) | 請求期間ごとの使用額の上限 |

## 手順

### 1. 開発者登録とアプリ作成(✅ [getting-access](https://docs.x.com/x-api/getting-started/getting-access.md))

1. https://console.x.com を開き、**X アカウントでサインイン**する。
2. **開発者契約とポリシー**(Developer Agreement and Policy)を読み、同意する。
3. API の**使い道**など基本情報を入力する。
4. ダッシュボードで **New App** を押し、アプリの名前・説明・用途を入力する。
5. 認証情報が生成される。**一度しか表示されない**ので、すぐにパスワードマネージャーなどへ保存する。なくしたら再発行(古いものは無効になる)。

**アプリの名前と説明の例**(汎用例): 名前「my-weekly-report」、説明「自分のアカウントの投稿の成績を週1回取得し、表計算にまとめる。投稿や他人のデータの収集は行わない」。正直かつ具体的に書きます(⚪)。

### 2. 認証情報の使い分け(✅ 同ページ)

| 認証情報 | 何ができる | 使う場面 |
|---|---|---|
| Bearer Token | 公開データの読み取り(アプリとして) | 公開プロフィール・公開投稿の取得 |
| Client ID & Secret | OAuth 2.0 でユーザーの代わりに操作 | **投稿・自分のデータの読み取り(推奨)** |
| Access Token & Secret | OAuth 1.0a で自分のアカウントとして操作 | 従来方式。OAuth 2.0 へのトークン交換が可能([02-x-api](02-x-api.md) §3) |
| API Key & Secret | アプリの識別、OAuth 1.0a の署名 | 上と組み合わせて使う |

**投稿には「ユーザーとしての認証」が必要**です。Bearer Token(App-only)で投稿しようとすると権限エラーになります(✅ 403 の原因として「ユーザーコンテキストの認証が必要なエンドポイント」)。

### 3. 費用の上限を先に決める(✅ [pricing](https://docs.x.com/x-api/getting-started/pricing.md))

| 設定 | 内容 |
|---|---|
| 支出上限 | 請求期間ごとの上限額。**達するとその期間はリクエストがブロック**される |
| 自動チャージ | 補充額としきい値を設定。残高がしきい値を下回った最初の時点で実行。5分に最大1回。既定の支払い方法の保存が必要 |
| 無料クレジット | 初めての支払いカードの保存と初回のクレジット購入で **$20**。初回の自動チャージに最大 **$50** のマッチ |

### 4. OAuth 2.0 の準備(✅ [authorization-code](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md))

1. アプリ設定で OAuth 2.0 を使えるようにし、**callback URL(リダイレクト先)** を登録する(手元で試すなら `http://127.0.0.1:...` のような URL を使う例が多い ⚪)。
2. アプリの種類を選ぶ: 自分の PC やサーバーで動く bot は **confidential client**(client secret を持てる)。
3. スコープを決める: 投稿だけなら `tweet.read`、`tweet.write`、`users.read`、定期実行なら `offline.access` を追加。画像を付けるなら `media.write`。
4. 認可 → 認可コード(**30秒**で失効)→ トークン交換 → アクセストークン(**2時間**)。

流れの詳しい説明は [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)。公式の Python SDK(XDK)は `pip install xdk`(Python 3.8 以上 ✅ [install](https://docs.x.com/xdks/python/install.md))で入り、認証の処理を助けてくれます。

## 具体例

### 例 1: 読み取り(Bearer Token)

[15-python-first-steps](15-python-first-steps.md) の「具体例 1」を参照してください。公式の最初のリクエストと同じ `GET /2/users/by/username/{username}` です(✅)。

### 例 2: テキストだけの投稿(OAuth 2.0 のユーザートークン)

[02-x-api](02-x-api.md) §10 と同じ内容に、エラー時の表示を加えたものです(概念。動作は未検証)。

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.environ["X_USER_ACCESS_TOKEN"]     # tweet.write を含む OAuth 2.0 トークン

r = requests.post(
    "https://api.x.com/2/tweets",
    headers={"Authorization": f"Bearer {token}"},
    json={"text": "API からのテスト投稿です"},   # URL を含めると単価が上がる
    timeout=30,
)
if r.ok:
    print("投稿 ID:", r.json()["data"]["id"])   # ID は文字列で保存する
else:
    print(r.status_code, r.json())             # 401/403/429 は 14-errors を参照
```

### 例 3: 費用の見積もり(✅ 単価は pricing)

| 使い方 | 月の回数 | 計算 | 月額 |
|---|---|---|---|
| テキスト投稿を毎日1回 | 30 | 30 × $0.015 | $0.45 |
| URL 付き投稿を毎日1回 | 30 | 30 × $0.200 | $6.00 |
| 自分の投稿を毎週100件取得(Owned Reads) | 400 | 400 × $0.001 | $0.40 |
| 他人のユーザー情報を毎日10件取得 | 300 | 300 × $0.010 | $3.00 |

→ **URL 付き投稿が費用の大半**になりやすいことが分かります。為替や税の扱いは請求画面で確認してください([06-cost-planning](../40-pricing/06-cost-planning.md))。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| 認証情報を保存し忘れた | 一度しか表示されない | 再発行する(古いものは無効) |
| 投稿で 403 | Bearer Token で投稿している / `tweet.write` がない | OAuth 2.0 のユーザートークンを使い、スコープを確認 |
| 2時間後に 401 | アクセストークンの期限切れ | `offline.access` でリフレッシュトークンを得て更新 |
| 返信の投稿で 403 | 2026年2月からの制限(呼び出されていない投稿への返信は不可) | 仕様として受け入れる([02-x-api](02-x-api.md) §3) |
| リクエストが急に全部止まった | 支出上限に到達、または残高不足 | Developer Console で残高と上限を確認 |
| 自動いいね・フォローができない | self-serve の API から削除済み | 仕様。手動で行う |

## 注意点

- 自動化のルール(スパム・なりすまし)を守る([08-automation-and-tools](08-automation-and-tools.md))。
- 有料の PR 投稿は `paid_partnership` を付ける([02-x-api](02-x-api.md) §3、[legal-compliance](../01-common/legal-compliance.md))。
- 支払い・請求の詳細や税の扱いは公式で要確認(⚪ #36)。

## チェックリスト

- [ ] Developer Console で開発者契約に同意し、アプリを作った
- [ ] 認証情報をパスワードマネージャーに保存した
- [ ] `.env` と `.gitignore` を用意した
- [ ] 支出上限を設定した
- [ ] スコープを最小限にした(`offline.access` は定期実行時のみ)
- [ ] 読み取りで動作確認してから投稿を試した

## 関連ページ / 次に読む

- [02-x-api](02-x-api.md) — 料金表・2026年の変更・v1.1 からの移行
- [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md) — 画像・動画とレート制限
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)
- [01-x-and-grok](../40-pricing/01-x-and-grok.md) — X の料金プラン全体

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 登録手順、4種類の認証情報、一度だけ表示、保管の推奨 |
| https://docs.x.com/make-your-first-request.md | 2026-11-03 | Bearer Token の取得場所、最初のリクエスト |
| https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md | 2026-11-03 | 認可コード30秒、トークン2時間、スコープ |
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | 単価、支出上限、自動チャージ、無料クレジット |
| https://docs.x.com/xdks/python/install.md | 2026-11-03 | XDK のインストール |
| https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md | 2026-11-03 | 403 の原因 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(02-x-api から初心者向けの導入部分を独立。登録手順、認証情報の使い分け、費用上限、投稿のコード例、費用の見積もり) |
