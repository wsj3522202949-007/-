---
id: tool-04956
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Powered-Semantic-Plagiarism-Detection-System-for-Modified-Texts
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/bhumika609/ai-powered-semantic-plagiarism-detection-system-for-modified-texts
created: 2026-07-18
updated: 2026-07-18
no: 4956
category: 一、去 AI 味 / Humanizer 库
repo: Bhumika609/AI-Powered-Semantic-Plagiarism-Detection-System-for-Modified-Texts
stars: 0
url: https://github.com/bhumika609/ai-powered-semantic-plagiarism-detection-system-for-modified-texts
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Bhumika609/AI-Powered-Semantic-Plagiarism-Detection-System-for-Modified-Texts

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/bhumika609/ai-powered-semantic-plagiarism-detection-system-for-modified-texts
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-based plagiarism detector that identifies modified and paraphrased text using semantic similarity, NLP features, and XGBoost classification.
- **本地描述**：AI-based plagiarism detector that identifies modified and paraphrased text using semantic similarity, NLP features, and XGBoost classification.
- **拉取时间**：2026-07-25 18:00:49

---

# AI-Powered Semantic Plagiarism Detection for Modified Texts

## Overview

Traditional plagiarism detection systems rely heavily on exact text matching and often fail to identify paraphrased or modified content. This project presents an AI-powered semantic plagiarism detection system capable of detecting plagiarism even when the original text has been rephrased.

The system combines Natural Language Processing (NLP), Sentence Transformers, and Machine Learning techniques to analyze semantic meaning, sentence structure, keyword overlap, and grammatical patterns.

---

## Features

### Semantic Similarity Analysis
Uses Sentence-BERT (all-mpnet-base-v2) embeddings to compare the meaning of two texts rather than their exact wording.

### Keyword Overlap Detection
Measures common important words between documents.

### POS Structure Comparison
Compares Part-of-Speech patterns to identify structural similarities.

### Length Similarity Analysis
Checks similarity in sentence lengths and writing patterns.

### Machine Learning Classification
Uses XGBoost to classify text pairs as plagiarized or original.

### Interactive Dashboard
Built using Streamlit with:

- Semantic scores
- Keyword scores
- POS similarity scores
- Plagiarism percentage
- Visual charts
- Sentence-level highlighting

### PDF Report Generation
Generates downloadable plagiarism reports.

---

## System Architecture

Input Texts
      |
      V
Feature Extraction
      |
      |---- Semantic Similarity (Sentence-BERT)
      |---- Keyword Overlap
      |---- Length Similarity
      |---- POS Similarity
      |
      V
Feature Vector
      |
      V
XGBoost Classifier
      |
      V
Plagiarism Prediction
      |
      V
Dashboard + Visualization + PDF Report

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- XGBoost
- Scikit-Learn

### NLP
- Sentence Transformers
- SpaCy
- NLTK

### Visualization
- Matplotlib

### Web Framework
- Streamlit

### Report Generation
- ReportLab

---

## Dataset

The system is trained on sentence-pair datasets containing:

- Original sentences
- Modified/paraphrased sentences
- Binary plagiarism labels

Dataset columns:

- sentence1
- sentence2
- label

---

## Feature Engineering

The following features are extracted:

### Semantic Similarity
Cosine similarity between sentence embeddings.

### Keyword Overlap
Jaccard similarity between keyword sets.

### Length Similarity
Relative comparison of sentence lengths.

### POS Similarity
Comparison of grammatical structures using Part-of-Speech tags.

The final feature vector consists of:

```python
[
 semantic_similarity * 2,
 semantic_similarity²,
 semantic_similarity³,
 keyword_overlap,
 length_similarity,
 pos_similarity * 0.3
]
```

---

## Model

### XGBoost Classifier

Parameters:

```python
n_estimators=200
max_depth=5
learning_rate=0.1
```

The trained model is stored as:

```text
model.pkl
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/semantic-plagiarism-detector.git

cd semantic-plagiarism-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download NLP Models

```bash
python -m spacy download en_core_web_sm
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
├── app.py
├── model.py
├── features.py
├── train_model.py
├── evaluate.py
├── load_data.py
├── model.pkl
├── train.csv
├── val.csv
├── test.csv
├── requirements.txt
└── README.md
```

---

## Results

The system successfully identifies:

- Direct plagiarism
- Paraphrased plagiarism
- Sentence restructuring
- Synonym replacement
- Partial content copying

It provides:

- Plagiarism percentage
- Sentence-level matches
- Semantic similarity scores
- Visual analytics dashboard

---

## Applications

- Academic Integrity Checking
- Research Paper Verification
- Assignment Evaluation
- Content Originality Analysis
- Article Similarity Detection
- Educational Institutions

---

## Future Enhancements

- Deep Learning Classification Models
- Multi-language Support
- Real-time API Integration
- Large Document Comparison
- Explainable AI Visualization

---

## Authors

Developed as a Machine Learning and Natural Language Processing research project focused on detecting semantic plagiarism in modified texts.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

