---
id: tool-05145
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: PHISHING-EMAIL-DETECTOR-USING-AI-PROJECT
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shakar-afzal/phishing-email-detector-using-ai-project
created: 2026-07-18
updated: 2026-07-18
no: 5145
category: 一、去 AI 味 / Humanizer 库
repo: SHAKAR-AFZAL/PHISHING-EMAIL-DETECTOR-USING-AI-PROJECT
stars: 2
url: https://github.com/shakar-afzal/phishing-email-detector-using-ai-project
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# SHAKAR-AFZAL/PHISHING-EMAIL-DETECTOR-USING-AI-PROJECT

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shakar-afzal/phishing-email-detector-using-ai-project
- **Stars**：2
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered phishing email detector built with Python & Flask, achieving 95% accuracy. Demonstrates end-to-end ML pipeline from text preprocessing to real time web deployment.
- **本地描述**：AI-powered phishing email detector built with Python & Flask, achieving 95% accuracy. Demonstrates end-to-end ML pipeline from text preprocessing to real time web deployment.
- **拉取时间**：2026-07-25 18:07:47

---

# Phishing Email Detector Using AI/ML Powered Security

_An intelligent machine learning system that detects the phishing emails using Python and Flask to enhance cybersecurity and protect users from email-based attacks._

---

## Table of Contents
- [Overview](#overview)
- [Project Objective](#project-objective)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Methodology](#methodology)
- [Model Performance](#model-performance)
- [Web Application](#web-application)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)
- [Role & Contribution](#role--contribution)
- [Authors](#authors)

---

## Overview
Phishing emails are the one of the most common cybersecurity threats, often deceiving users into revealing sensitive information or downloading the malicious software.  

This project presents a **machine learning-based phishing email detector** that analyzes the email text and classifies it as **Phishing** or **Legitimate** through an interactive Flask Web Application.

---

## Project Objective
The primary goals of the project are:

- Build a reliable phishing email classification model  
- Transform raw email text into meaningful numerical features  
- Achieve high accuracy and recall in detection  
- Deploy user-friendly web interface for real-time predictions  
- Demonstrate an end-to-end ML pipeline  

---

## Dataset
🗂️ **Dataset File Used:** CEAS_08.csv  

The dataset contains **39,154 email records** with the labeled phishing and legitimate emails.

### Key Features
- Sender  
- Receiver  
- Date  
- Subject  
- Body  
- Urls  
- Label Used (1 = Phishing, 0 = Legitimate)

---

## Tools and Technologies
- **Python**
- **Scikit Learn**
- **Flask**
- **HTML**
- **CSS**
- **CountVectorizer**
- **Logistic Regression**
- **GitHub**

---

## Methodology

### Data Preprocessing
- Text Cleaning and Normalization  
- Feature extraction using **CountVectorizer**  
- Train test split (80/20)  

### Feature Engineering
CountVectorizer was used because it:

- Converts text into numerical vectors  
- Captures word frequency patterns  
- Works efficiently for email classification  

### Model Selection
Models evaluated:

- Logistic Regression ✅ (Selected)  
- Random Forest ❌ (Higher complexity)  
- SVM ❌ (Higher computational cost)  

**Final Choice:** Logistic Regression due to its simplicity, speed, and strong binary classification performance.

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | **95%** |
| Precision | **93%** |
| Recall | **97%** |

✅ High recall ensures phishing emails are rarely missed.

---

## Web Application

The project includes a responsive **Flask-based web interface**.

### Features
- Enter email content in a text box  
- Instant phishing classification  
- Clean and modern UI  
- Color-coded prediction results  
- Responsive layout  

<img width="498" height="437" alt="INTERFACE" src="https://github.com/user-attachments/assets/1ec27d5d-3b77-4b9e-8aab-72a5a3d3391f" />

### UI Improvements
- Centralized Design  
- Styled CSS Interface  
- Button hover Effects  
- Improved the Usability  

---

## Future Enhancements

- 🌍 Multilingual email detection  
- 📬 Real-time email service integration  
- 🤖 Transformer-based models (BERT, etc.)  
- ☁️ Cloud deployment  
- 🔌 REST API support  

---

## Conclusion
The machine learning model successfully detects phishing emails with high accuracy and recall. The combination of **CountVectorizer** and **Logistic Regression** provides a fast and efficient baseline solution.

This system can help the organizations to:

- Enhance overall email security 
- Reduce phishing risks  
- Automate threat detection  
- Boost user awareness and vigilance  

---

## Role And Contribution
- Problem Understanding  
- Data Preprocessing  
- Feature Engineering  
- Model Training & Evaluation  
- Flask App Development  
- UI Styling  
- Performance Analysis  
- End-to-End ML Implementation  

---

## Authors
**Mian Shakar Afzal**   &   **Muhammad Salman**  

[LinkedIn](https://www.linkedin.com/in/mian-shakar-afzal-959b443a8/) | [GitHub](https://github.com/SHAKAR-AFZAL) | [Email](mailto:mianshakarafzal@gmail.com)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
