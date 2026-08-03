---
id: tool-01182
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: GPT2-api
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/richstokes/gpt2-api
created: 2026-07-18
updated: 2026-07-18
no: 1182
category: 二、网文 / 长篇 AI 写作系统 库
repo: richstokes/GPT2-api
stars: 29
url: https://github.com/richstokes/gpt2-api
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# richstokes/GPT2-api

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/richstokes/gpt2-api
- **Stars**：29
- **语言**：Python
- **License**：MIT
- **Topics**：ai, gpt, gpt-2, machinelearning, python, text-generation
- **GitHub 描述**：🤖 (Easily) run your own GPT-2 API. Post writing prompts, get AI-generated responses
- **本地描述**：🤖 (Easily) run your own GPT-2 API. Post writing prompts, get AI-generated responses
- **拉取时间**：2026-07-23 23:13:30

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

HTTP API that lets you make (concurrent) GPT-2 requests and receive the generated text output as JSON.

## Build n Run
`./bnr.sh`  

Uses a docker image to remove the complexity of getting a working python+tensorfloww environment working locally. 


## You can then send a request with 
```
curl --request POST --data '{"wp":"Never gonna give you up"}' http://localhost:2666/wp
```
