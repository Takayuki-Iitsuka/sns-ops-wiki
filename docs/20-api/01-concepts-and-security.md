---
title: API の基本概念とセキュリティ
platform: common
topic: api
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md
  - https://developers.google.com/youtube/v3/determine_quota_cost
  - https://developers.line.biz/ja/docs/messaging-api/verify-webhook-signature/
---

# API の基本概念とセキュリティ

> **このページで分かること**: API を安全に使うための全体像(認証・トークン管理・レート制限・リトライ・ログ・規約)。各テーマの詳しいページへの入口。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

API を使うときに守るべきことは、大きく4つです。

1. **正しく許可を得る**(認証・認可。OAuth 2.0 とスコープ)→ [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)
2. **鍵を漏らさない**(トークン・キーの管理)→ [13-secrets-management](13-secrets-management.md)
3. **上限を守る**(レート制限・クォータ・料金)→ [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)
4. **規約を守る**(自動化のルール、個人情報)→ [08-automation-and-tools](08-automation-and-tools.md)

このページは、これらを1ページで見渡すための要約です。

## 用語

| 用語 | 意味 |
|---|---|
| OAuth 2.0 | 他のサービスの権限を安全に委譲する仕組み。パスワードを渡さずトークンで操作 |
| PKCE(Proof Key for Code Exchange) | 認可コードの横取りを防ぐ拡張。公開クライアントで推奨 |
| Bearer token(ベアラートークン) | 持っていれば使えるトークン。**漏れたら悪用される** |
| Access token / Refresh token | 短期の操作用トークン / 更新用の長期トークン |
| Scope(スコープ、権限範囲) | トークンで許可する操作(例: 投稿、読み取り) |
| API key / secret | アプリを識別する鍵。**秘密情報** |
| Webhook(ウェブフック) | サービス側から通知を受け取る URL |
| Rate limit(レート制限) | 一定時間あたりの呼び出し上限 |
| Quota(クォータ) | 1日あたりの利用量の上限(YouTube など) |
| Idempotency(冪等性) | 同じ操作を再実行しても結果が変わらない性質 |
| Endpoint(エンドポイント) | 操作ごとの URL(例: `POST /2/tweets`) |
| Signature verification(署名の検証) | Webhook が本物のサービスから届いたかを確かめる処理 |

## 認証の基本フロー

1. 開発者ポータルでアプリを作成(X、Meta、Google Cloud、TikTok など)。
2. 必要な**スコープだけ**を申請。
3. 利用者(自分のアカウント)が OAuth で許可。
4. アクセストークンを取得し、API 呼び出しに使う。
5. 期限が来たらリフレッシュトークンで更新。
6. 一部のサービスは**アプリ審査**(Meta、TikTok、YouTube の監査)が必要。

有効期限の例: X のアクセストークンは既定で **2時間**、リフレッシュトークンは `offline.access` スコープを付けたときだけ発行(✅ [X](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md))。サービス別の一覧は [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)。

## トークン・鍵の管理(必須)

1. **public リポジトリには絶対に書かない**(ソース、設定、ログ、スクリーンショット、Issue/PR も)。このリポジトリは検査スクリプトで秘密情報らしき文字列を検出するが、**万能ではない**。
2. 保管: 環境変数、シークレット管理(GitHub Actions の Secrets、パスワードマネージャー、クラウドのシークレット管理)。
3. 権限は最小(読み取りのみで足りるなら書き込みを付けない)。
4. 定期的に**ローテーション**(再発行)。不要になったら失効。
5. 漏えいが疑われたら**直ちに失効**し、再発行、履歴の調査。コミット履歴に出たら鍵を無効化(履歴の書き換えだけでは不十分)。
6. ログにトークンを出さない。エラーメッセージのマスク。
7. 端末の保護(ディスク暗号化、画面ロック)。

