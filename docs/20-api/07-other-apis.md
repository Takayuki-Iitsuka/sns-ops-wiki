---
title: その他の API(Facebook・LINE・Bluesky・Twitch・note)
platform: common
topic: api
last_verified: 2026-11-03
confidence: ⚪
---

# その他の API

> 公式本文は未取得。一般的な理解(⚪)と二次資料(🟡)です。公式で確認してください (#39, #40)。

## Facebook(Graph API / Pages API)

| 項目 | 内容 |
|---|---|
| 用途 | ページの投稿(テキスト・写真・動画)、予約、コメント、インサイト |
| 認証 | Meta アプリ、ページアクセストークン |
| 権限 | 例: `pages_manage_posts`、`pages_read_engagement`(審査が必要 ⚪) |
| 注意 | Instagram と同じ Meta アプリで管理できる。API バージョンの廃止サイクルに注意 |

## LINE(Messaging API)

| 項目 | 内容 |
|---|---|
| 用途 | 友だちへの配信(broadcast、narrowcast、push)、応答(reply)、リッチメニューの設定 |
| 認証 | チャネルアクセストークン(長期/ステートレス) |
| Webhook | 友だち追加・メッセージ受信のイベントを受ける。**署名の検証が必須** |
| 課金 | 送信通数が料金プランの上限に影響([02-line-official-account](../09-other-services/02-line-official-account.md)) |

## Bluesky(AT Protocol)

| 項目 | 内容 | 確度 |
|---|---|---|
| 認証 | アプリパスワードで `com.atproto.server.createSession`、または OAuth | ⚪ |
| 投稿 | `com.atproto.repo.createRecord` で `app.bsky.feed.post` を作成 | ⚪ |
| 画像 | `com.atproto.repo.uploadBlob` でアップロードし、投稿に埋め込む | ⚪ |
| リッチテキスト | ハッシュタグ・メンション・リンクは **facets**(バイト範囲の指定)で表現 | ⚪ |
| 上限 | 300 grapheme、画像1〜2MB・4枚、動画の上限は資料により不一致 | 🟡 |
| 確認先 | AT Protocol の lexicon(`app.bsky.embed.*`) | — |

## Twitch(Helix API / EventSub)

配信情報の取得、チャットのモデレーション、EventSub による通知。フォロー・サブスクの通知を受けて Discord や X に連動するなどの用途(⚪)。

## Discord(Webhook / Bot)

通知は **Webhook** が最も簡単(トークン管理が不要。URL が秘密)。ボットは Bot Token と Gateway/REST。上限・レート制限・特権インテントの要点は [04-discord](../09-other-services/04-discord.md) §8(⚪ 公式未取得 #65)。

## note

- 公式の**公開 API は確認できていません**(⚪ 要確認 #43)。
- 非公式の API を使った自動投稿・スクレイピングは、規約違反やアカウント停止のリスクがある。**公式の予約投稿**を使う。
- 外部サイトとの連携は、RSS やサイトからのリンクで足りる場合が多い。
