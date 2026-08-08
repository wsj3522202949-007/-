---
id: tool-01532
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: multimind-story
summary: 多 Agent 协作自动产文
source: https://github.com/msrain0625/multimind-story
created: 2026-07-18
updated: 2026-07-18
no: 1532
category: 二、网文 / 长篇 AI 写作系统 库
repo: msrain0625/multimind-story
stars: 1
url: https://github.com/msrain0625/multimind-story
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5b6f9f7bbfa837f7
  - methods/最强写作方法论_全球最强综合版.md
---

# msrain0625/multimind-story

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/msrain0625/multimind-story
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Multi-agent AI story generator — text · image · layout
- **本地描述**：Multi-agent AI story generator — text · image · layout
- **拉取时间**：2026-07-23 23:23:46

---

# multimind-story

A multi-agent pipeline that turns a one-line idea into an illustrated storybook (HTML/PDF).

Three agents run in sequence: one writes the story, one generates scene images, one composes the final layout. Each agent has a single responsibility and communicates through a shared `StoryContext` object.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Motivation

I kept running into the same friction when prototyping story-based content: LLMs are good at narrative text, and image generation models are good at visuals, but gluing them together always required manual back-and-forth. This project automates that handoff. You give it an idea, it gives you a complete document.

## How it works

```
idea (str)
  └─> StoryAgent     — calls LLM, returns structured chapters + scene prompts
        └─> ImageAgent    — generates one image per scene (async, parallel)
              └─> LayoutAgent  — merges text + images into HTML, optionally exports PDF
```

The `StoryAgent` prompts the model to return structured JSON with chapter content and a visual scene description for each chapter. That scene description goes directly into the `ImageAgent` as a generation prompt — no manual rewriting needed.

`ImageAgent` runs all image requests concurrently via `asyncio`. If Stability AI fails it falls back to DALL-E; if neither key is present it writes a placeholder image so the rest of the pipeline still completes.

`LayoutAgent` uses a Jinja2 template and WeasyPrint for the PDF export. The HTML output works standalone with no external dependencies.

## Setup

```bash
git clone https://github.com/msrain0625/multimind-story
cd multimind-story
python -m venv venv && venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
# fill in your API keys, then:
python quick_test.py   # verify the LLM connection
python app.py          # start Gradio UI at localhost:7860
```

## Configuration

The LLM backend is swappable. Defaults to Kimi (Moonshot) since it's cheap and the API is OpenAI-compatible. Set `LLM_PROVIDER` in `.env` to switch:

```
LLM_PROVIDER=kimi       # moonshot-v1-8k  (default)
LLM_PROVIDER=openai     # gpt-4o-mini
LLM_PROVIDER=deepseek   # deepseek-chat
```

Image generation requires either `STABILITY_API_KEY` or `OPENAI_API_KEY`. If both are missing the pipeline still runs — chapters get placeholder images instead.

## Project layout

```
backend/
  agents/
    story_agent.py    # LLM call + JSON parsing
    image_agent.py    # async image generation, Stability AI + DALL-E
    layout_agent.py   # Jinja2 → HTML, WeasyPrint → PDF
pipeline.py           # orchestrates the three agents
app.py                # Gradio UI
quick_test.py         # sanity check without starting the UI
```

## Notes

- Story generation with `moonshot-v1-8k` takes roughly 15–30s for 3 chapters.
- Image generation runs in parallel — 3 images adds about 10–20s depending on the API.
- WeasyPrint requires system-level dependencies on Windows (see [their docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)). PDF export is optional; HTML output works without it.
- `.env` is gitignored. Never commit your keys.

## Stack

Python 3.10+, OpenAI SDK, Gradio, Jinja2, WeasyPrint, Pillow, aiohttp
