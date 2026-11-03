---
title: Threads ルール・チェックリスト
platform: threads
topic: policy
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/create-posts.md
  - https://developers.facebook.com/documentation/threads/reference/publishing.md
---

# Threads のルールとチェックリスト

> **このページで分かること**: Threads で気をつける規約の領域、AI ラベル・PR・自動化の注意点、運用の各段階のチェックリスト。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [legal-compliance](../01-common/legal-compliance.md)

一次資料: Meta のコミュニティ規定、Instagram/Threads の利用規約、Threads API の利用規約(本文は未取得 #34)。

## 概要

Threads は Meta のサービスなので、基本的に **Instagram と同じ考え方のルール** が適用されると考えられます(⚪ 規約本文は未取得 #28)。違反すると投稿の削除や表示の制限、アカウントの停止につながることがあります(⚪)。

初心者が特に気をつけたいのは次の4つです。

1. 他人への攻撃・晒し・差別
2. 他人の画像・文章・音楽の無断使用
3. PR(広告)・AI 生成であることを隠すこと
4. 同じ内容の大量投稿や、規約に反する自動化

## 用語

| 用語 | 意味 |
|---|---|
| Community Guidelines(コミュニティ規定) | 利用者が守るべきルール |
| AI label(AI ラベル) | AI で作った内容であることを示す表示 |
| rate limit(レート制限) | 一定時間に実行できる回数の上限 |
| geo-gating(国の限定) | 投稿を表示する国を指定すること |
| fediverse(フェディバース) | Threads の投稿を共有できる、他の分散型 SNS |

## 注意領域(⚪ 一般論)

| 領域 | 要点 |
|---|---|
| 規約 | Instagram のルールに準ずる。ヘイト・嫌がらせ・誤情報 |
| API の自動化 | 利用規約・レート制限を守る([20-api](../20-api/README.md)) |
| 広告・PR | [legal-compliance](../01-common/legal-compliance.md) |
| 生成 AI | ラベル・規約は要確認 |

## 手順 / 仕様

### 公式の開発者文書で確認できたこと(✅)

| 項目 | 内容 | 出典 |
|---|---|---|
| AI ラベル | 投稿画面に AI ラベルの選択肢があり、API でも `is_made_with_ai` で付けられる。付けなくても **自動で AI ラベルが付く場合がある** | [Posts](https://developers.facebook.com/documentation/threads/posts.md) |
| API の公開上限 | 投稿 250件・返信 1,000件・削除 100件 / 24時間 | [overview](https://developers.facebook.com/documentation/threads/overview.md) |
| API の権限 | 投稿には `threads_basic` と `threads_content_publish`。審査前はテスターのアカウントにしか投稿できない | [Create Posts](https://developers.facebook.com/documentation/threads/create-posts.md) |
| フェディバース | 共有を有効にした利用者の対象投稿は、API 経由でもフェディバースに共有される | 同上 |
| 国の限定 | 表示する国を指定できる(`allowlisted_country_codes`) | [Publishing reference](https://developers.facebook.com/documentation/threads/reference/publishing.md) |
| リンク | 1投稿5つまで | [Posts](https://developers.facebook.com/documentation/threads/posts.md) |

### AI で作った投稿の扱い(手順)

1. 生成 AI で画像・文章を作ったら、投稿画面で AI ラベルを選ぶ(✅ 選択肢がある)。
2. 本文にも「AI で生成」などと書くと誤解を防げる(⚪)。
3. 実在の人物・団体と誤解される画像は作らない([ai-usage-policy](../01-common/ai-usage-policy.md)、[ai-rules-by-platform](../01-common/ai-rules-by-platform.md))。

### フェディバース共有の注意(⚪)

- 共有した投稿は Threads の外のサーバーにも届きます。削除しても、相手のサーバーに残る可能性があります(⚪ 一般的な仕組み)。
- 個人的な内容や、消すかもしれない投稿は共有をオフにしてから出すと安全です。

### 違反の通知を受けたとき(⚪)

1. 通知の内容(対象の投稿・理由)を記録する。
2. アプリの案内に従い、見直しを求める(異議申立て)。事実と根拠だけを書く。
3. 同じ種類の投稿を出さない。
4. 他の場所(note・メール・Instagram)で読者に連絡できるようにしておく([funnel](../30-strategy/02-funnel.md))。

## チェックリスト

- [ ] 1投稿1論点、文字数は余裕をもって
- [ ] タグは1つ(公式確認後に更新)
- [ ] 画像は 4:5 を基本、代替テキスト
- [ ] PR・広告の表記
- [ ] 返信範囲の設定
- [ ] 他サービスの文面のコピペでない

> 「タグは1つ」は、開発者文書で **1投稿に1つ** と確認できました(✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md))。

### 初期設定(一度だけ)

- [ ] 2段階認証を設定した([account-security](../01-common/account-security.md))
- [ ] プロフィールを Instagram と揃えた
- [ ] 隠しワード・メンションの範囲を設定した
- [ ] フェディバース共有のオン/オフを決めた

### 投稿前

- [ ] 本文500字以内、リンク5つ以内(✅)
- [ ] トピックタグは1つ、`.` と `&` を含まない(✅)
- [ ] 画像・動画に代替テキスト(1,000字以内 ✅)
- [ ] AI 生成なら AI ラベル
- [ ] 写り込み・位置情報を確認した([privacy](../01-common/privacy-and-personal-info.md))

### 投稿後

- [ ] 返信と承認待ちを確認した([04-engagement](04-engagement.md))
- [ ] 誤りがあれば15分以内に編集、過ぎたら返信で訂正(編集期限は 🟡)

### 週次・月次

- [ ] 週1回、インサイトを記録した([06-analytics-and-tips](06-analytics-and-tips.md))
- [ ] 月1回、規約・収益化の変更を確認した([05-monetization](05-monetization.md))
- [ ] 月1回、API 連携やツールの権限を見直した

## 具体例

| 場面 | 判断 |
|---|---|
| 生成 AI で作ったイラストを投稿 | AI ラベルを付け、本文にも明記 |
| 企業から商品を受け取って紹介 | 冒頭に PR 表記 |
| 同じ告知文を1日に何度も投稿 | スパムとみなされる恐れ。内容と時間を変える |
| 地域限定のお知らせ | 国の限定(API)は国単位。地域の店なら本文で地域を明記 |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| AI ラベルを付けずに AI 画像を投稿した | 付け直すか、本文で明記する。自動でラベルが付く場合もある(✅) |
| API の上限を超えてエラーになった | 24時間の上限(✅)を確認し、間隔を空ける |
| フェディバース共有中の投稿を消したのに残っていた | 共有先に残る可能性がある。共有の設定を見直す |

## 注意点

- このページは規約の要約ではありません。判断に迷ったら公式の規約・コミュニティ規定を読んでください(#28、#34)。
- 法律の観点は [legal-compliance](../01-common/legal-compliance.md) を参照してください。

## 関連ページ / 次に読む

- [08-faq](08-faq.md)(困ったとき)
- [legal-compliance](../01-common/legal-compliance.md)、[ai-rules-by-platform](../01-common/ai-rules-by-platform.md)、[crisis-response](../01-common/crisis-response.md)、[Threads API](../20-api/04-threads-api.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | API の上限(✅) |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | AI ラベル、トピックタグ、リンク(✅) |
| https://developers.facebook.com/documentation/threads/create-posts.md | 2026-11-03 | 権限、フェディバース(✅) |
| https://developers.facebook.com/documentation/threads/reference/publishing.md | 2026-11-03 | 国の限定(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、開発者文書で確認した事項 ✅、AI ラベルの手順、フェディバースの注意、違反時の手順、段階別チェックリスト、具体例、よくある失敗)。「タグは1つ」を開発者文書で確認 |
