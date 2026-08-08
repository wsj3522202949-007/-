---
id: tool-00561
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/gautam-andani/story-generator
created: 2026-07-18
updated: 2026-07-18
no: 561
category: 二、网文 / 长篇 AI 写作系统 库
repo: gautam-andani/story-generator
stars: 1
url: https://github.com/gautam-andani/story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8092e460a491cc12
  - methods/最强写作方法论_全球最强综合版.md
---

# gautam-andani/story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gautam-andani/story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：django-application, openai-api
- **GitHub 描述**：Django backed web app which uses Open AI APIs to generate a story of his preference along with a suitable image.
- **本地描述**：Django backed web app which uses Open AI APIs to generate a story of his preference along with a suitable image.
- **拉取时间**：2026-07-23 22:55:25

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


# Story Generator

Django backed web app which uses Open AI APIs to generate a story of his preference along with a suitable image.


## Run

First of all add your api key in story_teller/story_teller/views.py Line 51

Now to run the webserver on localhost:

In project directory

```bash
  cd story_teller
  python3 manage.py runserver
```
Then open this url in browser

http://127.0.0.1:8000/
