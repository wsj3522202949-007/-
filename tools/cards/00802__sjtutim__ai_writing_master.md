---
id: tool-00802
type: tool
area: 库
status: active
tags: [RAG, Vue, 协议未明, 需API密钥, 中文友好, 人物设定]
title: ai_writing_master
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/sjtutim/ai_writing_master
created: 2026-07-18
updated: 2026-07-18
no: 802
category: 二、网文 / 长篇 AI 写作系统 库
repo: sjtutim/ai_writing_master
stars: 16
url: https://github.com/sjtutim/ai_writing_master
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 21084e383d932228
  - methods/最强写作方法论_全球最强综合版.md
---

# sjtutim/ai_writing_master

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sjtutim/ai_writing_master
- **Stars**：16
- **语言**：Vue
- **License**：None
- **Topics**：—
- **GitHub 描述**：AWM is a TypeScript RAG writing system with Nuxt 3 frontend, Express backend, pgvector search, and MinIO storage. It ingests Word/text to Markdown, chunks and embeds with bge-m3, and streams grounded generations using chosen prompts, styles, and scoped collections. Outputs stay auditable with metadata and RBAC.
- **本地描述**：AWM is a TypeScript RAG writing system with Nuxt 3 frontend, Express backend, pgvector search, and MinIO storage. It ingests Word/text to Markdown, chunks and embeds with bge-m3, and streams grounded generations using chosen prompts, styles, and scoped collections. Outputs stay auditable with metadata and RBAC.
- **拉取时间**：2026-07-23 23:02:25

---

# AI4Write

<div align="center">

