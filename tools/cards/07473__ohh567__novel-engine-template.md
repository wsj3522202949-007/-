---
id: tool-07473
type: tool
area: 库
status: active
tags: [多Agent, 大纲规划, Python, 协议宽松, 需API密钥, 中文友好]
title: novel-engine-template
summary: 多 Agent 协作自动产文
source: https://github.com/ohh567/novel-engine-template
created: 2026-07-18
updated: 2026-07-18
no: 7473
category: 画龙补充 / 扩容入库 — 补充源
repo: ohh567/novel-engine-template
stars: 4
url: https://github.com/ohh567/novel-engine-template
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: b14cefae6f856e7c
  - methods/QUICK_START.md
---

# ohh567/novel-engine-template

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ohh567/novel-engine-template
- **Stars**：4
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI multi-agent novel writing engine template
- **本地描述**：novel-engine-template
- **拉取时间**：2026-07-25 19:22:58

related:
  - methods/QUICK_START.md
---

# Novel Engine Template

一个可 fork 的中文长篇小说 AI 写作引擎模板。核心流程是：

`Director 章节设计 → Writer 初稿 → Critic 评审 → Patch Reviser 局部修订 → Quality Gate → Archivist 更新状态库`

## 适合做什么

- 写长篇网文/类型小说，保持章节连续性。
- 用 `state_db/` 保存角色状态、世界规则、最近章节、伏笔。
- 每章从 `plot/vol*/act*.md` 读取单章节拍，自动组装不同 Agent 需要的上下文。
- Critic 不通过时优先做局部 patch 修订，避免整章重抽卡导致设定漂移。

## 快速开始

```bash
git clone https://github.com/<your-name>/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate
pip install -r engine/requirements.txt
cp .env.example .env
```

编辑 `.env`，填入你的 OpenAI 兼容接口配置：

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export NOVEL_ENGINE_MODEL="gpt-4o"
```

也可以直接在命令前传环境变量：

```bash
OPENAI_API_KEY="your-api-key" OPENAI_BASE_URL="https://api.openai.com/v1" NOVEL_ENGINE_MODEL="gpt-4o" python -m engine.main_orchestrator --chapter 1
```

## 写自己的小说

你需要先改这些文件：

- `state_db/characters.json`：角色卡与当前状态
- `state_db/world_lore.json`：世界规则
- `state_db/plot_timeline.json`：当前总摘要、最近章节、伏笔
- `plot/vol1/outline.md`：第一卷大纲
- `plot/vol1/act1.md`：每章节拍
- `agents/*.md`：如果你的题材不同，可以调整 Agent 规则

然后生成章节：

```bash
python -m engine.main_orchestrator --chapter 1
```

常用参数：

- `--outline "..."`：直接传入本章大纲，不从 plot 读取。
- `--no-state-update`：只保存正文，不更新 `state_db/`；适合回修旧章。
- `--no-director`：跳过 Director，只让 Writer 写。
- `--no-patch-revision`：Critic 不通过时禁用局部 patch，直接完整修订。
- `--no-archivist-evidence`：Archivist 使用整章正文，不使用证据段落裁剪。
- `--strict-quality`：Quality Gate 出现 ERROR 时中断保存。
- `--push-github`：生成成功后只提交并推送本章正文。

## 目录结构

```text
agents/       Agent 系统提示词
engine/       Python 编排引擎
state_db/     动态状态库
plot/         分卷大纲和章节节拍
chapters/     生成后的正文
summary/      章节摘要
writing/      写作规范/参考
```

## 注意

- 不要把 `.env`、真实 API key、私人正文备份提交到公开仓库。
- 公开模板默认只包含示例状态和示例大纲，不包含任何私有小说正文。
- 这是 OpenAI SDK 兼容接口；只要服务支持 `/v1/chat/completions` 一般都能用。
