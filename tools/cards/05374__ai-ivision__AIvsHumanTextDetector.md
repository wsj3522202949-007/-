---
id: tool-05374
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AIvsHumanTextDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ai-ivision/aivshumantextdetector
created: 2026-07-18
updated: 2026-07-18
no: 5374
category: 一、去 AI 味 / Humanizer 库
repo: ai-ivision/AIvsHumanTextDetector
stars: 0
url: https://github.com/ai-ivision/aivshumantextdetector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ai-ivision/AIvsHumanTextDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ai-ivision/aivshumantextdetector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ai-ivision/AIvsHumanTextDetector
- **拉取时间**：2026-07-25 18:16:13

---

# AI vs Human Text Detection System 🧠👤

This project is designed to detect whether a given piece of text is written by an AI or a human using a machine learning pipeline. It uses Natural Language Processing (NLP), SMOTE for class imbalance, multiple ML models, and an ensemble Voting Classifier. A Streamlit-based UI is provided for easy interaction.

---

## 📊 Dataset Reference

This project uses the dataset available on Kaggle:

**Kaggle Dataset Title**: [AI Generated Text Dataset](https://www.kaggle.com/datasets/denvermagtibay/ai-generated-essays-dataset)

- **Source**: Uploaded by [Denver Magtibay](https://www.kaggle.com/denvermagtibay)
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **The dataset contains 1,460 text passages**:
    - 85 AI-generated (~6%)
    - 1,375 human-written (~94%)
- **Features**:
  - `text`: Essay or written content
  - `generated`: Binary label — `1` if AI-generated, `0` if human

> Make sure to download and place the CSV file in the `data/` directory to run the project.

---

## 🔧 Features

- Text preprocessing & cleaning
- TF-IDF vectorization
- Handling class imbalance using SMOTE
- Training multiple models
- Voting ensemble for final prediction
- Streamlit UI for live predictions
- Saved vectorizer and models (`joblib`)

---

## 🧪 Models Used

- Logistic Regression
- Random Forest
- XGBoost
- Multinomial Naive Bayes
- VotingClassifier (hard voting)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-text-detector.git
   cd ai-text-detector
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK stopwords:
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

---

## 🚀 Run the App

To launch the Streamlit UI:

```bash
streamlit run app.py
```

---

## 🗃 Directory Structure

```
.
├── data/
│   └── AIGeneratedEssaysDataset.csv
├── model/
│   ├── vectorizer.pkl
│   └── classifier.pkl
├── app.py
├── model_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Future Improvements

- Integrate LLM-based transformers (e.g., BERT)
- Add LIME/SHAP explainability
- Use Flask/FastAPI for production API

---

## 🧑‍💻 Author

**Arnab Gupta**  
Data Scientist | ML Engineer  
Agency: **ThirdEyeVision**

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📜 License

This project is licensed under the MIT License.
