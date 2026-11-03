---
title: Bluesky
platform: bluesky
topic: overview
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://docs.bsky.app/
  - https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/embed/images.json
  - https://www.engadget.com/social-media/bluesky-adds-3-minute-video-uploads-and-inbox-management-features-220317950.html
  - https://engadget.com/2244638/bluesky-now-supports-10-minute-videos-larger-file-sizes/
---

# Bluesky

> **このページで分かること**: Bluesky(ブルースカイ)の特徴、アカウントの始め方、投稿の仕様、運用のコツ。
>
> **対象**: 初心者  **先に読むページ**: [サービスの選び方](../01-common/choosing-platforms.md)

## 概要

AT Protocol に基づく分散型の短文 SNS。**API とプロトコルが公開**されており、自動化・独自フィード・ボットが作りやすいのが特徴です。収益化プログラムはなく、集客・技術コミュニティ向けです。

見た目と使い方は X(旧 Twitter)に近く、短い文章・画像・動画を投稿し、フォロー・いいね・リポストで広がります。
大きな違いは、**どのタイムライン(フィード)を見るかを利用者が選べる**ことと、**自分のドメインをハンドル(ID)にできる**ことです。

## 用語

| 用語 | 意味 |
|---|---|
| AT Protocol(エーティー プロトコル) | Bluesky の土台になっている公開の通信規格 |
| 分散型 | 1つの会社のサーバーだけに依存しない仕組み |
| ハンドル | `@name.bsky.social` のような ID。自分のドメインも使える |
| カスタムフィード | 条件で投稿を集めた独自のタイムライン。誰でも作れる |
| スターターパック | おすすめアカウントやフィードをまとめて紹介する機能(⚪ 名称は要確認) |
| grapheme(書記素) | 人が「1文字」と感じる単位。絵文字や結合文字も1つと数える |
| アプリパスワード | 外部ツール用の専用パスワード。本来のパスワードを渡さずに済む |
| lexicon(レキシコン) | AT Protocol のデータ形式の定義。投稿の上限などもここに書かれる |

## 手順: アカウントを始める(⚪ 画面の表記は変わる可能性)

1. 公式アプリ(iOS・Android)または Web 版を開き、アカウントを作成します。
2. メールアドレス・パスワード・生年月日を入力し、ハンドルを決めます(例: `@yourname.bsky.social`)。
3. プロフィール画像・バナー・自己紹介を設定します。自己紹介には「何を投稿するか」を書きます。
4. 興味のある話題を選び、フォローするアカウントやフィードを追加します。
5. 2段階認証(メールでの確認コード ⚪ 方式は要確認)を有効にします([アカウントのセキュリティ](../01-common/account-security.md))。
6. 自己紹介の投稿を作り、プロフィールに**固定**します。

### 独自ドメインをハンドルにする(任意)

1. 自分のドメイン(例: `example.com`)を持っている必要があります。
2. 設定のハンドル変更から「自分のドメインを使う」を選びます(⚪)。
3. 表示される値を、ドメインの DNS に TXT レコードとして登録します(⚪ 手順は公式で確認)。
4. 確認が通ると、ハンドルが `@example.com` になります。

公式サイトや店のドメインをハンドルにすると、**本物のアカウントだと分かりやすく**なります(⚪)。

## 仕様(🟡 二次資料。資料間で不一致 #39)

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| 文字数 | 300 grapheme(書記素)単位 | 🟡 | 検索要約(lexicon の型定義) |
| 画像 | 最大4枚。容量 1MB(従来)/ 2MB(新しい報告) | 🟡 | [lexicon(GitHub)](https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/embed/images.json) の古い写しは 1,000,000 バイト |
| 動画 | 1本。3分・100MB(従来)/ 10分・300MB(新しい報告) | 🟡 | 下の経緯を参照 |
| ハッシュタグ・メンション・リンク | 可(リッチテキストの facets として表現) | ⚪ | — |
| 代替テキスト | 画像に付けられる | ⚪ | — |

> 公式の確認先: AT Protocol の lexicon(`app.bsky.embed.images`、`app.bsky.embed.video`)。

