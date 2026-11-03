---
title: Threads 初期設定と投稿
platform: threads
topic: setup
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/create-posts.md
  - https://developers.facebook.com/documentation/threads/create-posts/polls.md
  - https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md
  - https://developers.facebook.com/documentation/threads/create-posts/ghost-posts.md
  - https://developers.facebook.com/documentation/threads/create-posts/spoilers.md
  - https://developers.facebook.com/documentation/threads/reference/publishing.md
---

# Threads 初期設定と投稿

> **このページで分かること**: Threads の登録・プロフィール・プライバシー設定と、投稿の種類・投稿/編集/予約/削除の手順。
>
> **対象**: 初心者  **先に読むページ**: [Threads 概要](README.md)、[アカウントの安全](../01-common/account-security.md)

## 概要

Threads は、Instagram と同じ Meta のアカウント基盤を使うテキスト中心のサービスです。Instagram を使っている人は、プロフィールを引き継いで素早く始められます。

最初にやることは次の4つです。

1. 登録(Instagram で、または単独で)
2. プロフィールを整える
3. 公開範囲・返信範囲などのプライバシー設定
4. 最初の投稿(自己紹介)

## 用語

| 用語 | 意味 |
|---|---|
| profile(プロフィール) | 名前・自己紹介・リンク・画像 |
| public / private profile(公開 / 非公開) | 誰でも見られるか、承認したフォロワーだけか |
| fediverse(フェディバース) | Mastodon など、互いにつながる分散型 SNS。Threads の投稿を共有する設定がある |
| text attachment(テキスト添付) | 本文とは別に長文を付ける機能 |
| ghost post(ゴースト投稿) | 24時間後に自動でアーカイブされるテキスト投稿 |
| spoiler(スポイラー、ネタバレ防止) | 文字や画像をぼかして隠す機能 |
| draft(下書き)/ scheduled post(予約投稿) | 保存した投稿 / 日時指定の投稿 |

## 手順 / 仕様

### 初期設定

1. **Instagram アカウントでログイン**してプロフィールを引き継ぐ(⚪ 要確認)。
2. **プロフィール**: 名前・bio・リンク。Instagram と表記を揃える。
3. **プライバシー**: 公開/非公開、返信できる人の範囲、メンション・引用の許可。
4. **フェディバース共有** ⚪: 他サービスとの連携機能がある場合は設定を確認(提供状況は要確認)。
5. **2段階認証**: Instagram/Meta アカウント側で設定([account-security](../01-common/account-security.md))。

#### 登録方法の補足

