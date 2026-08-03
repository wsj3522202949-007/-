---
id: tool-05310
type: tool
area: 库
status: active
tags: [去AI味, TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: Humanize-audit
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/syntax9090/humanize-audit
created: 2026-07-18
updated: 2026-07-18
no: 5310
category: 一、去 AI 味 / Humanizer 库
repo: Syntax9090/Humanize-audit
stars: 0
url: https://github.com/syntax9090/humanize-audit
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Syntax9090/Humanize-audit

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/syntax9090/humanize-audit
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A small open-source toolkit that scans text files (Markdown, plain text, CSV, JSON) and generates a humanization report for LinkedIn posts, blog articles, and other content.
- **本地描述**：A small open-source toolkit that scans text files (Markdown, plain text, CSV, JSON) and generates a humanization report for LinkedIn posts, blog articles, and other content.
- **拉取时间**：2026-07-25 18:13:51

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Humanize-audit
##Humanize-audit — Linked In/blog Content Humanization Audit

A small open-source toolkit that scans text files (Markdown, plain text, CSV, JSON) and generates a humanization report for LinkedIn posts, blog articles, and other content.


It detects issues that make writing robotic/boring/over-optimized for SEO and suggests concrete fixes.

Features

Read files or directories and extract content (supports .md, .txt, .html, .csv, .json).

Heuristics for: passive voice, readability (Flesch), sentence length, filler words, marketing buzzwords, over-optimization signs, missing personalization, weak/absent CTA, excessive jargon, emoji usage.

Outputs: JSON report, pretty HTML report, and a short rewrite suggestion per flagged item.

Configurable rules (rules.yml) so maintainers and contributors can extend checks.
