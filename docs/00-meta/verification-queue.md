---
title: 要検証リスト(公式確認待ち)
last_verified: 2026-11-03
confidence: ⚪
---

# 要検証リスト

> **このページで分かること**: 公式でまだ確認できていない事項の一覧。ここに載っている数値・条件は、使う前に公式で確かめてください。確認できたら該当ページを ✅ に更新し、この表に記録します。

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
| `www.w3.org`、`www.soumu.go.jp`、`www.cao.go.jp`、`www.ppc.go.jp`、`about.instagram.com`、`transparency.meta.com`、`www.tiktok.com/support`、`newsroom.tiktok.com`、`twitch.tv`、`bsky.network`(docs.bsky.app の転送先)、`one.google.com`、`www.lycbiz.com`、`kdp.amazon.co.jp`、`fanbox.cc` など創作支援系、`support.substack.com`、`support.spotify.com`、`www.capcut.com`、`docs.github.com` | **接続できず(2026-11-03 の全ページ加筆時、セッションのネットワーク制限)** | 許可後に再取得、または貼り付け |
| `www.facebook.com`(ヘルプ) | 403 | ブラウザで確認 |
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

## 全ページ加筆で見つかった要検証(2026年11月3日に追加)

全ページを初心者向けに加筆した際に、公式本文で確認できなかった事項です。既存の番号と重なる内容は、下の「既存項目の進捗」に記録しています。

