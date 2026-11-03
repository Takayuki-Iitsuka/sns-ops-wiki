# 今後の追加候補

> **このページで分かること**: まだページがないサービスと、追加するときの手順。
>
> **対象**: このナレッジベースに新しいサービスのページを追加したい人。

## 追加候補のサービス

| サービス | 優先度 | どんなサービスか(⚪ 一般知識) | メモ |
|---|---|---|---|
| Pinterest | 低 | 画像を「ピン」として保存・検索する、検索エンジンに近い使われ方のサービス | 縦長 2:3 が一般的 ⚪ |
| Mastodon / Misskey | 低 | 運営者の異なるサーバー(インスタンス)同士がつながる分散型 SNS | 日本語圏のインスタンスがある。仕組みは [Bluesky](../09-other-services/01-bluesky.md) の「分散型」の説明も参考 |
| ニコニコ動画 | 低 | 日本語圏の動画・ライブ配信サービス。画面上を流れるコメントが特徴 | ライブ配信の共通事項は [live-streaming](../01-common/live-streaming.md) |
| Substack / Medium | 低 | ニュースレター・記事の配信サービス | 共通事項は [newsletter-and-email](../01-common/newsletter-and-email.md) に記載済み。サービス別ページは未作成 |
| Lemon8 | 低 | 画像中心の投稿サービス | — |
| Spotify for Creators | 低 | ポッドキャストの配信 | 共通事項は [podcast-and-audio](../01-common/podcast-and-audio.md) に記載済み |

> 作成済み: [Discord](../09-other-services/04-discord.md)、[X Subscriptions](../02-x/12-subscriptions.md)(2026年(皇紀2686年・令和8年)11月3日)。ライブ配信・ニュースレター・ポッドキャスト・コミュニティ運営・ソーシャルリスニング・多言語・動画編集アプリは、サービス横断の共通ページとして [01-common](../README.md) に作成済みです。

## 追加の手順

1. `docs/NN-<service>/` のフォルダを作る(`NN` は空いている番号、`<service>` は小文字 kebab-case)。
2. [page-template](../00-meta/page-template.md) をコピーして、`README.md`(索引)と、初期設定・投稿・画像/動画仕様・文章・反応・収益化・分析・規約のページを作る。既存のサービスのフォルダ(例: [05-youtube](../05-youtube/README.md))の構成を参考にする。
3. 数値・条件には確度ラベルと出典を付ける。確認できない事項は [verification-queue](../00-meta/verification-queue.md) に最大番号の次から登録する。
4. [画像の仕様比較](../01-common/image-specs-comparison.md)・[動画の仕様比較](../01-common/video-specs-comparison.md)・[収益化の比較](../01-common/monetization-comparison.md)の表に列や行を追加する。
5. [docs の索引](../README.md) と [サービスの選び方](../01-common/choosing-platforms.md) に追記する。
6. `python3 -I scripts/check_wiki.py` を実行してエラーが 0 であることを確認する。
