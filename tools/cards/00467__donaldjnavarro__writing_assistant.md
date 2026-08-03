---
id: tool-00467
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: writing_assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/donaldjnavarro/writing_assistant
created: 2026-07-18
updated: 2026-07-18
no: 467
category: 二、网文 / 长篇 AI 写作系统 库
repo: donaldjnavarro/writing_assistant
stars: 0
url: https://github.com/donaldjnavarro/writing_assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# donaldjnavarro/writing_assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/donaldjnavarro/writing_assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：exe, python, writing
- **GitHub 描述**：Analysis tools for reviewing written works
- **本地描述**：Analysis tools for reviewing written works
- **拉取时间**：2026-07-23 22:52:42

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# WRITING ASSISTANT APP

App that analyzes a block of text and gives some metrics and visualization to give writers perspective on their writing.

## Getting Started

### Launch Virtual Environment

Do this first, whether running in python or generating EXEs.

```bash
.\venv\Scripts\activate
```

### Run without EXE

```bash
python main.py
```

### Create new EXE

Build command. Version numbers will be generated based on existing file versions in the `dist/` folder.

```bash
python scripts/build.py
```

Deprecated build command:
~~pyinstaller --onefile main.py~~

## Framework Overview

### Architecture

`main.py` The main python file

`main.spec` Config file for the EXE compiler

`scripts/build.py` Handles the versioning and other particulars of new EXE builds

`dist/` Where new EXEs will be created

`requirements.txt` pip package manager config

### Tools

* **Package manager**: PIP
* **EXE**: PyInstaller
* **UI**: wxPython
