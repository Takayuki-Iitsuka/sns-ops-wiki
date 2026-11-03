---
title: Facebook リール・動画・ストーリーズ・ライブ
platform: facebook
topic: posting
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/video-api/guides/reels-publishing.md
  - https://creators.facebook.com/tools/reels
  - https://creators.facebook.com/tools/crossposting
  - https://creators.facebook.com/tools/live
---

# Facebook リール・動画・ストーリーズ・ライブ

> **このページで分かること**: Facebook でリール・通常動画・ストーリーズ・ライブを投稿する手順、Instagram からのクロスポストの設定、ライブの開始条件。
>
> **対象**: 初心者  **先に読むページ**: [01-setup-and-posting](01-setup-and-posting.md)、[02-media-specs](02-media-specs.md)

## 概要

Facebook の動画には、目的の違う形式があります(⚪ 役割は経験則)。

| 形式 | 役割 | 主な条件 |
|---|---|---|
| リール | フォロワー以外への発見 | 9:16 推奨 ✅ |
| 通常動画 | 講座・記録など長めの内容 | 16:9 が一般的 ⚪ |
| ストーリーズ | 日常・告知(24時間 ⚪) | 9:16 |
| ライブ | リアルタイムの交流 | **作成から60日以上・フォロワー100人以上** ✅ |

