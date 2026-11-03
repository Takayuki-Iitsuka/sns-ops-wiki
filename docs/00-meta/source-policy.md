---
title: 出典方針
last_verified: 2026-11-03
confidence: ✅
---

# 出典方針

> **このページで分かること**: このナレッジベースが情報の根拠(出典)をどう選び、どう書くか。自分で情報を調べるときに、どの資料を信用すればよいか。
>
> **対象**: 読者全員、とくにページを編集・追記する人。**先に読むページ**: [読み方と確度ラベル](how-to-read.md)

## 概要

SNS の情報はインターネット上にあふれていますが、古い情報や、根拠のない「噂」も多く混ざっています。たとえば「Instagram のハッシュタグは30個まで」という情報は、時期や資料によって食い違います。このナレッジベースでは、**誰が出した情報か**を重視し、根拠の強さに応じて確度ラベル(✅🟡⚪)を付けます。

## 用語

| 用語 | 意味 |
|---|---|
| primary source(一次資料) | 情報を決めた本人が出した資料。サービスの公式ヘルプ、規約、開発者文書、法令など |
| secondary source(二次資料) | 一次資料をもとに第三者が書いた解説・報道 |
| tertiary source(三次資料) | 二次資料をさらにまとめたもの。まとめ記事、個人ブログ、SNS の投稿など |
| changelog(変更履歴) | サービスや API の変更点を時系列で記録した公式ページ |

## 優先順位

1. **一次資料**(最優先): 各サービスの公式ヘルプセンター、公式ブログ、利用規約、開発者ドキュメント、法令(e-Gov 法令検索)、消費者庁等の公的機関
2. **二次資料**: 信頼できる報道・業界メディア。必ず一次資料での裏取りを `verification-queue.md` に登録
3. **三次資料**: 個人ブログ・まとめ記事。原則として根拠にしない(裏取りの手がかりとしてのみ使う)

### 資料の見分け方

| 確かめること | 一次資料の特徴 |
|---|---|
| ドメイン(URL のサービス名部分) | 運営会社のドメイン(例: `help.x.com`、`support.google.com`、`developers.facebook.com`、`www.caa.go.jp`) |
| 書き手 | 運営会社・官公庁の名義 |
| 日付 | 更新日が書かれている(なければ注意) |
| 言語 | 日本語版と英語版で内容が違うことがある(日本の利用者には日本語版を優先) |

## 記載ルール

- 数値・条件の直後に確度ラベルを付ける。例: `5MB ✅`
- 出典は「ページ末尾の出典」節に URL と確認日を書く。表の中では「出典」列に URL を書く。
- 公式ページが日本語/英語で内容が異なる場合は、日本語の利用者に適用される版(日本語ページ)を優先し、差異を注記する。
- 「〜と言われている」「〜らしい」は書かない。確認できなければ ⚪ を付けるか、記載しない。
- 同じ公式資料の中で値が食い違う場合は、両方を書き「不一致」と明記する(例: Instagram API の公開上限 100 と 50 → [要検証リスト](verification-queue.md) #37)。
- 料金は「税込/税抜」「通貨」「確認日」「為替の影響」を必ず書く。

### 書き方の例

| 良い例 | 悪い例 |
|---|---|
| 写真は最大5MB ✅(出典: docs.x.com、2026-11-03 確認) | 写真は5MBまでらしい |
| 上限が5個に引き下げられたと報道されている 🟡(公式 API 文書は30個 ✅) | 上限は5個(出典なし) |
| 朝に投稿すると反応が多いことがある ⚪ | 朝に投稿すべき |

## 調べ方の手順

1. まず **公式ヘルプ・開発者文書** を検索します(例: 検索語に `site:support.google.com` を付ける)。
2. 見つからなければ **公式ブログ・公式アカウントのお知らせ** を探します。
3. それでもなければ、報道・解説記事(🟡)を使い、[要検証リスト](verification-queue.md) に登録します。
4. 確認した日付を必ず記録します。

### 取得のコツ(2026年(皇紀2686年・令和8年)11月時点)

| ホスト | コツ |
|---|---|
| `docs.x.com` | URL 末尾に `.md` を付けると Markdown で読める |
| `developers.facebook.com` | `/documentation/...` の末尾に `.md` |
| `support.google.com` | `?hl=ja` で日本語版 |
| `help.x.com`、`www.help-note.com` | 自動取得は bot 確認で失敗しやすい。ブラウザで開いて確認する |
| `help.instagram.com` | JavaScript で描画されるため、ブラウザで確認する |

## 公式ヘルプの主な入口(確認用)

| サービス | 入口 |
|---|---|
| X | https://help.x.com/ja |
| X 開発者 | https://docs.x.com/ |
| Instagram | https://help.instagram.com/ |
| Meta(Instagram のクリエイター向け) | https://creators.facebook.com/ |
| Meta 開発者 | https://developers.facebook.com/ |
| Threads | https://help.instagram.com/(Threads のヘルプは Instagram ヘルプ内) ⚪ |
| Facebook | https://www.facebook.com/help/ |
| note | https://www.help-note.com/hc/ja |
| YouTube | https://support.google.com/youtube/?hl=ja |
| TikTok | https://support.tiktok.com/ja |
| LINE 公式アカウント | https://www.lycbiz.com/jp/ ⚪ |
| LINE 開発者 | https://developers.line.biz/ja/ |
| Bluesky | https://docs.bsky.app/ |
| 消費者庁 | https://www.caa.go.jp/ |
| 国税庁 | https://www.nta.go.jp/ |
| 文化庁(著作権) | https://www.bunka.go.jp/seisaku/chosakuken/ |
| e-Gov 法令検索 | https://laws.e-gov.go.jp/ |

## 関連ページ / 次に読む

- [出典一覧](sources.md)
- [要検証リスト](verification-queue.md)
- [編集規約](../../CONTRIBUTING.md)

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/llms.txt | 2026-11-03 | docs.x.com の Markdown 索引 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 新規作成 |
| 2026-11-03 | 初心者向けに加筆(資料の見分け方、書き方の例、調べ方の手順、取得のコツ、入口の追加) |
