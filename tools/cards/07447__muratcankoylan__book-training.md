---
id: tool-07447
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: book-training
summary: 风格微调/文风迁移
source: https://github.com/muratcankoylan/book-training
created: 2026-07-18
updated: 2026-07-18
no: 7447
category: 画龙补充 / 扩容入库 — 补充源
repo: muratcankoylan/book-training
stars: 35
url: https://github.com/muratcankoylan/book-training
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f3eb7158b84cc509
  - methods/QUICK_START.md
---

# muratcankoylan/book-training

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/muratcankoylan/book-training
- **Stars**：35
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A complete pipeline for training language models to write in a specific author's style using Supervised Fine-Tuning (SFT) with LoRA.
- **本地描述**：book-training
- **拉取时间**：2026-07-25 19:22:09

---

# Book Training: Style Transfer via SFT

A complete pipeline for training language models to write in a specific author's style using Supervised Fine-Tuning (SFT) with LoRA.

## Project Overview

This repository demonstrates how to:
1. Extract and segment text from EPUB books
2. Generate diverse instruction-response pairs using LLMs
3. Train a small model (Qwen3-8B-Base) with LoRA
4. Validate genuine style transfer vs. memorization

## Results

Trained on Gertrude Stein's "Three Lives" (1909):

| Metric | Value |
|--------|----related:
  - methods/QUICK_START.md
---|
| Training Examples | 591 |
| Final Test Loss | 213 (from 7,584) |
| Loss Reduction | 97% |
| Training Time | ~15 min |
| AI Detector Score | ~50-70% Human (Pangram) |

The model applies Stein's style to modern scenarios not in training data, confirming style transfer rather than memorization.

## Repository Structure

```
├── skills/book-sft-pipeline/     # Reusable skill for AI agents
│   ├── SKILL.md                  # Main skill definition
│   ├── references/               # Segmentation, training docs
│   ├── scripts/                  # Example pipeline code
│   └── examples/gertrude-stein/  # Complete case study
├── src/
│   ├── pipeline.ts               # Dataset generation pipeline
│   └── train-tinker.ts           # Tinker training setup
├── train_tinker.py               # LoRA training script
├── chat.py                       # Interactive model testing
├── test_style_transfer.py        # Style validation tests
├── hf-dataset/                   # HuggingFace dataset files
│   ├── train.jsonl               # 591 training examples
│   ├── test.jsonl                # 49 test examples
│   └── README.md                 # Dataset card
└── three-lives-sft-dataset.jsonl # Full generated dataset
```

## Quick Start

### 1. Generate Dataset

```bash
npm install
npx tsx src/pipeline.ts
```

### 2. Train with Tinker

```bash
pip install tinker python-dotenv
python train_tinker.py
```

### 3. Test the Model

```bash
python chat.py
```

## Dataset

Available on HuggingFace: [MuratcanKoylan/gertrude-stein-style-sft](https://huggingface.co/datasets/MuratcanKoylan/gertrude-stein-style-sft)

```python
from datasets import load_dataset
dataset = load_dataset("MuratcanKoylan/gertrude-stein-style-sft")
```

## Key Techniques

### Prompt Diversity
15 prompt templates × 5 system prompts = 75 unique combinations per chunk. Prevents overfitting to specific phrasings.

### Fine-Grained Segmentation
150-400 word chunks with overlap. Smaller chunks capture more stylistic patterns.

### Modern Scenario Testing
Validate style transfer by prompting about topics the author never wrote about (real estate offices, smartphones, etc.).

## Skills for AI Agents

The `/skills/book-sft-pipeline` folder contains a complete skill definition that enables AI agents to replicate this pipeline for any book:

```
skills/book-sft-pipeline/
├── SKILL.md              # Agent-readable instructions
├── references/           # Technical documentation
├── scripts/              # Example implementations
└── examples/             # Case studies with results
```

## Sample Output

**Prompt**: Write about a tech startup founder in the style of Gertrude Stein.

**Output**:
> She was always working, always she was working on her startup. The investors they would come and they would go and she would talk to them about the product. She was a good founder, always she was a good founder. She had this way of explaining things, simple and direct, and the investors they would listen.

## License

MIT

Source text "Three Lives" by Gertrude Stein (1909) is in the public domain.

