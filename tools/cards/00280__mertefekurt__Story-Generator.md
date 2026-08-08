---
id: tool-00280
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 本地写作]
title: Story-Generator
summary: 搭大纲/分卷/节拍
source: https://github.com/mertefekurt/story-generator
created: 2026-07-18
updated: 2026-07-18
no: 280
category: 二、网文 / 长篇 AI 写作系统 库
repo: mertefekurt/Story-Generator
stars: 0
url: https://github.com/mertefekurt/story-generator
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 14ec2bc16dbc71bc
  - methods/最强写作方法论_全球最强综合版.md
---

# mertefekurt/Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mertefekurt/story-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Powered Story Generator
- **本地描述**：AI Powered Story Generator
- **拉取时间**：2026-07-23 22:47:14

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Generator

![Story Generator cover](https://github.com/mertefekurt/Story-Generator/blob/main/assets/readme-cover.svg)

Long-form story drafting from a configurable outline.

## How it moves

![Workflow diagram](https://github.com/mertefekurt/Story-Generator/blob/main/assets/readme-diagram.svg)

## First session

```bash
git clone https://github.com/mertefekurt/Story-Generator.git
cd Story-Generator
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp theme.config theme.local.config
python story_generator.py --config theme.local.config
```

## Useful edges

- Designed as a focused desktop lab repo.
- Keeps setup short.
- Prioritizes readable output over infrastructure.

## Where to look

```text
.gitignore          project file
install_and_run.sh  project file
requirements.txt    runtime dependencies
story_generator.py  main generator
test_pdf.py         project file
```
