---
id: tool-01515
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Writer-s-Agent-Editor
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dry-bread/writer-s-agent-editor
created: 2026-07-18
updated: 2026-07-18
no: 1515
category: 二、网文 / 长篇 AI 写作系统 库
repo: dry-bread/Writer-s-Agent-Editor
stars: 0
url: https://github.com/dry-bread/writer-s-agent-editor
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# dry-bread/Writer-s-Agent-Editor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dry-bread/writer-s-agent-editor
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An IDE-like AI agent for document editing. Edit documents in-place with structure-aware, diff-based patches. Supports paragraphs, headings, lists, and tables with controllable changes, previews, and undo—bringing Copilot-style workflows to writing.
- **本地描述**：An IDE-like AI agent for document editing. Edit documents in-place with structure-aware, diff-based patches. Supports paragraphs, headings, lists, and tables with controllable changes, previews, and undo—bringing Copilot-style workflows to writing.
- **拉取时间**：2026-07-23 23:23:17

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Writer's Agent Editor

Writer's Agent Editor 是一个支持 AI 辅助的富文本编辑器，专为创作公众号文章而设计。通过"就地编辑"和"结构化操作"，结合多个大语言模型，提升写作效率。

## 📖 文档

- **[需求文档](./REQUIREMENTS.md)** - 产品需求和功能规划
- **[架构设计](./ARCHITECTURE.md)** - 系统整体架构
- **[前端开发规范](./frontend/FRONTEND_ARCHITECTURE.md)** ⭐ - 前端代码组织和设计规范（**必读**）

## 🏗️ 前端架构

本项目采用 **Feature-based + 三层架构** 设计：

```
frontend/src/
├── features/              # 按功能模块组织
│   ├── editor/            # 编辑器功能
│   │   ├── components/    # UI 组件
│   │   ├── viewmodel/     # 状态管理 (RxJS)
│   │   └── services/      # 业务逻辑
│   └── chat/              # 聊天功能
│       ├── components/
│       ├── viewmodel/
│       └── services/
└── shared/                # 共享代码
    ├── base/              # BaseViewModel, BaseService
    ├── hooks/             # useObservable
    └── types/
```

**关键设计**：
- **Components** - 纯 UI，使用 ViewModel
- **ViewModel** - RxJS 响应式状态管理
- **Services** - API 调用和业务逻辑

详细规范请查看 [前端开发规范](./frontend/FRONTEND_ARCHITECTURE.md)。

## 🚀 快速开始

```bash
# 安装依赖
cd frontend
npm install

# 启动开发服务器
npm run dev
```
