---
title: API 入門(はじめての人向け)
platform: common
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/make-your-first-request.md
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md
  - https://developers.google.com/youtube/v3/getting-started
---

# API 入門(はじめての人向け)

> **このページで分かること**: API とは何か、どう動くのか、リクエストとレスポンスの読み方、始めるまでに何が必要か。
>
> **対象**: プログラミング経験がほとんどない初心者  **先に読むページ**: なし(このページが入口です)。次に [01-concepts-and-security](01-concepts-and-security.md) へ。

## 概要

API(Application Programming Interface、アプリケーション・プログラミング・インターフェース)は、**プログラムからサービスを操作するための公式の窓口**です。人がアプリの画面をタップして投稿する代わりに、プログラムが「この文章を投稿して」とサービスに頼みます。

レストランにたとえると分かりやすくなります。

| レストラン | API の世界 |
|---|---|
| お客さん | あなたのプログラム |
| メニュー | API の仕様書(どんな注文ができるか) |
| 店員さんへの注文 | **リクエスト**(request、要求) |
| 運ばれてきた料理 | **レスポンス**(response、応答) |
| 会員証 | **アクセストークン**(access token、利用許可証) |
| 「1人1日3品まで」 | **レート制限**(rate limit、回数の上限) |

SNS 運用で API を使うと、次のようなことができます。

- 自分の投稿の数字(表示回数・いいね数)を毎週自動で表計算に集める。
- 決めた時刻に投稿する(予約投稿)。
- 新しいコメントが来たらチャットに通知する。

ただし、**公式アプリの予約投稿や分析画面で足りるなら API は不要**です。判断の基準は [10-benefits-of-api](10-benefits-of-api.md) を見てください。

## 用語

| 用語 | 意味 |
|---|---|
| API(公式の窓口) | プログラムからサービスを操作する入口 |
| Web API(ウェブ API) | インターネット経由(HTTP)で使う API。SNS の API はほぼこれ |
| endpoint(エンドポイント) | 操作ごとに決まった URL。例: 「投稿する」用の URL |
| HTTP method(HTTP メソッド) | 操作の種類。GET(取得)、POST(作成)、DELETE(削除)など |
| request(リクエスト) | プログラムからサービスへの「お願い」 |
| response(レスポンス) | サービスからの「返事」 |
| header(ヘッダー) | リクエスト・レスポンスに付く付帯情報。認証情報もここに入れる |
| body(ボディ、本文) | 送る・受け取るデータの本体 |
| JSON(ジェイソン) | データの書き方の一種。`{"名前": "値"}` の形 |
| status code(ステータスコード) | 結果を表す3桁の数字。200 は成功、401 は認証エラーなど |
| API key(API キー) | アプリを識別する鍵。**秘密情報** |
| access token(アクセストークン) | 「この人の代わりに操作してよい」という許可証。**秘密情報** |
| SDK(Software Development Kit、開発キット) | API を使いやすくする公式の部品集 |
| developer account(開発者アカウント) | API を使うために登録する専用アカウント |

## 仕組み: 1回の API 呼び出しで起きること

```
あなたのプログラム                        SNS のサーバー
     │  ① リクエスト                          │
     │  GET https://api.example.com/v1/me     │
     │  Authorization: Bearer (トークン)      │
     │ ─────────────────────────────────────▶ │
     │                                        │ ② トークンを確認
     │                                        │    回数の上限を確認
     │  ③ レスポンス                          │
     │  200 OK                                │
     │  {"data": {"id": "123", ...}}          │
     │ ◀───────────────────────────────────── │
```

1. プログラムが**エンドポイント**(URL)に**リクエスト**を送ります。
2. サーバーは、トークンが正しいか、権限(スコープ)が足りるか、回数の上限を超えていないかを確認します。
3. サーバーが**ステータスコード**と**データ(JSON)**を返します。

## リクエストの読み方

