---
title: X(旧 Twitter)概要
platform: x
topic: overview
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/fundamentals/counting-characters.md
  - https://docs.x.com/x-api/fundamentals/edit-posts.md
  - https://docs.x.com/developer-guidelines.md
---

# X(旧 Twitter)

> **このページで分かること**: X がどんなサービスで、何に向いているか。このフォルダのページをどの順番で読めばよいか。
>
> **対象**: X をこれから始める初心者 / 運用を見直したい中級者  **先に読むページ**: [はじめての SNS 運用](../00-meta/beginners-guide.md)(別担当が作成予定)

## 概要

X は、短い文章(ポスト)を中心に、画像・動画・投票などを投稿できるサービスです。2023年(皇紀2683年・令和5年)に名称が Twitter から X に変わりました(⚪ 一般知識)。

短文・即時性・拡散(リポスト)に強く、日本では利用者が多いため、速報・話題・コミュニティ形成に向くとされます(⚪)。

| 項目 | 内容 |
|---|---|
| 主な形式 | 短文ポスト、画像、動画、GIF、投票、スレッド |
| 強み | 拡散力、リアルタイム性、検索 |
| 弱み | 流れが速い、炎上リスク、アルゴリズムと有料機能の影響 |
| 向く用途 | 認知、情報発信、交流、告知 |
| 向かない用途 | 長く残したい解説(note やブログの方が探されやすい)、写真の世界観づくり(Instagram の方が得意) ⚪ |

### X の基本ルールをひと目で

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| 1ポストの文字数 | 重み付きで **280**。日本語(全角)は1字=2なので **約140字** | ✅ | [docs.x.com Counting Characters](https://docs.x.com/fundamentals/counting-characters.md) |
| URL | 長さに関係なく **23字** として数える | ✅ | 同上 |
| 画像 | 1ポストに **写真4枚まで**、または GIF 1つ、または動画1つ | ✅(API) | [20-api/02-x-api](../20-api/02-x-api.md) |
| 編集 | 投稿から **30分以内に5回まで** | ✅(API 文書) | [docs.x.com Edit Posts](https://docs.x.com/x-api/fundamentals/edit-posts.md) |
| 長文 | Premium で **最大25,000字** | 🟡 | [help.x.com X Premium how to](https://help.x.com/en/using-x/x-premium-how-to) |

## 用語

旧名称と現在の名称が混在しているので、最初に覚えておくと迷いません。

| 用語 | 意味 |
|---|---|
| post(ポスト) | 投稿のこと。旧名称は「ツイート」 |
| repost(リポスト) | 他人のポストを自分のフォロワーに再共有すること。旧名称は「リツイート」 |
| quote(引用ポスト) | 他人のポストを埋め込み、自分のコメントを付けて投稿すること |
| reply(返信、リプライ) | ポストへの返事 |
| thread(スレッド) | 自分のポストに自分で返信をつなげた、連続した投稿 |
| impression(インプレッション) | ポストが画面に表示された回数 |
| Premium(プレミアム) | X の有料プラン。長文・長い動画・編集などが使える(料金は [40-pricing/01-x-and-grok](../40-pricing/01-x-and-grok.md)) |
| @ID(ユーザー名、ハンドル) | `@` から始まるアカウント固有の名前 |

> 用語: 旧名称の「ツイート」は現在「ポスト」、「リツイート」は「リポスト」。

## 読む順番(初心者向け)

1. **最初の1日**: [01-account-setup](01-account-setup.md) でプロフィールと安全設定を済ませる。
2. **最初の1週間**: [02-posting](02-posting.md) → [04-text-hashtags](04-text-hashtags.md) → [05-alt-text](05-alt-text.md) で投稿の基本を覚える。
3. **画像・動画を作るとき**: [03-media-specs](03-media-specs.md)。
4. **反応が来はじめたら**: [06-engagement](06-engagement.md) と [10-policies](10-policies.md)。
5. **1か月たったら**: [08-analytics](08-analytics.md) と [09-tips](09-tips.md) で振り返る。
6. **収益を考えるとき**: [07-monetization](07-monetization.md)、月額購読は [12-subscriptions](12-subscriptions.md)。
7. **困ったとき**: [13-faq](13-faq.md)。

## ページ一覧

1. [01-account-setup](01-account-setup.md) 初期設定
2. [02-posting](02-posting.md) 投稿ルート
3. [03-media-specs](03-media-specs.md) 画像・動画仕様
4. [04-text-hashtags](04-text-hashtags.md) 文字数・ハッシュタグ
5. [05-alt-text](05-alt-text.md) 画像説明文
6. [06-engagement](06-engagement.md) コメント・返信
7. [07-monetization](07-monetization.md) 収益化
8. [08-analytics](08-analytics.md) 分析
9. [09-tips](09-tips.md) コツ
10. [10-policies](10-policies.md) ルール
11. [11-checklist](11-checklist.md) 運用チェックリスト
12. [12-subscriptions](12-subscriptions.md) — Subscriptions(月額購読)の資格・手数料・機能
13. [13-faq](13-faq.md) よくある質問とトラブル対処

## 注意点

- X は仕様変更が速いサービスです。アプリのボタン名や場所は、このページの記載と違うことがあります(⚪)。
- 公式ヘルプ(`help.x.com`)は自動取得できないため、ヘルプ由来の数値は 🟡 にしています。開発者向け文書(`docs.x.com`)で確認できたものは ✅ です。
- API の数値(✅)と、アプリで投稿するときの上限は同じとは限りません。

## 関連ページ / 次に読む

- [01-account-setup](01-account-setup.md)
- [X API](../20-api/02-x-api.md)、[料金](../40-pricing/01-x-and-grok.md)
- [用語集](../00-meta/glossary.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/fundamentals/counting-characters.md | 2026-11-03 | 文字数の数え方(✅) |
| https://docs.x.com/x-api/fundamentals/edit-posts.md | 2026-11-03 | 編集のルール(✅) |
| https://docs.x.com/developer-guidelines.md | 2026-11-03 | 開発者ガイドライン(✅) |
| https://help.x.com/en/using-x/x-premium-how-to | 2026-11-03 | 検索要約のみ(🟡) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(基本ルール表、用語、読む順番、12-subscriptions と 13-faq を索引に追加。ページ一覧の並びを修正) |
