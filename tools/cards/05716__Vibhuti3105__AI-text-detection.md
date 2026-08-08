---
id: tool-05716
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-text-detection
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/vibhuti3105/ai-text-detection
created: 2026-07-18
updated: 2026-07-18
no: 5716
category: 一、去 AI 味 / Humanizer 库
repo: Vibhuti3105/AI-text-detection
stars: 1
url: https://github.com/vibhuti3105/ai-text-detection
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8c8c1490adaf7df6
  - methods/改稿润色指令库.md
---

# Vibhuti3105/AI-text-detection

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vibhuti3105/ai-text-detection
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Generated Text Detection system using a fine-tuned BERT model to classify human-written vs LLM-generated text. Implemented as a black-box detector with robustness and failure-mode analysis, and runnable locally via a Streamlit interface.
- **本地描述**：AI-Generated Text Detection system using a fine-tuned BERT model to classify human-written vs LLM-generated text. Implemented as a black-box detector with robustness and failure-mode analysis, and runnable locally via a Streamlit interface.
- **拉取时间**：2026-07-25 18:28:58

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-Generated Text Detection using BERT

A machine learning system that detects whether a given text is human-written or AI-generated using a fine-tuned BERT-based sequence classification model. The project focuses on black-box AI-text detection, robustness analysis, and real-world failure modes.

## ✨ Key Features

**Black-Box AI-Text Detection**
Detects AI-generated text without relying on watermarking or model internals.

**BERT-Based Classification**
Fine-tuned BERT model captures semantic, lexical, and syntactic patterns to distinguish human and LLM-generated text.

**Robust Dataset Curation**
Trained on 35,500+ samples aggregated from multiple public datasets, including adversarial and diverse writing styles.

**Interactive Web Interface**
Streamlit-based UI for real-time inference and probability scoring.

## 🧠 How It Works (High Level)

**Preprocessing**
Text is normalized and tokenized using BERT-compatible preprocessing.

**Model Inference**
A fine-tuned BERT sequence classification model predicts the probability of AI-generated content.

**Decision Layer**
Outputs a probability score (0–1) along with a human/AI classification, optimized for low false-positive rates.

## 📊 Model Details

**Architecture**: BERT (Bidirectional Encoder Representations from Transformers)

**Training Data**: Mixed dataset of human-written and AI-generated essays

**Dataset Size**: 35,500+ samples

**Evaluation Metric**: F1-Score (98.2% on benchmark datasets)

**Output**: Probability score ∈ [0, 1]

## ⚠️ Known Limitations & Failure Modes

Performance degrades on heavily corrupted or typo-rich text, where token embeddings become unreliable.

Distribution shift between training and unseen test data can affect confidence calibration.

In some noisy scenarios, simpler lexical models (e.g., TF-IDF) may outperform deep models.

## 🛠️ Tech Stack

**Frontend**: Streamlit

**Backend**: TensorFlow 2.15

**Model**: BERT via TensorFlow Hub

**Language**: Python 3.10

## 🚀 Local Development

```bash
# Clone the repository
git clone https://github.com/Vibhuti3105/AI-text-detection.git
cd AI-text-detection

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/streamlit_app.py
```
