---
title: Google の料金(Google AI・YouTube Premium・Gemini API・生成画像/動画)
platform: google
topic: pricing
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://cloud.google.com/model-garden/pricing
---

# Google の料金

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
