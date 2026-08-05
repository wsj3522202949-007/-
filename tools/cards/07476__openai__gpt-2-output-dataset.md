---
id: tool-07476
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: gpt-2-output-dataset
summary: 风格微调/文风迁移
source: https://github.com/openai/gpt-2-output-dataset
created: 2026-07-18
updated: 2026-07-18
no: 7476
category: 画龙补充 / 扩容入库 — 补充源
repo: openai/gpt-2-output-dataset
stars: 2027
url: https://github.com/openai/gpt-2-output-dataset
tier: "S"
use_case: "风格微调/文风迁移"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# openai/gpt-2-output-dataset

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/openai/gpt-2-output-dataset
- **Stars**：2027
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Dataset of GPT-2 outputs for research in detection, biases, and more
- **本地描述**：gpt-2-output-dataset
- **拉取时间**：2026-07-25 19:23:03

related:
  - methods/QUICK_START.md
---

# gpt-2-output-dataset

This dataset contains:
- 250K documents from the WebText test set
- For each GPT-2 model (trained on the WebText training set), 250K random samples (temperature 1, no truncation) and 250K samples generated with Top-K 40 truncation

We look forward to the research produced using this data!

### Download

For each model, we have a training split of 250K generated examples, as well as validation and test splits of 5K examples.

All data is located in Google Cloud Storage, under the directory `gs://gpt-2/output-dataset/v1`.  (NOTE: everything has been migrated to Azure `https://openaipublic.blob.core.windows.net/gpt-2/output-dataset/v1/`)

There, you will find files:

- `webtext.${split}.jsonl`
- `small-117M.${split}.jsonl`
- `small-117M-k40.${split}.jsonl`
- `medium-345M.${split}.jsonl`
- `medium-345M-k40.${split}.jsonl`
- `large-762M.${split}.jsonl`
- `large-762M-k40.${split}.jsonl`
- `xl-1542M.${split}.jsonl`
- `xl-1542M-k40.${split}.jsonl`

where split is one of `train`, `test`, and `valid`.

We've provided a script to download all of them, in `download_dataset.py`.

#### Finetuned model samples

Additionally, we encourage research on detection of finetuned models.  We have released data under `gs://gpt-2/output-dataset/v1-amazonfinetune/` with samples from a GPT-2 full model finetuned to output Amazon reviews.

### Detectability baselines

We're interested in seeing research in detectability of GPT-2 model family generations.

We provide some [initial analysis](detection.md) of two baselines, as well as [code](./baseline.py) for the better baseline.

Overall, we are able to achieve accuracies in the mid-90s for Top-K 40 generations, and mid-70s to high-80s (depending on model size) for random generations.  We also find some evidence that adversaries can evade detection via finetuning from released models.

### Data removal requests

If you believe your work is included in WebText and would like us to remove it, please let us know at webtextdata@openai.com.
