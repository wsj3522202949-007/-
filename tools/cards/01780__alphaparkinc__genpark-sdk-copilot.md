---
id: tool-01780
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: genpark-sdk-copilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/alphaparkinc/genpark-sdk-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1780
category: 二、网文 / 长篇 AI 写作系统 库
repo: alphaparkinc/genpark-sdk-copilot
stars: 3
url: https://github.com/alphaparkinc/genpark-sdk-copilot
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: baa1279a6b8c2fa4
  - methods/最强写作方法论_全球最强综合版.md
---

# alphaparkinc/genpark-sdk-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alphaparkinc/genpark-sdk-copilot
- **Stars**：3
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：An autonomous SDK integration guardrail. Prevents AI hallucinations by forcing agents to ingest official `llms.txt` documentation and clone verified boilerplates before writing custom code.
- **本地描述**：An autonomous SDK integration guardrail. Prevents AI hallucinations by forcing agents to ingest official `llms.txt` documentation and clone verified boilerplates before writing custom code.
- **拉取时间**：2026-07-23 23:30:56

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# GenPark SDK Copilot (API Tamer)

Stop fighting AI code hallucinations when integrating complex, fast-moving APIs (like Stripe, Agora, Clerk, Supabase).

**GenPark SDK Copilot** is an open-source skill that serves as an autonomous guardrail for your development agent. Instead of letting the LLM guess outdated API parameters, this skill forces the agent into a strict, foolproof workflow.

## The "Tamer" Protocol
When you instruct your agent to build an integration using this skill, it is bound by these rules:
1. **Zero Hallucination Tolerance:** The agent is forbidden from relying on pre-trained weights for API calls.
2. **Mandatory Ingestion:** The agent must immediately fetch the official documentation structured for LLMs (e.g., `https://docs.provider.com/llms.txt`).
3. **Clone Before You Code:** For new projects, the agent is forbidden from scaffolding from scratch. It must use the `exec` tool to `git clone` the official Quickstart or Boilerplate repository provided by the vendor.
4. **Iterative Verification:** Only after the boilerplate is cloned and successfully running locally may the agent begin modifying the code to meet your custom requirements.

## Usage
Simply invoke the skill and tell your agent what API to integrate:
```bash
openclaw use genpark-sdk-copilot --target "Stripe Checkout in Next.js"
```

*Built by the GenPark open-source community.*
