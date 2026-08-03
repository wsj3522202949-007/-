---
id: tool-01354
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议传染, 本地优先, 英文文档, 改稿润色, 本地写作]
title: scrolls
summary: 风格微调/文风迁移
source: https://github.com/blackdchase/scrolls
created: 2026-07-18
updated: 2026-07-18
no: 1354
category: 二、网文 / 长篇 AI 写作系统 库
repo: BlackDChase/scrolls
stars: 14
url: https://github.com/blackdchase/scrolls
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# BlackDChase/scrolls

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/blackdchase/scrolls
- **Stars**：14
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：An AI powered story generator tool. Made for writers.
- **本地描述**：An AI powered story generator tool. Made for writers.
- **拉取时间**：2026-07-23 23:18:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# scrolls
- An AI powered story generator tool. Made for writers. Scrolls is a text editor specifically built to leverage the capabilities of NLG models that allow us to apply the feature of auto-complete not just to words, but also to sentences and paragraphs. This allows us to use auto-complete by predicting what could come next in a pattern of text, and then send suggestions to the user based on the input.

## DEMO
- This demo is symantically simmilar, but differs in terms of input and working. [Demo of Model][https://colab.research.google.com/drive/11rpFX6bC7Bw6oFZhmAedXhx_WMTNyV88]
- This demo is pure frontend and how this model is running. [Text Editor][https://github.com/BlackDChase/scrolls]
- Demo Model code in demo.py, runabel at google collab.
## How to train orignal
### Download the model
```
sh download_345.sh
```
### Finetuning
```
cd gpt-2/
sh finetune.sh
```
