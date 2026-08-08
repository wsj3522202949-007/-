---
id: tool-00472
type: tool
area: 库
status: active
tags: [RAG, TTS, Python, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: GenAI-writing-assistant-project
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/cylinderstudio/genai-writing-assistant-project
created: 2026-07-18
updated: 2026-07-18
no: 472
category: 二、网文 / 长篇 AI 写作系统 库
repo: cylinderStudio/GenAI-writing-assistant-project
stars: 0
url: https://github.com/cylinderstudio/genai-writing-assistant-project
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ac2e9a103ff9ab7f
  - methods/最强写作方法论_全球最强综合版.md
---

# cylinderStudio/GenAI-writing-assistant-project

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cylinderstudio/genai-writing-assistant-project
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Exercise to build an writer's tool that enforces a brand voice
- **本地描述**：Exercise to build an writer's tool that enforces a brand voice
- **拉取时间**：2026-07-23 22:52:51

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Writing Assistant Project

This project is an experiment to create a generative AI assistant that could help a company’s marketing, advertising, or PR teams quickly generate documents that conform to style, tone, and brand guidelines.

<img src="https://github.com/user-attachments/assets/b2955ece-2557-4810-93bd-0e1f85cc0fa7" alt="UI" width="600"/>

**This repo contains the Python scripts used to:**
1. Create training data
2. Fine-tune a base model with training data and save as GGUF
3. Clean, chunk and upsert data for RAG vector database
4. Create a UI with inference logic
    - `app.py`: model inference only
    - `app-plus-rag.py`: inference + vector database/RAG

**Model Training**
Fine-tuning was performed on Meta Llama 3.1 8B Instruct, using Google Colab and the [Unsloth](https://github.com/unslothai/unsloth) framework.

**RAG**
Retrieval Augmented Generation is provided with [Pinecone](https://www.pinecone.io/).

**Inference**
Fine-tuned model is stored on Hugging Face and uses [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index). The user interface was built with [Gradio](https://www.gradio.app/).
