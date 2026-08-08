---
id: tool-07542
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: llm2novel
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/sicyuan404/llm2novel
created: 2026-07-18
updated: 2026-07-18
no: 7542
category: 画龙补充 / 扩容入库 — 补充源
repo: sicyuan404/llm2novel
stars: 0
url: https://github.com/sicyuan404/llm2novel
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a6a5aa0ad1f258ae
  - methods/QUICK_START.md
---

# sicyuan404/llm2novel

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/sicyuan404/llm2novel
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：一个基于 Streamlit 的智能小说创作平台，提供从构思到成稿的全流程 AI 辅助写作体验。
- **本地描述**：llm2novel
- **拉取时间**：2026-07-25 19:25:06

---

# 📚 Novel Agno - 智能小说创作助手

一个基于 Streamlit 的智能小说创作平台，提供从构思到成稿的全流程 AI 辅助写作体验。

## ✨ 主要功能

### 🎯 核心工作流
```
├── 🏠 基础信息
│   ├── 书名
│   ├── 简介
│   └── 封面
│   
├── 💡 核心想法 + 
│   ├── 金手指
│   ├── 想法1
│   └── 想法2

├── 🌍 世界观 

├── 📑 总大纲

├── 📚 卷纲
│   ├── 第一卷 卷纲：【待命名】
│   └── 第二卷 卷纲：【待命名】 
 
├── 📚 章纲
│   ├── 📄 第一章 章纲：【章节标题待定】
│   └── 📄 第二章 章纲：【章节标题待定】

└── 📚 正文
    ├── 📄 第一章 正文：【章节标题待定】
    └── 📄 第二章 正文：【章节标题待定】
```

### 🤖 AI 功能特性

- **智能提示词管理**：支持全局和单书级别的 AI 角色配置
- **多模式写作辅助**：
  - 续写/扩写
  - 提供灵感
  - 润色优化
- **上下文关联**：AI 可参考大纲、世界观等内容进行创作
- **优先级配置**：本书独立设置 > 全局通用设置 > 系统默认

### 📝 编辑器功能

- **层级化内容管理**：支持卷、章的多级结构
- **实时保存**：编辑内容自动保存
- **快速导航**：侧边栏提供便捷的内容切换
- **引用系统**：可引用其他部分内容作为 AI 创作参考

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Streamlit

### 安装步骤

1. 克隆项目
```bash
git clone <repository-url>
cd novel-agno
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动应用
```bash
streamlit run Home.py
```

### 配置说明

首次使用需要在 **设置页面** 配置 AI 服务：

1. 选择 AI 提供商（支持 DeepSeek、OpenAI 等）
2. 填入 API Key
3. 配置模型参数

## 📖 使用指南

### 1. 创建新小说
- 在主页点击"创建新小说"
- 填写书名和基础信息

### 2. 构思阶段
- 使用 **核心想法** 功能设计金手指和卖点
- 在 **世界观** 页面构建设定
- 制定 **总大纲** 规划全书结构

### 3. 细化大纲
- 创建分卷，设置卷纲
- 逐章设计章纲，明确每章内容

### 4. 正文创作
- 基于章纲进行正文写作
- 使用 AI 辅助续写、润色
- 支持引用大纲内容保持连贯性

### 5. 提示词定制
- 在 **Prompts 管理** 页面自定义 AI 角色
- 支持为不同书籍设置专属写作风格
- 可随时恢复默认配置

## 🛠 技术架构

- **前端**：Streamlit
- **后端**：Python
- **AI 集成**：OpenAI API 兼容接口
- **数据存储**：JSON 文件

## 📁 项目结构

```
novel-agno/
├── Home.py              # 主页面
├── utils.py             # 核心工具类
├── pages/               # 页面组件
│   ├── 1_✏️_Editor.py   # 编辑器页面
│   ├── 2_⚙️_Config.py   # 配置页面
│   └── 3__Prompts.py    # 提示词管理页面
├── novels/              # 小说数据存储
├── .gitignore           # Git 忽略文件
└── readme.md            # 项目说明
```

## 🔧 自定义配置

### AI 提示词系统

系统提供三层提示词配置：

1. **系统默认**：内置的专业写作提示词
2. **全局通用**：影响所有书籍的通用配置
3. **本书独立**：针对单本书的特殊风格定制

### 支持的写作阶段

- `meta`: 基础信息完善
- `idea`: 核心想法构思
- `worldview`: 世界观构建
- `general_outline`: 总大纲规划
- `volume_outline`: 卷纲设计
- `chapter_outline`: 章纲细化
- `content`: 正文写作

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

related:
  - methods/QUICK_START.md
---

**提示**：请确保在 `.gitignore` 中排除敏感信息（如 API Key）和个人创作内容。
