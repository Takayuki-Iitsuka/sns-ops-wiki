---
title: 認証の基本(OAuth 2.0・アクセストークン・スコープ)
platform: common
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md
  - https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md
  - https://developers.facebook.com/documentation/threads/get-started.md
  - https://developers.tiktok.com/doc/oauth-user-access-token-management
  - https://developers.line.biz/ja/docs/basics/channel-access-token/
  - https://developers.google.com/youtube/v3/getting-started
---

# 認証の基本(OAuth 2.0・アクセストークン・スコープ)

> **このページで分かること**: API の「鍵」と「許可証」の違い、OAuth 2.0 の流れ、スコープの選び方、トークンの有効期限(サービス別)。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

API を使うとき、サービスは必ず「**あなたは誰か**」と「**何をしてよいか**」を確認します。

- **認証**(authentication、本人確認): 誰が呼び出しているか。
- **認可**(authorization、許可): その人(アプリ)に何を許すか。

SNS の API では、**OAuth 2.0(オーオース 2.0)** という仕組みで認可を受けるのが一般的です。OAuth 2.0 では、あなたのアプリに**パスワードを渡さず**、代わりに期限付きの**アクセストークン**を受け取ります。ホテルの「カードキー」に似ています。フロントで本人確認をすると、決まった部屋だけ・決まった期間だけ開くカードがもらえます。

## 用語

| 用語 | 意味 |
|---|---|
| OAuth 2.0(オーオース 2.0) | パスワードを渡さずに権限を委ねる標準的な仕組み |
| client ID(クライアント ID) | アプリの識別番号。公開されても直ちに危険ではないが、むやみに出さない |
| client secret(クライアントシークレット) | アプリの秘密の合言葉。**秘密情報** |
| access token(アクセストークン) | API を呼ぶときに付ける許可証。**秘密情報**。有効期限が短い |
| refresh token(リフレッシュトークン) | アクセストークンを再発行するための長期の鍵。**秘密情報** |
| Bearer token(ベアラートークン) | 「持っている人が使える」トークン。`Authorization: Bearer ...` で送る |
| scope(スコープ、権限範囲) | トークンで許す操作の範囲。例: 読み取りだけ、投稿も可 |
| redirect URI / callback URL(リダイレクト先) | 利用者が「許可」を押した後に戻ってくる URL。事前登録が必要 |
| authorization code(認可コード) | 許可の直後に一瞬だけ渡される引換券。トークンと交換する |
| PKCE(ピクシー、Proof Key for Code Exchange) | 認可コードの横取りを防ぐ追加の仕組み |
| state(ステート) | なりすましの防止に使うランダムな文字列 |
| App-only(アプリ専用)認証 | 利用者を介さず、アプリとして公開データを読む方式 |
| User context(ユーザーコンテキスト) | 特定の利用者の代わりに操作する方式。投稿には必須 |

## 認証方式の種類

| 方式 | 何に使う | 例 |
|---|---|---|
| API キーのみ | 公開データの読み取り | YouTube の公開動画の情報取得(✅ API キーでの `list` は公開データのみ返る) |
| アプリ専用トークン(Bearer) | 公開データの読み取り | X の App-only Bearer Token(✅) |
| OAuth 2.0(ユーザー代行) | 投稿・自分の非公開データ | X の投稿、Instagram の公開、YouTube のアップロード |
| チャネルアクセストークン | 公式アカウントからの送信 | LINE Messaging API(✅) |
| アプリパスワード | 簡易な代替パスワード | Bluesky(⚪) |

