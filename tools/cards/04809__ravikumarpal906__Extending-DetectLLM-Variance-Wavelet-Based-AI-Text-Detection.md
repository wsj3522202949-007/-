---
id: tool-04809
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Extending-DetectLLM-Variance-Wavelet-Based-AI-Text-Detection
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ravikumarpal906/extending-detectllm-variance-wavelet-based-ai-text-detection
created: 2026-07-18
updated: 2026-07-18
no: 4809
category: 一、去 AI 味 / Humanizer 库
repo: ravikumarpal906/Extending-DetectLLM-Variance-Wavelet-Based-AI-Text-Detection
stars: 0
url: https://github.com/ravikumarpal906/extending-detectllm-variance-wavelet-based-ai-text-detection
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
content_hash: 332b654712ef84a7
  - methods/改稿润色指令库.md
---

# ravikumarpal906/Extending-DetectLLM-Variance-Wavelet-Based-AI-Text-Detection

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ravikumarpal906/extending-detectllm-variance-wavelet-based-ai-text-detection
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Extended DetectLLM (EMNLP 2023) with 4 novel zero-shot AI-text detectors — Log-Rank Variance, Normalized Perturbed Variance, DWT Variance, and LR-Diff — achieving up to 99.18% AUROC across GPT-Neo, GPT2-XL, and OPT-2.7B
- **本地描述**：Extended DetectLLM (EMNLP 2023) with 4 novel zero-shot AI-text detectors — Log-Rank Variance, Normalized Perturbed Variance, DWT Variance, and LR-Diff — achieving up to 99.18% AUROC across GPT-Neo, GPT2-XL, and OPT-2.7B
- **拉取时间**：2026-07-25 17:55:08

---

# Extending DetectLLM: Variance & Wavelet-Based AI Text Detection

> **CS590: Deep Learning** | IIT Guwahati | May 2026

A research project extending the [DetectLLM](https://arxiv.org/abs/2306.05540) framework (Su et al., EMNLP 2023) with four novel zero-shot detectors for machine-generated text, achieving up to **99.18% AUROC** — consistently outperforming existing baselines across 3 models and 3 datasets.

---

## Motivation

DetectLLM (LRR and NPR) characterizes text purely through the **mean** of word-rank sequences. We asked: *what if we also exploit the spread, shape, and frequency content of those rank sequences?* This project implements and evaluates four new metrics built on that intuition.

---

## Novel Methods Proposed

| Method | Type | Core Idea |
|--------|------|-----------|
| **LRV** — Log-Rank Variance | Zero-shot (no perturbation) | Variance of log-rank values across tokens; AI text has lower spread |
| **NPV** — Normalized Perturbed Variance | Perturbation-based | Ratio of variance in perturbed copies vs. original; AI text's rank spread changes more |
| **DWT Variance** | Zero-shot (no perturbation) | Variance of high-frequency wavelet detail coefficients (cD₁); human text has more "burstiness" |
| **LR-Diff** | Zero-shot (no perturbation) | Mean absolute difference between consecutive log-ranks; AI text flows more smoothly |

---

## Results (AUROC)

Tested on 150 samples per dataset, with 50 T5-Large perturbations for perturbation-based methods.

| Model | Dataset | DetectGPT | Log-Rank | LRR | NPR | **LR-Diff** | **NPV** | **LRV** | **DWT** |
|-------|---------|-----------|----------|-----|-----|-------------|---------|---------|---------|
| GPT-Neo 2.7B | XSum | 66.20% | 80.98% | 89.90% | 90.43% | 91.44% | **95.93%** | 93.06% | 94.33% |
| GPT-Neo 2.7B | SQuAD | 72.39% | 88.52% | 94.90% | 72.92% | 93.29% | 92.03% | **97.09%** | 95.38% |
| GPT-Neo 2.7B | WritingPrompts | 54.36% | 92.20% | 97.48% | 94.84% | 96.56% | **99.18%** | 98.17% | 98.00% |
| GPT2-XL | XSum | 63.61% | 76.95% | 85.71% | 91.28% | 86.19% | **95.00%** | 88.40% | 91.72% |
| GPT2-XL | SQuAD | 79.92% | 93.70% | 96.54% | 80.45% | 96.82% | 92.95% | 97.15% | **97.33%** |
| GPT2-XL | WritingPrompts | 53.07% | 94.23% | 96.26% | 96.44% | 96.93% | **98.46%** | 96.66% | 98.21% |
| OPT-2.7B | XSum | 60.00% | 71.73% | 77.76% | 88.68% | 82.58% | **92.71%** | 84.38% | 88.47% |
| OPT-2.7B | SQuAD | 74.21% | 85.97% | 91.42% | 79.32% | 90.97% | 89.14% | 91.57% | **93.86%** |
| OPT-2.7B | WritingPrompts | 58.74% | 83.25% | 88.50% | **95.02%** | 89.55% | 94.76% | 87.97% | 92.66% |

**Our four metrics win or tie the best baseline in 8 out of 9 test cases.**

---

## Experimental Setup

- **Scoring models:** GPT2-XL (1.5B), GPT-Neo 2.7B, OPT-2.7B
- **Perturbation model:** T5-Large (50 perturbations per sample)
- **Datasets:** XSum (news), SQuAD (Wikipedia), WritingPrompts (stories)
- **Protocol:** First 30 tokens used as prompt; model generates AI continuation at temperature 1.0; all 8 metrics evaluated; AUROC reported
- Identical setup to the original DetectLLM paper for direct comparability

---

## Key Takeaways

- **LRV and DWT are zero-shot** — they require only a single forward pass, with no expensive perturbation step, yet rival perturbation-based methods like NPR
- **NPV consistently delivers the highest AUROC** in most settings, especially on news and story domains
- Word rank sequences carry rich structural signal beyond their mean — variance and frequency decomposition expose it

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---


