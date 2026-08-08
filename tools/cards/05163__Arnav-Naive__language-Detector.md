---
id: tool-05163
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: language-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/arnav-naive/language-detector
created: 2026-07-18
updated: 2026-07-18
no: 5163
category: 一、去 AI 味 / Humanizer 库
repo: Arnav-Naive/language-Detector
stars: 1
url: https://github.com/arnav-naive/language-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 31e704dd7e0901e1
  - methods/改稿润色指令库.md
---

# Arnav-Naive/language-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/arnav-naive/language-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Linguist AI is a high-performance machine learning application designed to identify the language of any given text. Built using **Multinomial Naive Bayes** and **Natural Language Processing (NLP)** techniques, it can detect 22 different languages with high precision.
- **本地描述**：Linguist AI is a high-performance machine learning application designed to identify the language of any given text. Built using **Multinomial Naive Bayes** and **Natural Language Processing (NLP)** techniques, it can detect 22 different languages with high precision.
- **拉取时间**：2026-07-25 18:08:26

---

# 🌍 Linguist AI - Language Detection System

Linguist AI is a high-performance machine learning application designed to identify the language of any given text. Built using **Multinomial Naive Bayes** and **Natural Language Processing (NLP)** techniques, it can detect 22 different languages with high precision.

---

## 🚀 Key Features
- **Multilingual Support:** Detects 22 languages including English, Hindi, Spanish, French, Chinese, and more.
- **Micro-Cleaning Engine:** Advanced preprocessing that strips noise (numbers/special chars) while preserving linguistic integrity.
- **Premium Web Interface:** A sleek, glassmorphic UI built with Flask for real-time interaction.
- **Technical Rigor:** Follows a full ML lifecycle from EDA to deployment.

---

## 🛠️ Technical Architecture

### 1. The Algorithm: Multinomial Naive Bayes
The core detection engine uses the **Multinomial Naive Bayes (MNB)** classifier. 
- **How it works:** MNB is based on Bayes' Theorem and is particularly suited for text classification with discrete features (like word counts). 
- **Probabilistic Logic:** It calculates the probability of a text belonging to a specific language based on the frequency of its words relative to the overall dataset.
- **Efficiency:** Unlike deep learning models, MNB is extremely fast and effective for medium-sized text datasets.

### 2. NLP Technique: Bag of Words (BoW)
To convert text into numerical data that the algorithm can understand, we use **CountVectorizer**:
- It creates a **Vocabulary** of all unique words across 22,000 samples.
- Every input text is converted into a **Sparse Matrix** representing word frequencies.

### 3. Data Preprocessing
Before training, the raw dataset undergoes "Data Cleaning":
- **Normalization:** Converting all text to lowercase.
- **Noise Removal:** Stripping numbers and special characters to focus on alphabetic patterns unique to each language.
- **Standardization:** Removing extra whitespaces for consistent vectorization.

### 4. Evaluation Metrics
The model is evaluated using:
- **Accuracy Score:** Achieving over 91% accuracy on unseen test data.
- **Confusion Matrix:** Visualizing precisely where the model might confuse similar languages.
- **Classification Report:** Precision, Recall, and F1-score for every individual language.

---

## 📦 Project Structure
- `language detection.ipynb`: The research and development notebook (The "ML Back").
- `app.py`: The Flask production server for the web application.
- `train_model.py`: Utility script for model retraining and persistence.
- `model.pkl` & `vectorizer.pkl`: Serialized trained models for fast inference.
- `language.csv`: The core dataset (22,000 rows).

---

## 💻 Installation & Setup

1. **Clone the repository** (or navigate to the project folder).
2. **Install Dependencies:**
   ```bash
   pip install pandas numpy scikit-learn flask joblib matplotlib seaborn
   ```
3. **Run the Training (Optional):**
   ```bash
   python train_model.py
   ```
4. **Launch the Application:**
   ```bash
   python app.py
   ```
5. **Access the UI:** Open `http://127.0.0.1:5000` in your browser.

---

## 🌐 Supported Languages
The system supports 22 languages, including but not limited to:
- English
- Hindi
- Spanish
- French
- Chinese
- Russian
- Arabic
- Dutch
- Turkish
- ...and many more!

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*Built with ❤️*
