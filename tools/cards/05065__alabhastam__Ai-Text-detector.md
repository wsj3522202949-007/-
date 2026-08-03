---
id: tool-05065
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Ai-Text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/alabhastam/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5065
category: 一、去 AI 味 / Humanizer 库
repo: alabhastam/Ai-Text-detector
stars: 0
url: https://github.com/alabhastam/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# alabhastam/Ai-Text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/alabhastam/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Ai-Text-detector
- **本地描述**：Ai-Text-detector
- **拉取时间**：2026-07-25 18:04:46

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Human vs AI Text Classifier (LSTM)

Classify text as human- or AI-generated with an LSTM neural network (TensorFlow/Keras) and also classic models.

- **Dataset:** CSV with `text` and `generated` (0=human, 1=AI) columns
- **How to run:**  
  1. Install requirements: `pip install numpy pandas scikit-learn tensorflow matplotlib`  
  2. Edit and run `main.py` or the Jupyter notebook with your data

**Results:** Confusion matrix, classification report, and training accuracy plot. we got around 99 percent acc.

[Made by [Ali_Abdollahi](https://kaggle.com/Ali_Abdollahi)
