---
id: tool-07570
type: tool
area: 库
status: active
tags: [校对, Jupyter Notebook, 协议未明, 本地优先, 中文友好, 改稿润色, 本地写作]
title: chinese_spelling_correction
summary: 错别字/语法/风格校对
source: https://github.com/tedyeh/chinese_spelling_correction
created: 2026-07-18
updated: 2026-07-18
no: 7570
category: 画龙补充 / 扩容入库 — 补充源
repo: tedyeh/chinese_spelling_correction
stars: 6
url: https://github.com/tedyeh/chinese_spelling_correction
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e7850adb11a4b157
  - methods/QUICK_START.md
---

# tedyeh/chinese_spelling_correction

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/tedyeh/chinese_spelling_correction
- **Stars**：6
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：grammatical-error-correction, instruction-tuning, spelling-correction, text-generation, text-to-text
- **GitHub 描述**：Chinese Grammar Error and Spelling Error Correction System - 中文文法錯誤及錯別字校正系統 
- **本地描述**：chinese_spelling_correction
- **拉取时间**：2026-07-25 19:25:55

related:
  - methods/QUICK_START.md
---

# Chinese Grammarly - Chinese Grammatical Error Correction

<p align='center'>
🤗<a href='https://huggingface.co/CodeTed/CGEDit'>Huggingface Repo</a> •📃<a href=''>[Paper Coming Soon]</a> •👨️<a href='https://github.com/TedYeh'>Cheng-Hung Yeh</a>
</p>

![](https://github.com/tedyeh/chinese_spelling_correction/blob/main/img/interface.png) 

## Overview
A Web Interface for Chinese Grammatical Error Correction.

**Spelling-T5-Base** instruction-tuned on over 1M sentences in traditional mandarin.

**Grammar-T5-Base** instruction-tuned on 5 tasks and over 150k sentences in traditional mandarin.

## Usage

install necessary packages.
```bash
pip install -r requirements.txt
```

Setup flask web interface.
```bash
cd csc_t5
python demo.py
```

Finally, if you want to retrain the t5-cged model, following this command:
```bash
cd csc_t5
python training_zh_prompt_model_csc.py --do_train --do_predict
```
