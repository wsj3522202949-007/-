---
id: tool-00659
type: tool
area: 库
status: active
tags: [互动叙事, TypeScript, 协议未明, 需API密钥, 中文友好]
title: ai-story-generator
summary: 互动叙事/聊天写故事
source: https://github.com/richwzz77-cloud/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 659
category: 二、网文 / 长篇 AI 写作系统 库
repo: richwzz77-cloud/ai-story-generator
stars: 0
url: https://github.com/richwzz77-cloud/ai-story-generator
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# richwzz77-cloud/ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/richwzz77-cloud/ai-story-generator
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：qunar story
- **本地描述**：qunar story
- **拉取时间**：2026-07-23 22:58:16

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI 故事冒险生成器

一个基于大型语言模型的互动式文本冒险游戏生成器，类似 AI Dungeon。

## 功能特性

- 🎮 互动式故事生成
- 👤 用户系统与故事存档
- 🌟 多种故事背景和角色
- 💾 自动保存与分支功能
- 🔗 故事分享与协作
- 🎨 现代化用户界面

## 技术栈

### 前端
- React 18
- TypeScript
- Tailwind CSS
- Zustand (状态管理)
- React Router

### 后端
- Node.js + Express
- TypeScript
- Prisma (数据库 ORM)
- JWT (身份认证)
- OpenAI API

### 数据库
- PostgreSQL (生产环境)
- SQLite (开发环境)

## 快速开始

1. 安装依赖
```bash
npm install
```

2. 设置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，添加必要的 API 密钥
```

3. 启动开发服务器
```bash
npm run dev
```

## 项目结构

```
├── client/          # React 前端
├── server/          # Node.js 后端
├── shared/          # 共享类型定义
└── docs/           # 文档
```

## 环境变量

```env
# 数据库
DATABASE_URL="postgresql://username:password@localhost:5432/ai_story"

# JWT 密钥
JWT_SECRET="your-jwt-secret"

# OpenAI API
OPENAI_API_KEY="your-openai-api-key"

# 服务器配置
PORT=3001
NODE_ENV=development
```
