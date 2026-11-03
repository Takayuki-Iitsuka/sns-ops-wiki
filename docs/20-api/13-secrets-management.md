---
title: API キー・トークンの安全な保管
platform: common
topic: api
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://developers.tiktok.com/doc/content-sharing-guidelines
---

# API キー・トークンの安全な保管

> **このページで分かること**: 鍵(キー・トークン・シークレット)をどこに置き、どう使い、漏れたらどうするか。`.env` ファイルと `.gitignore` の具体的な書き方。
>
> **対象**: 初心者(最初に必ず読む)  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

API の鍵は**家の合鍵と同じ**です。漏れると、他人があなたのアカウントで投稿したり、X API のような従量課金なら**あなたのお金で API を使われたり**します。

いちばん多い事故は「**コードに鍵を直接書き、そのまま GitHub などに公開する**」ことです。このリポジトリも public なので、**鍵・トークン・パスワードは絶対に書きません**(→ [CONTRIBUTING](../../CONTRIBUTING.md))。

X の公式文書も、認証情報について次を勧めています(✅ [getting-access](https://docs.x.com/x-api/getting-started/getting-access.md)):

- 発行されたらすぐにパスワードマネージャーや安全な保管庫に保存する(**一度しか表示されない**)。
- コードに直接書かず、**環境変数**を使う。
- 認証情報のファイルを **`.gitignore`** に入れ、git にコミットしない。
- 定期的に再発行する。
- 必要なスコープだけを求める。

TikTok の規約も、`client_secret` を第三者に共有したりオープンソースのプロジェクトに埋め込んだりすることを禁止しています(✅ [content-sharing-guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines))。

## 用語

| 用語 | 意味 |
|---|---|
| secret(シークレット、秘密情報) | API キー、client secret、アクセストークン、リフレッシュトークン、パスワードの総称 |
| environment variable(環境変数) | OS がプログラムに渡す「名前=値」の設定。コードの外に鍵を置ける |
| `.env` ファイル(ドットエンブ) | 環境変数をまとめて書いておく、手元専用のテキストファイル |
| `.gitignore`(ギットイグノア) | git に「このファイルは記録しない」と伝える設定ファイル |
| commit(コミット) | git に変更を記録すること。一度記録すると履歴に残る |
| rotation(ローテーション、再発行) | 鍵を新しく作り直し、古い鍵を無効にすること |
| revoke(失効) | 鍵・トークンを使えなくすること |
| secret manager(シークレット管理) | 鍵を暗号化して保管する専用の仕組み(GitHub Actions の Secrets、クラウドのシークレット管理など) |

## 手順: `.env` と `.gitignore` で鍵を分ける

### 1. `.gitignore` を先に作る(最重要)

プロジェクトのフォルダに `.gitignore` というファイルを作り、次を書きます。**`.env` を作る前に**やります。

```gitignore
# 鍵を入れるファイルは記録しない
.env
.env.*
!.env.example
*.pem
*.key
client_secret*.json
token*.json
```

### 2. `.env.example`(見本)を作る

値の入っていない見本は共有してかまいません。どんな名前の鍵が必要かを伝えるためのものです。

```dotenv
# コピーして .env を作り、値を入れる(.env はコミットしない)
X_BEARER_TOKEN=YOUR_BEARER_TOKEN
X_CLIENT_ID=YOUR_CLIENT_ID
IG_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
YOUTUBE_API_KEY=YOUR_API_KEY
```

### 3. `.env`(本物)を作る

`.env.example` をコピーして `.env` を作り、`YOUR_...` の部分を本物の値に置き換えます。**このファイルは自分の PC の中だけ**に置きます。

### 4. コードから読み込む(Python)

`python-dotenv` という部品を使うと、`.env` を環境変数として読み込めます(⚪ インストールは `pip install python-dotenv`)。

```python
import os
from dotenv import load_dotenv

load_dotenv()                                  # .env を読み込む
token = os.environ.get("X_BEARER_TOKEN")       # 名前で取り出す
if not token:
    raise SystemExit("X_BEARER_TOKEN が設定されていません(.env を確認)")
```

### 5. コミット前に確認する

```bash
git status          # .env が一覧に出ていないことを確認
git diff --cached   # 記録する内容に鍵が混ざっていないか目で見る
```

## 保管場所の選び方

| 置き場所 | 向いている場面 | 注意 | 確度 |
|---|---|---|---|
| パスワードマネージャー | 発行直後の控え、手作業 | 共有するなら共有用の保管庫を使う | ⚪ |
| `.env` ファイル | 自分の PC で動かすスクリプト | `.gitignore` 必須。PC のディスク暗号化も | ⚪ |
| OS の環境変数 | 一時的な実行 | シェルの履歴に残ることがある | ⚪ |
| GitHub Actions の Secrets | 定期実行(GitHub 上) | ログでは伏せ字になるが、**加工して出力すると漏れる**ことがある | ⚪ |
| クラウドのシークレット管理 | サーバーで常時動かす | アクセス権を最小に | ⚪ |
| ✕ コードに直接 | — | **禁止** | — |
| ✕ スプレッドシート・チャット・メール | — | **禁止**(共有・転送で広がる) | — |

## 漏れたかもしれないときの対応

順番が大切です。**まず鍵を止め、その後で掃除**します。

1. **すぐに失効・再発行する**。X では再発行すると古い認証情報は無効になります(✅ [getting-access](https://docs.x.com/x-api/getting-started/getting-access.md))。Meta・Google・TikTok・LINE も各管理画面で再発行します。
2. 連携しているツール・スクリプトの鍵を**新しい鍵に差し替える**。
3. 漏れていた期間の**利用履歴・請求・投稿**を確認する(覚えのない投稿、X の請求額の急増など)。
4. git の履歴から消す(必要に応じて)。ただし**履歴の書き換えだけでは不十分**です。すでに誰かが複製した可能性があるため、1 を必ず先にやります(⚪)。
5. 原因を記録し、再発防止(`.gitignore`、コミット前の確認)を追加する。

## 具体例

| 良い例 | 悪い例 |
|---|---|
| `token = os.environ["X_BEARER_TOKEN"]` | `token = "AAAA...本物の値..."` |
| エラー時に `print(r.status_code)` だけ出す | エラー時にヘッダーごと `print(r.request.headers)`(トークンが表示される) |
| 読み取り専用・投稿用でトークンを分ける | 何でもできるトークン1つを全ツールに渡す |
| 共同作業者には各自で発行してもらう | 自分の鍵をチャットで配る |
| 質問するときはエラー文の鍵部分を `***` に置き換える | スクリーンショットに鍵が写ったまま投稿する |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| `.gitignore` を後から作ったので `.env` がすでにコミット済み | `.gitignore` は記録済みのファイルには効かない(⚪)。鍵を再発行し、`git rm --cached .env` で記録から外す |
| 鍵をスクリーンショットで共有した | 再発行する。画像は削除しても転送先に残る |
| 「このリポジトリは private だから」と鍵を書いた | 後で public にしたり、フォークや共同作業者から漏れたりする。private でも書かない |
| ノーコードツールにパスワードを入力した | 公式の OAuth 連携か確認し、違うなら使わない([11-tool-integrations](11-tool-integrations.md)) |

## 注意点

- このリポジトリの `scripts/check_wiki.py` は、鍵らしい文字列をいくつかの形式で検出しますが、**すべては見つけられません**。人の目での確認が前提です。
- 例には `YOUR_API_KEY` のようなプレースホルダだけを使います。**本物らしく見える架空の文字列**も、検査や他人を混乱させるので書きません。
- 端末の保護(画面ロック、ディスク暗号化、OS の更新)も鍵の保護の一部です([account-security](../01-common/account-security.md))。

## チェックリスト

- [ ] `.gitignore` に `.env` を入れてから `.env` を作った
- [ ] コードに鍵を直接書いていない
- [ ] `git status` で `.env` が出ないことを確認した
- [ ] ログ・エラー表示にトークンを出していない
- [ ] 鍵の控えをパスワードマネージャーに保存した
- [ ] 漏えい時の再発行の場所(各管理画面)を把握している
- [ ] 不要になった鍵・連携を失効させた

## 関連ページ / 次に読む

- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) — トークンの種類と期限
- [15-python-first-steps](15-python-first-steps.md) — `.env` を使った最初のプログラム
- [08-automation-and-tools](08-automation-and-tools.md) — GitHub Actions での定期実行
- [account-security](../01-common/account-security.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 認証情報は一度だけ表示、環境変数・`.gitignore`・定期再発行の推奨、再発行で旧鍵は無効 |
| https://developers.tiktok.com/doc/content-sharing-guidelines | 2026-11-03 | `client_secret` の共有・オープンソースへの埋め込みの禁止 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(`.env`・`.gitignore` の手順、保管場所の比較、漏えい時の対応、良い例・悪い例) |
