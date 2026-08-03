---
id: tool-05537
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Plagiarism-Detector-Pro
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/alpha-cassius/plagiarism-detector-pro
created: 2026-07-18
updated: 2026-07-18
no: 5537
category: 一、去 AI 味 / Humanizer 库
repo: Alpha-Cassius/Plagiarism-Detector-Pro
stars: 1
url: https://github.com/alpha-cassius/plagiarism-detector-pro
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Alpha-Cassius/Plagiarism-Detector-Pro

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/alpha-cassius/plagiarism-detector-pro
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Plagiarism Detector Pro is a powerful and intuitive application designed to analyze and detect plagiarism in text documents. This tool allows users to upload CSV files containing source and plagiarized text samples, train AI models using machine learning techniques, and accurately classify text as original or plagiarized.
- **本地描述**：Plagiarism Detector Pro is a powerful and intuitive application designed to analyze and detect plagiarism in text documents. This tool allows users to upload CSV files containing source and plagiarized text samples, train AI models using machine learning techniques, and accurately classify text as original or plagiarized.
- **拉取时间**：2026-07-25 18:22:21

---

# 📜 Plagiarism Checker & CSV Model Trainer

This project consists of two applications:
1. **Plagiarism Checker** 🕵️‍♂️: A GUI tool to detect plagiarism in text using a trained machine learning model.
2. **CSV Model Trainer** 📊: A GUI tool to load, edit, and train a plagiarism detection model using CSV data.

---

## 🚀 Features
### Plagiarism Checker
- 🔍 Detects plagiarism using a trained ML model.
- 📄 Allows text input for analysis.
- ✅ Provides clear feedback on plagiarism detection.
- 🎨 User-friendly interface with a modern dark theme.

### CSV Model Trainer
- 📂 Load and process CSV files with text data.
- ✏️ Edit dataset entries (add/delete rows).
- 🏋️ Train a model using **Logistic Regression, Random Forest, or SVM**.
- 💾 Save the trained model for use in the Plagiarism Checker.

---

## 🛠 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Alpha-Cassius/Plagiarism-Detector-Pro.git
   cd Plagiarism-Detector-Pro
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the applications**:
   - Plagiarism Checker:
     ```bash
     python app.py
     ```
   - CSV Model Trainer:
     ```bash
     python train.py
     ```

---

## 🏗 How It Works
### Plagiarism Detection Flow
1. User enters text.
2. The text is vectorized using **TF-IDF**.
3. The trained model predicts whether the text is plagiarized or not.
4. The result is displayed with color-coded feedback.

### Training Model Flow
1. Load a CSV file containing `source_text`, `plagiarized_text`, and `label`.
2. Select a machine learning algorithm (**Logistic Regression, Random Forest, SVM**).
3. Train the model and evaluate accuracy.
4. Save the trained model for use in the Plagiarism Checker.

---

## 📂 File Structure
```
📁 plagiarism-checker/
│── app.py              # Plagiarism Checker GUI
│── train.py            # CSV Model Trainer GUI
│── model.pkl           # Saved ML model (generated after training)
│── vectorizer.pkl      # TF-IDF vectorizer (generated after training)
│── requirements.txt    # Required dependencies
```

---

## 📜 License
This project is open-source and available for personal and educational use.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👨‍💻 Author
Developed by **Vaibhav Pandey**. 🚀

