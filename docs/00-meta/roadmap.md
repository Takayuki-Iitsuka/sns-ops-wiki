---
title: wiki 自体のロードマップ
platform: common
topic: meta
last_verified: 2026-11-03
confidence: ⚪
---

# wiki 自体のロードマップ

> **このページで分かること**: このナレッジベース自体の今後の計画(完了したこと・次にやること)。

## 範囲

このリポジトリは **SNS 運用の知識**に限る。特定の題材(テーマ)の内容は別の wiki で管理する。

## 完了(2026年(皇紀2686年・令和8年)11月3日)

- [x] X・Instagram・note の基本ページ(初期設定〜ルール、チェックリスト)
- [x] YouTube・TikTok・Threads・Facebook の追加
- [x] その他(Bluesky・LINE・Twitch)、収益化サービス(FANBOX・Fantia・Patreon・Ko-fi・BOOTH・SUZURI・KDP・アフィリエイト・メンバーシップ設計)
- [x] **API 活用ガイド**(X API v1.1→v2、Instagram/Threads/YouTube/TikTok/その他、自動化、パイプライン設計)
- [x] **画像・動画の横断比較と書き出しプリセット**
- [x] 共通ガイド(企画・ブランド・文章術・検索・AI 方針・著作権・炎上対応 ほか)
- [x] 戦略(KPI・導線・収益化・税務・リスク・調査)
- [x] 検査スクリプトと CI 設定(`scripts/check_wiki.py`、`.github/workflows/check.yml`)
- [x] 料金プラン(`40-pricing`)、スマホ最適化、ALT の詳細、ハッシュタグ、AI ルール、API のメリット、ツール連携、案件・メディアキット、未整備事項の考察
- [x] **全ページの初心者向け加筆**(各ページに「このページで分かること」・概要・用語・手順・具体例・よくある失敗・チェックリスト・出典・変更履歴)
- [x] 入門ページ(はじめての SNS 運用、サービスの選び方、最初の30日、用語解説)
- [x] 未整備領域の共通ページ(ライブ配信、ニュースレター、ポッドキャスト、コミュニティ運営、ソーシャルリスニング、多言語、動画編集アプリ)
- [x] API の入門・認証・秘密情報の管理・エラー対処・Python の最初の一歩、X API の始め方
- [x] 雛形の追加(投稿カレンダー、月次レビュー、メディアキット)

## 次にやること(優先順)

| # | 項目 | 前提 |
|---|---|---|
| 1 | 公式ヘルプ・開発者文書の裏取り([verification-queue](verification-queue.md) の優先度 高と #72〜#130。接続できないホストはネットワーク設定の許可が必要) | 公式本文を取得できる環境、または貼り付け |
| 2 | 運用アカウントの現状記入([31-accounts](../31-accounts/README.md)) | 本人の記入 |
| 3 | 画像・動画テンプレ(比率別・安全領域つき)の作成 | デザインツールの選定 |
| 4 | 書き出し用スクリプト(Pillow/ffmpeg)の追加 | export-presets の確定 |
| 5 | Pinterest の追加。Discord・X Subscriptions は作成済み(公式での裏取り待ち #64〜#71)([99-planned](../99-planned/README.md)) | 優先度の判断 |
| 6 | 投稿データの検証スクリプト(YAML の文字数・画像仕様チェック) | [09-architecture-patterns](../20-api/09-architecture-patterns.md) |
| 7 | 閲覧サイト化(MkDocs 等) | 公開方針 |

## 運用ルール

- 変更は作業ブランチに積み、区切りで PR を作る。
- 大きな更新の前後で `python3 -I scripts/check_wiki.py` を実行する。
- 見直しの記録は [quality-review-log](quality-review-log.md)。

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成 |
| 2026-11-03 | 全ページ加筆の完了を記録し、次にやることを更新 |
