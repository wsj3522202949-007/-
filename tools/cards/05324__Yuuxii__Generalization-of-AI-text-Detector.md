---
id: tool-05324
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Generalization-of-AI-text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/yuuxii/generalization-of-ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5324
category: 一、去 AI 味 / Humanizer 库
repo: Yuuxii/Generalization-of-AI-text-Detector
stars: 3
url: https://github.com/yuuxii/generalization-of-ai-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4fb686b499bb79f5
  - methods/改稿润色指令库.md
---

# Yuuxii/Generalization-of-AI-text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/yuuxii/generalization-of-ai-text-detector
- **Stars**：3
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Yuuxii/Generalization-of-AI-text-Detector
- **拉取时间**：2026-07-25 18:14:23

---

# Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis

Source code for the paper  **[Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis](https://arxiv.org/pdf/2601.07974)**  
*(Accepted to EACL 2026)*

**Authors:** Yuxi Xia, Kinga Stańczak, Benjamin Roth

---

## Repository Overview

This repository contains the source code, benchmark dataset references, and analysis scripts accompanying our paper on **generalization in AI-generated text detection**.

The project investigates **why AI-text detectors often fail to generalize across language models, prompting strategies, and domains**, with a focus on **linguistic feature shifts** and **stylometric variation**.

---

## Generalization Benchmark Dataset

The benchmark dataset is publicly available on Hugging Face:

👉 **[AI-detector-generalization-benchmark](https://huggingface.co/datasets/yuxixia/AI-detector-generalization-benchmark)**

This dataset contains AI-generated texts produced by **7 large language models**, using **6 prompting strategies** across **4 text domains**.


### Dataset Composition

**AI-text generators:**

| Model Family | Model Variant | Provider |
|-------------|---------------|----------|
| Mistral | Mistral-Large-Instruct-2411 (123B) | Mistral AI |
| DeepSeek | DeepSeek-R1-Distill-Llama-70B | DeepSeek |
| Llama | Llama-3.3-70B-Instruct | Meta AI |
| Qwen | Qwen2.5-72B-Instruct | Alibaba |
| Qwen | Qwen2.5-32B-Instruct | Alibaba |
| Qwen | Qwen2.5-14B-Instruct | Alibaba |
| Solar | solar-propreview-instruct (22B) | Upstage |


**Prompting Strategies**

1. 0-shot  
2. 3-shot  
3. Style-conditioned  
4. 0-shot Chain-of-Thought (CoT)  
5. 1-shot Chain-of-Thought (CoT)  
6. Self-refine  

**Text Domains**

| Domain | Source Dataset |
|--------|----------------|
| Scientific Abstracts | arXiv |
| Product Reviews | AmazonReviews2023 |
| News Articles | CNN/Daily Mail |
| Question Answering | ASQA |


**Dataset Statistics**

| Property | Value |
|----------|-------|
| Examples per Domain | 3,000 |
| Total Source Examples | 12,000 |
| Train / Validation / Test Split | 50% / 17% / 33% |

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---


## Train AI-Text Detectors

Training commands are provided in:

```bash
train.sh
```

## Linguistic Analysis

Commands for extracting linguistic features are provided in:

```bash
linguistic_features.sh
```
Stylometric feature extraction:
```bash
stylometric_features.sh
```

## Results

Generalization results are under:
```bash
heatmap_acces/
```
Linguistic shifts result from training to test set:
```bash
heatmap_features/
```

Computed correlation results:
```bash
heatmap_corr/
```

The notebook for correlation analysis is provided in:
```bash
heatmap_corr.ipynb
```


## Citation

If you use this repository or dataset, please cite:

```bibtex
@misc{xia2026explaininggeneralizationaigeneratedtext,
  title={Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis},
  author={Yuxi Xia and Kinga Stańczak and Benjamin Roth},
  year={2026},
  eprint={2601.07974},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2601.07974}
}
```
