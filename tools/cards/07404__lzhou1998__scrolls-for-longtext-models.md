---
id: tool-07404
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 本地写作]
title: scrolls-for-longtext-models
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/lzhou1998/scrolls-for-longtext-models
created: 2026-07-18
updated: 2026-07-18
no: 7404
category: 画龙补充 / 扩容入库 — 补充源
repo: lzhou1998/scrolls-for-longtext-models
stars: 0
url: https://github.com/lzhou1998/scrolls-for-longtext-models
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6368155431918e34
  - methods/QUICK_START.md
---

# lzhou1998/scrolls-for-longtext-models

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lzhou1998/scrolls-for-longtext-models
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Do experiments on SCROLLS benchmark for my own long text models
- **本地描述**：scrolls-for-longtext-models
- **拉取时间**：2026-07-25 19:20:52

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
  - [GovReport](https://scrolls-tau.s3.us-east-2.amazonaws.com/gov_report.zip)
  - [SummScreenFD](https://scrolls-tau.s3.us-east-2.amazonaws.com/summ_screen_fd.zip)
  - [QMSum](https://scrolls-tau.s3.us-east-2.amazonaws.com/qmsum.zip)
  - [NarrativeQA](https://scrolls-tau.s3.us-east-2.amazonaws.com/narrative_qa.zip)
  - [Qasper](https://scrolls-tau.s3.us-east-2.amazonaws.com/qasper.zip)
  - [QuALITY](https://scrolls-tau.s3.us-east-2.amazonaws.com/quality.zip)
  - [ContractNLI](https://scrolls-tau.s3.us-east-2.amazonaws.com/contract_nli.zip)


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
When citing SCROLLS, please make sure to cite all of the original dataset papers. [[bibtex]](https://scrolls-tau.s3.us-east-2.amazonaws.com/scrolls_datasets.bib)
