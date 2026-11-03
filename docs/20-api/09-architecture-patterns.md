---
title: 投稿パイプラインの設計
platform: common
topic: api
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/x-api/fundamentals/rate-limits.md
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.google.com/youtube/v3/determine_quota_cost
---

# 投稿パイプラインの設計

> **このページで分かること**: 複数の SNS へ安全に投稿する仕組み(パイプライン)の全体像、設計の要点、投稿データの書き方、段階的な導入。
>
> **対象**: 中級者(初心者は「概要」と「用語」だけでも可)  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)、[08-automation-and-tools](08-automation-and-tools.md)

## 概要

複数サービスへ、**同じ元データから形式を変えて投稿**するための設計案です。

**パイプライン**(pipeline、流れ作業の仕組み)は、工場のベルトコンベアに似ています。原稿 → 検査 → 画像の書き出し → 承認 → 投稿 → 記録、と順に流れ、どこかで問題があればそこで止まります。

初心者がいきなり全部を作る必要はありません。下の「段階的な導入」の1〜2(手動+チェックリスト、公式の予約機能)から始めてください。

## 用語

| 用語 | 意味 |
|---|---|
| pipeline(パイプライン) | 処理を順につないだ流れ |
| adapter(アダプタ) | サービスごとの違い(文字数・画像形式など)を吸収する部品 |
| queue(キュー、待ち行列) | 投稿を順番待ちさせる場所 |
| dry run(ドライラン) | 実際には投稿せず、送る内容だけを表示する試運転 |
| idempotency(冪等性) | 同じ処理を何度実行しても結果が1回分になる性質。二重投稿の防止 |
| backoff(バックオフ) | 失敗後に待ち時間を空けて再試行すること |
| YAML(ヤムル) | 人が読みやすい設定ファイルの書き方 |
| front matter(フロントマター) | Markdown の先頭に YAML で書く付帯情報 |

## 全体像

```
[企画・原稿(Markdown, private)]
        │ 検証(文字数・画像仕様・必須項目)
        ▼
[メディア生成] 画像を比率別に書き出し(export-presets)
        │
        ▼
[投稿キュー] サービス別アダプタ ─ 人の承認ゲート
   ├─ X          (v2: POST /2/tweets + メディア)
   ├─ Instagram  (JPEG・公開URL → media → media_publish)
   ├─ Threads    (container → threads_publish)
   ├─ YouTube    (手動推奨 / 限定用途で API)
   └─ Bluesky    (createRecord + uploadBlob)
        │
        ▼
[ログ・ID 保存] 投稿 ID・日時・結果(秘密は保存しない)
        │
        ▼
[計測] インサイト取得 → 週次レビュー
```

## 設計の要点

1. **元データはサービス非依存**: 本文、画像、alt text、タグ、広告表記の有無、公開日時を YAML front matter で保持。
2. **アダプタ層**: サービスごとの制約(文字数、画像形式、比率、タグ数)をコードで吸収。仕様変更時はアダプタだけ直す。
3. **検証を先に**: 投稿前に仕様を機械的に検査(例: Instagram API なら JPEG・8MB 以内)。
4. **冪等性**: 同じ投稿を二重に出さない。内部 ID と、サービス側 ID の対応表を持つ。
5. **ドライラン**: 実際に投稿せず、送信内容を表示するモード。
6. **人の承認**: 公開前に「承認済み」フラグが必要。
7. **リトライとバックオフ**: 429/5xx のみ。上限回数を決める。
8. **失敗の通知**: メール等。
9. **レート・クォータの余裕**: 上限の 50% 以内で運用。
10. **鍵の分離**: サービスごとに最小権限のトークン。

### サービスごとの「アダプタ」で吸収する違い(✅ 各ページの公式値)

