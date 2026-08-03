---
id: tool-05388
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Fake-News-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ritikasinghchandel210506-ctrl/fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 5388
category: 一、去 AI 味 / Humanizer 库
repo: ritikasinghchandel210506-ctrl/Fake-News-Detector
stars: 1
url: https://github.com/ritikasinghchandel210506-ctrl/fake-news-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ritikasinghchandel210506-ctrl/Fake-News-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ritikasinghchandel210506-ctrl/fake-news-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-Powered Fake News Detection using Text Classification
- **本地描述**：AI-Powered Fake News Detection using Text Classification
- **拉取时间**：2026-07-25 18:16:43

---

# 📰 AI-Powered Fake News Detection Using Advanced Text Classification

An end-to-end Machine Learning and Natural Language Processing (NLP) pipeline built from scratch to detect, preprocess, and classify news articles as **Real** or **Fake**. This project forms a core component of the Summer Internship Program in AI & ML (2026) under the **Indian Institute of Computing and Technology (IICT)**.

---

## 🛠️ Complete Tech Stack & Technologies Used

* **Core Language:** Python 3.x
* **Data Manipulation & Processing:** 
  * `Pandas` (Data frame handling, loading, slicing, and concatenating tabular datasets)
  * `NumPy` (Vector manipulation and low-level array configurations)
* **Natural Language Processing & Feature Extraction:**
  * `Regular Expressions (re)` (Custom text cleaning regex patterns for character filtering)
  * `Scikit-Learn TfidfVectorizer` (Term Frequency-Inverse Document Frequency extraction)
* **Machine Learning & Deep Learning Frameworks:**
  * `Scikit-Learn KNeighborsClassifier` (Instance-based non-parametric clustering)
  * `Scikit-Learn LogisticRegression` (Linear parametric boundary plane classification)
  * `Scikit-Learn RandomForestClassifier` (Ensemble bagging decision trees)
  * `Scikit-Learn MLPClassifier` (Multi-Layer Perceptron neural network architecture)
* **Data Visualization & Metrics Evaluation:**
  * `Matplotlib` (Subplot rendering and canvas configuration management)
  * `Seaborn` (Heatmap matrix visualization layouts)
  * `Scikit-Learn Metrics` (Accuracy score tracker, validation split, confusion matrix)
* **Development Workspace & Controls:**
  * `Jupyter Notebook` (Interactive algorithmic testing environment)
  * `Git / GitHub` (Version control, system backup, and code hosting)

---

## 🧠 Theoretical Engineering Concepts Implemented

* **Natural Language Processing (NLP):** Engineering unstructured text string matrices into dense, clean numeric representations legible by machine algorithms.
* **Text Normalization From Scratch:** Complete removal of heavy string variations by standardizing letter cases, stripping raw embedded HTML token structures, and executing punctuation pattern masking.
* **Regular Expression Cleansing Mask:** Programmatic elimination of all special characters, formatting anomalies, symbols, and quotation marks using an optimized regex target filter mask ([^\w\s]) while preserving structural word boundaries.
* **TF-IDF Vectorization Vector Math:** Weighting language tokens by tracking word importance based on their localized frequency in a single text document versus their global frequency across the whole corpus, limited to the top 5,000 statistical terms.
* **Parametric vs. Non-Parametric Framework Benchmarking:** Analyzing structural linear classifiers (Logistic Regression optimizing log-odds spaces) directly against instance-based clustering math (K-Nearest Neighbors using spatial proximity parameters).
* **Ensemble Bagging & Variance Reduction:** Implementing a 100-tree Random Forest layout to reduce high variance and prevent model overfitting across complex linguistic text boundaries.
* **Feedforward Multi-Layer Neural Networks:** Deploying an Artificial Neural Network (MLP) mapping text vectors through 100 hidden nodes, computing cross-entropy errors, and updating network weights via backpropagation optimizer layers.

---

## 🛠️ System Architecture & Execution Workflow

