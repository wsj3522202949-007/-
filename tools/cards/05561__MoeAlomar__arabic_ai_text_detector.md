---
id: tool-05561
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: arabic_ai_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/moealomar/arabic_ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5561
category: 一、去 AI 味 / Humanizer 库
repo: MoeAlomar/arabic_ai_text_detector
stars: 2
url: https://github.com/moealomar/arabic_ai_text_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: a22e9245b1c2e46d
  - methods/改稿润色指令库.md
---

# MoeAlomar/arabic_ai_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/moealomar/arabic_ai_text_detector
- **Stars**：2
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：MoeAlomar/arabic_ai_text_detector
- **拉取时间**：2026-07-25 18:23:15

---



# 🧠 Arabic AI Text Detector | كاشف النصوص العربية

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-4.0%2B-orange)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)

A robust machine learning application designed to distinguish between **Human-written** and **AI-generated** text in Arabic. This project features a dual-model approach, hosting both a lightweight **Hybrid XGBoost** model and a powerful **Fine-Tuned AraBERT** deep learning model in a single interface.

##  Live Demo
Try the app directly on Hugging Face Spaces:
**[Arabic AI Text Detectors Space](https://huggingface.co/spaces/MoeAlomar/Arabic_ai_text_detectors)**

---

## Models Overview

This repository implements two distinct approaches to AI detection:
### 1. Hybrid XGBoost Model (Statistical & Linguistic)
A high-performance classifier achieving **93.16% accuracy**. This model combines surface-level statistical patterns with deep morphological analysis to distinguish human nuances from AI consistency.

* **Input Processing:**
    * **Character N-grams (TF-IDF):** Captures surface features like punctuation habits, spacing, and orthography.
* **Linguistic Features:** Extracted using **Farasa** (specialized Arabic NLP toolkit), including:
    * **Morphological Ratios:** Frequency of Nouns, Verbs, Adjectives, Determiners, and Particles.
    * **Stylometric Stats:** Average Sentence Length, Word Length, and Type-Token Ratio (TTR).
    * **Unknown Token Ratio:** Specifically targets informal words, misspellings, and dialectal terms that AI models rarely generate.
* **Classifier:** XGBoost trained on the combined vector of N-grams and linguistic features.

### 2. Fine-Tuned AraBERT (Deep Learning)
A Transformer-based model optimized for understanding semantic context in Arabic.
* **Base Model:** `aubmindlab/bert-base-arabertv02`
* **Preprocessing:** Uses `ArabertPreprocessor` for text normalization.
* **Training:** Fine-tuned on a specialized dataset of human vs. AI Arabic text.

---

## Project Structure

```
arabic_ai_text_detector/
│
├── app.py                     # Main application file (Gradio UI)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
└── Models/                    # Trained Model Files
    ├── Hybrid_XGBoost_model/
    │   ├── hybrid_xgb.pkl               # The XGBoost Classifier (Joblib)
    │   ├── tfidf_vectorizer.pkl         # TF-IDF Vectorizer
    │   └── linguistic_feature_columns.pkl # Feature definitions
    │
    └── Fine_tuned_model/
        ├── config.json
        ├── pytorch_model.bin            # The Fine-Tuned BERT weights
        ├── tokenizer.json
        └── vocab.txt
```

-----

## 📦 Requirements

  * `gradio`
  * `xgboost`
  * `scikit-learn`
  * `pandas`
  * `numpy`
  * `spacy`
  * `torch`
  * `transformers`
  * `arabert`
  * `joblib`

--related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📝 Usage

1.  **Select a Tab:** Choose between the **Hybrid Model** (Statistical) or **AraBERT Model** (Deep Learning).
2.  **Input Text:** Paste the Arabic text you want to analyze into the text box.
3.  **Analyze:** Click the button to run the prediction.
4.  **View Results:** The model will display the probability of the text being "Human-Written" vs. "AI-Generated".


```
```
