---
id: tool-01027
type: tool
area: 库
status: active
tags: [RAG, 多Agent, Python, 协议宽松, 需API密钥, 英文文档, 人物设定]
title: Agentic-RAG-Visual-Story-Generator
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/tungducvu/agentic-rag-visual-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1027
category: 二、网文 / 长篇 AI 写作系统 库
repo: TungDucVu/Agentic-RAG-Visual-Story-Generator
stars: 1
url: https://github.com/tungducvu/agentic-rag-visual-story-generator
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 263b2f4cbf2fbeb7
  - methods/最强写作方法论_全球最强综合版.md
---

# TungDucVu/Agentic-RAG-Visual-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tungducvu/agentic-rag-visual-story-generator
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：agentic-ai, ai, chromadb, gpt-4o, langgraph, llm, multimodel-ai, python, rag, retrieval-augmented-generation, story-generation, streamlit, text-to-speech, vector-database, visual-storytelling
- **GitHub 描述**：An Agentic AI-powered visual storytelling system that generates rich, creative narratives from images using Multimodal LLMs + Retrieval-Augmented Generation (RAG).
- **本地描述**：An Agentic AI-powered visual storytelling system that generates rich, creative narratives from images using Multimodal LLMs + Retrieval-Augmented Generation (RAG).
- **拉取时间**：2026-07-23 23:08:57

---

# 📖 Agentic RAG Visual Story Generator

An **Agentic AI-powered visual storytelling system** that generates rich, creative narratives from images using **Multimodal LLMs + Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Overview

This project combines:

- 🧠 **LLM (GPT-4o)** for story generation  
- 🖼️ **Multimodal input (images + text)**  
- 🔎 **RAG (Retrieval-Augmented Generation)** for contextual storytelling  
- 🧩 **LangGraph Agentic Workflow** for structured reasoning  
- 🗃️ **Chroma Vector DB** for similarity search  
- ☁️ **Cloudinary** for image hosting  
- 🎙️ **Text-to-Speech** for narration  
- 🌐 **Streamlit UI** for interaction  

👉 The system takes an uploaded image and generates a **context-aware story** by retrieving similar image-text pairs and blending them creatively.

---

## 🧠 How It Works

### 🔁 Pipeline Flow

1. Image Upload  
2. Image Captioning (LLM Tool Node)  
3. Dynamic Query Generation  
4. Vector Search (MMR Retrieval)  
5. Context Extraction (Text + Images)  
6. Multimodal Story Generation (LLM)  
7. Output + Voice Narration  

---

## 🏗️ Architecture

```
User Image
   ↓
LLM (Caption Generator)
   ↓
Dynamic Query
   ↓
Chroma DB (MMR Search)
   ↓
Retrieved Stories + Images
   ↓
Multimodal Prompt
   ↓
GPT-4o
   ↓
Generated Story + Audio
```

---

## ⚙️ Tech Stack

| Component        | Technology |
|----------------|----------|
| LLM            | GPT-4o (via OpenAI-compatible API) |
| Embeddings     | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB      | Chroma |
| Workflow       | LangGraph |
| Backend        | Python |
| UI             | Streamlit |
| Image Hosting  | Cloudinary |
| TTS            | pyttsx3 |

---

## 📂 Project Structure

```
├── Agentic_Workflow.py
├── chroma_store/
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
LLM_API_KEY=your_api_key
LLM_BASE_URL=your_base_url

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/agentic-rag-story-generator.git
cd agentic-rag-story-generator
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run Agentic_Workflow.py
```

---

## 🧩 Key Features

- Retrieval-Augmented Generation (RAG)  
- Agentic Workflow (LangGraph)  
- Multimodal Reasoning (Image + Text)  
- Max Marginal Relevance (MMR) Search  
- Text-to-Speech Output  

---

## ⚠️ Limitations

- Requires external APIs  
- Performance depends on dataset quality  
- Base64 conversion may slow down processing  

---

## 🔮 Future Improvements (not yet done)

- Hybrid search (image + text embeddings)  
- Better caching & optimization  
- Multi-step storytelling memory  
- Full deployment (FastAPI + frontend)  

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📜 License

MIT License
