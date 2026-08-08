---
id: tool-05068
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AIvsHuman-TextDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/717824i312-cell/aivshuman-textdetector
created: 2026-07-18
updated: 2026-07-18
no: 5068
category: 一、去 AI 味 / Humanizer 库
repo: 717824i312-cell/AIvsHuman-TextDetector
stars: 0
url: https://github.com/717824i312-cell/aivshuman-textdetector
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
content_hash: 8fc10c002d76a498
  - methods/改稿润色指令库.md
---

# 717824i312-cell/AIvsHuman-TextDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/717824i312-cell/aivshuman-textdetector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：717824i312-cell/AIvsHuman-TextDetector
- **拉取时间**：2026-07-25 18:04:52

---

# 🧠 AI vs Human Text Detection System

## 📌 Project Overview

This project is a Machine Learning-based web application that classifies whether a given text is:

* Human-written
* AI-generated

It uses Natural Language Processing (NLP) techniques and classification algorithms to analyze text and provide prediction, confidence score, and decision level.

---

## 🚀 Features

* Text preprocessing (lowercase + punctuation removal)
* TF-IDF vectorization
* Machine Learning models:

  * Logistic Regression
  * Naive Bayes (for comparison)
* Confidence-based decision layer:

  * Acceptable
  * Needs Review
  * Likely AI-generated
* Web interface using Flask
* Word count analysis

---

## 🗂️ Project Structure

```
├── app.py
├── main.py
├── dataset.csv
├── dataset1.csv
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-text-detector.git
cd ai-text-detector
```

### 2. Install dependencies

```
pip install flask pandas scikit-learn
```

---

## ▶️ How to Run

### Run Flask App

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

### Run Model Training (Optional)

```
python main.py
```

---

## 🧪 Model Details

### Preprocessing

* Convert text to lowercase
* Remove punctuation

### Vectorization

* TF-IDF (Term Frequency - Inverse Document Frequency)

### Algorithms Used

* Logistic Regression (Primary)
* Multinomial Naive Bayes (Comparison)

---

## 📊 Decision Logic

| Confidence  | Decision            |
| ----------- | ------------------- |
| ≥ 0.80      | Acceptable          |
| 0.60 – 0.79 | Needs Review        |
| < 0.60      | Likely AI-generated |

---

## 📌 Example Output

```
Prediction: Human
Confidence: 0.85
Decision: Acceptable
Word Count: 120
Level: High
```

---

## 📈 Future Improvements

* Use deep learning models (LSTM, BERT)
* Improve dataset quality
* Add API support
* Deploy on cloud

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👩‍💻 Author

Deepa
