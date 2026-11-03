---
title: 他のツールとの連携
platform: common
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md
  - https://docs.x.com/tools/mcp
---

# 他のツールとの連携

> **このページで分かること**: SNS と他のツール(予約ツール・ノーコード・表計算・チャット・AI)をつなぐ方法、費用の見方、安全な連携の原則、選び方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [10-benefits-of-api](10-benefits-of-api.md)

## 概要

SNS 運用は、**複数のツールを「つなぐ」**ほど効率が上がります。ただし連携は**費用の二重化・規約・セキュリティ**を伴います。

> X 側の費用・制約は ✅(docs.x.com)。ノーコードツールの料金は 🟡([05-ai-and-creative-tools](../40-pricing/05-ai-and-creative-tools.md))。

初心者は、**プログラムを書かない連携**(サービス内蔵の連携、予約ツール、ノーコード)から始めるのが安全です。どの方法でも、裏側では各サービスの API と OAuth(パスワードを渡さない許可の仕組み)が使われています。

## 用語

| 用語 | 意味 |
|---|---|
| integration(連携) | 2つ以上のツールをつないでデータや操作を受け渡すこと |
| trigger / action(トリガー / アクション) | 「〜が起きたら」/「〜をする」。ノーコードの基本の組み立て |
| RSS(アールエスエス) | サイトの新着情報を機械が読める形で配る仕組み |
| webhook(ウェブフック) | 出来事をすぐに相手の URL へ知らせる仕組み |
| polling(ポーリング) | 一定間隔で「新着はある?」と確認しに行く方式 |
| MCP(Model Context Protocol) | AI アシスタントが外部ツールを呼び出すための共通の仕組み |
| OAuth 連携 | パスワードを渡さず、権限(スコープ)を絞って許可する連携 |
| revoke(連携の解除) | 許可した連携を取り消すこと |

## 1. 連携の種類

| 種類 | 例 | 特徴 |
|---|---|---|
| **A. サービス内蔵の連携** | Instagram↔Facebook のクロス投稿、Threads↔Instagram、note の SNS 連携(自動ポスト ⚪) | 追加費用なし。設定のみ |
| **B. 予約・管理ツール** | Buffer、Later、Hootsuite、Metricool、Publer | 複数サービスを一元管理 |
| **C. ノーコード自動化** | Zapier、Make、IFTTT | トリガー→アクション |
| **D. 表計算・BI** | Google スプレッドシート(Apps Script)、Looker Studio、Notion、Airtable | 台帳・ダッシュボード |
| **E. デザイン** | Canva、Adobe Express、CapCut | 比率別テンプレ。**note の Canva 連携は 2025年(皇紀2685年・令和7年)12月1日に終了**(🟡) |
| **F. 通知・チーム** | Slack、Discord(webhook)、メール | 新着コメントなどの通知 |
| **G. 計測** | GA4、UTM パラメータ | 流入の測定([link-in-bio-and-utm](../01-common/link-in-bio-and-utm.md)) |
| **H. AI 連携** | X MCP、Docs MCP(✅)、AI アシスタントの MCP/コネクタ、GitHub Actions | 下書き・分類・要約 |
| **I. 自作スクリプト** | 公式 API+GitHub Actions など | 柔軟、保守が必要 |

## 2. よく使う連携パターン

| やりたいこと | 組み立て | 主な注意 |
|---|---|---|
| **note の新着記事を X に告知** | note の RSS → ノーコード → X 投稿 | **X API は従量課金**。URL 付き投稿は $0.200 ✅。ツールが API 枠を含むか確認 |
| **YouTube 新着を通知** | YouTube の RSS/API → Slack/Discord/LINE | 自分のチームへの通知なら安全 |
| **フォームの回答を台帳へ** | Google フォーム → スプレッドシート → Slack | 個人情報の扱い |
| **週次の成績を集計** | X(Owned Reads)・Instagram・YouTube の取得 → スプレッドシート | 読み取りのみ。トークンを最小権限で |
| **画像の自動書き出し** | デザイン→比率別の書き出し(export-presets)→ 命名規則 | 実ファイルはリポジトリに入れない |
| **投稿計画をカレンダーに** | スプレッドシート → Google カレンダー | 公開前の投稿案を public リポジトリに置かない |
| **返信候補の下書き** | コメント取得 → AI で候補 → **人が承認** | **自動送信は避ける** |
| **投稿前の検査** | 画像・テキストを検査スクリプトで検証 | 本リポジトリの `scripts/check_wiki.py` の考え方 |
| **バックアップ** | 公式のデータ書き出し+API の定期取得 | [data-backup](../01-common/data-backup-and-portability.md) |

## 3. 連携の費用の見方(重要)

```
合計費用 = ツール料金 + 各サービスの API 費用 + 保守の手間
```

- **X 連携は特に注意**: ノーコードの料金が安くても、**X API の従量課金が別にかかる**(ツール側が API を肩代わりするかはツールの説明を確認)。
- 無料プランは**回数・ステップの制限**がある(IFTTT は2アプレット、Zapier/Make も制限 🟡)。
- 多段のワークフローは**ステップ数だけ課金**されるツールがある(Zapier は各ステップが1タスク 🟡)。

## 4. 連携の設計原則

