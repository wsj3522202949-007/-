---
id: tool-05241
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: language-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ivanlaulintiong/language-detector
created: 2026-07-18
updated: 2026-07-18
no: 5241
category: 一、去 AI 味 / Humanizer 库
repo: IvanLauLinTiong/language-detector
stars: 1
url: https://github.com/ivanlaulintiong/language-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8c820e51fa87b821
  - methods/改稿润色指令库.md
---

# IvanLauLinTiong/language-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ivanlaulintiong/language-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：ai, ai-applications-project, language-detection
- **GitHub 描述**：A language detector which can identify types of language based on written texts
- **本地描述**：A language detector which can identify types of language based on written texts
- **拉取时间**：2026-07-25 18:11:17

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Language Detector

![app.png](https://github.com/IvanLauLinTiong/language-detector/blob/main/app.png)

This app used pretrained [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) model and fine-tuned on the
[common_language](https://huggingface.co/datasets/common_language) dataset under PyTorch and HuggingFace framework. It can detect 45 languages based on user text input and is hosted on HuggingFace space platform.

## Fine-tuned Model

Download: [language-detection-fine-tuned-on-xlm-roberta-base](https://huggingface.co/ivanlau/language-detection-fine-tuned-on-xlm-roberta-base)

## Demo

Try it out: [language detector](https://huggingface.co/spaces/ivanlau/language-detection-xlm-roberta-base)

## Files Description

- `hf_demo`
  - repo for HuggingFace space app demo

- `datset`
  - folder where train and test dataset will be downloaded to.

- `xlm_roberta_base_commonlanguage_language_detector.ipynb`
  - notebook for fine-tuning xlm-roberta-base model
