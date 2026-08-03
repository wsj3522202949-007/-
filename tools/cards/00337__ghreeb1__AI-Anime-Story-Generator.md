---
id: tool-00337
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Anime-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ghreeb1/ai-anime-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 337
category: 二、网文 / 长篇 AI 写作系统 库
repo: ghreeb1/AI-Anime-Story-Generator
stars: 1
url: https://github.com/ghreeb1/ai-anime-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ghreeb1/AI-Anime-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ghreeb1/ai-anime-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Anime Story Generator  transforms stories or dialogues into anime-style comics. It uses NLP to analyze text, structure scenes, and extract dialogues, while Stable Diffusion generates high-quality illustrations. A web interface assembles panels with speech bubbles, merging AI and creativity in storytelling.
- **本地描述**：AI Anime Story Generator  transforms stories or dialogues into anime-style comics. It uses NLP to analyze text, structure scenes, and extract dialogues, while Stable Diffusion generates high-quality illustrations. A web interface assembles panels with speech bubbles, merging AI and creativity in storytelling.
- **拉取时间**：2026-07-23 22:48:55

---

# AI Story-to-Comic Generator 📖🎨

Prototype full-stack project that transforms **short stories** into **comic pages** using NLP and image generation.  

---

## 🚀 Features
- **FastAPI Backend**  
  Endpoints for:
  - Story parsing  
  - Prompt generation  
  - Image generation (Stable Diffusion)  
  - Comic assembly  

- **Streamlit Frontend**  
  Prototype UI for entering a story and viewing generated comics.  

- **NLP Utilities** (`nlp/`)  
  For text parsing, scene extraction, and dialogue handling.  

- **Generation Utilities** (`generation/`)  
  For prompt formatting and Stable Diffusion integration.  

---

## ⚡ Quickstart (Development)

1. Clone the repo & install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Start the backend (FastAPI):  
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```

3. Start the frontend (Streamlit):  
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

---

## 🎨 Stable Diffusion Configuration

To enable **GPU image generation** with Hugging Face `diffusers`, set the following environment variables:

- `SD_MODEL_ID` → Model ID (default: `runwayml/stable-diffusion-v1-5`)  
- `HF_TOKEN` → (optional) Hugging Face access token (for private models)  
- `SD_OUTPUT_DIR` → Output directory for generated images (default: `output/images`)  

👉 If `diffusers` or CUDA are not available, the app will **fall back to placeholder images** so the UI remains functional.  

Example (Linux/Mac):
```bash
export SD_MODEL_ID="runwayml/stable-diffusion-v1-5"
export HF_TOKEN="your_hf_token_here"
export SD_OUTPUT_DIR="./output/images"
```

---

## 📂 Project Structure
```
AI-Story-to-Comic-Generator/
│── backend/              # FastAPI backend
│   └── main.py
│── frontend/             # Streamlit frontend prototype
│   └── streamlit_app.py
│── nlp/                  # NLP utilities (story parsing, dialogues, etc.)
│── generation/           # Prompt + image generation utils
│── output/               # Generated images & comics
│── requirements.txt
│── README.md
```

---

## 🛠 Tech Stack
- **Backend** → FastAPI  
- **Frontend** → Streamlit  
- **Image Generation** → Stable Diffusion (`diffusers`)  
- **NLP** → spaCy / custom utilities  
- **Assembly** → PIL / custom scripts  

---

## 📌 Notes
- This is a **prototype**, not production-ready.  
- Works even without GPU (uses placeholder images).  

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🔮 Future Work / Roadmap
- [ ] Add **automatic speech bubbles** with text overlay.  
- [ ] Support for **multi-panel comic pages**.  
- [ ] Improve **text clarity inside images**.  
- [ ] Fine-tuned Stable Diffusion models for **comic / manga style**.  
- [ ] Export final comics as **PDF / CBZ formats**.  
- [ ] Enhance frontend with **drag-and-drop editing**.  
- [ ] Multi-language story input support.  

## 📧 Contact

**Developer:**  
<h2 align="center">Mohamed Khaled</h2>

<p align="center">
  <a href="mailto:qq11gharipqq11@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/mohamed-khaled-3a9021263" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://github.com/ghreeb1/AI-Anime-Story-Generator" target="_blank">
    <img src="https://img.shields.io/badge/-Project%20Link-24292F?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>



