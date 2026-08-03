---
id: tool-01461
type: tool
area: 库
status: active
tags: [RAG, 多Agent, 大纲规划, TypeScript, 协议宽松, 需API密钥, 中文友好, 人物设定]
title: NovelCraft-Agent-with-Memory-RAG
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/autumnsnow919/novelcraft-agent-with-memory-rag
created: 2026-07-18
updated: 2026-07-18
no: 1461
category: 二、网文 / 长篇 AI 写作系统 库
repo: Autumnsnow919/NovelCraft-Agent-with-Memory-RAG
stars: 2
url: https://github.com/autumnsnow919/novelcraft-agent-with-memory-rag
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Autumnsnow919/NovelCraft-Agent-with-Memory-RAG

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/autumnsnow919/novelcraft-agent-with-memory-rag
- **Stars**：2
- **语言**：TypeScript
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Autumnsnow919/NovelCraft-Agent-with-Memory-RAG
- **拉取时间**：2026-07-23 23:21:41

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NovelCraft - AI 小说创作助手

NovelCraft 是一个智能的、代理式（Agentic）小说写作环境，旨在帮助作者创作连贯、高质量的故事。它结合了现代富文本编辑器与强大的 AI 代理，该代理拥有长期记忆、RAG（检索增强生成）能力以及专业的写作技能。

## 功能特性

### 🧠 核心记忆系统 (Core Memory System)
NovelCraft 维护着你小说的结构化记忆，确保 AI 永远不会忘记关键细节：
- **小说圣经 (Novel Bible)**：存储世界规则、魔法系统和设定细节。
- **角色数据库 (Character Database)**：追踪角色档案、关系和状态更新。
- **时间线 (Timeline)**：记录按时间顺序发生的事件，防止连贯性错误。
- **伏笔账本 (Foreshadowing Ledger)**：追踪埋下的伏笔，确保它们得到收束。
- **风格指南 (Style Guide)**：保持章节间一致的语气和文风。

### 🤖 专业代理技能 (Specialized Agent Skills)
AI 不仅仅是一个聊天机器人，它拥有专业的角色：
- **世界构建者 (World Builder)**：从简单的想法生成丰富的设定、派系和历史。
- **章节作家 (Chapter Writer)**：根据你的大纲和上下文起草完整的章节。
- **润色与重写 (Polish & Rewrite)**：在遵守你的风格指南的同时提高散文质量。
- **情节扩展者 (Plot Extender)**：当你卡住时，提供多种情节发展方向的建议。
- **记忆档案员 (Memory Archivist)**：自动分析新章节以更新核心记忆。

### 🔍 RAG (检索增强生成)
- **向量搜索 (Vector Search)**：自动索引你的章节和记忆。
- **上下文感知 (Context Awareness)**：代理在写作时检索相关的过去事件和细节，即使在长篇作品中也能确保持续性。

### ✍️ 现代编辑器
- **无干扰写作 (Distraction-Free Writing)**：专注于文本的干净界面。
- **分屏视图 (Split View)**：在编辑器旁边查看你的记忆/笔记。
- **代理集成 (Agent Integration)**：与代理聊天，就地预览草稿，并通过差异视图（Diff View）应用更改。

## 技术栈
- **框架**: Next.js 15 (App Router)
- **语言**: TypeScript
- **数据库**: SQLite (via Prisma)
- **向量数据库**: Vectra (本地基于文件的向量存储)
- **UI**: Tailwind CSS, Shadcn/UI
- **LLM 集成**: OpenAI 兼容 API (适用于 OpenAI, Anthropic, DeepSeek, LocalLLMs 等)

## 快速开始

### 前置要求
- Node.js 18+
- npm 或 pnpm

### 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/autumnsnow919/novel-agent.git
   cd novel-agent
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 配置环境：
   在根目录创建一个 `.env` 文件：
   ```env
   # 数据库 (默认 SQLite)
   DATABASE_URL="file:./dev.db"

   # LLM 提供商 (示例：OpenAI 或兼容的 API)
   OPENAI_API_KEY="sk-..."
   OPENAI_BASE_URL="https://api.openai.com/v1"
   OPENAI_MODEL="gpt-4o"
   
   # Embedding 模型 (可选，默认为 text-embedding-3-small 或兼容模型)
   EMBEDDING_MODEL="text-embedding-3-small"
   ```

4. 初始化数据库：
   ```bash
   npx prisma generate
   npx prisma db push
   ```

5. 运行开发服务器：
   ```bash
   npm run dev
   ```

6. 在浏览器中打开 [http://localhost:3000](http://localhost:3000)。

## 使用指南

1. **创建小说**：点击顶部下拉菜单中的 "Create New" (新建)。
2. **世界构建**：使用 `/world-builder` 技能生成你的设定。
3. **写作**：手动编写或要求代理 `/chapter-writer` (写章节)。
4. **保存**：当你保存 (Ctrl+S) 时，系统会自动索引内容并更新记忆。
5. **回顾**：检查 "Memory" (记忆) 选项卡，查看 AI 如何追踪你的故事。

## 许可证
Apache License 2.0
