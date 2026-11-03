---
title: X API(v1.1 から v2 への移行)
platform: x
topic: api
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/x-api/migrate/overview
  - https://docs.x.com/x-api/media/introduction
  - https://devcommunity.x.com/t/important-update-legacy-x-api-basic-plans-are-moving-to-pay-per-use-ppu/266305
---

# X API(v1.1 から v2 への移行)

> **公式本文は未取得**です。検索要約(docs.x.com、X Developers の告知、二次資料)に基づく 🟡。価格・期日・エンドポイントの形は**開発者コンソールと docs.x.com で必ず確認**してください (#36)。

## 現状の整理

| 項目 | 内容 | 確度 |
|---|---|---|
| v1.1 の位置づけ | 旧世代。X の移行ガイドは「いずれ(eventually)非推奨にする」と説明し、v2 への移行を促す | 🟡 |
| 廃止日(sunset) | **確定した日付は確認できず**(検索結果に公式の廃止通知なし) | 🟡 |
| v2 の位置づけ | 現行世代。v1.1 の標準エンドポイントの置き換えと、Enterprise 向け機能を含む | 🟡 |
| 料金体系 | 2026年(皇紀2686年・令和8年)2月6日に、段階プランから**従量課金(pay-per-use、PPU)**が標準に | 🟡 |
| 単価の報告 | 投稿作成 $0.015/件、**リンク付き投稿は $0.20/件(2026年4月に追加)**、投稿読み取り $0.005/件とする資料 | 🟡 二次資料 |
| 旧 Basic | 2026年6月1日以降、自動で PPU へ移行。オプトアウトすると API アクセス終了 | 🟡 X Developers の告知 |
| 旧 Pro | 2026年9月1日以降、請求サイクル末で終了し PPU へ移行 | 🟡 開発者コミュニティの告知 |

## 移行の考え方

1. **v1.1 のまま使い続けない**: 廃止日が未確定でも、新機能・サポートは v2 に集中する。
2. **コストを再見積もり**: 従量課金は「投稿数」「読み取り数」に比例する。**リンクを含む投稿の単価が高い**ため、リンクの出し方(返信に置く、プロフィールに置く、note 側から誘導する)も設計対象。
3. **段階的に置き換え**: 読み取り → 投稿 → メディアの順に。

## 主なエンドポイントの対応(⚪ 移行ガイドに基づく一般的な対応)

| やりたいこと | v1.1 | v2 |
|---|---|---|
| 投稿する | `POST statuses/update` | `POST /2/tweets` |
| 投稿を削除 | `POST statuses/destroy/:id` | `DELETE /2/tweets/:id` |
| 自分のタイムライン | `GET statuses/user_timeline` | `GET /2/users/:id/tweets` |
| 検索(直近) | `GET search/tweets` | `GET /2/tweets/search/recent` |
| いいね | `POST favorites/create` | `POST /2/users/:id/likes` |
| リポスト | `POST statuses/retweet/:id` | `POST /2/users/:id/retweets` |
| 自分の情報 | `GET account/verify_credentials` | `GET /2/users/me` |
| フォロー | `POST friendships/create` | `POST /2/users/:id/following` |
| メディアのアップロード | `POST media/upload`(upload.x.com) | v2 のメディアアップロード(下記) |

## 認証

| 方式 | 用途 | 備考 |
|---|---|---|
| OAuth 2.0 Authorization Code with PKCE | ユーザー代行の投稿 | スコープ例: `tweet.read` `tweet.write` `users.read` `offline.access` `media.write` ⚪ |
| OAuth 1.0a(User Context) | 従来の方式。v2 でも一部使える | v1.1 からの移行を楽にする |
| Bearer Token(アプリ専用) | 公開情報の読み取り | 書き込み不可 |

## 応答形式の違い(移行時の落とし穴 ⚪)

- v2 は**既定で最小限のフィールド**しか返さない。`tweet.fields`、`user.fields`、`expansions` で明示的に要求する。
- ID は**文字列**として扱う(数値で扱うと桁あふれ)。
- 構造が「`data` / `includes` / `errors` / `meta`」に分かれる。
- ページネーションは `next_token`/`pagination_token`。

## メディアを含む投稿(🟡)

| 項目 | 値 |
|---|---|
| 上限(公式文書の要約) | 画像 5MB、GIF 15MB、動画 512MB(`media_category=amplify_video`) |
| 方式 | チャンクアップロード(画像/GIF/動画)を推奨。単純アップロードは画像のみ |
| エンドポイント | 旧: `https://upload.x.com/1.1/media/upload.json`。v2: `/2/media/upload` 系(**`initialize`/`append`/`finalize` の三段階とする資料と、`command=INIT` とする資料が不一致**) |
| スコープ | v2 は OAuth 2.0 の `media.write` が必要とする資料 |
| 投稿への添付 | メディアのアップロード後、`POST /2/tweets` の `media.media_ids` に ID を渡す |
| 推奨動画 | H.264 High Profile、30 または 60fps、1280×720(横)/ 720×1280(縦)/ 720×720(正方形) |

> 実装前に、docs.x.com のメディアアップロードのリファレンスで**現行のリクエスト形式**を確認 (#36)。

## alt text(画像説明)の付与(⚪ 要確認)

画像にメタデータとして付与する API がある(v1.1 の `media/metadata/create` に相当)。v2 での提供形態は公式で確認。

## レート制限

エンドポイントごとに15分ウィンドウなどで制限。応答ヘッダー(`x-rate-limit-limit`/`remaining`/`reset`)を見て調整([01-concepts-and-security](01-concepts-and-security.md))。

## 移行チェックリスト

- [ ] 開発者コンソールで現在のプラン(PPU か)と残高を確認
- [ ] v1.1 を呼んでいる箇所を洗い出す
- [ ] OAuth 2.0 PKCE へ移行(または OAuth 1.0a を継続)
- [ ] 投稿・削除・メディアを v2 に置換
- [ ] レスポンスのフィールド指定を追加
- [ ] リンク付き投稿の単価を踏まえた運用に変更
- [ ] 自動化の規約を再確認([08-automation-and-tools](08-automation-and-tools.md))
- [ ] テストアカウントで確認→本番

## コード例(概念。動作は未検証。鍵は環境変数から読む)

```python
import os, requests
token = os.environ["X_USER_ACCESS_TOKEN"]  # OAuth 2.0 のユーザートークン
r = requests.post(
    "https://api.x.com/2/tweets",
    headers={"Authorization": f"Bearer {token}"},
    json={"text": "テスト投稿"},
    timeout=30,
)
r.raise_for_status()
print(r.json())
```

鍵やトークンを**コードやコミットに書かない**。
