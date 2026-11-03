---
title: YouTube Data API v3
platform: youtube
topic: api
last_verified: 2026-11-03
confidence: ✅
sources:
  - https://developers.google.com/youtube/v3/getting-started
  - https://developers.google.com/youtube/v3/determine_quota_cost
  - https://developers.google.com/youtube/v3/docs/videos/insert
  - https://developers.google.com/youtube/v3/revision_history
---

# YouTube Data API v3

> **このページで分かること**: YouTube Data API でできること、始める手順(Google Cloud)、API キーと OAuth の使い分け、クォータ(1日の割り当て量)、アップロードの制約、最小コード。
>
> **対象**: 初心者〜中級者  **先に読むページ**: [00-api-for-beginners](00-api-for-beginners.md)

> 2026年(皇紀2686年・令和8年)11月3日に **developers.google.com の公式文書を直接取得**して、以前の 🟡(#38)を ✅ に更新しました。ただし「未監査プロジェクトの非公開制限」は公式文書の間で記述が食い違っています(下記)。

## 概要

YouTube Data API v3 は、YouTube の動画・再生リスト・コメント・チャンネル情報をプログラムから扱う公式 API です。**料金ではなく「クォータ」**(quota、1日に使える量)で利用量が制限されます。1日の割り当ては**太平洋時間(PT)の午前0時にリセット**されます(✅ [quota](https://developers.google.com/youtube/v3/determine_quota_cost))。

再生数などの詳しい分析は、別の **YouTube Analytics API / Reporting API** を使います。

## 用語

| 用語 | 意味 |
|---|---|
| Google Cloud console(グーグル クラウド コンソール) | API の有効化・鍵の発行・クォータ確認をする管理画面 |
| project(プロジェクト) | Google Cloud でのアプリの単位。鍵とクォータはプロジェクトごと |
| API key(API キー) | 公開データの読み取りに使う鍵 |
| OAuth 2.0 client ID(OAuth クライアント ID) | 利用者の許可を得て操作するための ID |
| quota(クォータ) / unit(ユニット) | 1日に使える量 / その単位。操作ごとにコストが決まっている |
| quota bucket(クォータの枠) | 操作のグループごとの別枠。2026年6月から一部のメソッドが専用の枠に |
| `part`(パート) | レスポンスに含める情報のまとまり(`snippet`、`statistics` など) |
| audit(監査) | YouTube API サービスの規約に沿っているかの確認 |

## 主な用途

| 用途 | API |
|---|---|
| 動画のアップロード | `videos.insert` |
| サムネイル設定 | `thumbnails.set` |
| メタデータ更新 | `videos.update` |
| 字幕 | `captions.insert` ほか |
| 再生リスト | `playlists`、`playlistItems` |
| コメント管理 | `commentThreads`、`comments` |
| 検索 | `search.list`(クォータが重い ⚪ → 2026年6月から専用の枠 ✅ 下記) |
| 分析 | YouTube Analytics API、Reporting API |

## 始める手順(✅ [getting started](https://developers.google.com/youtube/v3/getting-started)。画面名は変わる可能性 ⚪)

1. **Google アカウント**を用意する。
2. **Google Cloud console** でプロジェクトを作る。
3. **API ライブラリ**で「YouTube Data API v3」を有効にする(有効な API の一覧に出ているか確認)。
4. 認証情報を作る。
   - 公開データだけを読む → **API キー**(API キーでの `list` は公開データのみ返る ✅)。
   - 投稿・更新・削除、本人だけが見られる情報 → **OAuth 2.0 クライアント ID**(**insert・update・delete はすべて OAuth が必要** ✅)。
5. 鍵を `.env` に保存([13-secrets-management](13-secrets-management.md))。
6. クォータの使用量は Cloud console の**クォータ**画面で確認。増やしたいときは**クォータ拡張フォーム**で申請(✅)。

## 重要な制約

### 未監査プロジェクトのアップロードと非公開(✅ ただし公式文書間で不一致)

| 公式文書 | 記述 |
|---|---|
| [Revision History](https://developers.google.com/youtube/v3/revision_history) の 2020年(皇紀2680年・令和2年)7月28日の項 | 2020年7月28日以降に作成された**未検証の API プロジェクト**から `videos.insert` でアップロードされた動画は**非公開に制限**。解除には**監査**(利用規約への準拠確認)が必要 |
| [videos.insert リファレンス](https://developers.google.com/youtube/v3/docs/videos/insert) の `status.privacyStatus` の説明(2026-11-03 取得) | 「Videos uploaded from unverified API projects are **not restricted** to private viewing mode.」(未検証のプロジェクトからの動画は非公開に制限されない)。未指定なら既定は公開。ただし作成者のアカウント設定により非公開になる場合がある |

以前の本ページの記載(🟡):

> 2020年7月28日以降に作成された**未検証の API プロジェクトからアップロードされた動画は、非公開に制限される**。解除には**API 監査(利用規約への準拠確認)**を受ける。クォータの余裕とは無関係。

→ 現行のリファレンスでは制限がないと読めますが、制限の解除を告知する改訂履歴は見当たりませんでした。**本番運用の前に、限定公開のテスト動画で実際の公開状態を確認**してください(要検証)。監査の推奨自体は改訂履歴で繰り返し述べられています(✅)。

→ 自動アップロードを検討する場合は、まず**手動(YouTube Studio)で運用**し、API は読み取り・メタデータ更新など限定的な用途から。監査の申請手順は公式で確認。

### クォータ(✅ [quota](https://developers.google.com/youtube/v3/determine_quota_cost)、2026-11-03 取得)

| 項目 | 内容 | 確度 |
|---|---|---|
| 既定の1日クォータ | **10,000 ユニット**(`search.list` と `videos.insert` を除く全メソッドの共通枠) | ✅ |
| `videos.insert` | **1回 1 ユニット、専用の枠で 100回/日** | ✅ |
| `search.list` | **1回 1 ユニット、専用の枠で 100回/日** | ✅ |
| 読み取り(`videos.list`、`channels.list`、`commentThreads.list` など) | 1 ユニット | ✅ |
| 書き込み(`videos.update`、`thumbnails.set`、`comments.insert`、`playlistItems.insert`) | 50 ユニット | ✅ |
| `captions.insert` | 400 ユニット | ✅ |
| 失敗したリクエスト | **最低 1 ユニット消費** | ✅ |
| リセット | 太平洋時間の午前0時 | ✅ |

経緯(✅ [Revision History](https://developers.google.com/youtube/v3/revision_history)):

| 日付 | 変更 |
|---|---|
| 2025年(皇紀2685年・令和7年)12月4日 | 動画アップロードのコストを約 1,600 ユニットから約 100 ユニットに変更と文書を更新 |
| 2026年6月1日 | 粒度の細かいクォータへ移行。`videos.insert` と `search.list` がそれぞれ**専用の枠**に |
| 2026年6月3日 | `videos.batchGetStats`(動画の統計の一括取得)を追加。専用の枠で 1 ユニット、既定 10,000 ユニット/日 |
| 2026年9月14日 | `thumbnails.set` のサムネイルの最大容量が **2MB から 50MB** に |

以前の本ページの記載(🟡)は「従来 1,600ユニット(約6本/日)。2026年6月1日に 1 ユニットへ下がったとする資料と、100回/日の専用バケットとする資料がある(不一致)」、`search.list` は「100 ユニット/回」(⚪)でした。公式では `videos.insert` について**両方とも正しく、「1回1ユニット、専用枠で100回/日」**です。`search.list` も現行は「1回1ユニット、専用枠で100回/日」です(✅)。

→ 使用量は Google Cloud のクォータ画面で確認し、各メソッドのコストは**公式のクォータ表で確認してから**見積もる。

## 認証

OAuth 2.0。アップロードには `youtube.upload` スコープ(✅ ほかに `youtube`、`youtubepartner`、`youtube.force-ssl` のいずれでも可 [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert))。**チャンネル所有者の同意**が必要。サービスアカウントは使えない場合が多い(⚪)。

アップロードできるファイル: 最大 **256GB**、MIME タイプ `video/*` または `application/octet-stream`(✅ 同ページ)。アップロード数の上限を超えると `uploadLimitExceeded` エラー(✅)。

## 具体例: 自分の動画の再生数を読む(API キー、概念)

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
r = requests.get(
    "https://www.googleapis.com/youtube/v3/videos",
    params={
        "part": "snippet,statistics",
        "id": "YOUR_VIDEO_ID",             # 動画 URL の v= の後ろの文字列
        "key": os.environ["YOUTUBE_API_KEY"],
    },
    timeout=30,
)
for v in r.json().get("items", []):
    print(v["snippet"]["title"], v["statistics"].get("viewCount"))
```

`videos.list` は 1 ユニットです(✅)。毎日1回の取得なら、クォータをほとんど使いません。

## よくある失敗と対処

| 症状 | 原因 | 対処 |
|---|---|---|
| 403 で「API が有効でない」趣旨のエラー | プロジェクトで API を有効にしていない | API ライブラリで有効化(⚪ 文言は要確認) |
| API キーで投稿・更新できない | 書き込みは OAuth が必要 | OAuth 2.0 クライアントで認可 |
| 夕方に急に使えなくなる | 1日のクォータを使い切った | リセットは PT の午前0時(日本時間で16時または17時 ⚪)。`part` を絞る |
| エラーの再試行でクォータが減る | 失敗も最低1消費 | 4xx は再試行しない |
| アップロードした動画が非公開のまま | アカウント設定、または未監査の制限(上記の不一致) | 動画の状態を確認し、必要なら監査を申請 |

## 運用の指針

1. 長尺動画の投稿は**手動**で品質管理(サムネイル・字幕・チャプター)し、メタデータの一括更新などに API を使う。
2. 分析の自動取得(Analytics API)で週次レビューを効率化。
3. コメントの自動返信は**スパム扱いの危険**があるため、半自動(下書き)に留める。

## 関連ページ / 次に読む

- [01-setup-and-posting](../05-youtube/01-setup-and-posting.md)、[08-upload-and-shorts](../05-youtube/08-upload-and-shorts.md) — アプリ・Studio での投稿
- [15-python-first-steps](15-python-first-steps.md) — API キーでの最初の呼び出し
- [12-auth-oauth-and-tokens](12-auth-oauth-and-tokens.md)、[14-errors-and-troubleshooting](14-errors-and-troubleshooting.md)
- [02-google](../40-pricing/02-google.md) — Google の料金プラン

## 出典

| URL | 確認日 | 備考 |
|---|---|---|
| https://developers.google.com/youtube/v3/getting-started | 2026-11-03 | 始める手順、API キーと OAuth の使い分け、`part` |
| https://developers.google.com/youtube/v3/determine_quota_cost | 2026-11-03 | クォータ表、専用枠、リセット時刻 |
| https://developers.google.com/youtube/v3/docs/videos/insert | 2026-11-03 | スコープ、256GB、非公開制限の記述 |
| https://developers.google.com/youtube/v3/revision_history | 2026-11-03 | 2020年の非公開制限、2025〜2026年のクォータ変更 |

## 変更履歴

| 日付 | 内容 |
|---|---|
| 2026-11-03 | 検索要約と二次資料に基づき作成(🟡 #38) |
| 2026-11-03 | 公式文書を直接取得して ✅ に更新。クォータを公式値に修正(`videos.insert`・`search.list` は1回1ユニット・専用枠100回/日)。非公開制限について公式文書間の不一致を併記。初心者向けに概要・用語・始める手順・コード例・よくある失敗・出典を追加 |
