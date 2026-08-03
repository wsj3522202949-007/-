---
id: tool-05724
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 去AI味, 本地写作]
title: LINGJIAN-Zero-shot-AI-generated-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/msx1234564-debug/lingjian-zero-shot-ai-generated-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5724
category: 一、去 AI 味 / Humanizer 库
repo: msx1234564-debug/LINGJIAN-Zero-shot-AI-generated-text-detector
stars: 1
url: https://github.com/msx1234564-debug/lingjian-zero-shot-ai-generated-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# msx1234564-debug/LINGJIAN-Zero-shot-AI-generated-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/msx1234564-debug/lingjian-zero-shot-ai-generated-text-detector
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：这是大创项目---灵鉴AI生成文本检测器的开源代码。
- **本地描述**：这是大创项目---灵鉴AI生成文本检测器的开源代码。
- **拉取时间**：2026-07-25 18:29:16

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 灵鉴
**灵鉴检测器的开源代码**

## 数据
以下文件夹为实验数据集：
* ./exp_Open_source_model -> 开源生成模型实验.
* ./exp_API-based_model -> 闭源生成模型实验.

## 代理模型加载
huggingface上下载
* BART-base: https://huggingface.co/facebook/bart-base
* OPT-350m: https://huggingface.co/facebook/opt-350m


## 环境
* Python3.8
* PyTorch2.1.0

GPU: NVIDIA 3090 GPU with 24GB memory

## 快速开始
Please run following commands for a demo:
请运行以下指令以开始复现实验
```
python eval.py
```