YouTube では、**作成・更新・削除のすべてと、本人だけが見られる情報の取得に OAuth 2.0 が必要**です(✅ [YouTube getting started](https://developers.google.com/youtube/v3/getting-started))。

## OAuth 2.0(認可コード+PKCE)の流れ

X の公式ガイドに沿った流れです(✅ [authorization-code](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md))。

```
① アプリ: 「許可ページ」の URL を作る(client_id、redirect_uri、scope、state、PKCE の値)
        │
② 利用者: ブラウザで許可ページを開き、内容を確認して「許可」
        │
③ サービス: redirect_uri に戻す。URL に「認可コード」が付く
        │
④ アプリ: 認可コードをトークンに交換(token エンドポイントへ POST)
        │
⑤ アプリ: アクセストークン(+リフレッシュトークン)を安全に保存
        │
⑥ アプリ: API 呼び出しのヘッダーに Authorization: Bearer <アクセストークン>
        │
⑦ 期限切れ前に: リフレッシュトークンで新しいアクセストークンを取得
```

X の場合の具体値(✅ 同ページ):

| 項目 | 値 |
|---|---|
| 許可ページ | `https://x.com/i/oauth2/authorize` |
| トークン交換 | `POST https://api.x.com/2/oauth2/token` |
| 認可コードの有効期間 | **30秒**(すぐに交換する) |
| アクセストークンの有効期間 | 既定で **2時間** |
| リフレッシュトークン | **`offline.access` スコープを含めたときだけ**発行 |
| 更新の方法 | `grant_type=refresh_token` と `refresh_token`、`client_id` を POST |
| クライアントの種類 | confidential(機密: Web アプリ・自動化 bot。client secret を持てる)/ public(公開: スマホアプリ・ブラウザだけのアプリ。secret を持てない) |

**初心者が引っかかりやすい点**

1. **redirect URI は完全一致**が基本です。末尾の `/` の有無、`http` と `https` の違いでも失敗します(⚪)。
2. 認可コードは**一度しか使えず、期限も短い**(X は30秒 ✅)。
3. 自分のアカウントだけを使う場合でも、投稿には OAuth のユーザー認証が必要です。

## スコープの選び方

**必要最小限だけ**を申請します。漏れたときの被害が小さくなり、利用者にも安心してもらえます。

X の主なスコープ(✅ 公式表から抜粋):

| スコープ | できること | 使う場面 |
|---|---|---|
| `tweet.read` | 投稿を読む | 分析・バックアップ |
| `users.read` | アカウント情報を読む | ほぼ常に必要 |
| `tweet.write` | 投稿する | 予約投稿 |
| `media.write` | 画像・動画をアップロード | メディア付き投稿 |
| `offline.access` | リフレッシュトークンを得る | 定期実行(2時間を超えて使う) |
| `tweet.moderate.write` | 返信を非表示にする | 荒らし対策 |
| `dm.read` / `dm.write` | DM の読み取り・送信 | 原則使わない(リスク高) |

Meta(Instagram・Threads)、YouTube のスコープは各ページを参照してください([03](03-instagram-graph-api.md)、[04](04-threads-api.md)、[05](05-youtube-data-api.md))。

## トークンの有効期限(サービス別)

| サービス | アクセストークン | 長期トークン / リフレッシュ | 確度 | 出典 |
|---|---|---|---|---|
| X(OAuth 2.0) | 2時間 | `offline.access` でリフレッシュトークン | ✅ | [X](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md) |
| Instagram(Instagram ログイン) | 短期 1時間 | 長期 60日(App Dashboard で発行したトークンも60日) | ✅ | [IG](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md)、[access_token](https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md) |
| Threads | 短期 1時間(認可コードも1時間) | 長期 60日。期限前に `GET /refresh_access_token` で更新。公開プロフィールの許可は90日(更新でさらに90日延長) | ✅ | [Threads](https://developers.facebook.com/documentation/threads/get-started.md) |
| TikTok | 2時間 | リフレッシュトークン 180日。**更新のたびに新しいリフレッシュトークンに置き換える** | ✅ | [TikTok](https://developers.tiktok.com/doc/oauth-user-access-token-management) |
| LINE(チャネルアクセストークン) | ステートレス 15分 / 短期 30日 / v2.1 は最大30日で任意指定 | 長期は無期限(チャネルごとに1件) | ✅ | [LINE](https://developers.line.biz/ja/docs/basics/channel-access-token/) |
| YouTube(Google OAuth) | — | — | ⚪ 要確認 | — |

→ **期限切れは必ず起きます**。定期実行するなら「期限の前に自動更新」「更新に失敗したら通知」を最初から組み込みます。

## 具体例: トークンの使い方(Python)

```python
import os
import requests

# トークンは環境変数から読む(コードに書かない)
token = os.environ["X_USER_ACCESS_TOKEN"]

r = requests.get(
    "https://api.x.com/2/users/me",
    headers={"Authorization": f"Bearer {token}"},
    timeout=30,
)
print(r.status_code)   # 200 なら成功、401 ならトークンを確認
```

リフレッシュの例(概念。X の公式ガイドの項目名に合わせた形。動作は未検証):

```python
import os
import requests

r = requests.post(
    "https://api.x.com/2/oauth2/token",
    data={
        "grant_type": "refresh_token",
        "refresh_token": os.environ["X_REFRESH_TOKEN"],
        "client_id": os.environ["X_CLIENT_ID"],
    },
    timeout=30,
)
r.raise_for_status()
new_tokens = r.json()   # 新しいトークンは安全な保管場所へ。print しない
```

## よくある失敗と対処

| 症状 | 原因の候補 | 対処 |
|---|---|---|
| 許可後に「redirect_uri が不正」 | 登録した URL と1文字違う | アプリ設定の callback URL と完全に一致させる |
| 交換時に `invalid_grant` 系のエラー | 認可コードの期限切れ・再利用 | 許可からやり直し、すぐ交換する |
| 2時間後に 401 | アクセストークンの期限切れ | リフレッシュする。`offline.access` を付けたか確認(X) |
| 403(権限不足) | スコープ不足、アプリの権限設定が読み取りのみ | スコープを追加して**再認可**(スコープを足しても既存トークンには反映されない ⚪) |
| TikTok で更新が突然失敗 | 古いリフレッシュトークンを使った | 更新のたびに保存し直す(✅ ローテーション) |

## 注意点

- トークンは**パスワードと同じ扱い**です。ログ・スクリーンショット・チャットに貼らない。
- 他人のアカウントを扱う(代理運用など)場合は、アプリ審査や本人の同意が必要になることがあります(Meta の Advanced Access など ✅ [03](03-instagram-graph-api.md))。
- 保管の方法は [13-secrets-management](13-secrets-management.md)。

## チェックリスト

- [ ] スコープは最小限か(読み取りだけで足りるなら書き込みを付けない)
- [ ] redirect URI をアプリ設定に登録した
- [ ] トークンを環境変数・シークレット管理に保存した
- [ ] 期限切れ前の自動更新と、失敗時の通知がある
- [ ] 不要になったトークン・連携を失効させる手順を知っている

## 関連ページ / 次に読む

- [13-secrets-management](13-secrets-management.md) — 鍵の保管
- [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) — 401/403 の対処
- [16-x-api-getting-started](16-x-api-getting-started.md) — X での具体的な手順
- [account-security](../01-common/account-security.md) — アカウント自体の守り方

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md | 2026-11-03 | X の OAuth 2.0、スコープ表、有効期限 |
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 認証情報の4種類 |
| https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/get-started.md | 2026-11-03 | Instagram の短期1時間・長期60日 |
| https://developers.facebook.com/documentation/instagram-platform/reference/access_token.md | 2026-11-03 | 長期トークンへの交換(`ig_exchange_token`) |
| https://developers.facebook.com/documentation/threads/get-started.md | 2026-11-03 | Threads のトークンと許可の期間 |
| https://developers.tiktok.com/doc/oauth-user-access-token-management | 2026-11-03 | TikTok の2時間・180日・ローテーション |
| https://developers.line.biz/ja/docs/basics/channel-access-token/ | 2026-11-03 | LINE のチャネルアクセストークン4種類 |
| https://developers.google.com/youtube/v3/getting-started | 2026-11-03 | YouTube の API キーと OAuth の使い分け |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(初心者向けに OAuth 2.0 の流れ、スコープ、サービス別の有効期限、コード例を整理) |
