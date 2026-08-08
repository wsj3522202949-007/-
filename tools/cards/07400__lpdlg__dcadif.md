---
id: tool-07400
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: dcadif
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/lpdlg/dcadif
created: 2026-07-18
updated: 2026-07-18
no: 7400
category: 画龙补充 / 扩容入库 — 补充源
repo: lpdlg/dcadif
stars: 0
url: https://github.com/lpdlg/dcadif
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4b1a87be2d640add
  - methods/QUICK_START.md
---

# lpdlg/dcadif

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lpdlg/dcadif
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：DCADif: Decoupled Conditional Adaptive Time-dynamic Fusion Diffusion Inpainting of Traditional Chinese Mural Paintings
- **本地描述**：dcadif
- **拉取时间**：2026-07-25 19:20:46

related:
  - methods/QUICK_START.md
---

# DCADif
DCADif: Decoupled Conditional Adaptive Time-dynamic Fusion Diffusion Inpainting of Traditional Chinese Mural Paintings

## Project Profile

Our work proposes the DCADif framework, an innovative diffusion model that addresses the critical challenge of disentangling structure and style in the inpainting of traditional Chinese murals. This approach establishes a new benchmark for the digital preservation of cultural heritage. Central to our framework is a Decoupled Conditional Encoder that uses parallel pathways—a CLIP encoder for structural line art and a novel SwinStyle Encoder for artistic features—to achieve orthogonal representations. Furthermore, our Time-Adaptive Feature Fusion (TAFF) module dynamically adjusts the influence of these features over the diffusion timestep, mimicking an expert's coarse-to-fine strategy by prioritizing structure before refining style. Validated on our new, large-scale MuralVerse-S dataset, DCADif demonstrates state-of-the-art performance, effectively bridging the gap between structural accuracy and artistic authenticity.

## Method Overview

We introduce the Decoupled Conditional Adaptive Time-dynamic Fusion framework (DCADif), which for the first time realizes a fine-grained decoupling of structure and style for diffusion-based inpainting, providing a new technological paradigm for the high-fidelity digital preservation of cultural heritage. By integrating a novel Decoupled Conditional Encoder with parallel pathways, a dual-stream mechanism is designed to enhance the model's ability to capture orthogonal representations: a pre-trained CLIP for structural line art and a SwinStyle Encoder for multi-scale artistic features. The framework also introduces a Time-Adaptive Feature Fusion (TAFF) module to improve the model's ability to dynamically modulate guidance throughout the denoising process. Additionally, a composite loss function is employed to effectively resolve the trade-off between pixel-level accuracy and perceptual realism. Based on the self-built large-scale dataset, MuralVerse-S, DCADif achieves state-of-the-art performance, significantly outperforming existing methods. This framework not only provides a powerful tool for restoring damaged murals but also offers new insights into achieving both structural accuracy and artistic authenticity in generative restoration.

## Code

We will upload the training scripts, testing code, and the complete
