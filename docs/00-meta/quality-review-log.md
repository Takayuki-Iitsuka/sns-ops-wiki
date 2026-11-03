---
title: 品質レビューの記録
platform: common
topic: meta
last_verified: 2026-11-03
confidence: ⚪
---

# 品質レビューの記録

「作る → 検査する → 抜けを探す → 直す」を繰り返した記録です。

## レビュー観点(毎回)

1. **要件の網羅**: 投稿ルート、収益化基準、ノウハウ、コメント、ハッシュタグ、画像の説明文、画像・動画の形式・サイズ・比率、API
2. **事実の根拠**: 数値に確度ラベルと出典があるか(推測で埋めていないか)
3. **整合**: 内部リンク、用語・表記、年の換算、番号の参照(#N)
4. **範囲**: SNS 運用に限る(特定の題材を含まない)
5. **安全**: 秘密情報、権利、配慮

## 2026年(皇紀2686年・令和8年)11月3日

### パス1〜4: 初期構成と拡充
- X・Instagram・note、共通、テーマ、戦略、スクリプトを作成(56→93ファイル)。
- 検査: リンク切れ・front matter・年の換算 0件。

### パス5: 方針転換(SNS 専用化)
- 題材別の層(テーマ運用、アカウント別の方針)を削除し、汎用の企画・ブランド・慎重な話題のページに置き換えた。
- 削除前の内容は git 履歴(コミット 783b615)に残る。別の wiki へ移す場合はそこから取り出せる。

### パス6: 範囲の拡大
- 追加: YouTube、TikTok、Threads、Facebook、Bluesky、LINE、Twitch、収益化サービス(5ページ)、API(10ページ)。
- 追加: 画像・動画の横断比較、書き出しプリセット。
- 検索で得た二次資料を要検証リスト(#29〜#43)に登録。**公式本文は引き続き未取得**。

### パス7: 公式文書の直接取得(ネットワーク許可後)
- `docs.x.com`(`.md` 付き URL)、`developers.facebook.com`(`.md`)、`support.google.com`(YouTube)、LINE、消費者庁の本文を取得し、✅ に更新。
- **訂正**: X の動画上限は「2分20秒・512MB」ではなく、Post は**20分・8GB(Premium 125分・16GB)**。「2分20秒・512MB」は DM 動画。YouTube のサムネイル「2MB 未満」は**モバイルのみ**で、パソコンは 50MB。Instagram リールの API 上限は**15分・300MB**。
- **新事実**: X は 2026年に Following・Likes・Quote の API を self-serve から削除、自動リプライは「呼び出された場合」のみ、URL 付き投稿は $0.20、`paid_partnership` フィールド追加。Instagram API は `alt_text`・`is_ai_generated`・パートナーシップ表示に対応。公開上限は公式ページ内で 100 と 50 が併記。
- 取得できなかった: `help.x.com`・`www.help-note.com`(Cloudflare の bot 確認)、`help.instagram.com`(JS 描画)。回避は行っていない。

### 要件の突合せ

| 要件 | 状況 |
|---|---|
| 投稿ルート | 各サービスの投稿ページ、posting-workflow ✓ |
| 収益化基準 | 各サービスの monetization、比較、戦略 ✓(条件は未確認) |
| ノウハウ | 各 tips、writing-guide、content-planning ✓ |
| コメント | 各 engagement、共通、crisis-response ✓ |
| ハッシュタグ | 各 text、共通 hashtags ✓ |
| 画像の説明文 | 各 alt、共通 alt-text ✓(note は機能未確認 #16) |
| 画像・動画の形式・サイズ・比率 | 比較表2本、書き出しプリセット、各 media-specs ✓(公式未確認が残る) |
| API(X の v1.1→v2 を含む) | 20-api ✓(価格・期日・エンドポイントは未確認 #36〜#38) |
| 収益化できる追加サービス | YouTube、TikTok、Facebook、Twitch、創作支援系 ✓ |

### 残課題(次パスへ)

- 公式の裏取りは進んだが、**X アプリの仕様・収益分配、note、TikTok、Bluesky、Twitch、KDP、国税庁**は未取得。
- 運用アカウントの現状が未記入。
- 実運用の検証データ(投稿の反応)が存在しない。
- TikTok・Facebook の公式仕様がほぼ未調査。

## 次回のレビュー予定

公式ヘルプの確認後、または運用開始から4週後。
