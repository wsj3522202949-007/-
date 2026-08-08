---
id: tool-01864
type: tool
area: 库
status: active
tags: [RAG, 大纲规划, Vue, 协议未明, 本地优先, 中文友好, 人物设定, 本地写作]
title: Novel-Writing-Tool
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/gtz2187/novel-writing-tool
created: 2026-07-18
updated: 2026-07-18
no: 1864
category: 二、网文 / 长篇 AI 写作系统 库
repo: gtz2187/Novel-Writing-Tool
stars: 0
url: https://github.com/gtz2187/novel-writing-tool
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9c12823a2e4c435a
  - methods/最强写作方法论_全球最强综合版.md
---

# gtz2187/Novel-Writing-Tool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gtz2187/novel-writing-tool
- **Stars**：0
- **语言**：Vue
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：gtz2187/Novel-Writing-Tool
- **拉取时间**：2026-07-23 23:33:20

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 墨者 MoZhe

墨者是一个本地优先的小说创作桌面工作台。项目使用 Electron 承载桌面窗口，Vue 3 负责渲染进程，NestJS 提供本地 API，所有创作数据默认保存到本机文件系统中。

当前版本重点搭好了核心创作链路：项目管理、富文本正文写作、大纲、人物、世界观、时间线、伏笔、灵感便签、项目设置、快照备份，以及本地 AI 占位接口。

## 功能概览

- 项目列表：新建、打开、复制、删除项目，并可选择项目存储目录。
- 工作台总览：展示连续写作天数、今日目标、最近章节、章节进度、待办和灵感碎片。
- 正文编辑器：基于 Tiptap/ProseMirror，支持富文本写作、预览、基础格式、查找替换、自动保存、专注模式。
- 正文联动：正文中识别人物、地点/世界观、伏笔、时间线事件和大纲节点，以淡标记和右侧上下文面板呈现。
- 章节关联：可从选中文本快速创建并绑定人物、地点/设定、伏笔和时间线事件。
- 大纲系统：维护卷、章、节树状结构，可编辑状态、目标字数、摘要，并从大纲进入或创建正文。
- 人物库：维护人物基础资料、性格标签、阵营、背景、人际关系，并提供一度关系图。
- 世界观词条：维护名称、别名、分类、摘要、正文、标签和词条关联。
- 时间线：支持多条时间线、事件编辑、人物/地点/章节关联，以及时间轴预览。
- 伏笔管理：维护埋下章节、计划揭示章节、实际揭示章节、状态，并做基础一致性检查。
- 灵感便签板：创建和编辑彩色便签卡片。
- 设置中心：保存主题、默认项目目录、编辑器字体/字号/行高/自动保存间隔、AI 配置和音频列表。
- 项目快照：将项目元数据和各类实体文件打包为 zip 快照。
- 导出与备份：支持项目体检、快照列表/恢复、导入项目，以及 Markdown、Word、PDF、ePub 导出。
- 结构联动：自动维护人物出场统计、时间线事件章节关联，并提示孤立引用和伏笔顺序冲突。
- AI 占位能力：提供本地问答、实体提取和人物推荐接口，便于后续替换为真实大模型或 RAG。

## 技术栈

- 桌面壳：Electron 35
- 前端：Vue 3、Vue Router、Pinia、Vite
- 编辑器：Tiptap / ProseMirror
- 后端：NestJS 11、本地 HTTP API
- 数据存储：`fs-extra` 写入本地 JSON / Markdown 文件
- Markdown：`marked`
- 快照打包：`archiver`
- 语言：TypeScript

## 目录结构

```text
electron/             Electron 主进程与 preload
server/               NestJS 本地服务
server/src/projects/  项目文件读写、CRUD、快照
server/src/ai/        本地 AI 占位与推荐逻辑
shared/               前后端共享类型与默认数据
src/                  Vue 3 渲染进程
src/components/       通用组件与业务模块
src/stores/           Pinia 工作台状态
src/lib/              API 客户端与格式化工具
tests/                核心数据与导出单元测试
```

## 本地运行

```bash
npm install
npm run dev
```

`npm run dev` 会同时启动：

- Vite 渲染进程：`http://localhost:5173`
- NestJS 本地服务：`http://127.0.0.1:3777/api`
- Electron 主进程编译监听
- Electron 桌面窗口

## 常用命令

```bash
# 开发模式
npm run dev

# 构建渲染进程、服务端和 Electron 主进程
npm run build

# TypeScript 类型检查
npm run lint:types

# 核心单元测试
npm run test:unit

# 仅预览 Vite 构建产物
npm run preview

# 启动已构建的本地服务
npm run start:server
```

## 打包安装包

建议在目标系统对应环境下打包。例如要给 Windows 用户安装，优先在 Windows 上执行 `dist:win`。

