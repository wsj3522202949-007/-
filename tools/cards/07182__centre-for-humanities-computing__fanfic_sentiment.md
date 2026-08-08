---
id: tool-07182
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: fanfic_sentiment
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/centre-for-humanities-computing/fanfic_sentiment
created: 2026-07-18
updated: 2026-07-18
no: 7182
category: 画龙补充 / 扩容入库 — 补充源
repo: centre-for-humanities-computing/fanfic_sentiment
stars: 1
url: https://github.com/centre-for-humanities-computing/fanfic_sentiment
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6cb67a9be7c093e9
  - methods/QUICK_START.md
---

# centre-for-humanities-computing/fanfic_sentiment

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/centre-for-humanities-computing/fanfic_sentiment
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：fanfic_sentiment
- **拉取时间**：2026-07-25 19:13:21

related:
  - methods/QUICK_START.md
---



# Sentiment Analysis for fanfic & other texts 🎭

this script runs sentiment analysis on text datasets (like fanfic or whatever you have) using huggingface transformer models 🤗 plus dictionary-based tools: **vader** and **syuzhet**.

## what it does ⚙️

### contionous score SA tagging
- takes a csv dataset with a `text` column (and optionally a `work_id` or similar id)  
- cleans up the text (whitespace, etc)  
- skips empty, missing, or super long texts (>2 million chars)  
- splits text into sentences using spacy’s (En) sentence segmenter  -- so we are scoring *sentences* here
- runs sentiment analysis with vader, syuzhet, and any huggingface transformer models you specify
- saves partial results as json files along the way so you don’t lose progress  
- logs everything for debugging  

*then:*
### fanfiction sentiment dynamics
- does some testing on differences in sentiment dynamics for different fanfiction subsets

## how to do SA 🚀

install requirements, then, in terminal:

```bash

python -m src.get_sent \
    --dataset-name data/MythFic_texts.csv \
    --model-names cardiffnlp/xlm-roberta-base-sentiment-multilingual \
    #cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual \
    --n-rows 5

```
- dataset path
- HF model names (can be multiple); *still when adding a new one please make sure that the labels (pos, neg, neutr) map onto the expected labels in* ```utils.LABEL_NORMALIZATION```
- n-rows (optional) is for testing the script and setup, for example 5 rows

## Look at the data
- in ```notebooks/notebook.ipynb``` you'll find a script to open the SA data extracted and do some initial testing
- in ```stats.r``` you'll find some statistical significance testing for the sets of fanfiction


## details

### VADER & SYUZHET
- scored by default, average (compound score) per sentence of what these dictionaries give us

### SA transformer-based details
- if any sentence is too long (i.e., exceeds model max tokens), it will be chunked into the necessary chunks and the scores returned will be an average of all chunks
- max token length is retrieved automatically, so chunking will conform to the max token length of the model
- binary scores (pos, neg, neutr) are converted to a continuous scale using the confidence score for the assingment. So a score of pos, confidence: 0.6 will give us a score of 0.6. A score of neg, confidence: 0.6 will give us -0.6. Neutral labels will always tranform to 0. For more detail, see ```utils.get_sentiment```


## Repo structure

````
├── src                              <- main folder for code 
|   ├── get_sent.py                  <- script to extract SA
|   ├── utils.py                     <- helper functions for SA extraction
|   ├── saffine                      <- folder for higher-level SA feature extraction (hurst) and detrending
|   └── get_derived_features.py      <- functions (used in notebooks) to get higher-level SA features
├── logs                             <- logs generated in SA extraction
├── results                          <- results folder
|   ├── partial_results              <- saved 1000 iteration chunks of SA scores
|   ├── figs                         <- visualizations generated in notebooks
├── notebooks                        <- notebooks for processing and testing SA dynamics in extracted data
├── README.md                        <- top-level README for this project
└── requirements.txt                 <- necessary packages
```
