---
title: 未整備・追加すべき事項の考察(検索調査つき)
platform: common
topic: meta
last_verified: 2026-11-03
confidence: 🟡
---

# 未整備・追加すべき事項の考察

2026年(皇紀2686年・令和8年)11月3日の検索調査で見つけた**最新動向**と、**未整備の領域**をまとめます。調査結果の多くは報道・解説記事(🟡)で、公式確認が必要です。

## 1. 検索調査で分かった最近の動き

| 領域 | 動き | 確度 | 反映先 |
|---|---|---|---|
| **X** | 旧収益分配は 2026年9月7日に終了、9月8日から **Original Content Rewards** の申請開始(自動移行なし)。条件は 18歳以上・Premium 系・認証済みフォロワー500人以上・直近90日で50万インプレッション以上(複数の報道で一致) | 🟡 | [X 収益化](../02-x/07-monetization.md) |
| **X API** | 従量課金、URL 付き $0.200、いいね・フォロー・引用の API 削除、返信は呼び出された場合のみ、`paid_partnership` | ✅ | [02-x-api](../20-api/02-x-api.md) |
| **X Money** | 米国の Premium/Premium+ 向けに 2026年7月に開始。**日本では未提供**(商標出願のみ報道) | 🟡 | [01-x-and-grok](../40-pricing/01-x-and-grok.md) |
| **Grok** | 日本政府が 2026年1月、性的画像の生成に安全対策強化を要請と報道 | 🟡 | [ai-rules](../01-common/ai-rules-by-platform.md) |
| **Meta One** | 2026年9月発表。Instagram Plus 319円、Core 949円、Premium 2,900円、クリエイター向けバンドル2,000円〜 | 🟡 | [03-meta](../40-pricing/03-meta.md) |
| **Instagram のハッシュタグ** | 上限 5 個に段階的に引き下げ(2025年12月〜と報道)。API 文書は 30 のまま | 🟡/✅ | [hashtags](../01-common/hashtags.md) |
| **Instagram** | 新形式「Instants」、AI キャプション、リールの成果予測ツール、オリジナル優遇(2026年春〜と報道)。Instagram アフィリエイト | 🟡 | 要追跡 |
| **Threads** | 4億 MAU、クリエイター収益シェアは主に米国など。**日本は対象外**(2026年4月時点) | 🟡 | [07-threads/05](../07-threads/05-monetization.md) |
| **YouTube** | 収益化条件の緩和(500人で機能の一部 ✅)、Shorts の視聴回数の数え方変更(2025年3月31日 ✅)、**YouTube ショッピングのアフィリエイトが日本に導入(楽天市場がパートナー)** | ✅/🟡 | [05-monetization](../05-youtube/05-monetization.md) |
| **TikTok** | 日本の TikTok Shop は GMV の約6割がライブ経由と報道 | 🟡 | [06-tiktok/05](../06-tiktok/05-monetization.md) |
| **Google AI** | AI Pro に YouTube Premium Lite が付属、Ultra 5x/20x | 🟡 | [02-google](../40-pricing/02-google.md) |
| **LINE** | 2026年10月に追加メッセージ料金の改定 | 🟡 | [LINE](../09-other-services/02-line-official-account.md) |
| **note** | Canva 連携の終了(2025年12月1日) | 🟡 | [11-tool-integrations](../20-api/11-tool-integrations.md) |

## 2. 今回追加したページ

| ページ | 内容 |
|---|---|
| [40-pricing](../40-pricing/README.md)(7) | 料金プラン(X・Grok・Google・Meta・その他・AI/制作/予約ツール・費用見積り) |
| [mobile-viewing-optimization](../01-common/mobile-viewing-optimization.md) | iPhone・Android の画面特性に基づく画像・動画サイズの考察 |
| [alt-text](../01-common/alt-text.md)(全面改訂) | ALT の詳細(サービス別、種類別、日本語、動画のアクセシビリティ、AI) |
| [hashtags](../01-common/hashtags.md)(全面改訂) | ハッシュタグの効率的な使い方 |
| [ai-rules-by-platform](../01-common/ai-rules-by-platform.md) | AI 利用のルールと設定 |
| [10-benefits-of-api](../20-api/10-benefits-of-api.md) / [11-tool-integrations](../20-api/11-tool-integrations.md) | API のメリット、ツール連携 |
| [link-in-bio-and-utm](../01-common/link-in-bio-and-utm.md) | リンク設計・UTM 計測 |
| [data-backup-and-portability](../01-common/data-backup-and-portability.md) | バックアップ・持ち出し |
| [privacy-and-personal-info](../01-common/privacy-and-personal-info.md) | 個人情報の扱い |
| [music-and-licensing](../01-common/music-and-licensing.md) | 音楽・音源の権利 |
| [07-sponsorship-and-media-kit](../30-strategy/07-sponsorship-and-media-kit.md) | 案件・メディアキット |

## 3. まだ未整備の領域(優先度順)

| 優先 | 領域 | 内容 | 前提 |
|---|---|---|---|
| 高 | **公式本文の裏取り** | X アプリの仕様と収益分配、note の手数料、TikTok、国税庁、Meta のアプリ内ヘルプ | 本文の貼り付け/取得 |
| 高 | **収益化の新動向の公式確認** | Original Content Rewards、YouTube ショッピングの条件、Instagram のアフィリエイト、TikTok Shop | 公式ヘルプ |
| 高 | **税務** | 副業の確定申告、インボイス、海外サービスの支払い(消費税) | 国税庁 |
| 中 | 動画編集アプリ | CapCut、Instagram の編集アプリ、YouTube Create | 公式の仕様 |
| 中 | ライブ配信 | YouTube ライブ、X、Instagram ライブ、TikTok ライブの設定・収益・規約 | 公式 |
| 中 | ニュースレター・メール | Substack、メルマガの配信(自前の資産)|  |
| 中 | ポッドキャスト・音声 | Spotify、YouTube のポッドキャスト | |
| 中 | 多言語・海外 | 英語の併記、海外ファン向け | |
| 中 | ソーシャルリスニング | 言及・ブランドのモニタリング | |
| 中 | コミュニティ運営 | Discord、LINE オープンチャット、Facebook グループ | |
| 低 | Pinterest・Lemon8・ニコニコ | [99-planned](../99-planned/README.md) | |
| 低 | 契約書・請求書のひな形 | 専門家の確認が必要 | |
| 低 | 保険・法人化の判断 | 専門家 | |

## 4. 継続的に追う指標(月次)

- 各サービスの**料金・上限・収益化条件**の変更(公式のお知らせ・changelog)
- X の changelog(https://docs.x.com/changelog.md)、Meta の開発者お知らせ、YouTube のヘルプの更新
- 日本政府・消費者庁・文化庁の動き(ステマ、AI、著作権)

## 5. この考察の限界

- 検索結果の多くは**マーケティング系ブログ**で、公式発表ではない。数値と時期が一致しないものは両論併記した。
- 検索は日本語・英語。ニッチな領域(ニコニコ、個別 SNS)は未調査。
