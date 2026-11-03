---
title: 自動化の方針・ツール・規約
platform: common
topic: api
last_verified: 2026-11-03
confidence: ⚪
sources:
  - https://docs.x.com/changelog.md
  - https://docs.x.com/x-api/getting-started/getting-access.md
  - https://developers.tiktok.com/doc/content-sharing-guidelines
---

# 自動化の方針・ツール・規約

> **このページで分かること**: SNS 運用をどこまで自動化してよいか、段階ごとのリスク、やってよいこと・いけないこと、ツールの選び方、GitHub Actions での定期実行の安全な形。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

## 概要

「自動化」と一口に言っても、**公式アプリの予約投稿**から**自作プログラムでの自動投稿**まで幅があります。段階が上がるほど便利ですが、**規約違反・誤投稿・鍵の漏えい**のリスクも上がります。

初心者は次の順に進めるのが安全です。

1. 公式の予約機能を使いこなす。
2. 読み取り(分析データの取得)だけを自動化する。
3. 投稿の自動化は、**人の承認を挟んで**から。

各サービスは自動化について明確なルールを持っています。例えば X は2026年(皇紀2686年・令和8年)に、**呼び出されていない投稿への API からの返信**や、**API からのいいね・フォロー・引用**を self-serve のプランで使えなくしました(✅ [02-x-api](02-x-api.md) §3)。TikTok は、他サービスからのコピー投稿や社内ツール的なアップロードを意図された用途ではないとしています(✅ [06-tiktok-api](06-tiktok-api.md))。

## 用語

| 用語 | 意味 |
|---|---|
| automation(自動化) | 人が毎回操作しなくても処理が動くようにすること |
| scheduled post(予約投稿) | 日時を指定して後で公開する投稿 |
| third-party tool(サードパーティツール) | SNS 運営会社以外が作ったツール |
| no-code(ノーコード) | プログラムを書かずに画面操作で連携を作る方式(Zapier・Make・IFTTT など) |
| scraping(スクレイピング) | 画面の内容をプログラムで抜き出すこと。多くのサービスで規約上の制限あり |
| approval gate(承認ゲート) | 人が「承認」するまで公開しない仕組み |
| GitHub Actions(ギットハブ アクションズ) | GitHub 上でプログラムを定期実行できる仕組み |
| cron(クロン) | 「毎週月曜9時」のような定期実行の書き方 |

## 自動化の段階

| 段階 | 内容 | 規約リスク |
|---|---|---|
| 0. 手動 | アプリで投稿 | なし |
| 1. 公式の予約機能 | Meta Business Suite、YouTube Studio、各サービスの予約 | 低 |
| 2. 公認サードパーティ | 公式 API を使う予約ツール | 低〜中(ツールの信頼性) |
| 3. 自作スクリプト(公式 API) | 自分のアカウントのみ | 中(規約・制限・管理) |
| 4. ノーコード連携(Zapier / Make / IFTTT など) | 他サービスとのトリガー連携 | 中 |
| 5. 非公式 API・スクレイピング・ブラウザ自動操作 | — | **高(原則やらない)** |

## やってよいこと / やってはいけないこと(⚪ 一般論。規約は各サービスで確認)

| よい | 避ける |
|---|---|
| 自分のアカウントへの予約投稿 | 自動フォロー・自動いいね・自動リプライの乱用 |
| 公式 API でのインサイト取得 | 同一内容の大量投稿(スパム) |
| 通知(新着コメントをメールで) | 複数アカウントでの水増し |
| 下書きの自動作成 → 人が確認して公開 | 他人のデータの大量収集・再配布 |
| 投稿結果のログ | ボットを人間のように装う(必要なら自動化の表示) |

## 人間の承認ゲート(推奨)

AI(生成 AI)による投稿案・返信案は、**必ず人が確認してから公開**([ai-usage-policy](../01-common/ai-usage-policy.md))。誤情報・不適切表現・ステマの表示漏れを防ぐ。

## ツールの選定基準([tools](../01-common/tools.md) も参照)

| 基準 | 確認すること |
|---|---|
| 公式 API の利用か | 認証情報をツールに渡す前に、公式の連携(OAuth)か確認 |
| 権限範囲 | 読み取りのみで足りるか |
| 費用 | 月額、投稿数制限、X API の従量課金の扱い |
| データの扱い | 投稿内容・分析データの保存先 |
| 停止時の影響 | サービス終了時のデータ持ち出し |