1. **一方向から始める**(取得→集計→通知)。双方向・自動投稿は後。
2. **承認ゲート**: 公開・返信・DM は人が確認([08-automation-and-tools](08-automation-and-tools.md))。
3. **最小権限**: 読み取りのみで足りるなら書き込み権限を付けない。
4. **鍵は連携先に直接渡さない**。公式の OAuth 連携を使い、不要になったら**連携を解除**。
5. **失敗の通知**: エラーで止まったことに気づける仕組み。
6. **ログ**(何をいつ実行したか。トークンは記録しない)。
7. **冪等性**: 二重投稿を防ぐ(内部 ID と投稿 ID の対応表)。
8. **停止ボタン**: 緊急時にすべての自動化を止められるようにする。
9. **規約確認**: 各サービスの自動化ルール(X の自動返信制限 ✅、Instagram の公開上限 ✅)。
10. **データの置き場所**: 投稿案・顧客情報は **private** に。

## 5. 選定基準

| 基準 | 確認すること |
|---|---|
| 連携方法 | 公式 API+OAuth か(パスワード入力を求めない) |
| 権限 | 求めるスコープが最小か |
| 費用 | 月額+従量(特に X) |
| 制限 | 回数・ステップ・ポーリング間隔(IFTTT は約60分 🟡) |
| 停止時の影響 | サービス終了時のデータ持ち出し |
| 日本語・時間帯 | 日本語・日本時間(JST)に対応しているか |
| 対応サービス | 例: **Later は X と Bluesky に非対応**とする記載 🟡 |

## 6. AI 連携(✅ X の公式ツールを含む)

| 項目 | 内容 |
|---|---|
| **X MCP** | ホスト型。200以上の X API エンドポイントを AI からツールとして呼べる(✅ docs.x.com/tools/mcp) |
| **Docs MCP** | AI がドキュメントを検索・読み取り |
| **llms.txt / llms-full.txt / skill.md** | AI 向けのドキュメント索引・要約 ✅ |
| **OpenAPI 仕様** | `https://api.x.com/2/openapi.json` ✅ |
| **返信モデレーション** | X Activity API → Grok(xAI)で分類 → Hide Replies ✅ |
| **GitHub Actions** | 検査・定期取得。鍵は Secrets に |

**注意**: AI にトークンを渡すと、AI が意図しない操作をするリスクがある。**読み取り専用のトークン**から試し、書き込みは承認付きに。[ai-rules-by-platform](../01-common/ai-rules-by-platform.md)。

## 7. 連携の落とし穴

- **ステップが増えるほど障害点が増える**。
- 自動投稿で**同じ内容の連投**(スパム扱い)。
- **ツール側のアカウント乗っ取り**(連携先が侵害されると SNS も影響)。
- **仕様変更**である日突然止まる(X のメディアアップロードの変更 ✅ など)。
- **個人情報**がツール経由で第三者に渡る。

## 8. 段階的な導入

1. 公式機能+スプレッドシート(手動入力)。
2. 通知の自動化(Slack/Discord)。
3. 取得の自動化(読み取りのみ)。
4. 予約投稿(承認付き)。
5. クロス投稿・AI 下書き。

構成の設計は [09-architecture-patterns](09-architecture-patterns.md)。

## 9. 手順: 連携を安全に始める(⚪ 一般的な手順。画面名はサービスごとに異なる)

1. **目的を1つに決める**(例: 「note の新着記事を X で告知」)。
2. ツールの説明で、**公式の OAuth 連携**か(SNS のパスワードを入力させないか)を確認する。
3. 許可画面で**求められる権限(スコープ)**を読む。X なら `tweet.write` は投稿、`dm.read` は DM の読み取り(✅ [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md))。目的に対して多すぎるなら使わない。
4. **費用**を計算する: ツール料金+ API 費用(X の URL 付き投稿は1回 $0.200 ✅)。
5. まず**自分だけに見える形**(下書き・通知)で試す。
6. 本番にしたら、**失敗通知**と**停止方法**を確認する。
7. 使わなくなったら、SNS 側の設定画面(「連携しているアプリ」など ⚪)から**連携を解除**する。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 無料プランの回数を超えて連携が止まった | 回数・ステップの上限を確認し、頻度を下げる |
| RSS → X の自動告知で URL 付き投稿の費用がかさんだ | 本文に URL を入れない設計、または手動で告知 |
| 退職・担当交代後も、前任者の連携が残っていた | 定期的に連携アプリの一覧を棚卸しし、不要なものを解除 |
| AI にトークンを渡したら、意図しない操作をした | 読み取り専用のトークンから試し、書き込みは承認付きに |

## 関連ページ / 次に読む

- [09-architecture-patterns](09-architecture-patterns.md) — 構成の設計
- [08-automation-and-tools](08-automation-and-tools.md) — 規約と自動化の段階
- [13-secrets-management](13-secrets-management.md) — 鍵を連携先に渡すときの注意
- [tools](../01-common/tools.md)、[05-ai-and-creative-tools](../40-pricing/05-ai-and-creative-tools.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | X API の単価(URL 付き投稿 $0.200、Owned Reads) |
| https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md | 2026-11-03 | X のスコープ一覧 |
| https://docs.x.com/tools/mcp | 2026-11-03 | X MCP(本文の §6 で既出の出典を明記) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(このページで分かること・概要・用語・連携を安全に始める手順・よくある失敗・関連ページ・出典を追加。既存の種類・パターン・費用・原則・選定基準・AI 連携は維持) |
