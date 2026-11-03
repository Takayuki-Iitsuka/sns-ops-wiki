---
title: TikTok API
platform: tiktok
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.tiktok.com/doc/content-posting-api-get-started
  - https://developers.tiktok.com/doc/content-sharing-guidelines
  - https://developers.tiktok.com/doc/oauth-user-access-token-management
  - https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit
---

# TikTok API

> **このページで分かること**: TikTok の API の種類、投稿(Content Posting API)の準備と流れ、**未監査アプリの制限**、投稿数の上限、トークン、守るべき画面の要件。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)

> 以前は「公式・二次資料とも調査できていません」(⚪ #32)でしたが、2026年(皇紀2686年・令和8年)11月3日に **developers.tiktok.com の公式文書を直接取得**して確認しました(✅)。画面名などは変わる可能性があります。

## 概要

TikTok の API は **TikTok for Developers**(developers.tiktok.com)でアプリを登録して使います。投稿用の **Content Posting API** には、利用者が自分で操作する画面(UI)の要件が細かく決まっており、**「人が確認して投稿する」アプリ**を前提にしています。

特に重要なのは次の2点です。

1. **監査(audit)を通っていないアプリからの投稿は、すべて非公開(本人のみ閲覧)に制限**されます(✅)。
2. 他のサービスからのコピー投稿や、**自社で管理するアカウントへの社内ツール的なアップロードは、意図された用途ではない**とされています(✅)。

→ 個人やお店の運用で「自分のアカウントに自動投稿したい」だけなら、**公式アプリの予約投稿や公認ツールを使う方が現実的**です。

## 用語

| 用語 | 意味 |
|---|---|
| TikTok for Developers | TikTok の開発者サイト。アプリ登録・審査を行う |
| Login Kit | TikTok アカウントでのログイン(OAuth) |
| Content Posting API | 動画・写真の投稿 API |
| Direct Post(直接投稿) | アプリから直接公開する方式 |
| `video.publish` | 直接投稿に必要なスコープ |
| unaudited client(未監査のクライアント) | 監査を通っていないアプリ |
| `SELF_ONLY` | 本人のみ閲覧(非公開) |
| `creator_info` | 投稿前に取得する、投稿者の情報と投稿可能な条件 |
| `FILE_UPLOAD` / `PULL_FROM_URL` | ファイルを送る方式 / TikTok が URL から取りに行く方式 |
| domain verification(ドメイン認証) | URL から取らせるために、自分のドメインを登録・確認すること |

## 主な API(⚪ 一覧。投稿以外の詳細は未取得)

| API | 用途 |
|---|---|
| Login Kit | TikTok アカウントでのログイン、OAuth |
| Content Posting API | 動画/フォトの投稿(下書きへのアップロード、または直接投稿) |
| Display API | 自分のプロフィール・動画の表示 |
| Research API | 研究者向け(申請・審査) |

## 準備の手順(✅ [Content Posting API get started](https://developers.tiktok.com/doc/content-posting-api-get-started))

1. TikTok for Developers で**アプリを登録**する。
2. アプリに **Content Posting API** を追加し、**Direct Post** の設定を有効にする。
3. `video.publish` スコープの承認を得る。投稿する利用者もアプリに許可する。
4. 利用者のアクセストークンと open ID を取得する。
5. 公開投稿を可能にするには**監査**を申請する。

## 未監査アプリの制限と上限(✅ [content sharing guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines))

| 項目 | 内容 |
|---|---|
| 未監査アプリの投稿 | **`SELF_ONLY`(本人のみ)に制限**。投稿時点でアカウントが非公開である必要 |
| 未監査アプリの利用者数 | **24時間で5人まで** |
| 後から公開にする | アカウントを公開にしてから、各投稿の公開範囲を「全員」に変更 |
| 投稿数の上限 | 1クリエイターアカウントあたり**おおむね15件/日**(すべての Direct Post アプリで共有) |
| アプリごとの上限 | 監査申請の利用見込みに基づく、24時間のアクティブなクリエイター数の上限 |

## 投稿の流れ(✅ get started)

1. **投稿者情報の取得**: `POST /v2/post/publish/creator_info/query/`。投稿できない状態なら、中止して利用者に後で再試行するよう伝える(✅ ガイドライン)。
2. **投稿の開始**: `POST /v2/post/publish/video/init/`(`post_info` と `source_info`)。写真は `/v2/post/publish/content/init/`。
3. **アップロード**: `FILE_UPLOAD` なら返された `upload_url` に PUT。`PULL_FROM_URL` は**認証済みのドメイン・URL プレフィックス**からのみ(写真はこの方式のみ)。
4. **状態の確認**: `POST /v2/post/publish/status/fetch/`(`publish_id`)。処理は非同期。

## 画面(UI)の必須要件(✅ ガイドライン)

| 要件 | 内容 |
|---|---|
| 投稿者の表示 | 投稿画面で最新の `creator_info` を取得し、ニックネームを表示 |
| 動画の長さ | `max_video_post_duration_sec` 以内か確認 |
| 公開範囲 | 利用者が**既定値なし**のドロップダウンから選ぶ |
| コメント・デュエット・ステッチ | どれも**既定でオフ** |
| 商業コンテンツの開示 | 既定オフ。オンなら「Your brand」「Branded content」の少なくとも1つを選ばないと公開ボタンは無効。ブランドコンテンツは非公開にできない |
| 同意 | 公開前に音楽利用の確認(ブランドコンテンツならブランドコンテンツポリシーも)への同意文を表示 |
| 透明性 | プレビューを表示し、**明示的な同意まで送信しない**。処理に数分かかる旨を伝える |
| 禁止 | 投稿内容にブランド名・ロゴ・透かし・宣伝リンクなどを**アプリ側で追加**すること。`client_secret` の第三者共有・オープンソースへの埋め込み |

## トークンとレート制限(✅)

| 項目 | 値 | 出典 |
|---|---|---|
| アクセストークン | **2時間** | [token management](https://developers.tiktok.com/doc/oauth-user-access-token-management) |
| リフレッシュトークン | **180日**。更新のたびに**新しい値に置き換える** | 同上 |
| レート制限 | **1分間のスライディングウィンドウ**。`/v2/user/info/`、`/v2/video/list/`、`/v2/video/query/` は各 600 | [rate limit](https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit) |
| 超過時 | HTTP 429、`rate_limit_exceeded` | 同上 |

投稿系エンドポイントのレート制限は今回の取得範囲では確認できていません(⚪ 要確認)。

## 制約(⚪ 要確認として残す項目)

- 直接投稿の機能は**審査(監査)を通るまで制限**があり、投稿の公開範囲が限定される場合がある。→ **✅ 未監査は `SELF_ONLY` に制限**(上記)。
- 動画の仕様は UI より厳しいことがある([02-media-specs](../06-tiktok/02-media-specs.md))。最大の長さは投稿者ごとに `creator_info` で返る(例のレスポンスでは 300秒 ✅。ただし例の値)。
- ユーザーの明示的な同意と、投稿内容の開示(ブランドコンテンツ・AI 生成の設定)が API でも必要。→ **✅ 同意と商業コンテンツの開示は必須**(上記)。AI 生成の設定の API 上の扱いは未確認(⚪)。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| 投稿が自分にしか見えない | 未監査アプリ | 仕様。監査を申請するか、公式アプリで投稿 |
| 6人目の利用者が投稿できない | 未監査は24時間5人まで | 監査を申請 |
| `PULL_FROM_URL` で失敗 | ドメイン未認証 | ドメイン・URL プレフィックスを認証、または `FILE_UPLOAD` |
| 2時間後に 401 | アクセストークンの期限切れ | リフレッシュ(新しいリフレッシュトークンを保存) |
| 429 | 1分間の上限超過 | 待って再試行([14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)) |

## 運用の指針

1. 個人利用の予約投稿は、公式の機能や公認ツールを優先。
2. 審査・利用規約を満たせるかを先に確認してから実装。
3. 自動化の規約リスクは [08-automation-and-tools](08-automation-and-tools.md)。

## 関連ページ / 次に読む

- [01-setup-and-posting](../06-tiktok/01-setup-and-posting.md) — アプリでの投稿
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[13-secrets-management](13-secrets-management.md)
- [08-automation-and-tools](08-automation-and-tools.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.tiktok.com/doc/content-posting-api-get-started | 2026-11-03 | 準備、投稿の流れ、未監査は非公開 |
| https://developers.tiktok.com/doc/content-sharing-guidelines | 2026-11-03 | 未監査5人/24時間、約15件/日、UI 要件、禁止事項 |
| https://developers.tiktok.com/doc/oauth-user-access-token-management | 2026-11-03 | トークン2時間・180日 |
| https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit | 2026-11-03 | 1分間のスライディングウィンドウ、429 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 一般的な理解(⚪ #32)で作成 |
| 2026-11-03 | 公式文書を直接取得して ✅ に更新(未監査の制限、上限、投稿の流れ、UI 要件、トークン、レート制限)。初心者向けに概要・用語・失敗例・出典を追加。既存の ⚪ の記述は残し、確認できた点を併記 |
