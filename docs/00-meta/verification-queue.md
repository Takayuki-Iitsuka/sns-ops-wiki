---
title: 要検証リスト(公式確認待ち)
last_verified: 2026-11-03
confidence: ⚪
---

# 要検証リスト

公式ヘルプ・開発者文書で確認できていない項目です。確認したら該当ページを ✅ に更新し、「確認済み」の表へ移します。番号は参照されているため**振り直さない**こと。

## 取得できる公式ソースと、できないソース(2026年(皇紀2686年・令和8年)11月3日時点)

| ホスト | 状況 | 取得方法 |
|---|---|---|
| `docs.x.com` | ✅ 取得できる | URL 末尾に `.md` を付けると Markdown で取得(`/llms.txt` に索引) |
| `developers.facebook.com`(Instagram・Threads) | ✅ 取得できる | `/documentation/...` の末尾に `.md` |
| `support.google.com`(YouTube ヘルプ) | ✅ 取得できる | `?hl=ja` の HTML を本文抽出 |
| `developers.line.biz`、`www.caa.go.jp`、`laws.e-gov.go.jp` | ✅ 取得できる | HTML |
| `help.instagram.com` | 接続可だが本文は JavaScript 描画で空 | 要:貼り付け |
| `help.x.com`、`www.help-note.com`、`devcommunity.x.com` | **Cloudflare の bot 確認で 403** | 要:ブラウザから貼り付け |
| `discord.com`、`support.discord.com`、`creator-support.discord.com`、`legal.x.com` | **名前解決できず(セッションのネットワーク制限)** | 許可後に再取得、または貼り付け |
| `developers.tiktok.com`、`support.tiktok.com`、`atproto.com`、`docs.bsky.app`、`dev.twitch.tv`、`kdp.amazon.com`、`www.nta.go.jp` 等 | 接続可。本文は未取得 | 次回取得 |

## 優先度 高(運用・収益・API に直結)

| # | サービス | 確認事項 | 現在の記載 | 確度 |
|---|---|---|---|---|
| 1 | X | アプリでの収益分配プログラムの現行名称・条件(`help.x.com` は取得不可) | 旧 Creator Revenue Sharing の終了と後継の報道のみ | 🟡 |
| 2 | Instagram | Gifts のフォロワー条件(500 / 1,000 / 5,000 と不一致) | 不一致 | 🟡 |
| 3 | Instagram | Subscriptions の条件(10,000 フォロワーとする資料) | 要確認 | 🟡 |
| 4 | Instagram | アプリのフィード写真の比率に 3:4 が追加されたか(API は 4:5〜1.91:1 ✅) | 二次資料のみ | 🟡 |
| 5 | note | 有料記事・メンバーシップ・サポートの手数料率(`www.help-note.com` は取得不可) | 10%(税抜)+決済手数料とする比較記事のみ | 🟡 |
| 6 | note | 有料記事の価格範囲、振込条件 | 未確認 | ⚪ |
| 36 | X API | 旧 Basic/Pro の**自動移行日**(6月1日・9月1日は X Developers の告知経由の二次情報)、v1.1 の廃止日(公式文書に記載なし) | [02-x-api](../20-api/02-x-api.md) §4 | 🟡 |
| 37 | Instagram API | **公開上限が 100 か 50 か**(同一の公式ページ内で併記)、アプリ審査の要件 | [03-instagram-graph-api](../20-api/03-instagram-graph-api.md) §6 | ✅/不一致 |
| 38 | YouTube API | `videos.insert` のクォータコスト、監査の手順(`developers.google.com` 未取得) | 二次資料のみ | 🟡 |
| 29 | YouTube | 収益配分の割合(55% など)、メンバーシップの価格、エンゲージ ビューの定義(YPP の資格要件は ✅) | ⚪ | ⚪ |

## 優先度 中(画像・動画・投稿仕様)