| 項目 | 内容 | 確度 | 出典 |
|---|---|---|---|
| Instagram で登録 | Instagram のアカウントでログインし、プロフィールを読み込める | ⚪ | — |
| Instagram なしで登録 | 2025年(皇紀2685年・令和7年)にプライバシーポリシーが改定され、メールアドレスや電話番号で直接登録できるようになったとされる | 🟡 | [Open Terms Archive](https://opentermsarchive.org/en/memos/threads-expands-profile-creation-beyond-instagram-users/) |
| Facebook で登録 | 一部で試験中とする報道 | 🟡 | [Engadget](https://www.engadget.com/social-media/threads-is-testing-facebook-account-sign-ups-191214734.html) |
| フェディバース共有 | 共有を有効にした利用者の、API 経由の対象投稿も 2024年(皇紀2684年・令和6年)8月28日からフェディバースに共有 | ✅ | [Create Posts](https://developers.facebook.com/documentation/threads/create-posts.md) |

#### プライバシー設定のおすすめ(⚪ 表記は変わる可能性)

| 設定 | 初心者のおすすめ | 理由 |
|---|---|---|
| 公開/非公開 | 発信が目的なら **公開** | 非公開だとフォロワー以外に届かない |
| 返信できる人 | 最初は「すべての人」、荒れたら狭める | [04-engagement](04-engagement.md) |
| メンション | 「フォロー中の人」など狭めに | 知らない人からの巻き込みを防ぐ |
| 隠しワード | NG ワードを登録 | 不快な返信を見ずに済む |
| フェディバース共有 | 意味が分かるまで **オフ** | 共有した投稿は他サービスにも広がる |

### 投稿の種類

| 種類 | 概要 | 確度 |
|---|---|---|
| テキスト | 短文。**500字まで** | ✅ |
| テキスト添付(長文) | **10,000字まで**。テキストのみの投稿に付けられる。太字・斜体・ハイライト・下線・取り消し線が使える | ✅ |
| 画像 | 1枚、またはカルーセル(複数枚) | ✅ |
| カルーセル | 画像・動画を混ぜて **2〜20件** | ✅ |
| 動画 | **最大5分** | ✅ |
| 投票 | **選択肢2〜4個、各25字まで**。テキストのみの投稿に付けられる | ✅ |
| GIF | API の提供元は GIPHY のみ | ✅ |
| 返信・引用 | 会話。引用は他人の投稿を埋め込んでコメント | ✅ |
| スレッド(連投) | 続きの投稿 | ⚪ |
| スポイラー | 文字(1投稿10か所まで)や画像・動画をぼかす | ✅ |
| ゴースト投稿 | テキストのみ。**24時間後に自動アーカイブ**。返信には使えない | ✅ |
| 位置情報タグ | 場所を付ける | ✅(API の `location_id`) |
| 国の限定 | 表示する国を指定 | ✅(API の `allowlisted_country_codes`) |

出典: [overview](https://developers.facebook.com/documentation/threads/overview.md)、[Posts](https://developers.facebook.com/documentation/threads/posts.md)、[Polls](https://developers.facebook.com/documentation/threads/create-posts/polls.md)、[Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md)、[Spoilers](https://developers.facebook.com/documentation/threads/create-posts/spoilers.md)、[Ghost posts](https://developers.facebook.com/documentation/threads/create-posts/ghost-posts.md)、[Publishing reference](https://developers.facebook.com/documentation/threads/reference/publishing.md)。いずれも API の仕様で、アプリでの表示名は ⚪ です。

### 投稿手順

1. 「＋」で新規投稿。テキストとメディアを追加。
2. 返信できる人、承認要否を選ぶ。
3. 広告・PR は表記(ブランドコンテンツ機能が使えるか要確認 ⚪)。
4. 投稿。API を使えば予約が可能([20-api/04-threads-api](../20-api/04-threads-api.md))。

さらに細かく分けると(⚪ 表記は変わる可能性):

1. 本文を書く(500字以内 ✅)。
2. 必要ならトピックタグを1つ付ける([03-text-hashtags-alt](03-text-hashtags-alt.md))。
3. 画像・動画を添付し、代替テキストを付ける。
4. 生成 AI で作った内容なら **AI ラベル** を付ける(投稿画面に AI ラベルの選択肢がある ✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md))。
5. 返信できる人・返信の承認を選ぶ([04-engagement](04-engagement.md))。
6. プレビューを確認して投稿する。

### 編集・予約・削除

| 操作 | 内容 | 確度 | 出典 |
|---|---|---|---|
| 編集 | 投稿から **15分以内**(2024年10月に5分から延長と報道) | 🟡 | [GIGAZINE](https://gigazine.net/gsc_news/en/20241002-threads-edit-limit-update-fediverse) |
| フェディバースへの共有 | 共有を有効にしている場合、編集期間が終わってから共有されるとする報道 | 🟡 | 同上 |
| 予約投稿(アプリ) | 2025年1月から利用可能。**最大75日先** まで。返信は予約できない | 🟡 | [TechCrunch](https://techcrunch.com/2025/01/23/threads-rolls-out-a-post-scheduler-markup-feature-and-more)、[MacRumors](https://macrumors.com/2025/01/24/threads-now-lets-you-schedule-posts) |
| 予約の手順 | 投稿画面の「…」メニューから「日時を指定」を選ぶ | 🟡 | 同上(表記は変わる可能性) |
| 予約投稿(API) | 外部ツールや自作の仕組みで公開時刻を制御 | ✅ | [20-api/04-threads-api](../20-api/04-threads-api.md) |
| 削除 | API での削除は 100件/24時間まで | ✅ | [overview](https://developers.facebook.com/documentation/threads/overview.md) |

## 運用方針

- Instagram と**役割分担**: Instagram=ビジュアル、Threads=会話・短い考え。
- 同じ内容の完全コピーは避ける。
- 1日の投稿数は少なめ・継続重視。API での公開は 250件/24時間が上限 ✅(公式の overview で確認。通常運用では十分)。

## 具体例

### 最初の自己紹介投稿(地域の店の例)

```
はじめまして。駅前で小さなパン屋をしています。
Threads では、焼き上がりの時間や、仕込みの裏話を書いていきます。
好きなパンを返信で教えてください!
```

- 何者か → 何を書くか → 返信しやすい質問、の順。

### 投票の例(イラストアカウント)

- 本文: 「次に描く季節はどれがいいですか?」
- 選択肢: 「春」「夏」「秋」「冬」(各25字以内 ✅)

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| Instagram の投稿をそのまま貼った | Threads 向けに短く、会話を誘う形に書き直す |
| 画像付き投稿に投票を付けようとした | 投票はテキストのみの投稿に付ける(✅) |
| 長文を本文に詰め込んで切れた | 本文は500字以内、長文はテキスト添付(10,000字)へ |
| 編集しようとしたら期限切れ | 編集は15分以内(🟡)。訂正は返信で追記 |
| フェディバース共有をよく分からずにオンにした | 共有の意味を確認し、不要ならオフ |

## 注意点

- 登録方法・予約・編集の条件はアプリの更新で変わります(🟡)。アプリの表示を優先してください。
- 位置情報タグは生活圏が推測される原因になります。自宅周辺では付けないでください([privacy](../01-common/privacy-and-personal-info.md))。

## チェックリスト

- [ ] 2段階認証を設定した
- [ ] プロフィールの名前・bio・リンクを Instagram と揃えた
- [ ] 公開範囲・メンション・隠しワードを設定した
- [ ] フェディバース共有のオン/オフを意識して選んだ
- [ ] 自己紹介の投稿を出した

## 関連ページ / 次に読む

- 次に読む: [02-media-specs](02-media-specs.md)、[03-text-hashtags-alt](03-text-hashtags-alt.md)
- [Threads API](../20-api/04-threads-api.md)、[Instagram の初期設定](../03-instagram/README.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | 文字数・上限(✅) |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | 投稿の種類、AI ラベル、GIF(✅) |
| https://developers.facebook.com/documentation/threads/create-posts.md | 2026-11-03 | フェディバース共有(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/polls.md | 2026-11-03 | 投票(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md | 2026-11-03 | テキスト添付(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/ghost-posts.md | 2026-11-03 | ゴースト投稿(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/spoilers.md | 2026-11-03 | スポイラー(✅) |
| https://developers.facebook.com/documentation/threads/reference/publishing.md | 2026-11-03 | 位置情報・国の限定(✅) |
| https://opentermsarchive.org/en/memos/threads-expands-profile-creation-beyond-instagram-users/ | 2026-11-03 | Instagram なしの登録(🟡) |
| https://www.engadget.com/social-media/threads-is-testing-facebook-account-sign-ups-191214734.html | 2026-11-03 | Facebook 登録の試験(🟡) |
| https://gigazine.net/gsc_news/en/20241002-threads-edit-limit-update-fediverse | 2026-11-03 | 編集15分(🟡) |
| https://techcrunch.com/2025/01/23/threads-rolls-out-a-post-scheduler-markup-feature-and-more | 2026-11-03 | 予約投稿(🟡) |
| https://macrumors.com/2025/01/24/threads-now-lets-you-schedule-posts | 2026-11-03 | 予約は最大75日先(🟡) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(登録方法の補足、プライバシー設定表、投稿の種類を ⚪ から ✅ に更新、詳細な投稿手順、編集・予約・削除、具体例、よくある失敗、チェックリスト)。API の公開上限 250件/24時間を 🟡 から ✅(公式 overview)に更新 |
