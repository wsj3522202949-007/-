---
id: tool-00997
type: tool
area: 库
status: active
tags: [RAG, 协议宽松, 需API密钥, 英文文档, 人物设定]
title: writers-assistant
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/writer-in-fancy-pants/writers-assistant
created: 2026-07-18
updated: 2026-07-18
no: 997
category: 二、网文 / 长篇 AI 写作系统 库
repo: writer-in-fancy-pants/writers-assistant
stars: 0
url: https://github.com/writer-in-fancy-pants/writers-assistant
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# writer-in-fancy-pants/writers-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/writer-in-fancy-pants/writers-assistant
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A comprehensive knowledge extraction, understanding, and generation tool to assist creative writing.
- **本地描述**：A comprehensive knowledge extraction, understanding, and generation tool to assist creative writing.
- **拉取时间**：2026-07-23 23:08:06

---

# 🧙 Lore Engine

A pipeline for extracting structured world-building data from unstructured text, building a knowledge graph + vector database, and generating new story chapters using all accumulated context.

---

## Project Structure

```
lore_engine/
├── data/
│   ├── raw/              # Your source .txt files go here
│   ├── entities/         # Extracted YAML entity files
│   └── output/           # Generated chapters
├── scripts/
│   ├── 01_extract_entities.py     # Entity/lore extraction → YAML
│   ├── 02_build_knowledge_graph.py # Build Neo4j-style graph + NetworkX
│   ├── 03_build_vector_db.py       # Embed text chunks → ChromaDB
│   └── 04_generate_chapter.py      # Multi-step chapter generation
├── config/
│   └── settings.yaml     # API keys, model config, paths
├── requirements.txt
└── README.md
```

---

## Setup

```bash
pip install -r requirements.txt
```

Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

Or put it in `config/settings.yaml`.

---

## Pipeline

### Step 1 — Extract Entities & Lore

```bash
python scripts/01_extract_entities.py --input data/raw/
```

Outputs YAML files to `data/entities/`:
- `characters.yaml`
- `locations.yaml`
- `factions.yaml`
- `lore.yaml`
- `summary.yaml`

### Step 2 — Build Knowledge Graph

```bash
python scripts/02_build_knowledge_graph.py
```

Reads entity YAMLs, builds a NetworkX knowledge graph, saves as:
- `data/output/knowledge_graph.json` (node-link format)
- `data/output/knowledge_graph.png` (visualization)

### Step 3 — Build Vector Database

```bash
python scripts/03_build_vector_db.py
```

Chunks raw text + entity descriptions, embeds them, stores in ChromaDB at `data/output/chroma_db/`.

### Step 4 — Generate Next Chapter

```bash
python scripts/04_generate_chapter.py \
  --previous_chapter data/output/chapter_01.txt \
  --instructions "The hero discovers the betrayal. Tension, rain, cliffhanger ending." \
  --output data/output/chapter_02.txt
```

Uses a **5-step generation pipeline**:
1. Retrieve relevant context from vector DB
2. Extract relevant graph relationships
3. Draft story beats / outline
4. Write the full chapter draft
5. Refine for consistency and style

---

## Entity YAML Format

### characters.yaml
```yaml
characters:
  - name: Aelindra Voss
    aliases: [The Pale Warden, Aeli]
    role: protagonist
    description: A former inquisitor haunted by her past.
    traits: [stoic, perceptive, ruthless when cornered]
    affiliations: [The Silver Accord]
    locations_visited: [Thornwall, The Ash Wastes]
    relationships:
      - character: Drevok
        type: rival
        notes: Old mentor turned adversary
    first_appeared: chapter_01
    status: alive
```

### locations.yaml
```yaml
locations:
  - name: Thornwall
    type: city
    description: A fortress city on the edge of the Ash Wastes.
    factions_present: [The Silver Accord, The Ember Court]
    notable_features: [The Obsidian Gate, Warden's Spire]
    connected_to: [The Ash Wastes, Deepmere]
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Tips

- Drop multiple `.txt` files into `data/raw/` — the extractor handles them all and merges entities intelligently.
- Re-run `01_extract_entities.py` after adding new chapters to keep entities up to date.
- The vector DB is **persistent** — re-running `03_build_vector_db.py` adds new content without duplication.
- Pass `--verbose` to any script for detailed logging.
