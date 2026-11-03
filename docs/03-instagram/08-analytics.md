---
title: Instagram インサイト
platform: instagram
topic: analytics
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md
  - https://developers.facebook.com/documentation/instagram-platform/api-reference/instagram-user/insights.md
  - https://developers.facebook.com/documentation/instagram-platform/changelog.md
---

# Instagram インサイト(分析)

> **このページで分かること**: インサイト(分析画面)の開き方、主な指標の意味(公式定義)、指標の変更点、週次の見方と改善の手順。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [analytics-kpi](../01-common/analytics-kpi.md)

共通: [analytics-kpi](../01-common/analytics-kpi.md)

## 概要

インサイト(Insights)は、投稿がどれだけ見られ、どんな反応があったかを確認できる分析機能です。**プロアカウントでのみ**使えます(⚪ アプリ。API はプロアカウントが前提 ✅)。

分析の目的は「数字を眺めること」ではなく、**次に作る投稿を決めること**です。初心者は次の3つだけ毎週見れば十分です(⚪)。

1. **閲覧数(views)とリーチ**: どれだけ届いたか
2. **保存・シェア**: 役に立った・人に勧めたいと思われたか
3. **フォロー数の増減**: どの投稿でフォローが増えたか

## 用語

| 用語 | 意味 |
|---|---|
| views(閲覧数・再生数) | コンテンツが再生・表示された回数 |
| reach(リーチ) | コンテンツを1回以上見た**ユニーク**(重複なし)アカウント数。推定値 |
| impressions(インプレッション) | 表示回数。**API では廃止**され views に置き換え(下記) |
| interactions(インタラクション) | いいね・保存・コメント・シェアなどの反応の合計 |
| accounts engaged(反応したアカウント) | 反応したアカウントの数 |
| profile activity(プロフィールのアクティビティ) | 投稿を見た後にプロフィールで取った行動(リンクのタップ、電話など) |
| skip rate(スキップ率) | リールが冒頭3秒以内に飛ばされた割合 |

## 手順 / 仕様

### 見る場所(⚪ メニュー名は変わる可能性)

- プロアカウントのプロフィール画面 →「インサイト」または「プロフェッショナルダッシュボード」⚪
- 各投稿の下の「インサイトを見る」
- パソコンでは Meta Business Suite からも確認できます(⚪)。

### 主な指標(公式の定義 ✅)

