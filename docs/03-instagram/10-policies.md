---
title: Instagram ルール・ポリシー
platform: instagram
topic: policy
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://help.instagram.com/512371932629820
  - https://developers.facebook.com/documentation/instagram-platform/changelog.md
  - https://creators.facebook.com/earn-money/earn-from-brands/
---

# Instagram のルール・ポリシー

> **このページで分かること**: Instagram で守るべきルールの種類(利用規約・コミュニティガイドライン・収益化ポリシー)、特に注意が必要な領域、違反通知を受けたときの手順。
>
> **対象**: 初心者  **先に読むページ**: [legal-compliance](../01-common/legal-compliance.md)

一次資料: Instagram コミュニティガイドライン、利用規約、Meta パートナー収益化ポリシー(入口: https://help.instagram.com/ 。作成時は本文が JavaScript 描画で取得できず、未確認 #28)。

## 概要

Instagram のルールは、主に次の3層になっています(⚪ 整理の仕方)。

| ルール | 対象 | 内容の例 |
|---|---|---|
| **利用規約**(Terms of Use) | すべての利用者 | 年齢要件、禁止行為、権利の扱い |
| **コミュニティガイドライン** | すべての投稿 | 暴力・ヘイト・嫌がらせ・スパムなどの禁止 |
| **パートナー収益化ポリシー**など | 収益化機能を使う人 | オリジナル性、真正なエンゲージメント |

収益化には、通常のガイドラインより**厳しい基準**が加わります(🟡 [パートナー収益化ポリシー](https://help.instagram.com/512371932629820)の検索要約)。

加えて、日本の法律(景品表示法、著作権法、個人情報保護法など)も守る必要があります([legal-compliance](../01-common/legal-compliance.md))。

## 用語

| 用語 | 意味 |
|---|---|
| Community Guidelines(コミュニティガイドライン) | Instagram の投稿ルール |
| Community Standards(コミュニティ規定) | Meta 全体の投稿ルール |
| Account Status(アカウントステータス) | 違反の有無や制限状況を確認できる画面 |
| appeal(異議申し立て) | 削除や制限に対して見直しを求めること |
| AI info label(AI 情報ラベル) | AI で生成・編集したことを示す表示 |
| Paid partnership label(タイアップ投稿ラベル) | 企業から対価を得た投稿であることを示す表示 |

## 手順 / 仕様

### 注意領域(⚪ 一般論)

| 領域 | 要点 | 運用での注意 |
|---|---|---|
| オリジナル性 | 他者コンテンツの再投稿は推奨度・収益化に影響し得る | 他人の画像・動画の転載をしない |
| 著作権・音楽 | 音源の商用利用の可否(ビジネスアカウントは使える音源が限定される場合あり) | リールの BGM は権利クリアのものに |
| ブランドコンテンツ | 有料パートナーシップのラベル等 | [legal](../01-common/legal-compliance.md) の広告表記 |
| フォロワー購入・自動化 | 規約違反 | — |
| 年齢制限 | 規約の年齢要件を確認 | 原則13歳以上 🟡([ヘルプ](https://help.instagram.com/517920941588885)の検索要約) |
| 暴力・ヘイト・危険な内容 | 削除対象 | 暴力的な描写は文脈と表現を選ぶ |
| 宗教・政治 | 攻撃的・差別的な表現は削除対象 | [慎重な話題の扱い](../01-common/sensitive-topics-and-accuracy.md) |
| AI 生成コンテンツ | ラベル表示の規約・機能は要確認 | [ai-usage-policy](../01-common/ai-usage-policy.md) |
| 位置情報・個人情報 | 他者のプライバシーに配慮 | 来店客・参拝者など第三者を写さない |

### 公式文書で確認できたこと(✅)

| 項目 | 内容 | 出典 |
|---|---|---|
| AI 生成の自己申告 | API で `is_ai_generated=true` を指定すると **AI 情報ラベル**が付く(2026年(皇紀2686年・令和8年)6月22日の変更履歴) | [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md) |
| タイアップ投稿ラベル | 公開時に「Paid partnership」ラベルを付けられる(API、2026年4月22日) | 同上 |
| 著作権のある音源 | 著作権のある音源を含む動画は、API でも動画ファイルの URL が返されない(2026年7月30日) | 同上 |
| ブランドコンテンツ | 企業との関係は「タイアップ投稿」ラベルで開示する | [Meta for Creators](https://creators.facebook.com/earn-money/earn-from-brands/) |

### 違反時

1. 通知の内容を記録。
2. 異議申立て(アプリ内)。
3. 再発防止。凍結に備えて他拠点を用意。

もう少し詳しい手順(⚪ メニュー名は変わる可能性):

1. 通知のスクリーンショットを保存し、日時・対象の投稿・理由を記録します。
2. 設定の「アカウントステータス」で、違反の内容と制限の有無を確認します。
3. 誤りだと考える場合は、表示される「異議を申し立てる」から申請します。理由は事実を簡潔に書きます。
4. 結果を待つ間、同じ種類の投稿を控えます。
5. 本当に違反だった場合は、同じ投稿を削除し、制作ルールを見直します。
6. 重大な制限に備えて、メールマガジンや他 SNS など**別の連絡手段**を持っておきます([data-backup-and-portability](../01-common/data-backup-and-portability.md))。

### 平常時の備え

- 規約の更新を月1回確認し、[verification-queue](../00-meta/verification-queue.md) に記録。
- 連携アプリの棚卸し、2段階認証。

## 具体例

| 状況 | 判断(⚪) |
|---|---|
| 友人の写真を許可なく投稿 | 本人の同意を取ってから |
| 企業から商品を無償で受け取り紹介 | 対価(無償提供を含む)があれば広告表記が必要([legal-compliance](../01-common/legal-compliance.md)) |
| 生成 AI で作った画像を投稿 | AI 情報ラベルを付け、キャプションでも明記 |
| 有名な曲を自分の編集アプリで BGM に | 権利処理が不明なら使わない。アプリの音楽ライブラリを使う |
| 他人のリールを「おすすめ紹介」として再投稿 | 許可がなければしない。リミックス・共有機能を使う |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 「規約違反で停止します」という DM のリンクを開いた | Instagram からの正式な通知はアプリ内に届く。DM のリンクは開かない |
| 異議申し立てで感情的に書いた | 事実(日時・内容・自分の権利)を簡潔に |
| 何が違反か分からず同じ投稿を繰り返した | アカウントステータスで理由を確認 |
| フォロワー購入サービスを使った | 規約違反のおそれ。利用をやめ、連携アプリを解除 |

## 注意点

- 規約・ガイドラインの本文は取得できておらず(#28)、このページの多くは一般論です。重要な判断は公式本文を確認してください。
- 法律が関わる場合(権利侵害・誹謗中傷・景品表示法など)は、専門家への相談も検討します。

## チェックリスト

- [ ] 利用規約・コミュニティガイドラインを一度読んだ
- [ ] 収益化する場合はパートナー収益化ポリシーを読んだ
- [ ] 他人の素材・音源の権利を確認している
- [ ] 案件にはタイアップ投稿ラベル、AI 生成には AI 情報ラベル
- [ ] アカウントステータスの場所を確認した
- [ ] 別の連絡手段(メール・他 SNS)を用意した

## 関連ページ / 次に読む

- [legal-compliance](../01-common/legal-compliance.md)、[ai-rules-by-platform](../01-common/ai-rules-by-platform.md)、[music-and-licensing](../01-common/music-and-licensing.md)
- [image-sources-and-copyright](../01-common/image-sources-and-copyright.md)、[crisis-response](../01-common/crisis-response.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://help.instagram.com/ | 2026-11-03 | 入口。本文は JavaScript 描画で未取得(#28) |
| https://help.instagram.com/512371932629820 | 2026-11-03 | 🟡 パートナー収益化ポリシー(検索要約) |
| https://help.instagram.com/517920941588885 | 2026-11-03 | 🟡 年齢要件(検索要約) |
| https://developers.facebook.com/documentation/instagram-platform/changelog.md | 2026-11-03 | ✅ AI 情報ラベル、タイアップ投稿ラベル、著作権保護 |
| https://creators.facebook.com/earn-money/earn-from-brands/ | 2026-11-03 | ✅ タイアップ投稿ラベルによる開示 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(ルールの3層、用語、公式で確認できた項目 ✅、違反時の詳しい手順、具体例、よくある失敗、チェックリスト)。既存の表・入口 URL は維持 |
