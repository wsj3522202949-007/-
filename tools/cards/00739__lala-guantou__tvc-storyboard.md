---
id: tool-00739
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: tvc-storyboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lala-guantou/tvc-storyboard
created: 2026-07-18
updated: 2026-07-18
no: 739
category: 二、网文 / 长篇 AI 写作系统 库
repo: lala-guantou/tvc-storyboard
stars: 5
url: https://github.com/lala-guantou/tvc-storyboard
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# lala-guantou/tvc-storyboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/lala-guantou/tvc-storyboard
- **Stars**：5
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered TVC storyboard generator. 5-stage workflow for 30s TVC nine-grid panels.
- **本地描述**：AI-powered TVC storyboard generator. 5-stage workflow for 30s TVC nine-grid panels.
- **拉取时间**：2026-07-23 23:00:35

---

# tvc-storyboard

AI-powered TVC storyboard generator. Given product information, this skill guides an AI Agent through a 5-stage confirmation workflow to generate a professional 30-second TVC storyboard in the form of two 3×3 nine-grid panel images, along with video scripts and deliverable prompts.

**Works with AI coding agents**: [Claude Code](https://claude.com), [Cursor](https://cursor.com), [OpenClaw](https://openclaw.ai), and any agent that supports the `SKILL.md` format.

---

## What It Does

- Takes product briefs, brand guidelines, or raw product info as input
- Runs a 5-stage confirmation workflow: **Creative → Concept Visuals → Style → Script → Storyboard**
- Generates two 3×3 nine-grid panel images representing two 15-second segments of a 30s TVC
- Outputs structured video scripts and prompt JSON for downstream use
- Fully stateful — supports pause, resume, and backtracking to any stage

---

## Quick Start

### 1. Install the Skill

**Option A — Clone into Claude Code**

```bash
cd ~/.claude/commands/
git clone https://github.com/lala-guantou/tvc-storyboard.git
```

**Option B — Clone into OpenClaw / compatible agents**

```bash
cd <your-agent-project>/skills/
git clone https://github.com/lala-guantou/tvc-storyboard.git
```

**Option C — Download ZIP**

Download from GitHub and extract to your skills directory.

---

### 2. Configure Environment

Create a `.env` file in the project root (or in the agent's workspace root):

```bash
BLTCY_API_KEY=your_bltcy_api_key_here   # Required — BLTCY OpenAI-compatible image API
BLTCY_BASE_URL=https://api.bltcy.ai/v1   # Optional — defaults to BLTCY endpoint
GEMINI_API_KEY=your_gemini_api_key_here  # Required — Gemini for concept visual exploration
IMAGE_MODEL=gpt-image-2                   # Optional — defaults to gpt-image-2
IMAGE_SIZE=1536x1024                      # Optional — defaults to 1536x1024
```

Get your BLTCY API key at [bltcy.ai](https://bltcy.ai). Get your Gemini API key at [ai.google.dev](https://ai.google.dev).

---

### 3. Run

In your AI agent, invoke the skill with a natural language trigger:

```
Make a TVC storyboard for [product name]
```

Or use any of these keywords: `TVC`, `分镜`, `storyboard`, `九宫格`, `广告创意`, `video storyboard`, `3x3 grid`

---

## Workflow Overview

| Stage | Name | Output |
|-------|------|--------|
| 0 | Project Init | Creates project folder and state file |
| 1 | Creative Direction | Big Idea, Visual Metaphor, Film Proposition (3 directions → pick 1) |
| 1.5 | Concept Visuals | 4 concept reference images for visual direction validation |
| 2 | Brand Style | Style direction, color palette, mood, lighting, art style |
| 3 | Script | 30s script split into 2×15s segments, 9 shots per segment |
| 4 | Storyboard | Two 3×3 nine-grid panel images + delivery prompt JSON |

Every stage requires user confirmation before proceeding. You can backtrack to any previous stage at any time.

---

## Directory Structure

```
tvc-storyboard/
├── SKILL.md              # Skill definition (trigger, workflow, tool specs)
├── README.md             # This file
├── README_zh-CN.md       # 中文使用说明
├── LICENSE               # MIT License
├── .gitignore            # Excludes .env, project data, generated images
├── scripts/
│   ├── tvc.py            # Python3 — project state management, script orchestration
│   ├── volcano-gen.mjs   # Node.js — BLTCY image generation (gpt-image-2)
│   ├── gemini-gen.mjs    # Node.js — Gemini concept visual generation
│   └── requirements.txt  # Python dependencies
└── deploy.sh             # GitHub push helper
```

---

## State & Persistence

Projects are saved to `{WORKSPACE}/tvc-projects/{project-name}/state.json` with full stage history. You can pause mid-workflow and resume later:

```bash
# View current project status
python3 scripts/tvc.py status

# Load an existing project
python3 scripts/tvc.py load "project-name"

# List all projects
python3 scripts/tvc.py projects
```

---

## Prerequisites

- Python 3.8+
- Node.js 18+
- BLTCY API Key (for `gpt-image-2`)
- Gemini API Key (for concept visuals)

---

## Author

**lala 罐头** — Available on Douyin, Xiaohongshu, and Bilibili.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT — free to use, modify, and distribute. See [LICENSE](https://github.com/lala-guantou/tvc-storyboard/blob/main/LICENSE).
