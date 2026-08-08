---
id: tool-07559
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: cs577-project
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/subangkar/cs577-project
created: 2026-07-18
updated: 2026-07-18
no: 7559
category: 画龙补充 / 扩容入库 — 补充源
repo: subangkar/cs577-project
stars: 0
url: https://github.com/subangkar/cs577-project
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c60ef5beaceec576
  - methods/QUICK_START.md
---

# subangkar/cs577-project

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/subangkar/cs577-project
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：cs577-project
- **拉取时间**：2026-07-25 19:25:36

---

# AI Generated Text Detection Using Adversarial Learning

This repository contains the implementation of our CS577 project, where we explore improving the robustness of AI-generated text detection by using adversarial learning, inspired by the RADAR framework.

Original paper reference: [RADAR: Robust AI-text detection via adversarial learning](https://dl.acm.org/doi/10.5555/3666122.3666784)

---

## 🚀 Overview

Recent advancements in large language models (LLMs) have made it increasingly difficult to distinguish between machine-generated and human-written text. This project aims to:

* Investigate the robustness of AI-text detectors under adversarial paraphrasing.
* Develop a hybrid paraphrasing strategy combining backtranslation and neural paraphrasing.
* Train a distilBERT-based detector to classify texts as AI-generated or human-written.

---

## 📌 Features

* **Hybrid paraphrasing pipeline**: Combines multilingual backtranslation and lexical neural paraphrasing.
* **Adversarial training loop**: Reinforcement learning-based paraphraser competes against a binary classifier.
* **Evaluation on real-world data**: Includes a manually annotated dataset of LinkedIn posts.

---

## ⚙ Requirements

* Python >= 3.9
* PyTorch >= 2.6.0 with CUDA support
* HuggingFace `transformers` & `datasets`
* NLTK
* Helsinki-NLP models

---

## 🧰 Datasets

| Split      | Source                 | Count |
| ---------- | ---------------------- | ----- |
| Training   | OpenWebText (filtered) | 9,000 |
| Validation | OpenWebText (filtered) | 1,000 |
| Test       | LinkedIn posts         | 45    |

---

## 🚀 Implementation Details

### Hybrid Paraphrasing Pipeline

* **Backtranslation:** English → French → English using Helsinki-NLP.
* **Neural paraphrasing:** NLTK-based paraphraser to create more natural variations.

### Model Architecture

* **Detector:** `distilbert-base-uncased` binary classifier.
* **Paraphraser:** `t5-small` fine-tuned with PPO.

### Adversarial Training

* Paraphraser generates samples to fool the detector.
* Detector learns from these new samples to improve classification.

### Evaluation Metrics

* AUROC, Accuracy, F1, Precision, Recall.

---

## 🛠 Usage

```bash
git clone https://github.com/Subangkar/cs577-project.git
cd cs577-project

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt
```

Run training:

```bash
python radar.py
```

Run evaluation:

```bash
python radar_evaluate.py
```

related:
  - methods/QUICK_START.md
---

