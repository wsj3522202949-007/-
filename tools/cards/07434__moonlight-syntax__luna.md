---
id: tool-07434
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: luna
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/moonlight-syntax/luna
created: 2026-07-18
updated: 2026-07-18
no: 7434
category: 画龙补充 / 扩容入库 — 补充源
repo: moonlight-syntax/luna
stars: 12
url: https://github.com/moonlight-syntax/luna
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 851149dfc62fa732
  - methods/QUICK_START.md
---

# moonlight-syntax/luna

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/moonlight-syntax/luna
- **Stars**：12
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：LUNA: a Framework for Language Understanding and Naturalness Assessment.
- **本地描述**：luna
- **拉取时间**：2026-07-25 19:21:46

related:
  - methods/QUICK_START.md
---

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/MoonlightSyntax/LUNA/-/blob/main/.pre-commit-config.yaml)


# LUNA: a Framework for Language Understanding and Naturalness Assessment

The framework provides a set of well-known automated evaluation metrics for text generation tasks.

The library includes the following metrics:

- Blanc: [paper](https://aclanthology.org/2020.eval4nlp-1.2/)
- Mover score: [paper](https://aclanthology.org/D19-1053/)
- BLEU: [paper](https://aclanthology.org/P02-1040/)
- METEOR: [paper](https://aclanthology.org/W05-0909/)
- ROUGE: [paper](https://aclanthology.org/W04-1013/)
- chrF: [paper](https://aclanthology.org/W15-3049/)
- BERTScore: [paper](https://arxiv.org/abs/1904.09675)
- BARTScore: [paper](https://arxiv.org/abs/2106.11520)
- Data statistics metrics: [paper](https://aclanthology.org/N18-1065/)
  - Compression
  - Coverage
  - Length
  - Novelty
  - Density
  - Repetition
- ROUGE-We: [paper](https://aclanthology.org/D15-1222/)
- S3: [paper](https://aclanthology.org/W17-4510/)
- BaryScore: [paper](https://arxiv.org/abs/2108.12463)
- DepthScore: [paper](https://arxiv.org/abs/2103.12711)
- InfoLM: [paper](https://arxiv.org/abs/2112.01589)

## Installation

### Installation from the source

Clone the repository and install the library from the root:

```bash
git clone https://github.com/Moonlight-Syntax/LUNA.git
pip install .
```

Another way is to use `poetry`. Then, run `poetry install` from the root.


## Quick start

The user can either trigger the `Calculator` to evaluate metrics or integrate the code itself.

### Calculator

The easiest way to evaluate NLG models is to execute the following snippet:

```python
from luna.calculate import Calculator

# Choose to compute in a sequential or a parallel setting
calculator = Calculator(execute_parallel=True)
metrics_dict = calculator.calculate(
  metrics=[depth_score, s3_metrics], # both are LUNA's metrics
  candidates=candidates,
  references=references
)

print(metrics_dict)
>>> {"DepthScore": ..., "S3": ...}
```

### Integrate the evaluations

All the metrics in the library follow the same interface:

```python
class Metrics:
    def evaluate_batch(self, hypothesyses: List[str], references: Optional[List[str]]) -> List[float]:
        *some code here*

    def evaluate_example(self, hypothesys: str, reference: Optional[str]) -> float:
        *some code here*
```

Thus, to evaluate your examples run the following code:

```python
from luna import MetricName

metric = MetricName()
result = metric.evaluate_example("Generated bad model by example", "Gold example")
results = metric.evaluate_batch(["Generated bad model by example 1", "Generated bad model by example 2"],
                                 ["Gold example 1", "Gold example 2"])
```


## Development

### Contribute to the library

We are open for issues and pull requests. We hope that LUNA's functionality is wide enough but we believe that it can always be elaborated and improved.

### Pre-commit hooks

We use [pre-commit hooks](https://pre-commit.com/) to check the code before commiting.

To install the hooks run the following:

```bash
pip install pre-commit
pre-commit install
```

After that every commit will trigger standard checks on code style, including `black`, `isort` etc.

### Tests

Tests for `luna` are located in the `tests` directory. To run them, execute:

```bash
pytest tests
```
