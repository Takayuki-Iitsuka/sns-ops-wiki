---
title: X 画像の説明文(ALT)
platform: x
topic: alt
last_verified: 2026-11-03
confidence: ⚪
---

# X の画像説明文(ALT)

## 設定手順 ⚪

1. 画像を添付する。
2. 画像上の「ALT」または「説明を追加」を選ぶ。
3. 説明文を入力して保存。画像ごとに設定する。

## 仕様

| 項目 | 内容 | 確度 |
|---|---|---|
| 文字数上限 | **1,000字**(API の Create Media Metadata の `alt_text` の最大長) | ✅ docs.x.com(アプリ上の上限も同じかは未確認) |
| 画像ごと | 4枚それぞれ設定可 | ⚪ |

## 書き方

共通原則は [alt-text](../01-common/alt-text.md)。X では本文の字数を使わないので、**画像内の文字は ALT に書く**のが有効（スクリーンショットなど）。

## 例

> スクリーンショット。SNS運用の週次カレンダーで、月曜は「X: 告知」、水曜は「note: 記事公開」、金曜は「Instagram: 画像3枚」と入力されている。

## API で付ける場合(✅ docs.x.com)

- **Create Media Metadata** で `alt_text`(**最大1,000字**)を設定。**$0.005/回**。
- 手順: メディアをアップロードして `media_id` を得る → メタデータで alt を付与 → `POST /2/tweets` に `media_ids` を渡す。
- 画像4枚なら 4 回(= $0.02)。月30枚で $0.15([06-cost-planning](../40-pricing/06-cost-planning.md))。

## 詳細ガイド

種類別の書き方、日本語の注意、読み上げテスト、AI での作成は [alt-text 詳細ガイド](../01-common/alt-text.md) と [alt-text-log](../../templates/alt-text-log.md)。
