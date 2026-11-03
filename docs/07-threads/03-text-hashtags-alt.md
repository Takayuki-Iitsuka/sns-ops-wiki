---
title: Threads 文章・トピックタグ・代替テキスト
platform: threads
topic: text
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.facebook.com/documentation/threads/posts.md
  - https://developers.facebook.com/documentation/threads/posts/accessibility.md
  - https://developers.facebook.com/documentation/threads/reference/publishing.md
  - https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md
  - https://developers.facebook.com/documentation/threads/create-posts/spoilers.md
---

# Threads の文章・タグ・代替テキスト

> **このページで分かること**: Threads の文章の書き方、トピックタグのルール、代替テキストの付け方、長文・スポイラーの使い方。
>
> **対象**: 初心者  **先に読むページ**: [01-setup-and-posting](01-setup-and-posting.md)

## 概要

Threads は「会話」のサービスです。長い説明より、**短く・問いかけで終わる** 文章の方が返信をもらいやすいとされます(⚪)。

タグは X や Instagram と違い、**1投稿に1つ** だけ付けられます(✅ 開発者文書)。どのタグを選ぶかが大事になります。

## 用語

| 用語 | 意味 |
|---|---|
| topic tag(トピックタグ) | 投稿の話題を示すタグ。1投稿に1つ |
| alt text(代替テキスト) | 画像・動画の内容を説明する文章。読み上げソフトが読む |
| text attachment(テキスト添付) | 本文とは別に長文(10,000字まで)を付ける機能 |
| spoiler(スポイラー) | ネタバレ防止のため文字や画像を隠す機能 |
| link preview(リンクプレビュー) | URL の内容がカード形式で表示されるもの |

## 文章

- 冒頭で要点を示し、会話を誘う質問で終える。
- 長文より**短く複数の観点**を。
- 他サービス(X・Instagram)の文面をそのままコピーしない。

### 文章の仕様(✅ 開発者文書)

