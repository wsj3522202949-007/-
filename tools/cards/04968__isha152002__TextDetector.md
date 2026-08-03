---
id: tool-04968
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: TextDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/isha152002/textdetector
created: 2026-07-18
updated: 2026-07-18
no: 4968
category: 一、去 AI 味 / Humanizer 库
repo: isha152002/TextDetector
stars: 0
url: https://github.com/isha152002/textdetector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# isha152002/TextDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/isha152002/textdetector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A zero-shot AI-generated text detector built on the statistical properties of language model distributions. No training data. No fine-tuning. Generalises across models and domains.
- **本地描述**：A zero-shot AI-generated text detector built on the statistical properties of language model distributions. No training data. No fine-tuning. Generalises across models and domains.
- **拉取时间**：2026-07-25 18:01:18

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector — Zero-Shot Statistical Detection

A zero-shot AI-generated text detector built on the statistical properties of language model distributions. No training data. No fine-tuning. Generalises across models and domains.

## Core Idea

LLMs generate text by sampling from their own probability distributions — so AI-generated text consistently sits in high-probability regions of the model's distribution. Human text wanders into lower-probability, more individual territory.

This detector exploits that gap. For each token position, it measures how far the actual token sits above the model's typical output using a z-score, then averages across the passage to produce a single detection score.

One forward pass. No external models. No perturbations.

## Method

- Run text through a language model once to get conditional distributions at every token position
- At each position, compute the expected log-probability and variance under the model's own distribution
- Compute a z-score: how far does the actual token sit above typical?
- Average z-scores across all positions → final detection score
- Evaluate using AUROC — threshold-independent, class-imbalance robust

## Stack

- Python, PyTorch, HuggingFace Transformers
- Scoring model: GPT-Neo-2.7B
- Hardware: Kaggle free-tier T4 GPU

## Structure

```
├── core/
│   ├── scoring.py        # z-score computation
│   ├── sampling.py       # conditional distribution sampling
│   └── model.py          # model + tokenizer loading
├── evaluation/
│   ├── metrics.py        # AUROC, TPR, FPR
│   └── evaluate.py       # evaluation pipeline
├── data/
│   └── dataset_loader.py # dataset loading
├── inference/
│   └── infer.py          # single text inference
└── notebooks/
    └── detect.ipynb      # main Kaggle notebook
```

## Results

Evaluated on human vs AI-generated text across news, Wikipedia, and story writing domains.
Detailed results and ablations in `notebooks/detect.ipynb`.
