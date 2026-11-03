---
title: Instagram ストーリーズとハイライト
platform: instagram
topic: posting
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md
---

# Instagram ストーリーズとハイライト

> **このページで分かること**: 24時間で消えるストーリーズの投稿手順、スタンプ(ステッカー)の使い方、ストーリーズをプロフィールに残す「ハイライト」の作り方。
>
> **対象**: 初心者  **先に読むページ**: [02-posting](02-posting.md)

## 概要

ストーリーズ(Stories)は、**24時間で自動的に消える**縦型の投稿です ✅([IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md))。気軽に投稿でき、質問・アンケートなどの**スタンプでフォロワーと交流**できます。

消えてしまう投稿を、テーマ別にプロフィールへ残しておく機能が**ハイライト**です。ハイライトは「自己紹介」「よくある質問」「メニュー」など、**初めて来た人向けの案内板**として使えます(⚪)。

## 用語

| 用語 | 意味 |
|---|---|
| Stories(ストーリーズ) | 24時間で消える縦型の投稿 |
| sticker(スタンプ、ステッカー) | ストーリーズに貼る機能部品。質問・アンケート・リンク・メンションなど |
| link sticker(リンクスタンプ) | 外部サイトへのリンクを貼るスタンプ |
| Close Friends(親しい友達) | 選んだ人だけにストーリーズを見せるリスト |
| archive(アーカイブ) | 消えたストーリーズが自分だけに見える形で保存される場所 |
| highlight(ハイライト) | ストーリーズをプロフィールに残す機能 |
| highlight cover(ハイライトのカバー) | ハイライトの丸いアイコン画像 |

## 手順 / 仕様

