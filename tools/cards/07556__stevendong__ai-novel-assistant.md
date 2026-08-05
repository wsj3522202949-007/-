---
id: tool-07556
type: tool
area: 库
status: active
tags: [Vue, 协议未明, 需API密钥, 中文友好]
title: ai-novel-assistant
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/stevendong/ai-novel-assistant
created: 2026-07-18
updated: 2026-07-18
no: 7556
category: 画龙补充 / 扩容入库 — 补充源
repo: stevendong/ai-novel-assistant
stars: 5
url: https://github.com/stevendong/ai-novel-assistant
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# stevendong/ai-novel-assistant

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/stevendong/ai-novel-assistant
- **Stars**：5
- **语言**：Vue
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Powered Intelligent Novel Writing Collaboration Platform. Let AI be your writing partner, not your replacement
- **本地描述**：ai-novel-assistant
- **拉取时间**：2026-07-25 19:25:31

---

<div align="center">

[项目Logo占位图 - 建议尺寸: 200x200px, PNG格式, 包含AI和书本元素的现代化图标]

# Smart Pen

[![GitHub Stars](https://img.shields.io/github/stars/stevendong/ai-novel-assistant?style=social)](https://github.com/yourusername/ai-novel-assistant/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/stevendong/ai-novel-assistant?style=social)](https://github.com/yourusername/ai-novel-assistant/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/stevendong/ai-novel-assistant)](https://github.com/yourusername/ai-novel-assistant/issues)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/stevendong/ai-novel-assistant/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

`[English](./README.en.md)` | 简体中文

**AI驱动的智能小说创作协作平台**

让AI成为你的写作伙伴，而不是替代品

[在线演示](#) | [快速开始](#-快速开始) 

</div>

## ⚡ 项目概述

AI Novel Assistant 是一个专为长篇小说创作设计的智能写作辅助平台，通过 AI 技术帮助作家提升创作效率和质量。

### 🎯 核心优势

1. **智能而不越界** - AI 提供建议但不替代创作，保持作者的创作主导权
2. **全流程支持** - 从大纲规划到最终定稿，覆盖小说创作的完整生命周期
3. **知识管理** - 系统化管理角色、世界观、情节线等复杂创作要素
4. **一致性保障** - AI 自动检测并提示角色性格、世界设定、情节逻辑等方面的矛盾
5. **专业编辑体验** - 基于 Tiptap Editor，提供接近 IDE 的强大编辑功能
6. **灵活部署** - 支持本地部署和云端部署，数据完全可控

### 🎬 演示资源

- [功能演示视频占位](#) - 5分钟快速了解核心功能
- [创作流程演示](#) - 完整的小说创作工作流展示
- [示例项目](#) - 查看使用本工具创作的示例小说项目

> "传统写作工具只是记录文字，而 AI Novel Assistant 是一个真正理解你创作需求的智能伙伴。"

---

## 🏗️ 系统架构

### 架构图

[系统架构图占位 - 建议尺寸: 800x600px, 展示前后端分离架构、数据库、AI服务集成]

```
┌─────────────────────────────────────────────────────────────┐
│                        客户端层 (Vue 3)                      │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │项目管理  │角色管理  │世界设定  │章节编辑  │AI助手面板│  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP/WebSocket
┌───────────────────────┴─────────────────────────────────────┐
│                      API 网关层 (Express)                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  认证中间件  │  速率限制  │  CORS  │  日志记录        │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                        业务逻辑层                             │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │项目服务  │角色服务  │设定服务  │章节服务  │AI服务    │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
└───────┬───────────────────────────────────────┬─────────────┘
        │                                       │
┌───────┴──────────┐                  ┌─────────┴────────────┐
│   数据持久层      │                  │    外部服务集成       │
│  ┌────────────┐  │                  │  ┌────────────────┐ │
│  │  Prisma ORM│  │                  │  │  OpenAI API    │ │
│  └─────┬──────┘  │                  │  ├────────────────┤ │
│        │         │                  │  │  Mem0 AI       │ │
│  ┌─────┴──────┐  │                  │  ├────────────────┤ │
│  │SQLite/PG   │  │                  │  │  Cloudflare R2 │ │
│  └────────────┘  │                  │  └────────────────┘ │
└──────────────────┘                  └──────────────────────┘
```

### 核心组件说明

| 组件 | 职责 | 关键技术                          |
|------|------|-------------------------------|
| **项目管理引擎** | 小说项目的CRUD操作、元数据管理、进度追踪 | Prisma ORM, SQLite/PostgreSQL |
| **知识库系统** | 角色档案、世界设定、情节线的结构化存储和检索 | 关系型数据库设计、全文搜索                 |
| **智能编辑器** | 章节内容编辑、多标签管理、自动保存、版本控制 | Tiptap Editor, WebSocket      |
| **AI 协作引擎** | 对话模式、内容增强、一致性检查、情节建议 | OpenAI API, Mem0 AI, 提示工程     |
| **导出引擎** | EPUB、TXT等多格式导出，保留格式和元数据 | epub-gen, Archiver            |
| **认证系统** | 用户身份验证、会话管理、权限控制 | JWT, Clerk (可选)               |

### 完整工作流程

以下是一个典型的小说创作工作流程：

| 步骤 | 操作 | 涉及模块 | AI辅助 |
|------|------|----------|--------|
| 1 | 创建小说项目，填写标题、简介、类型等元数据 | 项目管理 | - |
| 2 | 定义主要角色，包括外貌、性格、背景故事、关系网 | 角色管理 | AI生成角色建议、性格分析 |
| 3 | 构建世界观，添加地点、规则、文化、历史等设定 | 世界设定 | AI协助完善设定逻辑 |
| 4 | 创建章节大纲，规划情节发展 | 章节编辑 | AI提供情节建议和冲突点 |
| 5 | 编写章节内容，使用AI助手进行对话和增强 | 智能编辑器 + AI面板 | 对话式创作、文本润色、扩写 |
| 6 | 运行一致性检查，发现并修复矛盾 | AI协作引擎 | 自动检测角色、设定、情节矛盾 |
| 7 | 导出成品，生成EPUB或TXT格式 | 导出引擎 | - |

### 项目目录结构

```
ai-novel-assistant/
├── client/                          # 前端应用 (Vue 3 + TypeScript)
│   ├── public/                      # 静态资源
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/                  # 样式和资源文件
│   │   │   ├── base.css            # 基础样式
│   │   │   ├── main.css            # Tailwind CSS 入口
│   │   │   └── logo.svg
│   │   ├── components/              # 可复用组件
│   │   │   ├── layout/             # 布局组件
│   │   │   │   ├── MainLayout.vue  # 主布局框架
│   │   │   │   ├── HeaderBar.vue   # 顶部导航栏
│   │   │   │   ├── Sidebar.vue     # 左侧导航栏
│   │   │   │   └── StatusBar.vue   # 底部状态栏
│   │   │   ├── project/            # 项目相关组件
│   │   │   │   ├── ProjectCard.vue
│   │   │   │   └── ProjectForm.vue
│   │   │   ├── character/          # 角色管理组件
│   │   │   │   ├── CharacterList.vue
│   │   │   │   ├── CharacterDetail.vue
│   │   │   │   └── CharacterFormModal.vue
│   │   │   ├── editor/             # 编辑器组件
│   │   │   │   ├── ChapterEditor.vue
│   │   │   │   ├── MonacoEditor.vue
│   │   │   │   └── EditorToolbar.vue
│   │   │   └── ai/                 # AI 助手组件
│   │   │       ├── AIAssistantPanel.vue
│   │   │       ├── ChatInterface.vue
│   │   │       └── EnhancementPanel.vue
│   │   ├── views/                   # 页面视图
│   │   │   ├── ProjectManagement.vue    # 项目管理页
│   │   │   ├── CharacterManagement.vue  # 角色管理页
│   │   │   ├── WorldSettingManagement.vue # 世界设定页
│   │   │   ├── ChapterEditor.vue        # 章节编辑页
│   │   │   └── ProgressStats.vue        # 进度统计页
│   │   ├── stores/                  # Pinia 状态管理
│   │   │   ├── project.ts          # 项目状态
│   │   │   ├── character.ts        # 角色状态
│   │   │   ├── chapter.ts          # 章节状态
│   │   │   └── ai.ts               # AI 助手状态
│   │   ├── services/                # API 服务层
│   │   │   ├── api.ts              # Axios 配置
│   │   │   ├── projectApi.ts       # 项目 API
│   │   │   ├── characterApi.ts     # 角色 API
│   │   │   └── aiApi.ts            # AI API
│   │   ├── router/                  # Vue Router 配置
│   │   │   └── index.ts
│   │   ├── types/                   # TypeScript 类型定义
│   │   │   └── index.ts
│   │   ├── App.vue                  # 根组件
│   │   └── main.ts                  # 应用入口
│   ├── index.html
│   ├── vite.config.ts              # Vite 配置
│   ├── tsconfig.json               # TypeScript 配置
│   ├── tailwind.config.js          # Tailwind CSS 配置
│   └── package.json
│
├── server/                          # 后端应用 (Node.js + Express)
│   ├── routes/                      # API 路由
│   │   ├── novels.js               # 项目路由
│   │   ├── characters.js           # 角色路由
│   │   ├── settings.js             # 世界设定路由
│   │   ├── chapters.js             # 章节路由
│   │   ├── ai.js                   # AI 服务路由
│   │   ├── export.js               # 导出路由
│   │   └── auth.js                 # 认证路由
│   ├── middleware/                  # Express 中间件
│   │   ├── auth.js                 # 认证中间件
│   │   ├── errorHandler.js         # 错误处理
│   │   └── rateLimiter.js          # 速率限制
│   ├── services/                    # 业务逻辑层
│   │   ├── aiService.js            # AI 服务集成
│   │   ├── exportService.js        # 导出服务
│   │   └── consistencyService.js   # 一致性检查
│   ├── prisma/                      # Prisma ORM
│   │   ├── schema.prisma           # 数据库 Schema
│   │   ├── migrations/             # 数据库迁移文件
│   │   └── seed.js                 # 种子数据
│   ├── utils/                       # 工具函数
│   │   ├── logger.js               # 日志工具
│   │   └── helpers.js
│   ├── config/                      # 配置文件
│   │   └── database.js
│   ├── index.js                     # 服务器入口
│   ├── .env.example                 # 环境变量示例
│   └── package.json
│
├── scripts/                         # 构建和部署脚本
│   ├── setup.sh                    # 自动化设置脚本
│   ├── deploy.sh                   # 部署脚本
│   ├── backup.sh                   # 数据备份脚本
│   └── pre-deploy-check.sh         # 部署前检查
│
├── docs/                           # 文档
│   ├── API.md                      # API 文档
│   ├── DEPLOYMENT.md               # 部署指南
│   └── DEVELOPMENT.md              # 开发指南
│
├── .env.example                    # 根环境变量示例
├── package.json                    # 根 package.json (Monorepo)
├── CLAUDE.md                       # Claude Code 开发指南
├── MONOREPO.md                     # Monorepo 架构说明
├── LICENSE                         # MIT 许可证
└── README.md                       # 项目说明文档
```

---

## 🚀 快速开始

### 方式一：Docker 部署 (推荐)

Docker 是最快速、最简单的部署方式，无需手动配置环境。

#### 前置要求
- Docker >= 20.10
- Docker Compose >= 2.0

#### 启动步骤

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/ai-novel-assistant.git
cd ai-novel-assistant

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key

# 3. 启动服务（一键启动）
docker compose up -d

# 4. 访问应用
# 前端: http://localhost:3000
# 后端 API: http://localhost:3001
# Prisma Studio: http://localhost:5555
```

#### 数据库配置

如果使用 PostgreSQL 作为生产数据库：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `DATABASE_URL` | PostgreSQL 连接字符串 | `postgresql://noveluser:changeme@localhost:5432/novel_db` |
| `POSTGRES_USER` | 数据库用户名 | `noveluser` |
| `POSTGRES_PASSWORD` | 数据库密码 | `changeme` |
| `POSTGRES_DB` | 数据库名称 | `novel_db` |

```bash
# 快速启动本地 PostgreSQL (Docker)
docker compose -f docker-compose.postgres.yml up -d postgres

# 应用数据库迁移
npm run db:push
```

### 方式二：源码部署

适合开发者和需要自定义配置的用户。

#### 前置要求
- Node.js >= 20.19.0
- npm >= 9.0.0
- SQLite 3 (开发) 或 PostgreSQL 14+ (生产)

#### 安装步骤

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/ai-novel-assistant.git
cd ai-novel-assistant

# 2. 安装依赖（Monorepo 统一管理）
npm install

# 3. 配置服务端环境变量
cp server/.env.example server/.env
# 编辑 server/.env，配置以下必需项：
# - OPENAI_API_KEY: 你的 OpenAI API 密钥
# - DATABASE_URL: 数据库连接字符串

# 4. 配置客户端环境变量
cp client/.env.example client/.env
# 编辑 client/.env，配置：
# - VITE_API_BASE_URL: 后端 API 地址（默认 http://localhost:3001）

# 5. 初始化数据库
npm run db:push

# 6. 启动开发服务器（前端+后端同时启动）
npm run dev

# 前端服务: http://localhost:5173
# 后端服务: http://localhost:3001
```

#### 分步启动（可选）

如果需要单独启动前端或后端：

```bash
# 仅启动前端
npm run client:dev

# 仅启动后端
npm run server:dev

# 打开 Prisma Studio 数据库管理界面
npm run db:studio
```

### 方式三：一键自动化设置

使用项目提供的自动化脚本：

```bash
# 运行自动设置脚本（会自动检测环境、安装依赖、配置数据库）
./scripts/setup.sh

# 脚本会执行：
# - 检查 Node.js 和 npm 版本
# - 安装所有依赖
# - 复制环境变量模板
# - 初始化数据库
# - 提示下一步操作
```

---

## ⚙️ 环境配置

### 必需配置

#### 服务端环境变量 (`server/.env`)

```bash
# OpenAI API 配置（必需）
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx

# 数据库配置
DATABASE_URL="file:./prisma/novels.db"  # SQLite (开发环境)
# DATABASE_URL="postgresql://user:password@host:5432/dbname"  # PostgreSQL (生产环境)

# 服务器配置
PORT=3001
NODE_ENV=development

# CORS 配置
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

#### 客户端环境变量 (`client/.env`)

```bash
# API 配置（必需）
VITE_API_BASE_URL=http://localhost:3001
```

### 可选配置

#### Clerk 现代化认证（推荐用于生产环境）

```bash
# 客户端 (client/.env)
VITE_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxx

# 认证功能开关
VITE_ALLOW_AUTH_MODE_SWITCH=true      # 允许切换认证模式
VITE_ENABLE_SOCIAL_LOGIN=true         # 启用社交登录
VITE_ENABLE_EMAIL_VERIFICATION=true   # 启用邮箱验证
```

#### Cloudflare R2 对象存储（用于文件上传）

```bash
# 服务端 (server/.env)
R2_ACCOUNT_ID=your_r2_account_id
R2_ACCESS_KEY_ID=your_r2_access_key
R2_SECRET_ACCESS_KEY=your_r2_secret_key
R2_BUCKET_NAME=ai-novel-assistant
R2_PUBLIC_URL=https://your-bucket.r2.cloudflarestorage.com
```

#### 反向代理和安全配置

```bash
# 服务端 (server/.env)
TRUST_PROXY=loopback,linklocal,uniquelocal  # 可信代理配置
RATE_LIMIT_WINDOW_MS=900000                 # 速率限制时间窗口（15分钟）
RATE_LIMIT_MAX_REQUESTS=100                 # 时间窗口内最大请求数
```

### 获取 API 密钥

<details>
<summary><b>📝 OpenAI API Key 获取指南</b></summary>

1. 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
2. 登录或注册账号
3. 点击 "Create new secret key"
4. 复制生成的密钥（格式：`sk-proj-...`）
5. 将密钥填入 `server/.env` 的 `OPENAI_API_KEY`

**注意事项：**
- 密钥只显示一次，务必保存
- 建议设置使用限额避免意外费用
- 不要将密钥提交到版本控制系统
</details>

<details>
<summary><b>🔐 Clerk Publishable Key 获取指南</b></summary>

1. 访问 [Clerk Dashboard](https://dashboard.clerk.com)
2. 创建新应用或选择现有应用
3. 在 "API Keys" 页面找到 "Publishable Key"
4. 复制密钥（格式：`pk_test_...` 或 `pk_live_...`）
5. 将密钥填入 `client/.env` 的 `VITE_CLERK_PUBLISHABLE_KEY`

**配置建议：**
- 开发环境使用 `pk_test_` 密钥
- 生产环境使用 `pk_live_` 密钥
- 启用 Email 和 Social Login 提升用户体验
</details>

---

## 🎨 核心功能详解

### 1. 项目管理

[项目管理界面截图占位 - 建议尺寸: 1200x800px, 展示项目列表、统计数据、筛选功能]

**功能亮点：**
- 📂 多项目管理，每个项目独立数据空间
- 📊 实时统计：总字数、章节数、角色数、完成度
- 🏷️ 项目分类和标签系统
- 🔍 快速搜索和筛选
- 📈 写作进度可视化

### 2. 角色管理系统

[角色管理界面截图占位 - 建议尺寸: 1200x800px, 展示角色卡片、详情面板、关系图谱]

**功能亮点：**
- 👤 详细角色档案：外貌、性格、背景、能力
- 🕸️ 角色关系网络可视化
- 📝 角色成长轨迹记录
- 🤖 AI 辅助生成角色建议
- 🔗 章节引用追踪

**角色属性模板：**
```
基本信息：姓名、年龄、性别、种族、职业
外貌特征：身高、体型、发色、眼色、标志性特征
性格特点：MBTI、核心性格、优点、缺点、恐惧
背景故事：出身、经历、转折点、动机、目标
能力系统：技能、特殊能力、装备、战力评估
社交关系：亲人、朋友、敌人、情感关系
```

### 3. 世界设定管理

[世界设定界面截图占位 - 建议尺寸: 1200x800px, 展示设定分类、详情编辑、关联标签]

**功能亮点：**
- 🌍 分类管理：地理、历史、文化、规则、组织、科技等
- 🗺️ 地点详情：描述、地图、相关事件
- ⚖️ 规则系统：魔法体系、修炼等级、社会制度
- 📅 时间线管理：历史事件、重大节点
- 🔗 设定关联和引用追踪

### 4. 智能章节编辑器

[编辑器界面截图占位 - 建议尺寸: 1400x900px, 展示Monaco编辑器、多标签、工具栏]

**功能亮点：**
- ✨ 专业编辑器：基于 Monaco Editor，提供代码级编辑体验
- 📑 多标签管理：同时打开多个章节，快速切换
- 💾 自动保存：实时保存草稿，永不丢失内容
- 📊 实时统计：字数、段落数、预计阅读时间
- 🎯 大纲模式：章节大纲、情节点、伏笔管理
- ⌨️ 快捷键支持：提升编辑效率

**编辑器快捷键：**
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+S` | 保存章节 |
| `Ctrl+F` | 查找 |
| `Ctrl+H` | 替换 |
| `Ctrl+/` | 切换注释 |
| `Ctrl+K Ctrl+F` | 格式化文本 |
| `Alt+↑/↓` | 移动行 |

### 5. AI 智能助手面板

[AI助手界面截图占位 - 建议尺寸: 800x1000px, 展示对话模式、增强模式、检查模式]

#### 5.1 对话模式

与 AI 进行创作讨论，获取灵感和建议。

**使用场景：**
- 💭 讨论情节发展方向
- 🎭 探讨角色性格和动机
- 🌈 头脑风暴创意点子
- ❓ 咨询写作技巧和建议

**示例对话：**
```
作者: 主角在这一章遇到了背叛，我该如何处理他的情绪反应？
AI: 考虑到主角之前建立的信任和性格特点，可以从以下几个方向展开...
```

#### 5.2 内容增强模式

选中文本，使用 AI 进行智能改写和优化。

**增强功能：**
- 📝 **文本润色**：优化语句流畅度和文采
- 📖 **内容扩写**：补充细节和场景描写
- 🎯 **重点提炼**：压缩冗余，突出核心
- 🎨 **风格转换**：改变叙述风格和语气
- 🌟 **创意增强**：添加修辞和意象

**操作流程：**
1. 在编辑器中选中需要优化的文本
2. 打开 AI 助手面板，切换到"增强"模式
3. 选择增强类型（润色/扩写/提炼/转换）
4. AI 生成建议版本
5. 一键应用或继续调整

#### 5.3 一致性检查模式

AI 自动扫描全文，检测并提示矛盾之处。

**检查项目：**
- 👤 角色一致性：性格前后矛盾、能力设定冲突
- 🌍 设定一致性：世界观规则违背、地理描述矛盾
- 📖 情节一致性：时间线错乱、因果逻辑问题
- 🗣️ 对话一致性：称呼错误、信息泄露
- 📅 时间一致性：日期计算错误、季节混乱

**检查报告示例：**
```
⚠️ 发现 3 处潜在问题：

1. 角色矛盾 (第12章 vs 第18章)
   - 张三在第12章提到从未去过北方
   - 第18章回忆中却出现在北方城市的场景
   建议：调整第12章表述或删除第18章相关回忆

2. 时间线问题 (第5章)
   - 故事发生在冬季，却出现荷花盛开的描写
   建议：修改季节或更换景物描写

3. 设定冲突 (第22章)
   - 违反了第3章建立的魔法规则：禁咒需要24小时准备
   建议：增加准备时间描写或调整规则设定
```

### 6. 多格式导出

[导出界面截图占位 - 建议尺寸: 800x600px, 展示导出选项、格式选择、预览]

**支持格式：**
- 📱 **EPUB**：电子书标准格式，支持封面、目录、元数据
- 📄 **TXT**：纯文本格式，保留章节结构
- 📋 **Markdown**：保留格式标记，便于后续编辑
- 🌐 **HTML**：网页格式，适合在线阅读

**导出配置：**
```
✅ 包含元数据（标题、作者、简介）
✅ 生成目录导航
✅ 嵌入封面图片
✅ 保留章节层级
✅ 自定义字体和排版
```

---

## 🎓 使用教程

### 完整创作流程示例

#### 第一步：创建新项目

```
1. 点击"新建项目"按钮
2. 填写项目信息：
   - 小说标题：《星际迷航：未知领域》
   - 类型：科幻小说
   - 简介：一群星际探险家的冒险故事...
   - 目标字数：200,000
3. 点击"创建"
```

#### 第二步：构建角色库

```
1. 进入"角色管理"
2. 创建主角：
   - 姓名：艾琳·科尔
   - 性格：理性、果断、富有同情心
   - 背景：前军官，现探险队长
   - 使用 AI 助手生成更多背景细节
3. 创建配角和反派
4. 建立角色关系网
```

#### 第三步：设定世界观

```
1. 进入"世界设定"
2. 添加地理设定：
   - 主要星球：泰拉星、诺瓦星
   - 空间站：曙光站
3. 添加规则设定：
   - 超光速航行原理
   - 外星种族特征
4. 添加组织设定：
   - 星际联盟
   - 探险者协会
```

#### 第四步：规划章节大纲

```
1. 进入"章节编辑器"
2. 创建章节：
   - 第一章：启程
   - 大纲：艾琳接受任务，组建队伍，准备出发
   - 情节点：遇到老朋友、发现线索、意外事件
3. 使用 AI 对话模式讨论情节发展
```

#### 第五步：开始创作

```
1. 打开第一章编辑器
2. 根据大纲开始写作
3. 遇到困难时：
   - 使用 AI 对话模式寻求建议
   - 使用增强模式润色段落
4. 定期保存（自动保存已启用）
```

#### 第六步：一致性检查

```
1. 完成若干章节后，运行一致性检查
2. 查看 AI 生成的检查报告
3. 逐项修复发现的问题
4. 重新检查确认
```

#### 第七步：导出成品

```
1. 进入"导出"功能
2. 选择格式：EPUB
3. 配置封面和元数据
4. 点击"导出"
5. 下载生成的电子书文件
```

### 最佳实践建议

#### ✅ 推荐做法

1. **先规划后创作**：先完善角色和世界观，再开始写作正文
2. **定期检查**：每完成 5-10 章就运行一次一致性检查
3. **善用大纲**：在编辑器中使用大纲功能规划章节结构
4. **AI 辅助而非替代**：将 AI 建议作为参考，保持自己的创作风格
5. **备份数据**：定期导出项目数据备份

#### ❌ 避免做法

1. **过度依赖 AI**：不要让 AI 直接生成大段内容
2. **忽略一致性**：不要等全书完成才检查矛盾
3. **频繁切换模式**：专注于当前创作任务
4. **忽略元数据**：角色和设定要及时记录，避免遗忘

---

## 🔧 进阶配置

### 数据库迁移到 PostgreSQL

生产环境推荐使用 PostgreSQL 替代 SQLite。

#### 使用 Supabase (推荐)

Supabase 提供免费的 PostgreSQL 数据库托管。

```bash
# 1. 访问 https://supabase.com 创建项目
# 2. 获取数据库连接字符串

# 3. 更新环境变量
# server/.env
DATABASE_URL="postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres"

# 4. 应用数据库 Schema
cd server
npx prisma generate
npx prisma db push

# 5. 测试连接
node test-db-connection.js
```

#### 使用本地 PostgreSQL

```bash
# 1. 使用 Docker 启动本地 PostgreSQL
docker compose -f docker-compose.postgres.yml up -d postgres

# 2. 配置连接字符串
DATABASE_URL="postgresql://noveluser:changeme@localhost:5432/novel_db"

# 3. 应用迁移
npm run db:push

# 4. (可选) 迁移 SQLite 数据
node scripts/migrate-sqlite-to-postgres.js
```

### 自定义 AI 提示词

修改 AI 助手的行为和风格。

#### 配置文件位置

```
server/config/ai-prompts.js
```

#### 自定义对话模式提示词

```javascript
// server/config/ai-prompts.js
module.exports = {
  dialogue: {
    systemPrompt: `你是一位经验丰富的小说创作顾问。
    你的职责是帮助作者思考情节、角色、世界观等创作问题。

    请遵循以下原则：
    - 提供建议而非直接创作内容
    - 鼓励作者发挥自己的创意
    - 提出开放式问题引导思考
    - 考虑作品的整体一致性

    当前项目信息：
    - 小说类型：{genre}
    - 目标读者：{audience}
    - 已有角色：{characters}
    - 世界观设定：{worldSettings}`,
  },

  enhancement: {
    polish: `优化以下文本的语言表达，使其更流畅、更有文采，但保持原意不变...`,
    expand: `扩展以下文本，补充细节描写、场景氛围、人物动作等...`,
    condense: `精简以下文本，保留核心信息，删除冗余内容...`,
  },

  consistency: {
    systemPrompt: `分析以下内容，检测是否存在矛盾...`,
  }
};
```

### 集成其他 AI 模型

项目支持集成多种 AI 服务。

#### 添加 Claude API 支持

```javascript
// server/services/aiService.js

const Anthropic = require('@anthropic-ai/sdk');

const anthropic = new Anthropic({
  apiKey: process.env.CLAUDE_API_KEY,
});

async function chatWithClaude(messages) {
  const response = await anthropic.messages.create({
    model: 'claude-3-5-sonnet-20241022',
    max_tokens: 1024,
    messages: messages,
  });

  return response.content[0].text;
}
```

#### 配置模型切换

```bash
# server/.env
AI_PROVIDER=openai  # openai | claude | azure | custom
OPENAI_API_KEY=sk-...
CLAUDE_API_KEY=sk-ant-...
```

### 自定义主题和样式

修改客户端界面样式。

#### Tailwind 配置

```javascript
// client/tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          // ... 自定义主色调
          900: '#0c4a6e',
        },
      },
    },
  },
};
```

#### 全局样式变量

```css
/* client/src/assets/base.css */
:root {
  --color-background: #ffffff;
  --color-text: #213547;
  --sidebar-width: 280px;
  --header-height: 64px;
  /* 自定义 CSS 变量 */
}
```

---

## 🚢 部署指南

### 部署到 Railway

Railway 提供简单的全栈应用部署。

```bash
# 1. 安装 Railway CLI
npm install -g @railway/cli

# 2. 登录 Railway
railway login

# 3. 初始化项目
railway init

# 4. 添加环境变量
railway variables set OPENAI_API_KEY=sk-...
railway variables set DATABASE_URL=postgresql://...

# 5. 部署
railway up
```

### 部署到 Render

Render 提供免费的 Web 服务托管。

#### 配置文件

```yaml
# render.yaml
services:
  - type: web
    name: ai-novel-assistant
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production
      - key: OPENAI_API_KEY
        sync: false
      - key: DATABASE_URL
        sync: false
```

#### 部署步骤

```bash
# 1. 连接 GitHub 仓库到 Render
# 2. 创建新的 Web Service
# 3. 选择仓库和分支
# 4. 配置环境变量
# 5. 点击 "Create Web Service"
```

### 使用 Docker 部署

#### 构建镜像

```bash
# 构建生产镜像
docker build -t ai-novel-assistant:latest .

# 运行容器
docker run -d \
  -p 3000:3000 \
  -p 3001:3001 \
  -e OPENAI_API_KEY=sk-... \
  -e DATABASE_URL=postgresql://... \
  -v /data/novels:/app/server/prisma \
  --name ai-novel-assistant \
  ai-novel-assistant:latest
```

#### Docker Compose 生产配置

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
      - "3001:3001"
    environment:
      NODE_ENV: production
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      DATABASE_URL: ${DATABASE_URL}
    volumes:
      - novel-data:/app/server/prisma
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: noveluser
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: novel_db
    volumes:
      - postgres-data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  novel-data:
  postgres-data:
```

### Nginx 反向代理配置

```nginx
# /etc/nginx/sites-available/ai-novel-assistant
server {
    listen 80;
    server_name your-domain.com;

    # 前端
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # 后端 API
    location /api {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket 支持
    location /ws {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }
}
```

---

## 🤝 参与贡献

我们欢迎所有形式的贡献！

### 贡献方式

- 🐛 **报告 Bug**：[提交 Issue](https://github.com/stevendong/ai-novel-assistant/issues/new?template=bug_report.md)
- 💡 **功能建议**：[提交 Feature Request](https://github.com/stevendong/ai-novel-assistant/issues/new?template=feature_request.md)
- 📖 **改进文档**：修正错误、补充说明、翻译文档
- 💻 **贡献代码**：修复 Bug、开发新功能

### 开发流程

```bash
# 1. Fork 本仓库
# 2. 克隆你的 Fork
git clone https://github.com/stevendong/ai-novel-assistant.git
cd ai-novel-assistant

# 3. 创建功能分支
git checkout -b feature/amazing-feature

# 4. 进行开发
# 请遵循项目代码规范（见 CLAUDE.md）

# 5. 提交更改
git add .
git commit -m "feat: add amazing feature"

# 6. 推送到你的 Fork
git push origin feature/amazing-feature

# 7. 创建 Pull Request
# 访问 GitHub 页面，点击 "New Pull Request"
```

### 代码规范

在提交 PR 之前，请确保：

- ✅ 代码通过 TypeScript 类型检查
- ✅ 遵循 ESLint 规则（如已配置）
- ✅ 添加必要的注释说明
- ✅ 更新相关文档
- ✅ 测试功能正常工作
- ✅ Commit 信息遵循约定（见下方）

### Commit 信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
feat: 添加新功能
fix: 修复 Bug
docs: 文档更新
style: 代码格式调整（不影响功能）
refactor: 代码重构
test: 添加测试
chore: 构建配置或辅助工具变更
```

示例：
```bash
git commit -m "feat: add character relationship visualization"
git commit -m "fix: resolve chapter auto-save issue"
git commit -m "docs: update deployment guide"
```

### 开发环境设置

详细的开发指南请参考：
- `[CLAUDE.md](./CLAUDE.md)` - Claude Code 开发指南
- `[MONOREPO.md](./MONOREPO.md)` - Monorepo 架构说明

---

## 📅 开发路线图

### 🎯 当前版本 (v1.0.0)

- [x] 核心项目管理功能
- [x] 角色和世界设定系统
- [x] 章节编辑器（Monaco Editor）
- [x] AI 对话、增强、检查模式
- [x] EPUB/TXT 导出功能
- [x] 统一认证系统（Clerk + JWT）
- [x] 基础权限管理

### 🚀 下一版本 (v1.1.0) - 计划中

- [ ] **版本控制系统**
  - 章节历史版本管理
  - 差异对比和回滚功能
  - 多版本分支支持

- [ ] **协作功能**
  - 多人实时协作编辑
  - 评论和批注系统
  - 团队权限管理

- [ ] **智能分析**
  - 写作风格分析
  - 可读性评分
  - 情感曲线可视化

- [ ] **移动端支持**
  - 响应式界面优化
  - 移动端专用编辑器
  - PWA 支持

### 🔮 未来规划 (v2.0.0+)

- [ ] **多 AI 模型支持**
  - Claude、Gemini、国产大模型集成
  - 自定义模型切换
  - 本地模型部署支持

- [ ] **高级导出功能**
  - PDF 带格式导出
  - Word DOCX 格式
  - 自定义模板系统
  - 出版社格式预设

- [ ] **插件系统**
  - 开放插件 API
  - 社区插件市场
  - 自定义 AI 提示词插件

- [ ] **桌面应用**
  - Electron 打包
  - 离线模式支持
  - 本地 AI 模型集成

- [ ] **数据分析**
  - 写作习惯分析
  - 生产力统计
  - 创作热力图

- [ ] **社区功能**
  - 作品分享平台
  - 社区评论和点赞
  - 创作教程和模板库

### 💬 需求征集

欢迎在 [Discussions](https://github.com/stevendong/ai-novel-assistant/discussions) 中提出你的功能需求和建议！

---

## ⚠️ 免责声明

1. **AI 生成内容**：本工具使用第三方 AI 服务（OpenAI 等），生成的内容质量和准确性由 AI 服务提供商负责。请勿完全依赖 AI 生成的内容，务必进行人工审核。

2. **数据隐私**：
   - 使用云端 AI 服务时，你的小说内容会被发送到 AI 服务提供商的服务器
   - 请勿在小说中包含真实的个人敏感信息
   - 建议使用自托管部署以获得更好的隐私保护

3. **版权声明**：
   - 使用本工具创作的小说版权归作者本人所有
   - AI 辅助生成的内容可能存在版权争议，请谨慎使用
   - 禁止使用本工具创作侵权内容

4. **服务可用性**：
   - 本项目依赖第三方 AI 服务，可能因服务商原因导致功能不可用
   - 请定期备份你的小说数据
   - 开发者不对数据丢失承担责任

5. **使用限制**：
   - 请遵守当地法律法规
   - 禁止使用本工具创作违法违规内容
   - AI API 调用会产生费用，请注意成本控制

---

## 📄 开源许可

本项目采用 `[MIT License](LICENSE)` 开源协议。

```
MIT License

Copyright (c) 2025 AI Novel Assistant Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 致谢

### 技术栈

感谢以下开源项目和服务：

- [Vue.js](https://vuejs.org/) - 渐进式 JavaScript 框架
- [Ant Design Vue](https://antdv.com/) - 企业级 UI 组件库
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - 强大的代码编辑器
- [Prisma](https://www.prisma.io/) - 现代 TypeScript ORM
- [Tailwind CSS](https://tailwindcss.com/) - 实用优先的 CSS 框架

### 贡献者

感谢所有为本项目做出贡献的开发者！

[贡献者头像墙占位 - 使用 GitHub Contributors 自动生成]

<a href="https://github.com/stevendong/ai-novel-assistant/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=stevendong/ai-novel-assistant" />
</a>

### 赞助商

[赞助商 Logo 占位区域]

如果这个项目帮助到了你，欢迎[赞助支持](https://github.com/sponsors/stevendong)项目发展！

---

## 📞 联系我们

- 📧 **Email**: support@ai-novel-assistant.com
- 💬 **Discussions**: [GitHub Discussions](https://github.com/stevendong/ai-novel-assistant/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/stevendong/ai-novel-assistant/issues)
- 📱 **社交媒体**: [Twitter](https://twitter.com/yourhandle) | [知乎](#)

---

## 📊 项目统计

![GitHub Stars](https://img.shields.io/github/stars/stevendong/ai-novel-assistant?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/stevendong/ai-novel-assistant?style=for-the-badge)
![GitHub Issues](https://img.shields.io/github/issues/stevendong/ai-novel-assistant?style=for-the-badge)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/stevendong/ai-novel-assistant?style=for-the-badge)
![GitHub Last Commit](https://img.shields.io/github/last-commit/stevendong/ai-novel-assistant?style=for-the-badge)
![GitHub Contributors](https://img.shields.io/github/contributors/stevendong/ai-novel-assistant?style=for-the-badge)

related:
  - methods/QUICK_START.md
---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！⭐**

Made with ❤️ by the AI Novel Assistant Team

[回到顶部](#ai-novel-assistant)

</div>
