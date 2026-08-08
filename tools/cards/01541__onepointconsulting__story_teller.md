---
id: tool-01541
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: story_teller
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/onepointconsulting/story_teller
created: 2026-07-18
updated: 2026-07-18
no: 1541
category: 二、网文 / 长篇 AI 写作系统 库
repo: onepointconsulting/story_teller
stars: 6
url: https://github.com/onepointconsulting/story_teller
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5460995b2856c9c6
  - methods/最强写作方法论_全球最强综合版.md
---

# onepointconsulting/story_teller

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/onepointconsulting/story_teller
- **Stars**：6
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Simple Tool Used to generate stories from plot descriptions using Gen AI models
- **本地描述**：Simple Tool Used to generate stories from plot descriptions using Gen AI models
- **拉取时间**：2026-07-23 23:24:03

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Teller

This is a small experiment of an app which can be used to generate epic stories using LLMs.

## Pre-requisites

You will need to have an [OpenAI API key](https://platform.openai.com/api-keys) and in case you want to use the My Midjourney API, a [MyMidjourney Token](https://www.mymidjourney.ai/setup).

## Installation instructions

Please make sure to install [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) first.

```bash
conda create -n story_teller python=3.12
conda activate story_teller
pip install poetry
poetry install
# This is important for PDF generation
playwright install
```

## Running unit tests

```bash
python -m unittest
```

## Running the command line application

```bash
python.exe ./story_teller/story_teller_main_cli.py
```

## Running the local GUI application

```bash
python .\story_teller\ui\wx\main.py
```

If you are on Windows and have Powershell installed, you can simply run this script:

```
.\start.ps1
```

## Fundamental Environment Variables

There are three expected environment variables:

```
OPENAI_API_KEY=<key>
TMP_FOLDER=<output folder for your stories>

MY_MIDJOURNEY_BEARER_TOKEN=<My Midjourney token (optional)>
```
