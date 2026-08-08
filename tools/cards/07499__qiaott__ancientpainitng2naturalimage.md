---
id: tool-07499
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ancientpainitng2naturalimage
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/qiaott/ancientpainitng2naturalimage
created: 2026-07-18
updated: 2026-07-18
no: 7499
category: 画龙补充 / 扩容入库 — 补充源
repo: qiaott/ancientpainitng2naturalimage
stars: 15
url: https://github.com/qiaott/ancientpainitng2naturalimage
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 82795b051bdc69b4
  - methods/QUICK_START.md
---

# qiaott/ancientpainitng2naturalimage

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/qiaott/ancientpainitng2naturalimage
- **Stars**：15
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Ancient Painting to Natural Image: A New Solution for Painting Processing
- **本地描述**：ancientpainitng2naturalimage
- **拉取时间**：2026-07-25 19:23:44

related:
  - methods/QUICK_START.md
---

# AncientPainitng2NaturalImage
Pytorch implementation for the paper [[Ancient Painting to Natural Image: A New Solution for Painting Processing]](https://arxiv.org/pdf/1901.00224.pdf) .

![image](images/example.jpg)

## Getting Started
### Installation
- Install PyTorch and dependencies from http://pytorch.org
- Install Torch vision from the source.
```bash
git clone https://github.com/pytorch/vision
cd vision
python setup.py install
```
- Install python libraries [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate).
```bash
pip install visdom
pip install dominate
```
- Clone this repo:
```bash
git clone https://github.com/qiaott/AncientPainitng2NaturalImage.git
cd AncientPainitng2NaturalImage
```
- Download our datasets (e.g. CBP, CFP) from [here](https://drive.google.com/open?id=1ilqfMC3A9Kt6CaoZZCT9tI-wWRl1kLFB) .


### Train/Test

- Train a model:
```bash
./do_train.sh
```

- Test a model:
```bash
./do_test.sh
```

You can play with your own dataset by changing the dataroot.

##Citation
If you use this code/datasets for your research, please cite our papers.
```bash
@inproceedings{qiao2019ancient,
  title={Ancient Painting to Natural Image: A New Solution for Painting Processing},
  author={Qiao, Tingting and Zhang, Weijing and Zhang, Miao and Ma, Zixuan and Xu, Duanqing},
  booktitle={2019 IEEE Winter Conference on Applications of Computer Vision (WACV)},
  pages={521--530},
  year={2019},
  organization={IEEE}
}
```
## Acknowledgments
Code is inspired by [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

