---
id: tool-05589
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Plagiarism_AI_Detector_Frontend
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/kevin-savaliya/plagiarism_ai_detector_frontend
created: 2026-07-18
updated: 2026-07-18
no: 5589
category: 一、去 AI 味 / Humanizer 库
repo: kevin-savaliya/Plagiarism_AI_Detector_Frontend
stars: 2
url: https://github.com/kevin-savaliya/plagiarism_ai_detector_frontend
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# kevin-savaliya/Plagiarism_AI_Detector_Frontend

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kevin-savaliya/plagiarism_ai_detector_frontend
- **Stars**：2
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Plagiarism & AI Detection System is a smart web app built with Flask (backend) and React.js (frontend) to detect AI-generated content from uploaded files or text inputs and perform plagiarism detection between two texts using Cosine, TF-IDF, Jaccard, and Average similarity measures, displaying results visually via charts.
- **本地描述**：Plagiarism & AI Detection System is a smart web app built with Flask (backend) and React.js (frontend) to detect AI-generated content from uploaded files or text inputs and perform plagiarism detection between two texts using Cosine, TF-IDF, Jaccard, and Average similarity measures, displaying results visually via charts.
- **拉取时间**：2026-07-25 18:24:18

---

# 📚 Plagiarism & AI Detection System

An intelligent web-based platform to detect **AI-generated content** and check **text similarity (plagiarism)** between two texts using advanced NLP and ML algorithms.

This project includes a **React.js frontend**, **Flask backend**, and integrates multiple models and statistical techniques for robust analysis.

> 🌐 **Live Frontend**: [Plagiarism & AI Detection (Frontend)](https://plagiarism-ai-detector-frontend.vercel.app)
> 🔗 **Backend API**: [Render Hosted API](https://plagiarism-ai-detector-backend.onrender.com)

---

## 📌 Features

### 🤖 AI Detection

* Upload files: `.txt`, `.pdf`, `.docx`, `.csv`, `.xlsx`, etc., or directly input text.
* Detects AI-generated content using fine-tuned Transformer models (e.g. GPT-2, Roberta).
* Displays:

  * **Pie chart** showing AI vs Human content proportion.
  * **Confidence-based status:**

    * <30% → Likely human-written
    * 30-70% → Uncertain (could be either human or AI)
    * >70% → Likely AI-generated
    * Confidence <50% → Low confidence in analysis.
* Text analysis summary:

  * Word Count, Sentence Count, Paragraph Count
  * Unique Words
  * Average Word Length
  * Average Sentence Length

### 📖 Plagiarism (Similarity) Detection

* Compares two texts and calculates **four similarity metrics**:

  * **Jaccard Similarity**: Measures intersection over union of word sets.
  * **Cosine Similarity**: Measures the cosine angle between two text vectors.
  * **TF-IDF Similarity**: Uses term frequency-inverse document frequency vector comparison.
  * **Average Similarity**: Mean of Cosine, Jaccard, and TF-IDF scores.
* Displays results in **bar charts** for intuitive understanding.

---

## 🛠️ Technologies Used

| Layer              | Technology / Library                               |
| ------------------ | -------------------------------------------------- |
| Frontend           | React.js, Axios, Material-UI, Chart.js             |
| Backend            | Flask, Flask-RESTful, Python                       |
| ML/NLP             | Transformers (GPT-2, Roberta), SpaCy, Scikit-learn |
| Data               | pandas, numpy, PyPDF2 (PDF parsing)                |
| Visualization      | Chart.js, matplotlib, seaborn                      |
| Hosting (Frontend) | Vercel                                             |
| Hosting (Backend)  | Render                                             |

---

## 🧠 How It Works

### 🔍 AI Detection Flow

1. **Text/File Input** → Preprocessing (tokenization, cleaning).
2. **Feature Extraction**: sentence length, repetition, complexity.
3. **AI Model Evaluation** using fine-tuned transformers.
4. **Confidence Score Calculation**.
5. **Output**:

   * Probability of AI-generated content.
   * Pie chart visualization.
   * Text analysis summary and status.

### 📝 Similarity Detection Flow

1. **Text-to-Text Comparison**:

   * Preprocessing → Vectorization (TF-IDF) → Similarity calculations.
2. **Output**:

   * Bar chart displaying all four similarity metrics.
   * Detailed plagiarism report.

---

## ▶️ Getting Started

### 🔧 Prerequisites

* **Frontend**:

  * Node.js (v14+)
* **Backend**:

  * Python 3.10
  * pip

---

## 🔽 Clone the Repositories

### Frontend

```bash
git clone https://github.com/kevin-savaliya/Plagiarism_AI_Detector_Frontend.git
cd Plagiarism_AI_Detector_Frontend
```

### Backend

```bash
git clone https://github.com/kevin-savaliya/Plagiarism_AI_Detector_Backend.git
cd Plagiarism_AI_Detector_Backend
```

---

## ▶️ Running the Project

### 🚀 Start Backend

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app/main.py
```

### 🚀 Start Frontend

```bash
cd Plagiarism_AI_Detector_Frontend
npm install

# Create .env file with:
# REACT_APP_API_URL=https://plagiarism-ai-detector-backend.onrender.com

npm start
```

---

## 🛠 Environment Variables

### Frontend `.env`

```env
REACT_APP_API_URL=https://plagiarism-ai-detector-backend.onrender.com
```

### Backend `.env`

(Optional, if you use any secrets or API keys)

---

## 🔮 Future Improvements

* 📝 **Database integration** for user history and analytics.
* 🧠 **Enhanced AI detection** with multiple classification models.
* 📄 **Export plagiarism/AI reports** as PDF.
* 🗂️ **Bulk file uploads** with queued analysis.
* 🔐 **User authentication and dashboards**.

---

## 👨‍💻 Author

**Kevin Savaliya**

* GitHub: [@kevin-savaliya](https://github.com/kevin-savaliya)
* Frontend: [Plagiarism & AI Detector (Vercel)](https://plagiarism-ai-detector-frontend.vercel.app)
* Backend API: [Render Hosted API](https://plagiarism-ai-detector-backend.onrender.com)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

> ⭐️ **If you found this project helpful, please star the repository to support my work!**