### 主な仕様

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| 表示期間 | **24時間** | ✅ | [IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md) |
| 推奨比率 | **9:16** | ✅ | 同上 |
| 画像(API) | JPEG、最大 8MB、sRGB | ✅ | 同上 |
| 動画(API) | 3秒以上・**最大60秒**、最大 100MB、MOV/MP4 | ✅ | 同上 |
| 動画(アプリ) | 1クリップ最大60秒、長い動画は分割されるとする資料 | 🟡 | [Kapwing](https://www.kapwing.com/resources/how-to-post-60-second-instagram-story/) |
| API からのスタンプ | リンク・アンケート・位置情報スタンプは**API では付けられない**(メンションは可) | ✅ | [IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md) |
| 代替テキスト(API) | ストーリーズは**非対応** | ✅ | 同上 |
| コラボ(API) | ストーリーズは**非対応** | ✅ | 同上 |
| インサイトの保存期間 | ストーリーズの指標は**24時間のみ**取得可(ハイライトに入れると後でも取れる場合あり) | ✅ | [IG Media Insights](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md) |

### ストーリーズの投稿手順(アプリ)

⚪ ボタン名は変わる可能性があります。

1. ホーム画面左上の自分のアイコン、または「＋」→「ストーリーズ」を選びます。
2. その場で撮影するか、カメラロールから写真・動画を選びます。
3. 文字・手描き・スタンプを追加します。文字は**上下の端を避けて**配置します。上部はアカウント名、下部は返信欄で隠れるためです(⚪)。
4. 公開範囲を選びます。
   - **ストーリーズ**: 通常の公開範囲(公開アカウントなら誰でも)
   - **親しい友達**: 選んだ人だけ(⚪)
5. 「シェア」で公開します。

### よく使うスタンプ

| スタンプ | 使い方の例(⚪) |
|---|---|
| 質問 | 「次に作ってほしいレシピは?」→ 回答を次の投稿のネタにする |
| アンケート(投票) | 「AとBどちらの色が好き?」 |
| クイズ | 「この道具の名前は?」 |
| リンク | ブログ記事・予約ページ・通販ページへ誘導。クリック数は「リンクのクリック」で計測 ✅ |
| メンション | 協力者・取引先のアカウントを紹介 |
| 位置情報 | 店舗・イベント会場 |
| カウントダウン | 発売日・イベント開始の告知 |

リンクのクリック数(`link_clicks`)は、2026年(皇紀2686年・令和8年)6月22日に API 指標に追加されました ✅([Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md))。

### ハイライトの作り方

1. プロフィール画面で「＋(新規)」を押すか、公開中のストーリーズ右下の「ハイライト」を押します(⚪)。
2. 追加したいストーリーズを選びます(過去のものは**アーカイブ**から選べます。アーカイブ保存は設定で有効にしておきます ⚪)。
3. ハイライトの名前を付けます。プロフィールで途中まで表示されるため、**短い名前**にします(⚪)。
4. カバー画像を選びます。色やアイコンをそろえるとプロフィールが整って見えます。
5. 後から「ハイライトを編集」で追加・削除・並べ替えができます(⚪)。

ハイライトの構成例(⚪):

| ハイライト名 | 中身 |
|---|---|
| はじめに | 自己紹介、アカウントで発信していること |
| よくある質問 | 質問スタンプへの回答をまとめたもの |
| メニュー / 作品 | 商品・料金・作品の一覧 |
| お客様の声 | 許可を得たレビューの紹介 |
| お知らせ | 定休日・イベント情報(古い情報は削除) |

## 具体例

**良い例(地域の雑貨店の週末告知)**

1. 1枚目: 新商品の写真 +「今週末から販売」
2. 2枚目: アンケートスタンプ「どの色が気になる?」
3. 3枚目: カウントダウンスタンプ「販売開始まで」
4. 4枚目: 位置情報スタンプ + 営業時間

**避けたい例**: 文字だけの画像を10枚以上連続で投稿する。途中で離脱されやすく、伝えたいことが埋もれます(⚪)。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 消えた後に「あの投稿をまた見たい」と言われた | ハイライトに保存する。アーカイブ保存を有効にしておく |
| 質問スタンプの回答をそのまま公開して個人名が出た | 回答を共有する際は名前が表示されるか確認し、必要なら画像化して名前を消す(⚪) |
| ハイライトに古い価格や終了したイベントが残っている | 月1回ハイライトを見直す([11-checklist](11-checklist.md)) |
| リンクスタンプの先が分からず押されない | 「レシピ全文はこちら」など、リンク先の内容を文字で添える |
| 外部ツールで予約したストーリーズにスタンプが付かない | API ではリンク・アンケートなどのスタンプは付けられない ✅。スタンプが必要な回はアプリから投稿 |

## 注意点

- ストーリーズの**返信数**は、日本のユーザーからの返信が API の集計に含まれません(日本は2021年(皇紀2681年・令和3年)4月14日から)✅([IG Media Insights](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md))。アプリ内の受信箱で確認します。
- 閲覧者が少ない(5未満の)ストーリーズは API でインサイトが返されません ✅。
- 自宅周辺や現在地がリアルタイムで分かる投稿は避け、**時間をずらして投稿**するのが安全です([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。

## チェックリスト

- [ ] 文字は上下の端を避けて配置した
- [ ] スタンプ(質問・アンケート・リンク)を目的に合わせて選んだ
- [ ] リンク先の説明を文字で添えた
- [ ] アーカイブ保存を有効にした
- [ ] ハイライトを「はじめに」「よくある質問」など目的別に整理した
- [ ] 古い情報のハイライトを削除した

## 関連ページ / 次に読む

- [12-reels](12-reels.md)、[06-engagement](06-engagement.md)、[08-analytics](08-analytics.md)
- [live-streaming](../01-common/live-streaming.md)、[link-in-bio-and-utm](../01-common/link-in-bio-and-utm.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | ✅ ストーリーズ24時間、画像・動画仕様、API のスタンプ制限 |
| https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md | 2026-11-03 | ✅ ストーリーズの指標、日本の返信の扱い |
| https://developers.facebook.com/documentation/instagram-platform/changelog.md | 2026-11-03 | ✅ `link_clicks` の追加 |
| https://www.kapwing.com/resources/how-to-post-60-second-instagram-story/ | 2026-11-03 | 🟡 アプリの1クリップ60秒 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(ストーリーズの投稿手順、スタンプ、ハイライトの作り方、仕様、よくある失敗) |
