---
id: tool-05653
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/samuelalex3737/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5653
category: 一、去 AI 味 / Humanizer 库
repo: samuelalex3737/AI-Text-Detector
stars: 0
url: https://github.com/samuelalex3737/ai-text-detector
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
content_hash: 705844a75ea69ae3
  - methods/改稿润色指令库.md
---

# samuelalex3737/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/samuelalex3737/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：samuelalex3737/AI-Text-Detector
- **拉取时间**：2026-07-25 18:26:42

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 🕵️‍♂️ AI Text Detector

**Live Web App:** [AI Text Detector on Streamlit](https://ai-text-detector-upya3xfth6by324drtsl9b.streamlit.app/)  
**GitHub Repository:** [samuelalex3737/AI-Text-Detector](https://github.com/samuelalex3737/AI-Text-Detector)

## Overview
This is a flagship internal tool developed as a capstone activity for the Master of AI in Business (MAIB) program. The tool uses a fine-tuned **DistilBERT** sequence classifier to distinguish between human-written text (IMDB reviews) and AI-generated text (produced by GPT-2). 

It was built through a hands-on "adversarial minimax game" mimicking a Generative Adversarial Network (GAN) architecture:
1. **Round 1:** The base discriminator was trained on Human vs. AI text.
2. **Adversarial Red-Teaming:** The generator was used to create adversarial attacks (prompt injection, high temperature sampling, and light human editing) to fool the detector.
3. **Round 2:** The discriminator was retrained on the adversarial examples to patch the vulnerabilities, demonstrating the continuous arms race of AI detection.

## Features
- **Live Streamlit Interface:** A clean, user-friendly frontend allowing users to paste text and receive real-time inference.
- **Robust Model:** A fine-tuned `distilbert-base-uncased` model capable of running entirely on the CPU or seamlessly scaling to GPU.
- **Dynamic Chunking:** Overcomes GitHub's 100MB file limit by safely chunking the `model.safetensors` file into 45MB pieces and dynamically reassembling them at runtime on Streamlit Cloud.
- **Policy Disclaimers:** Built with strong product and policy judgment, explicitly warning users about false-positive rates, particularly regarding ESL and neurodivergent writers.

## Usage
Visit the [Live Web App](https://ai-text-detector-upya3xfth6by324drtsl9b.streamlit.app/) and paste at least 100 characters of text to test the model's confidence scores in real-time.

*Note: As this is a statistical model, it cannot guarantee 100% accuracy and is designed to trigger human review rather than automatic academic penalty.*
