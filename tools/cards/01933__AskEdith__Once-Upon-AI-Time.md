---
id: tool-01933
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Once-Upon-AI-Time
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/askedith/once-upon-ai-time
created: 2026-07-18
updated: 2026-07-18
no: 1933
category: 二、网文 / 长篇 AI 写作系统 库
repo: AskEdith/Once-Upon-AI-Time
stars: 74
url: https://github.com/askedith/once-upon-ai-time
tier: "A"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AskEdith/Once-Upon-AI-Time

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/askedith/once-upon-ai-time
- **Stars**：74
- **语言**：Python
- **License**：None
- **Topics**：gpt-3, stable-diffusion, stablediffusion
- **GitHub 描述**：GPT-3 and Stable Diffusion powered short story generator
- **本地描述**：GPT-3 and Stable Diffusion powered short story generator
- **拉取时间**：2026-07-23 23:35:20

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Once Upon AI Time

Check out the demo: [http://onceuponaitime.com](http://onceuponaitime.com).

## Dependencies

You'll need an OpenAI account with access to GPT-3, and a Replicate (replicate.com) account.

## Setup

Set Environment Variables

```
export OPENAI_API_KEY=XXX
export REPLICATE_API_TOKEN=XXX
```

Install depencencies & run Once Upon AI Time

```
python3 -m pip install -r requirements.txt
streamlit run main.py
```

## Example

![Example Story](https://github.com/AskEdith/Once-Upon-AI-Time/blob/main/the_rock_president.jpeg)
