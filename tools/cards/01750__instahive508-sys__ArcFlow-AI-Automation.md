---
id: tool-01750
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ArcFlow-AI-Automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/instahive508-sys/arcflow-ai-automation
created: 2026-07-18
updated: 2026-07-18
no: 1750
category: 二、网文 / 长篇 AI 写作系统 库
repo: instahive508-sys/ArcFlow-AI-Automation
stars: 1
url: https://github.com/instahive508-sys/arcflow-ai-automation
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# instahive508-sys/ArcFlow-AI-Automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/instahive508-sys/arcflow-ai-automation
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ArcFlow is an AI-powered automation platform built for the Arc.Network ecosystem. With a visual drag-and-drop canvas, it lets you trigger effortless workflows, connect advanced AI models (Gemini, OpenAI, Claude), and execute secure blockchain transactions with Circle—all without writing a single line of code.
- **本地描述**：ArcFlow is an AI-powered automation platform built for the Arc.Network ecosystem. With a visual drag-and-drop canvas, it lets you trigger effortless workflows, connect advanced AI models (Gemini, OpenAI, Claude), and execute secure blockchain transactions with Circle—all without writing a single line of code.
- **拉取时间**：2026-07-23 23:30:03

---

# ArcFlow

**N8N-Style Workflow Automation with Arc Network & Circle Integration**

ArcFlow is a production-ready workflow automation platform inspired by n8n, featuring native integration with Arc Network and Circle for blockchain-powered automation.

## ✨ Features

- **80+ Node Types** - Triggers, data transformation, HTTP, databases, AI, and more
- **Expression Engine** - Full n8n-style expressions with `$json`, `$node`, `$items`, `$now`
- **AI Integration** - Gemini, OpenAI, Claude with tool calling and memory
- **Credential Management** - 25+ credential types with secure storage
- **Arc/Circle Blockchain** - Native USDC transfers, smart contracts, CCTP bridging
- **Visual Canvas** - Drag-and-drop workflow builder with zoom/pan

## 🚀 Quick Start

### Installation

This project is zero-dependency. No installation required.

```bash
# 1. Download or Clone
git clone https://github.com/your-org/arcflow.git
cd arcflow

# 2. Start the built-in server
php -S localhost:3000 router.php
```

Open `http://localhost:3000` in your browser.

## 📚 Node Categories

| Category | Examples |
|----------|-------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| **Triggers** | Manual, Webhook, Schedule, x402 Payment |
| **AI** | Gemini, OpenAI, Claude, Window Buffer Memory |
| **Data** | Set, Code, IF, Switch, Loop, Merge, Sort |
| **Actions** | HTTP Request, Email, Slack, Discord, Telegram |
| **Database** | PostgreSQL, MySQL, Supabase |
| **Google** | Sheets, Drive, Gmail, Calendar |
| **Arc/Circle** | Wallet, USDC Transfer, Smart Contract, CCTP, Gas Station |

## 🔐 Credential Types

- Google OAuth2, OpenAI, Anthropic, Gemini
- PostgreSQL, MySQL, Supabase, Slack, Discord, Telegram
- Circle Developer (WaaS), Arc Wallet, ArcScan
- Header Auth, Basic Auth, Bearer Token, and more

## 📖 Documentation

- **Workflow Editor**: `landwork.html` - Main canvas for building workflows
- **Credentials**: `credits.html` - Manage API keys and OAuth connections
- **API**: `api.php` - Workflow and credential storage endpoints
- **Nodes Backend**: `nodes1.php` - Server-side node execution

## 🏗️ Architecture

```
ArcFlow/
├── index.html          # Landing page
├── landwork.html       # Workflow editor
├── credits.html        # Credentials list
├── landcredits.html    # Credential editor
├── nodes1.js           # Frontend engine (11,000+ lines)
├── nodes1.php          # Backend handlers (3,000+ lines)
├── api.php             # Storage API
├── router.php          # HTTP router + webhooks
├── style.css           # UI styles
└── storage/            # Data persistence
```

## 🔒 Security

- SSL verification enabled for all external requests
- Parameterized database queries (SQL injection prevention)
- Encrypted Circle entity secrets (RSA-OAEP)
- Webhook signature verification

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🌍 Deployment

Ready to go live? Check out our comprehensive **[Deployment Guide](https://github.com/instahive508-sys/ArcFlow-AI-Automation/blob/main/DEPLOY.md)** for instructions on hosting ArcFlow on Ubuntu with Nginx.

## 🙏 Acknowledgments

- **Made by Instaflect AI**
- Inspired by [n8n](https://n8n.io)
- Built for the Arc Network Hackathon
- Powered by Circle's Programmable Wallets

