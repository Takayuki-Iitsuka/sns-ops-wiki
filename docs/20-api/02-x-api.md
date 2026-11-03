---
title: X API(v1.1 から v2 への移行)
platform: x
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://docs.x.com/x-api/migrate/overview.md
  - https://docs.x.com/x-api/migrate/x-api-endpoint-map.md
  - https://docs.x.com/x-api/getting-started/pricing.md
  - https://docs.x.com/x-api/fundamentals/rate-limits.md
  - https://docs.x.com/x-api/media/introduction.md
  - https://docs.x.com/x-api/media/quickstart/best-practices.md
  - https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md
  - https://docs.x.com/changelog.md
---

# X API(v1.1 から v2 への移行)

> **このページで分かること**: X API の現状(v2 が主、従量課金)、料金表、2026年(皇紀2686年・令和8年)の主な変更、v1.1 から v2 への置き換え、認証方式。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)。はじめて登録する人は [16-x-api-getting-started](16-x-api-getting-started.md)、画像・動画とレート制限は [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md)

> 2026年(皇紀2686年・令和8年)11月3日に **docs.x.com の公式 Markdown を直接取得**して確認しました(✅)。ただし価格などは頻繁に変わるため、実運用前に Developer Console(https://console.x.com)で現在値を確認してください。末尾の「公式で確認できなかった点」に注意。

## 概要

X API は、X(旧 Twitter)をプログラムから操作する公式の窓口です。2026年(皇紀2686年・令和8年)の時点で、**v2 が主たる API** で、料金は**使った分だけ払う従量課金**です。古い v1.1 を使っているプログラムは、v2 へ置き換える必要があります。

このページは「X API の全体像と料金・移行」をまとめます。初めて使う人の手順は [16-x-api-getting-started](16-x-api-getting-started.md) にあります。

## 用語

| 用語 | 意味 |
|---|---|
| v1.1 / v2 | API のバージョン(世代)。v2 が新しく、主に使うもの |
| pay-per-usage(従量課金) | 使った回数・件数に応じて払う料金体系 |
| resource(資源) | 投稿・ユーザーなど、API が返すデータ1件 |
| Owned Reads(自分のデータの読み取り) | 自分のアカウントのデータを読むときの安い単価 |
| endpoint map(エンドポイントの対応表) | v1.1 の URL が v2 のどれに当たるかの表 |
| summoned(呼び出された) | 相手が @メンションや引用であなたを呼んだ状態 |
| self-serve(自助サービス) | Enterprise 以外の、自分で申し込んで使うプラン |
| Enterprise(エンタープライズ) | 大口向けの個別契約プラン |

## 1. 現状(✅)

| 項目 | 内容 |
|---|---|
| v2 の位置づけ | **X API v2 が primary(主たる)API**。投資と革新は v2 に集中 |
| v1.1 の扱い | 「**いずれ(eventually)非推奨にするつもり**」。**廃止日は公式文書に記載なし** |
| 料金体系 | **pay-per-usage(従量課金)**。サブスクなし、クレジットを前払い購入し、使った分が引かれる |
| 管理画面 | Developer Console(https://console.x.com)。2026年(皇紀2686年・令和8年)2月6日に従量課金とともに公開 |
| SDK | 公式の XDK(Python と TypeScript)、ローカルの Playground、MCP サーバー |
| 無料クレジット | **初めての支払いカードの保存と初回のクレジット購入**で **$20**、初回の自動チャージに対し最大 **$50** のマッチ(合計最大 $70)。付与から3か月で失効 |

## 2. 料金表(✅ 公式の料金ページ。2026年11月3日取得)

**読み取り**(返された資源1件あたり)

| 資源 | 単価 |
|---|---|
| Posts: Read | $0.005 |
| User: Read | $0.010 |
| DM Event: Read | $0.010 |
| Following/Followers: Read | $0.010 |
| List / Space / Community / Note: Read | $0.005 |
| Like / Mute / Block: Read | $0.001 |

- **Owned Reads(自分のデータの読み取り): $0.001/件**(2026年4月20日から)。対象は自分の `GET /2/users/{id}/tweets`、`/mentions`、`/liked_tweets`、`/bookmarks`、`/followers`、`/following`、`/blocking`、`/muting`、`/owned_lists`、`/followed_lists`、`/list_memberships`、`/pinned_lists`。**自分のアカウントの分析や個人ダッシュボードが安く作れる**。
- 同じ資源は **24時間(UTC)内の再取得は課金されない**(重複排除。保証ではない)。
- 従量課金プランの **Post 読み取りは月300万件が上限**(それ以上は Enterprise)。

**書き込み・操作**(1リクエストあたり)

| 操作 | 単価 |
|---|---|
| **Post: Create** | **$0.015** |
| **Post: Create(URL を含む)** | **$0.200** |
| Post: Create(summoned = 呼び出されて返信) | $0.010 |
| Media Metadata(alt text など) | $0.005 |
| DM Interaction / User Interaction: Create | $0.015 |
| Interaction: Delete | $0.010 |
| Content: Manage / List: Manage / Bookmark | $0.005 |
| Counts: Recent / All | $0.005 / $0.010 |

→ **URL を含む投稿は単価が約13倍**($0.200 vs $0.015)。自動投稿ではリンクを本文に入れず、**返信やプロフィール・note 側から誘導する**設計が費用面で有利。ただし運用上の優位性はサービスの方針で変わるため、費用と効果を測る。

> 価格は変更されうる。公式の料金ページでも「現在の価格は Developer Console を参照」とされている。

## 3. 2026年の主な変更(✅ changelog)

| 日付 | 変更 | 影響 |
|---|---|---|
| 2月6日 | 従量課金を正式公開 | 旧 Basic/Pro は「引き続き利用可能、従量課金へ切替可」と告知(その後の移行日は下記) |
| 2月23日 | **LLM 生成スパム対策**: `POST /2/tweets` による**返信は、元の投稿者があなたのアカウントを「呼び出した」場合(@メンションまたは引用)にのみ可能**。@メンションや引用の自動化にも追加の制限 | **自動リプライ bot は原則成立しない**(Enterprise は対象外) |
| 3月〜 | X Activity API の整備(`post.create`、`dm.*`、`follow.*` ほか)、旧 Account Activity の一部非推奨 | リアルタイム通知 |
| 4月16日 | Owned Reads $0.001、Post 作成 $0.015、URL 付き $0.20。**Following・Likes・Quote Post は API から自助サービス(self-serve)の全プランで削除** | 自動いいね・自動フォローは不可 |
| 5月4日 | 検索を新インデックスへ。キーワード検索で**リポストが返らなくなった** | 検索ロジックの調整 |
| 6月3日 | **`paid_partnership` フィールド**: 投稿作成時に `"paid_partnership": true` で有料プロモーションのラベルを付与。読み取りは `tweet.fields=paid_partnership` | **ステマ規制への対応に使える**([legal-compliance](../01-common/legal-compliance.md)) |
| 6月11日 | Articles の下書き・公開エンドポイント | 長文記事 |
| 9月1日 | メディアのサイズ・長さの制限を文書化。**v2 の新メディアアップロードパス**に統一 | 下記 §6 |
| 9月21日 | **OAuth 1.0a のユーザートークンを OAuth 2.0 に交換**(`grant_type=urn:ietf:params:oauth:grant-type:token-exchange`、`POST /2/oauth2/token`)。再認可の画面なし | 既存ユーザーの移行が容易 |
| 10月1日 | 返信モデレーションの guide が Grok と X Activity API を使う形に | 自動非表示の設計 |
| 10月2日 | 無料クレジットの付与(§1) | — |

## 4. 旧プラン(Basic / Pro)の移行日(🟡 公式文書ではなく X Developers の告知経由)

- 旧 **Basic は 2026年6月1日以降**、旧 **Pro は 2026年9月1日以降**に従量課金へ自動移行するとの告知がある(検索結果で確認。X の開発者コミュニティ投稿)。**公式ドキュメント(docs.x.com)には移行日の記載を確認できていない**。
- 旧プランの契約がある場合は、Developer Console の表示と請求を直接確認する(#36)。

## 5. v1.1 から v2 への対応表(✅ 公式のエンドポイントマップ)

| やりたいこと | v1.1 | v2 | 備考 |
|---|---|---|---|
| 投稿の取得 | `GET statuses/show` / `statuses/lookup` | Posts lookup(`GET /2/tweets`、`/2/tweets/:id`) | |
| **投稿する** | `POST statuses/update` | **Manage Posts(`POST /2/tweets`)** | |
| 削除 | `POST statuses/destroy/:id` | `DELETE /2/tweets/:id` | |
| タイムライン | `GET statuses/user_timeline` ほか | Timelines(`GET /2/users/:id/tweets` ほか) | 自分の分は Owned Reads |
| 検索 | `GET search/tweets` | Search Tweets(Recent / Full-archive) | 30日検索は [No Replacement Planned] |
| ストリーム | `GET statuses/filter` / `sample` | Filtered stream / Volume stream | |
| リポスト | `POST statuses/retweet/:id` ほか | Manage Retweets | |
| いいね | `POST favorites/create` ほか | Manage Likes | **API からの いいね・フォロー・引用は self-serve で削除済み(4月16日)** |
| 返信の非表示 | — | Hide replies | |
| メディア | `POST media/upload`(upload.twitter.com) | **`POST /2/media/upload/...`**(下記 §6) | |
| alt text | `POST media/metadata/create` | Create Media Metadata(`alt_text` は **最大1,000字** ✅) | $0.005/リクエスト |

## 6. メディアを含む投稿(✅ 要約。詳細は [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md))

- 流れ: `POST /2/media/upload/initialize` → `append` → `finalize` →(必要なら状態確認)→ `POST /2/tweets` の `media.media_ids` に ID を渡す。旧方式の `command=INIT/APPEND/FINALIZE` は使わない(9月1日に切替 ✅)。
- 主な上限: 画像 **5MB**、GIF **15MB**、動画は通常アカウント **20分・8GB**、Premium/認証済み **125分・16GB**。投稿には写真4枚まで、または GIF 1つ、または動画1つ(✅)。
- 上限は**認証したユーザーのアカウント種別**と `media_category` で決まり、API プランでは決まらない(✅)。

## 7. レート制限(✅ 要約。詳細は [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md))

- `POST /2/tweets` は App あたり 10,000/24時間、**User あたり 100/15分**。`GET /2/tweets/search/recent` は App 450/15分・User 300/15分(✅)。
- 応答ヘッダー `x-rate-limit-limit` / `remaining` / `reset` を見る。429 は待機して再試行([14-errors-and-troubleshooting](14-errors-and-troubleshooting.md))。

## 8. 認証(✅)

| 方式 | 用途 |
|---|---|
| OAuth 2.0 Authorization Code Flow with PKCE | ユーザー代行(推奨。スコープで権限を絞れる) |
| OAuth 1.0a User Context | 従来方式。**9月21日から OAuth 2.0 へのトークン交換が可能** |
| App-only(Bearer Token) | 公開情報の読み取り |
| Basic 認証 | Enterprise API |

## 9. 移行チェックリスト

- [ ] Developer Console で現在のプランと残高、請求を確認
- [ ] 自動チャージとスペンドの上限を設定(想定外の課金を防ぐ)
- [ ] v1.1 を呼んでいる箇所を洗い出し、[エンドポイントマップ](https://docs.x.com/x-api/migrate/x-api-endpoint-map.md) で置換
- [ ] **自動いいね・自動フォロー・自動引用・自動リプライは API では使えない**前提に設計変更
- [ ] OAuth 1.0a のトークンは**トークン交換**で OAuth 2.0 へ
- [ ] メディア投稿を v2 の `initialize/append/finalize` に置換
- [ ] 取得項目を `tweet.fields` / `expansions` で明示(v2 は既定で最小限しか返さない)
- [ ] ID は文字列で扱う
- [ ] `paid_partnership` による PR 表示の運用
- [ ] テストは Playground(ローカルのエミュレータ)で
- [ ] 自動化の規約を再確認([08-automation-and-tools](08-automation-and-tools.md))

## 10. コード例(概念。動作は未検証。トークンは環境変数から読む)

```python
import os, requests

token = os.environ["X_USER_ACCESS_TOKEN"]  # OAuth 2.0 のユーザートークン(tweet.write 必須)
r = requests.post(
    "https://api.x.com/2/tweets",
    headers={"Authorization": f"Bearer {token}"},
    json={"text": "テスト投稿"},   # URL を含めると単価が上がる
    timeout=30,
)
r.raise_for_status()
print(r.json())
```

トークンやキーを**コードやコミットに書かない**。

## 11. 公式で確認できなかった点(#36)

- 旧 Basic/Pro の**自動移行日**(§4)。
- v1.1 の**廃止日**(公式文書にはない)。
- ~~OAuth 2.0 の個別スコープの完全な一覧~~ → 2026-11-03 に公式の認可コードのページで一覧を確認(✅ [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md))。
- 日本の税務・請求書の扱い(Developer Console の請求画面で確認)。

## 12. 関連ページ / 次に読む

- [16-x-api-getting-started](16-x-api-getting-started.md) — 登録から最初の投稿まで(初心者向け)
- [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md) — メディア投稿とレート制限の詳細
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)
- [01-x-and-grok](../40-pricing/01-x-and-grok.md)、[06-cost-planning](../40-pricing/06-cost-planning.md) — 料金・見積もり

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/migrate/overview.md | 2026-11-03 | v2 が primary、v1.1 の扱い |
| https://docs.x.com/x-api/migrate/x-api-endpoint-map.md | 2026-11-03 | v1.1 → v2 の対応表 |
| https://docs.x.com/x-api/getting-started/pricing.md | 2026-11-03 | 料金表、無料クレジット(2026-11-03 に再取得) |
| https://docs.x.com/x-api/fundamentals/rate-limits.md | 2026-11-03 | レート制限 |
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | メディアの上限 |
| https://docs.x.com/x-api/media/quickstart/best-practices.md | 2026-11-03 | 動画の推奨 |
| https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md | 2026-11-03 | 分割アップロード |
| https://docs.x.com/changelog.md | 2026-11-03 | 2026年の変更 |
| https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md | 2026-11-03 | OAuth 2.0 のスコープ(§11 の一部を解消) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | docs.x.com の公式 Markdown を取得して ✅ に更新(既存) |
| 2026-11-03 | 初心者向けに加筆(このページで分かること・概要・用語・関連ページ・出典を追加)。§6・§7 の詳細を [17-x-api-media-and-rate-limits](17-x-api-media-and-rate-limits.md) へ移設し要約を残した。登録手順は [16-x-api-getting-started](16-x-api-getting-started.md) を新設。無料クレジット $20 の条件を公式の料金ページの現行表記(カード保存**と**初回購入)に修正 |
