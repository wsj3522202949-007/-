---
id: tool-04818
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: TextShield
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/utkarsh212004/textshield
created: 2026-07-18
updated: 2026-07-18
no: 4818
category: 一、去 AI 味 / Humanizer 库
repo: Utkarsh212004/TextShield
stars: 0
url: https://github.com/utkarsh212004/textshield
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
content_hash: 5ab2dd4c492f8035
  - methods/改稿润色指令库.md
---

# Utkarsh212004/TextShield

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/utkarsh212004/textshield
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered fake news and spam detector using NLP, TF-IDF and Logistic Regression — built with Python and Streamlit
- **本地描述**：AI-powered fake news and spam detector using NLP, TF-IDF and Logistic Regression — built with Python and Streamlit
- **拉取时间**：2026-07-25 17:55:29

---

# 🛡️ TextShield — AI Fake News & Spam Detector

> NLP-powered text classifier built with Python, Scikit-learn and Streamlit

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-orange?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat)

## 🎯 What it does
- 🗞️ **Fake News Detector** — Classifies news articles as real or fake
- 📩 **Spam Detector** — Classifies SMS/email messages as spam or legitimate

## 📊 Model Performance
| Task | Algorithm | Accuracy | F1 Score |
|------|-----------|----------|-------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Fake News | Logistic Regression | ~99% | 0.991 |
| Spam Detection | Logistic Regression | ~98% | 0.982 |

## 🗃️ Datasets
- **ISOT Fake News Dataset** — 44,898 news articles
- **SMS Spam Collection** — 5,574 messages

## 🛠️ Tech Stack
- **Language:** Python
- **ML:** Scikit-learn, NLTK
- **Vectorization:** TF-IDF (5,000 features, bigrams)
- **Models:** Logistic Regression, Naive Bayes, Linear SVM
- **App:** Streamlit
- **Version Control:** Git & GitHub

## 🚀 How to run locally
```bash
git clone https://github.com/Utkarsh212004/TextShield.git
cd TextShield
pip install -r requirements.txt
streamlit run app.py
```

## 👨‍💻 Built by
**Utkarsh Jain** — MCA AI & Data Science  
JECRC University, Jaipur
