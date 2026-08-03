---
id: tool-07358
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 需API密钥, 中文友好, 人物设定]
title: worldweaver
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/kivencheng2004/worldweaver
created: 2026-07-18
updated: 2026-07-18
no: 7358
category: 画龙补充 / 扩容入库 — 补充源
repo: kivencheng2004/worldweaver
stars: 0
url: https://github.com/kivencheng2004/worldweaver
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# kivencheng2004/worldweaver

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/kivencheng2004/worldweaver
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：中文: 专为创作者打造的 AI 世界观构建助手。支持 RAG 知识库检索、设定一致性检查和本地 Markdown 管理。
- **本地描述**：worldweaver
- **拉取时间**：2026-07-25 19:19:27

related:
  - methods/QUICK_START.md
---

# 🕸️ WorldWeaver - AI Worldbuilding Assistant

**WorldWeaver** 是一个基于大语言模型（LLM）的命令行工具，旨在辅助作家、游戏策划和跑团主持人（DM）构建、管理和完善架空世界观。

它不仅仅是一个聊天机器人，更是一个拥有**长期记忆**和**逻辑审查**能力的创作副驾驶，帮你将零散的灵感编织成一个完整、自洽的世界。

## ✨ 核心功能

*   **🧠 检索增强生成 (RAG)**: 
    *   利用向量数据库 (ChromaDB) 存储你的设定。
    *   在对话中自动检索相关的旧设定作为上下文，确保 AI 不会"忘记"你三个月前写的设定。
*   **📝 本地化文件管理**:
    *   所有设定以 **Markdown + YAML Frontmatter** 格式存储在本地。
    *   你可以随时用 Obsidian、VS Code 或 Typora 编辑它们，数据完全属于你。
*   **⚖️ 一致性检查**:
    *   AI 会分析你的新设定，并与现有数据库进行比对，自动指出时间线冲突、战力崩坏或逻辑矛盾。
*   **💬 沉浸式创作**:
    *   支持多模型切换 (Claude 3.5, GPT-4, Llama 3)。
    *   提供头脑风暴、情节续写和设定提取功能。

## 🛠️ 技术栈

*   **Language**: Python 3.10+
*   **LLM API**: OpenRouter (支持 OpenAI, Anthropic, Google 等主流模型)
*   **Vector DB**: ChromaDB (本地嵌入式向量库)
*   **UI**: Rich (精美的终端交互界面)

## 🚀 快速开始

### 1. 安装依赖

确保你已安装 Python 3.10 或更高版本。

```bash
git clone https://github.com/yourusername/worldweaver.git
cd worldweaver
pip install -r requirements.txt
```

### 2. 配置 API Key

本项目使用 OpenRouter API 以支持多种模型。
在项目根目录下创建一个 `.env` 文件：

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. 运行

```bash
python main.py
```

## 📖 使用指南

启动程序后，你将看到以下菜单：

1.  **对话模式 (Chat Mode)**: 
    *   自由对话。
    *   输入 `/save`：AI 自动从刚才的对话中提取设定并保存为文件。
    *   输入 `/check`：检查刚才 AI 生成的内容是否与旧设定冲突。
2.  **创建新设定 (Create Entity)**:
    *   引导式创建角色、地点、势力等。
    *   保存前自动进行一致性审查。
3.  **搜索设定 (Search)**:
    *   支持关键词搜索和语义搜索（例如搜索"火系魔法"能找到"烈焰风暴"）。

## 📂 数据结构

你的设定将保存在 `./data/worldbuilding` 目录下，结构如下：

```text
data/
└── worldbuilding/
    ├── characters/   # 角色
    ├── locations/    # 地点
    ├── items/        # 物品
    ├── factions/     # 势力
    └── history/      # 历史事件
```

## 🤝 贡献

欢迎提交 Issue 或 Pull Request！如果你有好的想法（比如接入绘图 AI 或生成关系图谱），请随时分享。

## 📄 License

MIT License
