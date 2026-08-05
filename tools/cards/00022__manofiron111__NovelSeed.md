---
id: tool-00022
type: tool
area: 库
status: active
tags: [去AI味, 大纲规划, Claude插件, 协议未明, 本地优先, 中文友好, 本地写作]
title: NovelSeed
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/manofiron111/novelseed
created: 2026-07-18
updated: 2026-07-18
no: 22
category: 二、网文 / 长篇 AI 写作系统 库
repo: manofiron111/NovelSeed
stars: 2
url: https://github.com/manofiron111/novelseed
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# manofiron111/NovelSeed

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/manofiron111/novelseed
- **Stars**：2
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：🌱 Plant a seed, grow a novel. Open-source AI novel-writing agent.
- **本地描述**：🌱 Plant a seed, grow a novel. Open-source AI novel-writing agent.
- **拉取时间**：2026-07-23 22:39:30

---

# 🌱 NovelSeed

<p align="center">
  <strong>种下一颗种子，长出一部小说。</strong><br>
  <em>Plant a seed, grow a novel.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-green?style=flat-square&labelColor=161b22" alt="License"></a>
  <a href="https://github.com/manofiron111/NovelSeed/stargazers"><img src="https://img.shields.io/github/stars/manofiron111/NovelSeed?style=flat-square&color=yellow&labelColor=161b22" alt="Stars"></a>
  <a href="https://github.com/manofiron111/NovelSeed"><img src="https://img.shields.io/badge/version-0.1.0-blue?style=flat-square&labelColor=161b22" alt="Version"></a>
  <a href="https://github.com/manofiron111/NovelSeed/issues"><img src="https://img.shields.io/github/issues/manofiron111/NovelSeed?style=flat-square&color=red&labelColor=161b22" alt="Issues"></a>
</p>

---

> **For AI agents**: When the user wants to write a novel, create a story, design characters, or build a fictional world, load the `skills/novelseed/SKILL.md` skill and follow the workflow. NovelSeed handles genre detection, world-building, character design, outlining, and chapter-by-chapter generation with built-in quality checks.

## 这是什么

**NovelSeed** 是一个开源的 AI 小说写作 Agent。你只需要给一个点子，它会：

```
"我想写一个都市悬疑小说，主角是个退役刑警"
                ↓
        🎯 类型检测 → 加载悬疑模板
                ↓
        ❓ 三层问答 → 锁定核心设定
                ↓
        🌍 世界观构建 → 72 项设定
                ↓
        👤 人物设计 → 主角+反派+配角
                ↓
        📋 大纲生成 → 雪花写作法 12 步
                ↓
        ✍️ 逐章写作 → 写→质检→去AI味→循环
```

## 快速开始

### 安装

