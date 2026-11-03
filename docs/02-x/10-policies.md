---
title: X ルール・ポリシー
platform: x
topic: policy
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/developer-guidelines.md
  - https://docs.x.com/x-api/posts/create-or-edit-post.md
  - https://docs.x.com/x-api/fundamentals/data-dictionary.md
  - https://help.x.com/en/using-x/automated-account-labels
---

# X のルール・ポリシー

> **このページで分かること**: X で気をつけるべき規約の領域、自動化・PR・AI 生成の開示、違反の通知を受けたときの対応。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [legal-compliance](../01-common/legal-compliance.md)

規約は頻繁に更新されます。公式の「Xルール」「利用規約」を一次資料として確認(入口: https://help.x.com/ja。作成時は bot 確認で本文を取得できず、未確認 #28)。

## 概要

X には、すべての利用者が守る「X ルール」と「利用規約」があり、違反すると **表示の制限・投稿の削除・アカウントのロックや凍結** になることがあります(⚪)。

初心者が特に気をつけたいのは次の4つです。

1. **スパム**: 同じ内容の連投、無関係なタグ、大量のメンション
2. **権利**: 他人の画像・文章・音楽の無断使用
3. **開示**: PR(広告)・AI 生成・bot(自動化)であることを隠さない
4. **人への攻撃**: 嫌がらせ・差別・個人情報の晒し

## 用語

| 用語 | 意味 |
|---|---|
| platform manipulation(プラットフォーム操作) | 不正な方法で表示や反応を水増しすること |
| suspension(凍結) | アカウントが使えなくなる措置 |
| appeal(異議申立て) | 措置が誤りだと考えるときに見直しを求めること |
| Automated label(自動化ラベル) | bot アカウントであることを示すプロフィールの表示 |
| Parody label(パロディラベル) | パロディアカウントであることを示す表示 |
| paid partnership(有料提携) | 報酬を受けた PR 投稿 |

## 注意すべき領域(⚪ 一般論)

| 領域 | 要点 | 運用での注意 |
|---|---|---|
| スパム・プラットフォーム操作 | 自動化、大量フォロー、同一内容の連投、複数アカウントでの水増し | 同じ画像・文面の連投、宣伝の反復 |
| 嫌がらせ・ヘイト | 禁止 | 論争が荒れたときの対応 |
| センシティブメディア | 設定が必要な場合あり | 戦闘・流血の描写を画像にするとき |
| 著作権 | 権利者からの申立てで削除あり | イラスト・写真・翻訳文の引用([image-sources](../01-common/image-sources-and-copyright.md)) |
| なりすまし | 禁止。パロディはラベル要件あり | 公的機関・他人を名乗らない |
| 広告・案件 | [legal-compliance](../01-common/legal-compliance.md) | 書籍紹介のアフィリエイト |
| 自動化ボット | ラベル・規約要件 | 定期投稿ボットの導入前に規約確認 |
| 生成 AI | ラベル・規約は要確認 | [ai-usage-policy](../01-common/ai-usage-policy.md) |
| 収益化ポリシー | プログラムごとの追加規約 | [07-monetization](07-monetization.md) |

## 手順 / 仕様

### 公式資料で確認できた要件(✅ docs.x.com)

| 項目 | 内容 | 出典 |
|---|---|---|
| 自動化アカウントのラベル | bot は **「Automated」ラベルを表示** し、bio に bot であることと運営者を書き、人が管理するアカウントと関連付ける | [開発者ガイドライン](https://docs.x.com/developer-guidelines.md) |
| 非 API の自動化 | ブラウザ自動操作・スクレイピングは **永久凍結** | 同上 |
| スパムの例 | 複数アカウントで同じ内容、偽の反応、トレンド操作、大量投稿、求められていない自動返信・一斉 DM | 同上 |
| いいね | 本人の操作でなければならない。自動・大量・無差別のいいねは禁止 | 同上 |
| レート制限 | 回避・悪用しない | 同上 |
| PR の開示 | 投稿時に `paid_partnership` で有料提携を示せる | [Create or Edit Post](https://docs.x.com/x-api/posts/create-or-edit-post.md) |
| AI 生成の開示 | 投稿時に `made_with_ai` で AI 生成メディアを含むことを示せる | 同上 |
| パロディ | ユーザー情報に「Parody ラベルの有無」の項目がある | [Data Dictionary](https://docs.x.com/x-api/fundamentals/data-dictionary.md) |

上の多くは開発者(API 利用者)向けの文書ですが、自動化・スパムの考え方は通常の運用にも当てはまります。

### bot アカウントにラベルを付ける手順(🟡)

1. bot アカウントでログインし、設定のアカウント情報から「自動化」の項目を開く(🟡 解説記事による。表記は変わる可能性)。
2. 管理者(人が運用するアカウント)を指定して接続する。
3. プロフィールの名前の下に「自動化」ラベルが出ることを確認する(🟡 [help.x.com 自動化ラベル](https://help.x.com/en/using-x/automated-account-labels))。

## 違反したとき

1. 通知の内容(違反とされた投稿・規約条項)を記録する。
2. 異議申立てフォームを使い、事実を簡潔に説明する。
3. 同種の投稿を再び出さない。
4. 凍結に備え、**note・メール・Instagram に読者の逃げ道**を用意([funnel](../30-strategy/02-funnel.md))。

### 異議申立ての文例(⚪)

```
対象の投稿: (投稿の URL)
説明: この画像は自分で撮影した写真で、第三者の権利を侵害していません。
撮影日と元データを保管しています。見直しをお願いします。
```

- 感情的にならず、事実と根拠だけを書きます。
- 取引先名・個人情報は書きません。

## 平常時の備え

- 規約の更新通知を受け取る(メール)。
- 月1回、[verification-queue](../00-meta/verification-queue.md) に変更を追記。
- 外部ツールの連携は最小限。
- 投稿データのバックアップを定期的に取る([data-backup-and-portability](../01-common/data-backup-and-portability.md))。

## 具体例

| 場面 | 判断 |
|---|---|
| 新商品の告知を、1時間おきに同じ文面で10回投稿 | スパムの恐れ。内容を変え、間隔を空ける |
| 企業から商品をもらって紹介 | PR 表記が必要([legal-compliance](../01-common/legal-compliance.md)) |
| 生成 AI で作った画像を投稿 | AI 生成であることを明記([ai-rules-by-platform](../01-common/ai-rules-by-platform.md)) |
| 天気を毎朝自動投稿する bot | 自動化ラベル・bio の記載が必要(✅) |
| 有名人の名前でアカウントを作る | なりすまし。パロディでもラベルが必要 |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 外部ツールの「自動いいね」を使ってロックされた | すぐ連携を解除し、パスワードを変更 |
| 他人のイラストを「拾い画」として投稿した | 削除し、今後は許可を得たもの・自作のみ使う |
| PR 表記を後から付け忘れに気づいた | すぐ追記・訂正ポスト |
| 通知を読まずに同じ投稿を繰り返した | 通知を記録し、原因を特定してから投稿を再開 |

## 注意点

- このページは公式規約の要約ではなく、注意点の整理です。判断に迷ったら必ず公式ページを読んでください(#28)。
- 法律に関わること(景品表示法・著作権法など)は [legal-compliance](../01-common/legal-compliance.md) を参照してください。

## チェックリスト

- [ ] 同じ内容を連投していない
- [ ] 他人の画像・文章を許可なく使っていない
- [ ] PR・AI 生成・bot を開示している
- [ ] 外部ツールの自動化機能を確認した
- [ ] 読者の逃げ道(note・メール)を用意した

## 関連ページ / 次に読む

- 次に読む: [11-checklist](11-checklist.md)
- [legal-compliance](../01-common/legal-compliance.md)、[ai-rules-by-platform](../01-common/ai-rules-by-platform.md)、[crisis-response](../01-common/crisis-response.md)、[05-risk-register](../30-strategy/05-risk-register.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/developer-guidelines.md | 2026-11-03 | 自動化・スパム・いいねのルール(✅) |
| https://docs.x.com/x-api/posts/create-or-edit-post.md | 2026-11-03 | `paid_partnership`、`made_with_ai`(✅) |
| https://docs.x.com/x-api/fundamentals/data-dictionary.md | 2026-11-03 | Parody ラベルの項目(✅) |
| https://help.x.com/en/using-x/automated-account-labels | 2026-11-03 | 自動化ラベル(🟡 検索要約) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、公式の開発者文書で確認できた要件 ✅、bot ラベルの手順 🟡、異議申立ての文例、具体例、よくある失敗、チェックリスト) |
