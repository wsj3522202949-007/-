---
id: tool-07208
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: pgrdiff
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/czy-code/pgrdiff
created: 2026-07-18
updated: 2026-07-18
no: 7208
category: 画龙补充 / 扩容入库 — 补充源
repo: czy-code/pgrdiff
stars: 3
url: https://github.com/czy-code/pgrdiff
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6bd9d7d917313804
  - methods/QUICK_START.md
---

# czy-code/pgrdiff

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/czy-code/pgrdiff
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：All-in-One Mural Restoration with Prompt-Guided Residual Diffusion & Learning Mural Restoration from Degraded Data via Unsupervised Low-rank Residual Diffusion
- **本地描述**：pgrdiff
- **拉取时间**：2026-07-25 19:14:11

related:
  - methods/QUICK_START.md
---

# All-in-One Mural Restoration with Prompt-Guided Residual Diffusion

## Installation

1. Download source code and dataset:
    * `git clone https://github.com/CZY-Code/PGRDiff.git`
    * Download the datasets
        - [DUNHUANG](https://www.kaggle.com/datasets/xuhangc/dunhuang-grottoes-painting-dataset-and-benchmark)
        - [muralv2](https://pan.quark.cn/s/737e3843ce53?pwd=d8zT)
        
   
2.  Pip install dependencies:
    ```
    conda env create -f install.yaml
    ```

## Dataset Preparation
Unzip and move dataset into ROOT

### Directory structure of dataset     
    ├── PGRDiff
    │   ├── code
    │   ├── DUNHUANG
    │   │   ├── train
    │   │   ├── test
    │   ├── muralv2
    │   │   ├── images
    │   │   ├── masks
    │   ├── install.yaml
    │   ├── README.md

## Training
```
cd ./code
python train.py
```
or
```
accelerate launch train.py
```
    
## Evaluation
```
cd ./code
python metric.py
```
## Pre-trained Models
    ├── code                     
    ├── DUNHUANG
    │   ├── train         
    │   ├── test
    ├──muralv2
    │   ├── images
    │   ├── masks
    ├── install.yaml
    ├── README.md

## Training
```
cd ./code
python train.py
```
or
```
accelerate launch train.py
```
    
## Evaluation
```
cd ./code
python metric.py
```
## Pre-trained Models
* Download the weights of trained models
    - [Weight for DUNHUANG](https://pan.quark.cn/s/f75148cab005?pwd=Lsi3)
    - [Weight for muralv2](https://pan.quark.cn/s/197e10e66555?pwd=VY36)
* Move the weights into the folder `./code/results/sample/`

## Acknowledgement
This implementation is based on / inspired by:
* [RDDM](https://github.com/nachifur/RDDM)
* [IR-SDE](https://github.com/Algolzw/image-restoration-sde)
* [LRDiff](https://github.com/CZY-Code/LRDiff)
* [StrDiffusion](https://github.com/htyjers/StrDiffusion)
