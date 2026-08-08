---
id: tool-05551
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/cvexa/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5551
category: 一、去 AI 味 / Humanizer 库
repo: cvexa/ai-text-detector
stars: 0
url: https://github.com/cvexa/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9929a817725af806
  - methods/改稿润色指令库.md
---

# cvexa/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/cvexa/ai-text-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A NestJS-based API that analyzes text to determine the probability of it being AI-generated
- **本地描述**：A NestJS-based API that analyzes text to determine the probability of it being AI-generated
- **拉取时间**：2026-07-25 18:22:53

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector API

A NestJS-based API that analyzes text to determine the probability of it being AI-generated.

## Features

- Text analysis for AI-generated content detection
- Probability score with confidence rating
- Multiple analysis features:
  - Repetitive patterns detection
  - Text complexity analysis
  - Natural language patterns analysis

## Installation

```bash
npm install
```

## Running the app

```bash
# development
npm run start

# watch mode
npm run start:dev

# production mode
npm run start:prod
```

## API Usage

### Analyze Text

```http
POST /text-analysis/analyze
Content-Type: application/json

{
  "text": "Your text to analyze here"
}
```

#### Response

```json
{
  "aiProbability": 0.75,
  "confidence": 0.85,
  "features": {
    "repetitivePatterns": 0.6,
    "complexityScore": 0.8,
    "naturalityScore": 0.7
  }
}
```

- `aiProbability`: Number between 0 and 1 indicating the likelihood of AI-generated text (higher = more likely AI-generated)
- `confidence`: Confidence level of the analysis (higher = more confident)
- `features`: Detailed scores for different analysis aspects

## Testing

```bash
# unit tests
npm run test

# test coverage
npm run test:cov
``` 
