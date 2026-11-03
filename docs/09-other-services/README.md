---
title: その他のサービス(索引と比較)
platform: common
topic: overview
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.line.biz/ja/docs/messaging-api/pricing/
---

# その他のサービス

> **このページで分かること**: 主要 SNS 以外で、運用や収益化の候補になるサービスの一覧と、目的別の選び方。
>
> **対象**: 初心者  **先に読むページ**: [サービスの選び方](../01-common/choosing-platforms.md)

## 概要

主要サービス(X・Instagram・note・YouTube・TikTok・Threads・Facebook)以外で、**運用・収益化の観点で候補になるサービス**です。

最初から全部を使う必要はありません。
多くの場合、**主軸の SNS を1つ決め、補助として1つ足す**くらいが続けやすい量です(⚪)。
例: Instagram を主軸に、常連客への連絡用に LINE 公式アカウントを足す。

## 用語

| 用語 | 意味 |
|---|---|
| 分散型 SNS | 1つの会社のサーバーだけに依存しない SNS(Bluesky・Mastodon など) |
| プッシュ型 | 相手の画面に直接届く連絡手段(LINE・メールなど) |
| ライブ配信 | リアルタイムで映像を届けること |
| コミュニティ型 | 参加者どうしが会話する場(Discord など) |

## 一覧

| サービス | 主な用途 | 収益化 | ページ |
|---|---|---|---|
| Bluesky | 分散型の短文 SNS | なし(外部誘導) | [01-bluesky](01-bluesky.md) |
| LINE 公式アカウント | 友だちへの直接配信 | 自社商品・サービスの販売、メッセージ課金(コスト) | [02-line-official-account](02-line-official-account.md) |
| Twitch | ゲーム・ライブ配信 | サブスク、Bits、広告(Affiliate/Partner) | [03-twitch](03-twitch.md) |
| Discord | ファンのコミュニティ運営 | Server Subscriptions(有料メンバー)、Premium Apps | [04-discord](04-discord.md) |
| ファンクラブ・販売系 | 継続支援・物販・電子書籍 | 手数料を引いた売上 | [10-creator-economy](../10-creator-economy/README.md) |

## 費用の目安

| サービス | 始めるのにかかる費用 | 確度 |
|---|---|---|
| Bluesky | 無料 | ⚪ |
| LINE 公式アカウント | 無料プラン(月200通)あり。ライト 5,000円・スタンダード 15,000円(税別) | ✅ [LINE 開発者文書](https://developers.line.biz/ja/docs/messaging-api/pricing/) |
| Twitch | 無料(配信機材・PC は別) | ⚪ |

詳しい料金は [その他サービスの料金](../40-pricing/04-other-services.md) を参照してください。

## 選び方の目安(⚪)

| 目的 | 候補 |
|---|---|
| 友だち・会員に確実に届けたい | LINE 公式アカウント、メール([ニュースレター](../01-common/newsletter-and-email.md)) |
| 技術系・オープンな場 | Bluesky、Mastodon 系 |
| ライブ配信を主軸 | Twitch、YouTube ライブ([ライブ配信](../01-common/live-streaming.md)) |
| ファンどうしの交流の場 | Discord([コミュニティ運営](../01-common/community-management.md)) |
| 継続支援・販売 | [creator-economy](../10-creator-economy/README.md) |

## 選ぶときの手順

1. 目的を1つに絞ります(例: 「常連客に新商品を知らせたい」)。
2. 上の表から候補を2つ選びます。
3. 費用・運用の手間(週に何時間かかるか)を比べます。
4. 1か月試し、続けられるか・反応があるかで判断します([最初の30日](../01-common/first-30-days.md))。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 流行りのサービスに次々登録し、どれも放置 | 主軸1つ+補助1つに絞る |
| 放置アカウントが偽物と間違われる | 使わないならプロフィールに「更新停止」と書くか削除 |

## 追加候補(未作成)

Pinterest、ニコニコ動画、Mastodon/Misskey、Substack/Medium、Lemon8。追加する場合は [page-template](../00-meta/page-template.md) を使い、仕様・収益化条件・API を同形式で書く(番号は 05 以降)。

## 関連ページ

- [API(その他)](../20-api/07-other-apis.md)
- [収益化の比較](../01-common/monetization-comparison.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.line.biz/ja/docs/messaging-api/pricing/ | 2026-11-03 | LINE 公式アカウントの料金プラン例(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要・用語・費用の目安・選ぶ手順・よくある失敗を追加。Discord(04-discord)を索引に追加し、追加候補から削除) |
