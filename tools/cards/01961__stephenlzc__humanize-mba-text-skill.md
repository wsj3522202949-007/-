---
id: tool-04796
type: tool
area: 库
status: active
tags: [去AI味, 协议未明, 本地优先, 中文友好, 本地写作]
title: humanize-mba-text-skill
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/stephenlzc/humanize-mba-text-skill
created: 2026-07-18
updated: 2026-07-18
$11961
category: 一、去 AI 味 / Humanizer 库
repo: stephenlzc/humanize-mba-text-skill
stars: 33
language: Python
license: MIT
url: https://github.com/stephenlzc/humanize-mba-text-skill
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 08131ec6b8df95d1
  - methods/改稿润色指令库.md
---

# Humanize MBA Text - 去除 AI 写作痕迹

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Claude-Skill-orange.svg" alt="Claude Skill">
  <img src="https://img.shields.io/badge/Version-1.5-brightgreen.svg" alt="Version: 1.5">
  <img src="https://img.shields.io/badge/Kimi-CLI-blue.svg" alt="Kimi CLI">
  <img src="https://img.shields.io/badge/中文-🇨🇳-red.svg" alt="中文">
  <a href="README_EN.md"><img src="https://img.shields.io/badge/English-🇺🇸-inactive.svg" alt="English"></a>
  <a href="README_KR.md"><img src="https://img.shields.io/badge/한국어-🇰🇷-inactive.svg" alt="한국어"></a>
  <a href="README_JP.md"><img src="https://img.shields.io/badge/日本語-🇯🇵-inactive.svg" alt="日本語"></a>
</p>

<p align="center">
  <b>专门针对中国 MBA 毕业论文的 AI 写作痕迹检测与去除工具</b>
</p>

<p align="center">
  <code>#AI-Detection</code> <code>#Academic-Writing</code> <code>#MBA-Thesis</code> <code>#Claude-Skill</code> <code>#Text-Humanization</code> <code>#ChatGPT-Alternative</code> <code>#LLM-Writing</code> <code>#Research-Tools</code> <code>#Academic-Integrity</code> <code>#Chinese-NLP</code>
</p>

---

## 🎯 项目简介

这是一个专门为**中国 MBA 毕业论文**设计的 AI 写作痕迹检测与去除工具。基于 MBA 论文的学术规范和实践要求，通过多维度检测方法识别文本中的 AI 生成特征，并提供具体的修改建议，帮助你将 AI 生成的文本改写为自然、人类化的学术写作风格。

### ✨ 版本 1.5 新特性（段落级句长 CV + 报告可读性升级）

- 📐 **段落级句长 CV 分析**：参考 `AI_artifact_detection` 方法，以段落内句子长度的变异系数（CV）作为核心 AI 信号，中文按 CJK 字符、英文按单词计数
- 📊 **中文 CV 报告**：检测 Markdown 报告末尾自动附加五段式 CV 报告——整体统计 / CV 分布 / Uniform 段落详情 / 章节汇总 / 句长分布
- 🔁 **改写前后对比**：新增 `scripts/detect_compare.py`，输入改写前、改写后两个文本，输出中文 Before/After 对比 Markdown
- 🌐 **可选英文检测模式**：`sentence_length.analyze(text, language="en")` 支持英文散文的句长 CV 检测
- 🎯 **内容片段带上下文**：详细问题列表中的内容片段现在显示匹配处前后约 20 字，便于快速定位
- 📝 **修改建议完整显示**：不再截断修改建议，完整输出所有提示
- 📋 **Uniform 段落完整表格**：CV < 0.30 的段落全部以表格列出，不再限制 20 条
- ⏰ **真实生成时间**：报告末尾显示实际生成时间（YYYY-MM-DD HH:MM:SS）

> 历史版本（1.4 / 1.3 / 1.2）特性已归档至 [`FEATURE.md`](https://github.com/stephenlzc/humanize-mba-text-skill/blob/main/FEATURE.md)。

### 核心功能

- ✅ **多层级 AI 检测**：从规则匹配（regex）→ 散文统计（5 维 CV/指纹）→ 语义链（10 维跨段/跨章）三层叠加
- ✅ **段落级句长 CV 报告**：基于 `AI_artifact_detection` 方法，输出 Uniform 段落、CV 分布、章节汇总、句长分布
- ✅ **改写前后对比**：`scripts/detect_compare.py` 一键生成 Before/After 中文对比报告
- ✅ **章节特定规则**：针对绪论、理论、分析、建议、结论 5 个章节的优化策略
- ✅ **MBA 论文规范**：符合中国高校 MBA 论文字数、结构、格式要求
- ✅ **结构化改写计划**：每个 issue 都附 location + skeleton + recommended replacements + 目标字数
- ✅ **自动修复**：自动处理中英文混排空格等简单问题
- ✅ **智能反馈**：生成详细的修改建议和前后对比示例
- ✅ **Claude Skill 集成**：可作为 Claude Code 的 Skill 直接使用

### 技术参考

本项目在优化策略设计上参考了 [thesis-optimizer](https://github.com/Haimbeau1o/thesis-optimizer) 项目的三维协同优化理念：
- 🔍 **降AI检测率**：句式多样化、语气自然化、逻辑人性化
- 📉 **降查重率**：深度语义改写、引用规范化、专业术语处理  
- ✨ **学术润色**：表达精准化、学术规范性、可读性优化

---

## 🎓 MBA 论文核心原则

本工具基于中国 MBA 论文的学术规范设计，遵循以下核心原则：

### 1. 实践导向
- 必须来源于企业管理实际，解决具体管理问题
- 避免纯理论空谈

### 2. 小题大做
- 选题聚焦明确，"小题深做"
- 核心概念不超过 2-3 个
- 避免选题过大、过于宽泛

### 3. 数据溯源
- 所有数据必须注明来源
- 确保准确性和可信度
- 删除"相关数据显示"等模糊表述

### 4. 理论支撑
- 运用 1-2 个相关理论作为分析框架
- 避免就事论事

### 5. 结构规范
- 正文字数 ≥ 3 万字
- 每章至少 4 节（含本章小结）
- 每节内容充实，避免一节不足一页

### 6. 学术诚信
- 复制率 < 15%
- 不编造数据，所有引用可核实

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/stephenlzc/humanize-mba-text-skill.git
cd humanize-mba-text-skill

# 安装依赖（如需使用 transformers 模型）
pip install transformers torch
```

### 基础使用

#### 1. 基础检测

```bash
# 使用基础规则检测
python scripts/detect_ai_patterns.py your_text.txt --format markdown --output report.md
```

#### 2. 多维度融合检测（推荐）

```bash
# 使用多维度检测
python scripts/multi_detecto
