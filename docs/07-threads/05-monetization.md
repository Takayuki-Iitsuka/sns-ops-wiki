---
title: Threads 収益化
platform: threads
topic: monetization
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://www.engadget.com/meta-is-offering-some-creators-thousands-of-dollars-in-bonuses-for-threads-posts-193950157.html
---

# Threads の収益化

> **このページで分かること**: Threads の収益化の現状(公式プログラムは未確認)と、他サービスへの導線で収益を作る設計。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [収益化の比較](../01-common/monetization-comparison.md)

> **公式の収益化プログラムの有無・条件は未確認**です (#34)。確認できるまで、収益化は「他サービスへの誘導」で設計します。

## 概要

2026年(皇紀2686年・令和8年)11月時点で、日本の一般の利用者が Threads から直接お金を受け取れる公式の仕組みは、**公式資料では確認できていません**(⚪ #34)。

そのため Threads は「収益の入口(認知・信頼づくり)」と考え、収益は note・YouTube・自社サイト・物販など **他の場所で得る** 設計にします。

## 用語

| 用語 | 意味 |
|---|---|
| bonus program(ボーナスプログラム) | 投稿の成果に応じて運営が報奨金を払う仕組み |
| funnel(ファネル、導線) | 知る → 興味を持つ → 行動する、の流れ |
| branded content(ブランドコンテンツ) | 企業から依頼・報酬を受けた投稿(PR) |
| link in bio(プロフィールのリンク) | プロフィールに置く外部リンク |

## 現時点の設計(⚪)

| 手段 | 方法 |
|---|---|
| 導線 | プロフィールのリンクから note・YouTube・書籍・通販へ |
| 案件 | ブランド案件(広告表記必須) |
| 自前の資産 | Threads は会話・認知に使い、収益は note・YouTube で |

## 手順 / 仕様

### 導線を作る手順(⚪)

1. **収益の場所を1つ決める**(例: note の有料記事、通販ページ)。
2. **プロフィールのリンク** をそこに向ける。複数あるならリンク集ページを1つ作る([link-in-bio-and-utm](../01-common/link-in-bio-and-utm.md))。
3. **計測用の UTM パラメータ** を付け、Threads からの流入を測る。
4. 投稿では、普段は価値ある情報を出し、**5〜10回に1回** 程度だけ案内する(⚪ 目安)。
5. 案内の投稿はテキストのみにすると、最初の URL がリンクプレビューになる(✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md))。リンクは1投稿5つまで(✅)。
6. 月1回、リンクのクリック数と売上の関係を振り返る([06-analytics-and-tips](06-analytics-and-tips.md))。

### PR 案件を受けるとき

1. 依頼内容・報酬・表記の方法を文書で確認する([07-sponsorship-and-media-kit](../30-strategy/07-sponsorship-and-media-kit.md))。
2. 投稿の冒頭に「PR」「広告」など分かる表記を入れる([legal-compliance](../01-common/legal-compliance.md))。
3. Threads にブランドコンテンツ用の機能があるかは ⚪ 要確認。
4. 生成 AI で作った画像を使う場合は AI ラベルを付ける(✅ [Posts](https://developers.facebook.com/documentation/threads/posts.md))。

## 確認項目

1. Meta の収益化ポリシーに Threads が含まれるか。
2. 地域(日本)での提供と条件(フォロワー数・年齢)。
3. 投げ銭/サブスクリプション機能の有無。

確認後、このページを更新し、[monetization-comparison](../01-common/monetization-comparison.md) に反映します。

## 報道(🟡)

- Threads は 2026年4月時点で**クリエイター収益シェアのプログラムを主に米国などで開始**。**日本は対象外**とする記事。
- 日本での提供は公式で確認する(#34)。

### その他の報道(🟡、記事により不一致)

| 内容 | 出典 |
|---|---|
| 2024年(皇紀2684年・令和6年)に、招待制のボーナスプログラムを一部のクリエイター(主に米国)で試験 | [Engadget](https://www.engadget.com/meta-is-offering-some-creators-thousands-of-dollars-in-bonuses-for-threads-posts-193950157.html) |
| ボーナスプログラムは終了したとする記事があるが、時期は記事により異なる | [解説記事](https://creatorstack-io.pages.dev/blog/threads-creator-bonuses-killed-monetization-guide-2026/)(🟡) |
| 2025年(皇紀2685年・令和7年)1月に米国と日本で広告のテストを開始とする記事 | [解説記事](https://www.makeinfluence.com/en/academy/threads-as-an-influencer-marketing-channel-whats-actually-there-in-2026)(🟡) |
| 「2026年時点でクリエイター向けの収益分配・投げ銭・有料購読はない」とする記事もある(上の「4月に開始」とは矛盾) | [解説記事](https://posteverywhere.ai/blog/can-you-make-money-on-threads)(🟡) |

報道どうしで食い違いがあるため、**公式の発表で確認するまで、収益化の前提にしない** でください。

## 具体例(⚪ 汎用の設計例)

| アカウント | Threads の使い方 | 収益の場所 |
|---|---|---|
| 料理アカウント | 毎日の小さなコツと質問 | note の有料レシピ集 |
| イラストアカウント | 制作の悩み・過程の共有 | 作品販売サイト・依頼受付 |
| 地域の店 | 仕込みの裏話、焼き上がり情報 | 来店・通販 |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 海外の報道を見て、日本でも収益化できると思い込んだ | アプリのプロフェッショナル向けメニューと公式発表で確認する |
| 毎回の投稿でリンクを貼り、反応が落ちた | 案内は5〜10回に1回程度にし、普段は価値ある投稿を |
| PR 表記を忘れた | すぐ追記し、訂正する |

## 注意点

- 収益化の状況は変わりやすい領域です。このページは 🟡/⚪ が中心です。
- 実際の収益額(非公開の数値)はこのリポジトリに書かないでください。

## チェックリスト

- [ ] 収益の場所を1つ決めた
- [ ] プロフィールのリンクを設定し、UTM を付けた
- [ ] 案内投稿の頻度を決めた
- [ ] PR 表記と AI ラベルのルールを決めた
- [ ] 公式の収益化の発表を月1回確認する

## 関連ページ / 次に読む

- 次に読む: [06-analytics-and-tips](06-analytics-and-tips.md)
- [monetization-comparison](../01-common/monetization-comparison.md)、[funnel](../30-strategy/02-funnel.md)、[03-monetization-roadmap](../30-strategy/03-monetization-roadmap.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | リンクプレビュー・リンク数・AI ラベル(✅) |
| https://www.engadget.com/meta-is-offering-some-creators-thousands-of-dollars-in-bonuses-for-threads-posts-193950157.html | 2026-11-03 | ボーナスプログラムの試験(🟡 報道) |
| https://creatorstack-io.pages.dev/blog/threads-creator-bonuses-killed-monetization-guide-2026/ | 2026-11-03 | ボーナス終了とする記事(🟡 解説記事) |
| https://www.makeinfluence.com/en/academy/threads-as-an-influencer-marketing-channel-whats-actually-there-in-2026 | 2026-11-03 | 広告テスト(🟡 解説記事) |
| https://posteverywhere.ai/blog/can-you-make-money-on-threads | 2026-11-03 | 収益分配なしとする記事(🟡 解説記事) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、導線を作る手順、PR 案件の手順、報道の整理(不一致を明記)、具体例、よくある失敗、チェックリスト) |
