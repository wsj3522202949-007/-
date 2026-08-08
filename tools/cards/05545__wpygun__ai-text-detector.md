---
id: tool-05545
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/wpygun/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5545
category: 一、去 AI 味 / Humanizer 库
repo: wpygun/ai-text-detector
stars: 0
url: https://github.com/wpygun/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: e181974cfb63ffdf
  - methods/改稿润色指令库.md
---

# wpygun/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/wpygun/ai-text-detector
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Chrome extension for real-time AI-generated text detection on social media
- **本地描述**：Chrome extension for real-time AI-generated text detection on social media
- **拉取时间**：2026-07-25 18:22:39

---

# AI Text Detector
 
> ⚠️ This project is currently in active development as part of my Bachelor's thesis at Vistula University.
 
A Chrome extension for real-time detection of AI-generated text on social media platforms.
 
## Goal
 
With the rapid rise of AI-generated content online, it's becoming increasingly difficult to distinguish human-written text from machine-generated text. This project aims to build a browser extension that detects AI-generated content in real time, directly in the user's browser while browsing social media.

## Planned features
 
- Real-time AI-generated text detection on Social media
- Visual highlighting of detected AI-generated content
- Confidence score displayed per post
- Lightweight UI

## Planned tech stack
 
**Backend API**
- Python
- Flask
 
**ML Model**
- RoBERTa (via HuggingFace Transformers)
- PyTorch

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

This project is developed as a Bachelor's thesis at Vistula University, Warsaw, under the working title:
*"A Browser Extension for Real-Time AI-Generated Content Detection on Social Media Platforms for Google Chrome"*
