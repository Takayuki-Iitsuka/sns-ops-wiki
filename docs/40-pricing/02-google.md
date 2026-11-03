---
title: Google の料金(Google AI・YouTube Premium・Gemini API・生成画像/動画)
platform: google
topic: pricing
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://cloud.google.com/model-garden/pricing
  - https://support.google.com/googleone/answer/14534406?hl=ja
---

# Google の料金

> **このページで分かること**: Google AI プラン、YouTube Premium、Gemini・Imagen・Veo の API 料金の違いと読み方、サブスクと API のどちらが安いかの計算例。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [料金プラン(索引と読み方)](README.md)
>
> **確認時点**: 2026年(皇紀2686年・令和8年)11月3日。表の中の年は西暦のみで表記します。

## 概要

Google の料金は「誰が・何のために払うか」で3つに分かれます。**視聴者・利用者として払うもの**(YouTube Premium、Google AI プラン)、**開発者として使った分だけ払うもの**(API)、そして**投稿者が受け取るもの**(YouTube の収益化)です。投稿者が YouTube に動画を載せること自体には料金はかかりません。

- 日本円のサブスク価格は 🟡(報道・比較記事)、API 料金は ✅(Google Cloud の公式料金ページ。米ドル)です。
- 日本の価格表示は「税込」と書かれているもの以外は、**購入画面で税込/税抜を確認**してください(⚪)。

## 用語

| 用語 | 意味 |
|---|---|
| Google AI プラン | Gemini などの上限を増やす個人向けサブスク(Plus / Pro / Ultra) |
| YouTube Premium / Premium Lite | 視聴者向けの広告なし再生などのサブスク。Lite は機能を絞った安いプラン |
| YPP / YouTube Partner Program(YouTube パートナー プログラム) | 投稿者が収益を受け取るためのプログラム |
| API(エーピーアイ) | プログラムから機能を使う仕組み。使った分だけ課金 |
| token(トークン) | AI が文章を処理する単位。料金は100万トークンあたりで表示 |
| long context(長文コンテキスト) | 一度に大量の文章を入力すること。一定量を超えると単価が上がる |
| promotion price(プロモーション価格) | 期間限定の割引価格。期限後に通常価格に戻る |

SNS 運用で関わる Google の料金は、**①利用者向けサブスク(Google AI、YouTube Premium)**、**②開発者向け API(Gemini、Imagen、Veo)**、**③投稿者の収益化(YouTube、AdSense)**の3つに分かれます。

## 1. 利用者向けサブスク(日本円。🟡 報道・比較記事)

### Google AI プラン(2026年5月の Google I/O で刷新)

| プラン | 月額(税込) | 主な内容 | 確度 |
|---|---|---|---|
| Google AI **Plus** | 1,200円 | 下位プラン | 🟡 |
| Google AI **Pro** | 2,900円(据え置き) | Gemini の上限拡大、**YouTube Premium Lite の個人プランが特典に追加** | 🟡 |
| Google AI **Ultra 5x**(新設) | 14,500円(月払いのみ) | Pro の約5倍の上限、クラウドストレージ 20TB | 🟡 |
| Google AI **Ultra 20x**(旧 Ultra) | 32,000円(値下げ) | 最上位。Veo 3.1 の完全版など | 🟡 |

