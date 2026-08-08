---
id: tool-07335
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 本地优先, 中文友好, 本地写作]
title: humanizer
summary: Claude Code 插件式写作流
source: https://github.com/jiakecong0724/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 7335
category: 画龙补充 / 扩容入库 — 补充源
repo: jiakecong0724/humanizer
stars: 1
url: https://github.com/jiakecong0724/humanizer
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 20e995e3fee0c341
  - methods/QUICK_START.md
---

# jiakecong0724/humanizer

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jiakecong0724/humanizer
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：人类化文章润色 是一个智能双语文本编辑工具，旨在识别和去除 AI 生成文本中的常见模式。作为 Claude Code 技能构建，它能自动检测文本是中文还是英文，并应用相应的规则集使你的写作听起来更自然、更有人味。
- **本地描述**：humanizer
- **拉取时间**：2026-07-25 19:18:15

---

# Humanizer: Bilingual AI Writing Pattern Remover
# 润色工具：双语 AI 写作痕迹去除器

<div align="center">

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/yourusername/humanizer-bilingual)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-purple.svg)](https://claude.ai)

**A bilingual text humanization tool that automatically detects language and removes AI writing patterns**

**双语文本人性化工具，自动检测语言并去除 AI 写作痕迹**

[English](#english) | [中文](#中文)

</div>

---

## English

### 📖 Overview

Humanizer is an intelligent, bilingual text editing tool designed to identify and remove common patterns found in AI-generated writing. Built as a Claude Code skill, it automatically detects whether your text is in Chinese or English and applies the appropriate set of rules to make your writing sound more natural and human.

Based on Wikipedia's comprehensive ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide and enhanced with practical tools from the community, this skill helps you transform sterile, algorithmic text into writing with genuine voice and personality.

### ✨ Features

| Feature | Chinese (28 patterns) | English (24 patterns) |
|---------|----------------------|----------------------|
| **Quality Scoring** | ✅ 6 dimensions, 60-point scale | ✅ 6 dimensions, 60-point scale |
| **Exemptions** | ✅ 5 scenarios | ✅ 4 scenarios |
| **Quick Checklist** | ✅ 6 items | ✅ 6 items |
| **Full Examples** | ✅ Complete Before/After | ✅ Complete Before/After |
| **Language-Specific Patterns** | Idiom stacking, particles, punctuation | Title case, curly quotes, em dashes |
| **Auto Language Detection** | ✅ | ✅ |

### 🎯 What It Detects

#### Content Patterns
- 🎈 **Significance inflation**: "marking a pivotal moment", "testament to"
- 📰 **Vague attributions**: "Experts believe", "Industry reports show"
- 🎪 **Promotional language**: "vibrant", "nestled", "breathtaking"
- 📋 **Formulaic structures**: "Despite these challenges..."

#### Language Patterns
- 🤖 **AI vocabulary**: "Additionally", "landscape", "crucial", "foster"
- 🔄 **Copula avoidance**: "serves as" instead of "is"
- 3️⃣ **Rule of three**: Forcing ideas into triplets
- 📚 **Synonym cycling**: protagonist→main character→central figure→hero

#### Style Patterns
- ➖ **Em dash overuse**: Too many — interruptions
- **B** **Excessive boldface**: Mechanical emphasis
- 😀 **Emoji decoration**: 🚀💡✅ in headers
- 💬 **Chatbot artifacts**: "I hope this helps!", "Great question!"

#### Chinese-Specific
- 🎎 成语堆砌 (Idiom stacking)
- 💬 语气词缺失 (Missing particles: 嘛、呢、啊)
- ，。Mixed punctuation (中英文标点混用)
- 📝 动词名词化 (Verb nominalization)

### 🚀 Quick Start

#### Installation

**Option 1: Direct Install (Recommended)**
```bash
# Clone to your Claude Code skills directory
git clone https://github.com/yourusername/humanizer-bilingual.git ~/.claude/skills/humanizer
```

**Option 2: Manual Install**
1. Download or clone this repository
2. Copy the entire folder to your Claude Code skills directory:
   - **macOS/Linux**: `~/.claude/skills/humanizer/`
   - **Windows**: `%USERPROFILE%\.claude\skills\humanizer\`

#### Verification
Restart Claude Code or reload skills, then type:
```
/humanizer
```
or use language-specific commands:
```
/润色    # For Chinese
/polish  # For English
```

### 💡 Usage

The tool automatically detects the language of your text:

**For English text:**
```
/polish Please humanize this text:

AI-assisted coding serves as an enduring testament to the transformative
potential of large language models...
```

**For Chinese text:**
```
/润色 请帮我人性化以下文本：

这个项目作为我们团队致力于创新的证明。此外，它展示了我们在
不断演变的技术格局中的关键作用...
```

**Or use the unified command:**
```
/humanizer [Your text in any language]
```

### 📊 Quality Scoring

Every rewritten text receives a quality score across 6 dimensions:

| Dimension | Score |
|-----------|-------|
| **Directness** | /10 |
| **Rhythm** | /10 |
| **Trust** | /10 |
| **Authenticity** | /10 |
| **Conciseness** | /10 |
| **Conventions** | /10 |

**Standards:** 54-60 Excellent | 42-53 Good | <42 Needs revision

### 📁 Project Structure

```
humanizer/
├── SKILL.md                          # Main entry point (language routing)
├── README.md                         # This file
└── .claude/
    └── skills/
        ├── README.md                 # Detailed documentation
        ├── zh/                       # Chinese module (28 patterns)
        │   ├── SKILL.md
        │   └── references/
        │       ├── 内容模式.md
        │       ├── 语言模式.md
        │       └── 风格与交流模式.md
        └── en/                       # English module (24 patterns)
            ├── SKILL.md
            └── references/
                ├── content-patterns.md
                ├── language-patterns.md
                └── style-patterns.md
```

### 🎓 Example

**Before (AI-generated):**
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. Additionally, these groundbreaking tools are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.

**After (Humanized):**
> AI coding assistants speed up some tasks. In a 2024 study by Google, developers using Codex completed simple functions 55% faster than a control group, but showed no improvement on debugging or architectural decisions.

### 🛡️ When to Exempt

Certain contexts may require some "AI patterns":

- **Technical Documentation**: Connectives are necessary structural elements
- **Legal Writing**: Excessive hedging is a legal norm
- **Academic Papers**: Vague attributions acceptable in literature reviews
- **Marketing Copy**: Promotional language is expected in advertising

### 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

If you find translation issues or want to improve the documentation:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

### 📄 License

This project is based on:
- [blader/humanizer](https://github.com/blader/humanizer) - Original English version
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) - Practical tools reference
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Pattern documentation

### 🙏 Credits

- Wikipedia's [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) community
- Original humanizer project by [blader](https://github.com/blader/humanizer)
- Stop-slop project by [hardikpandya](https://github.com/hardikpandya/stop-slop)

---

## 中文

### 📖 项目简介

人类化文章润色 是一个智能双语文本编辑工具，旨在识别和去除 AI 生成文本中的常见模式。作为 Claude Code 技能构建，它能自动检测文本是中文还是英文，并应用相应的规则集使你的写作听起来更自然、更有人味。

基于维基百科的综合指南["AI 写作特征"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，并融合社区实用工具的增强功能，这个技能帮助你将呆板、算法化的文本转变为具有真实声音和个性的写作。

### ✨ 功能特点

| 功能 | 中文版（28种模式） | 英文版（24种模式） |
|------|-------------------|-------------------|
| **质量评分** | ✅ 6维度60分制 | ✅ 6维度60分制 |
| **豁免条款** | ✅ 5种场景 | ✅ 4种场景 |
| **快速检查清单** | ✅ 6项 | ✅ 6项 |
| **完整示例** | ✅ 完整前后对比 | ✅ 完整前后对比 |
| **语言特有模式** | 成语堆砌、语气词、标点 | 标题大小写、弯引号、破折号 |
| **自动语言检测** | ✅ | ✅ |

### 🎯 检测内容

#### 内容模式
- 🎈 **意义膨胀**："标志着关键时刻"、"是……的证明"
- 📰 **模糊归因**："专家认为"、"行业报告显示"
- 🎪 **宣传性语言**："充满活力"、"坐落于"、"令人叹为观止"
- 📋 **公式化结构**："尽管存在这些挑战……"

#### 语言模式
- 🤖 **AI 词汇**："此外"、"格局"、"至关重要"、"培养"
- 🔄 **系动词回避**："作为"而非"是"
- 3️⃣ **三段式法则**：强行分成三组
- 📚 **同义词循环**：主人公→主要角色→中心人物→英雄

#### 风格模式
- ➖ **破折号过度**：太多——中断
- **B** **粗体过度**：机械式强调
- 😀 **表情符号装饰**：标题中的🚀💡✅
- 💬 **聊天机器人痕迹**："希望这对您有帮助！"、"好问题！"

#### 中文特有
- 🎎 成语堆砌（连续多个四字成语）
- 💬 语气词缺失（缺少"嘛"、"呢"、"啊"）
- ，。中英文标点混用
- 📝 动词名词化（"进行讨论"→"讨论"）

### 🚀 快速开始

#### 安装

**方式一：直接安装（推荐）**
```bash
# 克隆到 Claude Code 技能目录
git clone https://github.com/yourusername/humanizer-bilingual.git ~/.claude/skills/humanizer
```

**方式二：手动安装**
1. 下载或克隆本仓库
2. 将整个文件夹复制到 Claude Code 技能目录：
   - **macOS/Linux**: `~/.claude/skills/humanizer/`
   - **Windows**: `%USERPROFILE%\.claude\skills\humanizer\`

#### 验证安装
重启 Claude Code 或重新加载技能，然后输入：
```
/humanizer
```
或使用语言特定命令：
```
/润色    # 中文
/polish  # 英文
```

### 💡 使用方法

工具会自动检测文本语言：

**处理英文文本：**
```
/polish Please humanize this text:

AI-assisted coding serves as an enduring testament to the transformative
potential of large language models...
```

**处理中文文本：**
```
/润色 请帮我人性化以下文本：

这个项目作为我们团队致力于创新的证明。此外，它展示了我们在
不断演变的技术格局中的关键作用...
```

**或使用统一命令：**
```
/humanizer [任何语言的文本]
```

### 📊 质量评分

每个重写的文本都会在 6 个维度上获得质量评分：

| 维度 | 得分 |
|------|------|
| **直接性** | /10 |
| **节奏** | /10 |
| **信任度** | /10 |
| **真实性** | /10 |
| **精炼度** | /10 |
| **规范性** | /10 |

**标准：** 54-60 优秀 | 42-53 良好 | <42 需重新修订

### 📁 项目结构

```
humanizer/
├── SKILL.md                          # 主入口（语言路由）
├── README.md                         # 本文件
└── .claude/
    └── skills/
        ├── README.md                 # 详细文档
        ├── zh/                       # 中文模块（28种模式）
        │   ├── SKILL.md
        │   └── references/
        │       ├── 内容模式.md
        │       ├── 语言模式.md
        │       └── 风格与交流模式.md
        └── en/                       # 英文模块（24种模式）
            ├── SKILL.md
            └── references/
                ├── content-patterns.md
                ├── language-patterns.md
                └── style-patterns.md
```

### 🎓 示例

**改写前（AI 生成）：**
> 这个项目作为我们团队致力于创新的证明。此外，它展示了我们在不断演变的技术格局中的关键作用，突出了其持久的重要性。

**改写后（人性化）：**
> 这个项目用了三个月开发，主要解决了数据同步的延迟问题。团队五个人，现在日活跃用户 2000 多。

### 🛡️ 豁免场景

某些场景可能需要保留一些"AI 模式"：

- **技术文档**：连接词可能是必要的结构性词汇
- **法律/合同**：过度限定是法律行文的规范要求
- **学术论文**：模糊归因在综述中可接受
- **正式公文**：动词名词化是公文体惯例
- **营销文案**：宣传性语言在广告中是预期的

### 🤝 贡献

欢迎贡献！请随时提交 issue 或 pull request。

如果你发现翻译问题或想要改进文档：
1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/improvement`)
3. 提交你的更改 (`git commit -am '添加某些改进'`)
4. 推送到分支 (`git push origin feature/improvement`)
5. 开启一个 Pull Request

### 📄 许可

本项目基于：
- [blader/humanizer](https://github.com/blader/humanizer) - 原始英文版
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) - 实用工具参考
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - 模式文档

### 🙏 致谢

- 维基百科的 [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) 社区
- [blader](https://github.com/blader/humanizer) 的原始 humanizer 项目
- [hardikpandya](https://github.com/hardikpandya/stop-slop) 的 stop-slop 项目

---

<div align="center">

**⚠️ Important Note / 重要提示**

This tool is not designed to "fool" AI detectors, but to genuinely improve writing quality.
The best way to "de-AI" text is to give it real human thinking and voice.

这个工具不是为了"欺骗" AI 检测器，而是为了真正提升写作质量。
最好的"去 AI 化"方法是让文字有真实的人类思考和声音。

related:
  - methods/QUICK_START.md
---

**Made with ❤️ for better writing**

</div>