X の公式文書も「認証情報は一度しか表示されない」「環境変数を使う」「`.gitignore` に入れる」「定期的に再発行」を勧めています(✅ [getting-access](https://docs.x.com/x-api/getting-started/getting-access.md))。具体的な手順(`.env` の作り方など)は [13-secrets-management](13-secrets-management.md)。

## レート制限・リトライ

| 状況 | 対応 |
|---|---|
| HTTP 429 | 待機してから再試行(`Retry-After` や `x-rate-limit-reset` ヘッダーに従う) |
| HTTP 5xx | 指数バックオフ(2秒、4秒、8秒…)で最大数回 |
| 4xx(入力不正) | リトライしない。原因を修正 |
| 投稿の重複 | 投稿前に**既存投稿を確認**、または内部の投稿 ID を記録 |

- X は 429 の対処として「`x-rate-limit-reset` を読む、指数バックオフ、キャッシュ、時間分散」を挙げています(✅ [response codes](https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md))。
- YouTube は**失敗したリクエストもクォータを最低1消費**します(✅ [quota](https://developers.google.com/youtube/v3/determine_quota_cost))。無駄な再試行はクォータを減らします。
- 再試行のコード例は [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)。

## Webhook の安全な受け取り

Webhook は「何か起きたらサービスがあなたの URL に知らせる」仕組みです(例: LINE で友だち追加、X Activity API のイベント)。

1. 受け取る URL は HTTPS にする(⚪)。
2. **署名を検証**してから処理する。LINE は、リクエストヘッダーの署名を検証して「LINE プラットフォームから送られたか」「改ざんされていないか」を確認するよう求めています(✅ [LINE](https://developers.line.biz/ja/docs/messaging-api/verify-webhook-signature/))。
3. 同じイベントが2回届いても困らないようにする(冪等性 ⚪)。

## ログと監査

- 何を・いつ・どのアカウントに投稿したかを記録(トークンは記録しない)。
- 失敗の通知(メール/チャット)。

## 法令・規約

- 開発者向けの利用規約・ポリシーを守る(データの保存期間、再配布の禁止など)。
- 利用者のデータ(他人のアカウントの情報)を扱う場合は個人情報保護([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。
- 広告・PR の表記は API 投稿でも必要([legal-compliance](../01-common/legal-compliance.md))。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 「とりあえず全部の権限」でトークンを作った | 必要なスコープだけで作り直す |
| 429 で即座に再送を繰り返した | 待ち時間を守り、指数バックオフにする |
| Webhook の署名を検証せずに処理した | 偽のリクエストで誤動作しうる。必ず検証 |
| ログにリクエスト全体を出していた | ヘッダー(トークン)を伏せる |

## チェックリスト

- [ ] スコープは最小限
- [ ] 鍵は `.env` / シークレット管理にあり、コードとリポジトリにない
- [ ] トークンの期限切れ前の更新と、失敗時の通知がある
- [ ] 429・5xx だけを、待ち時間を増やしながら再試行する
- [ ] Webhook の署名を検証している
- [ ] 投稿ログ(トークンなし)を残している

## 関連ページ / 次に読む

- [00-api-for-beginners](00-api-for-beginners.md) — API 入門
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) — 認証
- [13-secrets-management](13-secrets-management.md) — 鍵の保管
- [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) — エラーとリトライ
- [account-security](../01-common/account-security.md) — アカウントの守り方

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md | 2026-11-03 | X のトークン有効期限 |
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 認証情報の保管の推奨 |
| https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md | 2026-11-03 | 429 の対処 |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | 失敗もクォータを消費 |
| https://developers.line.biz/ja/docs/messaging-api/verify-webhook-signature/ | 2026-11-03 | Webhook の署名検証(Messaging API リファレンスの「署名を検証する」から参照) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(このページで分かること・概要・各詳細ページへの導線・Webhook の署名検証・公式の裏付け・失敗例・チェックリスト・出典を追加。既存の用語・フロー・管理・リトライの内容は維持) |
