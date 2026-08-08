---
id: tool-01268
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: personalised-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/aditivvs03/personalised-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1268
category: 二、网文 / 长篇 AI 写作系统 库
repo: aditivvs03/personalised-story-generator
stars: 1
url: https://github.com/aditivvs03/personalised-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d20e3a0e503ce018
  - methods/最强写作方法论_全球最强综合版.md
---

# aditivvs03/personalised-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aditivvs03/personalised-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：generative-ai, gpt-neo, machine-learning, nlp, python, streamlit
- **GitHub 描述**：AI-powered story generator using GPT-Neo-125M and Streamli
- **本地描述**：AI-powered story generator using GPT-Neo-125M and Streamli
- **拉取时间**：2026-07-23 23:16:04

---

# ✨ Personalised Story Generator

An AI-powered web application that generates creative story continuations based on user-defined themes, characters, and prompts — built using **GPT-Neo-125M** and **Streamlit**.

---

## 🚀 Demo

> Enter a story beginning → Choose a theme → Watch AI continue your story!

---

## 🧠 Features

- 🎭 **5 Story Themes** — Horror, Fantasy, Romance, Mystery, Sci-Fi
- 👤 **Custom Character Names** — Personalize the story with your own hero
- 🎛 **Adjustable Story Length** — Control output between 100–500 words
- 🎨 **Beautiful UI** — Theme-based dynamic colors and gradient design
- 💾 **Download Stories** — Save your generated story as a `.txt` file
- ⚙️ **Advanced Settings** — Tune creativity level and view generation details

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend web interface |
| Hugging Face Transformers | GPT-Neo-125M model inference |
| PyTorch | Model backend |

---

## 📁 Project Structure

```
personalised-story-generator/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore           # Files to ignore in Git
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/aditivvs03/personalised-story-generator.git
cd personalised-story-generator
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

> **Note:** The GPT-Neo-125M model (~500MB) will be automatically downloaded from Hugging Face on first run.

---

## 🎯 How to Use

1. **Select a theme** from the dropdown (Horror, Fantasy, Romance, Mystery, Sci-Fi)
2. **Set story length** using the slider (100–500 words)
3. **Enter a character name** (optional)
4. **Write your story beginning** in the text area
5. Click **"🪄 Weave the Story!"**
6. Read your AI-generated continuation and download it if you like!

---

## 🔧 Model Details

- **Model:** [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M)
- **Temperature:** 0.85
- **Top-p Sampling:** 0.92
- **Repetition Penalty:** 1.3
- **Max Tokens:** Up to 1024

---

## 👩‍💻 Author

**Aditi V Shastry**
- GitHub: [@aditivvs03](https://github.com/aditivvs03)
- LinkedIn: [aditi-shastry-66a831326](https://www.linkedin.com/in/aditi-shastry-66a831326)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License

This project is open source and available under the [MIT License](https://github.com/aditivvs03/personalised-story-generator/blob/main/LICENSE).
