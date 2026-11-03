# CLAUDE.md — sns-ops-wiki 作業指針

- このリポジトリは **SNS 運用ナレッジベース**(Markdown)。特定の題材(テーマ)の内容は含めない(別の wiki で管理)。応答・文書は日本語。
- リポジトリは public。秘密情報(API キー・トークン・パスワード・非公開の運用数値)を書かない。
- 数値・条件を書く際は必ず確度ラベル(✅公式確認済 / 🟡二次資料 / ⚪一般知識)と出典 URL を付ける。確認できない事項は推測せず `docs/00-meta/verification-queue.md` に追記する(番号は振り直さない)。
- ページは `docs/00-meta/page-template.md` の雛形に従う。構成は `README.md` 参照。
- 年表記は「西暦(皇紀・和暦)」併記(例: 2026年(皇紀2686年・令和8年))。
- 作業後は `python3 -I scripts/check_wiki.py` を実行する。
- ブランチ運用: 指定の作業ブランチに commit/push。PR は依頼があった時のみ作成。
