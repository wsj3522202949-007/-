---
id: tool-05327
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Fake-News-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ishitasingh0724-arch/fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 5327
category: 一、去 AI 味 / Humanizer 库
repo: ishitasingh0724-arch/Fake-News-Detector
stars: 1
url: https://github.com/ishitasingh0724-arch/fake-news-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 54fb9053949f2233
  - methods/改稿润色指令库.md
---

# ishitasingh0724-arch/Fake-News-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ishitasingh0724-arch/fake-news-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：.# Fake News Classifier  Python NLP pipeline using `pandas` and `scikit-learn`.  ## 🚀 Steps 1. **Prep**: Cleaned data via Pandas. 2. **Vectors**: TF-IDF word encoding. 3. **AI**: Trained an `SGDClassifier`.  ## 📉 Result Hit 50.88% accuracy because the dataset uses scrambled dummy text with no real linguistic patterns.
- **本地描述**：.# Fake News Classifier  Python NLP pipeline using `pandas` and `scikit-learn`.  ## 🚀 Steps 1. **Prep**: Cleaned data via Pandas. 2. **Vectors**: TF-IDF word encoding. 3. **AI**: Trained an `SGDClassifier`.  ## 📉 Result Hit 50.88% accuracy because the dataset uses scrambled dummy text with no real linguistic patterns.
- **拉取时间**：2026-07-25 18:14:30

---

# Fake News Detection Project

This is a simple Python project that uses Machine Learning to look at news headlines and text to determine if they are Real or Fake. 

---

## 🛠️ How It Works (The 4 Steps)

1. **Clean the Data:** Opens the dataset spreadsheet using `pandas`, fills in missing blanks, and combines headlines with article text.
2. **Split the Data:** Splits the data into a **Study Pile (80%)** to train the AI and an **Exam Pile (20%)** to test it.
3. **Words to Numbers:** Converts English text into numbers using a tool called `TF-IDF Vectorizer` so the computer can calculate mathematical patterns.
4. **Train the AI:** Trains an `SGDClassifier` model to study the number patterns and guess whether an article is real or fake.

---

## 🪙 Why the Final Score is ~51%

The code runs perfectly and without any errors. However, the final accuracy score sits right around **50.88%** (a coin toss) because the dataset contains randomized, scrambled placeholder dummy text. 

Because the words have no real semantic meaning, the AI cannot find any actual linguistic patterns to learn from, resulting in random guessing. The pipeline is fully functional and ready to be used on a real-world news dataset.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 💻 How to Run

1. Make sure you have Python installed.
2. Install the required tools in your terminal:
   ```bash
   pip install pandas scikit-learn
