---
id: tool-07597
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 中文友好, 本地写作]
title: markdowntoindesignxml
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/waneen/markdowntoindesignxml
created: 2026-07-18
updated: 2026-07-18
no: 7597
category: 画龙补充 / 扩容入库 — 补充源
repo: waneen/markdowntoindesignxml
stars: 0
url: https://github.com/waneen/markdowntoindesignxml
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 902e692ea8c2ed68
  - methods/QUICK_START.md
---

# waneen/markdowntoindesignxml

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/waneen/markdowntoindesignxml
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Markdown file(.md)をIndesignで読み込むスクリプトです。
- **本地描述**：markdowntoindesignxml
- **拉取时间**：2026-07-25 19:26:47

related:
  - methods/QUICK_START.md
---

# MarkdownToInDesignXML
Markdown file(.md)をIndesignで読み込むスクリプトです。

## 要求
pandocをcmdから使用しています。

## 現在の仕様
対応しているタグ
 - p　（Articleタグに置換されます）
 - br
 - h1,h2.h3,etc
 - pre code （bmsタグに置換されます）
 - table
