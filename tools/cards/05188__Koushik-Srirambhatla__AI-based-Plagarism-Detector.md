---
id: tool-05188
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-based-Plagarism-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/koushik-srirambhatla/ai-based-plagarism-detector
created: 2026-07-18
updated: 2026-07-18
no: 5188
category: 一、去 AI 味 / Humanizer 库
repo: Koushik-Srirambhatla/AI-based-Plagarism-Detector
stars: 3
url: https://github.com/koushik-srirambhatla/ai-based-plagarism-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 40dfd79d5405bc83
  - methods/改稿润色指令库.md
---

# Koushik-Srirambhatla/AI-based-Plagarism-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/koushik-srirambhatla/ai-based-plagarism-detector
- **Stars**：3
- **语言**：HTML
- **License**：None
- **Topics**：flask, tailwindcss
- **GitHub 描述**：AI-powered plagiarism detection system built with Python Flask. Upload .txt, .pdf, or .docx files or paste text to check for plagiarism locally and online. Uses Sentence-Transformers for semantic similarity and provides detailed results with matching sentences and sources.
- **本地描述**：AI-powered plagiarism detection system built with Python Flask. Upload .txt, .pdf, or .docx files or paste text to check for plagiarism locally and online. Uses Sentence-Transformers for semantic similarity and provides detailed results with matching sentences and sources.
- **拉取时间**：2026-07-25 18:09:20

---

# AI-Powered Plagiarism Detection System

A **web-based plagiarism detection tool** built with **Python Flask** that checks text and documents for plagiarism both **locally** and **online** using AI-powered semantic similarity.

---

## 📝 Features
- Upload `.txt`, `.pdf`, or `.docx` files or paste text directly.
- AI-powered semantic comparison using **Sentence-Transformers**.
- Checks against:
  - Previously uploaded local files.
  - Online sources via web search.
- Shows **plagiarism percentage** and highlights matching sentences.
- Optimized for large documents using **caching** and **parallel processing**.

---

## 🛠️ Technologies Used
- Python 3.x
- Flask (Web framework)
- PyMuPDF & python-docx (Text extraction)
- BeautifulSoup & Requests (Web scraping)
- Sentence-Transformers, PyTorch, NumPy (AI similarity calculations)
- HTML/CSS & Jinja2 templates (Frontend)
- ThreadPoolExecutor (Parallel processing)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 💻 Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/plagiarism-detector.git
cd plagiarism-detector