X API の公式入門ページにある例です(✅ [docs.x.com](https://docs.x.com/make-your-first-request.md))。

```bash
curl "https://api.x.com/2/users/by/username/xdevelopers" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

| 部分 | 意味 |
|---|---|
| `curl` | コマンドから HTTP リクエストを送る道具(Mac・Linux・Windows 10 以降に標準で入っていることが多い ⚪) |
| `https://api.x.com` | API のサーバー(ホスト) |
| `/2/` | API のバージョン(X API v2) |
| `users/by/username/xdevelopers` | 「ユーザー名 xdevelopers の情報をください」という**エンドポイント** |
| `-H "Authorization: Bearer ..."` | **ヘッダー**。トークンを渡して「私は許可を持っています」と示す |
| `$BEARER_TOKEN` | 環境変数(後述)に入れたトークン。**コマンドに直接書かない** |

メソッドを指定していないので GET(取得)です。投稿するときは POST を使い、ボディに JSON を入れます。

## レスポンスの読み方

成功すると、次のような JSON が返ります(形の例。値は架空)。

```json
{
  "data": {
    "id": "1234567890",
    "name": "Example",
    "username": "example"
  }
}
```

- 主なデータは `data` の中にあります(✅ X の入門ページ)。
- `{ }` はひとまとまりのデータ(オブジェクト)、`[ ]` は一覧(配列)、`"id": "..."` は「名前: 値」の組です。
- **ID は文字列として扱う**のが安全です。X の ID は桁が大きく、数値として扱うと誤差が出るプログラム言語があります(⚪)。

失敗すると、ステータスコードとエラーの説明が返ります。X の場合はエラーに `title`、`detail`、`type` が入ります(✅ [response-codes](https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md))。

## ステータスコードの早見表

| コード | 意味 | 初心者向けの言い換え | 確度 |
|---|---|---|---|
| 200 / 201 | OK / Created | 成功 | ⚪ |
| 400 | Bad Request | 注文の書き方が間違っている(必須項目の漏れ、JSON の誤り) | ✅ X |
| 401 | Unauthorized | 会員証(トークン)がない・期限切れ・間違い | ✅ X |
| 403 | Forbidden | 会員証は本物だが、その操作の権限がない | ✅ X |
| 404 | Not Found | 対象が存在しない(削除済みの投稿など) | ✅ X |
| 429 | Too Many Requests | 回数の上限を超えた。待ってから再試行 | ✅ X |
| 500 / 502 / 503 | サーバー側の問題 | 相手側の不調。時間をおいて再試行 | ✅ X |

詳しい対処は [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)。

## 始めるまでの全体の流れ

| 順番 | やること | 説明 | 詳しいページ |
|---|---|---|---|
| 1 | 目的を決める | 「週次の数字を集める」など1つに絞る | [10-benefits-of-api](10-benefits-of-api.md) |
| 2 | 規約を読む | 自動化してよい範囲を確認 | [08-automation-and-tools](08-automation-and-tools.md) |
| 3 | 開発者アカウントを作る | X は Developer Console、Meta は Meta for Developers、Google は Google Cloud | 各サービスのページ |
| 4 | アプリを登録する | 「アプリ」はあなたのプログラムの登録名。ここで鍵が発行される | 同上 |
| 5 | 鍵を安全に保管する | `.env` ファイル+`.gitignore`。**絶対にコミットしない** | [13-secrets-management](13-secrets-management.md) |
| 6 | 認証を通す | OAuth 2.0 でアクセストークンを得る | [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) |
| 7 | まず「読み取り」を1回試す | 自分のプロフィールを取得するなど | [15-python-first-steps](15-python-first-steps.md) |
| 8 | 上限と料金を確認する | レート制限・クォータ・従量課金 | 各サービスのページ |

X の場合、開発者登録は「console.x.com に X アカウントでログイン → 開発者契約とポリシーに同意 → 使い道を入力 → New App でアプリ作成」の順です(✅ [getting-access](https://docs.x.com/x-api/getting-started/getting-access.md))。**鍵(認証情報)は一度しか表示されない**ため、すぐにパスワードマネージャーなどに保存します(✅ 同ページ)。

## レート制限と料金の考え方

- **レート制限**: 「15分に100回まで」のような回数の上限です。超えると 429 が返ります。サービス・エンドポイントごとに違います。
- **クォータ**(quota、割り当て量): YouTube のように「1日10,000ユニット」の形で決まるもの(✅ [YouTube](https://developers.google.com/youtube/v3/getting-started))。
- **料金**: X API は使った分だけ払う**従量課金**です(✅ [02-x-api](02-x-api.md))。Instagram・Threads・YouTube の API は、本ページの確認範囲では利用料金の記載はなく、上限で制御されています(⚪ 要確認)。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 鍵をコードに直接書いて GitHub に公開してしまった | すぐに鍵を**失効・再発行**する。履歴の削除だけでは不十分([13-secrets-management](13-secrets-management.md)) |
| いきなり自動投稿から作り始めた | まず**読み取り**だけで練習する。投稿は誤爆の影響が大きい |
| 401 が出て原因が分からない | トークンの貼り間違い、期限切れ、再発行で古い鍵が無効になった、の順に確認 |
| 403 が出る | アプリの権限(読み取りのみ/書き込み可)とスコープを確認 |
| 料金が想定より高い | 支出上限(spending limit)を先に設定する(X) |

## 注意点

- 本ページのコードは**仕組みの説明用**です。実際の値は各サービスの公式文書で確認してください。
- このリポジトリは public です。**キー・トークン・パスワードを書かない**でください(例は `YOUR_API_KEY` のようなプレースホルダのみ)。

## チェックリスト

- [ ] API でやりたいことを1つに絞った
- [ ] 公式の予約・分析機能で足りないことを確認した
- [ ] 開発者規約・自動化ルールを読んだ
- [ ] 鍵の保管場所(パスワードマネージャー、`.env`)を決めた
- [ ] `.gitignore` に `.env` を入れた
- [ ] 最初の1回は読み取り(GET)で試す

## 関連ページ / 次に読む

1. [01-concepts-and-security](01-concepts-and-security.md) — 基本概念とセキュリティの全体像
2. [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) — 認証・トークン・スコープ
3. [13-secrets-management](13-secrets-management.md) — 鍵の安全な保管
4. [15-python-first-steps](15-python-first-steps.md) — Python で最初の1回
5. [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) — エラーの対処
6. 用語全般は [glossary](../00-meta/glossary.md)、初心者向け用語は [basic-terms-explained](../01-common/basic-terms-explained.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/make-your-first-request.md | 2026-11-03 | 最初のリクエスト例、`data` フィールド |
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 開発者登録の手順、認証情報は一度だけ表示 |
| https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md | 2026-11-03 | ステータスコードとエラー形式 |
| https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md | 2026-11-03 | Instagram の最初の呼び出し例 |
| https://developers.google.com/youtube/v3/getting-started | 2026-11-03 | YouTube のクォータの考え方 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(初心者向けの API 入門。仕組み、リクエスト/レスポンスの読み方、始める手順、用語表) |
