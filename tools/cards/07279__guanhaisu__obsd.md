---
id: tool-07279
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: obsd
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/guanhaisu/obsd
created: 2026-07-18
updated: 2026-07-18
no: 7279
category: 画龙补充 / 扩容入库 — 补充源
repo: guanhaisu/obsd
stars: 232
url: https://github.com/guanhaisu/obsd
tier: "S"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# guanhaisu/obsd

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/guanhaisu/obsd
- **Stars**：232
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Deciphering Oracle Bone Language with Diffusion Models (ACL 2024 Best Paper)
- **本地描述**：obsd
- **拉取时间**：2026-07-25 19:16:26

related:
  - methods/QUICK_START.md
---

<div align="center">
  <img src="figures\obsd.png" alt="OBSD logo"/>
</div>

<h2 align="center"> <a href="https://arxiv.org/abs/2406.00684">OBSD: Deciphering Oracle Bone Language with Diffusion Models </a></h2>
<h4 align="center">Haisu Guan, Huanxin Yang, Xinyu Wang, Shengwei Han, Yongge Liu, Lianwen Jin, Xiang Bai, Yuliang Liu* </h4>
<p align="center">
  <a href="https://arxiv.org/abs/2406.00684"><img src="https://img.shields.io/badge/Arxiv-2406.00684-b31b1b.svg?logo=arXiv" alt="arXiv" /></a>
  <a href="http://vlrlabmonkey.xyz:8225/"><img src="https://img.shields.io/badge/Demo-blue" alt="Demo" /></a>
</p>

## Overview
OBSD (Oracle Bone Script Decipher) explores diffusion models for decoding oracle bone inscriptions and translating them into modern Chinese characters. This repository contains the official implementation, datasets, and training scripts from the paper.

## News
- ```2024-08-14``` 🚀 OBSD has been selected as the ACL 2024 Best Paper.
- ```2024-07-15``` 🚀 OBSD has been selected as the ACL 2024 Oral.
- ```2024-05-16``` 🚀 OBSD is accepted by ACL 2024 Main.
- ```2024-02-15``` 🚀 Source code released.

## Resources
- 📄 Paper: [arXiv 2406.00684](https://arxiv.org/abs/2406.00684)
- 🎮 Demo: [OBSD Online](http://vlrlabmonkey.xyz:8225/)
- 🗂️ Dataset: [Character Evolution Dataset](https://github.com/RomanticGodVAN/character-Evolution-Dataset)
- 🖼️ Modern character images: `data/modern_kanji.zip`
- 🛠️ Data processing helper: [`data/process.py`](./data/process.py)

## Data Preparation
Arrange your dataset so that oracle bone images (OBS) and their corresponding modern Chinese characters share the same filenames.

```text
Your_dataroot/
  train/  (training set)
    input/
      train_安_1.png  (OBS image)
      train_安_2.png
      train_北_1.png
      train_北_2.png
    target/
      train_安_1.png  (modern character)
      train_安_2.png
      train_北_1.png
      train_北_2.png
  test/  (test set)
    input/
      test_1.png  (OBS image)
      test_2.png
    target/
      test_1.png  (modern character)
      test_2.png
```

## Configuration
Update `configs.yaml` so that all paths point to your local setup.

```yaml
data:
  train_data_dir: "/Your_dataroot/train/"      # path to directory of train data
  test_data_dir: "/Your_dataroot/test/"        # path to directory of test data
  test_save_dir: "Your_project_path/OBS_Diffusion/result"
  val_save_dir: "Your_project_path/OBS_Diffusion/validation/"
  tensorboard: "Your_project_path/OBS_Diffusion/logs"

training:
  resume: "/Your_save_root/diffusion_model"    # path to pretrained model
```

## Quick Start
```bash
git clone https://github.com/guanhaisu/OBSD.git
cd OBS_Diffusion

conda create -n OBSD python=3.10
conda activate OBSD
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -r requirements.txt
```

## Training
```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.run --nproc_per_node=8 --nnodes=1 --node_rank=0 --master_addr=localhost --master_port=1234 train_diffusion.py
```

## Monitoring
```bash
tensorboard --logdir ./logs
```

## Evaluation & Refinement
```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.run --nproc_per_node=8 --nnodes=1 --node_rank=0 --master_addr=localhost --master_port=1234 eval_diffusion.py
CUDA_VISIBLE_DEVICES=0 python refine.py
```
Download the FontDiffuser weights from [Google Drive](https://drive.google.com/drive/folders/1kRwi5sfHn6oufydDmd-7X9pPFDZzFjkk?usp=drive_link) before running `refine.py`.

## Citation
```bibtex
@misc{guan2025decipheringoraclebonelanguage,
  title        = {Deciphering Oracle Bone Language with Diffusion Models},
  author       = {Haisu Guan and Huanxin Yang and Xinyu Wang and Shengwei Han and Yongge Liu and Lianwen Jin and Xiang Bai and Yuliang Liu},
  year         = {2025},
  eprint       = {2406.00684},
  archivePrefix= {arXiv},
  primaryClass = {cs.CV},
  url          = {https://arxiv.org/abs/2406.00684}
}
```