## 例: GitHub Actions による定期実行

このリポジトリのように Markdown で投稿計画を管理し、GitHub Actions で**検査**や**下書きの生成**を行う構成が可能。ただし:

- API 鍵は **GitHub の Secrets** に保管(リポジトリに書かない)。
- **public リポジトリ**では、ログ・出力に秘密や未公開の投稿内容を出さない。
- 公開前の投稿案は**private リポジトリ**で管理するのが安全([CONTRIBUTING](../../CONTRIBUTING.md))。

### GitHub Actions の設定例(⚪ 概念。書式は GitHub の公式文書で確認)

鍵はリポジトリの **Settings > Secrets and variables > Actions** に登録し、ワークフローからは名前で参照します(⚪ 画面名は変わる可能性)。

```yaml
# .github/workflows/weekly-report.yml(例)
name: weekly-report
on:
  schedule:
    - cron: "0 0 * * 1"        # 毎週月曜 0:00 UTC(日本時間 9:00)
  workflow_dispatch: {}         # 手動実行も可能に
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install requests
      - run: python scripts/weekly_report.py   # 読み取りだけを行うスクリプト
        env:
          X_USER_ACCESS_TOKEN: ${{ secrets.X_USER_ACCESS_TOKEN }}
```

- `cron` の時刻は **UTC(協定世界時)** です。日本時間は UTC+9 です(⚪)。
- スクリプトは**読み取りから**。投稿するなら「承認済み」フラグのあるものだけにします([09-architecture-patterns](09-architecture-patterns.md))。
- ログに鍵や未公開の内容を出さない。

## よくある失敗と対処

| 失敗 | 対処 |
|---|---|
| 予約ツールに SNS のパスワードを入力した | 公式の OAuth 連携か確認。違うならパスワードを変更し、連携を解除 |
| 自動投稿が同じ文面を連投した | 二重投稿の防止(投稿 ID の記録)と、停止ボタンを用意 |
| AI が作った返信を自動送信し、誤った内容が出た | 承認ゲートを必ず挟む |
| ツールの月額は安かったが、X API の費用が別にかかった | ツールの説明で API 費用の扱いを確認([11-tool-integrations](11-tool-integrations.md)) |
| 規約変更で突然動かなくなった | 月次で changelog を確認(下記) |

## チェックリスト

- [ ] 公式の予約機能で足りないことを確認した
- [ ] 各サービスの開発者規約・自動化ルールを読んだ
- [ ] 自分のアカウントだけを対象にしている
- [ ] 投稿・返信・DM は人が承認してから
- [ ] 鍵は Secrets / `.env` にあり、ログに出ない
- [ ] 緊急時にすべての自動化を止める方法がある

## 規約変更への備え

月次で各サービスの開発者規約・価格・上限を確認し、[verification-queue](../00-meta/verification-queue.md) に記録。

主な確認先: X の [changelog](https://docs.x.com/changelog.md)、YouTube の [Revision History](https://developers.google.com/youtube/v3/revision_history)(2026年6月のクォータ変更なども載る ✅ [05](05-youtube-data-api.md))、Meta・TikTok・LINE の開発者向けニュース。

## 関連ページ / 次に読む

- [10-benefits-of-api](10-benefits-of-api.md) — API を使うかどうかの判断
- [11-tool-integrations](11-tool-integrations.md) — ツール連携
- [09-architecture-patterns](09-architecture-patterns.md) — 投稿パイプラインの設計
- [13-secrets-management](13-secrets-management.md) — 鍵の保管

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://docs.x.com/changelog.md | 2026-11-03 | 返信・いいね・フォロー・引用の制限 |
| https://docs.x.com/x-api/getting-started/getting-access.md | 2026-11-03 | 認証情報の保管の推奨 |
| https://developers.tiktok.com/doc/content-sharing-guidelines | 2026-11-03 | 意図された用途、禁止事項 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 初心者向けに加筆(このページで分かること・概要・用語・GitHub Actions の設定例・よくある失敗・チェックリスト・関連ページ・出典を追加。既存の段階表・可否表・選定基準は維持) |
