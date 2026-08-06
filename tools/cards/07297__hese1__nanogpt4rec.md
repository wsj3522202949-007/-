---
id: tool-07297
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: nanogpt4rec
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/hese1/nanogpt4rec
created: 2026-07-18
updated: 2026-07-18
no: 7297
category: 画龙补充 / 扩容入库 — 补充源
repo: hese1/nanogpt4rec
stars: 2
url: https://github.com/hese1/nanogpt4rec
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# hese1/nanogpt4rec

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/hese1/nanogpt4rec
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Train transformer based recommenders fast
- **本地描述**：nanogpt4rec
- **拉取时间**：2026-07-25 19:17:01

related:
  - methods/QUICK_START.md
---

# NanoGPT4Rec: Sequential Recommendations
![](https://github.com/hese1/nanogpt4rec/blob/main/assets/nanogpt4rec.jpg)

This repository extends [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT) implementation to create a transformer-based recommendation system.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Train model
python train.py --epochs 40 --batch_size 32 --block_size 50 --device mps
```

## Model Architecture

- 6 transformer layers
- 8 attention heads
- 256 embedding dimension
- Context features:
  - 4 temporal features (sin/cos encoding)
  - 1 time delta
  - 1 rating
  - 1 genre
- User embeddings (32 dim)
- Weight tying between input embeddings and output layer

## Acknowledgments

Built upon [nanoGPT](https://github.com/karpathy/nanoGPT) by Andrej Karpathy and uses the [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/) dataset.

## License

See LICENSE file for details.
