---
id: tool-05207
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Phishing-URL-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rajkumar3887/phishing-url-detector
created: 2026-07-18
updated: 2026-07-18
no: 5207
category: 一、去 AI 味 / Humanizer 库
repo: Rajkumar3887/Phishing-URL-detector
stars: 1
url: https://github.com/rajkumar3887/phishing-url-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Rajkumar3887/Phishing-URL-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rajkumar3887/phishing-url-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-based phishing URL detector that analyzes website links and predicts if they are safe or malicious. Uses machine learning models and text vectorization to identify suspicious patterns in real time with a lightweight Flask API.
- **本地描述**：AI-based phishing URL detector that analyzes website links and predicts if they are safe or malicious. Uses machine learning models and text vectorization to identify suspicious patterns in real time with a lightweight Flask API.
- **拉取时间**：2026-07-25 18:10:03

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

***

# AI-Based Phishing Email Detector

**A smart, presentation-ready Flask web application that detects phishing, spam, and malicious email content using advanced NLP + Machine Learning.**  
Built with Python, Flask, scikit-learn, TF-IDF vectorization, and a custom-trained classifier pipeline. Designed for easy local testing, demonstration, and deployment.

***

## 🖼️ Screenshots

## Project Screenshots

Here are some screenshots of the phishing URL detector in action.

![Dashboard View](https://github.com/Rajkumar3887/Phishing-URL-detector/blob/main/statics/screenshots/screenshot1.png%20"Dashboard%20View")

![Analysis Result](https://github.com/Rajkumar3887/Phishing-URL-detector/blob/main/statics/screenshots/screenshot2.png%20"Analysis%20Result")

![Analysis Result](https://github.com/Rajkumar3887/Phishing-URL-detector/blob/main/statics/screenshots/screenshot3.png%20"Analysis%20Result")
***

## AI Model Highlights

### 🚀 AI Model Overview

This project uses a robust machine learning pipeline built using advanced Natural Language Processing (NLP) techniques to detect phishing, scam, and spam patterns—even sophisticated social-engineering attacks.

The model analyzes text using:

- **TF-IDF Vectorization**: Learns important keywords, term frequency patterns, and context.  
- **Custom NLP Feature Extraction**: Identifies suspicious words such as *verify, urgent, account, alert*, financial scam keywords, and embedded URLs.  
- **Optimized Classifier Pipeline**: Uses Logistic Regression and complementary models with tuned hyperparameters, balanced classes, and calibrated probability scores.

### 🎯 Model Performance (Test Summary)

- Accuracy: ~96–98%  
- High Precision: Prevents false phishing alerts  
- High Recall: Detects hidden and cleverly written phishing attempts  
- ROC AUC: ~0.97–0.99  

Model performance is comparable to entry-level industry spam/phishing filters found in common email systems.

### 🧠 What Makes This Model Special?

- **Explainability Layer** highlights suspicious words, URLs, and patterns found in the message.  
- **Phishing Probability Score** gives detailed confidence levels (e.g., *“Phishing Probability: 92% — High Risk”*).  
- **Supports Any Message Type** including emails, SMS, WhatsApp messages, fake OTPs, job scams, bank alerts, and social media scam texts.  
- **Fast, Lightweight, No GPU Needed** — runs instantly on laptops.  
- **Ideal for Projects & Real Use** — perfect for cybersecurity demos, college projects, and portfolio showcases.

***

## Quick Demo (Local Setup)

1. Clone the repository and enter the directory.
2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
python app.py
```

5. Open the browser and visit:  
**http://127.0.0.1:5000**

***

## Project Structure (Key Files)

```
Phishing_Email_Detector/
├─ app.py                     # Flask web application
├─ train_model.py             # Script to retrain / improve model
├─ phishing_model.joblib      # Trained ML model
├─ vectorizer.joblib          # TF-IDF vectorizer
├─ requirements.txt           # Dependencies
├─ README.md                  # Project documentation
├─ templates/
│  ├─ index.html              # Input page UI
│  └─ result.html             # Output/result display
├─ static/
│  └─ screenshots/
│     ├─ screenshot1.png      # Added screenshot 1
│     ├─ screenshot2.png      # Added screenshot 2
│     └─ screenshot3.png      # Added screenshot 3
│  └─ CSS/
│     └─ style.css            # Custom UI theme
└─ logs/
   └─ predictions.csv         # Saved predictions (optional)
```

***

## Retraining or Improving the Model

To retrain:

```bash
python train_model.py
```

- Saves the updated model as `phishing_model.joblib`.  
- If any pickling issues occur, save the vectorizer and model separately.  
- Make sure both model files remain in the project root for Flask to load them.

***

## How the Web App Works (Brief)

- `index.html` — user enters email/message text.  
- Sends the text to `/predict` in `app.py`.  
- The message is cleaned, vectorized, and passed to the ML model.  
- Output shows:
  - Phishing or Legitimate status  
  - Probability score  
  - Highlighted suspicious keywords  
  - Extracted URLs  
- Optionally logs results in `logs/predictions.csv`.

***

## Deployment Options

Supports easy deployment on:

- **Render**
- **Railway**
- **Vercel (via serverless)**
- **Heroku (if enabled)**

For deployment, include a **Procfile**:

```
web: gunicorn app:app
```

Push to GitHub, connect to the platform, and deploy.

***

## Tips & Troubleshooting

- Add `venv/` to `.gitignore`.  
- Ensure CSS file is correctly linked:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='CSS/style.css') }}">
```

- Avoid lambdas in models to prevent pickling issues.  
- Exclude model files if you want private models on GitHub.

***

## Usage Examples (Test Inputs)

### Phishing Example

```
Subject: Alert! Unusual Login Attempt

Your account will be locked. Verify your identity immediately:
http://secure-auth-user.com/login
```

### Legitimate Example

```
Subject: Meeting Reminder

This is a reminder for tomorrow's project discussion at 11 AM.
```

***

## Credits & License

**Developed by Raj**  
A portfolio-ready cybersecurity and machine learning project.

***
