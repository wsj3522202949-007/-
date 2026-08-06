---
id: tool-00860
type: tool
area: 库
status: active
tags: [去AI味, 提示词, 校对, 协议未明, 本地优先, 中文友好, 改稿润色, 本地写作]
title: semi-research-writing-prompts
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/hyperbolic-c/semi-research-writing-prompts
created: 2026-07-18
updated: 2026-07-18
no: 860
category: 二、网文 / 长篇 AI 写作系统 库
repo: hyperbolic-c/semi-research-writing-prompts
stars: 3
url: https://github.com/hyperbolic-c/semi-research-writing-prompts
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# hyperbolic-c/semi-research-writing-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hyperbolic-c/semi-research-writing-prompts
- **Stars**：3
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Domain-specific AI prompts for semiconductor research writing ✨
- **本地描述**：Domain-specific AI prompts for semiconductor research writing ✨
- **拉取时间**：2026-07-23 23:04:05

---

# semi-research-writing-prompts

> 本项目基于 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 重构，针对**半导体材料与器件**领域进行了领域适配和格式优化，用于该领域的AI写作。

## 项目背景

[awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 是一个开源的 AI 科研写作提示词库，收集了来自顶尖研究机构的写作技巧。本项目在此基础上进行二次开发：

- **领域适配**：将通用计算机科学提示词调整为半导体材料与器件领域
- **格式优化**：从 LaTeX 输出改为 Word 纯文本格式
- **内容精简**：整合拆分为更易用的独立文件

## 核心特点

- 🔬 **领域定制**：专为半导体材料与器件设计（光电探测器、LED、HEMT、MOSFET、二维材料等）
- 📝 **Word 友好**：输出纯文本格式，可直接复制到 Word 使用
- 🚀 **开箱即用**：每个场景对应独立文件，复制即用

## 文件列表

| 文件 | 功能 | 适用场景 |
|------|------|-------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| [zh2en-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/zh2en-semiconductor.md) | 中转英 | 中文草稿 → 英文论文 |
| [en2zh-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/en2zh-semiconductor.md) | 英转中 | 英文论文 → 中文理解 |
| [zh2zh-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/zh2zh-semiconductor.md) | 中转中 | 中文口语 → 学术规范 |
| [abbreviation-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/abbreviation-semiconductor.md) | 缩写 | 精简字数 |
| [expansion-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/expansion-semiconductor.md) | 扩写 | 补充细节 |
| [polish-en-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/polish-en-semiconductor.md) | 英文润色 | 提升英文质量 |
| [polish-zh-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/polish-zh-semiconductor.md) | 中文润色 | 提升中文质量 |
| [logic-check-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/logic-check-semiconductor.md) | 逻辑检查 | 最终校对 |
| [de-ai-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/de-ai-semiconductor.md) | 去 AI 味 | 去除机械感 |
| [architecture-diagram-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/architecture-diagram-semiconductor.md) | 架构图 | 器件结构可视化 |
| [figure-caption-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/figure-caption-semiconductor.md) | 图标题 | 生成英文图注 |
| [table-caption-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/table-caption-semiconductor.md) | 表标题 | 生成英文表注 |
| [experiment-analysis-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/experiment-analysis-semiconductor.md) | 实验分析 | 数据解读 |
| [reviewer-perspective-semiconductor.md](https://github.com/hyperbolic-c/semi-research-writing-prompts/blob/main/prompts/reviewer-perspective-semiconductor.md) | Reviewer 视角 | 稿件自审 |

## 使用方法

直接复制对应 .md 文件中的 prompt 内容到聊天框中使用。

## 致谢

感谢 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 项目提供的基础框架和内容。
