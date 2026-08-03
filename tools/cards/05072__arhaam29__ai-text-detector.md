---
id: tool-05072
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/arhaam29/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5072
category: 一、去 AI 味 / Humanizer 库
repo: arhaam29/ai-text-detector
stars: 0
url: https://github.com/arhaam29/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# arhaam29/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/arhaam29/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：SEA 820 NLP Final Project – Detecting AI-Generated Text
- **本地描述**：SEA 820 NLP Final Project – Detecting AI-Generated Text
- **拉取时间**：2026-07-25 18:05:02

---

# ai-text-detector
# SEA820 NLP Final Project

```
Arhaam Khan
ana40@myseneca.ca
Seneca Polytechnic
```

## Overview
This project aims to classify text as **human-written** or **AI-generated** using two different approaches:
1. **Classic Machine Learning**: TF-IDF + Logistic Regression
2. **Transformer-based Fine-Tuning**: DistilBERT from Hugging Face Transformers

We compare the models in terms of accuracy, precision, recall, and F1-score.

---

## Dataset
- **Source:** Kaggle, AI vs Human Text Dataset
- **Labels: Generated Column**
  - `0.0`: Human-written
  - `1.0`: AI-generated
- Dataset was preprocessed with tokenization, stopword removal, punctuation stripping, and lemmatization.
- For Transformer fine-tuning, a **stratified 5,000-row sample** was used for efficiency.

---

## Methodology
### 1. Data Exploration & Preprocessing
- Downloaded and loaded the dataset.
-	Performed a thorough exploratory data analysis (EDA). Analyze text length, vocabulary, and class distribution.
-	Created a robust data preprocessing pipeline. 
-	Decided on tokenization, cleaning, and how to handle text lengths.

### 2. Classic Model (TF-IDF + Logistic Regression)
- Preprocessing: Tokenization, stopword removal, punctuation removal, lemmatization
- Feature extraction: TF-IDF vectorization
- Classifier: Logistic Regression (`scikit-learn`)
- Experiments with **full dataset** and **5K stratified subset**

### 3. Transformer Model (DistilBERT)
- Tokenization using `AutoTokenizer` from Hugging Face
- Fine-tuned for binary classification using `Trainer` API
- Used stratified 5K sample for faster training

---

## Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| TF-IDF + Logistic Regression (Full Dataset) | 0.95 | 0.97 | 0.89 | 0.93 |
| TF-IDF + Logistic Regression (5K Subset) | 0.87 | 1.00 | 0.65 | 0.79|
| DistilBERT (5K Subset) | 0.97 | 0.96 | 0.96 | 0.96 |

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Project Strcuture
```
├── NB1_classic_model.ipynb # Full dataset TF-IDF Logistic Regression
├── NB3_StratifiedSample_TF_IDF.ipynb # TF-IDF Logistic Regression on stratified 5K subset
├── NB2_Transformer_Model.ipynb # DistilBERT fine-tuning on stratified 5K subset
└──  README.md # Project description & usage
```

## How to run
```
1. Open the notebooks in colab.
2. Run each cell using Shift+Enter or manually run the cells
```
