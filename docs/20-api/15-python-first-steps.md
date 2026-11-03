---
title: Python で API を呼ぶ最初の一歩
platform: common
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/make-your-first-request.md
  - https://docs.x.com/xdks/python/install.md
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md
  - https://developers.google.com/youtube/v3/getting-started
  - https://developers.google.com/youtube/v3/determine_quota_cost
---

# Python で API を呼ぶ最初の一歩

> **このページで分かること**: Python の準備から、鍵を `.env` に置いて API を1回呼び、結果を読むところまで。X・Instagram・YouTube の最小コード例。
>
> **対象**: プログラミング初心者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[13-secrets-management](13-secrets-management.md)

## 概要

最初の目標は「**自分の情報を1回だけ読み取る**」ことです。投稿(書き込み)は誤操作の影響が大きいので、読み取りで慣れてから進みます。

Python(パイソン)は、短いコードで API を呼べるプログラミング言語です。ここでは HTTP の通信に `requests`、`.env` の読み込みに `python-dotenv` という部品(ライブラリ)を使います(⚪ 一般的な選択)。

## 用語

| 用語 | 意味 |
|---|---|
| Python(パイソン) | プログラミング言語の一つ |
| terminal(ターミナル) | 文字でコマンドを入力する画面。Windows では「ターミナル」や PowerShell |
| library(ライブラリ) | 便利な機能をまとめた部品。`pip` で追加する |
| pip(ピップ) | Python のライブラリを入れる道具 |
| venv(仮想環境) | プロジェクトごとにライブラリを分けて入れる仕組み |
| `requests` | HTTP リクエストを送るライブラリ |
| `python-dotenv` | `.env` を読み込むライブラリ |
| XDK | X 公式の SDK。Python 版は `pip install xdk`、Python 3.8 以上(✅ [XDK install](https://docs.x.com/xdks/python/install.md)) |

## 手順

### 1. Python を入れる

公式サイト(python.org)から入れます。Mac は Homebrew、Windows は Microsoft Store からも入れられます(⚪ 表記・手順は変わる可能性)。入ったか確認します。

```bash
python3 --version     # Windows では python --version
```

### 2. 作業フォルダと仮想環境を作る

```bash
mkdir sns-api-practice
cd sns-api-practice
python3 -m venv .venv
source .venv/bin/activate        # Windows は .venv\Scripts\activate
pip install requests python-dotenv
```

`.gitignore` に `.venv/` と `.env` を入れます([13-secrets-management](13-secrets-management.md))。

### 3. `.env` に鍵を書く

```dotenv
X_BEARER_TOKEN=YOUR_BEARER_TOKEN
IG_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
YOUTUBE_API_KEY=YOUR_API_KEY
```

`YOUR_...` を、各サービスの管理画面で発行した本物の値に置き換えます。**このファイルは共有もコミットもしません**。

### 4. コードを書いて実行する

下の例を `x_lookup.py` のような名前で保存し、`python3 x_lookup.py` で実行します。

## 具体例 1: X でユーザー情報を読む

X 公式の入門ページと同じエンドポイントです(✅ [first request](https://docs.x.com/make-your-first-request.md))。Bearer Token は Developer Console のアプリ画面からコピーします(✅ 同ページ)。

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.environ["X_BEARER_TOKEN"]          # 値はコードに書かない

r = requests.get(
    "https://api.x.com/2/users/by/username/xdevelopers",
    headers={"Authorization": f"Bearer {token}"},
    timeout=30,
)

print("ステータス:", r.status_code)
if r.ok:
    user = r.json()["data"]                   # 主なデータは data の中
    print(user["id"], user["username"])
else:
    print("エラー:", r.json())                 # 401 ならトークン、403 なら権限を確認
print("残り回数:", r.headers.get("x-rate-limit-remaining"))
```

- **費用**: X API は従量課金です。他人のユーザー情報の読み取りは **User: Read $0.010/件**(✅ [pricing](https://docs.x.com/x-api/getting-started/pricing.md))。練習でも残高が減ります。自分のデータの読み取り(Owned Reads)は $0.001/件です(✅ 同ページ)。
- 支出上限(spending limit)を先に設定しておくと安心です([16-x-api-getting-started](16-x-api-getting-started.md))。

## 具体例 2: Instagram で自分のアカウントを読む

Instagram ログインの入門ページの最初の呼び出しです(✅ [IG get started](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md))。

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
r = requests.get(
    "https://graph.instagram.com/v26.0/me",
    params={
        "fields": "user_id,username",
        "access_token": os.environ["IG_ACCESS_TOKEN"],
    },
    timeout=30,
)
print(r.status_code, r.json())
```

- `fields` に**欲しい項目だけ**をカンマ区切りで書きます。
- Meta の API はトークンを URL のパラメータで渡す例が多いですが、その URL を**ログや画面共有に出さない**よう注意します。
- バージョン(`v26.0`)は公式の例の値です。古いバージョンは順に廃止されます。

## 具体例 3: YouTube で公開チャンネルの情報を読む

公開データの読み取りは **API キー**で行えます(✅ [YouTube getting started](https://developers.google.com/youtube/v3/getting-started))。`channels.list` のコストは **1 ユニット**です(✅ [quota](https://developers.google.com/youtube/v3/determine_quota_cost))。

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
r = requests.get(
    "https://www.googleapis.com/youtube/v3/channels",
    params={
        "part": "snippet,statistics",       # 欲しい情報のまとまり
        "forHandle": "@YouTube",            # 調べたいチャンネルのハンドル(⚪ 例)
        "key": os.environ["YOUTUBE_API_KEY"],
    },
    timeout=30,
)
print(r.status_code)
for item in r.json().get("items", []):
    print(item["snippet"]["title"], item["statistics"].get("subscriberCount"))
```

- `part` には必要なものだけを指定すると、通信量と待ち時間が減ります(✅ 同ページ)。
- `forHandle` パラメータの指定方法は公式リファレンスで確認してください(⚪ 要確認)。

## レスポンスを読むコツ

1. まず `print(r.status_code)` で成功か失敗かを見る。
2. 成功なら `r.json()` を表示し、**どの名前の下に何があるか**を確かめてから取り出す。
3. 見やすくするには `import json; print(json.dumps(r.json(), ensure_ascii=False, indent=2))`。
4. 一覧は `[ ]`。`for item in ...:` で1件ずつ扱う。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| `ModuleNotFoundError: No module named 'requests'` | ライブラリ未インストール、または仮想環境が有効でない | `source .venv/bin/activate` してから `pip install requests` |
| `KeyError: 'X_BEARER_TOKEN'` | `.env` がない、名前の綴り違い、`load_dotenv()` の呼び忘れ | `.env` の場所(実行するフォルダ)と名前を確認 |
| `KeyError: 'data'` | エラーが返っている | `r.status_code` と `r.json()` を先に表示 |
| 401 | トークンの貼り間違い・期限切れ | [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) |
| 日本語が `あ` のように表示される | JSON の既定の表示 | `json.dumps(..., ensure_ascii=False)` |

## 注意点

- このページのコードは**学習用の最小例**です。本番では、再試行・ログ・通知・二重投稿の防止を加えます([09-architecture-patterns](09-architecture-patterns.md))。
- 各サービスの最新の仕様・料金は公式で確認してください。
- **投稿の例**は各サービスのページにあります([16 X](16-x-api-getting-started.md)、[03 Instagram](03-instagram-graph-api.md)、[04 Threads](04-threads-api.md))。

## チェックリスト

- [ ] `python3 --version` が表示される
- [ ] 仮想環境を有効にして `requests`・`python-dotenv` を入れた
- [ ] `.gitignore` に `.env` と `.venv/` がある
- [ ] 読み取りの例が 200 で返った
- [ ] エラー時の表示にトークンが含まれない

## 関連ページ / 次に読む

- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md) — 投稿に必要なユーザー認証
- [16-x-api-getting-started](16-x-api-getting-started.md) — X で投稿するまで
- [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) — 再試行のコード

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/make-your-first-request.md | 2026-11-03 | ユーザー情報取得の例 |
| https://docs.x.com/xdks/python/install.md | 2026-11-03 | `pip install xdk`、Python 3.8 以上 |
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | User: Read と Owned Reads の単価 |
| https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md | 2026-11-03 | `GET /me?fields=user_id,username` |
| https://developers.google.com/youtube/v3/getting-started | 2026-11-03 | API キー、`part` パラメータ |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | `channels.list` 1 ユニット |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(Python の準備、`.env` の使い方、X・Instagram・YouTube の読み取りの最小例) |
