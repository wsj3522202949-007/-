---
id: tool-00070
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划]
title: n8n-ollama-blog-writer
summary: 搭大纲/分卷/节拍
source: https://github.com/bonskari/n8n-ollama-blog-writer
created: 2026-07-18
updated: 2026-07-18
no: 70
category: 二、网文 / 长篇 AI 写作系统 库
repo: bonskari/n8n-ollama-blog-writer
stars: 0
url: https://github.com/bonskari/n8n-ollama-blog-writer
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f8680b87a8a48d29
  - methods/最强写作方法论_全球最强综合版.md
---

# bonskari/n8n-ollama-blog-writer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bonskari/n8n-ollama-blog-writer
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：ai, automation, blog, blog-writer, blog-writing, content-creation, content-generation, local-ai, n8n, no-api-keys, ollama, privacy, self-hosted, workflow, writing
- **GitHub 描述**：Free n8n workflow: AI-powered blog writer pipeline using Ollama. Research, outline, draft, and edit blog posts with local AI. No API keys needed.
- **本地描述**：Free n8n workflow: AI-powered blog writer pipeline using Ollama. Research, outline, draft, and edit blog posts with local AI. No API keys needed.
- **拉取时间**：2026-07-23 22:40:55

---

# Free n8n Workflow: AI Blog Writer Pipeline (Ollama)

**Research, outline, draft, and edit blog posts with local AI — no API keys, no costs, no data leaving your machine.**

Enter a topic, get a polished blog post through a 4-stage AI pipeline: research → outline → draft → edit. Runs 100% locally with Ollama.

> This is **1 of 11 production-ready workflows** from the [Self-Hosted AI Workflow Pack for n8n + Ollama](https://bonskari.github.io/n8n-ai-workflows/). The full pack ($39, one-time) includes social media content generation, email auto-response, lead scoring, document summarization, and more.

---

## What This Workflow Does

```
You enter a topic + tone + word count
    |
    v
Stage 1: AI researches key points and angles
    |
    v
Stage 2: AI creates a structured outline
    |
    v
Stage 3: AI writes the full blog post draft
    |
    v
Stage 4: AI edits for grammar, flow, and SEO
    |
    v
You get a polished, ready-to-publish blog post
```

- **4-stage pipeline** mimics a real editorial process
- **Customizable tone and length** — from casual 500-word posts to formal 2000-word guides
- **SEO-aware editing** — the final pass optimizes for readability and search
- Runs 100% locally with Ollama — zero API costs

---

## Requirements

| Requirement | Details |
|---|---|
| **n8n** | Self-hosted, v1.0+ ([install guide](https://docs.n8n.io/hosting/)) |
| **Ollama** | Running on localhost:11434 ([install guide](https://ollama.ai/download)) |
| **Model** | Any Ollama model — `llama3:8b` recommended (larger models = better quality) |

---

## Setup (5 minutes)

### 1. Install Ollama and pull a model

```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3:8b
```

### 2. Import the workflow into n8n

1. Download `workflow.json` from this repo (or copy the JSON below)
2. In n8n: **Workflows** → **Add Workflow** → **...** menu → **Import from JSON**
3. Paste/upload and click **Import**

### 3. Customize

Open the **"Blog Parameters"** node and set:
- **topic** — What you want to write about
- **tone** — "professional", "casual", "technical", etc.
- **word_count** — Target length (e.g., 1500)

### 4. Run it

Click **Execute Workflow**. The 4-stage pipeline takes 2-5 minutes depending on your hardware and model size.

---

## Workflow JSON

Import `workflow.json` from this repo, or copy the JSON below into n8n:

<details>
<summary>Click to expand workflow JSON</summary>

See the `workflow.json` file in this repository.

</details>

---

## Tips for Better Results

- **Use `llama3:70b` or `mixtral:8x7b`** if your hardware supports it — dramatically better writing quality
- **Be specific with topics** — "How to set up Prometheus monitoring for Docker containers" beats "monitoring"
- **Adjust word count** — Longer posts (1500+) tend to be higher quality since the AI has more room to develop ideas
- **Run it multiple times** — Each run produces different content. Pick the best version.

---

## Example Output

Input: `topic: "Why developers should self-host their AI tools"`, `tone: "conversational"`, `word_count: 1000`

The pipeline produces a ~1000 word blog post with:
- Engaging introduction with a hook
- 3-4 well-developed sections with subheadings
- Practical examples and actionable advice
- SEO-optimized conclusion with a call to action

---

## Want All 11 Workflows?

This is just one workflow from the full pack. The **Self-Hosted AI Workflow Pack** includes:

| # | Workflow | What It Does |
|---|---|---|
| 1 | **AI Blog Writer Pipeline** | 4-stage blog post creation (this one) |
| 2 | **AI Social Media Generator** | Multi-platform content from a single topic |
| 3 | **AI YouTube-to-Newsletter** | Turn any YouTube video into an email newsletter |
| 4 | **AI Content Repurposer** | One blog post → 6 platform-specific pieces |
| 5 | **AI Lead Scorer** | Score and enrich incoming leads automatically |
| 6 | **AI Competitor Monitor** | Weekly competitor intelligence briefings |
| 7 | **AI Email Auto-Responder** | Classify emails, filter spam, draft replies |
| 8 | **AI Support Ticket Router** | Triage tickets by category, priority, sentiment |
| 9 | **AI Document Summarizer** | Summarize docs with Q&A generation |
| 10 | **AI Meeting Notes** | Structured summaries with action items |
| 11 | **AI Data Extractor** | Pull structured JSON from unstructured text |

All workflows run locally with Ollama. No API keys. No monthly fees. One-time purchase.

**[Get the full pack for $39 →](https://bonskari.github.io/n8n-ai-workflows/)**

---

## License

This free sample workflow is released under the MIT License.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

If this saved you time, give it a ⭐. It helps others find it.
