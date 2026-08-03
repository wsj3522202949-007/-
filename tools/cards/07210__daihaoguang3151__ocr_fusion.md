---
id: tool-07210
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: ocr_fusion
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/daihaoguang3151/ocr_fusion
created: 2026-07-18
updated: 2026-07-18
no: 7210
category: 画龙补充 / 扩容入库 — 补充源
repo: daihaoguang3151/ocr_fusion
stars: 4
url: https://github.com/daihaoguang3151/ocr_fusion
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# daihaoguang3151/ocr_fusion

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/daihaoguang3151/ocr_fusion
- **Stars**：4
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：OCR Fusion: EasyOCR/Tesseract/PaddleOCR/TrOCR/GOT
- **本地描述**：ocr_fusion
- **拉取时间**：2026-07-25 19:14:14

related:
  - methods/QUICK_START.md
---

## OCR Fusion: EasyOCR/Tesseract/PaddleOCR/TrOCR/GOT

根据个人实际需求尝试了几种不同的OCR，将他们集结在此repo中。

1. [EasyOCR](https://github.com/JaidedAI/EasyOCR)和[Tesseract](https://github.com/tesseract-ocr/tesseract)是之前较流行的轻量OCR工具；
2. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)效果不错，模型也很轻量；为了能在pytorch下直接使用，[PaddleOCR2Pytorch](https://github.com/frotms/PaddleOCR2Pytorch)提供了转换好的pytorch模型；
3. [TrOCR](https://github.com/microsoft/unilm/tree/master/trocr)是微软实现的，主要用于单行手写文字的识别；
4. [GOT](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)是清华最近开源的模型，支持多种形式的OCR识别，效果不错，推荐尝试。

## 内容

[环境](#环境)

[模型下载](#模型下载)

[DEMO](#DEMO)

## 环境

根据`requirements.txt`中的提示进行环境的安装，如有问题，请参考csdn。

## 模型下载

1. EasyOCR: [Jaided AI: EasyOCR model hub](https://www.jaided.ai/easyocr/modelhub/)

2. PaddleOCR (pytorch): [GitHub - frotms/PaddleOCR2Pytorch: PaddleOCR inference in PyTorch. Converted from [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)](https://github.com/frotms/PaddleOCR2Pytorch)

3. TrOCR: [microsoft/trocr-base-handwritten · Hugging Face](https://huggingface.co/microsoft/trocr-base-handwritten)

4. GOT: [stepfun-ai/GOT-OCR2_0 · Hugging Face](https://huggingface.co/stepfun-ai/GOT-OCR2_0)

## DEMO

```bash
cd src

# 如果是使用下载好的model，使用时需要在相应的py文件中修改模型的读取路径，比如：
# ocr_executor/gotocr_executor.py中 _MODEL_NAME = "/home/ubuntu/Projects_ubuntu/GOT_weights/"修改为你自己的本地路径

# 选择你需要的ocr执行器和图片，并且运行以下命令
python main.py
```
