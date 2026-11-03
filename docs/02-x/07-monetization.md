---
title: X 収益化
platform: x
topic: monetization
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://help.x.com/en/using-x/creator-revenue-sharing
  - https://help.x.com/en/rules-and-policies/subscriptions-policy
  - https://help.x.com/en/using-x/subscriptions-creator
  - https://docs.x.com/x-api/posts/create-or-edit-post.md
---

# X の収益化

> **このページで分かること**: X で収益を得る方法の全体像、収益分配プログラムの現状(報道ベース)、Subscriptions の条件、準備と注意点。
>
> **対象**: フォロワーが増えてきた初心者〜中級者  **先に読むページ**: [収益化の比較](../01-common/monetization-comparison.md)

> **最重要の注意**: 収益分配プログラムは最近変更された可能性が高く、現行条件は公式で確認できていません (#1)。

## 概要

X での収益化は大きく **(1) X から直接受け取るお金** と **(2) X を入口にして他で得るお金** に分かれます。

| 種類 | 例 | 向く段階 |
|---|---|---|
| X から直接 | 収益分配(Original Content Rewards)、Subscriptions(月額購読) | フォロワー・表示回数が多い段階 |
| X を入口に | note の有料記事、自社サイト、物販、案件(PR) | 最初から設計できる |

X のプログラムは条件が頻繁に変わるため、**最初は (2) の導線づくりから始める** のが安全です(⚪)。

## 用語

| 用語 | 意味 |
|---|---|
| revenue sharing(収益分配) | 広告などの収益の一部をクリエイターに分配する仕組み |
| Subscriptions(サブスクリプション、月額購読) | フォロワーが月額料金を払い、限定コンテンツを見られる仕組み |
| organic impressions(オーガニック表示) | 広告ではない通常の表示回数 |
| verified followers(認証済みフォロワー) | Premium などで認証されたアカウントのフォロワー |
| payout(支払い) | 収益の受け取り |
| PR(Public Relations、ここでは広告案件) | 企業から依頼・報酬を受けた投稿 |

## 状況（🟡 二次資料）

| 項目 | 内容 |
|---|---|
| 旧: Creator Revenue Sharing | 返信欄の広告収益を分配。条件として Premium 系契約、認証済みフォロワー500以上、直近3か月のオーガニックインプレッション500万以上 |
| 新: Original Content Rewards（報道） | 2026年(皇紀2686年・令和8年)9月に切り替わったとの報道。条件として Premium 系契約、18歳以上、認証済みフォロワー500以上、認証済み Home Timeline インプレッション直近90日で50万以上（返信除く）、オリジナルコンテンツ |
| 確度 | 🟡。正確な開始日・終了日・条件は未確認。 |

## 手順（確認後に記載）

- 申請場所: 設定内の収益化／クリエイター関連メニュー ⚪
- 支払い: 決済サービス（Stripe 等）の登録が必要とされてきた ⚪

### 申請前の準備(⚪ 一般的な流れ)

1. 条件(年齢・契約・フォロワー・表示回数)を、アプリの収益化メニューで確認する。
2. プロフィール(名前・bio・画像・ヘッダー)を整える(Subscriptions の条件にも含まれる 🟡)。
3. 本人確認と支払い方法の登録を準備する。
4. 規約(X ルール、収益化の基準)を読む([10-policies](10-policies.md))。
5. 申請後は審査結果を待つ。条件を満たしても承認される保証はない(🟡)。
6. 収入の記録を始める(税金の扱いは [04-tax-and-business](../30-strategy/04-tax-and-business.md))。

## その他の手段

| 手段 | 内容 | 確度 |
|---|---|---|
| Subscriptions | 月額購読者向けコンテンツ | ⚪ 日本での提供条件は要確認 |
| 外部誘導 | note、自社サイト、物販へ | — |
| 案件（PR） | ステマ規制に注意 [legal](../01-common/legal-compliance.md) | — |

### Subscriptions の条件(🟡 help.x.com の検索要約)

| 項目 | 内容 | 確度 |
|---|---|---|
| 年齢 | **18歳以上** | 🟡 |
| フォロワー | **2,000人以上**。ポリシーは「Premium 契約中の有効なフォロワー」、ヘルプ記事は「認証済みフォロワー」と表現が異なる | 🟡 |
| アカウント | 作成から3か月以上、直近30日に投稿あり、名前・bio・画像・ヘッダーが揃っている | 🟡 |
| 表示回数 | 直近3か月でオーガニック表示 **500万以上** とするヘルプ記事あり | 🟡 |
| 契約 | Premium、Premium Business、Premium Organizations のいずれか | 🟡 |
| 審査 | 条件を満たしても承認は保証されない | 🟡 |

出典: [Subscriptions policy](https://help.x.com/en/rules-and-policies/subscriptions-policy)、[About Creator Subscriptions](https://help.x.com/en/using-x/subscriptions-creator)。手数料・機能の詳細は [12-subscriptions](12-subscriptions.md) を参照してください。

### PR 投稿の開示(✅ API の項目)

- 投稿作成時の `paid_partnership` で有料提携であることを示せる(✅ [Create or Edit Post](https://docs.x.com/x-api/posts/create-or-edit-post.md))。
- アプリでの設定場所は ⚪ 要確認。いずれの場合も、本文に「PR」「広告」など分かる表記を入れる([legal-compliance](../01-common/legal-compliance.md))。
- 案件の受け方は [07-sponsorship-and-media-kit](../30-strategy/07-sponsorship-and-media-kit.md)。

## API 利用の費用

X の API は従量課金(pay-per-use)が標準になった(🟡)。自動投稿・分析を API で行う場合の費用は [02-x-api](../20-api/02-x-api.md) を参照。

## 方針

プログラムの条件は変動するため、**収益分配に依存しすぎない**。メールリスト・自サイト・note 等に読者を移す導線を持つ。

導線の作り方は [funnel](../30-strategy/02-funnel.md)、段階ごとの目標は [03-monetization-roadmap](../30-strategy/03-monetization-roadmap.md)。

## Original Content Rewards(🟡 複数の報道で一致。公式本文は未取得)

| 項目 | 内容 |
|---|---|
| 時期 | 旧収益分配は 2026年(皇紀2686年・令和8年)9月7日に終了。9月8日から申請開始。最後の支払いは9月11日ごろ、新制度の初回支払いは9月25日の見込みと報道 |
| 条件 | **18歳以上、Premium 系の契約、認証済みフォロワー 500人以上、直近90日で 50万インプレッション以上**(報道で一致)。居住国・日常的なオリジナル投稿も条件とする記事 |
| 移行 | **自動移行なし**。再申請・審査が必要。本人確認と支払い方法の登録が済んでいれば省略可 |
| 対象 | 「オリジナル」な投稿を重視。コピーや使い回しは対象外 |
| 不明 | 報酬の算定方法の詳細 |

確認: X の公式ヘルプ(`help.x.com` は未取得 #1)。

- 検索要約では、旧 Creator Revenue Sharing は **2026年8月7日に新規受付を停止** し、9月7日に終了とされる(🟡 [help.x.com Creator Revenue Sharing](https://help.x.com/en/using-x/creator-revenue-sharing) の検索要約と報道)。
- Premium 未契約のアカウントは、収益化メニューで「対象外」と表示されるとする記事がある(🟡)。

## 具体例(⚪ 汎用の設計例)

| アカウント | X の役割 | 収益の場所 |
|---|---|---|
| 料理アカウント | 毎日のコツを短く投稿 | note の有料レシピ集、料理教室の予約 |
| イラストアカウント | 制作過程・完成作品 | 作品販売サイト、依頼の受付 |
| 地域の店 | 焼き上がり・営業情報 | 来店・通販 |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 収益分配だけを当てにして、条件変更で収入がゼロに | 外部の導線(note・メール)を並行して育てる |
| 他人の投稿の転載でインプレッションを稼いだ | オリジナルでない投稿は対象外とされる(🟡)。規約違反の恐れもある |
| PR 表記を忘れた | すぐ追記・訂正する。景品表示法のステマ規制に注意 |
| 収入を記録していなかった | 毎月の入金を表にまとめる |

## 注意点

- 収益化の条件・名称・時期は、このページの記載から変わっている可能性が高いです。必ずアプリの収益化メニューと公式ヘルプで確認してください。
- 実際の収益額(非公開の数値)はこのリポジトリに書かないでください。

## チェックリスト

- [ ] アプリの収益化メニューで現在の条件を確認した
- [ ] 本人確認・支払い方法の準備をした
- [ ] 外部の導線(note・サイト・メール)を用意した
- [ ] PR 投稿の表記ルールを決めた
- [ ] 収入の記録表を作った

## 関連(料金・Grok)

X Premium の料金、Grok との関係、X API の従量課金は [40-pricing/01-x-and-grok](../40-pricing/01-x-and-grok.md)。

## 関連ページ / 次に読む

- [12-subscriptions](12-subscriptions.md)(Subscriptions の詳細)
- [monetization-comparison](../01-common/monetization-comparison.md)、[funnel](../30-strategy/02-funnel.md)、[legal-compliance](../01-common/legal-compliance.md)
- 次に読む: [08-analytics](08-analytics.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://help.x.com/en/using-x/creator-revenue-sharing | 2026-11-03 | 検索要約のみ(🟡)。新規受付停止と終了の時期 |
| https://help.x.com/en/rules-and-policies/subscriptions-policy | 2026-11-03 | Subscriptions の条件(🟡 検索要約) |
| https://help.x.com/en/using-x/subscriptions-creator | 2026-11-03 | Subscriptions の条件(🟡 検索要約) |
| https://docs.x.com/x-api/posts/create-or-edit-post.md | 2026-11-03 | `paid_partnership`(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、申請前の準備、Subscriptions の条件 🟡、PR 開示、具体例、よくある失敗、チェックリスト)。旧制度の新規受付停止(2026年8月7日)を 🟡 で追記。12-subscriptions へのリンクを追加 |
