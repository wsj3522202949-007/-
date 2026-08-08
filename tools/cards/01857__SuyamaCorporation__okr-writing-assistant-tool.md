---
id: tool-01857
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: okr-writing-assistant-tool
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/suyamacorporation/okr-writing-assistant-tool
created: 2026-07-18
updated: 2026-07-18
no: 1857
category: 二、网文 / 长篇 AI 写作系统 库
repo: SuyamaCorporation/okr-writing-assistant-tool
stars: 0
url: https://github.com/suyamacorporation/okr-writing-assistant-tool
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
content_hash: a941be2238ecc1c5
  - methods/最强写作方法论_全球最强综合版.md
---

# SuyamaCorporation/okr-writing-assistant-tool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/suyamacorporation/okr-writing-assistant-tool
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-generated app: OKR作成アシスタントツール (zerohuman-labs daily 2026-06-25)
- **本地描述**：AI-generated app: OKR作成アシスタントツール (zerohuman-labs daily 2026-06-25)
- **拉取时间**：2026-07-23 23:33:08

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# OKR作成アシスタントツール

Objective入力時にSMARTフレームワークをリアルタイム評価し、Key Resultsの測定可能性スコアとともに質の高いOKRを書けるよう支援するツール。

## 機能

- Objective入力 → SMART5項目（Specific/Measurable/Achievable/Relevant/Time-bound）をリアルタイムチェックしてチップ表示＋個別ヒント
- 曖昧表現（「改善する」「検討する」など）を自動検出して警告表示
- Key Results最大5件追加、各KRに測定可能性スコア（1〜5）を自動評価＋具体的な改善ヒント
- テンプレート3種（プロダクト/セールス/エンジニアリング）から一発入力
- localStorage に最大3件保存・読込、window.print() でPDF/印刷出力

## 技術メモ

静的SPA・Tailwind CSS CDN・正規表現ベースのSMART評価エンジン・localStorage で最大3件保存・print CSS で印刷最適化。
