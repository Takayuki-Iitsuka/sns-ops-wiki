---
title: 品質レビューの記録
platform: common
topic: meta
last_verified: 2026-11-03
confidence: ⚪
---

# 品質レビューの記録

> **このページで分かること**: このナレッジベースを作る過程で行った見直し(レビュー)の記録。何をいつ直したか、どんな訂正があったかが分かります。

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

### パス8: 料金・モバイル・ALT・AI・API 活用の拡充
- 追加: `40-pricing`(7)、`mobile-viewing-optimization`、`alt-text`(全面改訂)、`hashtags`(全面改訂)、`ai-rules-by-platform`、`20-api/10`・`11`、`link-in-bio-and-utm`、`data-backup`、`privacy`、`music`、`07-sponsorship`、`gap-analysis`、`templates/alt-text-log`。
- 調査: 料金(X Premium・Grok・Google AI・YouTube Premium・Meta One・note・ツール)、StatCounter、AI ラベル、ハッシュタグ、最近の動向を検索。**公式で直接確認**: X(xAI クレジット還元、MCP、Grok を使うモデレーション)、Google Cloud(Gemini・Imagen・Veo の料金)、YouTube の AI 開示、Instagram の `alt_text` 1,000字。
- 重要な発見: Instagram のハッシュタグ上限 5 個(報道)と公式 API 文書の 30 個が食い違う。X の Premium の円価格は 2026年の公式値を確認できない。Veo の料金単位が不明。
- 要検証リストを #63 まで拡張。

### パス9: 全ページの初心者向け加筆(2026年(皇紀2686年・令和8年)11月3日)

- 依頼: 全ファイルを初心者でも分かるように詳細・丁寧に加筆し、ページが増える場合は新規作成。
- 方法: フォルダ単位で8つの作業に分け、共通の執筆規約(雛形の節、確度ラベル、出典、年表記、既存の ✅ と出典を削らない)で加筆。数値は公式資料で確認し、確認できない事項は要検証リスト #72〜#130 に登録。
- 規模: 151 → 約184ファイル。主なページは 30〜50行 → 120〜250行。
- 雛形の改訂: [page-template](page-template.md) に「このページで分かること」「用語」「具体例」「よくある失敗と対処」「チェックリスト」を追加。
- **訂正**: YouTube バナーの安全領域 1546×423 → **1235×338**(✅)。YouTube のサムネイル「1280×720」→ **16:9・幅640px以上**(✅)。YouTube のハッシュタグ「60個超は無視」→ **60個を超えるとすべて無効**(✅)。Instagram API の `is_ai_generated` の追加時期「2025年以降」→ **2026年6月22日**(✅ changelog)。BOOTH の手数料は改定後の報告値 5.6%+45円を併記(🟡)。
- **解消**: 要検証 #15(X の文字数)、#31(YouTube の文字数・ハッシュタグ・バナー)、#34(Threads のタグ数)、#38(YouTube API のクォータ)、#40(LINE の料金プラン)、#41 の KDP 部分。
- **番号の衝突を修正**: 並行した別セッションが X Subscriptions・Discord の要検証を既存と同じ #59〜#66 で登録していたため、新しい側を #64〜#71 に付け替えた(既存の #59〜#63 は不変)。
- **接続できなかったホスト**: TikTok のヘルプ・ニュースルーム、W3C、総務省、内閣府、個人情報保護委員会、about.instagram.com、創作支援系、Discord、Spotify、Substack、CapCut、GitHub Docs ほか。該当箇所は 🟡/⚪ のまま。
- 検査: リンク切れ・front matter・年の換算 0件。

### 要件の突合せ

| 要件 | 状況 |
|---|---|
| 投稿ルート | 各サービスの投稿ページ、posting-workflow ✓ |
| 収益化基準 | 各サービスの monetization、比較、戦略 ✓(条件は未確認) |
| ノウハウ | 各 tips、writing-guide、content-planning ✓ |
| コメント | 各 engagement、共通、crisis-response ✓ |
| ハッシュタグ | 各 text、共通 hashtags ✓ |
| 画像の説明文 | 各 alt、共通 alt-text、文例集 ✓(note は機能未確認 #16) |
| 画像・動画の形式・サイズ・比率 | 比較表2本、書き出しプリセット、各 media-specs ✓(公式未確認が残る) |
| API(X の v1.1→v2 を含む) | 20-api ✓(X・Instagram・Threads は ✅。期日の一部は #36) |
| 料金プラン(Grok・Google を含む) | 40-pricing ✓(X API・Google Cloud は ✅、他は 🟡) |
| スマホ(iPhone・Android)での見やすさ | mobile-viewing-optimization ✓(計算に基づく考察) |
| ALT の詳細 | alt-text ✓、サービス別、API、記録表 |
| AI 利用のルール・設定 | ai-rules-by-platform ✓ |
| ハッシュタグの効率的な使い方 | hashtags ✓ |
| API のメリット・ツール連携 | 20-api/10・11 ✓ |
| 収益化できる追加サービス | YouTube、TikTok、Facebook、Twitch、創作支援系 ✓ |

| 初心者への分かりやすさ | 入門4ページ、全ページに概要・用語・手順・例・失敗・チェックリスト ✓(パス9) |

### 残課題(次パスへ)

- 公式の裏取りは進んだが、**X アプリの仕様・収益分配、note、TikTok、Bluesky、Twitch、KDP、国税庁**は未取得。
- 運用アカウントの現状が未記入。
- 実運用の検証データ(投稿の反応)が存在しない。
- TikTok・Facebook の公式仕様がほぼ未調査。

## 次回のレビュー予定

公式ヘルプの確認後、または運用開始から4週後。

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(パス1〜8) |
| 2026-11-03 | パス9(全ページの初心者向け加筆)を追記 |
