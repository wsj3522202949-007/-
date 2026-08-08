---
id: tool-07421
type: tool
area: 库
status: active
tags: [Pascal, 协议宽松, 本地优先, 中文友好, 本地写作]
title: narou-downloader
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/minouejapan/narou-downloader
created: 2026-07-18
updated: 2026-07-18
no: 7421
category: 画龙补充 / 扩容入库 — 补充源
repo: minouejapan/narou-downloader
stars: 8
url: https://github.com/minouejapan/narou-downloader
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4d4d2086c974f2be
  - methods/QUICK_START.md
---

# minouejapan/narou-downloader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/minouejapan/narou-downloader
- **Stars**：8
- **语言**：Pascal
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：小説家になろう系作品テキストダウンローダー
- **本地描述**：narou-downloader
- **拉取时间**：2026-07-25 19:21:22

related:
  - methods/QUICK_START.md
---

### narou-downloader
na6dlは小説家になろうおよび姉妹サイトで公開されている小説を青空文庫形式のテキストファイルでダウンロードするためのツールです。<br>
URLがhttps://ncode.syosetu.com/およびhttps://novel18.syosetu.com/で始まる作品をダウンロードすることが出来ます。<br>

### 動作環境
Windows10/11上のコマンドプロンプト上で動作します。

### 実行ファイルの作り方
* Delphi (XE2以降)の場合：na6dl.dprojを開いてビルドしてください。尚、ビルドするためにはTregExprライブラリが必要です。
* Lazarus（3.6以降）の場合：na6dl.lpiを開いてビルドして下さい。尚、ビルドするためにはTregExprライブラリとSimpleHTMLParserが必要です。Lazarusの場合はWindows上でクロスコンパイルするかLinux上のLazarusでビルドすることでLinux用の実行ファイルも出力可能です。
  * TregExprライブラリ：https://github.com/andgineer/TRegExpr
  * SimpleHTMLParser：https://github.com/minouejapan/SimpleHTMLParser

### 使い方
コマンドプロンプト上で、<br>
na6dl ダウンロードしたいなろう系小説トップページのURL (保存したいテキストファイル名)<br>
と入力して実行キーを押します。正常に実行されればna6dl.exeがあるフォルダにダウンロードした小説が青空文庫形式のテキストファイルで保存されます。<br>

尚、保存したファイル名の指定は省略できます。省略した場合はダウンロードした小説のタイトル名からファイル名を作成して保存します。<br>

### 禁止事項
1. na6dlを用いてWeb小 説サイトからダウンロードしたテキストファイルの第三者への販売や不特定多数への配信。 
2. ダウンロードしたオリジナル作品を著作者の了解なく加工（文章の流用や作品の翻訳等）しての再公開。 
3. その他、著作者の権利を踏みにじるような行為。 


### ライセンス
MIT
