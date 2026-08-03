---
id: tool-04820
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Fake_News_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sub703/ai_fake_news_detector
created: 2026-07-18
updated: 2026-07-18
no: 4820
category: 一、去 AI 味 / Humanizer 库
repo: sub703/AI_Fake_News_Detector
stars: 0
url: https://github.com/sub703/ai_fake_news_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sub703/AI_Fake_News_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sub703/ai_fake_news_detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：data-science, jupyter-notebook, machine-learning, model-calibration, natural-language-processing, nlp, pipeline, portfolio-project, python, scikit-learn, streamlit, svm, text-classification, tf-idf
- **GitHub 描述**：A production-grade NLP pipeline and interactive Streamlit web dashboard using a calibrated Linear SVM to detect text disinformation with 99.34% generalization accuracy.
- **本地描述**：A production-grade NLP pipeline and interactive Streamlit web dashboard using a calibrated Linear SVM to detect text disinformation with 99.34% generalization accuracy.
- **拉取时间**：2026-07-25 17:55:34

---

# **AI Fake News Detector**

---

# 🛡️ Building a Leak-Proof AI Fake News Detector 

Most fake news classifiers look great on paper but fail completely in the real world because they accidentally train on "dataset leaks"—like finding corporate wire tags unique to one source. This project implements a leak-proof, end-to-end Machine Learning pipeline and interactive Streamlit web dashboard. 

By training on a diversified corpus and keeping a completely separate dataset hidden for an honest generalization test, this pipeline achieves a **99.34% accuracy score on entirely unseen news origins**.

---

## 📊 Performance & Why I Skipped Transformers

A common trap in NLP is reaching for heavy, slow transformers right away. During my experiments, I benchmarked **Sentence Transformers (all-MiniLM-L6-v2)** and **Latent Semantic Analysis (LSA)**, but a streamlined, transparent approach proved significantly better for this specific vocabulary-driven task:

*   **My Core Pipeline (Sparse TF-IDF + Calibrated Linear SVM):** **96.40%** validation accuracy, scaling up to **99.34%** generalization accuracy on unseen external publishers.
*   **The Transformer Route (MiniLM Embeddings + LogReg):** Dropped down to **82.37%** accuracy while adding heavy computational lag over a CPU runtime.

### 🎯 Enforcing Real-World Safety Floors
*   **Target Precision Control:** Using default probabilities ($0.50$ cutoff) presents an unsafe balance where a real article might be falsely accused. I tuned the decision boundary up to a strict **0.57 threshold** to enforce a **minimum 97% precision constraint** against false alarms.
*   **A Graceful Fallback Layer:** If an incoming article yields a highly ambiguous probability between 43% and 57%, the web application safely defaults to an **"Uncertain, verify independently"** status rather than forcing a blind, risky guess.

---

## 🚀 Live Demo Interface Showcase

### 1. Flagging Clickbait Disinformation
The pipeline successfully leverages negative word weights to flag sensational language frames with absolute certainty:
![Likely Fake State](Screenshots/fake_demo.png)

### 2. Verifying Formal Journalistic Structure
The model isolates semantic layouts and structural phrasing to pass our strict 57% safety boundary cutoff floor:
![Likely Real State](Screenshots/real_demo.png)

### 3. Activating the Uncertainty Fallback Banners
When incoming language signals are mixed or too ambiguous to clear precision constraints, the UI declines to force a blind guess:
![Uncertain Safety Floor State](Screenshots/uncertain_demo.png)

---

## 🛠️ Critical Engineering Milestones

### 1. Defeating Dataset Leaks with Regex Prefilters
While inspecting the data, I caught a major trap: roughly 99.8% of legitimate news articles in the benchmark data started with an editorial wire marker like `WASHINGTON (Reuters) -`. Leaving those in means the model just learns to look for the word "Reuters" instead of evaluating actual deception. I designed regular expression routines to wipe these markers completely, forcing the model to learn genuine language composition.

### 2. Auditing Dataset Label Inversions
Documentation isn't always accurate. The dataset host stated that `0 = fake, 1 = real`, but an empirical validation check proved the files were distributed entirely backwards. Auditing and mapping this correctly upfront prevented the entire pipeline from learning an inverted logic structure.

### 3. Native Pipeline Encapsulation
To eliminate structural mismatches between training and local execution, I packaged both the text feature vectorizer and the calibrated classifier into a single serialized `Pipeline` object via `joblib`. 

---

## 📂 Project Structure
*   `app.py` - The interactive Streamlit user dashboard layout.
*   `fake_news_pipeline.joblib` - The fully self-contained, pre-trained deployment model artifact.
*   `notebook/` - Holds the complete, executed Google Colab experimental notebook showing evaluation plots, cross-validation checks, and model coefficient interpretations.

---

## 🏃‍♂️ Running the Web App Locally

1. **Clone the project workspace:**
   ```bash
   git clone https://github.com
   cd AI_Fake_News_Detector
   ```

2. **Acquire the Raw Datasets:**
   To replicate or view the training process, download the exact source files into a local `data/` folder sitting right next to the project:
   *   **WELFake Dataset:** Download from the [Kaggle WELFake News Classification Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification).
   *   **ISOT Dataset:** Download the `True.csv` / `Fake.csv` pair from the authoritative [Kaggle Fake and Real News Dataset by Clément Bisaillon](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).
   *(Note: These raw `.csv` files are automatically ignored by git via our `.gitignore` rules to keep the repository size clean and optimized).*

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## ✍️ Author

**[@sub703](https://github.com)**

If you have questions about the codebase, architecture choices, or want to collaborate on similar engineering workflows, feel free to get in touch:
* **GitHub Profile:** [@sub703](https://github.com)
* **Inquiries:** Open an issue or drop a discussion thread directly within this repository!

