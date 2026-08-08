---
id: tool-01392
type: tool
area: 库
status: active
tags: [RAG, 大纲规划, Python, 协议未明, 需API密钥, 中文友好, 人物设定]
title: novel-agent
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/xzstar/novel-agent
created: 2026-07-18
updated: 2026-07-18
no: 1392
category: 二、网文 / 长篇 AI 写作系统 库
repo: xzstar/novel-agent
stars: 0
url: https://github.com/xzstar/novel-agent
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6296006e7439d983
  - methods/最强写作方法论_全球最强综合版.md
---

# xzstar/novel-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xzstar/novel-agent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered novel writing system with LangChain + LangGraph. Three-tier memory, dual RAG (Vector + Temporal Graph), self-correction loop.
- **本地描述**：AI-powered novel writing system with LangChain + LangGraph. Three-tier memory, dual RAG (Vector + Temporal Graph), self-correction loop.
- **拉取时间**：2026-07-23 23:19:43

---

# novel-agent

基于 LangChain + LangGraph 的 AI 长篇小说写作系统，融合三层记忆、双 RAG（向量检索 + 时序知识图谱）和自校正循环，专为中文玄幻/仙侠类长篇小说设计。

## 核心特性

- **三层 Memory 系统**：短期（滑动窗口）+ 中期（章节摘要）+ 长期（向量库），避免长篇小说后期"遗忘"前期设定
- **双 RAG 并行检索**：
  - `VectorRAG`（FAISS）负责语义关联召回
  - `TemporalGraphRAG`（时序知识图谱）负责时序关联，可区分"第3章是敌人"和"第20章成为盟友"
- **双知识库**：剧情内容库（已写内容）+ 外部知识库（修仙设定、术语、人物原型参考）
- **自校正循环**：`ConsistencyChecker` 检查新内容与历史设定的一致性，对高严重性问题触发 `auto_fix` 重写（最多 3 次重试，避免死循环）
- **多写作风格**：内置 `古典仙侠`、`热血玄幻`、`轻松修仙`，可在 `config.yaml` 中扩展
- **可恢复写作**：通过 `--resume` 从指定卷/章继续，已写章节自动跳过

## 架构

```
main.py → WritingWorkflow (LangGraph)
    ├── generate_outline   # 生成全书大纲
    ├── plan_chapter       # 单章细纲规划
    ├── write_chapter      # 正文生成（双 RAG + 三层记忆）
    ├── check_consistency  # 一致性检查 + auto_fix
    ├── update_knowledge   # 更新知识库/图谱/记忆
    └── save_chapter       # 持久化
```

| 层 | 模块 | 作用 |
|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 三层记忆 | `src/memory/` | 短期对话、中期章节摘要、长期向量库 |
| 双 RAG | `src/rag/` | VectorRAG（语义）+ TemporalGraphRAG（时序） |
| 时序图谱 | `src/graph/` | `TemporalKnowledgeGraph` 追踪实体关系演变 |
| 知识库 | `src/knowledge/` | `PlotKnowledgeBase` + `ExternalKnowledgeBase` |
| 写作 Agent | `src/agent/` | OutlinePlanner / ChapterPlanner / NovelWriter / ConsistencyChecker |
| LLM 客户端 | `src/llm/` | `ARKClient`（火山引擎 ARK，OpenAI 兼容） |

## 快速开始

### 1. 安装依赖

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env：填入火山引擎 ARK API Key
#   ARK_API_KEY=你的真实APIKey
#   HF_ENDPOINT=https://hf-mirror.com   # 国内必设，用于下载 embedding 模型
```

在 [火山引擎 ARK 控制台](https://console.volcengine.com/ark) 创建推理接入点（模型推荐 `doubao-pro-4k` 或 `doubao-lite-4k`），将 Endpoint ID 填入 `config.yaml` 的 `llm.model` 字段。

### 3. 下载 Embedding 模型（可选）

默认使用本地 `bge-small-zh-v1.1` 模型。首次运行时若 `data/embedding_model/` 不存在，会自动从 HuggingFace 镜像下载，也可手动执行：

```bash
python download_model.py
```

### 4. 运行

```bash
# 完整写作（生成大纲 + 全部章节）
python main.py --title "幽明照海录" --genre "玄幻" --style "古典仙侠"

# 只生成大纲
python main.py --title "幽明照海录" --outline-only

# 测试单章（保存大纲到 output/outline.json，章节到 output/第N卷/）
python main.py --title "幽明照海录" --test-chapter --volume 1 --chapter 1

# 从指定卷/章继续
python main.py --title "幽明照海录" --resume --volume 1 --chapter 10
```

## 配置说明

编辑 `config.yaml`：

- `llm`：LLM 模型/Endpoint、温度、超时
- `memory`：三层记忆窗口大小、摘要间隔、向量库路径
- `knowledge`：剧情库与外部知识库的分块参数
- `temporal_graph`：时序图谱存储路径
- `workflow.outline`：总卷数、每卷章数、每章字数
- `embedding`：可选 `huggingface`（本地）或 `ark`（API）

## 数据持久化

- `output/第N卷/第XXX章_标题.md` - 生成章节
- `output/outline.json` - 大纲
- `output/stats.json` - 写作统计
- `data/vector_stores/` - FAISS 索引（自动创建）
- `data/temporal_graph/` - 时序图谱 JSON（自动创建）
- `data/plot_summaries/` - 章节摘要

## 添加新写作风格

编辑 `src/agent/writer.py` 的 `WRITING_STYLES`：

```python
"your_style": {
    "style": "文笔描述",
    "vocabulary": "关键词1, 关键词2",
    "dialogue": "对话风格描述",
},
```

运行时通过 `--style your_style` 指定。

## 技术栈

- LangChain + LangGraph - Agent 编排
- langchain-openai - LLM 集成（火山引擎 ARK，OpenAI 兼容协议）
- faiss-cpu - 向量检索
- networkx - 时序知识图谱
- sentence-transformers - 中文 embedding（`BAAI/bge-small-zh-v1.1`）

## License

MIT