```bash
npm run dist
npm run dist:win
npm run dist:mac
npm run dist:linux
```

打包结果会输出到 `dist/` 目录。常见文件包括：

- Windows：`dist/*.exe`
- macOS：`dist/*.dmg`
- Linux：`dist/*.AppImage` 或 `dist/*.deb`

## 本地数据结构

默认项目根目录为：

```text
%USERPROFILE%/Documents/MoZheProjects/
```

项目服务会在该目录下维护一个注册表文件：

```text
.mozhe-projects.json
```

每个项目会写入独立目录，结构大致如下：

```text
MoZheProjects/
└── 项目名_uuid/
    ├── project.moz.json
    ├── chapters/
    │   ├── 章节id.json
    │   └── 章节id.md
    ├── characters/
    ├── worldbuilding/
    ├── timeline/
    ├── foreshadowing/
    ├── notes/
    ├── assets/
    └── _snapshots/
```

`project.moz.json` 保存项目元信息、仪表盘、设置、大纲和各实体索引。章节会同时保存 JSON 元数据和 Markdown 正文。

## 本地 API

服务端全局前缀为 `/api`，默认监听端口为 `3777`。

主要接口：

- `GET /api/projects`：项目列表
- `POST /api/projects`：新建项目
- `GET /api/projects/:projectId`：读取项目详情
- `DELETE /api/projects/:projectId`：删除项目目录
- `POST /api/projects/:projectId/duplicate`：复制项目
- `POST /api/projects/:projectId/snapshot`：创建 zip 快照
- `GET /api/projects/:projectId/snapshots`：列出快照
- `POST /api/projects/:projectId/snapshots/:fileName/restore`：从快照恢复为新项目
- `POST /api/projects/import`：导入项目目录或 zip 快照
- `GET /api/projects/:projectId/reference-index`：读取项目引用索引
- `GET /api/projects/:projectId/validation`：读取项目体检结果
- `POST /api/projects/:projectId/export`：创建 Markdown / Word / PDF / ePub 导出
- `PUT /api/projects/:projectId/outline`：保存大纲
- `POST /api/projects/:projectId/chapters`：创建章节
- `PUT /api/projects/:projectId/chapters/:chapterId`：保存章节
- `POST /api/projects/:projectId/chapters/:chapterId/migrate-richtext`：迁移章节为富文本双轨内容
- `POST /api/projects/:projectId/chapters/:chapterId/detect-mentions`：按项目词典识别正文提及
- `PUT /api/projects/:projectId/chapters/:chapterId/mentions`：保存正文实体提及与绑定状态
- `POST /api/projects/:projectId/characters` / `PUT /api/projects/:projectId/characters/:characterId`：人物保存
- `POST /api/projects/:projectId/world` / `PUT /api/projects/:projectId/world/:entryId`：世界观词条保存
- `POST /api/projects/:projectId/timelines` / `PUT /api/projects/:projectId/timelines/:timelineId`：时间线保存
- `POST /api/projects/:projectId/foreshadowing` / `PUT /api/projects/:projectId/foreshadowing/:itemId`：伏笔保存
- `POST /api/projects/:projectId/notes` / `PUT /api/projects/:projectId/notes/:itemId`：便签保存
- `PUT /api/projects/:projectId/settings`：项目设置保存
- `POST /api/ai/ask`：本地 AI 占位问答
- `POST /api/ai/extract`：基于文本的实体提取占位
- `POST /api/ai/recommend-characters`：基于章节上下文的人物推荐

## 当前实现边界

这版已经把创作工作台的主体页面、富文本写作、正文联动、数据模型、文件持久化、结构体检、快照恢复和多格式导出搭好，但仍有一些能力是占位或基础实现：

- AI 设置可保存，但后端尚未真正调用在线模型。
- AI 问答、实体提取、人物推荐是本地启发式逻辑。
- 正文联动第一版使用确定性词典匹配，不依赖真实 AI/RAG。
- Word/ePub 导出使用服务端生成的基础文档结构；PDF 由 Electron 隐藏窗口把打印 HTML 输出为 PDF。
- RAG、向量库、复杂关系拓扑、白噪音混音、黑屋模式等还未实现。
- 当前已有核心单元测试，但还没有端到端测试。

## 开发提示

- Windows PowerShell 读取中文文件时建议显式使用 UTF-8，例如 `Get-Content -Raw -Encoding UTF8 README.md`。
- 渲染进程通过 `src/lib/api.ts` 固定访问 `http://127.0.0.1:3777/api`。
- Electron 开发模式不会主动启动内置服务，而是等待开发脚本中的 NestJS 服务；打包后主进程会从 `dist-server/server/main.js` 启动服务。
- 修改共享类型时，要同时检查前端模块、Pinia store 和 NestJS controller/service 的调用。