| 項目 | 値 | 出典 |
|---|---|---|
| 本文 | **500字まで** | [Posts](https://developers.facebook.com/documentation/threads/posts.md) |
| 絵文字 | API では UTF-8 のバイト数で数える(1つで複数字分になることがある) | 同上 |
| リンク | **1投稿5つまで**。テキストのみの投稿では最初の URL がプレビューになる | 同上 |
| 長文 | テキスト添付で **10,000字まで**。太字・斜体・ハイライト・下線・取り消し線 | [Text Attachments](https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md) |
| 長文の制限 | テキストのみの投稿に限る。投票付きの投稿には付けられない | 同上 |

### 書く手順(⚪)

1. 言いたいことを1文で書く(結論)。
2. 理由や具体例を1〜2文足す。
3. 最後に、答えやすい質問を置く(「あなたはどうしていますか?」)。
4. 500字を超えるなら、要点だけ本文に残し、詳細はテキスト添付か返信で続ける。

## タグ(トピック)

- Threads のタグは**1投稿に1つ**とする資料がある 🟡 (#34)。公式で確認。
- 検索・分類に使われる。自分の軸に合う1つを選ぶ([hashtags](../01-common/hashtags.md))。

### トピックタグのルール(✅ 開発者文書)

| ルール | 内容 |
|---|---|
| 個数 | **1投稿に1つ**。本文に複数書いても、最初の有効なタグだけがタグになる(API) |
| 長さ | **1〜50字** |
| 使えない文字 | ピリオド(.)、アンパサンド(&) |
| 本文中のタグの区切り | スペース・タブ・改行・`.` `&` `@` `!` `?` `,` `;` `:` の直前でタグが終わる |
| 数字だけ | `#1` のような数字だけは **タグにならない** |
| 推奨の付け方(API) | 本文に書くより `topic_tag` パラメータで指定する方法が推奨 |

出典: [Threads Posts](https://developers.facebook.com/documentation/threads/posts.md)。上の (#34) の「1つとする資料」は、開発者文書で確認できました。アプリで同じ動きかは 🟡 です。

### タグの選び方の手順(⚪)

1. 投稿の主題を一言で表す(例: 「作り置き」)。
2. Threads の検索でそのタグを見て、似た投稿が集まっているか確認する。
3. 広すぎる語(「料理」)と狭すぎる語(自分だけの造語)を避ける。
4. 毎回同じタグにする必要はないが、柱ごとに決めておくと迷わない。

## 代替テキスト

- 画像に代替テキストを付けられる(⚪ 要確認)。[alt-text](../01-common/alt-text.md) に従い画像ごとに書く。

### 代替テキストの仕様(✅ 開発者文書)

| 項目 | 内容 | 出典 |
|---|---|---|
| 対象 | **画像・動画**(カルーセルの各要素を含む)。テキストのみの投稿には付けない | [Accessibility](https://developers.facebook.com/documentation/threads/posts/accessibility.md) |
| 文字数 | **1,000字まで**(`alt_text`) | [Publishing reference](https://developers.facebook.com/documentation/threads/reference/publishing.md) |
| アプリでの付け方 | 画像を添付後、画像の編集メニューから入力する形とされる | ⚪ 表記は変わる可能性 |

### 代替テキストの例

| 画像 | 例 |
|---|---|
| 料理 | `木のまな板の上に、輪切りにした焼きたてのくるみパン。断面にくるみが見える。` |
| イラスト | `鉛筆の線画。窓辺で猫が丸くなって眠っている。` |
| 画面の写し | `表計算シートの画面。1週間の投稿予定が曜日ごとに並んでいる。` |

## スポイラー(ネタバレ防止 ✅)

- 文字の一部を隠せる(1投稿 **10か所まで**)。画像・動画・カルーセルもぼかせる。
- 出典: [Spoilers](https://developers.facebook.com/documentation/threads/create-posts/spoilers.md)。アプリでの操作手順は ⚪。

## 避けること

- 他人への攻撃的な引用・晒し。
- 無関係なタグ付け。
- リンクだけの投稿(何のリンクか分からない)。

## 具体例

| | 本文 | コメント |
|---|---|---|
| 良い例 | `作り置きのゆで卵、殻をむいてから保存派ですか?むかない派ですか?\nうちはむかずに3日で食べ切っています。` + タグ「作り置き」 | 問い+自分の答え。タグ1つ |
| 悪い例 | `#料理 #レシピ #作り置き #時短 今日のごはん` | 最初の `#料理` しかタグにならず、内容もない |
| 悪い例 | `#Q&A募集中` | `&` の前でタグが切れる(✅) |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| X と同じ感覚でタグを複数付けた | タグは1つ。本文の語として残すなら `#` を外す |
| 絵文字を多用して API で文字数オーバー | API では絵文字が複数字分になる。絵文字を減らす |
| 代替テキストを付け忘れた | 投稿前に全画像を確認する習慣にする |
| 長文を返信で10回つないだ | テキスト添付(10,000字)を使う |

## 注意点

- 数値は API の公式文書(✅)です。アプリで同じかは ⚪/🟡 です。
- 代替テキストに個人情報を書かないでください([privacy](../01-common/privacy-and-personal-info.md))。

## チェックリスト

- [ ] 冒頭で要点、最後に質問
- [ ] 本文500字以内、リンク5つ以内
- [ ] トピックタグは1つ、`.` と `&` を含まない
- [ ] 画像・動画に代替テキスト(1,000字以内)
- [ ] 他サービスの文面のコピーではない

## 詳細

- API の `alt_text` は今回の公式文書では確認できず(#34)。アプリでの設定は ⚪。
- [alt-text 詳細ガイド](../01-common/alt-text.md)。

> 2026年(皇紀2686年・令和8年)11月3日の追記: 上の「API の `alt_text` は確認できず」は、開発者文書(Accessibility と Publishing reference)で **確認できました**(画像・動画に設定可、1,000字まで ✅)。アプリでの設定手順は引き続き ⚪ です。

## 関連ページ / 次に読む

- 次に読む: [04-engagement](04-engagement.md)
- [hashtags](../01-common/hashtags.md)、[alt-text](../01-common/alt-text.md)、[writing-guide](../01-common/writing-guide.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/threads/posts.md | 2026-11-03 | 500字、トピックタグ、リンク(✅) |
| https://developers.facebook.com/documentation/threads/posts/accessibility.md | 2026-11-03 | 代替テキストの対象(✅) |
| https://developers.facebook.com/documentation/threads/reference/publishing.md | 2026-11-03 | `alt_text` 1,000字(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/text-attachments.md | 2026-11-03 | テキスト添付(✅) |
| https://developers.facebook.com/documentation/threads/create-posts/spoilers.md | 2026-11-03 | スポイラー(✅) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(概要、用語、文章の仕様 ✅、書く手順、トピックタグのルール ✅、タグの選び方、代替テキストの仕様 ✅ と例、スポイラー、具体例、よくある失敗、チェックリスト)。#34 のうちタグ1つ・`alt_text` を開発者文書で確認 |
