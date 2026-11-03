---
title: 料金プラン(索引と読み方)
platform: common
topic: pricing
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://cloud.google.com/model-garden/pricing
  - https://support.google.com/googleone/answer/14534406?hl=ja
---

# 料金プラン(索引と読み方)

> **このページで分かること**: 料金ページの一覧、料金表の読み方(確度ラベル、為替、税込/税抜、月払い/年払い)、契約前の確認手順。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [はじめての SNS 運用](../00-meta/beginners-guide.md)
>
> **確認時点**: 2026年(皇紀2686年・令和8年)11月3日。表の中の年は西暦のみで表記します。

各サービスの有料プラン・API 料金・AI 利用料・運用ツールの料金を、**運用者の立場**で整理します。

> **料金は最も変わりやすい情報です**。✅(公式の本文を直接確認)は **X API(docs.x.com)と Google Cloud の生成 AI 料金**のみで、他は 🟡(報道・比較記事)です。契約前に必ず公式の料金画面で確認してください(#44〜#52)。**iPhone のアプリ内課金は App Store の手数料が上乗せされ、Web・Android より高い場合**があります(例: YouTube Premium)。

## 概要

SNS は**無料で始められる**ものがほとんどです。料金がかかるのは、主に次の4つです。

1. **利用者向けの有料プラン**(X Premium、Meta One、YouTube Premium など)。
2. **API の従量課金**(X API、Gemini・Imagen・Veo の API など)。
3. **ツールのサブスク**(AI アシスタント、画像編集、予約投稿、自動化)。
4. **販売手数料**(note の有料記事、支援サイト、販売サイト)。

初心者は「まず無料 → 足りない機能が明確になったら1つずつ有料」の順で進めると、無駄な出費を防げます(⚪)。

## 用語

| 用語 | 意味 |
|---|---|
| 税込 / 税抜(税別) | 消費税を含む価格 / 含まない価格。税抜なら支払額は消費税分だけ高くなる |
| 原通貨 | サービスが料金を決めている通貨(米ドルなど)。このフォルダでは円に換算しない |
| 為替レート | ドルと円の交換比率。日々変わるため、円の支払額も変わる |
| 従量課金 | 使った量に応じて支払う方式 |
| サブスク(サブスクリプション) | 月額・年額で継続して支払う方式 |
| アプリ内課金 | App Store・Google Play 経由の支払い。Web と価格が違う場合がある |

## ページ一覧

| ページ | 内容 |
|---|---|
| [01-x-and-grok](01-x-and-grok.md) | **X(Premium、API)と Grok(SuperGrok、xAI API)の関係と料金** |
| [02-google](02-google.md) | **Google(Google AI、YouTube Premium、Gemini API、画像・動画生成)の料金** |
| [03-meta](03-meta.md) | Meta One、Meta Verified |
| [04-other-services](04-other-services.md) | note、LINE、創作支援系ほか |
| [05-ai-and-creative-tools](05-ai-and-creative-tools.md) | AI アシスタント、画像・動画ツール、予約・自動化ツール |
| [06-cost-planning](06-cost-planning.md) | 月額の見積り例と、費用を抑える設計 |

## 全体像(🟡 一部 ✅)

| 領域 | 無料で使える範囲 | 有料の主なプラン | 備考 |
|---|---|---|---|
| X | 投稿・閲覧 | Premium 系(Basic / Premium / Premium+) | 長文、動画の長さ、収益分配の条件、Grok の枠に関係 |
| X API | — | **従量課金のみ**(クレジット前払い) | ✅ 投稿 $0.015、URL 付き $0.200 |
| Grok | 無料枠あり(回数制限) | SuperGrok、Heavy | X の契約・X API・xAI API と**別立て**の面あり |
| Instagram / Facebook / Threads | 投稿・閲覧・基本機能 | Meta One(Instagram Plus など)、Meta Verified | 2026年9月に Meta One |
| YouTube | 投稿・視聴 | Premium、Premium Lite、Music Premium | 投稿者の収益化は別([05-monetization](../05-youtube/05-monetization.md)) |
| Google AI | Gemini の無料枠 | Google AI Plus / Pro / Ultra(5x、20x) | Pro に YouTube Premium Lite が付属 |
| note | 投稿・販売(手数料あり) | note プレミアム、note pro | 販売手数料は別([note 収益化](../04-note/07-monetization.md)) |
| LINE 公式 | 月200通 | ライト、スタンダード | 通数課金 |
| TikTok・Bluesky | 無料 | — | 収益化は条件制 |

## 為替・税

- ドル建ての料金は、**為替と決済手段**で円額が変わる。ここでは換算せず、原通貨で記載する。
- 日本の価格表示は多くが**税込**。事業の経費にする場合は消費税の扱い(インボイス)を確認([tax-and-business](../30-strategy/04-tax-and-business.md))。
- 海外サービスへの支払いは、消費税の扱い(リバースチャージなど)が関わる場合がある(⚪ 専門家に確認)。

### 料金表の読み方(⚪)

| 表記 | 意味と注意 |
|---|---|
| ✅ | 公式の料金ページ本文で確認済み(確認日を見る) |
| 🟡 | 報道・比較記事の値。**契約前に必ず公式画面で確認** |
| 「$20/月」 | 米ドル建て。円の支払額は為替・カード会社の手数料で変わる |
| 「(税別)」「(税抜)」 | 消費税が加算される |
| 「年払い $X/月」 | 1年分をまとめて払った場合の月あたりの額。月払いより安いことが多いが、一括で支払う |
| 「〜」「から」 | 最も安いプランの価格。必要な機能が上位プランにしかないことがある |

## 契約前の確認手順

1. **目的を一文で書く**(例: 「予約投稿の手間を減らしたい」)。
2. **無料機能で足りないか確認**する(各サービスの公式の予約・分析機能)。
3. **公式の料金ページ・購入画面**で、価格・通貨・税込/税抜・月払い/年払い・更新日を確認する。
4. **月額と年額で計算**する([見積り例](06-cost-planning.md))。
5. **解約方法と解約期限**を確認し、カレンダーに登録する。
6. 契約したら、[月次レビュー](../../templates/monthly-review.md)の費用欄と経費の記録([税務](../30-strategy/04-tax-and-business.md))に追加する。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 比較記事の価格をそのまま信じる | 公式の購入画面で最終確認する(このフォルダの 🟡 も同じ) |
| 為替が変わって請求額が増える | 円の見積りに余裕を持たせ、カード明細で実額を確認 |
| アプリ内課金で割高に契約 | Web・Android の価格と比べる |
| 税別価格を税込と勘違い | 「税別」「税抜」の表記を確認し、消費税を加える |

## チェックリスト

- [ ] 目的と、無料で足りない理由を書いた
- [ ] 公式画面で価格・通貨・税込/税抜を確認した
- [ ] 月額と年額を計算した
- [ ] 解約期限をカレンダーに入れた
- [ ] 費用を記録する場所を決めた

## 関連ページ / 次に読む

- [月額の見積り例](06-cost-planning.md)
- [個人の収益と税務](../30-strategy/04-tax-and-business.md)
- [消費税とインボイス](../30-strategy/08-consumption-tax-and-invoice.md)
- [ツール](../01-common/tools.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | X API 料金 ✅ |
| https://cloud.google.com/model-garden/pricing | 2026-11-03 | Google Cloud の生成 AI 料金 ✅ |
| https://support.google.com/googleone/answer/14534406?hl=ja | 2026-11-03 | Google AI Pro の特典 ✅(料金の記載なし) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、料金表の読み方、契約前の確認手順、よくある失敗、チェックリスト、関連ページ、出典表) |
