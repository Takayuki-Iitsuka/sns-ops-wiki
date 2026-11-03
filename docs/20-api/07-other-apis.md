---
title: その他の API(Facebook・LINE・Bluesky・Twitch・note)
platform: common
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/docs/pages-api/posts
  - https://developers.line.biz/ja/docs/messaging-api/getting-started/
  - https://developers.line.biz/ja/docs/basics/channel-access-token/
  - https://developers.line.biz/ja/reference/messaging-api/
  - https://developers.line.biz/ja/docs/messaging-api/pricing/
  - https://docs.bsky.app/docs/advanced-guides/rate-limits
---

# その他の API

> **このページで分かること**: Facebook ページ、LINE 公式アカウント(Messaging API)、Bluesky、Twitch、note の API の概要・始め方・上限・注意点。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

> 以前は「公式本文は未取得」でしたが、2026年(皇紀2686年・令和8年)11月3日に **Facebook ページの投稿 API と LINE の開発者文書を直接取得**して ✅ に更新しました。Bluesky は公式文書(docs.bsky.app)が別ホストへ転送され本文を取得できず、検索結果の要約のみ(🟡)。Twitch・note は ⚪ のままです (#39, #40, #43)。

## 概要

| サービス | API | 主な用途 | 始める場所 | 確度 |
|---|---|---|---|---|
| Facebook ページ | Graph API(Pages API) | ページへの投稿・予約・コメント・インサイト | Meta for Developers | ✅ |
| LINE 公式アカウント | Messaging API | 友だちへの配信・自動応答・リッチメニュー | LINE Official Account Manager → LINE Developers | ✅ |
| Bluesky | AT Protocol(XRPC) | 投稿・画像・フィード | アプリパスワード / OAuth | 🟡/⚪ |
| Twitch | Helix API / EventSub | 配信情報・チャット・通知 | Twitch Developers | ⚪ |
| note | 公式の公開 API は未確認 | — | — | ⚪ |

## 用語

| 用語 | 意味 |
|---|---|
| Page access token(ページアクセストークン) | Facebook ページとして操作するためのトークン |
| Page task(ページのタスク) | ページでの役割に応じた権限(`CREATE_CONTENT` など) |
| channel(チャネル) | LINE で API を使う単位。公式アカウントごとに作られる |
| provider(プロバイダー) | LINE Developers でチャネルを束ねる管理単位(会社・個人) |
| channel access token(チャネルアクセストークン) | LINE の API 呼び出しに使うトークン |
| channel secret(チャネルシークレット) | Webhook の署名検証などに使う LINE の秘密鍵 |
| token bucket(トークンバケット方式) | 使った分が時間とともに少しずつ回復するレート制限の方式 |
| App password(アプリパスワード) | Bluesky で、本当のパスワードの代わりにアプリ用に発行するパスワード |
| PDS(Personal Data Server) | Bluesky(AT Protocol)で利用者のデータを置くサーバー |
| grapheme(書記素) | 人が「1文字」と感じる単位。絵文字の組み合わせも1つと数える |

## Facebook(Graph API / Pages API)

| 項目 | 内容 |
|---|---|
| 用途 | ページの投稿(テキスト・写真・動画)、予約、コメント、インサイト |
| 認証 | Meta アプリ、ページアクセストークン |
| 権限 | 例: `pages_manage_posts`、`pages_read_engagement`(審査が必要 ⚪) |
| 注意 | Instagram と同じ Meta アプリで管理できる。API バージョンの廃止サイクルに注意 |

**投稿 API の公式仕様**(✅ [Pages API posts](https://developers.facebook.com/docs/pages-api/posts)):

| 項目 | 値 |
|---|---|
| エンドポイント | `POST /{page_id}/feed`(例: `https://graph.facebook.com/v26.0/{page_id}/feed`) |
| 権限 | `pages_manage_engagement`、`pages_manage_posts`、`pages_read_engagement`、`pages_read_user_engagement`(動画は `publish_video` も) |
| トークン | ページアクセストークン |
| ページのタスク | 操作する人が `CREATE_CONTENT`、`MANAGE`、`MODERATE` を実行できること |
| 予約投稿 | `published=false` と `scheduled_publish_time`(UNIX 秒、ISO 8601 など)。**リクエストから10分後〜30日後**の範囲 |

```python
import os
import requests

# 予約投稿の例(概念。動作は未検証)
r = requests.post(
    f"https://graph.facebook.com/v26.0/{os.environ['FB_PAGE_ID']}/feed",
    data={
        "message": "今週末は臨時休業します",
        "published": "false",
        "scheduled_publish_time": "2026-11-10T10:00:00+09:00",   # 10分後〜30日後
        "access_token": os.environ["FB_PAGE_ACCESS_TOKEN"],
    },
    timeout=30,
)
print(r.status_code, r.json())
```

エラーの読み方(code 190、368 など)は [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)。

## LINE(Messaging API)

| 項目 | 内容 |
|---|---|
| 用途 | 友だちへの配信(broadcast、narrowcast、push)、応答(reply)、リッチメニューの設定 |
| 認証 | チャネルアクセストークン(長期/ステートレス) |
| Webhook | 友だち追加・メッセージ受信のイベントを受ける。**署名の検証が必須** |
| 課金 | 送信通数が料金プランの上限に影響([02-line-official-account](../09-other-services/02-line-official-account.md)) |

### 始める手順(✅ [getting started](https://developers.line.biz/ja/docs/messaging-api/getting-started/))

1. **LINE 公式アカウントを作る**(ビジネス ID に登録 → 作成フォーム → LINE Official Account Manager で確認)。
2. LINE Official Account Manager で **Messaging API を有効にする**。このときチャネルが作られ、**プロバイダー**を選ぶ。
3. LINE Developers コンソールに同じアカウントでログインし、チャネルができたことを確認する。

注意(✅ 同ページ):

- **2024年(皇紀2684年・令和6年)9月4日以降、LINE Developers コンソールから Messaging API チャネルを直接作成できなくなりました**。公式アカウントから有効化します。
- **一度選んだプロバイダーは後から変更できず、Messaging API との連携も解除できません**。会社・個人の区別を決めてから選びます。

### チャネルアクセストークン(✅ [channel access token](https://developers.line.biz/ja/docs/basics/channel-access-token/))

| 種類 | 有効期間 | 発行上限 |
|---|---|---|
| 任意の有効期間を指定できるトークン(v2.1) | 最大30日 | チャネルごとに30件 |
| ステートレスチャネルアクセストークン | 15分 | 無制限 |
| 短期のチャネルアクセストークン | 30日 | チャネルごとに30件 |
| 長期のチャネルアクセストークン | 無期限 | チャネルごとに1件 |

期限切れ前に自動で新しいトークンを発行する仕組みが推奨されています(✅)。長期トークンは**期限がない分、漏れたときの被害が続く**ので保管に特に注意します([13-secrets-management](13-secrets-management.md))。

### レート制限(✅ [Messaging API リファレンス](https://developers.line.biz/ja/reference/messaging-api/))

| エンドポイント(抜粋) | 上限 |
|---|---|
| ナローキャスト・ブロードキャスト、送信数・友だち数・統計情報の取得 | **60リクエスト/時** |
| マルチキャスト | 200リクエスト/秒 |
| 上記以外(プッシュ、応答など) | 2,000リクエスト/秒 |

- 上限は**チャネル単位・エンドポイントごと**。超えると `429 Too Many Requests`。トークンバケット方式で徐々に回復します(✅)。

### 料金と送信数(✅ [pricing](https://developers.line.biz/ja/docs/messaging-api/pricing/))

- **応答メッセージ(reply)は通数に数えない**。プッシュ・マルチキャスト・ブロードキャスト・ナローキャストは数える。
- 通数は**送信対象の人数**で数える(1回に入れる吹き出しの数は関係ない)。ブロック中・存在しないユーザーは数えない。
- 当月の上限を超えるとエラーになり、送信されない。
- 日本のプラン例(税別、同ページ記載): コミュニケーション 月0円・200通、ライト 月5,000円・5,000通、スタンダード 月15,000円・30,000通(追加は1通最大約3円)。**2026年10月の改定の有無は別途確認**([02-line-official-account](../09-other-services/02-line-official-account.md)、#40)。

→ 自動応答を「reply」で作れば通数を消費しません。定期配信(push・broadcast)は通数を見積もってから使います。

## Bluesky(AT Protocol)

| 項目 | 内容 | 確度 |
|---|---|---|
| 認証 | アプリパスワードで `com.atproto.server.createSession`、または OAuth | ⚪ |
| 投稿 | `com.atproto.repo.createRecord` で `app.bsky.feed.post` を作成 | ⚪ |
| 画像 | `com.atproto.repo.uploadBlob` でアップロードし、投稿に埋め込む | ⚪ |
| リッチテキスト | ハッシュタグ・メンション・リンクは **facets**(バイト範囲の指定)で表現 | ⚪ |
| 上限 | 300 grapheme、画像1〜2MB・4枚、動画の上限は資料により不一致 | 🟡 |
| 確認先 | AT Protocol の lexicon(`app.bsky.embed.*`) | — |

**レート制限**(🟡 検索結果の要約。公式ページ [rate limits](https://docs.bsky.app/docs/advanced-guides/rate-limits) は取得時に別ホストへ転送され本文未取得):

| 項目 | 値 |
|---|---|
| ログイン(`createSession`) | 5分に30回、1日に300回(アカウント単位) |
| 書き込み | 1時間 5,000ポイント、1日 35,000ポイント(作成 = 3ポイント → 1時間に最大 1,666件) |
| 注意 | Bluesky が運営する PDS の値。他の事業者の PDS では異なる。今後変わる可能性あり |

→ **投稿のたびにログインし直さない**(1日300回の上限に当たる)。セッションを使い回します。

## Discord(Webhook / Bot)

通知は **Webhook** が最も簡単です(トークン管理が不要。ただし Webhook の URL 自体が秘密なので公開しない)。ボットは Bot Token と Gateway/REST を使います。上限・レート制限・特権インテントの要点は [04-discord](../09-other-services/04-discord.md) §8(⚪ 公式未取得 #70)。

## Twitch(Helix API / EventSub)

配信情報の取得、チャットのモデレーション、EventSub による通知。フォロー・サブスクの通知を受けて Discord や X に連動するなどの用途(⚪)。始め方・上限は公式(dev.twitch.tv)で要確認。

## note

- 公式の**公開 API は確認できていません**(⚪ 要確認 #43)。
- 非公式の API を使った自動投稿・スクレイピングは、規約違反やアカウント停止のリスクがある。**公式の予約投稿**を使う。
- 外部サイトとの連携は、RSS やサイトからのリンクで足りる場合が多い。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| Facebook の予約投稿でエラー | 予約時刻が10分後より前、または30日より先 | 範囲内にする |
| Facebook で権限エラー | ページのタスク不足、ページトークンでない | ページの役割と `pages_manage_posts` を確認 |
| LINE で 401 | チャネルアクセストークンが無効・期限切れ | 再発行。期限前の自動発行を組む |
| LINE の配信が月末に止まった | 当月の送信上限に到達 | プランと上限目安を確認 |
| LINE の Webhook が偽物かもしれない | 署名を検証していない | チャネルシークレットで署名を検証 |
| Bluesky で急にログインできない | ログインの回数上限 | セッションを使い回す |

## 関連ページ / 次に読む

- [01-bluesky](../09-other-services/01-bluesky.md)、[02-line-official-account](../09-other-services/02-line-official-account.md)、[03-twitch](../09-other-services/03-twitch.md)
- [01-setup-and-posting](../08-facebook/01-setup-and-posting.md) — Facebook ページ
- [03-instagram-graph-api](03-instagram-graph-api.md) — 同じ Meta の Instagram

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/docs/pages-api/posts | 2026-11-03 | ページ投稿の権限・タスク・予約の範囲 |
| https://developers.line.biz/ja/docs/messaging-api/getting-started/ | 2026-11-03 | 始める手順、2024年9月4日の変更、プロバイダーの注意 |
| https://developers.line.biz/ja/docs/basics/channel-access-token/ | 2026-11-03 | トークンの種類・期限・上限 |
| https://developers.line.biz/ja/reference/messaging-api/ | 2026-11-03 | レート制限、ステータスコード、署名検証 |
| https://developers.line.biz/ja/docs/messaging-api/pricing/ | 2026-11-03 | 通数の数え方、プラン例 |
| https://docs.bsky.app/docs/advanced-guides/rate-limits | 2026-11-03 | 🟡 検索結果の要約(本文は未取得) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 一般的な理解(⚪)と二次資料(🟡)で作成 |
| 2026-11-03 | Facebook ページの投稿 API と LINE の開発者文書を取得して ✅ を追加。Bluesky のレート制限を 🟡 で追加。初心者向けに概要の比較表・用語・コード例・失敗例・出典を追加。既存の表は維持 |
