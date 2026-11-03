---
title: Instagram 投稿ルート
platform: instagram
topic: posting
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/instagram-platform/content-publishing.md
---

# Instagram 投稿ルート

> **このページで分かること**: Instagram の投稿形式(フィード・カルーセル・リール・ストーリーズ・ライブ)の違いと、フィード投稿・カルーセル投稿の具体的な手順。
>
> **対象**: 初心者  **先に読むページ**: [01-account-setup](01-account-setup.md)

## 概要

Instagram には目的の違う投稿形式がいくつもあります。初心者は「全部やろう」とせず、**役割を決めて1〜2種類から始める**のが続けるコツです(⚪)。

| 形式 | 何が残るか | 主な役割(⚪ 経験則) | 詳しい手順 |
|---|---|---|---|
| フィード(1枚) | プロフィールに残る | 作品・世界観の紹介 | このページ |
| カルーセル | プロフィールに残る | 解説・手順・まとめ。スワイプで読ませる | このページ |
| リール | プロフィールとリールタブに残る | フォロワー以外への発見・拡散 | [12-reels](12-reels.md) |
| ストーリーズ | **24時間で消える** ✅(ハイライトに保存すると残る) | 日常・告知・質問 | [13-stories-and-highlights](13-stories-and-highlights.md) |
| ライブ | 配信後にアーカイブ可(⚪) | リアルタイムの交流・発表 | [live-streaming](../01-common/live-streaming.md) |

ストーリーズが24時間で消えることは API 文書に明記されています ✅([IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md))。

## 用語

| 用語 | 意味 |
|---|---|
| feed(フィード) | フォロワーのホーム画面に流れる通常の投稿。プロフィールのグリッド(一覧)に並ぶ |
| carousel(カルーセル) | 1つの投稿に複数の画像・動画を入れ、横にスワイプして見せる形式 |
| caption(キャプション) | 投稿に付ける説明文 |
| tag(タグ付け) | 写っている人・関係者のアカウントを画像上に表示する機能 |
| collab post(コラボ投稿) | 共同投稿者を招待し、相手のプロフィールにも同じ投稿を表示する機能 |
| grid(グリッド) | プロフィール画面の投稿一覧 |
| scheduled post(予約投稿) | 日時を指定して自動で公開する機能 |

## 手順 / 仕様

