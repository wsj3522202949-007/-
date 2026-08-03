---
id: tool-04812
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Hybrid-AI-Generated-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/joeee14/hybrid-ai-generated-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4812
category: 一、去 AI 味 / Humanizer 库
repo: Joeee14/Hybrid-AI-Generated-Text-Detector
stars: 0
url: https://github.com/joeee14/hybrid-ai-generated-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Joeee14/Hybrid-AI-Generated-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/joeee14/hybrid-ai-generated-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**： a heterogeneous ensemble fusing RoBERTa semantic embeddings (768-d), TF-IDF n-grams (10,000-d), and a statistical  perplexity feature through a soft-voting classifier of linear and tree-based models. 
- **本地描述**：a heterogeneous ensemble fusing RoBERTa semantic embeddings (768-d), TF-IDF n-grams (10,000-d), and a statistical  perplexity feature through a soft-voting classifier of linear and tree-based models.
- **拉取时间**：2026-07-25 17:55:16

---

﻿# Hybrid AI-Generated Text Detector

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-yellow)](https://huggingface.co/transformers/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A reproduction and **extension** of the **SENTINEL** paper — a state-of-the-art hybrid ensemble system for detecting AI-generated essays, achieving **AUC-ROC 0.999** and **99.48% accuracy**, surpassing the original paper's reported results.

---

## Table of Contents

- [Overview](#overview)
- [Key Results](#key-results)
- [Architecture](#architecture)
- [Dataset](#dataset)
- [Pipeline](#pipeline)
- [Visualisations](#visualisations)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Team](#team)

---

## Overview

This project implements and extends the **SENTINEL** framework for detecting AI-generated text, originally introduced in the paper *"SENTINEL: A Robust Detection System for AI-Generated Text"*. The system fuses **semantic embeddings** (RoBERTa), **statistical features** (TF-IDF), and optionally **perplexity signals** (GPT-2) into a powerful multi-branch ensemble classifier.

The goal was to:
1. **Reproduce** the SENTINEL paper's 2-branch architecture (RoBERTa + TF-IDF).
2. **Improve** upon it by adding a 3rd perplexity-based branch.
3. **Explain** predictions using SHAP and LIME for interpretability.

---

## Key Results

| Method | AUC-ROC | Accuracy | Features |
|---|---|---|---|
| Paper SENTINEL (baseline) | 0.9685 | 94.98% | RoBERTa + TF-IDF |
| **Our SENTINEL (2-Branch)** | **0.9990** | **99.48%** | RoBERTa + TF-IDF |
| Enhanced SENTINEL (3-Branch) | 0.9992 | 99.60% | RoBERTa + TF-IDF + Perplexity |

> Our 2-branch replication **outperforms the original paper** on both AUC-ROC (+3.05%) and accuracy (+4.5%). The 3-branch extension further improves upon this.

### Individual Model OOF Performance (5-Fold CV)

| Model | AUC-ROC |
|---|---|
| Multinomial Naïve Bayes (MNB) | 0.9955 |
| SGD Classifier | 0.9946 |
| LightGBM | 0.9991 |
| CatBoost | 0.9985 |

---

## Architecture

### 2-Branch SENTINEL (Reproduction)

`
Raw Text
   ├── Branch 1: RoBERTa Embeddings (768-dim)  ─────┐
   └── Branch 2: TF-IDF Features (10,000-dim)  ──────┤
                                                      ▼
                          Hybrid Feature Matrix (10,768-dim)
                                                      ▼
                    Ensemble: MNB + SGD + LightGBM + CatBoost
                                                      ▼
                          Optuna-optimised Weighted Voting
                                                      ▼
                              Final Prediction (AI / Human)
`

### 3-Branch Enhanced SENTINEL

`
Raw Text
   ├── Branch 1: RoBERTa Embeddings  ───────────────────┐
   ├── Branch 2: TF-IDF Features    ────────────────────┤
   └── Branch 3: GPT-2 Perplexity Score  ───────────────┤
                                                         ▼
                            Enhanced Hybrid Feature Matrix
                                                         ▼
                        Ensemble Classifier + Optuna Tuning
`

---

## Dataset

| Source | Description | Size |
|---|---|---|
| Kaggle Official | Human-written student essays | 1,378 rows |
| External (DRCAT) | Mixed human & AI essays | 44,868 rows |
| **Final Training Set** | Balanced 50/50 (AI / Human) | **20,000 rows** |

**AI sources covered:** mistral7binstruct_v2, llama_70b_v1, cohere-command, and more.

---

## Pipeline

`
1. Data Loading & Merging
      ↓
2. Text Cleaning & Preprocessing
      ↓
3. Tokenisation (RoBERTa)  +  TF-IDF Vectorisation
      ↓
4. Feature Extraction
      ├─ RoBERTa Embeddings  (via pooler_output)
      ├─ TF-IDF Features     (10,000 n-grams)
      └─ [Optional] GPT-2 Perplexity Scores
      ↓
5. Hybrid Feature Concatenation  →  (20000 × 10768)
      ↓
6. 5-Fold Stratified Cross-Validation
      ├─ MNB  |  SGD  |  LightGBM  |  CatBoost
      ↓
7. Optuna Ensemble Weight Optimisation  (50 trials)
      ↓
8. Final Evaluation  +  Error Analysis
      ↓
9. Explainability  →  SHAP  +  LIME
`

---

## Visualisations

The following charts are included in the repository:

| File | Description |
|---|---|
| aseline_comparison.png | Our results vs. paper baseline |
| blation_study_results.png | Performance across feature ablations |
| eature_importance.png | Top features driving predictions |
| error_analysis.png | Breakdown of misclassified samples |
| perplexity_analysis.png | Perplexity distribution: AI vs. Human |
| lime_explanations.png | LIME local explanations |
| innovation_comparison.png | 2-branch vs. 3-branch comparison |

---

## Requirements

`ash
pip install torch transformers scikit-learn lightgbm catboost optuna shap lime pandas numpy matplotlib seaborn tqdm joblib scipy
`

> **GPU recommended** for RoBERTa embedding extraction. CPU fallback is supported but significantly slower.

---

## Usage

Open and run Research_implementation.ipynb sequentially. The notebook is divided into the following sections:

1. **Imports & Setup** — install and import all dependencies.
2. **Data Loading & Merging** — load official Kaggle data + external DRCAT data.
3. **Preprocessing** — clean text, tokenise with RoBERTa tokeniser.
4. **Feature Extraction** — generate RoBERTa embeddings and TF-IDF features.
5. **Hybrid Feature Fusion** — concatenate into a single feature matrix.
6. **Cross-Validation & Training** — 5-fold stratified CV with 4 base classifiers.
7. **Ensemble Optimisation** — Optuna hyperparameter search for blend weights.
8. **Evaluation** — AUC-ROC, accuracy, confusion matrix, error analysis.
9. **Explainability** — SHAP and LIME visualisations.
10. **3-Branch Extension** — add GPT-2 perplexity as a third branch.

> **Note:** Large intermediate files (*.pkl, large CSVs) are excluded from the repository via .gitignore. These are generated during the notebook run.

---

## Project Structure

`
.
├── Research_implementation.ipynb   # Main notebook (full pipeline)
├── train_essays.csv                # Official Kaggle training essays
├── baseline_comparison.csv         # Baseline comparison metrics
├── final_kfold_errors.csv          # Error analysis from K-fold CV
├── final_project_summary.csv       # Top-line results summary
├── ablation_study_results.png      # Ablation study chart
├── baseline_comparison.png         # Baseline comparison chart
├── error_analysis.png              # Error analysis chart
├── feature_importance.png          # Feature importance chart
├── innovation_comparison.png       # 2- vs 3-branch comparison
├── lime_explanations.png           # LIME explainability chart
├── perplexity_analysis.png         # Perplexity distribution chart
└── .gitignore
`

---

## Team

Developed as part of the **AIU Natural Language Processing** final project (AIE241).

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*Built with RoBERTa, TF-IDF, LightGBM, CatBoost, Optuna, SHAP, and LIME.*
