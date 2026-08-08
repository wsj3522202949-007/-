---
id: tool-07384
type: tool
area: 库
status: active
tags: [大纲规划, TypeScript, 协议宽松, 本地优先, 中文友好, 本地写作]
title: novel-writing-agent
summary: 搭大纲/分卷/节拍
source: https://github.com/lianyichuan/novel-writing-agent
created: 2026-07-18
updated: 2026-07-18
no: 7384
category: 画龙补充 / 扩容入库 — 补充源
repo: lianyichuan/novel-writing-agent
stars: 10
url: https://github.com/lianyichuan/novel-writing-agent
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 063a40cd4de5ad95
  - methods/QUICK_START.md
---

# lianyichuan/novel-writing-agent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lianyichuan/novel-writing-agent
- **Stars**：10
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：🤖 智能小说写作管理系统 - AI-powered novel writing management system
- **本地描述**：novel-writing-agent
- **拉取时间**：2026-07-25 19:20:17

related:
  - methods/QUICK_START.md
---

# 小说写作Agent - Novel Writing Agent

🤖 一个基于AI的智能小说写作管理系统，专为长篇小说创作而设计。

## ✨ 特性

- 📝 **智能文档管理** - 统一管理作者意愿、剧情脉络、人物关系等核心文档
- 🎭 **剧情追踪系统** - 可视化监控多条主线剧情的发展进度
- 👥 **人物关系管理** - 维护复杂的人物关系网络和角色档案
- 🤖 **AI写作助手** - 集成Gemini API，支持章节大纲生成和内容创作
- 📊 **实时统计面板** - 监控写作进度、字数统计、质量评分
- 💾 **自动备份系统** - 保护您的创作成果
- 🎨 **现代化界面** - 基于Ant Design的美观用户界面

## 🛠️ 技术栈

- **前端**: React 18 + TypeScript + Ant Design + Monaco Editor
- **后端**: Node.js + Express + TypeScript
- **数据存储**: 本地文件系统 (txt文件)
- **AI集成**: OpenAI API / Claude API 支持
- **状态管理**: React Context + Hooks
- **文件监控**: Chokidar

## 📦 安装和运行

### 环境要求
- Node.js >= 16.0.0
- npm >= 8.0.0

### 快速开始

1. **克隆项目**
```bash
git clone <repository-url>
cd novel-writing-agent
```

2. **安装依赖**
```bash
npm run install:all
```

3. **配置环境变量**
```bash
# 复制环境变量模板
cp backend/.env.example backend/.env

# 编辑配置文件，添加你的API密钥
# 编辑 config/llm-config.json 配置LLM服务
```

4. **启动开发服务**
```bash
# 同时启动前后端服务
npm run dev

# 或者分别启动
npm run dev:backend  # 后端服务 (端口3001)
npm run dev:frontend # 前端服务 (端口3000)
```

5. **访问应用**
- 前端界面: http://localhost:3000
- 后端API: http://localhost:3001/api

## 📁 项目结构

```
novel-writing-agent/
├── frontend/                 # React前端
│   ├── src/
│   │   ├── components/       # 组件
│   │   │   ├── Dashboard/    # 主控制台
│   │   │   ├── DocumentEditor/ # 文档编辑器
│   │   │   ├── PlotTracker/  # 剧情追踪器
│   │   │   ├── CharacterManager/ # 人物管理器
│   │   │   └── WritingAgent/ # 写作Agent界面
│   │   ├── services/         # API服务
│   │   └── types/           # TypeScript类型定义
│   └── package.json
├── backend/                  # Node.js后端
│   ├── src/
│   │   ├── controllers/      # 控制器
│   │   ├── services/         # 业务逻辑
│   │   ├── models/          # 数据模型
│   │   ├── utils/           # 工具函数
│   │   └── routes/          # 路由
│   └── package.json
├── documents/               # 文档存储目录
│   ├── 作者意愿控制台.txt
│   ├── 主线剧情脉络.txt
│   ├── 原始人物关系.txt
│   ├── Agent执行手册.txt
│   └── chapters/           # 章节存储
├── config/                 # 配置文件
│   ├── llm-config.json     # LLM API配置
│   └── app-config.json     # 应用配置
└── package.json
```

## 🔧 配置说明

### LLM配置
编辑 `config/llm-config.json` 文件：
- 配置OpenAI或Claude API密钥
- 调整模型参数和限制
- 自定义写作提示词

### 应用配置
编辑 `config/app-config.json` 文件：
- 设置文档路径
- 调整写作参数
- 配置UI主题

## 📖 使用指南

1. **文档管理**: 在文档编辑器中维护核心设定文档
2. **剧情追踪**: 监控各条主线的发展进度
3. **人物管理**: 管理角色关系和设定
4. **AI写作**: 使用写作Agent自动生成章节内容
5. **质量控制**: 实时检查内容质量和一致性

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！