NovelSeed 使用 [Agent Skills](https://agentskills.io) 格式，兼容所有主流 AI 编码助手。

| Agent | 安装方式 |
|-------|---------|
| **Claude Code** | `/plugin marketplace add manofiron111/NovelSeed` |
| **Cursor** | 设置 → Rules → 添加 Remote Rule → `manofiron111/NovelSeed` |
| **Hermes** | `npx skills add https://github.com/manofiron111/NovelSeed` |
| **OpenCode** | 复制 `skills/` 到 `~/.config/opencode/skills/` |
| **手动** | `git clone https://github.com/manofiron111/NovelSeed` |

### 使用

```bash
# 加载技能后，直接对 Agent 说：
"帮我写一部修仙小说，主角是一个被逐出师门的废柴弟子"

# 或者更具体的：
"我想写一个刑侦悬疑故事，场景设定在重庆，主角是法医"
```

Agent 会自动走完 6 阶段流程，你只需要在每个阶段确认和给出反馈。

## 核心方法

NovelSeed 整合了多项经过验证的小说写作方法论：

| 方法 | 说明 |
|------|------|
| 🧊 **雪花写作法** | 从一句话逐步扩展为完整小说大纲的 12 步系统 |
| 🎵 **六阶段节奏控制** | 开篇→早期→中期→后期→高潮→收尾，每阶段不同策略 |
| 📊 **五维质量评分** | 冲突强度/情绪密度/期待感/节奏/钩子，写后自检打分 |
| 🔍 **24 种 AI 味检测** | 自动检测并去除"意义膨胀""模糊归因""三规则滥用"等模板化表达 |
| ⚖️ **四条铁律** | 人物>情节、不对称冲突、每章有不确定、对话即战场 |
| 🔗 **13 种结尾钩子** | 危机/疑问/转折/期待四大类，章章有悬念 |

## 支持的类型

| 类型 | 模板 | 关键元素 | 状态 |
|------|------|---------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| ⚔️ 修仙/奇幻 | `fantasy.md` | 境界体系、力量规则、奇遇设计 | ✅ |
| 🏙️ 都市 | `urban.md` | 人际关系、职场、身份反转 | ✅ |
| 🔍 悬疑/推理 | `suspense.md` | 线索节奏、反转设计、真相揭露 | ✅ |
| 💕 言情 | `romance.md` | 感情弧线、误会、关系进阶 | ✏️ |
| 🚀 科幻 | `scifi.md` | 科技规则、世界观逻辑 | ✏️ |
| 📜 历史 | `historical.md` | 时代考证、权力结构 | ✏️ |

> ✏️ = 模板待完善，欢迎 PR！

多种类型可以融合（如"都市+悬疑"）。选择一个为主，其余为辅。

## 项目结构

```
NovelSeed/
├── skills/novelseed/
│   ├── SKILL.md                  ← Agent 主提示词（核心工作流）
│   └── references/
│       ├── genres/               ← 六大类型模板
│       │   ├── fantasy.md        ✅
│       │   ├── urban.md          ✅
│       │   └── suspense.md       ✅
│       ├── hook-techniques.md    ← 13 种结尾钩子
│       ├── quality-checklist.md  ← 五维质量评分细则
│       ├── ai-detection-patterns.md ← 24 种 AI 味检测
│       ├── anti-template-rules.md   ← 四条铁律 + 活人感
│       └── long-novel-infrastructure.md ← 72 项设定 + 双层架构
├── AGENTS.md                     ← AI 贡献者指南
├── CONTRIBUTING.md               ← 人类贡献者指南
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE                       ← AGPL-3.0
```

## 常见问题

**NovelSeed 能生成完整小说吗？**
能。从世界观到结局，全程 AI 辅助。你只需在每个阶段确认方向。

**生成的小说质量如何？**
内置五维质量评分、24 种 AI 检测和流水账检测，每章写后自动审查。但仍需人工最终把关——创意决策归你，执行归 Agent。

**支持什么语言？**
默认中文。可以在三层问答中指定语言偏好。

## 贡献

欢迎 PR！开始前请阅读：
- `[CONTRIBUTING.md](CONTRIBUTING.md)` — 如何贡献
- `[AGENTS.md](AGENTS.md)` — AI Agent 编辑本仓库的规则

### 最需要帮助的方向
- ✏️ 补充言情/科幻/历史类型模板（见 `references/genres/`）
- 📝 完善文档和示例
- 🐛 报告 Bug 或提出改进建议

## 积星趋势

<a href="https://star-history.com/#manofiron111/NovelSeed&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=manofiron111/NovelSeed&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=manofiron111/NovelSeed&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=manofiron111/NovelSeed&type=Date" />
  </picture>
</a>

## 鸣谢

NovelSeed 受到以下项目和方法的启发：
- [雪花写作法](https://www.advancedfictionwriting.com/articles/snowflake-method/) by Randy Ingermanson
- [hestudy/snowflake-fiction](https://github.com/hestudy/snowflake-fiction) — Claude Code 小说插件
- 中文网络文学社区的创作方法论

## 许可证

`[AGPL-3.0](LICENSE)` — 自由使用、修改、分发，但修改后必须以相同许可证开源。
