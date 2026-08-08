---
id: tool-07144
type: tool
area: 库
status: active
tags: [文风迁移, Jupyter Notebook, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: text2img
summary: 风格微调/文风迁移
source: https://github.com/arinagoncharova2005/text2img
created: 2026-07-18
updated: 2026-07-18
no: 7144
category: 画龙补充 / 扩容入库 — 补充源
repo: arinagoncharova2005/text2img
stars: 0
url: https://github.com/arinagoncharova2005/text2img
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6e06e34427dd6d1c
  - methods/QUICK_START.md
---

# arinagoncharova2005/text2img

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/arinagoncharova2005/text2img
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Text-to-Image: Stable Diffusion Fine-tuning
- **本地描述**：text2img
- **拉取时间**：2026-07-25 19:12:11

related:
  - methods/QUICK_START.md
---

### Goal
Fine-tune Stable Diffusion on a custom dataset of book covers to generate images in a consistent “book cover” style from text prompts

### Tech stack
- PyTorch
- Hugging Face Diffusers
- Transformers
- PEFT (LoRA) 

### Results
Improved alignment between generated images and input prompts.
Achieved more coherent and stylistically consistent book cover outputs compared to the base Stable Diffusion model.