- 米国では Ultra が $100 / $200 の2段になったとの報道もあり、日本の価格・特典と異なる。
- Veo(動画生成):Pro は Veo 3.1 Fast、Ultra は音声付きの Veo 3.1 完全版とする記事(英語の解説。日本での提供状況は未確認)。
- Gemini Spark など一部機能は「US only, English only」と表記され、日本では使えない可能性。
- **Ultra への YouTube Premium 付帯**は日本では明確に確認できず。
- Google のヘルプには「一部の Google AI Pro メンバーシップには **YouTube Premium Lite 個人プラン**が自動的に含まれる」「YouTube Music Premium は含まれず、完全版の YouTube Premium は別途購入」とあります(✅ [Google One ヘルプ](https://support.google.com/googleone/answer/14534406?hl=ja)。料金の記載はなし)。

### YouTube Premium(日本。🟡 Gizmodo Japan 2026年4月、Selectra)

| プラン | Web・Android | iPhone・iPad(アプリ内課金) | 備考 |
|---|---|---|---|
| Premium(個人) | 1,280円/月 | **1,680円/月** | 年払い 12,800円(iPhone アプリ内は年払い不可) |
| Premium ファミリー | 2,280円/月 | — | |
| Premium 学割 | 780円/月 | iPhone アプリから申込不可 | 認証は定期更新、最長4年 |
| **Premium Lite** | 780円/月 | **980円/月** | 2026年2月からバックグラウンド再生・オフライン保存に対応 |
| Music Premium | 1,080円/月 | — | Premium Lite には含まれない |

- 米国では 2026年(皇紀2686年・令和8年)に値上げがあったが、**日本は対象外**(その後の改定は未確認)。
- **投稿者の収益化(YPP)とは別**。視聴者が Premium を使うと、Premium からの収益分配が投稿者に入る(広告収益の資格を満たす場合 ✅ [05-monetization](../05-youtube/05-monetization.md))。

## 2. 開発者向け API(✅ Google Cloud の公式料金ページ。2026年11月3日取得)

料金は米ドル。**200 を返したリクエストにのみ課金**(4xx・5xx は課金されない)。

### Gemini(テキスト・画像・動画の入出力)

| モデル | 入力(100万トークン) | 出力(100万トークン) | 備考 |
|---|---|---|---|
| Gemini 4 Argon | $2.00 | $10.00 | **2026年11月30日まで**(50% クレジット還元のプロモーション価格として表示) |
| Gemini 4 Argon | $4.00 | $20.00 | **2026年12月1日以降** |
| Gemini 3.x Flash 系 | — | — | 公式ページに 2026年12月31日までのプロモーションの記載あり。値は本文で確認 |

- 入力が **20万トークンを超える**と、入力・出力とも長文コンテキスト料金で課金。
- キャッシュした入力は割引(Argon で入力 $0.10)。
- グローバル以外のエンドポイントは割増(Argon で入力 $2.20 など)。

### 画像生成(1枚あたり。✅)

| モデル | 解像度 | 1枚あたり |
|---|---|---|
| Gemini 3 Pro Image | 1K・2K | **$0.134** |
| Gemini 3 Pro Image | 4K | **$0.24** |
| Gemini 3.1 Flash Image | 512 | $0.045 |
| Gemini 3.1 Flash Image | 1K | **$0.067** |
| Gemini 3.1 Flash Image | 2K | $0.101 |
| Gemini 3.1 Flash Image | 4K | $0.15 |
| Gemini 3.1 Flash-Lite Image | 1K | **$0.034** |
| Imagen 4 Ultra | — | $0.06 |
| Imagen 4 | — | $0.04 |
| **Imagen 4 Fast** | — | **$0.02** |
| Imagen 4(アップスケール 2K/3K/4K) | — | $0.06 |

### 動画生成(Veo。✅ 数値。単位は「1 count」と表記)

| モデル | 種別 | 720p / 1080p | 4K |
|---|---|---|---|
| Veo 3.1 | 動画+音声 | $0.40 | $0.60 |
| Veo 3.1 | 動画のみ | $0.20 | $0.40 |
| Veo 3.1 Fast | 動画+音声 | $0.10(720p)/ $0.12(1080p) | $0.30 |
| Veo 3.1 Fast | 動画のみ | $0.08(720p)/ $0.10(1080p) | $0.25 |
| Veo 3.1 Lite | 動画+音声 | $0.05(720p)/ $0.08(1080p) | — |
| Veo 3.1 Lite | 動画のみ | $0.03(720p)/ $0.05(1080p) | — |

> **「1 count」が1秒か1本かは、ページ本文だけでは断定できなかった**(一般には1秒あたりの課金と解釈されることが多いが未確認 #59)。見積り前に公式の注記を確認。

### Gemini Developer API(ai.google.dev)

別系統の料金ページ(無料枠あり)。`ai.google.dev` は未取得。二次資料ではモデル名・価格が不一致(🟡)。**API キーの取得元(AI Studio / Vertex)によって料金・制限が違う**ことに注意。

## 3. 運用者の見方(⚪)

| 目的 | おすすめ |
|---|---|
| 文章・企画の補助を日常的に | Gemini 無料枠→必要なら Google AI Pro(YouTube Premium Lite 付きなので、すでに Lite に入っているなら割安) |
| 画像生成を大量に | API の Imagen 4 Fast($0.02/枚)や Flash-Lite Image($0.034/枚)が安い。月30枚なら $1 未満〜 |
| 動画生成 | 単価が高いので、まず短く・低解像度で試す。商用・投稿前に規約・AI 表示を確認 |
| YouTube を見る(自分の視聴) | Premium または Lite。**iPhone だけ割高**なので Web から契約 |
| 収益化(投稿者) | YPP の条件を満たすこと。Premium とは別 |

## 4. 規約・AI 表示

- Google の生成物を投稿する場合の表示ルールは [ai-rules-by-platform](../01-common/ai-rules-by-platform.md)(YouTube は ✅)。
- 生成画像の著作権・商用利用は各サービスの規約で確認([ai-usage-policy](../01-common/ai-usage-policy.md))。

## 5. 計算例: サブスクと API のどちらが安いか(⚪ 為替は仮定)

| 前提 | 計算 | 結果 |
|---|---|---|
| Imagen 4 Fast で画像を月100枚(✅ $0.02/枚) | 100 × $0.02 | $2.00 |
| 円の目安(**仮に 1ドル = 150円**) | $2.00 × 150 | 約 300円 |
| Google AI Pro(🟡 2,900円/月)と同じ額で作れる枚数 | 2,900円 ÷ 150円 ÷ $0.02 | 約 966枚 |

- **画像だけ**が目的で枚数が少ないなら API のほうが安くなりやすいです。ただし API はプログラムの準備(API キーの管理など)が必要です([API の基本](../20-api/01-concepts-and-security.md))。
- サブスクには文章の補助、ストレージ、YouTube Premium Lite(一部のプラン)なども含まれるため、**画像の単価だけで比較しない**でください。
- 「1ドル = 150円」は計算方法を示すための仮の値です。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| プロモーション価格のまま見積もる | 期限(例: Gemini 4 Argon は 2026年11月30日まで)を確認し、通常価格でも見積もる |
| iPhone のアプリ内で YouTube Premium を契約して割高 | Web・Android の価格と比べる(🟡 1,280円 vs 1,680円) |
| YouTube Premium に入れば収益化できると思う | 視聴用の契約と、投稿者の収益化(YPP)は別 |
| API キーを公開の場所に貼る | キーは非公開の場所に保管。公開リポジトリには `YOUR_API_KEY` のような例示のみ |
| 試しに何度も生成して費用が膨らむ | 課金は 200 を返した(成功した)リクエストのみ(✅ Google Cloud の料金ページ)。成功した分は課金されるので、試作は少ない枚数・低解像度で行う |

## チェックリスト

- [ ] 必要なのは「視聴」「AI の補助」「API」のどれかを決めた
- [ ] 購入画面で現在の価格、税込/税抜、更新日を確認した
- [ ] API はプロモーション期限と通常価格を確認した
- [ ] API キーを安全に保管した
- [ ] 経費として記録する準備をした([税務](../30-strategy/04-tax-and-business.md))

## 関連ページ / 次に読む

- [YouTube の収益化](../05-youtube/05-monetization.md)
- [AI・制作ツールの料金](05-ai-and-creative-tools.md)
- [月額の見積り例](06-cost-planning.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://cloud.google.com/model-garden/pricing | 2026-11-03 | Gemini・画像・Veo の API 料金 ✅ |
| https://support.google.com/googleone/answer/14534406?hl=ja | 2026-11-03 | Google AI Pro の特典(YouTube Premium Lite 個人プランが一部プランに含まれる)✅。料金の記載なし |
| (Google AI プラン・YouTube Premium の日本の公式料金ページ) | — | one.google.com・youtube.com の料金ページは未取得(🟡 のまま) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、Google One ヘルプで YouTube Premium Lite の付帯を ✅ 確認、サブスクと API の計算例、よくある失敗、チェックリスト、出典表)。既存の ✅ と数値は変更なし |
