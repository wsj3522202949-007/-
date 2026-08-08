---
id: tool-05677
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-news-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sinpacchan/ai-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 5677
category: 一、去 AI 味 / Humanizer 库
repo: sinpacchan/ai-news-detector
stars: 1
url: https://github.com/sinpacchan/ai-news-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: c04802bf9855560b
  - methods/改稿润色指令库.md
---

# sinpacchan/ai-news-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sinpacchan/ai-news-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Automatic tool for Chromium based browser to detect misinformation and AI-generated text.
- **本地描述**：Automatic tool for Chromium based browser to detect misinformation and AI-generated text.
- **拉取时间**：2026-07-25 18:27:33

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

This is the code for Google Chrome browser extension that automatically detects if a news article is written by an AI, and if it contains misinformation.

This is a small sideproject I created to support my final thesis regarding AI and fake news detection for my Master's program at Kitami Institute of Technology, Japan.

To detect the articles, I have trained a BERT base model using fake and true articles written by both humans and AI-tools.

If you're going to use the extension, please take into consideration that the results are only predictions based on the pretrained model, so it is prone to make mistakes, especially since this extension is currently in very early development.

Consider buying me a coffee at: https://buymeacoffee.com/laslan07 to support my work in creating this tool more robust.
