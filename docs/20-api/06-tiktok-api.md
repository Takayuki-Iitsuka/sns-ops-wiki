---
title: TikTok API
platform: tiktok
topic: api
last_verified: 2026-11-03
confidence: ⚪
---

# TikTok API

> **今回、公式・二次資料とも調査できていません**。以下は一般的な理解(⚪)で、公式の TikTok for Developers で確認が必要です (#32)。

## 主な API(⚪)

| API | 用途 |
|---|---|
| Login Kit | TikTok アカウントでのログイン、OAuth |
| Content Posting API | 動画/フォトの投稿(下書きへのアップロード、または直接投稿) |
| Display API | 自分のプロフィール・動画の表示 |
| Research API | 研究者向け(申請・審査) |

## 制約(⚪ 要確認)

- 直接投稿の機能は**審査(監査)を通るまで制限**があり、投稿の公開範囲が限定される場合がある。
- 動画の仕様は UI より厳しいことがある([02-media-specs](../06-tiktok/02-media-specs.md))。
- ユーザーの明示的な同意と、投稿内容の開示(ブランドコンテンツ・AI 生成の設定)が API でも必要。

## 運用の指針

1. 個人利用の予約投稿は、公式の機能や公認ツールを優先。
2. 審査・利用規約を満たせるかを先に確認してから実装。
3. 自動化の規約リスクは [08-automation-and-tools](08-automation-and-tools.md)。
