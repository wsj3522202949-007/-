---
id: tool-00784
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: universe-book-writer
summary: Claude Code 插件式写作流
source: https://github.com/joshuazick1/universe-book-writer
created: 2026-07-18
updated: 2026-07-18
no: 784
category: 二、网文 / 长篇 AI 写作系统 库
repo: joshuazick1/universe-book-writer
stars: 0
url: https://github.com/joshuazick1/universe-book-writer
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# joshuazick1/universe-book-writer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/joshuazick1/universe-book-writer
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Multi-Universe Book Series Writing Assistant - A comprehensive tool for writing and managing book series across multiple fictional universes.
- **本地描述**：Multi-Universe Book Series Writing Assistant - A comprehensive tool for writing and managing book series across multiple fictional universes.
- **拉取时间**：2026-07-23 23:01:53

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Multi-Universe Book Series Writing Assistant

A modern, AI-powered writing assistant that helps authors create and manage book series across multiple fictional universes. The application provides a flexible, plugin-based architecture that supports any fictional universe through a consistent interface.

## Features

- World building and management
- Character development tools
- Story consistency checking
- AI-assisted writing with Ollama
- Real-time collaboration
- Plugin system for different universes

## Project Structure

The project is organized as a monorepo containing:

- `frontend`: React + TypeScript + Vite application
- `backend`: Node.js + Express + TypeScript server
- `ai-server`: Ollama server management
- `packages`: Shared core libraries
- `plugins`: Official universe plugins
- `tools`: Development utilities

## Getting Started

1. Install Git: Download and install from https://git-scm.com/downloads

2. Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd universe-book-writer
npm install
```

3. Build core packages:

```bash
npm run build
```

4. Start development servers:

```bash
# Frontend
cd frontend
npm run dev

# Backend (in a new terminal)
cd backend
npm run dev

# AI Server (in a new terminal)
cd ai-server
npm run dev
```

## Contributing

Please read our `[Contributing Guide](CONTRIBUTING.md)` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `[LICENSE](LICENSE)` file for details.
