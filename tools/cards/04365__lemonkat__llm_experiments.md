---
id: tool-04365
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 人物设定, RAG]
title: llm_experiments
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/lemonkat/llm_experiments
created: 2026-07-18
updated: 2026-07-18
no: 4365
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: lemonkat/llm_experiments
stars: 1
url: https://github.com/lemonkat/llm_experiments
tier: "B"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# lemonkat/llm_experiments

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/lemonkat/llm_experiments
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI agents that use embedding-based memory system to emulate social interactions and test character memories
- **本地描述**：AI agents that use embedding-based memory system to emulate social interactions and test character memories
- **拉取时间**：2026-07-25 17:44:30

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

LemonKat's LLM experiments

These are a couple experiments using GPT-3 and GPT-4’s APIs to emulate conversations between fictional characters using multiple LLM agents with associated character memories. 

I created a wrapper function so the actual LLM can be swapped out to test the responses of multiple commercial and open-source LLMs.

Inspired by the paper [_Generative Agents: Interactive Simulacra of Human Behavior_](https://arxiv.org/abs/2304.03442).

Each persona object carries a set of memories of recent events or things they know. When each persona responds, it recalls relevant memories, and sends those along with the conversation history to GPT-4 to generate a response.

To recall relevant memories for a given query, the system assigns each memory a "score", calculated as the sum of:
1. The "importance" of the memory, on a scale from 0.1 to 1.0, given by GPT-3.
2. The "recency" of the memory, which is 1.0 when it is created, and exponentially decays over time.
3. The "relevance" of the memory, which is the cosine similarity between the emebdding vectors of the memory and query.
The recall algorithm picks the top 10 memories with the highest score, and passes those to GPT-4 to produce the response.

For example, take the following conversation between me and a video game character, called Raiden (from Genshin Impact). In-lore, Raiden cannot cook, and this fact is represented in one of her persona's memories. When I ask Raiden whether or not she can cook, the recall algorithm pulls up the relevant memory, and informs GPT-4 to respond that she cannot cook. This all works despite the Raiden persona storing over 50 large memories.


> LemonKat: can you cook?  
> Raiden: I do not possess culinary skills. My focus lies elsewhere, in the governance of Inazuma and the pursuit of eternity. However, I am intrigued by the art of dessert making and its required patience.

To run:
1. create a `.env` file with `OPENAI_API_KEY` set to your OpenAI API key.
2. run `python3 main.py`
