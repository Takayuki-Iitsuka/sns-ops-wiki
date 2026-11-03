---
title: Instagram リールの作り方と投稿手順
platform: instagram
topic: posting
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md
  - https://developers.facebook.com/documentation/instagram-platform/changelog.md
  - https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md
---

# Instagram リールの作り方と投稿手順

> **このページで分かること**: リール(縦型の短い動画)の企画・撮影・編集・投稿の手順、カバー画像、音源、トライアルリール、リールの指標の見方。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [02-posting](02-posting.md)、[video-basics](../01-common/video-basics.md)

## 概要

リール(Reels)は、Instagram の縦型の短尺動画です。フォロワー以外にも表示されやすく、**新しい人に見つけてもらう入口**として使われます(⚪ 経験則)。

初心者がつまずきやすいのは次の3点です。

1. **最初の数秒**で何の動画か伝わらず、すぐにスワイプされる
2. 文字やボタンが**画面の端で隠れる**
3. **音楽の権利**を気にせず使い、ミュートや収益化不可になる

## 用語

| 用語 | 意味 |
|---|---|
| Reels(リール) | Instagram の縦型短尺動画 |
| cover(カバー画像) | リール一覧やプロフィールに表示される表紙画像 |
| original audio(オリジナル音源) | 自分で録音した音声。他の人が使えるようになる場合がある |
| trial reels(トライアルリール) | フォロワーには見せず、**フォロワー以外**にだけ試験的に表示するリール |
| remix(リミックス) | 他の人のリールに自分の映像を組み合わせる機能 |
| skip rate(スキップ率) | 冒頭3秒以内に飛ばされた割合 |
| safe zone(安全領域) | 画面上の文字やボタンに隠れない中央部分 |

## 手順 / 仕様

### 主な仕様

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| 推奨比率 | **9:16**(切れや余白を避けるため) | ✅ | [IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md) |
| 長さ(API) | **3秒以上、最大15分** | ✅ | 同上 |
| 容量(API) | 最大 **300MB** | ✅ | 同上 |
| フレームレート(API) | 23〜60 FPS | ✅ | 同上 |
| 長さ(アプリ) | 2025年(皇紀2685年・令和7年)1月に最大3分へ延長と報道。その後20分とする二次資料もあり不一致 | 🟡 #18 | [Engadget](https://www.engadget.com/social-media/instagram-swoops-in-with-3-minute-reels-and-rectangular-profile-grids-as-the-tiktok-ban-gets-real-201316339.html) |
| カバー画像 | JPEG・8MB 以下・sRGB。9:16 推奨。9:16 でない画像は**中央の 9:16** が使われ、フィードに表示する場合は**中央の 1:1** が使われる | ✅ | [IG User Media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md) |
| 音源名の変更 | オリジナル音源の名前は**1回だけ**変更できる | ✅ | 同上 |
| カルーセルへの追加 | 不可 | ✅ | 同上 |

詳しい書き出し設定は [03-media-specs](03-media-specs.md) と [export-presets](../01-common/export-presets.md) を参照してください。

### 1. 企画する

1. **1本で伝えることを1つ**に絞ります(例: 「卵焼きをきれいに巻くコツ」)。
2. 冒頭(最初の1〜3秒)で結論や完成形を見せます(⚪)。冒頭3秒の離脱は「スキップ率」としてインサイトで確認できます ✅。
3. 音なしでも内容が分かるよう、**字幕・テロップ**を入れます(⚪)。
4. 最後に「保存」「フォロー」「プロフィールのリンク」など次の行動を案内します。

### 2. 撮影・編集する

1. スマートフォンを**縦向き**にして撮影します。
2. 明るい場所で撮り、手ぶれを抑えます(三脚・スマートフォンスタンドが便利 ⚪)。
3. アプリ内の編集機能、または外部の動画編集アプリで編集します([video-editing-apps](../01-common/video-editing-apps.md))。
4. 文字は画面の**中央寄り**に置きます。下部はキャプション、右側はいいね・コメントのボタンで隠れやすいためです(⚪ 安全領域の正確な寸法は公式未確認)。

### 3. 投稿する(アプリ)

⚪ ボタン名は変わる可能性があります。

1. 「＋」→「リール」を選びます。
2. 撮影するか、カメラロールから動画を選びます(複数の動画をつなげることも可能 ⚪)。
3. **音源**を追加します。音楽ライブラリの曲、または撮影した元の音声を使います([music-and-licensing](../01-common/music-and-licensing.md))。
4. テキスト・字幕・ステッカーを追加し、表示時間を調整します。
5. 「次へ」で**キャプション**、ハッシュタグ、人物タグ、場所を入力します。
6. **カバー画像**を選びます。動画内の1コマか、別に作った画像を使えます。プロフィールのグリッドで切れないよう、重要な文字は中央に置きます。
7. 必要に応じて次を設定します。
   - **フィードにもシェア**(オフにするとリールタブのみ ✅ API の `share_to_feed`)
   - **コラボ**(最大3人 ✅)
   - **トライアル**(下記)
   - **AI 情報ラベル**、**タイアップ投稿ラベル**
