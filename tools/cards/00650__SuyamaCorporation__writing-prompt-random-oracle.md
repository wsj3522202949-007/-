---
id: tool-00650
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: writing-prompt-random-oracle
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/suyamacorporation/writing-prompt-random-oracle
created: 2026-07-18
updated: 2026-07-18
no: 650
category: 二、网文 / 长篇 AI 写作系统 库
repo: SuyamaCorporation/writing-prompt-random-oracle
stars: 0
url: https://github.com/suyamacorporation/writing-prompt-random-oracle
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6b29ddc0f25e20e1
  - methods/最强写作方法论_全球最强综合版.md
---

# SuyamaCorporation/writing-prompt-random-oracle

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/suyamacorporation/writing-prompt-random-oracle
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-generated app: 創作 お題 ランダムオラクル (zerohuman-labs daily 2026-07-04)
- **本地描述**：AI-generated app: 創作 お題 ランダムオラクル (zerohuman-labs daily 2026-07-04)
- **拉取时间**：2026-07-23 22:58:01

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 創作 お題 ランダムオラクル

登場人物・舞台・葛藤・テーマの4要素をランダム組み合わせて小説・エッセイ・シナリオの創作お題を生成するアプリ。

## 機能
- 登場人物・舞台・葛藤・テーマの4要素をジャンル別に多数内蔵（SF/ファンタジー/現代/ホラー/ミステリー/ロマンス/コメディ）
- ジャンルフィルターと詳細度スライダー（シンプル1文/中程度/詳細パラグラフ）で出力をコントロール
- 「お題を生成」ボタンでアニメーション付きのランダム組み合わせ生成
- 生成したお題のテキストコピー機能
- お気に入りお題をlocalStorageに保存・コレクション表示・削除
- 書き始め用10分タイマー内蔵（プログレスバー・スタート/リセット）

## 技術スタック
- 静的SPA（index.html 単一ファイル完結）
- Tailwind CSS CDN + CSSアニメーション（Oracle生成演出）
- localStorage（お気に入りお題の永続化）
