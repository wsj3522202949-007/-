---
id: tool-01413
type: tool
area: 库
status: active
tags: [提示词, 大纲规划, TypeScript, 协议未明, 需API密钥, 中文友好]
title: novel_edit
summary: 搭大纲/分卷/节拍
source: https://github.com/odelialan/novel_edit
created: 2026-07-18
updated: 2026-07-18
no: 1413
category: 二、网文 / 长篇 AI 写作系统 库
repo: Odelialan/novel_edit
stars: 1
url: https://github.com/odelialan/novel_edit
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Odelialan/novel_edit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/odelialan/novel_edit
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Novel_edit is an AI-powered novel writing platform that helps you create, edit, and expand stories with intelligent tools for character design, worldbuilding, outlines, and chapter drafting—all in one place.
- **本地描述**：Novel_edit is an AI-powered novel writing platform that helps you create, edit, and expand stories with intelligent tools for character design, worldbuilding, outlines, and chapter drafting—all in one place.
- **拉取时间**：2026-07-23 23:20:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Novel Edit

Novel Edit 是面向小说作者的本地优先写作平台，包含前端编辑界面、FastAPI 后端、AI 辅助写作、角色与大纲管理、写作统计、提示词管理和长篇生成流程。

## 版本信息

- 当前版本：v3.1.0
- 发布日期：2026年7月1日
- 系统作者：OdeliaLan
- Git 仓库：https://github.com/Odelialan/novel_edit.git
- 版本定位：长篇事实状态、写作统计和编辑器稳定性升级版

## 版本3.1修改摘要

### 长篇事实状态与审计工作台

- 新增长篇事实状态服务，支持每部小说维护 `truth/` 事实文件：当前世界状态、资源账本、未闭合伏笔、支线进度、情感弧线、角色信息边界和章节事实索引。
- 长篇生成流程新增事实状态上下文，项目规划、章节设计、章节正文和一致性检查可读取结构化事实文件。
- 新增长篇工作台前端面板，可初始化、查看和编辑事实文件，并展示事实文件就绪数、审计通过数和阻断问题数。
- 章节生成提交增加审计链路：通过审计后同步章节摘要、结构化记忆、提交哈希和事实状态变更记录。

### 写作统计与版本快照

- 新增写作活动日志服务，按天记录章节字数变更、来源、章节键和净增字数。
- 新增午夜快照服务和调度器，用于生成跨日期写作统计基线，改善每日写作统计准确性。
- 新增章节文件监听服务，对外部编辑造成的章节文件变化自动建立版本快照并记录写作活动。
- 优化统计服务，支持从活动日志、午夜快照和历史版本信息合并计算每日写作数据。

### 用户与认证

- 用户存储扩展个人资料字段，支持昵称、头像、简介和更新时间。
- 前端新增个人资料弹窗，支持修改资料和密码。
- 登录态校验和用户信息刷新逻辑更新，前端可展示更完整的用户资料。

### 编辑器与写作辅助

- Markdown 富文本编辑器增强块级编辑能力，改善标题、段落、列表和代码块的编辑体验。
- 章节编辑器和版本面板更新，增强版本快照展示、恢复和外部写入后的同步体验。
- AI 侧边栏新增随机命名/素材生成面板，支持人名、地名、功法、势力、等级、门派、神祇和杂项素材生成。
- 长篇生成面板接入工作台入口，便于在生成、审计和事实状态维护之间切换。

### 配置与运行结构

- 版本号升级到 `3.1.0`。
- 后端依赖新增时区数据支持，保证 Windows 和 Linux 上 `Asia/Shanghai` 统计逻辑一致。
- `start.ps1` 更新启动和运行检查逻辑。
- `.gitignore` 明确忽略虚拟环境、依赖缓存、日志、数据库、用户运行数据、大文件资料、说明文档和测试文件；保留系统提示词与默认运行配置。

## 上传范围

本版本上传范围包括：

- 后端应用代码：`backend/app/`
- 后端运行脚本：`backend/scripts/`
- 前端应用代码：`frontend/`
- 系统提示词：`novel_repo/ai_prompts/`
- 默认全局配置：`novel_repo/global_config.json`
- 默认角色提示词配置：`novel_repo/ai_character_prompts.json`
- Docker 与环境样例：`docker-compose.yml`、`env.example`
- 启动脚本：`start.ps1`

本版本忽略范围包括：

- 虚拟环境：`venv/`、`.venv/`
- 依赖缓存：`node_modules/`、`.next/`、`__pycache__/`
- 敏感信息：`.env`、`secrets/`、`ai_keys.json`、`users.json`
- 运行数据：日志、SQLite 数据库、用户写作目标、小说正文、生成内容和用户目录
- 大文件资料：`资料/`、`backup/`
- 非发布资料：`docs/`、`backend/tests/`、`deploy/`

## 技术栈

- 后端：FastAPI、Python 3.10+、Uvicorn、Pydantic
- 前端：Next.js、React、TypeScript、Ant Design、Tailwind CSS、Monaco Editor
- 存储：本地文件系统、SQLite
- AI：OpenAI 兼容接口、Gemini、本地或自定义模型配置

## 本地运行

### 后端

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy ..\env.example ..\.env
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 前端

```powershell
cd frontend
npm install
npm run dev
```

默认前端地址为 `http://localhost:3000`，后端地址为 `http://localhost:8000`。

## 环境变量要点

- `SECRET_KEY`：生产环境必须设置，不能使用示例值。
- `ADMIN_SETUP_TOKEN`：初始化首个管理员账号时使用。
- `OPENAI_API_KEY` / `GEMINI_API_KEY`：按实际模型提供商设置。
- `NOVEL_REPO_PATH`：小说仓库路径，默认指向项目根目录下的 `novel_repo`。
- `ALLOWED_ORIGINS`：前端访问来源，多个地址用英文逗号分隔。

## Git标注

版本3.1对应 Git 标签：`v3.1.0`。
