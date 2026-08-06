---
id: tool-01381
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: swrpg-gen
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/magicat777/swrpg-gen
created: 2026-07-18
updated: 2026-07-18
no: 1381
category: 二、网文 / 长篇 AI 写作系统 库
repo: magicat777/swrpg-gen
stars: 3
url: https://github.com/magicat777/swrpg-gen
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# magicat777/swrpg-gen

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/magicat777/swrpg-gen
- **Stars**：3
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered Star Wars RPG story generator with Neo4j, MongoDB, Weaviate, and LocalAI
- **本地描述**：AI-powered Star Wars RPG story generator with Neo4j, MongoDB, Weaviate, and LocalAI
- **拉取时间**：2026-07-23 23:19:24

---

# SWRPG-GEN: Star Wars RPG Story Generator

An AI-powered tabletop RPG assistant that helps Game Masters create immersive Star Wars narratives using graph databases, vector search, and local language models.

## 🌟 Features

- **AI Story Generation**: Context-aware narrative generation with streaming responses
- **Multi-Database Integration**: Neo4j (graph), MongoDB (documents), Weaviate (vectors)
- **Local LLM**: Privacy-focused with Mistral 7B running via LocalAI
- **Web Interface**: React 18 frontend with Star Wars-themed UI
- **GPU Accelerated**: Optimized for NVIDIA GPUs (RTX 4080 tested)

## 🚀 Tech Stack

- **Frontend**: React 18 + TypeScript + Vite + Styled Components
- **Backend**: Node.js + Express + TypeScript
- **Databases**: Neo4j, MongoDB, Weaviate
- **AI/ML**: LocalAI with Mistral 7B
- **Infrastructure**: Docker Compose with GPU support

## 📋 Prerequisites

- Ubuntu 22.04+ or compatible Linux
- Docker & Docker Compose
- NVIDIA GPU with 8GB+ VRAM (optional but recommended)
- 32GB+ RAM
- 100GB+ free disk space

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/magicat777/swrpg-gen.git
   cd swrpg-gen
   ```

2. Copy environment template:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Deploy services:
   ```bash
   ./scripts/deployment/deploy.sh
   ```

4. Access the application:
   - Frontend: http://localhost:3001
   - API: http://localhost:3000

## 📖 Documentation

Comprehensive documentation is available in the `/docs` directory:
- [Project Overview](https://github.com/magicat777/swrpg-gen/blob/main/docs/PROJECT_STATUS_OVERVIEW.md)
- [Backend Architecture](https://github.com/magicat777/swrpg-gen/blob/main/docs/BACKEND_ARCHITECTURE.md)
- [Database Schemas](https://github.com/magicat777/swrpg-gen/tree/main/docs/schemas/)
- [Setup Guides](https://github.com/magicat777/swrpg-gen/tree/main/docs/)

## 🏗️ Project Status

- **Development**: 89% complete (Phase 8/13)
- **Production Ready**: Passed E2E testing
- **Current Phase**: Deployment & Source Code Integration

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- LocalAI community for the excellent local LLM runtime
- Neo4j, MongoDB, and Weaviate teams for their databases
- The Star Wars fan community

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*May the Force be with your storytelling!*