Facebook でいう「リール」は、**短尺・長尺、縦・横を問わない動画**を指し、**3秒以上で長さの上限はない**とされています ✅([Meta for Creators](https://creators.facebook.com/tools/reels)、2023年(皇紀2683年・令和5年)ごろの記載)。

## 用語

| 用語 | 意味 |
|---|---|
| Reels(リール) | Facebook の動画形式(縦型が中心) |
| crosspost(クロスポスト) | Instagram の投稿を Facebook にも同時に出すこと |
| Live(ライブ) | リアルタイム配信 |
| encoder(エンコーダー) | パソコンのカメラ映像を配信用に変換するソフト(配信ソフト) |
| Live With | ゲストを招いて一緒に配信する機能 |
| stream key(ストリームキー) | 配信ソフトとページをつなぐ秘密の文字列。**他人に見せない** |

## 手順 / 仕様

### リールを投稿する(アプリ ⚪ ボタン名は変わる可能性)

1. ページに切り替え、「リール」または「投稿を作成」→「リール」を選びます。
2. 動画を撮影するか、カメラロールから選びます。
3. 音楽・テキスト・字幕を追加します。音源の権利に注意します([music-and-licensing](../01-common/music-and-licensing.md))。
4. 説明文(キャプション)とハッシュタグを入力します。
5. 公開範囲を確認します。ページのリールは公開です ✅(API では「公開」のみ)。
6. 「シェア」で公開します。

API で投稿する場合の条件(✅ [Reels Publishing API](https://developers.facebook.com/documentation/video-api/guides/reels-publishing.md)):

- 投稿できるのは**ページのみ**。長さは **3〜90秒**、ページあたり**24時間で30件**まで。
- 他のページを**コラボレーター**として招待し、相手のページにも表示できる。

### Instagram からクロスポストする

Instagram のプロアカウントから、リール・投稿・ストーリーズを Facebook にも自動で出せます ✅([Meta for Creators](https://creators.facebook.com/tools/crossposting))。

1. Facebook と Instagram の両方のアカウントを用意します。
2. Instagram のプロフィール → 右上メニュー →「設定とプライバシー」を開きます(⚪)。
3. 「他のアプリとシェア」などの項目で Facebook を選び、**ストーリーズ・投稿・リールごとに**クロスポストをオンにします ✅。

注意(⚪): Facebook と Instagram は見ている人が違います。ハッシュタグの量や文体を Facebook 向けに調整すると反応が変わることがあります。

### 通常の動画を投稿する

1. 「投稿を作成」→「写真・動画」で動画を選びます(⚪)。
2. **タイトル**と説明を入力します。講座や記録ならタイトルに内容と日付を入れます。
3. サムネイル(表紙)を選びます。
4. 字幕を付けます(自動字幕を使う場合は誤りを修正 ⚪)。
5. 公開または予約します。

### ストーリーズを投稿する(⚪)

1. ページのホームで「ストーリーズを作成」を選びます。
2. 写真・動画を選び、文字やスタンプを追加します。
3. 「シェア」で公開します。Instagram からのクロスポストも可能です ✅。

### ライブ配信をする

ライブの開始条件(✅ [Meta for Creators](https://creators.facebook.com/tools/live)、2022年(皇紀2682年・令和4年)ごろの記載):

| 条件 | 値 |
|---|---|
| アカウントの作成からの期間 | **60日以上** |
| フォロワー数 | **100人以上** |
| 配信先 | ページ・グループ・プロフィール・イベント |
| 方法 | スマートフォンのアプリ、またはカメラ+配信ソフト(エンコーダー) |

スマートフォンでの手順(⚪):

1. ページで「ライブ動画」を選びます。
2. タイトルと説明を入力し、公開範囲を確認します。
3. コメントのモデレーション(管理)設定を確認します。
4. 「ライブ動画を開始」を押します。
5. 終了後、録画の公開・削除・編集を選びます。

パソコンで配信ソフトを使う場合は、**ストリームキーを他人に見せない**ようにします(画面共有・スクリーンショットに注意)。詳しくは [live-streaming](../01-common/live-streaming.md)。

## 具体例

**地域のイベントでの使い分け(例)**

| 時期 | 形式 | 内容 |
|---|---|---|
| 2週間前 | リール | 前回の様子を30秒で紹介 |
| 1週間前 | ストーリーズ | カウントダウン、準備の様子 |
| 当日 | ライブ | 開会のあいさつを配信 |
| 翌日 | 通常動画 | 記録映像(16:9)とお礼の投稿 |

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| ライブのボタンが出ない | 作成60日以上・フォロワー100人以上の条件を確認 ✅ |
| ストリームキーを画面共有で見せてしまった | すぐにキーを再発行(リセット)する |
| Instagram のハッシュタグだらけの文が Facebook にそのまま出た | クロスポスト時に文面を調整するか、Facebook 用に別投稿 |
| 外部ツールからのリールが失敗した | 3〜90秒、9:16、1日30件以内を確認 ✅ |
| 字幕なしで、音を出せない人に伝わらなかった | 字幕を付ける |

## 注意点

- 長さ・条件は**アプリと API で異なる**ことがあります。
- 子どもや来場者が映る場合は、事前に撮影・配信の告知と同意を取ります([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。
- 収益化(Stars・広告など)は [04-monetization](04-monetization.md)。

## チェックリスト

- [ ] 形式ごとの役割を決めた
- [ ] リールは 9:16、字幕付き
- [ ] 音源の権利を確認
- [ ] クロスポストの対象(ストーリーズ・投稿・リール)を選んだ
- [ ] ライブの条件(60日・100人)を満たしている
- [ ] ストリームキーを安全に管理

## 関連ページ / 次に読む

- [02-media-specs](02-media-specs.md)、[03-engagement-and-groups](03-engagement-and-groups.md)、[04-monetization](04-monetization.md)
- [video-basics](../01-common/video-basics.md)、[live-streaming](../01-common/live-streaming.md)
- Instagram のリール: [03-instagram/12-reels](../03-instagram/12-reels.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/video-api/guides/reels-publishing.md | 2026-11-03 | ✅ API でのリール投稿(ページのみ、3〜90秒、30件/24時間、コラボレーター) |
| https://creators.facebook.com/tools/reels | 2026-11-03 | ✅ リールの定義(3秒以上・上限なし) |
| https://creators.facebook.com/tools/crossposting | 2026-11-03 | ✅ Instagram からのクロスポスト |
| https://creators.facebook.com/tools/live | 2026-11-03 | ✅ ライブの条件(60日・100人) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(リール・通常動画・ストーリーズ・ライブの投稿手順、クロスポスト、ライブの条件) |