1. **Data Ingestion & Label Assembly:** Merges decentralized textual records (True.csv and Fake.csv), injects ground-truth binary targets (1 for True, 0 for Fake), and shuffles rows to establish balanced empirical parameters.
2. **Text Preprocessing Filter:** Standardizes case syntax, strips raw HTML entities, maps out noisy special symbols/punctuation using a scratch-built regular expression mask, and regularizes internal spacing elements.
3. **Feature Engineering:** Implements Term Frequency-Inverse Document Frequency (TF-IDF Vectorization) constrained to the top 5,000 statistically descriptive language tokens.
4. **Validation Separation:** Executes an unconditional 80/20 train-test stratification split.
5. **Algorithmic Evaluation:** Sequences comparative optimization matrices for all four curriculum-specified classifiers.

---

## 📊 Experimental Results & Performance Matrix

The pipeline was evaluated on a balanced test set of 2,000 baseline verification rows. The empirical outputs show that ensemble and non-linear networks provide superior boundary separations:

| Algorithm Class | Framework Architecture | Overall Accuracy | Precision (Fake) | Recall (Fake) | F1-Score |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Ensemble | Random Forest | 99.25% | 0.99 | 0.99 | 0.99 |
| Deep Learning | MLP Neural Network | 98.75% | 0.99 | 0.98 | 0.99 |
| Parametric | Logistic Regression | 97.70% | 0.99 | 0.97 | 0.98 |
| Non-Parametric | K-Nearest Neighbors (K=5) | 87.45% | 0.87 | 0.88 | 0.88 |

### Confusion Matrix Plots
A high-resolution visualization grid capturing the true positives, false positives, true negatives, and false negatives for all models is automatically generated and exported as confusion_matrices.png upon running the code.

---

## 💻 Directory Structure

```text
Fake-News-Detection-Pipeline/
├── True.csv                # Raw dataset: Verified legitimate news items (Ignored by Git)
├── Fake.csv                # Raw dataset: Fabricated/Sensationalized items (Ignored by Git)
├── .gitignore              # Global tracking rules to avoid pushing heavy CSV files
├── README.md               # Professional documentation landing page
├── confusion_matrices.png  # Generated 2x2 grid chart of model evaluation data
└── fake_news_pipeline.ipynb # Core production Jupyter Notebook code cells 1 to 13
```
---

## 🚀 Step-by-Step Cloning & Execution Manual

### Step 1: Install Required Environment Prerequisite Frameworks
Open your command terminal, shell window, or PowerShell console and execute the following package installations to ensure all base technologies are actively mounted:
pip install pandas numpy scikit-learn matplotlib seaborn

### Step 2: Clone the Project Repository down to Local Storage
To pull this active framework directory structure from your cloud account onto your local desktop path, copy and execute these git navigation lines:
git clone https://github.com/ritikasinghchandel210506-crtl/Fake-News-Detector.git

### Step 3: Populate Dataset CSV Storage Files
1. Download the True.csv and Fake.csv dataset resource files.
2. Paste both files directly into the root folder directory of your freshly cloned workspace folder alongside your code repository.

### Step 4: Launch and Execute the Production Pipeline
Initiate the interactive programming server within your active directory pathway:
jupyter notebook

When the management window interface loads up inside your internet browser screen:
1. Double-click and open your core notebook worksheet file: fake_news_pipeline.ipynb.
2. Direct your mouse cursor to the top options menu selection toolbar.
3. Click directly on the "Kernel" drop-down selection options.
4. Click on "Restart & Run All" from the available list parameters.
5. The system will compile all code libraries, process your text cleaning scripts, extract TF-IDF mathematical matrices, fit all four predictive classifiers, plot your evaluation charts, and prompt the live article inference tester block automatically.

---

## 🔮 Interactive Prediction Inference Endpoint

The project features a standalone validation engine in Cell 13. You can feed any raw web-scraped article string into the function to fetch immediate classification predictions with a structural confidence rating:
```text
def predict_custom_article(news_text):
    cleaned_input = clean_text_from_scratch(news_text)
    vectorized_input = vectorizer.transform([cleaned_input])
    live_model = models["LogReg"]
    prediction = live_model.predict(vectorized_input)[0]
    # Rest of internal script handles live classification logic
```
---

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📜 License & Usage Terms

This project is licensed under the **MIT License** 
MIT License

Copyright (c) 2026
