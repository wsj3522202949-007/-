---
id: tool-04990
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Custom-AI-Detector
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/genaiap/custom-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 4990
category: 一、去 AI 味 / Humanizer 库
repo: GenAIAP/Custom-AI-Detector
stars: 0
url: https://github.com/genaiap/custom-ai-detector
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# GenAIAP/Custom-AI-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/genaiap/custom-ai-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI detector aims to be humanizer-proof. Which means humanizing an AI text won't evade the detection of AI. If any of my friends find this, I really wonder how they found it because this is my alt account. I will keep it public for now
- **本地描述**：An AI detector aims to be humanizer-proof. Which means humanizing an AI text won't evade the detection of AI. If any of my friends find this, I really wonder how they found it because this is my alt account. I will keep it public for now
- **拉取时间**：2026-07-25 18:02:07

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

I will continue to update this repo if I can think of more ways to detect AI.
This is entirely vibe coded, but all the ideas and mechanics are mine.\
Still trying to figure out why the false positive rates are sooo high though AI texts generally get higher AI scores.

The current system uses a trajectory pattern detection system and it basically just find the direction and distance from a word to another word in the embedding space. Like up 1.0-> down 1.2 -> left 3.4 etc. The distance is calculated based on basic subtraction and I'm considering changing it to the similarity score like dot product in attention mechanism. I chose this mechanism instead of burstiness or perplexity like other AI detectors because this is more resistant to synonym swapping or sentence rephrasing as the trajectories still move in somewhat that direction after swapping with a synonym.

The Attention Mechanism part:
I don't understand this part, I told the AI to take inspirations from the attention mechanism for diverse text lengths adaptability but it kinda turned this into a transformer I think
