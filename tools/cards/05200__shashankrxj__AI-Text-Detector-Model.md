---
id: tool-05200
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector-Model
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shashankrxj/ai-text-detector-model
created: 2026-07-18
updated: 2026-07-18
no: 5200
category: 一、去 AI 味 / Humanizer 库
repo: shashankrxj/AI-Text-Detector-Model
stars: 1
url: https://github.com/shashankrxj/ai-text-detector-model
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: bc5ce1fb04a713dd
  - methods/改稿润色指令库.md
---

# shashankrxj/AI-Text-Detector-Model

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shashankrxj/ai-text-detector-model
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：flask, lightgbm, logistic-regression, naive-bayes, natural-language-processing, python, random-forest, text-classification, tf-idf-vectorizer
- **GitHub 描述**：This is the code for the implementation of a Machine Learning model that classifies whether the given text is AI-generated or human-written.
- **本地描述**：This is the code for the implementation of a Machine Learning model that classifies whether the given text is AI-generated or human-written.
- **拉取时间**：2026-07-25 18:09:47

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detection Model
## Introduction
This project aims to develop a robust solution for detecting whether a piece of text was written by an AI or a human. It leverages machine learning classifiers such as RandomForest, LightGBM, Naive Bayes, and Logistic Regression, using TF-IDF vectorization for feature extraction. Two separate models (bigram and unigram) are built, allowing flexible choices based on feature representation.

## Model Architecture
### Unigram Model
The unigram model extracts unigram (single-word) features using TF-IDF. It employs two classifiers:<br>

1. Naive Bayes<br>
2. Logistic Regression<br>

The final prediction is based on an ensemble approach where the probabilities from both models are averaged to give a combined prediction.

### Bigram Model
The bigram model extracts bigram (word-pair) features from the text using TF-IDF. It utilizes two classifiers:<br>

1. RandomForest<br>
2. LightGBM<br>

Like the unigram model, the final prediction is based on the average of probabilities from both classifiers.

## Dataset
The model was trained on a dataset consisting of over 450,000 text samples, both AI-generated and human-written. The features for the model are extracted using TF-IDF with unigrams and bigrams.
find the dataset on [Kaggle](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text).
