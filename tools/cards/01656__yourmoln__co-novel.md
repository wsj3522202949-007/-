---
id: tool-01656
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: co-novel
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/yourmoln/co-novel
created: 2026-07-18
updated: 2026-07-18
no: 1656
category: 二、网文 / 长篇 AI 写作系统 库
repo: yourmoln/co-novel
stars: 0
url: https://github.com/yourmoln/co-novel
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# yourmoln/co-novel

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yourmoln/co-novel
- **Stars**：0
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：A tool for writing novels with AI assistance
- **本地描述**：A tool for writing novels with AI assistance
- **拉取时间**：2026-07-23 23:27:20

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# co-novel

一个用AI辅助写小说的助手。

## 项目结构

- `backend/` - 后端服务
- `frontend/` - 前端应用
- `docs/` - 文档

## 技术栈

- 后端: Python, FastAPI
- 前端: Vue, Element Plus
- 数据库: SQLite
- AI: OpenAI API

## 开发

### 环境设置

#### 前端

1. 安装依赖:

```bash
pnpm install
```

2. 启动开发服务器:

```bash
pnpm dev
```

#### 后端

1. 安装 [uv](https://github.com/astral-sh/uv) 包管理器
2. 安装依赖:

```bash
uv sync
```

3. 启动开发服务器:

```bash
uv run python -m main
```

## 部署

部署到 [Railway](https://railway.app) 或 [Render](https://render.com)。
