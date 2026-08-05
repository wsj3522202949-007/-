---
id: tool-07607
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 中文友好]
title: novel_gen
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/windinrain1975/novel_gen
created: 2026-07-18
updated: 2026-07-18
no: 7607
category: 画龙补充 / 扩容入库 — 补充源
repo: windinrain1975/novel_gen
stars: 5
url: https://github.com/windinrain1975/novel_gen
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/QUICK_START.md
---

# windinrain1975/novel_gen

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/windinrain1975/novel_gen
- **Stars**：5
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：novel_gen
- **拉取时间**：2026-07-25 19:27:06

---

# Novel Gen - AI驱动的智能小说生成器

Novel Gen 是一个基于大型语言模型 (LLM) 的自动化小说生成工具。它旨在帮助用户快速构建小说的完整架构、多层次大纲，并生成章节内容。本工具特别强化了针对网络爽文的节奏控制，引入了三段式节奏模型（50%困境铺垫 - 20-30%气氛推动 - 20-30%爽点爆发），以确保生成内容的阅读快感和市场潜力。

此外，项目内置了多轮审核机制，能够在各个生成阶段（架构、全局大纲、子故事、章节大纲）对内容的逻辑性、一致性和吸引力进行自动评估和优化，力求达到商业化出版标准。

`[English Version](README_EN.md)` | `[🚀 快速开始](QUICKSTART.md)` | `[配置文档](docs/CONFIG.md)` | `[使用指南](docs/USAGE.md)`

## ✨ 主要特点

- **🎯 分阶段智能生成**：从概念到架构，再到全局大纲、阶段子故事、章节大纲，最后生成正文，层层递进
- **🚀 AI驱动的爽文节奏控制**：内置针对网络爽文优化的三段式节奏模型，确保生成内容的阅读快感
- **🔍 多轮AI审核与优化**：在关键生成节点引入AI自动审核，主动发现并修正潜在问题，提升内容质量
- **⚙️ 灵活的配置选项**：用户可以通过 `config.json` 文件轻松配置API密钥、模型选择、生成参数等
- **🧩 模块化设计**：代码结构清晰，易于理解、维护和扩展新功能
- **📝 多种生成模式**：提供仅生成大纲、仅生成正文、检查修复等多种模式，满足不同需求
- **📁 智能文件管理**：生成的文件自动保存在 `output/小说名称/` 目录下，便于管理

## 🚀 快速开始

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/windinrain1975/novel_gen.git
cd novel_gen

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥

**方法一：使用配置向导（推荐）**
```bash
python setup_config.py
```

**方法二：手动配置**
```bash
# 复制配置模板
cp config.template.json config.json

# 编辑配置文件，填入您的API密钥
# 详细配置说明请参考 docs/CONFIG.md
```

### 3. 准备小说概念

创建一个文本文件（例如 `my_novel.txt`），格式如下：
```
我的小说标题
这里是小说的详细概念描述，包括主题、主角、背景、风格等...
```

### 4. 开始生成

**完整流程（推荐）**
```bash
python main.py my_novel.txt l
```

**其他模式**
```bash
# 仅生成大纲
python main.py my_novel.txt l --outline_only

# 仅生成正文（需要大纲已存在）
python main.py my_novel.txt l --content_only

# 检查和修复现有内容
python main.py my_novel.txt l --check_and_repair
```

参数说明：
- `l`: 长篇小说（>100k字）
- `m`: 中篇小说（<100k字）
- `s`: 短篇小说（<30k字）

## 📖 详细文档

- `[📋 配置文档](docs/CONFIG.md)` - 详细的配置选项说明
- `[📚 使用指南](docs/USAGE.md)` - 完整的使用教程
- `[🏗️ 架构说明](docs/ARCHITECTURE.md)` - 项目架构和设计理念
- `[🔧 开发指南](docs/DEVELOPMENT.md)` - 开发和贡献指南

## 📁 项目结构

```
novel_gen/
├── core/                       # 核心生成逻辑
│   ├── generator.py            # 主要的小说生成和审核流程
│   ├── state_manager.py        # 状态管理器
│   └── rag_engine.py           # RAG检索引擎
├── prompts/                    # LLM 提示词模板
│   ├── chapter.py              # 章节生成提示词
│   ├── framework.py            # 架构生成提示词
│   ├── outline.py              # 大纲生成提示词
│   └── review.py               # 审核相关提示词
├── utils/                      # 工具类函数
│   ├── llm_utils.py            # LLM API 调用封装
│   ├── json_utils.py           # JSON 清洗和修复
│   ├── file_utils.py           # 文件读写工具
│   └── progress_monitor.py     # 进度监控和日志
├── validators/                 # 内容验证器
│   ├── consistency.py          # 一致性验证
│   └── plot.py                 # 情节验证
├── models/                     # 数据模型
│   ├── character.py            # 人物模型
│   ├── world.py                # 世界模型
│   ├── item.py                 # 物品模型
│   └── technology.py           # 技术模型
├── docs/                       # 文档目录
├── output/                     # 生成文件输出目录
├── config.py                   # 配置管理类
├── config.template.json        # 配置文件模板
├── main.py                     # 主程序入口
├── setup_config.py             # 配置向导脚本
├── requirements.txt            # Python 依赖
├── LICENSE                     # MIT 许可证
├── README.md                   # 中文说明文档
└── README_EN.md                # 英文说明文档
```

## 🔧 配置说明

### 核心配置项

```json
{
  "llm_api_key": "your-api-key-here",
  "llm_base_url": "https://api.openai.com/v1",
  "llm_models": {
    "design_model": "gpt-4o",
    "content_model": "gpt-4o-mini"
  }
}
```

### 高级配置

- **审核设置**：控制各阶段的AI审核轮数
- **生成模式**：选择章节大纲生成策略
- **节奏控制**：调整爽文节奏分配比例
- **输出设置**：自定义文件保存格式

详细配置说明请参考 `[配置文档](docs/CONFIG.md)`。

## 🎯 使用场景

- **网络小说创作**：快速生成符合市场需求的爽文内容
- **创意写作辅助**：为作者提供灵感和结构化思路
- **内容策划**：批量生成小说大纲和章节框架
- **写作教学**：展示小说创作的系统化流程

## 🤝 贡献

欢迎各种形式的贡献！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证。详情请见 `[LICENSE](LICENSE)` 文件。

版权所有 (c) 2024 windinrain1975

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

related:
  - methods/QUICK_START.md
---

如果您觉得这个项目有用，请给我们一个 ⭐ Star！
