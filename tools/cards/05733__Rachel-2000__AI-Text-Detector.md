---
id: tool-05733
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rachel-2000/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5733
category: 一、去 AI 味 / Humanizer 库
repo: Rachel-2000/AI-Text-Detector
stars: 0
url: https://github.com/rachel-2000/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Rachel-2000/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rachel-2000/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Rachel-2000/AI-Text-Detector
- **拉取时间**：2026-07-25 18:29:36

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Project Abstract

The emergence of advanced large-scaled language generation models, which are capable to produce natural and indistinguishable text, have drawn increasing attentions to the AI-text detectors that prevent malicious use of fake texts. However, the existing language model based detectors, in type of text classification models, are susceptible to adversarial examples, perturbed versions of the original text imperceptible by humans but can fool DL models. There is still lack of studies that explore the ability of AI-text detectors resisting to state-of-the-art text attack recipes. In this project, I trained a BERT-based detector and evaluate its robustness under seven edging black-box text classification attack methods. To enhance the detector's ability against attacks, I further perform adversarial training on the base detector and evaluate its effectiveness through adversarial attacks.

