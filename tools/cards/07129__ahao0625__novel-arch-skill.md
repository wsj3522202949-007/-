---
id: tool-07129
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 本地写作]
title: novel-arch-skill
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/ahao0625/novel-arch-skill
created: 2026-07-18
updated: 2026-07-18
no: 7129
category: 画龙补充 / 扩容入库 — 补充源
repo: ahao0625/novel-arch-skill
stars: 1
url: https://github.com/ahao0625/novel-arch-skill
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: fc11322f8b95708a
  - methods/QUICK_START.md
---

# ahao0625/novel-arch-skill

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ahao0625/novel-arch-skill
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：ai-assisted-writing, ai-writing, fiction-writing, novel-creation, novel-writing, web-novel, writing-tool
- **GitHub 描述**：AI 网文创作项目架构搭建技能 — 基于通用架构方案，一键创建小说项目目录结构和核心文件
- **本地描述**：novel-arch-skill
- **拉取时间**：2026-07-25 19:11:43

---

# Novel Arch

> **AI 网文创作项目架构搭建技能** — 任何 AI 平台通用。给大纲，自动生成全部项目文件。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ahao0625/novel-arch-skill?style=flat&logo=github)](https://github.com/ahao0625/novel-arch-skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahao0625/novel-arch-skill?style=flat&logo=github)](https://github.com/ahao0625/novel-arch-skill/network/members)
[![GitHub issues](https://img.shields.io/github/issues/ahao0625/novel-arch-skill)](https://github.com/ahao0625/novel-arch-skill/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/ahao0625/novel-arch-skill)](https://github.com/ahao0625/novel-arch-skill)
[![GitHub release](https://img.shields.io/github/v/release/ahao0625/novel-arch-skill)](https://github.com/ahao0625/novel-arch-skill/releases)
[![Maintained](https://img.shields.io/badge/Maintained-YES!-green.svg)](https://github.com/ahao0625/novel-arch-skill)

[功能](#功能) · [使用方式](#使用方式) · [操作](#操作) · [安装](#安装) · [贡献](#贡献) · [许可](#许可)

---

## 功能

**给任意 AI 一个指令，自动完成整个网文项目搭建。** 不用装插件、不用配环境。

| 能力 | 说明 |
|:---|:---|
| 📁 **项目创建** | 一句话生成完整目录结构（13 个模块，含守御体系） |
| 📖 **章节写作** | AI 按创作流程写正文，自动维护日志/伏笔/索引 |
| ✏️ **设定管理** | 修改设定后自动同步速查锚点并记录变更日志 |
| 🔍 **质量审计** | 设定冲突检测、角色 OOC 检查、伏笔健康监控、红线违规拦截 |
| 📦 **关卷存档** | 卷结束时自动生成设定快照，为下一卷做准备 |

**适用题材：** 玄幻 · 仙侠 · 都市 · 科幻 · 历史 · 悬疑 · 言情 · 轻小说

**适用平台：** Claude · ChatGPT · DeepSeek · WorkBuddy · 通义千问 · Kimi · 任何支持文件读写的 AI

---

## 使用方式

### 快速开始

```
"新建一个玄幻小说项目，以下是大纲：【粘贴大纲】"
```

AI 会自动完成：解析大纲 → 创建目录 → 填充设定/人物/大纲 → 自检 → 输出报告。

### 日常操作

```
"继续写第 5 章，上一章写到主角被追杀至悬崖边"
"加一个反派角色，设定是..."
"对最近 10 章做一次审计"
"本卷写完了，关卷"
```

### 工作原理

```
用户指令 → AI 读取操作手册 → 按步骤执行 → 每步自检 → 输出结果
               ↑
      references/ai-operations-manual.md
      定义了完整执行流程、字段规范、自检规则
```

---

## 操作

| 操作 | 输入 | 输出 |
|:---|:---|---:|
| **新建项目** | 书名、类型、卷数、大纲 | 13 目录 + 全部核心文件（基于大纲填充） |
| **写入章节** | 章号、前情 | 正文文件 + 日志更新 + 伏笔更新 + 索引更新 |
| **更新设定** | 修改内容 | 对应文件 + 速查锚点同步 + 变更日志记录 |
| **运行审计** | （可选范围） | 审计报告（致命/警告/提示三级） |
| **关卷存档** | 卷号 | 设定快照 + 速查刷新 + 卷概述完善 |

---

## 安装

### WorkBuddy 用户

```bash
# 克隆仓库到 WorkBuddy skills 目录
git clone https://github.com/ahao0625/novel-arch-skill.git ~/.workbuddy/skills/novel-arch
```

或从 [Releases](https://github.com/ahao0625/novel-arch-skill/releases) 下载 zip 解压到 `~/.workbuddy/skills/novel-arch/`。

### 其他平台用户

AI 需要具有文件读写能力：
- **Claude** → Claude Projects 中上传 `references/ai-operations-manual.md`
- **ChatGPT** → Code Interpreter / Projects 中上传
- **其他平台** → 粘贴 `references/ai-operations-manual.md` 内容到对话

---

## 项目文件

```
novel-arch-skill/
├── SKILL.md                          # 技能定义（用户视角）
├── references/
│   ├── ai-operations-manual.md       # AI 操作手册（核心）
│   └── ai-novel-architecture.md      # 架构方案全文
├── scripts/
│   └── setup_project.py              # 目录搭建脚本（可选）
├── .github/
│   ├── workflows/ci.yml              # CI 工作流
│   ├── workflows/release.yml         # 自动发布
│   ├── ISSUE_TEMPLATE/               # Issue 模板
│   ├── PULL_REQUEST_TEMPLATE.md      # PR 模板
│   └── FUNDING.yml                   # 赞助配置
├── CODE_OF_CONDUCT.md                # 行为准则
├── CONTRIBUTING.md                   # 贡献指南
├── SECURITY.md                       # 安全政策
├── CHANGELOG.md                      # 更新日志
├── LICENSE                           # MIT 许可
└── .editorconfig                     # 编辑器配置
```

---

## 相关项目

| 项目 | 说明 |
|:---|:---|
| [general-writing-skill](https://github.com/ahao0625/general-writing-skill) | 通用写作技能 — 会写作、懂思考、文笔好 |
| [novel-audit-skill](https://github.com/ahao0625/novel-audit-skill) | 网文审计技能 — 11 维度系统性文本审计 |
| [novel-polish-skill](https://github.com/ahao0625/novel-polish-skill) | 网文润色技能 — 情感保真，人感优先 |

---

## 贡献

欢迎提交 [Issue](https://github.com/ahao0625/novel-arch-skill/issues) 报告问题或提出建议。

提交 PR 前请阅读 [CONTRIBUTING.md](https://github.com/ahao0625/novel-arch-skill/blob/main/CONTRIBUTING.md)。

---

## 许可

[MIT](https://github.com/ahao0625/novel-arch-skill/blob/main/LICENSE) © 2026 ahao0625

related:
  - methods/QUICK_START.md
---

<p align="center">
  <a href="https://github.com/ahao0625/novel-arch-skill/stargazers">⭐ Star 支持</a>
  ·
  <a href="https://github.com/ahao0625/novel-arch-skill/issues">💬 反馈问题</a>
  ·
  <a href="https://github.com/ahao0625/novel-arch-skill/releases">📦 下载发布版</a>
</p>
