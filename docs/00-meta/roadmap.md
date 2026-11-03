---
title: wiki 自体のロードマップ
platform: common
topic: meta
last_verified: 2026-11-03
confidence: ⚪
---

# wiki 自体のロードマップ

## 完了(2026年(皇紀2686年・令和8年)11月3日)

- [x] 3サービス(X・Instagram・note)の基本10ページ＋チェックリスト＋テーマ応用
- [x] 共通ガイド(画像・ハッシュタグ・alt・コメント・法令・AI・著作権・炎上・ツール・FAQ・動画・検索)
- [x] テーマ運用(古事記・日本書紀)10ページ
- [x] 全体戦略(KPI・導線・収益化・税務・リスク・調査)
- [x] 検査スクリプト `scripts/check_wiki.py`

## 次にやること(優先順)

| # | 項目 | 前提 |
|---|---|---|
| 1 | 公式ヘルプの裏取り([verification-queue](verification-queue.md) 全項目) | 公式本文を取得できる環境、または貼り付け |
| 2 | 運用アカウントの現状記入([kojiki-maro-jp](../07-accounts/kojiki-maro-jp.md)) | 本人の記入 |
| 3 | 神名辞典のデータ化(1柱1ファイル or 表) | 底本の決定 |
| 4 | 画像テンプレ(比率別・安全領域つき)の作成 | デザインツールの選定 |
| 5 | 動画の公式仕様の追加 | #18 |
| 6 | Threads・YouTube の追加([99-planned](../99-planned/README.md)) | 優先度の判断 |
| 7 | GitHub Actions による自動検査 | `.github/workflows/check.yml` |
| 8 | 閲覧サイト化(MkDocs 等) | 公開方針 |

## 運用ルール

- 変更は作業ブランチに積み、区切りで PR を作る。
- 大きな更新の前後で `python3 -I scripts/check_wiki.py` を実行する。
- 見直しの記録は [quality-review-log](quality-review-log.md)。
