---
title: X 運用チェックリスト
platform: x
topic: checklist
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/fundamentals/counting-characters.md
  - https://docs.x.com/x-api/fundamentals/edit-posts.md
  - https://docs.x.com/x-api/fundamentals/metrics.md
  - https://docs.x.com/developer-guidelines.md
---

# X 運用チェックリスト

> **このページで分かること**: X 運用の「一度だけ・投稿前・投稿後・週次・月次・トラブル時」にやることの一覧。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [X 概要](README.md)

## 概要

チェックリストは、慣れてきたころの **うっかりミス** を防ぐ道具です。印刷したり、自分のメモアプリにコピーしたりして使ってください。各項目の詳しい説明はリンク先のページにあります。

数値の根拠: 文字数は [Counting Characters](https://docs.x.com/fundamentals/counting-characters.md)(✅)、編集は [Edit Posts](https://docs.x.com/x-api/fundamentals/edit-posts.md)(✅)、指標は [Metrics](https://docs.x.com/x-api/fundamentals/metrics.md)(✅)、自動化は [開発者ガイドライン](https://docs.x.com/developer-guidelines.md)(✅)。

## 用語

| 用語 | 意味 |
|---|---|
| ALT(代替テキスト) | 画像の説明文([05-alt-text](05-alt-text.md)) |
| PR 表記 | 広告・案件であることを示す表記 |
| 固定ポスト | プロフィール上部に固定するポスト |

## 初期設定(一度だけ)

- [ ] 2段階認証、バックアップコードの保管(非公開)
- [ ] プロフィール画像・ヘッダー・bio・固定ポスト([01-account-setup](01-account-setup.md))
- [ ] プライバシー・通知・ミュート語の設定
- [ ] 連携アプリの棚卸し
- [ ] 自己紹介の導線(note の入口記事)
- [ ] 運用専用のメールアドレスで登録した
- [ ] bio は160字以内(🟡)、ヘッダーは 1500×500(🟡)
- [ ] 位置情報をオフにした
- [ ] bot の場合は自動化ラベルを設定した(✅)

## 投稿前

- [ ] 出典(一次資料)を確認した
- [ ] 固有名詞・年の表記が統一(年は「西暦(皇紀・和暦)」)
- [ ] 画像の比率・容量([03-media-specs](03-media-specs.md))
- [ ] ALT を設定([05-alt-text](05-alt-text.md))
- [ ] ハッシュタグは1〜2個程度([04-text-hashtags](04-text-hashtags.md))
- [ ] 広告・PR 表記の要否
- [ ] 断定表現を避けた([sensitive-topics](../01-common/sensitive-topics-and-accuracy.md))
- [ ] 重み付きで280以内(日本語は約140字、URL は23字 ✅)
- [ ] 返信の範囲を選んだ([02-posting](02-posting.md))
- [ ] 投票・予約投稿は公開後に編集できない前提で見直した(✅)
- [ ] 写り込み・個人情報がない([privacy](../01-common/privacy-and-personal-info.md))
- [ ] AI 生成の画像なら開示した

## 投稿後

- [ ] 最初の1時間は返信に対応
- [ ] 誤りの指摘があれば速やかに訂正
- [ ] 1週間後にインプレッション・保存(ブックマーク)・リンククリックを記録
- [ ] 誤字に気づいたら30分以内なら編集を検討(最大5回 ✅)
- [ ] 荒れたら返信の範囲を狭める・返信を非表示にする([06-engagement](06-engagement.md))

## 週次

- [ ] [週次レビュー](../../templates/weekly-review.md)
- [ ] 上位/下位3投稿の違いを言語化
- [ ] 次週の企画3件(柱の偏りを確認)
- [ ] 指標を記録した(API の非公開指標は投稿から30日以内のみ ✅)
- [ ] 次週に試すことを1つ決めた([08-analytics](08-analytics.md))

## 月次

- [ ] フォロワー推移と目標の差を確認した([01-goals-kpi-roadmap](../30-strategy/01-goals-kpi-roadmap.md))
- [ ] 固定ポスト・bio を見直した
- [ ] 連携アプリ・外部ツールを棚卸しした
- [ ] 規約・収益化条件の変更を確認した([10-policies](10-policies.md)、[07-monetization](07-monetization.md))
- [ ] データのバックアップを取った([data-backup-and-portability](../01-common/data-backup-and-portability.md))

## トラブル時

- [ ] 通知の内容を記録した
- [ ] 事実確認をしてから対応を決めた([crisis-response](../01-common/crisis-response.md))
- [ ] 必要なら訂正ポストを1本にまとめた
- [ ] 異議申立ては事実と根拠だけで書いた([10-policies](10-policies.md))
- [ ] 不正ログインの疑いがあればパスワード変更・2段階認証の再確認([account-security](../01-common/account-security.md))

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| チェックリストが長すぎて使わなくなった | 自分がよく忘れる項目だけ残した短い版を作る |
| 投稿後のチェックを忘れる | 投稿時刻の1時間後と1週間後にリマインダーを設定 |

## 注意点

- 各サービスの仕様は変わります。数値は各ページの確度ラベル(✅🟡⚪)を確認してください。

## 関連ページ / 次に読む

- [13-faq](13-faq.md)(困ったとき)
- [posting-workflow](../01-common/posting-workflow.md)、[画像チェックリスト](../../templates/image-checklist.md)、[投稿計画](../../templates/post-plan.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/fundamentals/counting-characters.md | 2026-11-03 | 文字数(✅) |
| https://docs.x.com/x-api/fundamentals/edit-posts.md | 2026-11-03 | 編集(✅) |
| https://docs.x.com/x-api/fundamentals/metrics.md | 2026-11-03 | 指標(✅) |
| https://docs.x.com/developer-guidelines.md | 2026-11-03 | 自動化(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、各段階の項目を追加、月次・トラブル時の節、よくある失敗、出典表) |
