---
id: tool-07527
type: tool
area: 库
status: active
tags: [Claude插件, Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: webnovel-writer-opencode
summary: Claude Code 插件式写作流
source: https://github.com/saemer2023/webnovel-writer-opencode
created: 2026-07-18
updated: 2026-07-18
no: 7527
category: 画龙补充 / 扩容入库 — 补充源
repo: saemer2023/webnovel-writer-opencode
stars: 2
url: https://github.com/saemer2023/webnovel-writer-opencode
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4e1f754c07e7c3bd
  - methods/QUICK_START.md
---

# saemer2023/webnovel-writer-opencode

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/saemer2023/webnovel-writer-opencode
- **Stars**：2
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：ai-writing, novel-writing, opencode, web-fiction, webnovel
- **GitHub 描述**：本项目是基于webnovel-writer 改编的 OpenCode 版本，目标是让用户在OpenCode 使用长篇网文创作系统，解决 AI 写作中的「遗忘」和「幻觉」问题，支持 200 万字量级 连载创作。
- **本地描述**：webnovel-writer-opencode
- **拉取时间**：2026-07-25 19:24:38

---

# Webnovel Writer for OpenCode

[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-purple)](https://opencode.ai)

> 基于 OpenCode 的长篇网文 AI 创作系统——降低 AI 写作中的「遗忘」和「幻觉」，支持 200 万字量级连载创作。

---

## 特性一览

| 特性 | 说明 |
|------|------|
| **完整写作工作流** | 项目初始化 → 大纲规划 → 章节写作 → 审查润色 → 发布 |
| **RAG 上下文管理** | 智能检索相关设定、角色、伏笔，保持长篇一致性 |
| **10 个写作技能** | 覆盖从 init 到 publish 的全流程 |
| **6 个专用 Agent** | 上下文搜集、数据处理、一致性审查、连贯性审查等 |
| **多维度质量检查** | 设定一致性、OOC、爽点密度、节奏控制、追读力 |
| **37+ 题材模板** | 修仙、都市、宫斗、悬疑等主流网文题材 |
| **Dashboard 可视化** | 实时查看项目状态、角色状态、伏笔追踪 |
| **一键发布番茄** | 浏览器自动化登录，HTTP API 直接上传章节 |
| **多种导出格式** | EPUB / TXT / JSON / Markdown |
| **版本隔离机制** | `upstream/` 只读源 + `sync-upstream.ps1` 同步，可追踪上游变更 |
| **批量写作** | 连续撰写多章节，断点自动保存 |
| **中断恢复** | 精确的工作流状态追踪，安全恢复 |

---

## 快速开始

### 前置条件

- [OpenCode](https://opencode.ai) 已安装并配置
- Python 3.10+
- Git

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/Saemer2023/webnovel-writer-opencode.git
cd webnovel-writer-opencode

# 2. 运行交互式安装（推荐）
python install.py
```

交互菜单自动检测安装状态，支持：

| 操作 | 命令 |
|------|------|
| Install / Update | `python install.py`（无参数） |
| 增量更新 | `python install.py --incremental` |
| 清洁安装 | `python install.py --clean` |
| 卸载 | `python install.py --uninstall` |
| 仅虚拟环境 | `python install.py --venv` |

> 中国大陆用户自动使用 GitHub 镜像 + PyPI 清华镜像加速。

### 开始使用

在 OpenCode 中打开项目目录，按阶段使用技能命令：

**第一阶段：初始化 + 大纲**

```bash
/webnovel-init              # 创建新项目
/webnovel-plan 1            # 规划第 1 卷大纲
```

**第二阶段：写作循环（逐章）**

```bash
/webnovel-write 1           # 写第 1 章
/webnovel-write 2           # 写第 2 章
/webnovel-write 3           # ... 逐章写下去
/webnovel-write-batch 4-10  # 或批量写 4-10 章
```

**第三阶段：审查 + 导出 + 发布**

```bash
/webnovel-review 1-5        # 审查前 5 章
/webnovel-export            # 导出正文
/webnovel-publish           # 发布到番茄小说
```

**辅助命令：**

```bash
/webnovel-query 角色名       # 查询设定
/webnovel-dashboard         # 打开可视化看板
/webnovel-learn             # 从已有章节提取写作模式
```

---

## 工作流程

```
项目初始化 (/webnovel-init)
    │
    ▼
大纲规划 (/webnovel-plan)
    │
    ▼
章节写作 (/webnovel-write)
    ├─→ context-agent 搜集上下文
    ├─→ 撰写章节正文
    ├─→ 多维度审查（6 个检查器）
    └─→ data-agent 更新索引 + 事件溯源
    │
    ▼
审查润色 (/webnovel-review)
    │
    ▼
发布上线 (/webnovel-publish / webnovel-export)
```

---

## Skills（10 个）

| 命令 | 说明 |
|------|------|
| `/webnovel-init` | 深度初始化网文项目，收集创作信息生成项目骨架 |
| `/webnovel-plan` | 构建卷纲和章节大纲，继承创意约束 |
| `/webnovel-write` | 撰写章节，支持 `--fast` 和 `--minimal` 模式 |
| `/webnovel-write-batch` | 批量写作多章节，断点恢复 |
| `/webnovel-review` | 使用检查器审查章节质量 |
| `/webnovel-export` | 导出正文为 MD / TXT / EPUB / JSON |
| `/webnovel-publish` | 发布章节到番茄小说平台 |
| `/webnovel-dashboard` | 可视化看板，卷结构 / 角色状态 / 伏笔追踪 |
| `/webnovel-query` | RAG 查询项目设定、角色、伏笔 |
| `/webnovel-learn` | 从当前会话提取可复用写作模式 |

---

## Agents（6 个）

| Agent | 说明 |
|-------|------|
| `context-agent` | 上下文搜集，生成创作执行包供写作直接使用 |
| `data-agent` | 数据处理，实体提取、场景切片、索引构建 |
| `chapter-writer-agent` | 正文起草，生成 3000-5000 字高质量章节 |
| `consistency-checker` | 设定一致性检查，战力 / 地点 / 时间线 / 实体 |
| `continuity-checker` | 连贯性检查，场景过渡、伏笔管理 |
| `ooc-checker` | 人物 OOC 检查，防止角色行为与人设冲突 |
| `high-point-checker` | 爽点密度检查，支持迪化误解 / 身份掉马模式 |
| `pacing-checker` | Strand Weave 节奏检查，防止读者疲劳 |
| `reader-pull-checker` | 追读力检查，评估钩子 / 微兑现 / 约束分层 |

---

## 项目结构

```
webnovel-writer-opencode/
├── .opencode/              # OpenCode 配置（核心）
│   ├── agents/             # Agent 定义
│   ├── skills/             # 10 个写作技能
│   ├── scripts/            # 30+ Python 工具脚本
│   ├── genres/             # 37+ 题材模板
│   ├── references/         # 写作参考（类型规则、核心约束）
│   ├── templates/          # 输出模板
│   ├── installer/          # 安装脚本
│   └── dashboard/          # 可视化看板前端
├── config/                 # 项目配置
│   └── upstream-delta.md   # 同步变更记录
├── install.py              # 交互式安装脚本（推荐）
├── install.ps1             # Windows 安装代理脚本
├── install.sh              # macOS/Linux 安装代理脚本
├── scripts/                # 工具脚本
│   ├── sync-upstream.ps1   # 上游同步脚本
│   └── convert-upstream.ps1# 格式转换脚本
├── upstream/               # 只读源（上游原始版本）
├── docs/                   # 文档
├── LICENSE                 # GPL v3
└── README.md
```

---

## 版本隔离说明

本项目采用 **upstream/ + .opencode/** 双目录结构：

- **`upstream/`** — 只读目录，保留上游（lingfengQAQ/webnovel-writer）的原始版本
- **`.opencode/`** — 工作目录，包含所有 lujih 特有文件和适配层
- **`scripts/sync-upstream.ps1`** — 自动同步上游变更，保护本地特有文件不被覆盖

当上游发布新版本时：
```powershell
# Windows
.\scripts\sync-upstream.ps1

# 脚本会自动：
# 1. 拉取上游最新代码
# 2. 保留本地特有文件（publisher/、export_manager/ 等）
# 3. 适配 agent frontmatter 格式差异
```

---

## 审查器系统

章节写作后经过 6 个维度审查：

1. **设定一致性** — 战力 / 道具 / 时间线一致性
2. **连贯性** — 场景过渡、伏笔管理
3. **OOC** — 角色行为与人设一致性
4. **爽点密度** — 追读动力评估
5. **节奏控制** — 读者疲劳预防
6. **追读力** — 钩子 / 微兑现 / 约束分层

---

## 技术栈

- **平台**: OpenCode
- **语言**: Python 3.10+
- **存储**: SQLite (RAG), JSON (状态/大纲), Markdown (正文/设定)
- **前端**: FastAPI + React 19 + ECharts (Dashboard)
- **RAG**: BM25 + Embedding + Re-ranker
- **导出**: python-epub-creator / Markdown / TXT / JSON

---

## 版权与许可

本项目基于 [GNU General Public License v3](https://github.com/saemer2023/webnovel-writer-opencode/blob/main/LICENSE) 发布。

### 衍生说明

本项目衍生于以下上游项目，在此表示感谢：

- **[lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)** (GPL v3) — 原版 Claude Code 网文创作系统
- **[lujih/webnovel-writer-opencode](https://github.com/lujih/webnovel-writer-opencode)** (GPL v3) — OpenCode 移植版

### 主要修改

相对于上游，本项目的主要变更：
- OpenCode 平台适配（`webnovel-writer-skill-install.sh` → `.opencode/` 架构）
- `install.py` 交互式安装（跨平台菜单，支持 --update/--clean/--uninstall）
- 版本隔离机制（`upstream/` 只读源 + `sync-upstream.ps1` 同步）
- 新增 `export_manager/` 子包（EPUB/TXT/JSON/MD 导出）
- 新增 `publisher/` 子包（番茄小说平台发布）
- 新增 `gen_manifest.py`（批量 manifest 生成）
- 新增 `webnovel-export` / `webnovel-publish` / `webnovel-write-batch` 技能
- 新增 `chapter-writer-agent.md`（正文起草 subagent）
- Agent frontmatter 格式适配（`convert-upstream.ps1`）
- 测试全绿（36/36）

related:
  - methods/QUICK_START.md
---

## 相关项目

- [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) — 原版 Claude Code 插件
- [lujih/webnovel-writer-opencode](https://github.com/lujih/webnovel-writer-opencode) — OpenCode 移植版
- [wmzy/opencode-novel-plugin](https://github.com/wmzy/opencode-novel-plugin) — OpenCode 小说创作插件
- [Narcooo/inkos](https://github.com/Narcooo/inkos) — 自主小说写作 AI Agent
