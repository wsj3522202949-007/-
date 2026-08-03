---
id: tool-07494
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: recommender-engine
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/pratikmakune3/recommender-engine
created: 2026-07-18
updated: 2026-07-18
no: 7494
category: 画龙补充 / 扩容入库 — 补充源
repo: pratikmakune3/recommender-engine
stars: 0
url: https://github.com/pratikmakune3/recommender-engine
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# pratikmakune3/recommender-engine

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/pratikmakune3/recommender-engine
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A simple book recommender engine built using sentence transformer
- **本地描述**：recommender-engine
- **拉取时间**：2026-07-25 19:23:36

related:
  - methods/QUICK_START.md
---

## Book Recommendation System (Streamlit + Sentence-Transformers)

A minimal semantic similarity demo that recommends books based on embeddings from `all-MiniLM-L6-v2`. The UI is built with Streamlit. Pick a book, and the app suggests similar titles using cosine similarity over sentence embeddings.

## Features

- **Interactive UI**: built with Streamlit
- **Semantic search**: `sentence-transformers` + `all-MiniLM-L6-v2`
- **Similarity metric**: `scikit-learn` cosine similarity

## Prerequisites

- Python 3.10–3.12
- macOS/Linux/Windows

## Setup

```bash
# 1) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 2) Upgrade pip and install dependencies
python -m pip install -U pip wheel
pip install streamlit sentence-transformers scikit-learn "numpy<2"
# Optional: faster file watching for Streamlit (macOS)
# xcode-select --install
# pip install watchdog
```

## Run the app

```bash
source .venv/bin/activate
streamlit run rag_streamlit.py
```

- The first run downloads the model (~100 MB).
- Streamlit will print a URL like `http://localhost:8501` (or another available port). Open it in your browser.

## Troubleshooting

- **NumPy 2.x compatibility**: If you see errors like “A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x” or “RuntimeError: Numpy is not available”, pin NumPy 1.x:

```bash
pip install "numpy<2"
```

- **Port already in use**: Run Streamlit on a different port:

```bash
streamlit run rag_streamlit.py --server.port 8502
```

- **Slow first run**: Model download happens once and is cached.
