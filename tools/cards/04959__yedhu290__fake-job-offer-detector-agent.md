---
id: tool-04959
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: fake-job-offer-detector-agent
summary: 多 Agent 协作自动产文
source: https://github.com/yedhu290/fake-job-offer-detector-agent
created: 2026-07-18
updated: 2026-07-18
no: 4959
category: 一、去 AI 味 / Humanizer 库
repo: yedhu290/fake-job-offer-detector-agent
stars: 0
url: https://github.com/yedhu290/fake-job-offer-detector-agent
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 99e27918de1d970a
  - methods/改稿润色指令库.md
---

# yedhu290/fake-job-offer-detector-agent

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/yedhu290/fake-job-offer-detector-agent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Agentic AI Capstone Project: Fake Job Offer Detector — heuristic + LLM-reasoning pipeline that flags scam job postings from pasted text or a job link
- **本地描述**：Agentic AI Capstone Project: Fake Job Offer Detector — heuristic + LLM-reasoning pipeline that flags scam job postings from pasted text or a job link
- **拉取时间**：2026-07-25 18:00:57

---

# Fake Job Offer Detector Agent

An agentic pipeline that analyzes a job posting — pasted text, an offer
email, or a job listing **URL** — and flags signs of employment scams:
payment requests, phishing for personal/financial info, unrealistic pay,
urgency pressure tactics, suspicious link structure (shorteners, raw IPs,
risky TLDs), and more. It then produces a risk score, a verdict, and a
plain-English explanation.

Built for the **Agentic AI Capstone Project**.

## Why this is "agentic"

Rather than one monolithic classifier, the request flows through a chain of
independent tools, each a specialist for one scam pattern (payment requests,
sensitive-info phishing, urgency language, generic email domains, unrealistic
pay, vague descriptions, informal contact channels, instant-hiring claims,
suspicious link structure, etc.). An orchestrator (`backend/agent/pipeline.py`)
runs every tool, and each tool's structured output (flag, weight, evidence)
becomes input to the next stage:

```
input: pasted text and/or a job URL
  -> [if URL: run 5 URL-structure tools on the link itself]
  -> [if URL: SSRF-guarded fetch + extract visible page text]
  -> [normalize combined text] -> [11 text detector tools]
  -> [scoring/aggregation] -> [verdict]
  -> [reasoning stage: LLM if available, else template] -> result
```

When a URL is provided, the agent fetches the page itself with a hardened
fetcher (`backend/agent/fetch_tool.py`): it blocks requests to private/
loopback/link-local addresses on every redirect hop (so it can't be used to
probe internal network services), caps response size, and degrades
gracefully — if the fetch fails or is blocked, the agent still returns a
verdict based on the URL's structure alone and surfaces a clear warning in
the UI instead of erroring out.

The reasoning stage is genuinely LLM-grounded: if an `ANTHROPIC_API_KEY` is
set, the agent asks Claude to explain the verdict *using only the flags the
detector tools already found* (it's not allowed to invent new ones). Without
a key, it falls back to a template-based explanation generator, so the whole
app runs with zero external dependencies or setup.

## Project structure

```
fake-job-offer-detector-agent/
├── backend/
│   ├── agent/
│   │   ├── tools.py       # 11 text-based red-flag detector tools
│   │   ├── url_tools.py   # 5 URL-structure detector tools
│   │   ├── fetch_tool.py  # SSRF-guarded page fetcher
│   │   ├── scoring.py     # weight aggregation + verdict thresholds
│   │   ├── llm_tool.py    # Claude reasoning step + template fallback
│   │   └── pipeline.py    # orchestrator
│   ├── main.py            # FastAPI app (serves API + frontend)
│   └── requirements.txt
├── frontend/               # plain HTML/CSS/JS, no build step
│   ├── index.html
│   ├── style.css
│   └── app.js
├── sample_data/            # example postings for demoing
│   ├── sample_fake_job.txt
│   └── sample_real_job.txt
└── .env.example
```

## Running locally

Requires Python 3.10+.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open **http://localhost:8000** in a browser. Paste a job posting (or click
one of the sample buttons) and click **Analyze Posting**.

### Optional: enable Claude-generated explanations

```bash
cp .env.example .env
# edit .env and set ANTHROPIC_API_KEY=sk-ant-...
export $(cat .env | xargs)   # or use python-dotenv / your shell's method
uvicorn main:app --reload --port 8000
```

Without a key, the app still works fully — it just uses the local template
explainer instead of calling Claude.

## How scoring works

Each detector tool that fires contributes a weight (3–28 points) to a total
risk score capped at 100:

| Score range | Verdict |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 0–25 | Likely Legitimate |
| 26–55 | Suspicious — Verify Further |
| 56–100 | Likely Fake / High Risk |

See `backend/agent/tools.py` for the full list of detectors and their
reasoning, and `backend/agent/scoring.py` for the thresholds.

## Disclaimer

This tool is a heuristic aid for a capstone project, not a substitute for
professional fraud verification. Always independently verify a company and
recruiter before sharing personal information, paying money, or accepting an
offer.
