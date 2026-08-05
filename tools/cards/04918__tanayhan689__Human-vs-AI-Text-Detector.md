---
id: tool-04918
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Human-vs-AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tanayhan689/human-vs-ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4918
category: 一、去 AI 味 / Humanizer 库
repo: tanayhan689/Human-vs-AI-Text-Detector
stars: 0
url: https://github.com/tanayhan689/human-vs-ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# tanayhan689/Human-vs-AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tanayhan689/human-vs-ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ML pipeline classifying text as human-written vs AI-generated using 14 engineered linguistic features (lexical diversity, complexity, informal phrasing, etc.). Compares four classifiers (up to 98.9% accuracy) and includes an interactive Streamlit app for live predictions and EDA.
- **本地描述**：ML pipeline classifying text as human-written vs AI-generated using 14 engineered linguistic features (lexical diversity, complexity, informal phrasing, etc.). Compares four classifiers (up to 98.9% accuracy) and includes an interactive Streamlit app for live predictions and EDA.
- **拉取时间**：2026-07-25 17:59:19

---

# 🤖 Human vs AI Text Detector

> A full-stack machine learning project that classifies text as **Human-written** or **AI-generated** using engineered linguistic features and an interactive Streamlit demo.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?logo=scikit-learn)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Overview

This project builds a complete ML pipeline to distinguish between human-written and AI-generated text using the **HumanVsAI-2026** dataset (~5,000 labelled samples). Instead of relying solely on raw TF-IDF features, we engineer interpretable linguistic signals that capture the stylistic patterns that separate humans from language models.

### Key results
| Model             | Accuracy | F1    | ROC AUC |
|-------------------|----------|-------|---------|
| GradientBoosting  | 98.9%    | 98.9% | 99.8%   |
| RandomForest      | 98.8%    | 98.8% | 99.7%   |
| LogisticRegression| 97.8%    | 97.8% | 99.5%   |
| LinearSVC (calib) | 97.5%    | 97.5% | 99.3%   |

*(5-fold stratified cross-validation on engineered features only — no raw text leakage)*

---

## 🗂️ Project Structure

```
human-vs-ai-detector/
│
├── data/
│   └── HumanVsAI-2026.csv          # Raw dataset
│
├── src/
│   ├── preprocessing.py            # Feature engineering pipeline
│   ├── eda.py                      # Exploratory data analysis + plots
│   ├── train.py                    # Model training & evaluation
│   └── predict.py                  # Inference wrapper + CLI
│
├── app/
│   └── app.py                      # Streamlit web app
│
├── models/
│   ├── best_model.pkl              # Serialised best classifier (after training)
│   └── model_meta.json             # Training metadata
│
├── assets/                         # Auto-generated evaluation plots
│   ├── confusion_matrix.png
│   ├── roc_curves.png
│   ├── model_comparison.png
│   ├── feature_importance.png
│   ├── pca_scatter.png
│   ├── feature_boxplots.png
│   └── correlation_heatmap.png
│
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone & install dependencies

```bash
git clone https://github.com/<your-username>/human-vs-ai-detector.git
cd human-vs-ai-detector
pip install -r requirements.txt
```

### 2. Generate EDA plots

```bash
python src/eda.py
```

### 3. Train the models

```bash
python src/train.py
```

This will:
- Engineer 14 linguistic features from the raw text
- 5-fold cross-validate four classifiers (LR, RF, GBM, SVC)
- Save the best model to `models/best_model.pkl`
- Generate evaluation plots in `assets/`

### 4. Run the Streamlit app

```bash
streamlit run app/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### 5. CLI prediction (optional)

```bash
python src/predict.py "honestly i dont like machine learning but its important i guess"
python src/predict.py "Machine learning models are widely used in studying for automation."
```

---

## 🔬 Engineered Features

The feature pipeline (`src/preprocessing.py`) extracts 14 interpretable signals:

| Feature               | Description                                         | Human signal | AI signal |
|-----------------------|-----------------------------------------------------|:---:|:---:|
| `complexity_score`    | Pre-computed linguistic complexity (0–1)            | ↓   | ↑   |
| `grammar_errors_count`| Number of detected grammar errors                  | varies | varies |
| `sentence_length`     | Token count of the sentence                         | ↓   | ↑   |
| `char_count`          | Total characters                                    | ↓   | ↑   |
| `word_count`          | Total words                                         | ↓   | ↑   |
| `avg_word_length`     | Mean character length per word                      | ↓   | ↑   |
| `lexical_diversity`   | Type-token ratio (unique/total words)               | ↑   | ↓   |
| `uppercase_ratio`     | Fraction of uppercase letters                       | ↓   | ↑   |
| `punctuation_density` | Punctuation chars / total chars                     | ↑   | ↓   |
| `starts_with_lowercase` | 1 if sentence begins lowercase                  | ↑   | ↓   |
| `has_emoji`           | 1 if any emoji present                              | ↑   | ↓   |
| `informal_word_count` | Count of slang/informal tokens (lol, kinda, etc.)   | ↑   | ↓   |
| `ai_phrase_count`     | Count of AI-typical phrases (deep learning, etc.)   | ↓   | ↑   |
| `typo_count`          | Rough count of likely typos                         | ↑   | ↓   |

---

## 📊 Dataset

**HumanVsAI-2026** contains 5,000 text samples:
- **Labels:** `Human` (2,462) / `AI` (2,538) — near-balanced
- **Sources:** blog, essay, tweet, research
- **Columns:** `id`, `text`, `label`, `source`, `complexity_score`, `grammar_errors_count`, `sentence_length`

Human texts are characterised by informal language, typos, emoji, slang, and lower structural complexity.  
AI texts exhibit formal phrasing, AI-domain vocabulary, and higher complexity scores.

---

## 🖥️ App Features

The Streamlit app (`app/app.py`) has three tabs:

| Tab | Content |
|-----|---------|
| 🔍 **Detector** | Paste any text → get Human/AI prediction with confidence gauge + feature breakdown |
| 📊 **Dataset EDA** | Interactive Plotly charts: class distribution, complexity histograms, scatter plots, raw data table |
| 📈 **Model Performance** | All evaluation plots: confusion matrix, ROC curves, feature importances, PCA projection |

---

## 📄 License

MIT — see `[LICENSE](LICENSE)` for details.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🙏 Acknowledgements

Dataset: HumanVsAI-2026 research corpus.  
Built with [scikit-learn](https://scikit-learn.org), [Streamlit](https://streamlit.io), and [Plotly](https://plotly.com).
