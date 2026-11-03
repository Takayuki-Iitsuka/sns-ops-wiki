---
title: Bluesky
platform: bluesky
topic: overview
last_verified: 2026-11-03
confidence: 🟡
---

# Bluesky

AT Protocol に基づく分散型の短文 SNS。**API とプロトコルが公開**されており、自動化・独自フィード・ボットが作りやすいのが特徴です。収益化プログラムはなく、集客・技術コミュニティ向けです。

## 仕様(🟡 二次資料。資料間で不一致 #39)

| 項目 | 値 | 確度 |
|---|---|---|
| 文字数 | 300 grapheme(書記素)単位 | 🟡 |
| 画像 | 最大4枚。容量 1MB(従来)/ 2MB(新しい報告) | 🟡 |
| 動画 | 1本。3分・100MB(従来)/ 10分・300MB(新しい報告) | 🟡 |
| ハッシュタグ・メンション・リンク | 可(リッチテキストの facets として表現) | ⚪ |
| 代替テキスト | 画像に付けられる | ⚪ |

> 公式の確認先: AT Protocol の lexicon(`app.bsky.embed.images`、`app.bsky.embed.video`)。

## 設定・運用

1. ハンドル(ドメインを自分で持つとアカウントの信頼性が上がる ⚪)。
2. プロフィール・固定投稿。
3. カスタムフィード/リスト/モデレーションの活用。
4. 規約・コミュニティガイドライン。

## API

AT Protocol は認証(アプリパスワード/OAuth)、レコード作成(`app.bsky.feed.post`)、画像のアップロード(blob)で投稿できる。詳細: [20-api/07-other-apis](../20-api/07-other-apis.md)。

## 収益化

公式のプログラムはなし。誘導先(note・YouTube・書籍・サポート)を用意する。

## 書き出し

[export-presets](../01-common/export-presets.md)(従来の 1MB 上限に合わせる)。