| サービス | 投稿の形 | 吸収すべき制約の例 | 詳細 |
|---|---|---|---|
| X | `POST /2/tweets` 1回(メディアは事前アップロード) | 画像 5MB、写真4枚まで、User あたり 100回/15分、URL 付きは高単価 | [02](02-x-api.md)、[17](17-x-api-media-and-rate-limits.md) |
| Instagram | コンテナ作成 → 公開 | JPEG のみ・8MB・4:5〜1.91:1、公開 URL の素材、公開上限 | [03](03-instagram-graph-api.md) |
| Threads | コンテナ作成 → 約30秒待つ → 公開 | テキスト500字、リンク5個以下、トピックタグ1つ | [04](04-threads-api.md) |
| YouTube | `videos.insert` | 専用枠で100回/日、OAuth 必須 | [05](05-youtube-data-api.md) |

## 投稿データの例(YAML)

```yaml
id: 2026-11-10-intro
publish_at: 2026-11-10T19:00:00+09:00
approved: true
ad_disclosure: false
text:
  x: "短文…"
  instagram: "キャプション…"
media:
  - file: intro_4x5.jpg   # export-presets の Instagram 縦長
    alt: "週間計画のカレンダー。月曜は告知、水曜は記事、金曜は画像と書かれている"
tags: ["SNS運用"]
```

### 具体例: 投稿前の検査(Python、概念)

API を呼ぶ前に、手元で仕様を確認するだけでも事故が大きく減ります。

```python
from pathlib import Path

LIMITS = {
    "x":        {"max_bytes": 5 * 1024 * 1024, "formats": {".jpg", ".jpeg", ".png", ".gif", ".webp"}},
    "instagram": {"max_bytes": 8 * 1024 * 1024, "formats": {".jpg", ".jpeg"}},
    "threads":  {"max_bytes": 8 * 1024 * 1024, "formats": {".jpg", ".jpeg", ".png"}},
}

def check_image(service, path):
    p = Path(path)
    rule = LIMITS[service]
    problems = []
    if p.suffix.lower() not in rule["formats"]:
        problems.append(f"{service}: 形式 {p.suffix} は不可")
    if p.stat().st_size > rule["max_bytes"]:
        problems.append(f"{service}: 容量オーバー")
    return problems

print(check_image("instagram", "intro_4x5.jpg") or "OK")
```

値は各ページの公式値(✅)に合わせています。仕様が変わったら、この表(アダプタ)だけを直します。

## 段階的な導入

1. 手動運用+この wiki のチェックリスト。
2. 公式の予約機能。
3. 検証スクリプト(`scripts/check_wiki.py` のように)を投稿データにも適用。
4. 分析取得の自動化(読み取りのみ)。
5. 必要なサービスだけ投稿 API(承認ゲート付き)。

## 避けること

- 完全自動で、承認なしに投稿し続ける構成。
- 1つのトークンですべてのサービスを扱うこと(そもそも不可)。
- public リポジトリに未公開の投稿案・鍵を置くこと。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| タイムアウト後の再送で二重投稿 | 内部 ID とサービス側の投稿 ID を記録し、再送前に確認 |
| 1つのサービスの失敗で全体が止まった | サービスごとに独立して処理し、失敗だけを通知 |
| 仕様変更で全部のコードを直す羽目に | 制約をアダプタ(設定表)にまとめる |
| 承認前の投稿が公開された | `approved: true` がないものは送らない、をコードで強制 |

## 関連ページ / 次に読む

- [08-automation-and-tools](08-automation-and-tools.md)、[11-tool-integrations](11-tool-integrations.md)
- [14-errors-and-troubleshooting](14-errors-and-troubleshooting.md) — 再試行の実装
- [export-presets](../01-common/export-presets.md) — 比率別の書き出し

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/x-api/fundamentals/rate-limits.md | 2026-11-03 | X のレート制限 |
| https://developers.facebook.com/documentation/instagram-platform/content-publishing.md | 2026-11-03 | Instagram の公開の流れ・上限 |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | Threads の公開の流れ、30秒の待機 |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | YouTube の専用枠 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(このページで分かること・概要・用語・サービス別のアダプタ表・投稿前検査のコード例・よくある失敗・関連ページ・出典を追加。既存の全体像・要点・YAML 例・導入段階は維持) |
