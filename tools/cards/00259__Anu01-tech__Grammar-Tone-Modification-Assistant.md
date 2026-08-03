---
id: tool-00259
type: tool
area: 库
status: active
tags: [校对, HTML, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: Grammar-Tone-Modification-Assistant
summary: 错别字/语法/风格校对
source: https://github.com/anu01-tech/grammar-tone-modification-assistant
created: 2026-07-18
updated: 2026-07-18
no: 259
category: 二、网文 / 长篇 AI 写作系统 库
repo: Anu01-tech/Grammar-Tone-Modification-Assistant
stars: 0
url: https://github.com/anu01-tech/grammar-tone-modification-assistant
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Anu01-tech/Grammar-Tone-Modification-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/anu01-tech/grammar-tone-modification-assistant
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A smart writing assistant that corrects grammar and adapts tone—Professional, Casual, or Persuasive—using Gemini API. Features split-screen UI, real-time rewriting, copy-to-clipboard, and secure API key storage. Learn LLM constraint techniques while building a polished, interactive web tool.
- **本地描述**：A smart writing assistant that corrects grammar and adapts tone—Professional, Casual, or Persuasive—using Gemini API. Features split-screen UI, real-time rewriting, copy-to-clipboard, and secure API key storage. Learn LLM constraint techniques while building a polished, interactive web tool.
- **拉取时间**：2026-07-23 22:46:38

---

# 🪄 Tone & Grammar Modification Assistant

An AI-powered writing companion that polishes your drafts, fixes grammar, spelling, and punctuation errors, and rewrites text to match your desired communication tone. Powered by Google Gemini APIs (1.5 Flash & Pro).

This repository contains **two complete implementations**:
1. **Frontend-Only Version**: A single-file `index.html` application utilizing Tailwind CSS and Vanilla JavaScript. Runs directly in any web browser.
2. **Python Web Application**: An interactive app built with Python, Streamlit, and the official Google Generative AI SDK.

---

## 🚀 Key Features

- **Split-Screen Workspace**: Left panel for raw input drafts and character metrics; right panel for polished, rewritten outputs.
- **Multiple Target Tones**: Effortlessly switch your writing tone between:
  - 👔 **Professional**: Formal, structured, and workplace-ready.
  - ☕ **Casual**: Relaxed, conversational, and friendly.
  - 🎯 **Persuasive**: Compelling, action-oriented, and convincing.
  - 🤝 **Empathetic**: Supportive, understanding, and warm.
- **Model Choice**: Toggle between **Gemini 1.5 Flash** (optimized for speed) and **Gemini 1.5 Pro** (optimized for deep reasoning and complex rewrites).
- **Secure Key Management**: Keep your API keys private. Keys are saved locally (browser `localStorage` or a local hidden JSON file) and never transmitted to external third-party servers.
- **Interactive UI Extras**:
  - Live character counts and input clearing.
  - Instant **Copy to Clipboard** utility with visual success transitions.
  - Custom dark-theme scrollbars, layout animations, and slide-in toast alerts.

---

## 🛠️ Usage Instructions

### Version 1: HTML / JS Client-Side (Zero Setup)
Perfect for instant use without installing developer tools or language environments.

1. Locate **`index.html`** in the repository.
2. Double-click the file to open it in your web browser.
3. Paste your Gemini API key in the header, click **Save Key**, and start writing.

---

### Version 2: Python / Streamlit App
Provides a robust, local development server experience using the official Python SDK.

#### 1. Install Dependencies
Make sure you have Python 3.9+ installed, then install the required packages:
```bash
pip install streamlit google-generativeai
```

#### 2. Run the Web Server
Launch the Streamlit dashboard:
```bash
streamlit run app.py
```
A local server will initialize and automatically open the application at `http://localhost:8501`.

---

## 🔑 How to Get a Gemini API Key

This application requires a Google Gemini API Key to communicate with AI models:

1. Visit the **[Google AI Studio](https://aistudio.google.com/)** and sign in using your Google account.
2. Click **Get API key** on the top menu bar or dashboard.
3. Select **Create API key** (either in a new project or an existing one) and copy the generated key.
4. Paste the copied key into either version of the application:
   - **HTML Version**: Paste in the top-right header input and click **Save Key**.
   - **Python Version**: Paste in the sidebar configuration input and click **Save Key**.

---

## 🔒 Security & Privacy Notice
Your API keys are stored entirely client-side:
* In the HTML version, the key is saved in your browser's local sandbox storage (`localStorage`).
* In the Python version, the key is saved in a hidden local configuration file (`.assistant_config.json`) in the project directory.

The keys are only loaded to authorize direct requests to the official Google Gemini API endpoint (`https://generativelanguage.googleapis.com`). They are never uploaded or tracked.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🧰 Tech Stack Used

* **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN), Inter Google Fonts.
* **Backend (Python App)**: Python 3, Streamlit Web Framework.
* **Core API**: Google Gemini API via REST and `google-generativeai` SDK.
