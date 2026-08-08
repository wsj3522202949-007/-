---
id: tool-05027
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AIPhishingDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/danishskh70/aiphishingdetector
created: 2026-07-18
updated: 2026-07-18
no: 5027
category: 一、去 AI 味 / Humanizer 库
repo: danishskh70/AIPhishingDetector
stars: 1
url: https://github.com/danishskh70/aiphishingdetector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3bf37fe15c7a1752
  - methods/改稿润色指令库.md
---

# danishskh70/AIPhishingDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/danishskh70/aiphishingdetector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai-security, bert, cybersecurity, deep-learning, distilbert, email-security, fraud-detection, huggingface, information-security, machine-learning, nlp, phishing-detection, pytorch, scikit-learn, spam-detection, text-classification
- **GitHub 描述**：This project is a simple command-line tool that analyzes email text and predicts whether the email is Phishing, Suspicious, or Legitimate. The goal of the project is to demonstrate how machine learning and modern NLP embeddings can be used to detect phishing emails in a practical, lightweight, and explainable way.
- **本地描述**：This project is a simple command-line tool that analyzes email text and predicts whether the email is Phishing, Suspicious, or Legitimate. The goal of the project is to demonstrate how machine learning and modern NLP embeddings can be used to detect phishing emails in a practical, lightweight, and explainable way.
- **拉取时间**：2026-07-25 18:03:25

---

<!-- # phishing-detector
This project is a simple command-line tool that analyzes email text and predicts whether the email is Phishing, Suspicious, or Legitimate. The goal of the project is to demonstrate how machine learning and modern NLP embeddings can be used to detect phishing emails in a practical, lightweight, and explainable way. -->
# AI Powered Phishing Email Detector

## Overview
A command-line tool that analyzes email text and predicts whether an email is Phishing, Suspicious, or Legitimate.
This project demonstrates how machine learning and modern NLP embeddings can be used to detect phishing emails in a practical, lightweight, and explainable way.

## What This Project Does
- Takes raw email text as input
- Converts the text into **semantic embeddings using DistilBERT**
- Uses a **Logistic Regression classifier** to predict phishing probability
- Outputs a **human-friendly verdict** with confidence

## Verdictsgit add .

- **LEGIT** --> (Safe email)
- **SUSPICIOUS** --> (Needs review)
- **PHISHING** --> (High risk)

## Tech Stack Used
- Python
- PyTorch
- HuggingFace Transformers (DistilBERT)
- Scikit-learn
- Pandas
- Joblib

## Why This Approach
Instead of using basic keyword matching or TF-IDF alone, this project uses **DistilBERT embeddings** to capture the **intent and context** of email text (urgency, threats, authority abuse).  
The **Logistic Regression classifier** keeps the system:
- Interpretable
- Lightweight
- Easy to debug
- Interview-friendly

## Project Structure
```
phishing-detector/
├── data/
│   └── emails/
│       └── combined.csv  # Dataset with email text & labels
├── model/
│   └── phishing_model.pkl  # Trained DistilBERT + Logistic Regression
├── train.py  # Training script
├── test.py   # CLI testing script
├── requirements.txt  # Python dependencies
└── README.md

```
## Python environment setup

```
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```
## Dataset Format
The CSV dataset must have two columns:
| Column | Description                      |
| ------ | -------------------------------- |
| text   | Email content                    |
| label  | 1 for phishing, 0 for legitimate |

## sample dataset
```
text,label
"Please verify your account immediately",1
"Team meeting at 5 PM today",0

```
## How Training Works
1. Load phishing email dataset
2. Tokenize emails using **DistilBERT tokenizer**
3. Generate embeddings from DistilBERT **CLS token**
4. Train **Logistic Regression** on embeddings
5. Evaluate accuracy
6. Save trained model using **Joblib**

## How Testing Works
1. Load saved model
2. Accept email text
3. Generate embedding using the same BERT model
4. Predict phishing probability
5. Convert probability into verdict

## Example Output
```
**Email:** Please verify your account immediately  
**Verdict:** PHISHING (High Risk)  
**Phishing Probability:** 99.93%

**Email:** Team meeting at 5 PM today  
**Verdict:** LEGIT  
**Phishing Probability:** 0.37%
```

## How to Run
1. Train the model:  
   ```
   python train.py
   ```
2. Test emails:  
   ```
   python test.py
   ```
## Model Evaluation Section
```
| Metric    | Score |
| --------- | ----- |
| Accuracy  | 96.4% |
| Precision | 95.1% |
| Recall    | 97.2% |
| F1-score  | 96.1% |
```
## Verdict Thresholds
| Probability | Verdict    |
| ----------- | -------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| 0 – 50%     | LEGIT      |
| 50 – 90%    | SUSPICIOUS |
| > 90%       | PHISHING   |


## Limitations
- Model is only as good as the dataset
- Some legitimate transactional emails may appear suspicious
- Does not analyze links, headers, or sender metadata

## Future Improvements
- Compare with TF-IDF baseline
- Add URL and domain analysis
- Add email header inspection
- Add simple web interface
- Add LLM-based explanation (optional)

