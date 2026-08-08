---
id: tool-07363
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 本地写作]
title: kakuyomu-cli
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/kokardy/kakuyomu-cli
created: 2026-07-18
updated: 2026-07-18
no: 7363
category: 画龙补充 / 扩容入库 — 补充源
repo: kokardy/kakuyomu-cli
stars: 0
url: https://github.com/kokardy/kakuyomu-cli
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: cd7bab48a01361e4
  - methods/QUICK_START.md
---

# kokardy/kakuyomu-cli

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/kokardy/kakuyomu-cli
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：kakuyomu-cli
- **拉取时间**：2026-07-25 19:19:35

related:
  - methods/QUICK_START.md
---

# kakuyomu CLI

Command line interface for kakuyomu.jp writers.

## install

`pip install kakuyomu-cli`

`kakuyomu --help`

# Commands

## Kakuyomu command

`kakuyomu --help`

```
Usage: kakuyomu [OPTIONS] COMMAND [ARGS]...

  Kakuyomu CLI

  Command line interface for kakuyomu.jp カクヨムの小説投稿・編集をコマンドラインから行うためのツール

Options:
  --help  Show this message and exit.

Commands:
  episode  エピソード関係のコマンド
  init     現在のディレクトリを小説の1タイトルのrootとして初期化する
  login    ログインする
  logout   ログアウトする
  status   ログインステータスを表示する
  work     小説タイトルに関するコマンド
```

## Work commands

`kakuyomu work --help`

```
Usage: kakuyomu work [OPTIONS] COMMAND [ARGS]...

  小説タイトルに関するコマンド

Options:
  --help  Show this message and exit.

Commands:
  list  小説タイトルの一覧を表示する
```

## Episode commands

`kakuyomu episode --help`

```
Usage: kakuyomu episode [OPTIONS] COMMAND [ARGS]...

  エピソード関係のコマンド

Options:
  --help  Show this message and exit.

Commands:
  create   リモートにエピソードを作成する
  fetch    リモートのエピソードをwork.tomlに同期する
  link     work.tomlのエピソードにファイルパスを設定する
  list     エピソードをリスト表示する
  publish  エピソードの公開予約を行う
  show     エピソードの内容を表示する
  unlink   エピソードからファイルパス設定を削除する
  update   リモートエピソードの内容をリンクされているファイルの内容に更新する
```

## Login

`kakuyomu login --help`

```
Usage: kakuyomu login [OPTIONS]

  ログインする

```

## usage

1.  小説のルートディレクトリに移動
2.  ログイン `kakuyomu login`
3.  初期設定 `kakuyomu init` 小説を選択
