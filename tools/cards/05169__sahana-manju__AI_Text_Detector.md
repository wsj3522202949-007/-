---
id: tool-05169
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Text_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sahana-manju/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5169
category: 一、去 AI 味 / Humanizer 库
repo: sahana-manju/AI_Text_Detector
stars: 1
url: https://github.com/sahana-manju/ai_text_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sahana-manju/AI_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sahana-manju/ai_text_detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project aims to differentiate between AI-generated and human-written text. I implemented multiple machine learning models, including BERT, Multinomial Naive Bayes (MultinomialNB), Random Forest, and XGBoost, to classify text based on its origin.
- **本地描述**：This project aims to differentiate between AI-generated and human-written text. I implemented multiple machine learning models, including BERT, Multinomial Naive Bayes (MultinomialNB), Random Forest, and XGBoost, to classify text based on its origin.
- **拉取时间**：2026-07-25 18:08:40

---

# 🧠 AI Text Detector

## 🔍 Introduction

In recent times, the use of AI-generated content has exploded — from blog posts and essays to code and creative writing. As powerful as these tools are, there's a growing need to **distinguish between human-written and AI-generated text**. This project tackles that problem by building an **AI Text Detector** that can classify a piece of text as either AI- or human-generated.

---

## 📦 Dataset

The dataset used in this project was downloaded from Kaggle’s [LLM Detect AI-Generated Text Competition](https://www.kaggle.com/competitions/llm-detect-ai-generated-text/data). It contains a mix of AI- and human-written passages.

---

## 🧹 Preprocessing & Feature Engineering

To improve model performance, several structural and linguistic features were engineered:

- `text_length` – Total number of characters
- `mean_word_length` – Average word length
- `sentences` – Number of sentences
- `sentence_length` – Average length of a sentence
- `mean_sentence` – Mean sentence word count
- `unique_word_count` – Count of unique words
- `proper_noun_count` – Number of proper nouns
- `number_count` – Number of numeric tokens

Additionally, **common typos were replaced with the token `TYPO`**. This helped models learn that the presence of typos strongly correlates with human-written text, as AI-generated text tends to be grammatically cleaner.

---

## 🤖 Models Used

Multiple models were trained and evaluated using **3-fold cross-validation**:

| Model                    | Mean F1 Score |
|--------------------------|----------|
| Multinomial Naive Bayes  | 64%      |
| Random Forest            | 84%      |
| XGBoost                  | 82%      |
| **BERT** (Transformer)   | **97%**  |

BERT significantly outperformed traditional machine learning models by leveraging deep contextual understanding of language.

---

## ✅ Conclusion

The project demonstrates that combining classic NLP features (like typo detection and word counts) with advanced models like BERT can effectively distinguish AI-generated content from human-written text. BERT’s 99% accuracy highlights the power of transformers in understanding nuanced language patterns, especially when enhanced with thoughtful preprocessing.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---


