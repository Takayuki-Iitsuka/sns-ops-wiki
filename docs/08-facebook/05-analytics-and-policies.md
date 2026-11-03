---
title: Facebook 分析・ルール・チェックリスト
platform: facebook
topic: analytics
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://creators.facebook.com/professional-dashboard
  - https://developers.facebook.com/documentation/pages-api/platforminsights/page.md
  - https://developers.facebook.com/documentation/pages-api/platforminsights/page/deprecated-metrics.md
  - https://creators.facebook.com/stay-safe/policies-and-guidelines
---

# Facebook の分析・ルール・チェックリスト

> **このページで分かること**: インサイト(分析)の見る場所と主な指標、「インプレッション」「ファン」から「閲覧」「フォロー」への指標の切り替え、守るべきルールの種類、運用チェックリスト。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [analytics-kpi](../01-common/analytics-kpi.md)

## 概要

Facebook の分析は、**プロフェッショナルダッシュボード**または **Meta Business Suite のインサイト**で見ます。ダッシュボードでは、リーチ・エンゲージメント・フォロワーの純増・3秒動画再生などの概要を、**最大過去90日**分まとめて確認できます ✅([Meta for Creators](https://creators.facebook.com/professional-dashboard))。

ここ数年で指標の名前と定義が大きく変わりました。過去の数字と比べるときは**指標が同じか**を必ず確認します(下記)。

## 用語

| 用語 | 意味 |
|---|---|
| reach(リーチ) | 見たユニークアカウント数 |
| views / media views(閲覧) | コンテンツが表示・再生された回数。旧「インプレッション」に代わる指標 |
| follows(フォロー) | ページをフォローしている人。旧「ファン(ページへのいいね)」に代わる指標 |
| engagement(エンゲージメント) | リアクション・コメント・シェアなどの反応 |
| net followers(フォロワーの純増) | 新規フォロー − フォロー解除 |
| 3-second video views(3秒動画再生) | 3秒以上再生された回数 |
| Community Standards(コミュニティ規定) | Meta の投稿ルール |

## 手順 / 仕様

### 分析(Meta Business Suite のインサイト ⚪)

| 指標 | 意味 |
|---|---|
| リーチ | 見たユニークアカウント数 |
| 反応・コメント・シェア | 反応の種類 |
| 動画の視聴時間・維持率 | 動画の評価 |
| フォロワーの属性 | 年齢・地域・時間帯 |
| リンクのクリック | 導線の効果 |

共通: [analytics-kpi](../01-common/analytics-kpi.md)

### 見る場所(⚪ メニュー名は変わる可能性)

1. ページに切り替え、「プロフェッショナルダッシュボード」を開きます。
2. 「インサイト」で全体の推移、「コンテンツ」で投稿ごとの数字を見ます。
3. パソコンでは Meta Business Suite の「インサイト」でも同じ情報を確認できます。

### 指標の切り替え(✅ Pages API の文書)

出典: [Deprecated Metrics](https://developers.facebook.com/documentation/pages-api/platforminsights/page/deprecated-metrics.md)。

| 旧指標 | 代わりの指標 | 廃止の時期 |
|---|---|---|
| `page_impressions_unique`(ページのリーチ) | `page_total_media_view_unique` | 6月15日(年は文書内で不一致。下記の注記) |
| `post_impressions_unique`(投稿のリーチ) | `post_total_media_view_unique` | 同上 |
| `page_fans`(ファン) | `page_follows` | 2025年(皇紀2685年・令和7年)11月15日 |
| `page_impressions`(表示回数) | `page_media_view` | 2025年11月15日 |
| `post_impressions`(投稿の表示回数) | `post_media_view` | 2025年11月15日 |

> 一覧ページは「2025年6月15日までに廃止」、インサイトの説明ページは「2026年(皇紀2686年・令和8年)6月15日までに廃止」と書いており、**公式文書内で年が一致しません**。いずれにしても現在は新しい指標(閲覧・フォロー)を使います。

データの保存(✅ [Page Insights](https://developers.facebook.com/documentation/pages-api/platforminsights/page.md)): 公開ページの指標データは **2年間**保存されます。長期比較のために月1回は記録しておきます。

### 週次の見方(⚪)

1. 先週の投稿の**リーチ・閲覧・反応・リンクのクリック**を記録します([weekly-review](../../templates/weekly-review.md))。
2. リーチに対して反応やクリックの多い投稿の型(テーマ・形式・時間帯)を書き出します。
3. 動画は視聴時間・3秒再生を見て、冒頭を改善します。
4. グループはメンバー250人以上でインサイトが使えます ✅([03-engagement-and-groups](03-engagement-and-groups.md))。

### ルール(⚪ 一般論)

| 領域 | 要点 |
|---|---|
| コミュニティ規定 | ヘイト・嫌がらせ・誤情報 |
| 収益化ポリシー | オリジナル性、再投稿の制限 |
| 著作権・音楽 | 権利者の申し立て |
| 広告・ブランドコンテンツ | 開示と承認の仕組み |
| 個人情報 | グループでの取り扱い |

公式で確認できたこと(✅):

- Meta は、スパム的なコンテンツや、**アルゴリズムを不正に操作して閲覧・フォロワー・収益を得ようとするアカウント**への対策を強化していると説明しています([Policies & Guidelines](https://creators.facebook.com/stay-safe/policies-and-guidelines))。
- 収益化するコンテンツは、コミュニティ規定に加えて**より高い基準**(パートナー収益化ポリシー・コンテンツ収益化ポリシー)を満たす必要があります 🟡([パートナー収益化ポリシー](https://www.facebook.com/business/help/169845596919485)の検索要約)。
- リールは Meta のデータポリシー、コミュニティ規定、Facebook と Instagram のコミュニティガイドライン、利用規約に従う必要があります ✅([Reels](https://creators.facebook.com/tools/reels))。
- 開発者向けには、ページの**違反・制限の状況**を取得する Page Integrity API があります ✅([Pages API 索引](https://developers.facebook.com/documentation/pages-api/llms.txt))。

### 違反通知を受けたとき(⚪)

1. 通知の内容(日時・対象・理由)をスクリーンショットで保存します。
2. ページの「アカウントステータス」(ページの品質)で詳細を確認します。
3. 誤りだと考える場合は、画面の案内から見直しを申請します。
4. 違反だった場合は同様の投稿を削除し、制作ルールを更新します。
5. 偽の通知(メッセージやメールのリンク)に注意します([account-security](../01-common/account-security.md))。

## 具体例

| 状況 | 判断(⚪) |
|---|---|
| 他のページの人気動画を転載 | 権利侵害・収益化対象外。共有ボタンで元の投稿をシェアする |
| 商品提供を受けた紹介投稿 | タイアップ投稿ラベル+PR 表記 |
| グループ内で個人の電話番号が書き込まれた | すぐ削除し、本人に連絡 |
| 古いレポートの「ファン数」と今の「フォロー数」を比較 | 指標が違う。切り替え時期を注記する |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 旧指標(インプレッション・ファン)の推移と新指標をつなげてグラフにした | 別の指標として分けて記録 |
| 90日より前の数字が見られない | ダッシュボードの概要は最大90日 ✅。月1回記録する |
| 規約違反の理由が分からないまま同じ投稿を繰り返した | アカウントステータスで理由を確認 |

## チェックリスト

- [ ] ページ管理者の2段階認証、権限
- [ ] 画像の比率とリンクプレビュー(1.91:1)
- [ ] 広告・PR の表記
- [ ] 予約投稿の確認
- [ ] 受信箱の対応時間を決めた
- [ ] 月次: 収益化条件・規約の確認を [verification-queue](../00-meta/verification-queue.md) に追記
- [ ] 週次: リーチ・閲覧・反応・クリックを記録した
- [ ] 月次: 指標を長期保存用に記録した(データは2年 ✅)
- [ ] グループのルール・モデレーターの体制を見直した
- [ ] 偽の通知・招待メッセージへの注意を管理者全員で共有した

## 関連ページ / 次に読む

- [analytics-kpi](../01-common/analytics-kpi.md)、[legal-compliance](../01-common/legal-compliance.md)、[crisis-response](../01-common/crisis-response.md)
- [04-monetization](04-monetization.md)、[03-engagement-and-groups](03-engagement-and-groups.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://creators.facebook.com/professional-dashboard | 2026-11-03 | ✅ ダッシュボードの指標、最大90日 |
| https://developers.facebook.com/documentation/pages-api/platforminsights/page.md | 2026-11-03 | ✅ データ保存2年、廃止予定の警告(2026年6月15日) |
| https://developers.facebook.com/documentation/pages-api/platforminsights/page/deprecated-metrics.md | 2026-11-03 | ✅ 廃止指標と代替(2025年6月15日・11月15日) |
| https://creators.facebook.com/stay-safe/policies-and-guidelines | 2026-11-03 | ✅ スパム・不正操作への対策 |
| https://creators.facebook.com/tools/reels | 2026-11-03 | ✅ リールが従うべき規約 |
| https://developers.facebook.com/documentation/pages-api/llms.txt | 2026-11-03 | ✅ Page Integrity API の存在 |
| https://www.facebook.com/business/help/169845596919485 | 2026-11-03 | 🟡 パートナー収益化ポリシー(検索要約) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(用語、見る場所、指標の切り替え ✅ と公式文書内の年の不一致、データ保存2年 ✅、週次の見方、公式で確認できたルール、違反時の手順、具体例、よくある失敗、チェックリストの追加項目)。既存の表・チェック項目は維持 |
