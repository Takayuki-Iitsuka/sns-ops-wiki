---
title: X よくある質問とトラブル対処
platform: x
topic: tips
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.x.com/fundamentals/counting-characters.md
  - https://docs.x.com/x-api/fundamentals/edit-posts.md
  - https://docs.x.com/x-api/media/introduction.md
  - https://docs.x.com/developer-guidelines.md
  - https://help.x.com/en/using-x/how-to-use-hashtags
---

# X よくある質問とトラブル対処

> **このページで分かること**: X の初心者がつまずきやすい質問と、その原因・対処。
>
> **対象**: 初心者  **先に読むページ**: [X 概要](README.md)

## 概要

困ったときは、まず **原因が「仕様」なのか「規約」なのか「設定」なのか** を切り分けます。このページは症状から探せるようにまとめています。共通の質問は [faq](../01-common/faq.md) も参照してください。

## 用語

| 用語 | 意味 |
|---|---|
| 403 エラー | 「権限がない」という意味のエラー。上限を超えた動画などで出る |
| ロック | 一時的にアカウントの操作が制限されること |
| shadowban(シャドウバン) | 表示が制限されているのではと利用者の間で言われる状態の俗称。公式の用語ではない(⚪) |

## 投稿・文字数

### Q. 140字以内なのに投稿できません

- 日本語は1字=2、絵文字は2、URL は23で数えます(✅ [Counting Characters](https://docs.x.com/fundamentals/counting-characters.md))。
- 対処: 絵文字や URL を減らすか、スレッドに分けます。詳しくは [04-text-hashtags](04-text-hashtags.md)。

### Q. 投稿を編集できません

- 編集できるのは **投稿から30分以内・5回まで** です(✅ [Edit Posts](https://docs.x.com/x-api/fundamentals/edit-posts.md))。
- 投票付き・予約投稿・他人への返信・コミュニティの投稿は編集できません(✅)。
- アプリで編集を使える契約の条件は ⚪ 要確認です。
- 対処: 削除して投稿し直すか、訂正の返信を付けます。

### Q. ハッシュタグがリンクになりません

- タグの中にスペースや句読点があると正しく機能しません(🟡 [How to use hashtags](https://help.x.com/en/using-x/how-to-use-hashtags))。
- 数字だけのタグは使えません(🟡)。

## 画像・動画

### Q. 画像の一部が切れて表示されます

- 単一画像は 2:1〜3:4 の範囲外だとトリミングされるとされます(🟡)。対処は [03-media-specs](03-media-specs.md)。

### Q. 動画がアップロードできない・403 エラーが出ます

- 通常アカウントの動画は **20分・8GB** まで、Premium・認証済みは **125分・16GB** まで(✅ API の仕様 [Media](https://docs.x.com/x-api/media/introduction.md))。
- 形式は MP4/MOV、H.264 + AAC-LC が推奨です(✅)。
- アプリからの投稿上限は API と同じとは限りません(⚪ #18)。

## 表示・反応

### Q. 急にインプレッションが減りました

- 原因はさまざまで、公式に確認できる判定方法はありません(⚪)。
- 確認すること:
  1. 同じ内容を連投していないか(スパムの恐れ ✅ [開発者ガイドライン](https://docs.x.com/developer-guidelines.md))
  2. 無関係なハッシュタグを付けていないか
  3. 外部ツールの自動いいね・自動フォローを使っていないか(✅ 禁止)
  4. 投稿の時間帯・形式が変わっていないか([08-analytics](08-analytics.md))
- 「シャドウバン」という言葉は公式の用語ではありません(⚪)。原因を推測で決めつけず、上の点を1つずつ確認します。

### Q. 返信が荒れてしまいました

- 返信の範囲を狭める、返信を非表示にする、ミュート・ブロック・通報を使います([06-engagement](06-engagement.md))。
- 引用で広がっている場合は、反論を急がず事実確認をします([crisis-response](../01-common/crisis-response.md))。

## アカウント

### Q. ログインできません・乗っ取られたかもしれません

1. 公式アプリ・公式サイトからパスワードの再設定を試す(届いたメールのリンクは送信元を確認)。
2. ログインできたら、パスワード変更・2段階認証の再設定・連携アプリの確認をする。
3. 不審な投稿・DM を削除し、フォロワーに知らせる。

詳しくは [account-security](../01-common/account-security.md)。

### Q. アカウントがロック・凍結されました

1. 通知の内容(対象の投稿・規約の条項)を記録する。
2. 求められた手続き(電話番号の確認など)があれば、公式の画面から行う。
3. 誤りだと考える場合は異議申立てをする([10-policies](10-policies.md))。
4. 再開までの間は、note・メールなど他の場所で読者に連絡する([funnel](../30-strategy/02-funnel.md))。

## 収益化

### Q. 収益化の条件を満たしているのに申請できません

- 条件・名称は 2026年(皇紀2686年・令和8年)に変更があったと報道されています(🟡)。Premium の契約が必要とされる点も確認してください([07-monetization](07-monetization.md))。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 原因を「シャドウバン」と決めつけて投稿をやめた | 上の確認項目を順に見る。4週間のデータで判断 |
| 不審な DM のリンクからログインした | すぐパスワードを変更し、連携アプリを確認 |
| 外部の「凍結解除代行」にパスワードを渡した | 渡さない。手続きは公式の画面からのみ |

## 注意点

- パスワード・バックアップコードを他人に教えないでください。公式がパスワードを聞くことは通常ありません(⚪)。
- 仕様は変わります。数値は各ページの確度ラベルを確認してください。

## 関連ページ / 次に読む

- [11-checklist](11-checklist.md)、[faq](../01-common/faq.md)、[account-security](../01-common/account-security.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/fundamentals/counting-characters.md | 2026-11-03 | 文字数(✅) |
| https://docs.x.com/x-api/fundamentals/edit-posts.md | 2026-11-03 | 編集(✅) |
| https://docs.x.com/x-api/media/introduction.md | 2026-11-03 | 動画の上限(✅ API) |
| https://docs.x.com/developer-guidelines.md | 2026-11-03 | スパム・自動化(✅) |
| https://help.x.com/en/using-x/how-to-use-hashtags | 2026-11-03 | ハッシュタグ(🟡 検索要約) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(初心者向けのよくある質問とトラブル対処) |
