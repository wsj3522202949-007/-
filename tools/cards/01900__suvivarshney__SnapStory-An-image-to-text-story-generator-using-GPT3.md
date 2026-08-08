---
id: tool-01900
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: SnapStory-An-image-to-text-story-generator-using-GPT3
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/suvivarshney/snapstory-an-image-to-text-story-generator-using-gpt3
created: 2026-07-18
updated: 2026-07-18
no: 1900
category: 二、网文 / 长篇 AI 写作系统 库
repo: suvivarshney/SnapStory-An-image-to-text-story-generator-using-GPT3
stars: 6
url: https://github.com/suvivarshney/snapstory-an-image-to-text-story-generator-using-gpt3
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 111bdfc62a47fc7f
  - methods/最强写作方法论_全球最强综合版.md
---

# suvivarshney/SnapStory-An-image-to-text-story-generator-using-GPT3

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/suvivarshney/snapstory-an-image-to-text-story-generator-using-gpt3
- **Stars**：6
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI based story generation for ECS289G at UC Davis
- **本地描述**：AI based story generation for ECS289G at UC Davis
- **拉取时间**：2026-07-23 23:34:21

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SnapStory-An-image-to-text-story-generator-using-GPT3
AI based story generation for ECS289G at UC Davis. 

GPT3 from OPENAI requires a key to use, which is billable afte a few hits. We cannot add our key to a public repository. To add the key, got to src/gpt3 and in the line 15, in the function "def gpt3_init():" add your own key for GPT3.

To run the model, got to src/ and do 'flask run'. The front-end should be uo at the mentioned url, which by default is '127.0.0.1:5000'
