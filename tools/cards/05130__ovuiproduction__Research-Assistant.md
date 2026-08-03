---
id: tool-05130
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: Research-Assistant
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/ovuiproduction/research-assistant
created: 2026-07-18
updated: 2026-07-18
no: 5130
category: 一、去 AI 味 / Humanizer 库
repo: ovuiproduction/Research-Assistant
stars: 1
url: https://github.com/ovuiproduction/research-assistant
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ovuiproduction/Research-Assistant

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ovuiproduction/research-assistant
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：all-minilm-l6-v2, artificial-intelligence, bart, faiss, fine-tuning, humanizer, natural-language-processing, question-answering, rag, research-assistant, search-engine, text-processing
- **GitHub 描述**：AI-Powered Research Assistant – A smart tool that helps researchers find relevant papers, recommend journals, ask questions about content, humanize AI text, and detect AI-generated writing. Powered by Large Language Models for enhanced research productivity.
- **本地描述**：AI-Powered Research Assistant – A smart tool that helps researchers find relevant papers, recommend journals, ask questions about content, humanize AI text, and detect AI-generated writing. Powered by Large Language Models for enhanced research productivity.
- **拉取时间**：2026-07-25 18:07:14

---

# 🎓 AI-ResearchMate: Humanizing and Assisting Research with LLMs

### [Demo](#)

An AI-powered co-research assistant that simplifies academic research using intelligent search, interactive Q&A, and humanized text transformation to help bypass AI content detection mechanisms.

---

## 🚀 Objective

**AI-ResearchMate** is designed to:
- Assist researchers in finding high-quality academic content.
- Answer research questions using a RAG (Retrieval-Augmented Generation) pipeline.
- Humanize AI-generated content to avoid AI detection.
- Identify and highlight AI-written sections in research drafts and rewrite them in a more human tone.

---

## 🧠 Features

- 🔍 **Smart Paper Search**: Retrieve top relevant research papers to basis of abstract , title or .author names.
- 🔍 **Smart Journal Search**: Suggesting Journals based on domain and keywords also filterring Qurtile based.
- 💬 **Interactive Q&A**: Ask questions about research content and get answers powered by Large Language Models.
- 📝 **AI Content Humanization**: Use BART-based pipeline to rewrite AI-generated text into human-like writing.
- 🚨 **AI Content Detection**: Detect and highlight AI-written content to improve authenticity and originality.

---

## 🧰 Tech Stack

- **Language**: Python
- **LLM Models**: BART (`facebook/bart-large` via HuggingFace) , all-MiniLM-L6-v2
- **Vector Search**: FAISS
- **Database**: MongoDB
- **Datasets**: 
  - ArXiv Paper Dataset
  - Journal Ranking Dataset
  - Self-Curated AI-Human Text Pair Dataset:
---

## 🛠️ Key Contributions

- 🔧 Developed a RAG-based **research & journal retrieval system** using document embeddings stored in FAISS.
- ✍️ Engineered a **BART-powered content humanization pipeline** that rewrites detected AI content to human tone.
- 🧪 Created an **AI content detector** to flag AI-written sections and replace them with more natural writing.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/AI-ResearchMate.git
   cd AI-ResearchMate
   ```

## License
This project is licensed under the [MIT License](https://github.com/ovuiproduction/Research-Assistant/blob/main/LICENSE)
