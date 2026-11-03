---
title: Facebook 初期設定と投稿
platform: facebook
topic: setup
last_verified: 2026-11-03
confidence: 🟡
sources:
  - https://creators.facebook.com/tools/facebook-pages-and-profiles
  - https://creators.facebook.com/tools/meta-business-suite
  - https://developers.facebook.com/documentation/pages-api/overview.md
  - https://developers.facebook.com/documentation/pages-api/posts.md
---

# Facebook 初期設定と投稿

> **このページで分かること**: 発信の拠点を「Facebook ページ」と「プロフェッショナルモードのプロフィール」のどちらにするか、ページの作り方、管理者の権限、Meta Business Suite、テキスト・写真・リンク投稿の手順と予約投稿。
>
> **対象**: 初心者  **先に読むページ**: [README](README.md)、[account-security](../01-common/account-security.md)

## 概要

Facebook は**実名の個人アカウント(プロフィール)**が土台です。発信用には次の2つの選択肢があります ✅([Meta for Creators](https://creators.facebook.com/tools/facebook-pages-and-profiles))。

| 拠点 | 特徴 |
|---|---|
| **Facebook ページ** | 個人のプロフィールとは**別のフィード**を持つ。店舗・団体・ブランド・活動名での発信向け |
| **プロフェッショナルモード**(プロフィール) | 個人のプロフィールと**同じフィード**のまま、発信者向けツールを使う |

どちらでも、リール・ライブなどの制作ツール、おすすめ表示による発見、安全機能、**収益化(Stars・サブスクリプション・コンテンツ収益化など。資格による)**、プロフェッショナルダッシュボードが使えます ✅。

初心者向けの目安(⚪):

- 店・団体・活動名で発信し、**私生活と分けたい** → **ページ**
- 個人名で発信し、友達とのつながりも活かしたい → **プロフェッショナルモード**
- API で投稿・分析したい、Instagram と連携したい → **ページ**(Pages API はページ単位 ✅)

## 用語

| 用語 | 意味 |
|---|---|
| profile(プロフィール) | 実名の個人アカウント |
| Page(ページ) | 店舗・団体・ブランド・発信者のための公開ページ |
| professional mode(プロフェッショナルモード) | 個人プロフィールで発信者向け機能を使う設定 |
| Meta Business Suite(メタ ビジネススイート) | Facebook と Instagram の投稿・分析・受信箱・広告をまとめて管理するツール |
| Professional Dashboard(プロフェッショナルダッシュボード) | 成果・収益化の資格・コメント管理をまとめた画面 |
| task / role(タスク / 役割) | ページで誰が何をできるかの権限 |
| crosspost(クロスポスト) | 同じ投稿を Instagram と Facebook に同時に出すこと |
| link preview(リンクプレビュー) | URL を貼ると表示される画像・タイトルのカード(OGP で決まる) |

## 手順 / 仕様

### 1. ページを作る(⚪ メニュー名は変わる可能性)

1. 個人アカウントでログインし、メニューから「ページ」→「新しいページを作成」を選びます。
2. **ページ名**を入力します。店名・活動名など、検索されたときに分かる名前にします。
3. **カテゴリ**を選びます(例: 「レストラン」「アーティスト」「地域のお店」)。
4. **自己紹介(説明)**を書きます。誰向けに何を発信するかを1〜2文で。
5. 連絡先・ウェブサイト・住所・営業時間を入力します。**公開したくない情報は入れない**ようにします。
6. プロフィール写真とカバー写真を設定します([02-media-specs](02-media-specs.md))。
7. **ユーザーネーム**(URL)を設定します。名刺・チラシに載せる前に決めます。
8. 「ボタンを追加」で「メッセージを送信」「予約する」など、訪問者に取ってほしい行動のボタンを1つ選びます。

### 2. 管理者と権限を設定する

Pages API の文書では、ページでできる操作が**タスク**として分かれています ✅([Pages API Overview](https://developers.facebook.com/documentation/pages-api/overview.md))。

| タスク | できること |
|---|---|
| `CREATE_CONTENT` | ページとして投稿する |
| `MODERATE` | コメントへの返信・削除、リンクした Instagram への投稿・コメント・DM 対応 |
| `MESSAGING` | ページとしてメッセージを送る |
| `ANALYZE` | インサイトを見る、どの管理者が投稿したか見る |
| `ADVERTISE` | 広告を作る |
| `MANAGE` | 権限を割り当てる |
| `VIEW_MONETIZATION_INSIGHTS` | 収益化のインサイトを見る |

画面上で「管理者(フルコントロール)」を与えた人は、すべてのタスクができます ✅。

運用のルール(⚪):

1. フルコントロールは**信頼できる2人以上**に付けます(1人だけだと、その人が使えなくなったときに管理できなくなります)。
2. 投稿担当・返信担当など、他の人には**必要な権限だけ**を与えます。
3. 担当者が替わったら、すぐに権限を外します。
4. 全員に**2段階認証**を設定してもらいます([account-security](../01-common/account-security.md))。

### 3. Meta Business Suite を使う

Meta Business Suite では、Facebook と Instagram の**投稿・予約・インサイト・受信箱(コメント・メッセージ)・広告・収益化**をまとめて管理できます。パソコンとスマートフォンアプリの両方で使えます ✅([Meta for Creators](https://creators.facebook.com/tools/meta-business-suite))。自分の役割によって表示される機能が変わります ✅。

Instagram プロアカウントをページにリンクすると、両方を同じ画面で扱えます([03-instagram/01](../03-instagram/01-account-setup.md))。

### 投稿の種類(⚪)

| 種類 | 概要 |
|---|---|
| テキスト・リンク | リンクプレビュー(約 1.91:1 の画像) |
| 写真 | 複数枚アルバム |
| 動画 | 通常動画、リール([06-reels-video-and-live](06-reels-video-and-live.md)) |
| ストーリーズ | 24時間 |
| ライブ | リアルタイム |
| イベント | 集客・告知 |
| グループ投稿 | コミュニティ([03-engagement-and-groups](03-engagement-and-groups.md)) |

### 投稿手順

1. Meta Business Suite または ページから作成。
2. 本文・メディア・リンク・タグ付け・位置。
3. 予約または公開。クロスポスト(Instagram など)も設定可能 ⚪。
4. 広告・PR は表記([legal-compliance](../01-common/legal-compliance.md))。

もう少し詳しく(⚪ ボタン名は変わる可能性):

1. ページに切り替えた状態で「投稿を作成」を押します(Business Suite なら「投稿を作成」)。
2. 本文を書きます。最初の1〜2行に要点を書くと、「もっと見る」で隠れても伝わります。
3. 写真・動画を追加するか、URL を貼ってリンクプレビューを表示させます。プレビューの画像は**リンク先のページの OGP 設定**で決まります([02-media-specs](02-media-specs.md))。
4. 必要ならタグ付け(人・ページ)、場所、気分・アクティビティを追加します。
5. 「今すぐ公開」か「日時を指定」(予約)を選びます。
6. Instagram にも出す場合は、Business Suite で配信先に Instagram を追加します。

### 予約投稿の仕様(API で確認できた値 ✅)

| 項目 | 値 | 確度 | 出典 |
|---|---|---|---|
| 予約できる範囲 | API 経由では**10分後〜30日後** | ✅ | [Pages API Posts](https://developers.facebook.com/documentation/pages-api/posts.md) |
| 地域を絞った配信 | 国・都市を指定して表示対象を限定できる(API の `targeting.geo_locations`) | ✅ | 同上 |
| 投稿の編集 | アプリで作った投稿は、そのアプリからのみ API で更新できる | ✅ | 同上 |
| Business Suite での予約の上限期間 | 未確認 | ⚪ | — |

## 具体例

**良い例(地域の料理教室のページ)**

```
【6月の親子料理教室】
7/13(土)10時〜 小学生と保護者向け・定員8組
メニュー: 手作りピザとサラダ
お申し込みはページの「予約する」ボタンから
```

→ 何の・いつの・誰向けの情報かが冒頭で分かります。

**避けたい例**: 長い挨拶のあとに日程が埋もれている投稿や、URL だけの投稿。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 管理者が1人だけで、退職後に誰も編集できない | フルコントロールを2人以上に。担当交代時に権限を更新 |
| 個人のプロフィールで店の告知をして友達に通知が行き過ぎた | 店の発信はページに分ける |
| リンクプレビューの画像が古いまま | リンク先の OGP 画像を更新する(共有デバッガーで再取得 ⚪) |
| 予約投稿の日時を間違えた | 予約一覧で日時と配信先を確認してから確定 |
| 「ページが停止されます」というメッセージのリンクを開いた | 偽の通知の可能性。アプリの「アカウントステータス」など正規の画面で確認する |

## 注意点

- Facebook は実名制です。個人アカウントの情報(生年月日・勤務先など)の公開範囲を見直します([privacy-and-personal-info](../01-common/privacy-and-personal-info.md))。
- 投稿の表示範囲(公開・友達のみなど)は、プロフィールの投稿では毎回確認します。ページの投稿は原則公開です(⚪)。
- 画面の名称は頻繁に変わります(⚪)。見つからないときは設定の検索欄を使います。

## チェックリスト

- [ ] ページかプロフェッショナルモードかを決めた
- [ ] ページ名・カテゴリ・説明・連絡先・ユーザーネームを設定した
- [ ] プロフィール写真・カバー写真を設定した
- [ ] 行動ボタン(メッセージ・予約など)を1つ設定した
- [ ] フルコントロールを2人以上に、他は必要な権限のみ
- [ ] 全管理者が2段階認証を設定した
- [ ] Meta Business Suite に Instagram をリンクした(必要な場合)

## 関連ページ / 次に読む

- 次に読む: [02-media-specs](02-media-specs.md)、[06-reels-video-and-live](06-reels-video-and-live.md)
- [03-engagement-and-groups](03-engagement-and-groups.md)、[05-analytics-and-policies](05-analytics-and-policies.md)
- API: [20-api/07-other-apis](../20-api/07-other-apis.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://creators.facebook.com/tools/facebook-pages-and-profiles | 2026-11-03 | ✅ ページとプロフェッショナルモードの違い |
| https://creators.facebook.com/tools/meta-business-suite | 2026-11-03 | ✅ Meta Business Suite の機能 |
| https://developers.facebook.com/documentation/pages-api/overview.md | 2026-11-03 | ✅ ページのタスク(権限) |
| https://developers.facebook.com/documentation/pages-api/posts.md | 2026-11-03 | ✅ 予約投稿の範囲(10分〜30日)、地域指定 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(ページとプロフェッショナルモードの比較 ✅、ページ作成手順、権限(タスク)✅、Meta Business Suite ✅、投稿の詳細手順、予約投稿の仕様 ✅、具体例、よくある失敗、チェックリスト)。既存の表・手順は維持 |
