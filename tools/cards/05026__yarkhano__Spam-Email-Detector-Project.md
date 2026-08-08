---
id: tool-05026
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Spam-Email-Detector-Project
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/yarkhano/spam-email-detector-project
created: 2026-07-18
updated: 2026-07-18
no: 5026
category: 一、去 AI 味 / Humanizer 库
repo: yarkhano/Spam-Email-Detector-Project
stars: 0
url: https://github.com/yarkhano/spam-email-detector-project
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 34bbc4755eb6652e
  - methods/改稿润色指令库.md
---

# yarkhano/Spam-Email-Detector-Project

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/yarkhano/spam-email-detector-project
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Spam Shield AI is a Python-based machine learning project for detecting spam emails from text in real time. It includes a training workflow (train.py) for data cleaning (regex), TF‑IDF vectorization, and model evaluation using precision/recall/F1, plus a lightweight FastAPI service (app.py) .
- **本地描述**：Spam Shield AI is a Python-based machine learning project for detecting spam emails from text in real time. It includes a training workflow (train.py) for data cleaning (regex), TF‑IDF vectorization, and model evaluation using precision/recall/F1, plus a lightweight FastAPI service (app.py) .
- **拉取时间**：2026-07-25 18:03:22

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 🛡️ Spam Shield AI: Machine Learning API

## 📖 Project Overview
Spam Shield is a full-stack Machine Learning application designed to analyze text and detect spam emails in real-time. It features a custom-trained AI model wrapped in a high-speed web API, complete with a clean, interactive user interface. 

Instead of just checking for accuracy, this project was built with real-world business logic in mind, ensuring that important emails are not accidentally deleted.

## ✨ Best Practices Implemented
* **Separation of Concerns:** The codebase is split into two distinct environments. `train.py` handles the heavy data processing and model training, while `app.py` serves as a lightweight, lightning-fast production web server.
* **Advanced Data Cleaning (Regex):** Real-world data is messy. I implemented Regular Expressions (Regex) to strip out noise (like "Subject:" prefixes, punctuation, and odd spacing), drastically improving the AI's learning quality.
* **Business-Focused Evaluation:** Accuracy can be misleading in spam detection. This model was evaluated using **Precision, Recall, and F1-Scores**, prioritizing high *Precision* (97.9%) to guarantee that safe, important emails are never accidentally flagged as spam (Zero False Alarms).
* **TF-IDF Vectorization:** Translated raw text into weighted mathematical vectors, teaching the AI to focus on unique, high-value words rather than generic vocabulary.

## 🚀 How to Run Locally

1. **Install Requirements:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt

It looks like the formatting got stripped out when you copied it over!

To make your README look incredibly professional on GitHub, you don't actually want to put *all* the text inside a `bash` block. In standard Markdown, `bash` blocks are strictly reserved for terminal commands so users can quickly copy and paste them. The rest of the text should use bolding and bullet points to make it highly readable.

Here is the exact Markdown code. Copy this entire block below and paste it directly into your `README.md` file. It will automatically create the beautiful gray `bash` boxes for the code and cleanly format the lists for your limitations and improvements!

```markdown
2. **(Optional) Train the Model:**
   If you want to re-train the AI brain from scratch using the CSV dataset, run:
   ```bash
   python train.py

```

3. **Start the Web Server:**
Launch the FastAPI application:
```bash
uvicorn app:app --reload

```


4. **Test it Out:**
Open your browser and navigate to `http://127.0.0.1:8000` to use the interactive UI, or visit `http://127.0.0.1:8000/docs` to test the raw API endpoints.

## 🚧 Limitations

* **Language Dependent:** The model currently relies on an English-language vocabulary dataset. It may struggle to classify spam written in other languages.
* **Text Only:** The model analyzes the text payload. It cannot currently read images or scan embedded file attachments for viruses.

## 🔮 Future Improvements

* **Automated Data Cleaning on Input:** Apply the exact same Regex cleaning logic to user input on the API side before prediction to further boost real-world accuracy.
* **Cloud Deployment:** Host the FastAPI server on a cloud platform (like Render or AWS) for public access.
* **Feedback Loop API:** Add a database and an endpoint where users can "Report as Incorrect", allowing the model to collect new data and learn from its mistakes over time.



   
