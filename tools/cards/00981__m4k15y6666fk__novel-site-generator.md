---
id: tool-00981
type: tool
area: 库
status: active
tags: [Nunjucks, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel-site-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/m4k15y6666fk/novel-site-generator
created: 2026-07-18
updated: 2026-07-18
no: 981
category: 二、网文 / 长篇 AI 写作系统 库
repo: m4k15y6666fk/novel-site-generator
stars: 0
url: https://github.com/m4k15y6666fk/novel-site-generator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# m4k15y6666fk/novel-site-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/m4k15y6666fk/novel-site-generator
- **Stars**：0
- **语言**：Nunjucks
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Static Site Generator, and some tools for writing novels.
- **本地描述**：Static Site Generator, and some tools for writing novels.
- **拉取时间**：2026-07-23 23:07:39

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Novel Site Generator

小説サイトを作るための

### 動作環境

macOS 12.4

~~~bash
git --version
git version 2.38.1

npm --version
8.19.3
~~~

### インストール

~~~bash
mkdir novel-site-generator

git clone https://github.com

npm install
~~~

### 起動

~~~bash
npm start
~~~

### 各画面の説明

#### リポジトリの作成

#### サイト設定画面

#### 小説編集画面（追加・編集・削除）

#### エディター画面

#### 小説編集画面（ソート）

#### バージョン管理画面

~~~bash
git revert <commit id>..HEAD
~~~

##### 高度なバージョン管理

~~~bash
cd $HOME/.local/share/novel-site-generator/data/[小説のリポジトリ]
git <git command>
~~~

### 小説データ

小説データ：

`$HOME/.local/share/novel-site-generator/data/[小説のリポジトリ]`

小説データ（バックアップ）：

`$HOME/.local/share/novel-site-generator/archive`

設定ファイル：

`$HOME/.config/novel-site-generator/config.json`

### ライセンス

このソフトは MIT ライセンスで提供されています。
