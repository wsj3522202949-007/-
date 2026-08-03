---
id: tool-01285
type: tool
area: 库
status: active
tags: [PHP, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: writing_novel
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/alice0421/writing_novel
created: 2026-07-18
updated: 2026-07-18
no: 1285
category: 二、网文 / 长篇 AI 写作系统 库
repo: alice0421/writing_novel
stars: 0
url: https://github.com/alice0421/writing_novel
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# alice0421/writing_novel

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alice0421/writing_novel
- **Stars**：0
- **语言**：PHP
- **License**：None
- **Topics**：—
- **GitHub 描述**：文GO ～小説執筆ツール～（アプリURL：https://novel-tool.herokuapp.com/login）
- **本地描述**：文GO ～小説執筆ツール～（アプリURL：https://novel-tool.herokuapp.com/login）
- **拉取时间**：2026-07-23 23:16:34

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 文GO ～小説執筆ツール～
## アプリを作った背景
Markdownにはリアルタイムプレビューがよくあるが、自分が知る限り小説執筆サイトにはない。

そのため、リアルタイムプレビューを搭載した小説執筆サイトを作成しようと考えた。

## 開発環境
Docker

Vue.js　HTML/CSS　Tailwind CSS　axios

Laravel9　Inertia.js　MySQL

## デモ
- アプリURL: https://novel-tool.herokuapp.com
- Github: https://github.com/alice0421/writing_novel.git
- テストアカウント
    - Email: test@gmail.com
    - Password: test2022

## 機能
### 小説一覧
- 以下の3つにカテゴリ分け
    - 最近更新した小説
    - 執筆中の小説
    - 執筆完了した小説
- SPAによる小説詳細画面
    - モーダルの使用
    - モーダルをコンポーネント化し、"小説執筆画面"で再利用
- 自作カルーセル使用
    - 画面サイズの変更に対応
- もっと見る機能
    - 各カテゴリには最大10件のみ表示

### 小説執筆画面
- タイトル、本文、著者名の編集
    - コンポーネント化した小説詳細画面を再利用
    - 著者名の記述がなければ、ユーザーが登録済みのペンネームを表示
- リアルタイム縦書きプレビュー
- 見出し、ルビ、傍点の挿入ボタン
    - 正規表現の使用
- 保存時のUI / UX
    - 画面上のボタン以外にも、ショートカットキー（Ctrl + S）での保存可能
    - 保存完了時、一定時間後に自動消失するフラッシュメッセージを表示

### 新規小説作成画面
- タイトル＆本文未記入時にフラッシュメッセージでエラーを表示
    - バリエーションエラーを使用
- 新規保存完了時にフラッシュメッセージを表示
    - 小説執筆画面で表示される、既存の小説を更新保存する際に出るフラッシュメッセージとは別のメッセージを表示
- 新規保存完了後に、"小説執筆画面"にリダイレクト

## 課題・将来性
- 小説一覧の読込の遅さ
    - DBから長い本文を全て持ってきている
- もっと見る機能が数件ずつ追加表示ではない
    - DBから全件持ってくることの無駄さ
- 小説削除機能と複製機能の追加
- 任意に命名したシリーズごとのカテゴリ分け機能の追加
- 小説執筆画面にメモ機能やアウトライン機能の追加
