---
id: tool-00984
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: news-copilot-reader
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tnowad/news-copilot-reader
created: 2026-07-18
updated: 2026-07-18
no: 984
category: 二、网文 / 长篇 AI 写作系统 库
repo: tnowad/news-copilot-reader
stars: 0
url: https://github.com/tnowad/news-copilot-reader
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tnowad/news-copilot-reader

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tnowad/news-copilot-reader
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai, flask, sveltekit, text-completion
- **GitHub 描述**：AI-powered news platform with custom transformer model for intelligent article completion and real-time writing assistance
- **本地描述**：AI-powered news platform with custom transformer model for intelligent article completion and real-time writing assistance
- **拉取时间**：2026-07-23 23:07:44

---

# News Copilot Reader

A full-stack news platform with AI-powered text generation and smart writing assistance.

[![CI](https://github.com/user/news-copilot-reader/actions/workflows/ci.yml/badge.svg)](https://github.com/user/news-copilot-reader/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Node 20](https://img.shields.io/badge/node-20-green.svg)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## Overview

News Copilot Reader is a web application that combines a news publishing platform with AI-assisted writing features. It provides article CRUD, user authentication, commenting, bookmarking, and smart text completion powered by a custom transformer model built from scratch.

## Architecture

```text
  Browser
     │
     ▼
  SvelteKit (port 5173)
     │
     │  HTTP / REST
     ▼
  Flask API (port 5000)
     │
     ├──── PostgreSQL (port 5432)
     ├──── Redis (port 6379)
     └──── Transformer model (PyTorch)
```

## Tech Stack

### Frontend
- SvelteKit 2 + TypeScript 5
- TailwindCSS 3 + Flowbite
- Monaco Editor for rich text editing
- svelte-i18n for internationalization (EN/VI)
- Vite 5 build tooling

### Backend
- Flask 3.0 + Gunicorn
- SQLAlchemy 2.0 + Flask-Migrate (Alembic)
- JWT authentication with refresh tokens
- Redis caching layer
- Marshmallow validation
- Rate limiting middleware
- Structured logging with structlog

### AI/ML
- Custom Transformer architecture:
  - Grouped Query Attention (GQA)
  - Sliding Window Attention
  - Rotary Position Embeddings (RoPE)
  - RMSNorm + SwiGLU activation
- SentencePiece BPE tokenizer
- Mixed precision training (FP16/BF16)
- Distributed training support (DDP)
- WandB experiment tracking

### Infrastructure
- Docker + Docker Compose
- GitHub Actions CI/CD
- Prometheus metrics

## Quick Start

### With Docker (Recommended)

```bash
docker compose up --build
```

This starts PostgreSQL, Redis, the backend API, and the frontend all at once.

### Manual Setup

**Prerequisites:** Python 3.11+, Node.js 20+, PostgreSQL 16, Redis 7, pnpm

```bash
# Backend
cd news-copilot-backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # Edit with your configuration
flask run

# Frontend (in another terminal)
cd news-copilot-frontend
pnpm install
pnpm dev
```

## Running Tests

```bash
# All tests
make test

# Backend tests with coverage
make test-backend-cov

# Frontend tests
make test-frontend
```

## Project Structure

```
news-copilot-reader/
├── .github/
│   └── workflows/ci.yml           # CI pipeline
├── news-copilot-frontend/         # SvelteKit frontend
│   ├── src/
│   │   ├── lib/
│   │   │   ├── services/          # API client layer
│   │   │   ├── widgets/           # Reusable UI components
│   │   │   ├── i18n/              # Internationalization
│   │   │   └── utils/             # Utility functions
│   │   └── routes/                # SvelteKit pages
│   └── tests/                     # Frontend tests
├── news-copilot-backend/          # Flask backend
│   ├── app/
│   │   ├── models/                # SQLAlchemy models
│   │   ├── routes/                # API blueprints
│   │   ├── services/              # Business logic
│   │   ├── middleware/            # Request/Security middleware
│   │   ├── decorators/            # Auth/Validation decorators
│   │   └── utils/                 # Helpers (logging, errors, etc.)
│   ├── migrations/                # Alembic migrations
│   └── tests/                     # Backend tests
├── news-copilot-models/           # Custom transformer models
│   ├── models/                    # Model architecture
│   ├── training/                  # Training pipeline
│   ├── inference/                 # Inference API
│   ├── data/                      # Data processing
│   ├── config/                    # Training configs
│   └── utils/                     # CLI tools
├── docker-compose.yml
├── Makefile
└── .pre-commit-config.yaml
```

## API Endpoints

| Group | Endpoints | Auth |
|-------|-----------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Auth | `POST /auth/sign-in`, `/sign-up`, `/refresh`, `/forgot-password`, `/reset-password` | JWT |
| Articles | `GET/POST /articles/`, `GET/PUT/DELETE /articles/:slug/:id` | JWT |
| Categories | `GET/POST /categories/` | Admin for write |
| Comments | `GET/POST /comments/` | JWT |
| Bookmarks | `GET/POST/DELETE /bookmarks/` | JWT |
| Generation | `POST /generate-text`, `/complete-article`, `/generate-headline` | JWT |
| Users | `GET /users/` | Admin |
| Health | `GET /health`, `/metrics` | Public |

Full API documentation is available in `[news-copilot-backend/README.md](news-copilot-backend/README.md)`.

## License

MIT
