---
id: tool-00989
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: CuseHacks-21
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/apurvamulay/cusehacks-21
created: 2026-07-18
updated: 2026-07-18
no: 989
category: 二、网文 / 长篇 AI 写作系统 库
repo: apurvamulay/CuseHacks-21
stars: 1
url: https://github.com/apurvamulay/cusehacks-21
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# apurvamulay/CuseHacks-21

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/apurvamulay/cusehacks-21
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Story Generator - Visualizes stories based on text using GPT2 and GAN(Generative Adversarial Networks)
- **本地描述**：AI Story Generator - Visualizes stories based on text using GPT2 and GAN(Generative Adversarial Networks)
- **拉取时间**：2026-07-23 23:07:53

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## AI Story Generator

## Install

```bash
$ pip install transformers
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
$ pip install bert-extractive-summarizer
$ pip install torch
$ pip install numpy
$ pip install torchvision

```

## Usage

```bash
Search Variable 'input_to_model' and set it to a random phrase.
In google collab set runtime -> change runtime -> GPU
```

Original notebook [![Open In Colab][colab-badge]][colab-notebook]

[colab-notebook]: <https://colab.research.google.com/drive/1dHhxY19Fv5brc1Nh3CwiDj-LaNtzE14F?usp=sharing>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>


[HTML file]: <https://github.com/apurvamulay/CuseHacks-21/blob/main/test.html> 
NOTE: Download the HTML file ([HTML file]) on your machine to see the exact output.


## References and Citations

### Git Repository <a href="https://github.com/lucidrains/big-sleep"> Lucid Rain</a>

```bibtex
@misc{unpublished2021clip,
    title  = {CLIP: Connecting Text and Images},
    author = {Alec Radford, Ilya Sutskever, Jong Wook Kim, Gretchen Krueger, Sandhini Agarwal},
    year   = {2021}
}
```

```bibtex
@misc{brock2019large,
    title   = {Large Scale GAN Training for High Fidelity Natural Image Synthesis}, 
    author  = {Andrew Brock and Jeff Donahue and Karen Simonyan},
    year    = {2019},
    eprint  = {1809.11096},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG}
}
```
