---
id: tool-05018
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Distilbert_ai_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ashchadha-iitg/distilbert_ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5018
category: 一、去 AI 味 / Humanizer 库
repo: AshChadha-iitg/Distilbert_ai_text_detector
stars: 1
url: https://github.com/ashchadha-iitg/distilbert_ai_text_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AshChadha-iitg/Distilbert_ai_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ashchadha-iitg/distilbert_ai_text_detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：AshChadha-iitg/Distilbert_ai_text_detector
- **拉取时间**：2026-07-25 18:03:06

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# DistilBERT AI Text Detector (updated)
This is a binary text classification model built on top of **distilbert-base-uncased**. It has been fine-tuned to distinguish between AI-generated and human-written text.


# Base model: 
DistilBERT (uncased)


# Task: Sequence classification

**Labels:**

0 → Human-written text

1 → AI-generated text


# Training Details:

Model is fine-tuned on a small custom dataset of **~1.4k samples**

**Batch size: 16**

**Epochs: 10**

**Learning rate: 5e-6**


# Performance:

**Accuracy: 0.5693 (~57%)**

**Precision: 0.6162**

**Recall: 0.9858**

**F1-score: 0.6814**


# Usage

Load the model and tokenizer with the Hugging Face Transformers library, provide a text input and the model will output a label indicating whether the text is AI-generated or human-written.


# Framework:

PyTorch, Hugging Face Transformers


# License: MIT License


# NOTE: 
This model is experimental and not intended for production use
