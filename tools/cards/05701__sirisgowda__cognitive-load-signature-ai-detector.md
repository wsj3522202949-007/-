---
id: tool-05701
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: cognitive-load-signature-ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sirisgowda/cognitive-load-signature-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5701
category: 一、去 AI 味 / Humanizer 库
repo: sirisgowda/cognitive-load-signature-ai-detector
stars: 1
url: https://github.com/sirisgowda/cognitive-load-signature-ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sirisgowda/cognitive-load-signature-ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sirisgowda/cognitive-load-signature-ai-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：artificial-intelligence, catboost, feature-engineering, feature-extraction, machine-learning, nlp, optuna, python, text-classification
- **GitHub 描述**：AI vs Human Text Detection using Cognitive Load Signature features, CatBoost, and Explainable Machine Learning.
- **本地描述**：AI vs Human Text Detection using Cognitive Load Signature features, CatBoost, and Explainable Machine Learning.
- **拉取时间**：2026-07-25 18:28:25

---

# Cognitive Load Signature (CLS): AI vs Human Text Detection

## Overview

The **Cognitive Load Signature (CLS)** project is a Machine Learning and Natural Language Processing (NLP) system designed to distinguish between **AI-generated** and **human-written** text.

Instead of relying on transformer embeddings or simple stylistic patterns, this approach uses **11 engineered cognitive load and stylometric features** to capture characteristics of human writing. The extracted features are used to train a **CatBoost classifier**, with hyperparameters optimized using **Optuna**, resulting in a highly accurate and interpretable text classification pipeline.

This project demonstrates practical applications of feature engineering, supervised machine learning, model optimization, and performance evaluation.

---

# Features

- AI-generated vs Human-written text classification
- Cognitive Load Signature (CLS) feature engineering
- CatBoost-based classification model
- Automated hyperparameter optimization using Optuna
- Comparison with multiple baseline ML models
- ROC Curve and Confusion Matrix generation
- Feature importance analysis
- Cross-validation and reproducible experiments

---

# Cognitive Load Signature (CLS) Features

The model uses the following handcrafted linguistic and cognitive features:

| Feature | Description |
|----------|-------------|
| Repair Fraction | Measures self-correction patterns |
| Hedge Density | Detects uncertainty-related words |
| Clause Restart Frequency | Captures interrupted or restarted clauses |
| Syntactic Depth Variance | Measures variation in sentence complexity |
| Repetition Entropy | Quantifies repetition patterns |
| Pause Markers | Counts pause-related punctuation |
| Average Sentence Length | Average number of words per sentence |
| Type-Token Ratio | Vocabulary richness |
| Punctuation Density | Frequency of punctuation usage |
| Average Word Length | Average length of words |
| Lexical Diversity | Measures vocabulary diversity |

---

# System Architecture

```
                  Input Text
                       │
                       ▼
            Feature Extraction Pipeline
                       │
                       ▼
      11 Cognitive Load Signature Features
                       │
                       ▼
             Data Preprocessing
                       │
                       ▼
          Train/Test Split (80:20)
                       │
                       ▼
      Optuna Hyperparameter Optimization
                       │
                       ▼
             CatBoost Classifier
                       │
                       ▼
      AI / Human Text Classification
                       │
                       ▼
 Performance Evaluation & Visualization
```

---

# Technology Stack

## Programming Language

- Python

## Machine Learning

- CatBoost
- Scikit-learn
- XGBoost
- LightGBM
- Optuna

## Data Processing

- NumPy
- Pandas

## Visualization

- Matplotlib

## Model Persistence

- Joblib

---

# Baseline Models

The proposed CatBoost model is compared against multiple baseline classifiers:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting
- K-Nearest Neighbors (KNN)
- XGBoost
- LightGBM

---

# Dataset

The repository includes:

- Engineered Cognitive Load Signature feature dataset (`cls_features_full.csv`)
- Binary labels:
  - **0 → Human-written text**
  - **1 → AI-generated text**

The dataset consists of engineered linguistic features extracted from AI-generated and human-written text samples.

---

# Results

The CatBoost model achieved strong classification performance:

| Metric | Score |
|--------|-------:|
| Accuracy | ~92% |
| Precision | ~93% |
| Recall | ~95% |
| F1-Score | ~94% |
| ROC-AUC | ~0.97 |

The repository also includes:

- ROC Curve
- Confusion Matrix
- Feature Importance Plot
- Model Comparison
- Evaluation Metrics

---

---

# Visual Results

## Model Comparison

![Model Comparison](results/model_comparison.png)

## ROC Curve

![ROC Curve](results/figures/roc_curve.png)

## Confusion Matrix

![Confusion Matrix](results/figures/confusion_matrix.png)

## Feature Importance

![Feature Importance](results/figures/feature_importance.png)

# Project Structure

```
cognitive-load-signature-ai-detector/
│
├── train.py
├── cls_features_full.csv
├── requirements.txt
├── README.md
│
└── results/
    ├── all_model_results.csv
    ├── best_params.pkl
    ├── model_comparison.png
    │
    └── figures/
        ├── roc_curve.png
        ├── confusion_matrix.png
        └── feature_importance.png
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/sirisgowda/cognitive-load-signature-ai-detector.git

cd cognitive-load-signature-ai-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the experiment:

```bash
python train.py
```

---

# Output

Running the pipeline generates:

- Optimized CatBoost model
- Evaluation metrics
- Model comparison results
- Feature importance plot
- ROC Curve
- Confusion Matrix
- Best hyperparameters
- Saved prediction results

---

# Implementation

- Designed and implemented the complete machine learning pipeline.
- Performed feature engineering using Cognitive Load Signature (CLS) features.
- Implemented CatBoost training with Optuna-based hyperparameter optimization.
- Evaluated multiple baseline machine learning models.
- Generated performance visualizations and analysis.
- Structured the repository and documented the project.

---

# Future Improvements

- Deep learning and transformer-based approaches
- Real-time AI text detection API
- Support for multilingual datasets
- Explainable AI dashboard
- Web application deployment
- Larger and more diverse datasets

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# License

This project was developed for educational and research purposes.