| # | サービス | 確認事項 | 現在の記載 | 確度 |
|---|---|---|---|---|
| 7 | X(アプリ) | アプリでの画像・動画の上限(API は ✅) | 5MB、2:1〜3:4 は全体表示(古いページの要約) | 🟡 |
| 9 | Instagram(アプリ) | 画像のファイル形式・容量上限 | 8〜30MB と不一致 | ⚪ |
| 10 | Instagram(アプリ) | カルーセル最大枚数(API は 20 ✅) | 20 | ⚪/✅ |
| 11 | Instagram | ハッシュタグの公式推奨数(上限 30 は API で ✅) | 推奨は少数とされる | ⚪ |
| 12 | note | 画像形式・本文内画像の推奨 | 見出し 1280×670、10MB | 🟡 |
| 13 | note | ハッシュタグの上限数 | 未確認 | ⚪ |
| 16 | note | 画像に代替テキストを設定する機能の有無と手順 | 未確認 | ⚪ |
| 17 | X・Instagram・YouTube | ヘッダー/バナー/カバーの推奨サイズ(YouTube バナーは本文未取得) | X 1500×500、YouTube 2560×1440(二次資料) | 🟡 |
| 18 | X・Instagram・TikTok ほか(アプリ) | アプリからの動画の長さ・容量(API は X・Instagram・Threads で ✅) | Instagram リールのアプリ上限は不一致 | 🟡 |
| 31 | YouTube | タイトル100字・説明5,000字・ハッシュタグの扱い、バナーの寸法 | ⚪ | ⚪ |
| 32 | TikTok | 動画の長さ・容量、キャプション文字数、フォト投稿、API の審査条件 | 二次資料で不一致 | 🟡 |
| 33 | TikTok | Creator Rewards の条件・日本の対象 | フォロワー1万・直近30日10万回視聴とする資料 | 🟡 |
| 34 | Threads | ハッシュタグ(トピックタグ)の個数、収益化プログラムの有無(文字数・メディア・上限は ✅) | タグ1つとする二次資料 | 🟡 |
| 35 | Facebook | 収益化の条件、画像・動画の公式仕様 | 資料により不一致 | 🟡 |
| 39 | Bluesky | 画像 1MB/2MB、動画 3分・100MB / 10分・300MB の現行値(`atproto.com` 未取得) | 不一致 | 🟡 |
| 40 | LINE | 料金プランの最新(2026年10月の改定)、画像の容量上限(リッチメニューのサイズは ✅) | 代理店系の記事のみ | 🟡 |
| 41 | 創作支援系 | FANBOX・Fantia・Patreon・Ko-fi・BOOTH・KDP の手数料、画像仕様(KDP 表紙を含む) | 比較記事で不一致 | 🟡 |
| 42 | Twitch | Affiliate/Partner の現行条件 | 資料により不一致 | 🟡 |
| 43 | note | 公式の公開 API の有無 | 未確認 | ⚪ |

## 料金・新動向・運用(2026年11月3日に追加)

| # | 確認事項 | 現在の記載 | 確度 |
|---|---|---|---|
| 44 | X Premium(Basic / Premium / Premium+)の日本円の現行価格(`help.x.com` は取得不可) | Premium+ は Web 1か月 6,080円(2025年2月改定)。他は不明/不一致 | 🟡 |
| 45 | Grok / SuperGrok の価格、X Premium との関係、xAI API(`docs.x.ai` 未取得)の公式単価 | 比較サイトのみ(SuperGrok 約 $30 など)。不一致 | 🟡 |
| 46 | Google AI Plus / Pro / Ultra の日本価格と特典(`one.google.com` 未取得)、Gemini Developer API(`ai.google.dev` 未取得) | 報道(Plus 1,200円、Pro 2,900円、Ultra 5x 14,500円、20x 32,000円)。Google Cloud の料金は ✅ | 🟡/✅ |
| 47 | YouTube Premium の日本の現行価格(iPhone は割高) | Gizmodo/Selectra(2026年4月ごろ) | 🟡 |
| 48 | Meta One・Meta Verified の日本価格 | 報道(Instagram Plus 319円、Core 949円、Premium 2,900円) | 🟡 |
| 49 | note プレミアム(500円)・note pro(80,000円/月)の公式価格、販売手数料 | help-note 記事の検索要約 | 🟡 |
| 50 | ChatGPT・Claude の日本円価格 | ドル建て(Plus/Pro $20、$100、$200 など) | 🟡 |
| 51 | Canva Pro・Adobe Express・CapCut Pro の価格 | Canva は不一致、他は未確認 | 🟡 |
| 52 | Buffer・Later・Hootsuite・Zapier・Make・IFTTT の現行価格 | 比較記事 | 🟡 |
| 53 | Instagram のアフィリエイトの日本での参加条件 | 報道のみ | 🟡 |
| 54 | X Money の日本提供(現状は米国のみ) | 商標出願の報道のみ | 🟡 |
| 55 | YouTube ショッピング アフィリエイト(日本、楽天市場がパートナー)の参加条件 | 報道のみ | 🟡 |
| 56 | Instagram のハッシュタグ上限 5 個(日本・API への適用)、公式 API 文書の「30個」との差 | 報道 vs 公式 API 文書 | 🟡/✅ |
| 57 | AI 開示の設定: Meta・TikTok・X の公式ルール、学習への利用のオプトアウト手順 | 報道・解説記事 | 🟡 |
| 58 | 端末の公式仕様(iPhone 17 以降、Pixel 10 など)、日本の機種別シェア、各アプリのフィード表示幅 | 一般知識 | ⚪ |
| 59 | Google Cloud の Veo 料金「1 count」の単位(秒か本か) | 公式ページに単位の説明なし | ✅数値/単位不明 |
| 60 | 各サービスのデータ書き出し機能の名称・手順(X、Instagram、TikTok、note、Bluesky、LINE) | 一般知識 | ⚪ |
| 61 | 個人情報保護法・外部送信規律の具体的な要件 | 一般知識 | ⚪ |
| 62 | 音楽の権利: JASRAC などとプラットフォームの包括契約の範囲 | 一般知識 | ⚪ |
| 63 | 案件の契約・報酬の相場・源泉徴収の扱い | 一般知識 | ⚪ |

## 法務・税務・規約(専門資料での確認)