動画の上限の経緯(🟡 報道):

| 時期 | 内容 | 出典 |
|---|---|---|
| 2025年(皇紀2685年・令和7年)3月 | 1分 → 3分に延長(アプリ 1.99) | 🟡 [Engadget](https://www.engadget.com/social-media/bluesky-adds-3-minute-video-uploads-and-inbox-management-features-220317950.html) |
| 2026年(皇紀2686年・令和8年)8月 | 10分・300MB に拡大と報道(300MB の時期は資料により6月とも) | 🟡 [Engadget](https://engadget.com/2244638/bluesky-now-supports-10-minute-videos-larger-file-sizes/) |

## 設定・運用

1. ハンドル(ドメインを自分で持つとアカウントの信頼性が上がる ⚪)。
2. プロフィール・固定投稿。
3. カスタムフィード/リスト/モデレーションの活用。
4. 規約・コミュニティガイドライン。
5. **ラベル・ミュートワード**で見たくない話題を減らす(⚪)。
6. X と同じ内容を投稿する場合も、300字に収まるよう要点を絞る。

## 具体例: 投稿文

```
地域の小さな店です。毎週金曜に新商品の写真を投稿します。
今日は秋の新作3種。店頭は11時から。
#地域の店 #新商品
```

| 良い例 | 悪い例 |
|---|---|
| 1投稿1話題。画像に代替テキスト | X の長文を貼り、300字を超えて切れる |
| 関心のあるフィードに入る話題語を入れる | 関係ないハッシュタグを大量に付ける |

## API

AT Protocol は認証(アプリパスワード/OAuth)、レコード作成(`app.bsky.feed.post`)、画像のアップロード(blob)で投稿できる。詳細: [20-api/07-other-apis](../20-api/07-other-apis.md)。
外部ツールに接続するときは、本来のパスワードではなく**アプリパスワード**を発行して使います(⚪)。キーやパスワードを公開リポジトリに書かないでください。

## 収益化

公式のプログラムはなし。誘導先(note・YouTube・書籍・サポート)を用意する([クリエイターエコノミー](../10-creator-economy/README.md))。

## 書き出し

[export-presets](../01-common/export-presets.md)(従来の 1MB 上限に合わせる)。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 画像がアップロードできない | 1MB 以下に圧縮して再試行(上限は 🟡 #39) |
| ハンドルを独自ドメインにしたらドメインの更新を忘れた | ドメインの期限を管理。失効するとハンドルが使えなくなるおそれ(⚪) |
| 外部ツールに本来のパスワードを入れた | パスワードを変更し、アプリパスワードを使う |
| フォローが少なくタイムラインが静か | 話題のフィード・スターターパックからフォローを増やす |

## 注意点

- 分散型でも、投稿は基本的に**公開**です。個人情報を書かないでください([個人情報](../01-common/privacy-and-personal-info.md))。
- 仕様の数値は二次資料です。投稿できないときは公式アプリの表示を優先してください。

## チェックリスト

- [ ] ハンドルとプロフィールを設定した
- [ ] 2段階認証を有効にした
- [ ] 自己紹介の投稿を固定した
- [ ] 画像は 1MB 以下・代替テキスト付き
- [ ] 外部ツールはアプリパスワードで接続した

## 関連ページ / 次に読む

- [02-line-official-account](02-line-official-account.md) / [03-twitch](03-twitch.md)
- [ソーシャルリスニング](../01-common/social-listening.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.bsky.app/ | 2026-11-03 | 公式開発者文書(本文未取得。リダイレクト先に接続不可) |
| https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/embed/images.json | 2026-11-03 | 画像 lexicon(検索要約 🟡) |
| https://www.engadget.com/social-media/bluesky-adds-3-minute-video-uploads-and-inbox-management-features-220317950.html | 2026-11-03 | 3分動画の報道 🟡 |
| https://engadget.com/2244638/bluesky-now-supports-10-minute-videos-larger-file-sizes/ | 2026-11-03 | 10分動画の報道 🟡 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(用語、始め方・独自ドメインの手順、動画上限の経緯 🟡、投稿例、よくある失敗、チェックリスト、出典を追加) |
