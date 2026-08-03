---
id: tool-00271
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 中文友好]
title: AI-Driven-Novel-Writing-Copilot
summary: 多 Agent 协作自动产文
source: https://github.com/chien6354/ai-driven-novel-writing-copilot
created: 2026-07-18
updated: 2026-07-18
no: 271
category: 二、网文 / 长篇 AI 写作系统 库
repo: Chien6354/AI-Driven-Novel-Writing-Copilot
stars: 0
url: https://github.com/chien6354/ai-driven-novel-writing-copilot
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Chien6354/AI-Driven-Novel-Writing-Copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/chien6354/ai-driven-novel-writing-copilot
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Driven Novel Writing Copilot
- **本地描述**：AI-Driven Novel Writing Copilot
- **拉取时间**：2026-07-23 22:46:59

---

# AI 写作助手（多 Agent 长篇小说流水线）

> 基于 v1.3 PRD 的全栈实现：FastAPI + LangGraph 多 Agent 后端，React + Antd 前端。

## 技术栈

| 层 | 选型 |
|----|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 后端 | Python 3.11 + FastAPI + SQLAlchemy 2 + Alembic + Celery + LangChain + LangGraph |
| 前端 | React 18 + TypeScript + Vite + Ant Design 5 + ECharts |
| 关系数据库 | MySQL 8.0（用户、书籍、章节元数据、埋点、点踩反馈、Prompt 版本） |
| 文档数据库 | MongoDB 7（Truth MD 全文、章节正文、Agent IO 快照、章节摘要） |
| 缓存/队列 | Redis 7 |
| 大模型 | DeepSeek（OpenAI 兼容） |

## 快速开始

### 1. 起依赖容器

```bash
cd backend
docker-compose up -d   # MySQL 3306 / Mongo 27017 / Redis 6379
```

### 2. 后端

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate         # Windows PowerShell
# source .venv/bin/activate    # macOS / Linux
pip install -r requirements.txt

cp .env.example .env
# 编辑 .env，填入 DEEPSEEK_API_KEY；MySQL/Mongo/Redis 默认指向 docker-compose

alembic upgrade head                                # 建表
python -m app.scripts.seed_prompts                  # 把 prompts/ 入库 + 创建管理员
uvicorn app.main:app --reload --port 8000           # API 服务
celery -A app.tasks.celery_tasks worker -l info     # 异步流水线
```

### 3. 前端

```bash
cd frontend
pnpm install   # 或 npm install
pnpm dev       # http://localhost:5173
```

## 目录结构

```
backend/
  app/
    main.py                     FastAPI 入口
    core/                       config / db / security / deps
    api/v1/                     auth / books / chapters / truth / feedback / prompts / admin
    models/                     SQLAlchemy ORM
    schemas/                    Pydantic
    services/                   prompt_loader / tracking / snapshot / memory
    agents/                     base / llm / constructor / writer / reviewer / reviser
      graphs/                   truth_init / truth_rebuild / preflight / chapter_pipeline / revision_loop
    tasks/                      Celery 任务
    scripts/                    seed_prompts 等运维脚本
  prompts/
    registry.yaml               template_key → file_path + version
    agents/                     10 个 Agent 模板
    genre/public/               预置公共题材（玄幻 / 都市 / 仙侠 / 都市异能 / 惊悚）
    global/system.baseline.md   全局底线
  alembic/                      数据库迁移
  docker-compose.yml            MySQL + MongoDB + Redis

frontend/
  src/
    pages/
      Login / Register
      Bookshelf                 我的书架
      BookInit                  初始化向导（弹窗外侧反馈区）
      BookWorkspace/            单书三子 Tab：章节列表 / 设定文件 / 统计
      ChapterCreate             含关键事件预审分支
      ChapterView               终稿 + 折叠展开各 Agent + 修订循环
      GenreManagement           题材管理（双 Tab：公共 / 我的）
      UserCenter
      Admin/                    管理员看板
    components/
      AgentStepCard             单步可视化卡片（含点踩点赞）
      PipelineProgress          SSE 实时进度
      MarkdownEditor
```

## 三个核心设计

### 1. 多 Agent 编排（LangGraph）

5 个 StateGraph：

- `truth_init` 建构师并发生成 9 个 Truth MD
- `truth_rebuild` 维持关键事件 → 重构受影响 MD
- `preflight` 关键事件预审
- `chapter_pipeline` 建构师 → 写手 → 审计员 ↔ 修订者（带最大轮次）
- `revision_loop` 终稿后用户修订意见循环（仅 reviewer ↔ reviser）

每个 Agent 节点经过 `BaseAgent` 装饰器统一埋点，自动写入 `agent_steps` 表 + MongoDB IO 快照 + SSE 推送。

### 2. Prompt 全外置（PRD §12）

- 业务代码只持有 `template_key`
- `prompts/registry.yaml` 维护 `template_key → 文件路径 + 默认模型`
- `services/prompt_loader.py` 启动入库到 `prompt_versions` 表，运行时按需取最新激活版本
- 每次调用记录 `prompt_version` + `prompt_bundle_hash`，便于 A/B 与回放

### 3. 管理员 Badcase 复盘

`/admin` 路由独立鉴权：

- 概览：每 Agent 平均耗时/Token、首审通过率、点踩率
- **Badcase 复盘页**：列表筛选 → 单条下钻 → 看 prompt 渲染全文 + Agent 输入输出 + 模板版本
- 公共题材管理：创建 / 发布 / 下线 / 版本历史

## 关键约束

- 已发布章节正文不可改；章节摘要写入即锁
- 题材 Prompt：公共由管理员发布，公共与私有可同名，靠 `[公共]` / `[私有]` 徽章区分
- 计费：**不做**，注册即无限使用，token/cost 仅供成本可观测
