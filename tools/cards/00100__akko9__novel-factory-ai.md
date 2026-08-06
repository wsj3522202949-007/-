---
id: tool-00100
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel-factory-ai
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/akko9/novel-factory-ai
created: 2026-07-18
updated: 2026-07-18
no: 100
category: 二、网文 / 长篇 AI 写作系统 库
repo: akko9/novel-factory-ai
stars: 1
url: https://github.com/akko9/novel-factory-ai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# akko9/novel-factory-ai

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/akko9/novel-factory-ai
- **Stars**：1
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：🧙‍♂️ AI-powered novel writing assistant. Features character planning, plot generation, and immersive writing tools. (React + TypeScript + Vite)
- **本地描述**：🧙‍♂️ AI-powered novel writing assistant. Features character planning, plot generation, and immersive writing tools. (React + TypeScript + Vite)
- **拉取时间**：2026-07-23 22:41:52

---

# 🧙‍♂️ AI 小说创作助手 (Novel Factory AI)

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![React](https://img.shields.io/badge/React-18-61DAFB.svg?logo=react) ![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6.svg?logo=typescript) ![Vite](https://img.shields.io/badge/Vite-6.0-646CFF.svg?logo=vite) ![Tailwind](https://img.shields.io/badge/Tailwind-3.0-38B2AC.svg?logo=tailwindcss)

> **从灵感到完本，AI 全程护航。**
> 
> 专为长篇小说作者打造的现代化写作工作台，融合“因果律叙事”理论与大模型能力，让创作更智能、更连贯。
>
> ---
>
> 🤖 **Vibe Coding 实践项目**：
> 本项目是 **Vibe Coding**（AI 驱动编程）的一次完整实践。**100% 的代码逻辑、UI 设计与架构决策均由 AI 辅助生成**。我们希望通过这个项目，展示 AI 在复杂业务逻辑构建中的潜力，同时也探索人机协作的新边界。

---

## ✨ 核心亮点 (Highlights)

| 🧠 **创意总监 (Planner)** | ✍️ **沉浸作家 (Writer)** |
| :--- | :--- |
| **深度策划向导**：分步构建世界观、角色与大纲 | **极简写作模式**：无干扰 UI，专注于文字本身 |
| **智能情节推演**：AI 基于因果律自动推演后续剧情 | **AI 灵感扩写**：卡文时一键润色、续写或生成初稿 |
| **卷级结构规划**：自动规划分卷节奏，长篇不崩 | **实时进度追踪**：字数统计、章节状态一目了然 |
| **动态世界观**：势力、规则、地理设定的可视化管理 | **上下文感知**：AI 写作时自动读取人设与前文摘要 |

## 🛠️ 技术架构 (Tech Stack)

本项目采用现代化的前端技术栈，确保高性能与良好的开发体验。

| 模块 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **核心框架** | ![React](https://img.shields.io/badge/-React_18-61DAFB?logo=react&logoColor=black) | 组件化开发，使用 Hooks 管理状态 |
| **构建工具** | ![Vite](https://img.shields.io/badge/-Vite-646CFF?logo=vite&logoColor=white) | 极速冷启动与热更新 |
| **开发语言** | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white) | 全局类型安全，减少运行时错误 |
| **样式方案** | ![Tailwind CSS](https://img.shields.io/badge/-Tailwind-38B2AC?logo=tailwindcss&logoColor=white) | 原子化 CSS，配合 `clsx` 灵活管理 |
| **数据存储** | ![IndexedDB](https://img.shields.io/badge/-IndexedDB-EC4D3F?logo=html5&logoColor=white) | **本地隐私优先**，无服务端依赖 |
| **UI 组件** | Lucide React + Sonner | 现代化的图标库与 Toast 通知 |
| **AI 交互** | Stream API | 支持流式响应，打字机效果 |

## 🚀 快速开始 (Quick Start)

只需三步，即可在本地启动你的 AI 写作助手。

### 1. 环境准备
确保你的电脑已安装：
*   [Node.js](https://nodejs.org/) (v18+)
*   [pnpm](https://pnpm.io/) (推荐) 或 npm
*   **LLM API Key**: 需要一个兼容 OpenAI 格式的 API Key (推荐 [DeepSeek](https://www.deepseek.com/)，性价比高且智能)。

### 2. 安装与运行

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/novel-factory-ai.git
cd novel-factory-ai

# 2. 安装依赖
pnpm install

# 3. 启动创作之旅 🚀
pnpm dev
```

浏览器访问 `http://localhost:3000` 即可开始使用。

## 📂 目录结构 (Structure)

```text
src/
├── components/
│   ├── ai/planner/    # 🎨 创意策划模块 (向导、世界观、大纲)
│   ├── ai/writer/     # ✒️ 沉浸写作模块 (编辑器、侧边栏)
│   └── ai/editor/     # 📝 智能润色模块
├── contexts/          # 🌍 全局状态 (小说数据、设置)
├── lib/               # 🔧 核心工具 (LLM 封装、DB 操作)
└── hooks/             # 🎣 自定义 Hooks
```

## 🤝 贡献与致谢 (Contributing & Credits)
### ⚠️ 现状与展望
本项目目前处于 **早期验证阶段 (Alpha)**，虽然核心流程已跑通，但仍存在诸多缺陷：
- 交互细节尚显粗糙，部分 UI 响应不够丝滑。
- AI 生成的长文一致性仍需进一步调优。
- 移动端适配尚未开始。

**我们需要你的帮助！** 无论你是擅长 React 的前端大佬，还是精通 Prompt Engineering 的炼丹师，亦或是热爱网文的作者，都欢迎提交 Issue 或 PR，一起完善这个工具。

### ❤️ 特别致谢
本项目在开发过程中，得到了 **[Trae](https://trae.ai/)** IDE 的强力支持。作为下一代 AI 原生编辑器，Trae 展现了惊人的上下文理解与代码生成能力，让本次 "Vibe Coding" 之旅变得异常顺滑。

欢迎提交 Issue 反馈 Bug，或提交 Pull Request 贡献代码。让我们一起打造最懂作者的写作工具！

## 📄 许可证 (License)

本项目基于 [MIT License](https://github.com/akko9/novel-factory-ai/blob/main/LICENSE) 开源。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Made with ❤️ by Novel Factory AI Team*
