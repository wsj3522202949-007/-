---
id: tool-04834
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Phishing_Email_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/padmini2007/phishing_email_detector
created: 2026-07-18
updated: 2026-07-18
no: 4834
category: 一、去 AI 味 / Humanizer 库
repo: Padmini2007/Phishing_Email_Detector
stars: 0
url: https://github.com/padmini2007/phishing_email_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Padmini2007/Phishing_Email_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/padmini2007/phishing_email_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：🛡️ AI-powered Phishing Email Detector built with Python & Scikit-learn. Combines TF-IDF text analysis with URL/keyword feature engineering to classify emails as Phishing or Safe. Includes a RandomForest model, performance metrics (accuracy, confusion matrix, ROC curve), and a colorful interactive Streamlit web app.
- **本地描述**：🛡️ AI-powered Phishing Email Detector built with Python & Scikit-learn. Combines TF-IDF text analysis with URL/keyword feature engineering to classify emails as Phishing or Safe. Includes a RandomForest model, performance metrics (accuracy, confusion matrix, ROC curve), and a colorful interactive Streamlit web app.
- **拉取时间**：2026-07-25 17:56:09

---


# 🛡️ Phishing Email Detection Model

A machine learning project built with **Python** and **Scikit-learn** that classifies emails as **Phishing** or **Safe**, combining TF-IDF text analysis with engineered security features (URL count, suspicious keywords, IP-based links, etc.). Includes a `RandomForestClassifier`, full evaluation metrics, and an interactive **Streamlit** web app.

---

## DEMO_VIDEO_LINK :
https://drive.google.com/file/d/1WMLvWweeq01rDiGy4SwfvVSOn8tzet-4/view?usp=drivesd

---

## LIVE URL:
https://phishing-email-detector-1-qclo.onrender.com

---

## ✨ Features
- RandomForest classifier trained on TF-IDF + handcrafted features
- Detects suspicious URLs, IP-based links, and urgency/scare keywords
- Reports Accuracy, Precision, Recall, F1-score, Confusion Matrix, and ROC Curve
- Interactive Streamlit web app with live confidence scores
- Saved model artifacts (`.joblib`) for instant reuse

---

## 🛠️ Tech Stack
Python · Scikit-learn · Pandas · NumPy · Matplotlib/Seaborn · Streamlit · Plotly

---

## 📁 Project Structure

phishing_detector/

├── generate_dataset.py      # Creates the labeled email dataset

├── feature_engineering.py   # Extracts URL/keyword/structural features

├── phishing_detector.py     # Trains, evaluates, and saves the model

├── app.py                   # Streamlit web app

├── requirements.txt

└── README.md

---

## ⚙️ Installation
```bash
git clone https://github.com/<your-username>/phishing-email-detector.git
cd phishing-email-detector
pip install -r requirements.txt
```

---

## ▶️ Usage
```bash
python generate_dataset.py      # creates emails_dataset.csv
python phishing_detector.py     # trains, evaluates, saves model
python -m streamlit run app.py  # launches the web app
```

---

## 📈 Model Performance
On the included dataset (600 emails, 80/20 split): **~100% accuracy**.
> Note: the bundled dataset is synthetically generated for demo purposes — use a real-world dataset (e.g. from Kaggle) for a realistic benchmark.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👩‍💻 Author
**Developed by PADMINI J**

## 📄 License
MIT License — free to use, modify, and distribute with attribution.
