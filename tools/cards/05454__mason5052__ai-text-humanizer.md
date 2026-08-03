---
id: tool-05454
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-text-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/mason5052/ai-text-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5454
category: 一、去 AI 味 / Humanizer 库
repo: mason5052/ai-text-humanizer
stars: 0
url: https://github.com/mason5052/ai-text-humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# mason5052/ai-text-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mason5052/ai-text-humanizer
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Transform AI-generated text into natural, human-sounding writing. Multi-pass pipeline with 4 measurable linguistic metrics. Powered by local LLMs via LM Studio.
- **本地描述**：Transform AI-generated text into natural, human-sounding writing. Multi-pass pipeline with 4 measurable linguistic metrics. Powered by local LLMs via LM Studio.
- **拉取时间**：2026-07-25 18:19:17

---

# AI Text Humanizer

A web-based tool that transforms AI-generated text into natural, human-sounding writing. Uses open-source LLMs hosted locally via LM Studio -- zero API cost.

## How It Works

The humanization pipeline uses 4 measurable linguistic metrics to detect AI patterns, then iteratively rewrites the text to reduce them:

| Metric | What It Measures | AI Text | Human Text |
|--------|-----------------|---------|------------|
| **Perplexity** | Word predictability (via LLM logprobs) | Low, uniform | High, variable |
| **Burstiness** | Sentence length variance | Low (uniform lengths) | High (mixed short/long) |
| **Vocabulary** | AI-typical word frequency | High ("moreover", "utilize") | Low (everyday words) |
| **Structure** | Sentence pattern diversity | Low (repetitive) | High (varied) |

### Pipeline Flow

```
Original text -> Analyze (4 metrics) -> LLM Rewrite -> Re-analyze
                                            ^                |
                                            |    (loop if score > threshold)
                                            +----------------+
                                                     |
                                              Post-process -> Final output
```

1. **Analyze**: Compute all 4 metrics on input text
2. **Rewrite**: LLM rewrites with prompt targeted at weakest metrics
3. **Re-analyze**: Check if score improved enough
4. **Repeat**: If score still above threshold, rewrite again (max 3 iterations)
5. **Post-process**: Rule-based cleanup (replace AI vocabulary, fix patterns)

## Setup

### Prerequisites

- Python 3.11+
- [LM Studio](https://lmstudio.ai/) with a model loaded and local server enabled (port 1234)

### Recommended Models (for LM Studio)

Any instruction-following model works. Good options:
- Qwen 2.5 7B/14B Instruct
- Llama 3.1 8B Instruct
- Mistral 7B Instruct v0.3

### Installation

```bash
git clone https://github.com/mason5052/ai-text-humanizer.git
cd ai-text-humanizer
pip install -r requirements.txt
```

### Run

1. Start LM Studio and load a model. Enable the local server (default port 1234).
2. Start the web app:

```bash
uvicorn app.main:app --reload --port 8000
```

3. Open http://localhost:8000 in your browser.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Web UI |
| POST | `/api/humanize` | Full humanization pipeline |
| POST | `/api/analyze` | Standalone text analysis (metrics only) |
| GET | `/api/health` | Service health check |

### POST /api/humanize

```json
{
    "text": "Your AI-generated text here...",
    "max_iterations": 3,
    "threshold": 0.45
}
```

### POST /api/analyze

```json
{
    "text": "Any text to check for AI patterns..."
}
```

## Configuration

Set via environment variables (prefix `HUMANIZER_`) or `.env` file:

| Variable | Default | Description |
|----------|---------|----------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `HUMANIZER_LM_STUDIO_BASE_URL` | `http://localhost:1234/v1` | LM Studio API URL |
| `HUMANIZER_MAX_ITERATIONS` | `3` | Max rewrite iterations |
| `HUMANIZER_SCORE_THRESHOLD` | `0.45` | Target score (0=human, 1=AI) |
| `HUMANIZER_TEMPERATURE` | `0.7` | LLM generation temperature |

## License

MIT
