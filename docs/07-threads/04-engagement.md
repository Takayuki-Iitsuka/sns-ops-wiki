---
title: Threads 会話・運用
platform: threads
topic: engagement
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/threads/reply-management.md
  - https://developers.facebook.com/documentation/threads/reference/publishing.md
  - https://developers.facebook.com/documentation/threads/posts/quote-posts.md
---

# Threads の会話・運用

> **このページで分かること**: 返信範囲・返信の承認・非表示などの機能、DM・コミュニティ、返信の書き方と荒れたときの対応。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [01-setup-and-posting](01-setup-and-posting.md)

共通: [comments-and-engagement](../01-common/comments-and-engagement.md)

## 概要

Threads は会話を中心に設計されたサービスです。自分の投稿だけでなく、**他の人の投稿への返信** が知ってもらうきっかけになりやすいとされます(⚪)。

一方、Instagram のフォロワー以外の人にも表示されるため、知らない人からの返信も届きます。返信範囲・承認・非表示の機能を最初に覚えておきましょう。

## 用語

| 用語 | 意味 |
|---|---|
| reply control(返信範囲) | 誰が返信できるかの設定 |
| reply approval(返信の承認) | 返信を自分が承認するまで公開しない設定 |
| hide reply(返信の非表示) | 届いた返信を隠す |
| restrict(制限) | 相手に気づかれずに、相手の返信を自分と相手にだけ見せる機能(Instagram と同様とされる ⚪) |
| hidden words(隠しワード) | 指定した語を含む返信を見えにくくする機能 |
| quote(引用) | 他人の投稿を埋め込んでコメントする投稿 |

## 機能(⚪)

| 機能 | 使い方 |
|---|---|
| 返信範囲の設定 | 誰が返信できるかを限定(荒れ対策) |
| 返信の承認 | 返信を事前確認 |
| 制限/ブロック/ミュート | Instagram と連動 |
| 隠しワード | NG ワードの非表示 |
| 引用 | 意見の共有。煽りに注意 |

## 手順 / 仕様

### 公式の開発者文書で確認できた仕様(✅)

