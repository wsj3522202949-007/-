---
id: tool-00926
type: tool
area: 库
status: active
tags: [RAG, Python, 协议宽松, 需API密钥, 英文文档, 人物设定]
title: Mini-HippoRAG
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/ankankar-zargon/mini-hipporag
created: 2026-07-18
updated: 2026-07-18
no: 926
category: 二、网文 / 长篇 AI 写作系统 库
repo: AnkanKar-Zargon/Mini-HippoRAG
stars: 1
url: https://github.com/ankankar-zargon/mini-hipporag
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: bd20e480a703c11c
  - methods/最强写作方法论_全球最强综合版.md
---

# AnkanKar-Zargon/Mini-HippoRAG

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ankankar-zargon/mini-hipporag
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Mini-HippoRAG is a smaller version of HippoRAG which is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents. RAG + Knowledge Graphs + Personalized PageRank. I added a different version of this here as my own implementation.
- **本地描述**：Mini-HippoRAG is a smaller version of HippoRAG which is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents. RAG + Knowledge Graphs + Personalized PageRank. I added a different version of this here as my own implementation.
- **拉取时间**：2026-07-23 23:06:04

---

# Mini-HippoRAG

Mini-HippoRAG is a smaller version of HippoRAG which is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents. RAG + Knowledge Graphs + Personalized PageRank. I added a different version of this here as my own implementation.

Minimal reimplementation of HippoRAG using the Groq API (free tier) for LLM calls and sentence-transformers for CUDA-accelerated local embeddings. Combines dense retrieval with a knowledge graph and personalized PageRank to answer multi-hop questions.

Retrieval score = 0.6 dense similarity + 0.4 PPR score

## Architecture
 
```
Indexing
 
Documents
    |
    +---> Sentence Embeddings  (BAAI/bge-small-en-v1.5, CUDA)
    |
    +---> OpenIE via Groq LLM
                |
                v
          Triples  (subject, relation, object)
                |
                v
          Knowledge Graph  (networkx)
 
Query time
 
Query
    |
    +---> Query Embedding
    |         |
    |         v
    |     Cosine similarity against all doc embeddings   -> dense score
    |
    +related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---> Entity similarity to find KG seed nodes
              |
              v
          Personalized PageRank over KG                  -> graph score
 
combined score = dense score * 0.6 + graph score * 0.4
    |
    v
Top-k documents
    |
    v
Groq LLM reads context and answers the question
```

## Setup

```bash
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
```

## Quickstart

```bash
# Sample dataset (9 docs, instant)
python run.py --dataset sample --reindex

# HotpotQA (150 docs, multi-hop benchmark)
python prepare_data.py --source hotpotqa
python run.py --dataset hotpotqa --reindex

# Limit queries for a fast test
python run.py --dataset hotpotqa --max_queries 10
```

## Models

llama-3.1-8b-instant is the default and works best on the free tier at 30 requests per minute. gemma2-9b-it is a good alternative. Reasoning models such as deepseek-r1-distill-llama-70b are supported and think blocks are stripped automatically before scoring.

```bash
python run.py --dataset sample --llm_model gemma2-9b-it
```

## Data Format

Corpus file at data/source/corpus.json:

```json
[{"title": "...", "text": "...", "idx": 0}]
```

Queries file at data/source/queries.json:

```json
[{"id": "q1", "question": "...", "answers": ["..."], "supporting_doc_ids": [0, 1]}]
```

Each dataset writes to its own subdirectory so sample and hotpotqa never overwrite each other.

## Outputs

Each dataset produces files under outputs/source/ and plots/source/.

outputs/source/index.pkl stores the knowledge graph and embeddings and is reused on subsequent runs. outputs/source/results.json contains all metrics and per-query answers. plots/source/ contains dashboard.png, knowledge_graph.png, retrieval_metrics.png, qa_metrics.png, and score_distribution.png.

## Evaluation

Retrieval: P@k, R@k, nDCG@k for k in 1 3 5, MRR, F1. Queries with no supporting docs are skipped rather than penalising the system.

QA: Exact Match and token-level F1 following the SQuAD convention. Common LLM verbal wrappers such as "The answer is" are stripped before scoring.

## Token Budget

Every LLM call is counted against a 100k token limit. Document texts are truncated to 700 characters before OpenIE. QA context is capped at 1400 characters. The index is cached after the first run so LLM calls only happen once per corpus.

## File Structure

```
hipporag-groq/
├── hipporag_groq.py    core engine: indexing, KG, PPR, retrieval, QA
├── evaluation.py       retrieval and QA metrics
├── visualize.py        plots
├── run.py              CLI runner, dataset-aware
├── prepare_data.py     downloads and converts datasets
├── data/
│   ├── sample/         9-doc toy corpus
│   └── hotpotqa/       150-doc multi-hop corpus after prepare_data.py
└── requirements.txt
```

## References

Gutierrez, B. J., Shu, Y., Gu, Y., Yasunaga, M., and Su, Y. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models. Advances in Neural Information Processing Systems, 2024. https://arxiv.org/abs/2405.14831

Gutierrez, B. J., Shu, Y., Qi, W., Zhou, S., and Su, Y. From RAG to Memory: Non-Parametric Continual Learning for Large Language Models. ICML, 2025. https://arxiv.org/abs/2502.14802

Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W., Salakhutdinov, R., and Manning, C. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. EMNLP, 2018. https://arxiv.org/abs/1809.09600
