---
id: tool-05749
type: tool
area: 库
status: active
tags: [多Agent, 文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ai-slop-detector
summary: 多 Agent 协作自动产文
source: https://github.com/pranmod01/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5749
category: 一、去 AI 味 / Humanizer 库
repo: pranmod01/ai-slop-detector
stars: 0
url: https://github.com/pranmod01/ai-slop-detector
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# pranmod01/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pranmod01/ai-slop-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Multi-Agent SLM Evaluators for AI Slop Detection - Built for AWS Small Language Build Day Hackathon
- **本地描述**：Multi-Agent SLM Evaluators for AI Slop Detection - Built for AWS Small Language Build Day Hackathon
- **拉取时间**：2026-07-25 18:30:18

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Multi-Agent SLM Evaluators for AI Slop Detection

Built for [AWS Small Language Build Day Hackathon](https://app.agihouse.org/events/smalllanguagemodel-20251108)

We’re building small language models (SLMs) to detect what we call AI slop — incoherent or low-fidelity model outputs that pass naive quality filters. The goal is to determine whether lightweight evaluators can act as early warning systems for generation failure, catching low-quality outputs before they reach expensive moderation or post-processing stages.

This project explores the frontier between language model evaluation and interpretability—testing whether small, specialized models can serve as auditors for generative pipelines, not just classifiers of human vs AI text.

## Approach
Four SLMs (1–3B parameters) act as specialized evaluators, each fine-tuned with LoRA adapters on a specific signal:
- Genericity Detector: spots vague, semantically thin language
- Substance Analyzer: measures information density and topical grounding
- Style Analyzer: captures characteristic rhythm and lexical regularity of synthetic text
- Repetition Detector: flags templated or autoregressive artifacts

Each model is trained on synthetic noisy generations and evaluated for cross-model generalization across model families (e.g., GPT vs Qwen). We’re probing whether the strongest discriminative signals come from token-level entropy or longer-range syntactic structure, using ensemble voting to integrate their judgments.

## Technical Stack
- Compute: AWS Trainium (trn1.2xlarge) with Neuron SDK optimization
- Models: Qwen 2.5 (1.5B) + 4 LoRA adapters (~5MB each)
- Framework: PyTorch + Transformers + PEFT
- Dataset: HC3 + synthetic noisy generations

## Why SLMs?
- Interpretability: Specialized evaluators reveal which signals drive decisions
- Efficiency: Small models enable near real-time content evaluation
- Safety: Transparent detection pipeline for trustable model monitoring
- Scalability: 10× cheaper than large-model inference for continuous quality checks
