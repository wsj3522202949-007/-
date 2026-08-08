---
id: tool-07569
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: scrolls
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/tau-nlp/scrolls
created: 2026-07-18
updated: 2026-07-18
no: 7569
category: 画龙补充 / 扩容入库 — 补充源
repo: tau-nlp/scrolls
stars: 69
url: https://github.com/tau-nlp/scrolls
tier: "A"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ce6b286406aad8bb
  - methods/QUICK_START.md
---

# tau-nlp/scrolls

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/tau-nlp/scrolls
- **Stars**：69
- **语言**：Python
- **License**：MIT
- **Topics**：benchmark, long-texts, natural-language-understanding
- **GitHub 描述**：The official code of EMNLP 2022, "SCROLLS: Standardized CompaRison Over Long Language Sequences".
- **本地描述**：scrolls
- **拉取时间**：2026-07-25 19:25:54

related:
  - methods/QUICK_START.md
---

# SCROLLS

This repository contains the official code of the paper: ["SCROLLS: Standardized CompaRison Over Long Language Sequences"](https://arxiv.org/abs/2201.03533).

Setup instructions are in the [baselines](https://github.com/tau-nlp/scrolls/tree/main/baselines)   and [evaluator](https://github.com/tau-nlp/scrolls/tree/main/evaluator)   folders. 

For the live leaderboard, checkout the [official website](https://scrolls-benchmark.com/). 

***
## Loading the SCROLLS Benchmark Datasets
- via [🤗 Datasets (huggingface/datasets)](https://github.com/huggingface/datasets) library (recommended):

    1. [Installation](https://github.com/huggingface/datasets#installation)
    2. Usage:

        ```python
        from datasets import load_dataset

        qasper_dataset = load_dataset("tau/scrolls", "qasper")
        """
        Options are: ["gov_report", "summ_screen_fd", "qmsum", "narrative_qa", "qasper", "quality", "contract_nli"]
        """
        ```
- via ZIP files, where each split is in a JSONL file:
  - [GovReport](https://huggingface.co/datasets/tau/scrolls/resolve/main/gov_report.zip)
  - [SummScreenFD](https://huggingface.co/datasets/tau/scrolls/resolve/main/summ_screen_fd.zip)
  - [QMSum](https://huggingface.co/datasets/tau/scrolls/resolve/main/qmsum.zip)
  - [NarrativeQA](https://huggingface.co/datasets/tau/scrolls/resolve/main/narrative_qa.zip)
  - [Qasper](https://huggingface.co/datasets/tau/scrolls/resolve/main/qasper.zip)
  - [QuALITY](https://huggingface.co/datasets/tau/scrolls/resolve/main/quality.zip)
  - [ContractNLI](https://huggingface.co/datasets/tau/scrolls/resolve/main/contract_nli.zip)


## Citation
```
@inproceedings{shaham-etal-2022-scrolls,
    title = "{SCROLLS}: Standardized {C}ompa{R}ison Over Long Language Sequences",
    author = "Shaham, Uri  and
      Segal, Elad  and
      Ivgi, Maor  and
      Efrat, Avia  and
      Yoran, Ori  and
      Haviv, Adi  and
      Gupta, Ankit  and
      Xiong, Wenhan  and
      Geva, Mor  and
      Berant, Jonathan  and
      Levy, Omer",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.823",
    pages = "12007--12021",
}
```
When citing SCROLLS, please make sure to cite all the original dataset papers. [[bibtex]](https://github.com/tau-nlp/scrolls/tree/main/scrolls_datasets.bib)