| # | サービス | 確認事項 | 現在の記載 | 確度 | 参照ページ |
|---|---|---|---|---|---|
| 72 | 共通 | 総務省「国民のためのサイバーセキュリティサイト」のパスワード推奨(10文字以上・定期変更は不要) | 検索要約のみ(www.soumu.go.jp 接続不可) | 🟡 | [account-security](../01-common/account-security.md) |
| 73 | 共通 | 改正障害者差別解消法の施行日 2024年4月1日(条文の義務は e-Gov で ✅) | 検索要約のみ(www.cao.go.jp 接続不可) | 🟡 | [alt-text](../01-common/alt-text.md) |
| 74 | 共通 | WCAG 2.1 の 1.4.3(コントラスト 4.5:1、大きな文字 3:1)・2.3.1(1秒に3回の点滅) | www.w3.org 接続不可 | 🟡 | [brand-and-visual-guidelines](../01-common/brand-and-visual-guidelines.md)、[alt-text](../01-common/alt-text.md) |
| 75 | 共通 | 公的相談窓口(違法・有害情報相談センター、法務省の人権相談、誹謗中傷ホットライン、#9110)の現行名称・内容 | 自治体・県警の案内から | 🟡 | [crisis-response](../01-common/crisis-response.md) |
| 76 | 共通 | 文化庁「AIと著作権に関する考え方」本文の論点(取りまとめ日・主体は ✅) | 本文 PDF 未取得 | 🟡 | [ai-rules-by-platform](../01-common/ai-rules-by-platform.md)、[ai-usage-policy](../01-common/ai-usage-policy.md) |
| 77 | YouTube | ライブ配信: 初回の有効化にかかる時間(最大24時間か)、モバイル配信の登録者数条件 | 公式ページに数値なし | ⚪ | [05-youtube/08](../05-youtube/08-upload-and-shorts.md)、[live-streaming](../01-common/live-streaming.md) |
| 78 | YouTube | 投稿(コミュニティ投稿)の作成手順と画像枚数、タグ欄の文字数上限(500字) | 未取得 | ⚪ | [05-youtube/03](../05-youtube/03-text-and-discovery.md)、[05-youtube/04](../05-youtube/04-engagement.md) |
| 79 | YouTube | 自動字幕の編集手順、プレミア公開の要件 | 未取得 | ⚪ | [05-youtube/01](../05-youtube/01-setup-and-posting.md)、[05-youtube/03](../05-youtube/03-text-and-discovery.md) |
| 80 | YouTube | ポッドキャスト: 再生リストをポッドキャストに設定する手順、RSS 取り込みの日本での対象(RSS 提出の手順は ✅) | 二次資料 | 🟡/⚪ | [podcast-and-audio](../01-common/podcast-and-audio.md) |
| 81 | YouTube API | 未監査プロジェクトの非公開制限が今も有効か(2020年の改訂履歴は制限あり、現行の videos.insert リファレンスは制限なし)、OAuth トークンの有効期限 | 公式文書間で不一致 | ✅/不一致 | [05-youtube-data-api](../20-api/05-youtube-data-api.md)、[12-auth](../20-api/12-auth-oauth-and-tokens.md) |
| 82 | YouTube Create | 日本での提供状況 | 2024年の報道では対象外 | 🟡 | [video-editing-apps](../01-common/video-editing-apps.md) |
| 83 | TikTok | LIVE の年齢・フォロワー条件(50人か1,000人か)、ギフトを受け取れる条件、日本での適用 | 資料間で不一致 | 🟡 | [06-tiktok/04](../06-tiktok/04-engagement.md)、[live-streaming](../01-common/live-streaming.md) |
| 84 | TikTok | TikTok Shop(日本は 2025年6月30日開始と報道)の手数料・参加条件 | 公式ニュースルームの検索要約 | 🟡 | [06-tiktok/05](../06-tiktok/05-monetization.md) |
| 85 | TikTok | 違反ストライク(90日で消える)の現行の仕組み、AI 生成ラベルの現行の要件 | 2023〜2024年の発表の要約 | 🟡 | [06-tiktok/07](../06-tiktok/07-policies-and-checklist.md) |
| 86 | TikTok | ビジネスアカウントの音源制限、プロフィールリンクの条件、ユーザー名の変更間隔、最低年齢、予約投稿の提供範囲 | 一般知識 | ⚪ | [06-tiktok/01](../06-tiktok/01-setup-and-posting.md)、[06-tiktok/08](../06-tiktok/08-posting-and-editing.md) |
| 87 | TikTok API | 投稿系エンドポイントのレート制限、AI 生成の申告の API 上の扱い | 未確認 | ⚪ | [06-tiktok-api](../20-api/06-tiktok-api.md) |
| 88 | X | プロフィール: 自己紹介160字、ヘッダー 1500×500、プロフィール・ヘッダーでアニメ GIF 不可 | help.x.com の検索要約 | 🟡 | [02-x/01](../02-x/01-account-setup.md)、[02-x/03](../02-x/03-media-specs.md) |
| 89 | X | ハッシュタグは2個までを推奨、スペース・句読点は使えない | 検索要約 | 🟡 | [02-x/04](../02-x/04-text-hashtags.md) |
| 90 | X | 長文ポスト 25,000字、長文は予約不可・編集は1時間以内(旧版の記述) | 検索要約 | 🟡 | [02-x/02](../02-x/02-posting.md)、[02-x/04](../02-x/04-text-hashtags.md) |
| 91 | X | アプリで編集を使える契約(Premium のみか)、予約投稿の最大期間とモバイルでの可否、返信範囲の既定と投稿後の変更 | 未確認・検索要約 | ⚪/🟡 | [02-x/02](../02-x/02-posting.md)、[02-x/06](../02-x/06-engagement.md) |
| 92 | X | 旧収益分配の新規受付停止日(2026年8月7日と報道) | 検索要約・報道 | 🟡 | [02-x/07](../02-x/07-monetization.md) |
| 93 | X | 自動化ラベルの設定手順、登録の年齢条件 | 解説記事・未確認 | 🟡/⚪ | [02-x/10](../02-x/10-policies.md)、[02-x/01](../02-x/01-account-setup.md) |
| 94 | X | アプリのライブ配信の条件、Live Studio が Premium 限定か | help.x.com の検索要約と報道 | 🟡 | [live-streaming](../01-common/live-streaming.md) |
| 95 | X | アプリの検索窓での検索演算子(`from:`・`-` など)の挙動(API の演算子は ✅) | 未確認 | ⚪ | [social-listening](../01-common/social-listening.md) |
| 96 | X API | v2 の単純アップロードで返る項目名 | 概念コードのみ | ⚪ | [17-x-api-media](../20-api/17-x-api-media-and-rate-limits.md) |
| 97 | Threads | Instagram なしでの登録、Facebook アカウントでの登録の試験 | 二次資料 | 🟡 | [07-threads/01](../07-threads/01-setup-and-posting.md) |
| 98 | Threads | 編集は15分以内、予約投稿は75日先まで | 報道 | 🟡 | [07-threads/01](../07-threads/01-setup-and-posting.md) |
| 99 | Threads | アプリでもトピックタグは1投稿1つか、アプリでの代替テキストの付け方(API は ✅) | API のみ ✅ | 🟡/⚪ | [07-threads/03](../07-threads/03-text-hashtags-alt.md) |
| 100 | Threads | DM(18歳以上)・グループ・コミュニティの日本での提供、アプリのインサイト(90日分) | 報道・解説記事 | 🟡 | [07-threads/04](../07-threads/04-engagement.md)、[07-threads/06](../07-threads/06-analytics-and-tips.md) |
| 101 | Threads API | ベース URL が graph.threads.com か graph.threads.net か(公式 Posts ページは .com)、API 利用料の有無 | 一部 ✅ | ✅/⚪ | [04-threads-api](../20-api/04-threads-api.md) |
| 102 | Instagram | 自己紹介150字、プロフィールのリンク最大5件、プロフィールのグリッド表示比率と「プレビューを調整」 | 二次資料・報道 | 🟡 | [03-instagram/01](../03-instagram/01-account-setup.md)、[03-instagram/03](../03-instagram/03-media-specs.md) |
| 103 | Instagram | トライアルリールをアプリで使う条件、予約投稿の最大期間、ストーリーズ動画の1クリップ60秒(API は ✅) | 未確認・二次資料 | ⚪/🟡 | [03-instagram/12](../03-instagram/12-reels.md)、[03-instagram/13](../03-instagram/13-stories-and-highlights.md) |
| 104 | Instagram | プロアカウントから個人に戻したときのインサイトの扱い、ライブの最長時間(4時間)・アーカイブ30日の現行値 | 未確認・2020年の報道 | ⚪/🟡 | [03-instagram/01](../03-instagram/01-account-setup.md)、[live-streaming](../01-common/live-streaming.md) |
| 105 | Instagram API | 長期トークンを更新できる条件、API の利用料金の有無 | 未確認 | ⚪ | [03-instagram-graph-api](../20-api/03-instagram-graph-api.md) |
| 106 | Instagram Edits | 公開日(2025年4月22日)、透かしなし、日本での提供 | 報道 | 🟡 | [video-editing-apps](../01-common/video-editing-apps.md) |
| 107 | Facebook | Pages Insights の指標廃止日(公式文書内で 2025年6月15日と 2026年6月15日が併記) | 公式内で不一致 | ✅/不一致 | [08-facebook/05](../08-facebook/05-analytics-and-policies.md) |
| 108 | Facebook | アプリでのリールの長さ(公式は「3秒以上・上限なし」の古いページ、API は 3〜90秒)、ライブの条件(作成から60日・フォロワー100人、2022年ごろのページ) | 公式だが古い | ✅(古い) | [08-facebook/02](../08-facebook/02-media-specs.md)、[08-facebook/06](../08-facebook/06-reels-video-and-live.md) |
| 109 | Facebook | サブスクリプションの日本での提供(提供国一覧に日本なし・招待制)、Creator Fast Track の対象国、グループの参加質問の数(最大3問) | 公式(要追跡)・検索要約 | ✅/🟡 | [08-facebook/03](../08-facebook/03-engagement-and-groups.md)、[08-facebook/04](../08-facebook/04-monetization.md) |
| 110 | note | メンバーシップ(公開プラン最大5つ、会費は変更不可、審査あり)、「つぶやき」終了の日付、note ID 変更の影響、本人確認の要否 | 検索要約・未確認 | 🟡/⚪ | [04-note/01](../04-note/01-account-setup.md)、[04-note/02](../04-note/02-posting.md) |
| 111 | note | UTM パラメータの計測結果を確認できるか | 未確認 | ⚪ | [30-strategy/02](../30-strategy/02-funnel.md) |
| 112 | LINE | 2026年10月改定後の追加メッセージ料金(20万通まで3円、超過分2.5円)、リッチメニュー画像の容量上限 | 検索要約・未取得 | 🟡/⚪ | [02-line](../09-other-services/02-line-official-account.md)、[07-other-apis](../20-api/07-other-apis.md) |
| 113 | LINE | オープンチャットの参加上限(5,000人か10,000人か)、共同管理者100人 | 2019年の報道・自治体資料 | 🟡 | [community-management](../01-common/community-management.md) |
| 114 | Patreon・Ko-fi | Patreon の標準手数料10%(2025年8月4日以降)、Ko-fi Gold の月額 | 検索要約 | 🟡 | [10-creator-economy/01](../10-creator-economy/01-fan-club.md) |
| 115 | BOOTH・SUZURI | BOOTH のサービス利用料 5.6%+45円(2025年10月28日〜)、SUZURI の振込条件 | 報道・未確認 | 🟡/⚪ | [10-creator-economy/02](../10-creator-economy/02-goods-and-digital.md) |
| 116 | KDP | 日本語版ヘルプとの差、KDP セレクトの独占配信の条件、Kindle+ の日本での名称、配信コストの計算の扱い(英語版ヘルプで ✅) | 英語版で ✅ | ✅/⚪ | [10-creator-economy/03](../10-creator-economy/03-kdp-ebooks.md) |
| 117 | Amazon アソシエイト | 必須の表記文言、2026年4月20日の規約改定の内容 | 報道・未取得 | 🟡/⚪ | [10-creator-economy/04](../10-creator-economy/04-affiliate.md) |
| 118 | Substack | 手数料10%と Stripe の手数料(0.5% か 0.7% か) | 公式 FAQ の検索要約 | 🟡 | [newsletter-and-email](../01-common/newsletter-and-email.md) |
| 119 | 総務省・消費者庁 | 特定電子メール法の省令の表示事項、電気通信事業法の外部送信規律の対象と通知方法(条文の所在は ✅) | 詳細は一般知識 | ⚪ | [newsletter-and-email](../01-common/newsletter-and-email.md)、[privacy-and-personal-info](../01-common/privacy-and-personal-info.md) |
| 120 | Spotify | Spotify Partner Program の日本の対象・条件 | 規約の検索要約 | 🟡 | [podcast-and-audio](../01-common/podcast-and-audio.md) |
| 121 | Discord | コミュニティ機能を有効にする条件 | 検索要約 | 🟡 | [community-management](../01-common/community-management.md) |
| 122 | JASRAC | 利用許諾契約を結んでいる動画サービスの最新一覧(TikTok を含むか) | 報道 | 🟡 | [music-and-licensing](../01-common/music-and-licensing.md) |
| 123 | CapCut | 現行の利用規約のコンテンツ利用許諾条項、商用利用の範囲、料金 | 報道のみ(capcut.com 接続不可) | 🟡 | [video-editing-apps](../01-common/video-editing-apps.md) |
| 124 | 税務 | 所得税の確定申告が不要(副業所得20万円以下)でも住民税の申告が必要か、確定申告する場合に20万円以下の副業所得も含めるか | 一般知識 | ⚪ | [30-strategy/04](../30-strategy/04-tax-and-business.md) |
| 125 | 税務 | 事業所得と雑所得を分ける具体的な基準、青色申告特別控除が雑所得に使えないこと、減価償却の基準額 | No.1500 に基準の記載なし・一般知識 | ⚪ | [30-strategy/04](../30-strategy/04-tax-and-business.md) |
| 126 | 税務 | 開業届の提出期限が「1か月以内」から「確定申告期限まで」に変わった時期(No.2090 の現行記載は ✅) | 時期は未確認 | ✅/⚪ | [30-strategy/04](../30-strategy/04-tax-and-business.md) |
| 127 | 税務 | SNS 投稿制作の報酬が源泉徴収の対象になるか、簡易課税の事業区分 | 契約内容しだい | ⚪ | [30-strategy/04](../30-strategy/04-tax-and-business.md)、[30-strategy/08](../30-strategy/08-consumption-tax-and-invoice.md) |
| 128 | インボイス | 登録番号の形式(T+13桁)と公表サイトの公開範囲、プラットフォーム経由の販売・海外サービス(リバースチャージ)の扱い | 解説記事・要確認 | ⚪ | [30-strategy/08](../30-strategy/08-consumption-tax-and-invoice.md)、[40-pricing](../40-pricing/README.md) |
| 129 | 料金 | Meta Verified の 2026年の日本価格(#48 の一部)、海外ツールの価格が税抜表示で購入時に消費税が加算されるか、販売サービスの手数料を税込・税抜のどちらに掛けるか | 確認できず・要確認 | 🟡/⚪ | [40-pricing/03](../40-pricing/03-meta.md)、[40-pricing/04](../40-pricing/04-other-services.md)、[40-pricing/05](../40-pricing/05-ai-and-creative-tools.md) |
| 130 | GitHub | Actions の Secrets の画面名・書式(docs.github.com 接続不可) | 一般知識 | ⚪ | [08-automation](../20-api/08-automation-and-tools.md)、[13-secrets](../20-api/13-secrets-management.md) |

### 既存項目の進捗(2026年11月3日の加筆時)

| # | 進捗 | 参照ページ |
|---|---|---|
| 2 | Meta 公式ブログ(2023年11月)は 5,000人、ヘルプの検索要約は 500人。不一致のまま | [03-instagram/07](../03-instagram/07-monetization.md) |
| 5・6 | note の手数料内訳(事務手数料 カード5%・キャリア15%・PayPay7%、利用料10%・定期購読マガジン20%、振込270円)、価格範囲100〜50,000円(上限100,000円の会員種別あり)、振込申請1,000円以上・毎月2日確定を検索要約で記載(🟡)。公式本文は未取得 | [04-note/07](../04-note/07-monetization.md) |
| 13・16 | note のハッシュタグ上限・代替テキストの現行手順は未確認(代替テキストは 2022年4月の機能追加の報道のみ) | [04-note/04](../04-note/04-text-hashtags.md)、[04-note/05](../04-note/05-alt-text.md) |
| 14 | 各 SNS の2段階認証・Exif 削除・非表示/ブロックの UI 名称は一般論のまま | [account-security](../01-common/account-security.md) |
| 15 | **X 分は解消**: 日本語・絵文字は2、URL は23として数え、上限は重み付きで280(✅ docs.x.com counting-characters) | [02-x/04](../02-x/04-text-hashtags.md) |
| 18 | Instagram リールのアプリ上限は 3分(2025年1月の報道)と 20分の資料があり不一致 | [03-instagram/12](../03-instagram/12-reels.md) |
| 29 | YouTube Shorts の収益分配 45%、AdSense の支払い基準額 ¥8,000 は ✅。長尺動画の 55% は ⚪ のまま | [05-youtube/05](../05-youtube/05-monetization.md) |
| 31 | **解消**: タイトル100字・説明5,000字、ハッシュタグ(最大3つ表示、60個超ですべて無効)、チャプター(0:00開始・3つ以上・各10秒以上)、バナーの安全領域 1235×338(✅ YouTube ヘルプ) | [05-youtube/03](../05-youtube/03-text-and-discovery.md)、[05-youtube/02](../05-youtube/02-media-specs.md) |
| 32 | API の審査条件は ✅(未監査は SELF_ONLY・24時間で5人まで)。アプリの動画の長さ(60分/10分/3分)・容量、キャプション(2,200字/4,000字)、フォト投稿35枚は 🟡 のまま | [06-tiktok-api](../20-api/06-tiktok-api.md)、[06-tiktok/02](../06-tiktok/02-media-specs.md) |
| 33 | TikTok Creator Rewards の条件は検索要約(🟡)のまま。support.tiktok.com・newsroom.tiktok.com はこの環境から接続できない | [06-tiktok/05](../06-tiktok/05-monetization.md) |
| 34 | **タグの個数は解消**: トピックタグは1投稿に1つ・1〜50字(✅ Threads API 文書)。収益化は記事間で矛盾(🟡) | [07-threads/03](../07-threads/03-text-hashtags-alt.md)、[07-threads/05](../07-threads/05-monetization.md) |
| 35 | Facebook の通常動画の長さ・容量、画像仕様、Business Suite の予約期間は未確認。ページ投稿の API 予約は10分後〜30日後(✅) | [08-facebook/02](../08-facebook/02-media-specs.md)、[07-other-apis](../20-api/07-other-apis.md) |
| 38 | **解消**: `videos.insert`・`search.list` は1回1ユニット、専用枠で100回/日(✅ developers.google.com determine_quota_cost) | [05-youtube-data-api](../20-api/05-youtube-data-api.md) |
| 39 | Bluesky の動画 300MB になった時期(6月か8月か)が不明。docs.bsky.app は転送先に接続できない | [09-other-services/01](../09-other-services/01-bluesky.md) |
| 40 | **料金プランは解消**: 0円/5,000円/15,000円(税別)、無料通数 200/5,000/30,000通(✅ LINE 開発者文書)。改定後の追加メッセージ料金は #112 | [02-line](../09-other-services/02-line-official-account.md) |
| 41 | **KDP は解消**: 日本で 70% ロイヤリティは 250〜1,650円(税込)かつ KDP セレクト登録(✅ kdp.amazon.com)。FANBOX・Fantia の手数料は不一致(🟡)、Fantia で Visa・Mastercard が使えない件(🟡) | [10-creator-economy/01](../10-creator-economy/01-fan-club.md)、[10-creator-economy/03](../10-creator-economy/03-kdp-ebooks.md) |
| 42 | Twitch Affiliate の新条件(25人・4時間・4日・平均3人)は二次資料、Partner は資料間で不一致(twitch.tv 接続不可) | [09-other-services/03](../09-other-services/03-twitch.md) |
| 46・47 | Google AI プラン・YouTube Premium の日本の公式価格は報道値のまま。一部の Google AI Pro に YouTube Premium Lite が含まれることは ✅ | [40-pricing/02](../40-pricing/02-google.md) |
| 56 | Instagram のハッシュタグ5個上限の公式発表元、3個上限のテストは報道のみ | [hashtags](../01-common/hashtags.md) |
| 60 | X のアーカイブ手順(help.x.com の検索要約)、Meta「情報のダウンロード」の形式・所要時間(解説記事)は 🟡 | [data-backup-and-portability](../01-common/data-backup-and-portability.md) |

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

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(#1〜#63) |
| 2026-11-03 | X Subscriptions・Discord の項目を #64〜#71 として追加(別セッションで #59〜#66 と重複していたものを付け替え) |
| 2026-11-03 | 全ページ加筆で見つかった項目 #72〜#130 と、既存項目の進捗を追加。接続できなかったホストを冒頭の表に追記 |