| # | 確認事項 | 確認先 |
|---|---|---|
| 22 | 副業所得20万円の確定申告要否、インボイス、開業届・青色申告 | 国税庁 |
| 23 | 有料での旅行・ツアーの募集と旅行業法の関係 | 観光庁・都道府県 |
| 24 | Amazon アソシエイト等の広告表記の規約 | 各プログラム規約 |
| 26 | 著作権の保護期間(死後70年、2018年12月30日の改正) | 文化庁 |
| 27 | 生成 AI 画像のラベル表示に関する各サービスの規約(Instagram API の `is_ai_generated` は ✅) | 各サービスの規約 |
| 28 | X・Instagram・note・TikTok・Threads の利用規約・ガイドライン本文(各 policies の根拠) | 各サービスの規約ページ |

## X Subscriptions・Discord(2026年11月3日に追加)

| # | 確認事項 | 現在の記載 | 確度 |
|---|---|---|---|
| 64 | X Subscriptions の資格要件(「500万インプレッション/3か月・ID 確認」か「フォロワー500人・30日」か)、Premium 契約の要否、日本での提供(`help.x.com`・`legal.x.com` は取得不可) | [12-subscriptions](../02-x/12-subscriptions.md) §2 | 🟡 |
| 65 | X Subscriptions の取り分(5万ドルまで最大97%、以降80%)、アプリ内購入手数料、最低支払額、価格帯 | [12-subscriptions](../02-x/12-subscriptions.md) §3 | 🟡 |
| 66 | X Subscriptions の機能(購読者限定ポスト・返信・Spaces・DM)、API での取得可否 | [12-subscriptions](../02-x/12-subscriptions.md) §4〜5 | 🟡/⚪ |
| 67 | Discord Server Subscriptions の条件(メンバー数 500 / 1,000、サーバー作成から30日、コミュニティ有効化、年齢)と**日本での提供**(`discord.com` 系は取得不可) | [04-discord](../09-other-services/04-discord.md) §5 | 🟡 |
| 68 | Discord の手数料(10%)、ストア手数料、Premium Apps(15% / 30%)、最低払出額($100) | [04-discord](../09-other-services/04-discord.md) §5 | 🟡 |
| 69 | Discord のアップロード上限、ブーストの段階と必要数、アイコン・バナー・絵文字・ステッカーの寸法 | [04-discord](../09-other-services/04-discord.md) §4 | ⚪ |
| 70 | Discord API の上限(Webhook の文字数・embed、レート制限)、特権インテントの審査 | [04-discord](../09-other-services/04-discord.md) §8 | ⚪ |
| 71 | Discord の最小年齢、Server Monetization Policy、Community Guidelines の要点 | [04-discord](../09-other-services/04-discord.md) §6 | ⚪/🟡 |

## 優先度 低

| # | 確認事項 |
|---|---|
| 14 | 各サービスの日本語 UI 名称(ボタン名)が最新か |
| 15 | 各サービスの文字数カウント規則(全角・URL・絵文字) |

## 確認済み(✅)

| # | 内容 | 出典(取得日 2026年(皇紀2686年・令和8年)11月3日) | 反映先 |
|---|---|---|---|
| 8 | X の alt text は**最大1,000字**(API の `alt_text`) | docs.x.com Create Media Metadata | [02-x/05-alt-text](../02-x/05-alt-text.md) |
| 25 | **2023年(皇紀2683年・令和5年)10月1日からステルスマーケティングは景品表示法違反** | 消費者庁 | [legal-compliance](../01-common/legal-compliance.md) |
| — | X API v2 が primary、v1.1 は「いずれ非推奨」。従量課金、単価、Owned Reads、メディア上限、レート制限、2026年の変更 | docs.x.com | [02-x-api](../20-api/02-x-api.md)、[x/03](../02-x/03-media-specs.md) |
| — | Instagram API の画像・リール仕様、キャプション2,200字・タグ30・メンション20、`alt_text`、`is_ai_generated`、パートナーシップ表示 | developers.facebook.com | [03-instagram-graph-api](../20-api/03-instagram-graph-api.md) |
| — | Threads API の画像・動画・500字・上限(250/1,000/100/500) | developers.facebook.com | [04-threads-api](../20-api/04-threads-api.md)、[07-threads/02](../07-threads/02-media-specs.md) |
| 29(一部) | **YPP の資格要件(500/1,000人、視聴時間、Shorts 視聴回数)、日本が対象国、機能一覧、再申請の期間** | YouTube ヘルプ | [05-monetization](../05-youtube/05-monetization.md) |
| 30 | YouTube のサムネイル(モバイル2MB・PC50MB、16:9 と 9:16、推奨解像度)、エンコード設定、Shorts 3分 | YouTube ヘルプ | [05-youtube/02](../05-youtube/02-media-specs.md) |
| 40(一部) | LINE リッチメニュー 2500×1686 / 2500×843 | LINE 開発者文書 | [LINE](../09-other-services/02-line-official-account.md) |

## 完了・移管

| # | 内容 | 状況 |
|---|---|---|
| 19〜21 | 古事記・日本書紀に関する確認(底本、神名、年中行事) | **別の wiki へ移管**(このリポジトリは SNS 専用) |