### 主な数値(公式に確認できたもの)

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| カルーセルの最大枚数 | **20件**(画像と動画の混在可。API) | ✅ | [Content Publishing](https://developers.facebook.com/documentation/instagram-platform/content-publishing.md) |
| カルーセルの最大枚数(アプリ) | 20件に拡大(2024年(皇紀2684年・令和6年)8月の報道) | 🟡 #10 | [PetaPixel](https://petapixel.com/2024/08/09/instagram-users-can-now-share-20-photos-videos-in-a-post-carousel-photodump) |
| カルーセルの切り抜き | **最初の画像の比率**に全体が合わせられる(API) | ✅ | [Content Publishing](https://developers.facebook.com/documentation/instagram-platform/content-publishing.md) |
| リールをカルーセルに入れる | **不可**(API) | ✅ | [IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md) |
| キャプション | 2,200字(API) | ✅ | 同上 |
| コラボ(共同投稿者) | **最大3人**。フィード画像・リール・カルーセルのみ、ストーリーズ不可(API) | ✅ | 同上 |
| 位置情報・人物タグ | 設定可(API の `location_id`・`user_tags`) | ✅ | 同上 |

画像・動画のサイズは [03-media-specs](03-media-specs.md)、文字数とハッシュタグは [04-text-hashtags](04-text-hashtags.md) を参照してください。

### フィード投稿(1枚)の手順

⚪ ボタン名はアプリの版により変わる可能性があります。

1. 画面下の「＋」(作成)をタップし、「投稿」を選びます。
2. カメラロールから写真を1枚選びます。
3. 比率を選びます。縦長 4:5 にするには、プレビュー左下の比率ボタンで調整します(⚪)。**重要な部分が端で切れていないか**確認します。
4. 「次へ」でフィルター・明るさなどを調整します。加工しすぎると色味の統一が崩れるので、毎回同じ設定にするのがおすすめです(⚪)。
5. 「次へ」でキャプションを入力します([04-text-hashtags](04-text-hashtags.md))。
6. 必要に応じて設定します。
   - **人物をタグ付け**: 写っている人・協力者
   - **場所を追加**: 店舗・イベント会場
   - **コラボ**: 共同で作った相手を招待(相手の承認が必要 ⚪)
   - **代替テキスト**: 「詳細設定」→「代替テキストを書く」([05-alt-text](05-alt-text.md))
   - **AI 情報ラベル**: AI で生成・大きく編集した画像の場合([10-policies](10-policies.md))
   - **ブランドコンテンツ(タイアップ投稿)ラベル**: 企業案件の場合([07-monetization](07-monetization.md))
7. 「シェア」で公開します。

### カルーセル投稿の手順

1. 「＋」→「投稿」で、写真選択画面の「複数を選択」をオンにします(⚪)。
2. 表示したい**順番どおりに**タップして選びます(番号が付きます)。
3. 比率は**1枚目に合わせて全体がそろう**ため、全枚数を同じ比率で作っておきます ✅。
4. 1枚ずつ編集・**代替テキスト**の入力ができます。図解の場合は画像内の文字の要点を書きます。
5. キャプション・タグ・場所を設定して「シェア」します。

カルーセルの構成例(⚪ 経験則):

| 枚目 | 役割 |
|---|---|
| 1 | 表紙。結論か問い(「初心者がやりがちな失敗3つ」) |
| 2〜(n-1) | 1枚に1つの要点。文字は大きく、余白を多めに |
| 最後 | まとめと行動の案内(「保存して見返してね」「質問はコメントへ」) |

### 予約投稿・下書き

- アプリの詳細設定、または **Meta Business Suite** で日時を指定して予約できます(⚪ 提供範囲・最大の予約期間は要確認)。
- 書きかけは下書きに保存できます(⚪)。
- 外部ツールや API で自動投稿する場合は [20-api/03-instagram-graph-api](../20-api/03-instagram-graph-api.md) を参照してください。API には**24時間あたりの公開上限**があります ✅。

### 投稿後に編集できること / できないこと

| 操作 | 可否 | 確度 |
|---|---|---|
| キャプション・タグ・場所・代替テキストの編集 | 可 | ⚪ |
| 画像の差し替え・比率の変更 | 原則不可(削除して再投稿) | ⚪ |
| カルーセルの1枚だけ削除 | 可能とされる(枚数が残る場合) | ⚪ 要確認 |
| アーカイブ(非表示にして保管) | 可 | ⚪ |

## 具体例

**良いカルーセルのキャプション(料理アカウント)**

```
材料3つで作れる朝ごはん、どれが好き?
① 卵とトーストのオープンサンド
② バナナヨーグルト
③ おにぎりと味噌汁
作り方は2枚目から。保存しておくと忙しい朝に便利です。
```

**悪い例**: 1枚目が小さな文字でぎっしり。スマートフォンでは読めず、スワイプされません。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| カルーセルの2枚目以降が切れた | 1枚目の比率に全体がそろうため、全枚数を同じ比率(例: 4:5)で作る |
| 投稿後に画像のミスに気づいた | 画像は差し替えできない前提で、公開前にスマートフォンで拡大確認する。誤りが大きければ削除して再投稿し、訂正をキャプションに書く |
| 毎日投稿を目標にして続かなかった | 週2〜3回など**続けられる頻度**から始め、週次で見直す([content-planning](../01-common/content-planning.md)) |
| リールをカルーセルに混ぜようとした | リールはカルーセルに入れられない ✅。動画をカルーセルの1枚として入れることは可能 |

## 注意点

- 運用頻度の目安(⚪ 経験則): フィード週2〜3回、ストーリーズ週数回、リール週1回〜。**質と継続を優先**します。
- 他人の写真・イラストを無断で使わない([image-sources-and-copyright](../01-common/image-sources-and-copyright.md))。
- 第三者の顔や車のナンバー、自宅が特定できる景色が写り込んでいないか確認します([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。

## チェックリスト

- [ ] 形式(フィード / カルーセル / リール / ストーリーズ)の役割を決めた
- [ ] 比率をそろえた(カルーセルは全枚数)
- [ ] キャプションの1行目に要点を書いた
- [ ] 代替テキストを入れた
- [ ] タグ付け・コラボ・場所を確認した
- [ ] 案件なら「タイアップ投稿」ラベル、AI 生成なら AI 情報ラベル

## 関連ページ / 次に読む

- [12-reels](12-reels.md)、[13-stories-and-highlights](13-stories-and-highlights.md)
- [03-media-specs](03-media-specs.md)、[04-text-hashtags](04-text-hashtags.md)、[05-alt-text](05-alt-text.md)
- [posting-workflow](../01-common/posting-workflow.md)、[content-planning](../01-common/content-planning.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/content-publishing.md | 2026-11-03 | ✅ カルーセル20件、切り抜き |
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | ✅ ストーリーズ24時間、コラボ最大3、リールはカルーセル不可 |
| https://petapixel.com/2024/08/09/instagram-users-can-now-share-20-photos-videos-in-a-post-carousel-photodump | 2026-11-03 | 🟡 アプリのカルーセル20枚(報道) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(形式の役割、フィード・カルーセルの手順、公式数値の表、予約・編集、具体例、よくある失敗、チェックリスト)。リール・ストーリーズの手順を新規ページ 12・13 に分割 |