8. 「シェア」で公開します。

### 4. トライアルリールを使う

トライアルリールは、**フォロワー以外にだけ**表示して反応を試し、後から通常のリールとして公開できる仕組みです ✅(API の `trial_params`。[Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md) 2025年12月3日)。

- 「いつもと違う企画を試したい」「フォロワーの反応を気にせず試したい」ときに使います(⚪)。
- アプリでの利用条件(フォロワー数など)は ⚪ 要確認です。

### 5. 投稿後に見る指標

| 指標 | 意味 | 確度 |
|---|---|---|
| 再生数(views) | Instagram で再生された回数 | ✅ |
| 平均再生時間 | 1回あたりの平均視聴時間 | ✅ |
| スキップ率 | **冒頭3秒以内に飛ばされた割合**(推定値・開発中の指標) | ✅ |
| 保存・シェア | 役に立った・人に教えたいと思われたか | ✅ |
| Facebook での再生 | Facebook にクロスポストした場合の再生 | ✅ |

出典: [IG Media Insights](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md)。詳しくは [08-analytics](08-analytics.md)。

## 具体例

**良い構成(15〜30秒の料理リール ⚪)**

| 秒数 | 内容 |
|---|---|
| 0〜2秒 | 完成品のアップ + テロップ「巻きすなしで卵焼き」 |
| 2〜20秒 | 手順を3つ。各ステップに番号付きテロップ |
| 20〜25秒 | 失敗しやすい点を1つ |
| 25〜30秒 | 「保存して週末に作ってみて」 |

**悪い例**: 冒頭10秒が挨拶と自己紹介。何の動画か分かる前に離脱されます。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| テロップがボタンやキャプションに隠れた | 文字を中央寄りに。投稿前にプレビューで確認 |
| 有名な曲を自分で編集アプリに入れたら音が消えた | アプリ内の音楽ライブラリか、権利を確認した音源を使う([music-and-licensing](../01-common/music-and-licensing.md)) |
| カバーがグリッドで切れて読めない | 文字は中央に。グリッドの表示比率は [03-media-specs](03-media-specs.md) |
| 他人の動画を切り抜いて投稿した | 無断転載は権利侵害・収益化対象外になり得る。自分で撮影した素材を使う([10-policies](10-policies.md)) |
| 横長動画をそのまま投稿し、上下が黒い帯に | 9:16 で撮影・書き出しする |

## 注意点

- 2026年(皇紀2686年・令和8年)7月30日以降、著作権のある音源を含む動画や、ダウンロードを許可していないリールは、API から動画ファイルの URL が返されなくなりました ✅([Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog.md))。アプリにも「リールのダウンロードを許可する」設定があります。
- 長いリールは推奨(おすすめ表示)に不利になるとする二次資料がありますが、公式の基準は未確認です(⚪)。
- 子どもや第三者が写る場合は、事前の同意と写り方に配慮します。

## チェックリスト

- [ ] 1本1テーマ、冒頭で結論
- [ ] 9:16 で撮影・書き出し
- [ ] 字幕・テロップを中央寄りに
- [ ] 音源の権利を確認
- [ ] カバー画像を設定(中央に重要要素)
- [ ] キャプション・ハッシュタグ・タグ付け
- [ ] 案件ならタイアップ投稿ラベル、AI 生成なら AI 情報ラベル

## 関連ページ / 次に読む

- [13-stories-and-highlights](13-stories-and-highlights.md)、[08-analytics](08-analytics.md)
- [video-basics](../01-common/video-basics.md)、[video-specs-comparison](../01-common/video-specs-comparison.md)、[mobile-viewing-optimization](../01-common/mobile-viewing-optimization.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md | 2026-11-03 | ✅ リール仕様、カバーの切り抜き、`share_to_feed`、音源名、コラボ |
| https://developers.facebook.com/documentation/instagram-platform/changelog.md | 2026-11-03 | ✅ トライアルリール、ダウンロード・著作権保護 |
| https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights.md | 2026-11-03 | ✅ リールの指標 |
| https://www.engadget.com/social-media/instagram-swoops-in-with-3-minute-reels-and-rectangular-profile-grids-as-the-tiktok-ban-gets-real-201316339.html | 2026-11-03 | 🟡 アプリのリール3分(報道) |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成(02-posting から分割。リールの企画・撮影・投稿手順、仕様、トライアルリール、指標) |