出典: [IG Media Insights](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md)、[IG User Insights](https://developers.facebook.com/documentation/instagram-platform/api-reference/instagram-user/insights.md)。

| 指標 | 意味 | 使い方 |
|---|---|---|
| 閲覧数(views) | Instagram で再生・表示された回数(開発中の指標) | 露出量 |
| リーチ | 見たユニークアカウント数(推定値) | 広がり |
| インプレッション/表示回数 | 総表示回数(名称・定義が変更される場合あり)。**API では廃止**(下記) | 露出量(過去データの比較用) |
| 保存 | 保存数 | 有益性 |
| シェア | 共有数 | 拡散 |
| リポスト | リポスト数(削除分を差し引き) | 拡散 |
| プロフィールへのアクセス | プロフィールが訪問された回数 | 興味 |
| フォロワー増減 | フォローされた数・解除された数(フォロワー100人未満の場合は API で取得不可) | 成長 |
| 平均再生時間(リール) | 1回あたりの平均再生時間 | 動画構成の改善 |
| 視聴維持率(リール) | どこまで見られたか(⚪ アプリの表示名) | 動画構成の改善 |
| スキップ率(リール) | 冒頭3秒以内に飛ばされた割合(推定・開発中) | 冒頭の改善 |
| リンクのクリック(ストーリーズ) | リンクスタンプなどのタップ数 | 導線の効果 |

### 指標の変更点(✅)

| 時期 | 変更 | 出典 |
|---|---|---|
| 2024年(皇紀2684年・令和6年)7月2日以降の投稿 | 投稿単位の `impressions` が廃止 | [IG Media Insights](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md) |
| 2025年(皇紀2685年・令和7年)4月21日 | アカウント単位の `impressions` が全バージョンで廃止。代わりに `views` | [IG User Insights](https://developers.facebook.com/documentation/instagram-platform/api-reference/instagram-user/insights.md) |
| 2025年12月3日 | `reels_skip_rate`、`reposts`、Facebook での再生(`facebook_views`)などを追加 | [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md) |
| 2026年(皇紀2686年・令和8年)4月22日 | 広告・Facebook を含む合計値(`total_views` など)を追加 | 同上 |

→ 過去のレポートと比べるときは、**「インプレッション」と「閲覧数」は別の指標**として扱います。

### データの注意点(✅ API の制限事項)

- 指標のデータは**最大48時間遅れる**ことがあります。投稿直後の数字は確定値ではありません。
- 指標データは**最大2年間**保存されます。長期比較のために、月1回は数字を記録しておきます。
- いいね・コメント・閲覧数などは**オーガニック(広告以外)のみ**の値です(合計値の指標を除く)。
- ストーリーズの指標は**24時間**しか取得できません。
- 年齢・地域などの属性は**上位45件**のみで、合計がフォロワー数と一致しないことがあります。

### 週次の見方(手順 ⚪)

1. 先週の投稿を一覧にし、**閲覧数・保存・シェア・フォロー**を記録します([weekly-review](../../templates/weekly-review.md))。
2. 閲覧数に対する保存・シェアの割合が高い投稿を「当たり」とします。
3. 当たりの投稿の**型**(テーマ・形式・1枚目・冒頭)を書き出します。
4. 次の週に同じ型で1〜2本作ります。
5. リールのスキップ率が高いものは、冒頭の1〜3秒を作り直します。
6. 月1回、フォロワーのアクティブな時間帯を確認し、投稿時間を調整します。

## 具体例

| 投稿 | 閲覧数 | 保存 | シェア | 読み取り(⚪) |
|---|---|---|---|---|
| A: 手順のカルーセル | 1,200 | 90 | 15 | 保存率が高い → 同じ型を続ける |
| B: 完成写真1枚 | 1,500 | 10 | 2 | 見られたが残らない → 手順や理由を足す |
| C: リール | 4,000 | 30 | 40 | シェアが多い → 冒頭の型を他のリールにも |

(数値は説明用の架空の例です。)

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 投稿直後の数字で一喜一憂した | データは最大48時間遅れる ✅。2〜3日後に記録 |
| インプレッションと閲覧数を同じものとして比較した | 別の指標。切り替え時期を表に書いておく |
| いいね数だけ見ていた | 保存・シェア・フォローなど目的に合う指標を見る |
| 個人アカウントでインサイトが見られない | プロアカウントに切り替える([01-account-setup](01-account-setup.md)) |
| データを記録しておらず、2年以上前と比較できない | 月1回スプレッドシートに記録 |

## 注意点

- 「開発中」「推定」とされる指標は、定義や値が変わることがあります ✅。
- アプリの表示名と API の指標名は一致しないことがあります(⚪)。
- 外部の分析ツールを使う場合は、権限の範囲を確認します([20-api](../20-api/README.md))。

## 見方のコツ

- 保存・シェアの比率が高い形式を増やす。
- リールは冒頭の離脱が多ければ最初の3秒を作り直す。
- 時間帯別のフォロワーのアクティブ時間を確認。

## チェックリスト

- [ ] プロアカウントでインサイトを開けた
- [ ] 週1回、閲覧数・保存・シェア・フォローを記録
- [ ] 当たり投稿の型を書き出した
- [ ] リールのスキップ率と平均再生時間を確認
- [ ] 月1回、数字を長期保存用に記録

## 関連ページ / 次に読む

- [analytics-kpi](../01-common/analytics-kpi.md)、[weekly-review](../../templates/weekly-review.md)
- [09-tips](09-tips.md)、[12-reels](12-reels.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md | 2026-11-03 | ✅ 投稿の指標、48時間の遅延、2年保存、ストーリーズ24時間 |
| https://developers.facebook.com/documentation/instagram-platform/api-reference/instagram-user/insights.md | 2026-11-03 | ✅ アカウントの指標、impressions 廃止、100人未満の制限、上位45件 |
| https://developers.facebook.com/documentation/instagram-platform/changelog.md | 2026-11-03 | ✅ 指標の追加履歴 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(用語、公式の指標定義 ✅、impressions 廃止と views への移行 ✅、データの注意点、週次の見方の手順、具体例、よくある失敗、チェックリスト)。既存の表は維持 |
