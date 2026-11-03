---
title: Threads 分析とコツ
platform: threads
topic: analytics
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/threads/insights.md
  - https://sproutsocial.com/insights/threads-metrics/
  - https://techcrunch.com/2025/01/23/threads-rolls-out-a-post-scheduler-markup-feature-and-more
---

# Threads の分析とコツ

> **このページで分かること**: Threads のインサイトで見られる指標の意味、見る場所、週次の振り返り手順と運用のコツ。
>
> **対象**: 投稿を始めて2〜4週間の初心者  **先に読むページ**: [analytics-kpi](../01-common/analytics-kpi.md)

共通: [analytics-kpi](../01-common/analytics-kpi.md)

## 概要

Threads には **インサイト(分析画面)** があり、閲覧数・反応・フォロワーの推移を見られます。API でも同じような指標を取得できます(✅)。

分析で知りたいのは「どの投稿が会話を生んだか」です。Threads は会話のサービスなので、**返信数** を特に重視すると方針が立てやすくなります(⚪)。

## 用語

| 用語 | 意味 |
|---|---|
| views(閲覧数) | 投稿が表示・再生された回数 |
| replies(返信) | 投稿への返信の数 |
| reposts / quotes(リポスト / 引用) | 再共有 / コメント付き共有の数 |
| shares(シェア) | 投稿が共有された数 |
| clicks(クリック) | 共有した URL が押された数 |
| follower demographics(フォロワー属性) | フォロワーの国・都市・年齢・性別の内訳 |

## 指標(⚪)

| 指標 | 意味 |
|---|---|
| 閲覧数 | 投稿が見られた回数 |
| いいね・返信・リポスト・引用 | 反応の種類 |
| フォロワー増 | 成長 |
| プロフィールへのアクセス | 興味 |

API でインサイト(閲覧・反応など)を取得できる([20-api/04-threads-api](../20-api/04-threads-api.md))。

### 公式の開発者文書で確認できた指標(✅)

**投稿ごと(メディアのインサイト)**

| 指標 | 定義・注意 |
|---|---|
| `views` | 投稿が再生・表示された回数。**開発中(in development)の指標** |
| `likes` | いいねの数 |
| `replies` | 返信の数。元の投稿なら返信の合計、返信自体なら直接の返信のみ |
| `reposts` | リポストの数 |
| `quotes` | 引用の数 |
| `shares` | シェアの数。**開発中の指標** |

**アカウント全体(ユーザーのインサイト)**

| 指標 | 定義・注意 |
|---|---|
| `views` | **プロフィール** が見られた回数(日ごとの推移) |
| `likes` / `replies` / `reposts` / `quotes` | 投稿全体の合計(返信は最上位の返信のみ) |
| `clicks` | 共有した URL のクリック数 |
| `followers_count` | フォロワー数 |
| `follower_demographics` | 国・都市・年齢・性別の内訳。**フォロワー100人以上** が必要 |

- 2024年(皇紀2684年・令和6年)4月13日より前の期間は指定できない(✅)。
- 出典: [Threads Insights API](https://developers.facebook.com/documentation/threads/insights.md)。

## 手順 / 仕様

### アプリでインサイトを見る(🟡)

| 項目 | 内容 | 確度 | 出典 |
|---|---|---|---|
| 場所 | プロフィール画面のインサイトのアイコン、Web は threads.com/insights とする解説 | 🟡 | [Sprout Social](https://sproutsocial.com/insights/threads-metrics/) |
| 期間 | 過去 **90日** まで | 🟡 | 同上 |
| 属性 | フォロワー100人以上で表示 | 🟡(API では ✅) | 同上 |
| 投稿ごとの指標 | 2025年(皇紀2685年・令和7年)1月から投稿ごとの指標を表示 | 🟡 | [TechCrunch](https://techcrunch.com/2025/01/23/threads-rolls-out-a-post-scheduler-markup-feature-and-more) |

アイコンの位置・表記は変わる可能性があります(⚪)。

### 週次の振り返り手順(⚪)

1. 毎週同じ曜日に、直近7日の投稿の「閲覧・いいね・返信・リポスト・引用」を表に記録する。
2. **返信率**(返信 ÷ 閲覧)を計算する。
3. 返信が多かった投稿3つの共通点(問いの形、テーマ、時間帯)を一言で書く。
4. 次週に試すことを1つ決める。
5. 月1回、フォロワー数とリンクのクリック数を確認する。

[weekly-review](../../templates/weekly-review.md) を使うと記録が楽です。

### 計算例(架空の数値)

| 投稿 | 閲覧 | 返信 | 返信率 |
|---|---|---|---|
| 質問で終わる投稿 | 1,200 | 24 | 2.0% |
| お知らせの投稿 | 2,000 | 4 | 0.2% |

→ 閲覧はお知らせの方が多いが、会話を生んだのは質問の投稿、と読めます。

## コツ(⚪)

1. 1投稿1論点。結論を先に。
2. 質問で終える。
3. Instagram の投稿を**補足**する形で使う。
4. 反応の良い投稿の型を記録([weekly-review](../../templates/weekly-review.md))。
5. 一定期間は**頻度を変えて**比較(週3 vs 週7)。
6. 自分の投稿より先に、**他の人の投稿へ丁寧に返信** する時間をとる([04-engagement](04-engagement.md))。
7. トピックタグは1つなので、柱ごとに使うタグを決めておく([03-text-hashtags-alt](03-text-hashtags-alt.md))。

## 具体例

| 気づき(例) | 次の行動 |
|---|---|
| 失敗談の投稿は返信が多い | 週1回は失敗談+質問の形にする |
| 画像付きより文字だけの方が返信が多い | 会話を狙う日は文字だけにする |
| リンクのクリックが少ない | リンクの前に「何が得られるか」を書く |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 閲覧数だけ見て判断した | 返信・引用など会話の指標も見る。`views` は開発中の指標(✅) |
| フォロワー属性が表示されない | フォロワー100人以上が必要(✅ API) |
| 頻度とテーマを同時に変えた | 1週に変えるのは1つだけ |
| 記録をためてから一気に見た | 週1回、同じ曜日に記録する |

## 注意点

- 指標の定義は API 文書(✅)に基づきます。アプリの表示とは異なる場合があります(⚪)。
- 実際の運用数値はこのリポジトリに書かず、手元の表に記録してください。

## チェックリスト

- [ ] 週1回、閲覧・返信などを記録した
- [ ] 返信率を計算した
- [ ] 返信が多かった投稿の共通点を書いた
- [ ] 次週に試すことを1つ決めた

## 関連ページ / 次に読む

- 次に読む: [07-policies-and-checklist](07-policies-and-checklist.md)
- [analytics-kpi](../01-common/analytics-kpi.md)、[01-goals-kpi-roadmap](../30-strategy/01-goals-kpi-roadmap.md)、[Threads API](../20-api/04-threads-api.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/insights.md | 2026-11-03 | 指標の定義、100人の条件、期間の制限(✅) |
| https://sproutsocial.com/insights/threads-metrics/ | 2026-11-03 | アプリのインサイト(🟡 解説記事) |
| https://techcrunch.com/2025/01/23/threads-rolls-out-a-post-scheduler-markup-feature-and-more | 2026-11-03 | 投稿ごとの指標(🟡 報道) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、開発者文書で確認した指標 ✅、アプリでの見方 🟡、週次の手順、計算例、コツの追加、具体例、よくある失敗、チェックリスト) |
