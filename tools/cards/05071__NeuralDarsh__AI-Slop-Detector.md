---
id: tool-05071
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Slop-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/neuraldarsh/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5071
category: 一、去 AI 味 / Humanizer 库
repo: NeuralDarsh/AI-Slop-Detector
stars: 0
url: https://github.com/neuraldarsh/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: b82a19532d5348cc
  - methods/改稿润色指令库.md
---

# NeuralDarsh/AI-Slop-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/neuraldarsh/ai-slop-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered web app to detect AI-generated content using HuggingFace RoBERTa + OpenAI
- **本地描述**：AI-powered web app to detect AI-generated content using HuggingFace RoBERTa + OpenAI
- **拉取时间**：2026-07-25 18:04:59

---

# 🚫 AI Slop Detector

A full-stack web application designed to identify low-quality, AI-generated content ("Slop") from websites. This project combines **Web Scraping**, **Natural Language Processing (NLP)**, and **Web Development** to help users verify the authenticity of online articles.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Transformers-orange?style=for-the-badge)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🌟 Key Features
* **Web Scraping:** Automatically extracts main article text from any URL using `BeautifulSoup4`.
* **AI Detection:** Utilizes a pre-trained **RoBERTa** model (via HuggingFace) specifically tuned to detect GPT-2/3/4 generated text.
* **Clean UI:** Simple, responsive interface built with Flask and minimalist CSS.
* **High Accuracy:** Provides a probability score (Confidence %) for every analysis.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **NLP Engine:** HuggingFace Transformers (`roberta-base-openai-detector`)
* **Scraping:** Requests, BeautifulSoup4
* **Environment:** Virtualenv, Dotenv (for API security)
