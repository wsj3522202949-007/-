---
id: tool-04891
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-vs-human-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/nancy-mk/ai-vs-human-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4891
category: 一、去 AI 味 / Humanizer 库
repo: Nancy-MK/ai-vs-human-text-detector
stars: 0
url: https://github.com/nancy-mk/ai-vs-human-text-detector
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
content_hash: e8b574829e0b97ee
  - methods/改稿润色指令库.md
---

# Nancy-MK/ai-vs-human-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/nancy-mk/ai-vs-human-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：bias-detection, explainable-ai, machine-learning, nlp, roberta, scikit-learn, shap
- **GitHub 描述**：Bias audit and SHAP explainability review comparing Naive Bayes, Logistic Regression, and fine-tuned RoBERTa on an imbalanced AI-vs-human text dataset.
- **本地描述**：Bias audit and SHAP explainability review comparing Naive Bayes, Logistic Regression, and fine-tuned RoBERTa on an imbalanced AI-vs-human text dataset.
- **拉取时间**：2026-07-25 17:58:17

---

# AI vs. Human Text Detector - NLP Bias Audit & Explainability Review

![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange) ![Transformers](https://img.shields.io/badge/HuggingFace-RoBERTa-yellow) ![SHAP](https://img.shields.io/badge/explainability-SHAP-red)

A model validation project that treats a text-classification task as a **risk and governance exercise**, not just an accuracy competition: quantifying dataset bias, comparing architectures on more than raw accuracy, and explaining *why* the best model makes its decisions before recommending it for use.

## Problem framing

Detecting AI-generated text is increasingly relevant to academic integrity, content moderation, and disclosure obligations under emerging AI regulation. A classifier that is "accurate" on an imbalanced dataset can still be a poor or unsafe choice if that accuracy is concentrated in the majority class. This project audits that risk directly rather than assuming it away.

## Dataset and bias audit

The working dataset contains **1,460 text samples**: **94% human-written** and **6% AI-generated**. A classifier that always predicts "human" would already score ~94% accuracy while being useless, so the first deliverable is a documented bias audit, not a model.

- Quantified the class imbalance and its effect on naive accuracy as a metric
- Applied **stratified sampling** for train/test splits so both classes are proportionally represented in every fold
- Selected evaluation metrics (precision, recall, F1, and confusion matrices) that stay meaningful under imbalance, rather than relying on accuracy alone
- Documented the mitigation decision and its trade-offs as a written control, in the same way a model risk review would record a decision and its rationale

## Models compared

| Model | Approach | Test accuracy |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Naive Bayes | TF-IDF features | 97.9% |
| Logistic Regression | TF-IDF features | 98.6% |
| RoBERTa (fine-tuned) | Transformer embeddings | Fine-tuned end-to-end; compared on interpretability and deployment cost, not accuracy alone |

Accuracy alone does not decide the "winner" here. The comparison is deliberately framed as a **deployment risk-profile assessment**: a simpler, fully interpretable TF-IDF + Logistic Regression pipeline is cheap to run and easy to audit, while a fine-tuned RoBERTa model may capture more nuance at the cost of transparency and compute. Which one is "better" depends on the regulatory and operational context it will be deployed into.

## Explainability (SHAP)

SHAP (SHapley Additive exPlanations) was applied to the trained models to identify which linguistic features actually drove each prediction, producing a written explainability review rather than just a notebook of plots:

- Token-level attribution for individual predictions (why *this* text was flagged as AI-generated)
- Global feature importance across the test set, to check whether the model is keying on genuine stylistic signals or on spurious artefacts of the dataset
- Findings written up as a short review report with recommendations, the same deliverable format used in model validation engagements

## Repository structure

```
ai-vs-human-text-detector/
  README.md
  requirements.txt
  src/
    bias_audit.py         # class-imbalance analysis and stratified split
    train_baselines.py    # TF-IDF + Naive Bayes / Logistic Regression
    train_roberta.py      # fine-tuning script for RoBERTa
    explainability.py     # SHAP-based interpretability analysis
```

## Getting started

```bash
git clone https://github.com/Nancy-MK/ai-vs-human-text-detector.git
cd ai-vs-human-text-detector
pip install -r requirements.txt

# 1. Audit the dataset for class imbalance
python src/bias_audit.py --data data/texts.csv

# 2. Train and evaluate the baseline models
python src/train_baselines.py --data data/texts.csv

# 3. Fine-tune RoBERTa (requires a GPU for reasonable runtime)
python src/train_roberta.py --data data/texts.csv

# 4. Generate SHAP explainability report for the chosen model
python src/explainability.py --model artifacts/logreg.joblib --data data/texts.csv
```

The dataset itself is not included in this repository; the scripts expect a CSV with `text` and `label` columns (`label` = 1 for AI-generated, 0 for human-written).

## Skills demonstrated

- Bias detection and algorithmic accountability
- Model validation across competing architectures
- SHAP-based explainability and audit-trail documentation
- Translating model behaviour into a deployment risk recommendation

## Tech stack

Python, scikit-learn, Hugging Face Transformers, PyTorch, SHAP, pandas, NumPy

## Licence

Developed for academic purposes. All rights reserved (c) Nancy Kamal.