| 項目 | 内容 | 出典 |
|---|---|---|
| 返信範囲の選択肢 | すべての人(`everyone`)/ フォロー中の人(`accounts_you_follow`)/ メンションした人のみ(`mentioned_only`)/ 元の投稿者のみ(`parent_post_author_only`)/ フォロワーのみ(`followers_only`)の5つ | [Reply management](https://developers.facebook.com/documentation/threads/reply-management.md) |
| 返信の承認 | 有効にすると、返信は **承認されるまで非表示**。保留中・無視した返信を一覧できる | 同上 |
| 承認の制限 | ゴースト投稿には返信の承認を設定できない | 同上 |
| 返信の非表示 | **最上位の返信** を非表示にすると、その下の返信もまとめて非表示 | 同上 |
| 引用 | 他人の投稿を引用でき、取得時に引用投稿と分かる | [Quote Posts](https://developers.facebook.com/documentation/threads/posts/quote-posts.md) |
| API の返信上限 | 1,000件/24時間 | [20-api/04-threads-api](../20-api/04-threads-api.md) |

アプリでの表示名は ⚪(表記は変わる可能性)です。

### 返信範囲を設定する手順(⚪)

1. 投稿画面の下部にある「返信できる人」の表示を押す。
2. 範囲を選ぶ(すべての人・フォロー中・メンションした人 など)。
3. 返信を承認制にする場合は、同じ画面で承認の設定をオンにする。
4. 投稿後に変える場合は、投稿の「…」メニューから変更する(⚪)。

### DM・コミュニティ(🟡 報道)

| 機能 | 内容 | 出典 |
|---|---|---|
| DM(ダイレクトメッセージ) | 2025年(皇紀2685年・令和7年)7月に提供開始。18歳以上。当初は相互フォローなどに限定。エンドツーエンド暗号化ではないと報道 | [The Week](https://www.theweek.in/news/sci-tech/2025/07/02/meta-rolls-out-threads-d-ms-to-all-users-minus-end-to-end-encryption-instagram-social-media.html) |
| グループチャット | 2025年10月ごろから段階的に提供と報道 | 同上の続報(🟡) |
| コミュニティ | 2025年10月2日に発表。話題ごとの集まり。投稿はおすすめ・フォロー中のフィードにも出る | [TechCrunch](https://techcrunch.com/2025/10/02/threads-takes-on-x-with-new-communities-feature) |

日本での提供範囲・条件は ⚪ 要確認です。

## コツ

1. 会話を始める**質問**を投稿の1〜2割に。
2. 他者の投稿への**具体的な返信**を日課にする(宣伝のみは避ける)。
3. Instagram のフォロワーからの流入を想定し、**プロフィールの一貫性**を保つ。
4. 議論が荒れたら [crisis-response](../01-common/crisis-response.md)。
5. 返信は「感謝 → 答え → 次の問い」の順にすると会話が続きやすい(⚪)。

### 荒れたときの手順(⚪)

1. 返信範囲を「フォロー中」などに狭める。
2. 攻撃的な返信は非表示にする(最上位の返信を隠すと、その下もまとめて隠れる ✅)。
3. 繰り返す相手は制限またはブロック。規約違反は報告。
4. 事実誤認が広がっている場合は、訂正を1つの投稿にまとめる。

## 具体例

### 返信の文例

| 場面 | 文例 |
|---|---|
| 感想 | `読んでくださってありがとうございます!どのパンが気になりましたか?` |
| 質問 | `いい質問です。冷凍なら2週間を目安にしています。解凍のコツも今度投稿しますね。` |
| 他人の投稿への返信 | `うちも同じ失敗をしました。生地を休ませる時間を10分延ばしたら改善しましたよ。` |

### 避けたい返信

- 宣伝リンクだけの返信
- 相手の投稿を引用して揶揄する
- 同じ文面を多数の投稿に返信する

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 知らない人からの返信が多く疲れた | 返信範囲・隠しワードを使う |
| 承認待ちの返信を放置した | 1日1回、保留中の返信を確認する |
| 引用で反論して対立が広がった | 引用より個別の返信か、静観を選ぶ |
| DM で営業を一斉送信した | やめる。スパムとみなされる恐れ([07-policies-and-checklist](07-policies-and-checklist.md)) |

## 注意点

- 返信も公開情報です。個人情報や取引先の情報を書かないでください([privacy](../01-common/privacy-and-personal-info.md))。
- 返信の自動化(API)は誤判定のリスクがあります。自動で非表示にする場合も、人が定期的に確認してください([20-api/04-threads-api](../20-api/04-threads-api.md))。

## チェックリスト

- [ ] 返信範囲と承認の使い方を理解した
- [ ] 隠しワードを登録した
- [ ] 1日1回、返信と承認待ちを確認する時間を決めた
- [ ] 他人の投稿への返信を日課にした
- [ ] 荒れたときの手順を把握した

## 関連ページ / 次に読む

- 次に読む: [05-monetization](05-monetization.md)
- [comments-and-engagement](../01-common/comments-and-engagement.md)、[crisis-response](../01-common/crisis-response.md)
- [コミュニティ運営](../01-common/community-management.md)(別担当が作成予定)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/reply-management.md | 2026-11-03 | 返信範囲5種、承認、非表示(✅) |
| https://developers.facebook.com/documentation/threads/reference/publishing.md | 2026-11-03 | `reply_control`、`enable_reply_approvals`(✅) |
| https://developers.facebook.com/documentation/threads/posts/quote-posts.md | 2026-11-03 | 引用(✅) |
| https://www.theweek.in/news/sci-tech/2025/07/02/meta-rolls-out-threads-d-ms-to-all-users-minus-end-to-end-encryption-instagram-social-media.html | 2026-11-03 | DM(🟡 報道) |
| https://techcrunch.com/2025/10/02/threads-takes-on-x-with-new-communities-feature | 2026-11-03 | コミュニティ(🟡 報道) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、開発者文書で確認した返信範囲5種・承認・非表示 ✅、設定手順、DM・コミュニティ 🟡、荒れたときの手順、返信の文例、よくある失敗、チェックリスト) |
