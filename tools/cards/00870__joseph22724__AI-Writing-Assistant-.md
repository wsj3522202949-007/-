---
id: tool-00870
type: tool
area: 库
status: active
tags: [校对, Java, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: AI-Writing-Assistant-
summary: 错别字/语法/风格校对
source: https://github.com/joseph22724/ai-writing-assistant-
created: 2026-07-18
updated: 2026-07-18
no: 870
category: 二、网文 / 长篇 AI 写作系统 库
repo: joseph22724/AI-Writing-Assistant-
stars: 0
url: https://github.com/joseph22724/ai-writing-assistant-
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 403663823e8b08a0
  - methods/最强写作方法论_全球最强综合版.md
---

# joseph22724/AI-Writing-Assistant-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/joseph22724/ai-writing-assistant-
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered writing tool with different modes
- **本地描述**：AI-powered writing tool with different modes
- **拉取时间**：2026-07-23 23:04:22

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-Writing-Assistant
AI-powered writing tool with different modes

## Setup
1. Java JDK 17 and Maven 
2. Get API key from https://aistudio.google.com/app/api-keys
3. go to/create "src/main/resources/config.properties " and add your key:

  api.key=" "
  
  api.url=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent
  
5. Run Main.java

## Features
- Creative writing mode
- Professional writing mode
- Academic writing mode
- Grammar Check mode
- Translation mode

## Design Patterns
- Strategy: Different writing modes
- Factory: Request creation
- Observer: UI updates using ActionListener

# Video Demos
## Ver 1.1
https://youtu.be/RTKqS4d6vFM

## Ver 1.0
https://youtu.be/GoUBtaMLi84 
