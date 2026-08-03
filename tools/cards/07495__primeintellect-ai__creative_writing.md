---
id: tool-07495
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: creative_writing
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/primeintellect-ai/creative_writing
created: 2026-07-18
updated: 2026-07-18
no: 7495
category: 画龙补充 / 扩容入库 — 补充源
repo: primeintellect-ai/creative_writing
stars: 0
url: https://github.com/primeintellect-ai/creative_writing
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# primeintellect-ai/creative_writing

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/primeintellect-ai/creative_writing
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：creative_writing
- **拉取时间**：2026-07-25 19:23:38

---

# Writing Environment (RL Story Generation)

This repository contains a lightweight environment for training and evaluating creative-writing models using reinforcement learning. It includes components for generating stories, evaluating them using rubric-based scoring, and configuring training runs.

---

## Overview

The environment is designed for experimenting with RLHF pipelines for story generation.  
A model produces a story based on a prompt, and a judge evaluates the output according to structured rubrics.  
The judge returns a numerical reward along with rubric-specific scores.

---

## Components

### 1. writing_bench.py

Runs the main writing-generation loop.  
It is responsible for:

- Loading tasks from JSON files  
- Sampling prompts and running generation episodes  
- Handling batch size, sequence length, rollouts, and sampling settings  
- Returning outputs suitable for RL training or evaluation workflows

---

### 2. writing_judge.py

Implements the rubric-based evaluation system.  
The judge performs the following:

- Reads task metadata and rubric definitions  
- Checks objective requirements (such as word count, POV, tense, genre, etc.)  
- Applies subjective scoring using a judge model  
- Produces a final numeric reward and a detailed rubric breakdown

---

### 3. Task Files

This repository includes two task sets:

- `generated_tasks8_train.json`  
- `generated_tasks8_eval.json`

Each task contains:

- A story prompt  
- Required stylistic or structural attributes  
- Rubric definitions used by the judge for scoring

These files are used during training and evaluation, respectively.

---

### 4. writing_configs.toml

Defines configuration settings for:

- Model selection  
- Checkpoint intervals  
- Batch sizes and rollout parameters  
- Sequence lengths and sampling settings  
- Environment parameters (such as which task file to load)  
- Optimizer and LoRA settings

This file serves as the central configuration point for training.

related:
  - methods/QUICK_START.md
---

## Running the Environment

Run the writing generation process and judge process:

```bash
python writing_bench.py --config writing_configs.toml

python writing_judge.py --tasks generated_tasks8_eval.json