![AI4Write](https://img.shields.io/badge/AI4Write-Local%20RAG%20Writing%20System-blue?style=for-the-badge)
![Vue 3](https://img.shields.io/badge/Vue-3.4-42b883?style=flat-square&logo=vue.js)
![Nuxt 3](https://img.shields.io/badge/Nuxt-3.11-00DC82?style=flat-square&logo=nuxt.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-3178c6?style=flat-square&logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38bdf8?style=flat-square&logo=tailwindcss)

**基于 RAG 技术的本地化智能写作系统**

[English](https://github.com/sjtutim/ai_writing_master/blob/main/README_EN.md) | 简体中文

![AI4Write Demo](demo.png)

</div>

---

## ✨ 特性

- **📚 知识库管理** - 支持 Word/TXT/Markdown/PDF 文档上传，自动转换为 Markdown 并进行向量化存储
- **✍️ 智能写作** - 基于知识库的上下文，调用大语言模型生成高质量内容
- **🎨 模板风格** - 支持自定义提示词模板和写作风格，灵活控制生成效果
- **🔒 本地部署** - 完全本地化运行，数据安全可控
- **👥 多用户支持** - 基于角色的访问控制 (RBAC)，支持团队协作

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────────────┐
│                        前端 (Nuxt 3)                             │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌─────────────┐   │
│  │  Pinia    │  │ Tailwind  │  │  Vue 3    │  │  Components │   │
│  └───────────┘  └───────────┘  └───────────┘  └─────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       后端 (Express + TypeScript)                │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌─────────────┐   │
│  │  Prisma   │  │  JWT Auth │  │  Jobs     │  │  API Routes │   │
│  └───────────┘  └───────────┘  └───────────┘  └─────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┼──────────────────┐
         ▼                    ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────────┐    ┌──────────────┐    ┌──────────────┐
│   PostgreSQL │    │      MinIO       │    │  bge-m3 API  │    │    Redis     │
│  (pgvector)  │    │   文件存储       │    │   向量化     │    │   缓存服务   │
└──────────────┘    └──────────────────┘    └──────────────┘    └──────────────┘
```

### 核心技术栈

| 层级 | 技术选型 |
|------|----------|
| 前端框架 | Nuxt 3 + Vue 3 (Composition API) |
| 状态管理 | Pinia |
| UI 样式 | Tailwind CSS |
| 后端框架 | Express + TypeScript |
| 数据库 ORM | Prisma |
| 向量数据库 | PostgreSQL + pgvector |
| 缓存服务 | Redis |
| 对象存储 | MinIO |
| 文本嵌入 | BGE-M3 |
| 大语言模型 | DeepSeek (OpenAI 兼容 API) |

## 🚀 快速开始

### 前置要求

- Node.js >= 18
- PostgreSQL >= 14 (需启用 pgvector 扩展)
- MinIO (对象存储)
- Redis (缓存服务)
- DeepSeek API Key (可选，用于本地部署)

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/yourusername/ai4write.git
cd ai4write
```

2. **安装依赖**

```bash
# 安装前端依赖
cd frontend && npm install

# 安装后端依赖
cd ../backend && npm install
```

3. **配置环境变量**

```bash
# 后端配置
cp backend/.env.example backend/.env
# 编辑 .env 文件，配置数据库连接、MinIO、API Key 等
```

4. **初始化数据库**

```bash
cd backend
npx prisma generate
npx prisma db push
npm run seed  # 可选：初始化测试数据
```

5. **启动服务**

```bash
# 启动后端 (端口 3001)
npm run dev:backend

# 新终端中启动前端 (端口 3007)
cd frontend && npm run dev:frontend
```

6. **访问应用**

打开浏览器访问 http://localhost:3007

### 默认账号

| 邮箱 | 密码 | 角色 |
|------|------|------|
| admin@ai4write.local | admin123 | 管理员 |
| test@ai4write.local | user123 | 普通用户 |

## 📁 项目结构

```
ai4write/
├── frontend/                 # Nuxt 3 前端项目
│   ├── assets/css/          # 全局样式
│   ├── components/          # Vue 组件
│   ├── layouts/            # 页面布局
│   ├── pages/              # 页面路由
│   ├── stores/             # Pinia 状态管理
│   ├── composables/        # 组合式函数
│   └── nuxt.config.ts      # Nuxt 配置
│
├── backend/                 # Express 后端项目
│   ├── src/
│   │   ├── controllers/    # 控制器
│   │   ├── routes/         # API 路由
│   │   ├── services/       # 业务逻辑
│   │   ├── middleware/     # 中间件
│   │   └── prisma/         # Prisma Schema
│   └── prisma/             # 数据库迁移
│
└── README.md               # 项目文档
```

## 🔧 配置说明

### Docker 部署

使用 Docker Compose 一键部署（包含 Nginx 反向代理）：

```bash
# 进入 docker 目录
cd docker

# 复制并配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库连接、MinIO、API Key 等

# 构建并启动所有服务
docker-compose up -d --build

# 查看日志
docker-compose logs -f
```

部署完成后，通过 `http://YOUR_DOMAIN:8089` 访问应用。

#### 架构说明

```
                    ┌─────────────────┐
                    │     Nginx       │
                    │   (端口 8089)   │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
    ┌─────────────────┐          ┌─────────────────┐
    │    Frontend     │          │     Backend     │
    │  (Nuxt 3:3000)  │          │ (Express:3001)  │
    └─────────────────┘          └─────────────────┘
```

- **Nginx** - 统一入口，反向代理前后端服务
  - `/` → 前端 (Nuxt 3)
  - `/api/*` → 后端 API (Express)
- **Frontend** - Nuxt 3 SSR 应用
- **Backend** - Express API 服务

> **注意**: 当前 Docker 配置假设 PostgreSQL、MinIO、Redis 等基础设施已在外部运行或单独部署。

### 环境变量配置

在 `docker` 目录下创建 `.env` 文件：

```env
# Node 环境
NODE_ENV=production

# ===========================================
# 对外服务端口
# ===========================================
PROXY_PORT=8089            # Nginx 代理端口（统一入口）

# ===========================================
# PostgreSQL (外部服务)
# ===========================================
POSTGRES_HOST=your-db-host
POSTGRES_PORT=5432
POSTGRES_USER=ai4write
POSTGRES_PASSWORD=your_password
POSTGRES_DB=ai4write

# ===========================================
# MinIO (对象存储)
# ===========================================
MINIO_ENDPOINT=your-minio-host
MINIO_PORT=9000
MINIO_USE_SSL=false
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=ai4write

# ===========================================
# Redis (外部服务)
# ===========================================
REDIS_HOST=your-redis-host
REDIS_PORT=6379
REDIS_URL=redis://:password@your-redis-host:6379/0

# ===========================================
# Embedding API (向量化服务)
# ===========================================
EMBEDDING_API_URL=http://your-embedding-host:8000/v1/embeddings
EMBEDDING_MODEL=text-embedding-bge-m3

# ===========================================
# DeepSeek/LLM API
# ===========================================
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_API_KEY=sk-xxx
DEEPSEEK_MODEL=deepseek-chat

# ===========================================
# JWT 配置
# ===========================================
JWT_SECRET=your-super-secret-jwt-key
JWT_EXPIRES_IN=7d

# ===========================================
# 前端 API 地址
# ===========================================
# 使用 Nginx 反向代理时，设置为空或相对路径
NUXT_PUBLIC_API_BASE_URL=
```

## 📖 使用指南

### 1. 创建知识库

1. 访问「知识库」页面
2. 点击「新建知识库」创建分类
3. 上传 Word/TXT/Markdown/PDF 文档或直接粘贴文本
4. 系统自动解析、向量化并存储

### 2. 开始写作

1. 访问「写作工作台」
2. 选择提示词模板 (可选)
3. 输入写作要求
4. 选择单一知识库 (可选)
5. 选择写作风格 (可选)
6. 点击「开始生成」

### 3. 管理模板

在「写作工作台」中切换到「模板管理」或「风格管理」标签页，可以：

- 创建/编辑/删除提示词模板
- 管理写作风格范文
- 设置分类组织模板

## 🛠️ 开发指南

### 添加新功能

```bash
# 1. 后端新增 API
backend/src/routes/api.ts     # 添加路由
backend/src/services/user.ts  # 添加业务逻辑

# 2. 前端新增页面
frontend/pages/admin.vue      # 新建页面
frontend/components/MyComponent.vue  # 新建组件
```

### 数据库迁移

```bash
# 创建迁移
npx prisma migrate dev --name add_user_field

# 执行迁移
npx prisma migrate deploy
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目基于 MIT 许可证开源，详见 [LICENSE](https://github.com/sjtutim/ai_writing_master/blob/main/LICENSE) 文件。

## 🙏 感谢

- [Nuxt.js](https://nuxt.com/) - Vue.js 框架
- [Tailwind CSS](https://tailwindcss.com/) - CSS 框架
- [DeepSeek](https://deepseek.com/) - 大语言模型
- [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) - 向量模型

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

**如果本项目对你有帮助，欢迎 ⭐ Star 支持！**

</div>
