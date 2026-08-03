---
id: tool-00523
type: tool
area: 库
status: active
tags: [RAG, Python, 协议宽松, 本地优先, 英文文档, 人物设定, 本地写作]
title: AI-Novelist-RAG---Long-Form-Story-Generation-with-Memory
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/nanfang-wuyu/ai-novelist-rag---long-form-story-generation-with-memory
created: 2026-07-18
updated: 2026-07-18
no: 523
category: 二、网文 / 长篇 AI 写作系统 库
repo: nanfang-wuyu/AI-Novelist-RAG---Long-Form-Story-Generation-with-Memory
stars: 1
url: https://github.com/nanfang-wuyu/ai-novelist-rag---long-form-story-generation-with-memory
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# nanfang-wuyu/AI-Novelist-RAG---Long-Form-Story-Generation-with-Memory

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nanfang-wuyu/ai-novelist-rag---long-form-story-generation-with-memory
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：nanfang-wuyu/AI-Novelist-RAG---Long-Form-Story-Generation-with-Memory
- **拉取时间**：2026-07-23 22:54:18

---

<!-- ---
title: "AI Novelist RAG"
emoji: "📚"
colorFrom: "indigo"
colorTo: "purple"
sdk: docker
sdk_version: 28.0.4
python_version: 3.10.16
app_port: 7860
accelerator: cpu # gpu when local, be online in future
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- -->


# AI Novelist RAG - Long-Form Story Generation with Memory

This is a dedicated AI system for generating long-form novels with coherent logic, consistent world-building, and thematic integrity, solving common LLMs issues like incoherence, self-contradiction, and theme drift.

This project combines Langchain, Retrieval-Augmented Generation (RAG), FAISS, FastAPI, and Gradio, along with OpenAI or local quantized models (e.g., LLaMA). It allows the AI to extract key information and context from its own outputs and store them in a vector database to “remember” what it’s written—resulting in more logical and immersive storytelling. 

This system is designed as both a technical practice and a creative tool. 

## Key Features

- High-quality novel generation (via OpenAI APIs or local LLMs)
- Automatic information extraction (currently via BERT-based summary model)
- Long-context memory (via FAISS vector store)
- Context-aware coherent prompt (via RAG-like context enhancement)
- Web-based UI (via Gradio)
- Experimental consistency scoring (planned to use long-context metrics)

## Project Structure

```
ai-novelist-rag/
├── app/
│   ├── main.py                # FastAPI + Gradio mount point
│   ├── apis/                  # API endpoints for generation, editing, benchmarks
│   ├── front_end/             # Gradio-based UI
│   ├── managers/              # Managers and chains for chapter, summary, and vector memory
│   ├── models/                # Model loading and wrapper logic
│   ├── tests/                 # (Not showed here) Jupyter notebooks for quick testing
│   └── utils/                 # General utilities 
│
├── data/                      # (Not showed here) Local store for texts, summaries, vector DB 
├── docker/                    # Dockerfile and config for deployment
├── scripts/
│   ├── setup.sh               # Install dependencies
│   └── start.sh               # Start the app program
│
├── requirements.txt
├── README.md
├── Dockerfile
└── .gitignore
```

## Getting Started

1. Install dependencies:

```bash
bash scripts/setup.sh
```

2. Start the app program:

```bash
bash scripts/start.sh
```

Default setup:

- Uses gpt-4o-mini (via OpenAI API) for novel generation
- Uses bart-large-cnn for chapter summarization  
- Configurable in config.py (coming soon)

Requires your own OpenAI API key

## Coming Soon

- Chinese-style writing support
- Multiple books/novels within the same workspace
- Streaming generation responses to frontend
- Benchmark consistency improvement with and without memory
- Deployment to Azure

## Contributing

This project is still under active development, Star, Fork, and PRs are welcome!
