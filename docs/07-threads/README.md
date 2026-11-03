---
title: Threads 概要
platform: threads
topic: overview
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/threads/overview.md
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/create-posts.md
---

# Threads

> **このページで分かること**: Threads がどんなサービスで、何に向いているか。このフォルダのページを読む順番。
>
> **対象**: Threads をこれから始める初心者  **先に読むページ**: [はじめての SNS 運用](../00-meta/beginners-guide.md)(別担当が作成予定)

## 概要

Meta が提供するテキスト中心のサービスで、Instagram アカウントと連携します。**公式 API が整備されている**ため、自動化・予約投稿の基盤にしやすい点が特徴です(🟡)。

2023年(皇紀2683年・令和5年)に公開されました(⚪ 一般知識)。当初は Instagram のアカウントが必要でしたが、その後 Instagram なしでも登録できるようになったとされます(🟡 [01-setup-and-posting](01-setup-and-posting.md))。

| 項目 | 内容 |
|---|---|
| 形式 | テキスト、画像、動画、カルーセル、投票(✅ API で確認) |
| 強み | Instagram 連携で導入が容易、会話中心、API が公式 |
| 弱み | 収益化プログラムは未確認、仕様変更が速い |
| 向く用途 | 会話・意見、Instagram からの導線、ストック型でない短文発信 |

### 基本ルールをひと目で(✅ 公式の開発者文書)

| 項目 | 値 | 出典 |
|---|---|---|
| 本文 | **500字まで** | [Threads API overview](https://developers.facebook.com/documentation/threads/overview.md) |
| 長文(テキスト添付) | **10,000字まで**(テキストのみの投稿) | [Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md) |
| カルーセル | **2〜20件** | overview |
| トピックタグ | **1投稿に1つ**、1〜50字 | [Threads Posts](https://developers.facebook.com/documentation/threads/posts.md) |
| リンク | **1投稿5つまで** | 同上 |
| 代替テキスト | 画像・動画ごとに **1,000字まで** | [Accessibility](https://developers.facebook.com/documentation/threads/posts/accessibility.md) |

上は API の仕様です。アプリから投稿するときも同じかは、各ページで確度を分けて書いています。

## 用語

| 用語 | 意味 |
|---|---|
| thread(スレッド、投稿) | Threads の投稿1件。続けてつなげた投稿の連なりも指す |
| topic tag(トピックタグ) | 投稿に付ける話題のタグ。1投稿に1つ |
| carousel(カルーセル) | 複数の画像・動画を横にスワイプして見せる投稿 |
| repost(リポスト)/ quote(引用) | 他人の投稿の再共有 / コメント付きの共有 |
| fediverse(フェディバース) | Mastodon など、互いにつながる分散型 SNS の総称 |
| insights(インサイト) | 閲覧数や反応などの分析データ |

## 読む順番(初心者向け)

1. [01-setup-and-posting](01-setup-and-posting.md) で登録・初期設定・投稿の手順を覚える。
2. [03-text-hashtags-alt](03-text-hashtags-alt.md) で文章・タグ・代替テキストの書き方を知る。
3. 画像・動画を使うときは [02-media-specs](02-media-specs.md)。
4. 反応が来たら [04-engagement](04-engagement.md)。
5. 1か月後に [06-analytics-and-tips](06-analytics-and-tips.md) で振り返る。
6. ルールと点検は [07-policies-and-checklist](07-policies-and-checklist.md)、困ったら [08-faq](08-faq.md)。

## ページ一覧

| ページ | 内容 |
|---|---|
| [01-setup-and-posting](01-setup-and-posting.md) | 初期設定と投稿 |
| [02-media-specs](02-media-specs.md) | 画像・動画・文字数 |
| [03-text-hashtags-alt](03-text-hashtags-alt.md) | 文章・タグ・代替テキスト |
| [04-engagement](04-engagement.md) | 会話・運用 |
| [05-monetization](05-monetization.md) | 収益化 |
| [06-analytics-and-tips](06-analytics-and-tips.md) | 分析とコツ |
| [07-policies-and-checklist](07-policies-and-checklist.md) | ルールとチェックリスト |
| [08-faq](08-faq.md) | よくある質問とトラブル対処 |
| API | [20-api/04-threads-api](../20-api/04-threads-api.md) |

> Meta の公式ヘルプ本文は取得できていません。数値は 🟡(二次資料)で公式の確認が必要です (#34)。

> 2026年11月3日の追記: 開発者文書(`developers.facebook.com`)で、トピックタグは **1投稿に1つ**(✅)、代替テキストは **1,000字まで**(✅)と確認しました。アプリのヘルプ(`help.instagram.com`)由来の項目と収益化は引き続き未確認です(#34)。

## 注意点

- Threads は機能追加が速く、アプリのボタン名は変わることがあります(⚪)。
- API の数値(✅)とアプリの上限が同じとは限りません。

## 関連ページ / 次に読む

- [01-setup-and-posting](01-setup-and-posting.md)
- [Threads API](../20-api/04-threads-api.md)、[Instagram](../03-instagram/README.md)、[用語集](../00-meta/glossary.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/overview.md | 2026-11-03 | 文字数・カルーセル・上限(✅) |
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | トピックタグ・リンク(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md | 2026-11-03 | テキスト添付10,000字(✅) |
| https://developers.facebook.com/documentation/threads/posts/accessibility.md | 2026-11-03 | 代替テキスト(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(基本ルール表 ✅、用語、読む順番、08-faq を追加。形式の確度を ⚪ から ✅ に更新) |
