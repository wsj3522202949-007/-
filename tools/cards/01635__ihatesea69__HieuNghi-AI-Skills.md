---
id: tool-01635
type: tool
area: 库
status: active
tags: [RAG, Claude插件, TeX, 协议宽松, 本地优先, 英文文档, 人物设定, 本地写作]
title: HieuNghi-AI-Skills
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/ihatesea69/hieunghi-ai-skills
created: 2026-07-18
updated: 2026-07-18
no: 1635
category: 二、网文 / 长篇 AI 写作系统 库
repo: ihatesea69/HieuNghi-AI-Skills
stars: 3
url: https://github.com/ihatesea69/hieunghi-ai-skills
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f18ebb368837aec5
  - methods/最强写作方法论_全球最强综合版.md
---

# ihatesea69/HieuNghi-AI-Skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ihatesea69/hieunghi-ai-skills
- **Stars**：3
- **语言**：TeX
- **License**：MIT
- **Topics**：agent-skills, agentskills, ai-research, claude-code, cursor, deepspeed, fine-tuning, gemini-cli, github-copilot, huggingface, langchain, llm, nextjs, rag, react, vllm
- **GitHub 描述**：101 curated Agent Skills for Claude Code, GitHub Copilot, Cursor, and Gemini CLI. Covers React/Next.js, Postgres, HuggingFace ML, AI research engineering (vLLM, DeepSpeed, LangChain, RAG, fine-tuning) and dev.to blog writing.
- **本地描述**：101 curated Agent Skills for Claude Code, GitHub Copilot, Cursor, and Gemini CLI. Covers React/Next.js, Postgres, HuggingFace ML, AI research engineering (vLLM, DeepSpeed, LangChain, RAG, fine-tuning) and dev.to blog writing.
- **拉取时间**：2026-07-23 23:26:43

---

# HieuNghi-AI-Skills

A curated collection of Agent Skills for AI coding agents — covering technical blogging, web engineering, HuggingFace ML workflows, and full-stack AI research engineering. Compatible with Claude Code, GitHub Copilot, Cursor, Gemini CLI, and OpenAI Codex.

Skills follow the [agentskills.io](https://agentskills.io/) open standard.

---

## Overview

This repository contains 114 production-ready skills organized into 5 collections:

| Collection | Skills | Domain |
|---|---|---|
| `devto_skills/` | 3 | Technical blog writing for dev.to |
| `engineering_skills/` | 5 | React, Next.js, mobile, UI/UX, Postgres |
| `huggingface_skills/` | 8 | HuggingFace Hub, model training, datasets |
| `airesearch_skills/` | 85 | Full AI research lifecycle (21 categories) |
| `wordpress_skills/` | 13 | WordPress plugin/theme/block development |

---

## How It Works

Each skill is a folder containing a `SKILL.md` file. When an AI agent starts in this workspace, it reads `AGENTS.md` at the root to discover all available skills and their trigger conditions. The agent loads individual skill instructions only when a relevant task is detected, keeping context usage minimal.

```
AGENTS.md              <- AI reads this first (entry point)
devto_skills/
  blog-writer/
    SKILL.md           <- Loaded when writing a dev.to article
    rules/             <- Detailed guidelines (loaded on demand)
    metadata.json
engineering_skills/
  react-best-practices/
    SKILL.md
    rules/             <- 57 individual rule files
...
```

---

## Skill Collections

### devto_skills — Technical Blog Writing

Skills for writing high-quality technical blog posts on [dev.to](https://dev.to).

| Skill | Description |
|---|---|
| `blog-writer` | SEO-optimized article writing with frontmatter, structure templates, title formulas, tag selection, and publish checklist |
| `thumbnail-generator` | Prompts for AI image generators to create 1000x420px cover images in hand-drawn infographic style |
| `illustration-generator` | Prompts for in-article diagrams — concept maps, workflows, architecture diagrams, comparisons |

---

### engineering_skills — Web Engineering Best Practices

Curated skills from Vercel Engineering and Supabase covering React, Next.js, mobile, UI/UX, and Postgres.

| Skill | Rules | Description |
|---|---|---|
| `react-best-practices` | 57 | React/Next.js performance optimization across 8 categories: waterfalls, bundle size, server/client rendering, re-renders |
| `composition-patterns` | — | React architecture patterns: compound components, state lifting, context/reducer, polymorphic APIs |
| `react-native-skills` | 16 | React Native and Expo best practices: FlashList, Reanimated, safe areas, platform-specific patterns |
| `web-design-guidelines` | 100+ | UI/UX audit: accessibility, focus states, forms, animation, typography, images, dark mode, i18n |
| `supabase-postgres-best-practices` | 32 | Postgres optimization: query performance, connection pooling, RLS, schema design, indexing |

---

### huggingface_skills — HuggingFace ML Workflows

Skills for the complete HuggingFace ecosystem — from Hub CLI operations to model training and evaluation.

| Skill | Description |
|---|---|
| `hugging-face-cli` | Download/upload models and datasets, manage repos, run cloud jobs via the `hf` CLI |
| `hugging-face-datasets` | Create and manage datasets on HF Hub, define configs, SQL-based transformation |
| `hugging-face-model-trainer` | Fine-tune LLMs using TRL (SFT, DPO, GRPO), GGUF conversion, hardware cost estimation |
| `hugging-face-evaluation` | Add eval results to model cards, import from Artificial Analysis API, run vLLM/lighteval |
| `hugging-face-jobs` | Execute Python scripts on HF infrastructure, manage scheduled jobs, monitor status |
| `hugging-face-trackio` | Track ML experiments with Trackio, log metrics, build real-time dashboards on HF Spaces |
| `hugging-face-paper-publisher` | Publish research papers on HF Hub, link to models/datasets, claim authorship |
| `hugging-face-tool-builder` | Build reusable scripts for HF API operations, chain API calls, automate repeated tasks |

---

### airesearch_skills — AI Research Engineering (85 Skills)

Production-ready skills covering the full AI research lifecycle, maintained by Orchestra Research.

| Category | Skills |
|---|---|
| Model Architecture | LitGPT, Mamba, NanoGPT, RWKV, TorchTitan |
| Tokenization | HuggingFace Tokenizers, SentencePiece |
| Fine-Tuning | Axolotl, LLaMA-Factory, PEFT, Unsloth |
| Mechanistic Interpretability | TransformerLens, SAELens, pyvene, nnsight |
| Data Processing | NeMo Curator, Ray Data |
| Post-Training | TRL, GRPO, OpenRLHF, SimPO, verl, slime, miles, torchforge |
| Safety & Alignment | Constitutional AI, LlamaGuard, NeMo Guardrails, Prompt Guard |
| Distributed Training | DeepSpeed, FSDP, Accelerate, Megatron-Core, Lightning, Ray Train |
| Infrastructure | Modal, Lambda Labs, SkyPilot |
| Optimization | Flash Attention, bitsandbytes, GPTQ, AWQ, HQQ, GGUF |
| Evaluation | lm-eval-harness, BigCode Eval, NeMo Evaluator |
| Inference Serving | vLLM, TensorRT-LLM, llama.cpp, SGLang |
| MLOps | Weights & Biases, MLflow, TensorBoard |
| Agents | LangChain, LlamaIndex, CrewAI, AutoGPT |
| RAG | Chroma, FAISS, Pinecone, Qdrant, Sentence Transformers |
| Prompt Engineering | DSPy, Instructor, Guidance, Outlines |
| Observability | LangSmith, Phoenix |
| Multimodal | CLIP, Whisper, LLaVA, BLIP-2, SAM, Stable Diffusion, AudioCraft |
| Emerging Techniques | MoE, Model Merging, Long Context, Speculative Decoding, Distillation, Pruning |
| ML Paper Writing | LaTeX templates, citation verification |
| Research Ideation | Research Brainstorming, Creative Thinking |

---

### wordpress_skills — WordPress Development (13 Skills)

Skills from the WordPress core team covering plugin/theme development, blocks, REST API, WP-CLI, performance, and more. Targets WordPress 6.9+.

| Skill | Description |
|---|---|
| `wordpress-router` | Classifies any WP repo and routes to the correct workflow/skill automatically |
| `wp-block-development` | Gutenberg block development: block.json, attributes, dynamic rendering, deprecations |
| `wp-block-themes` | Block themes: theme.json, templates, patterns, style variations, Site Editor |
| `wp-plugin-development` | Plugin architecture, hooks, Settings API, security, cron, release packaging |
| `wp-rest-api` | REST endpoints, WP_REST_Controller, schema validation, permission callbacks |
| `wp-interactivity-api` | Interactive blocks with data-wp-* directives and @wordpress/interactivity store |
| `wp-performance` | Backend profiling: WP-CLI doctor/profile, query optimization, caching, cron |
| `wp-wpcli-and-ops` | WP-CLI: db, search-replace, multisite, cron, scripting with wp-cli.yml |
| `wp-playground` | Disposable WP instances in browser or locally via @wp-playground/cli, blueprints |
| `wp-phpstan` | PHPStan static analysis: phpstan.neon, baselines, WP-specific typing |
| `wp-abilities-api` | WP Abilities API: wp_register_ability, REST exposure, permission checks |
| `wp-project-triage` | Inspect any WP repo and generate a structured JSON triage report |
| `wpds` | Build UIs using WordPress Design System (WPDS) components and tokens |

---

## Compatibility

Skills work automatically with the following AI agents when this repository is opened as a workspace or cloned locally:

| Agent | How it loads skills |
|---|---|
| Claude Code | Reads `AGENTS.md` automatically on startup |
| GitHub Copilot (VS Code) | Reads `AGENTS.md` automatically |
| Cursor | Reads `AGENTS.md` as project rules |
| Gemini CLI | Reads `AGENTS.md` automatically |
| OpenAI Codex | Reads `AGENTS.md` automatically |

---

## Installation

Clone this repository and open it as your workspace:

```bash
git clone https://github.com/nghidanh2005/HieuNghi-AI-Skills.git
cd HieuNghi-AI-Skills
```

Open in VS Code:

```bash
code .
```

AI agents will automatically discover skills via `AGENTS.md` when the workspace is active.

---

## Adding New Skills

See [CONTRIBUTING.md](https://github.com/ihatesea69/HieuNghi-AI-Skills/blob/main/CONTRIBUTING.md) for the full guide on adding skills, including:

- Choosing the right collection
- SKILL.md format and frontmatter requirements
- Creating `rules/` subfolders for large skill sets
- Updating `AGENTS.md` in 3 places (skill table, decision tree, structure tree)
- Creating a new collection from scratch

---

## Repository Structure

```
HieuNghi-AI-Skills/
├── AGENTS.md                              <- Central AI entry point
├── README.md                              <- This file
├── CONTRIBUTING.md                        <- Guide for adding new skills
├── LICENSE                                <- MIT
├── devto_skills/
│   ├── blog-writer/
│   │   ├── SKILL.md
│   │   ├── metadata.json
│   │   └── rules/
│   ├── thumbnail-generator/
│   │   ├── SKILL.md
│   │   └── metadata.json
│   └── illustration-generator/
│       ├── SKILL.md
│       └── metadata.json
├── engineering_skills/
│   ├── react-best-practices/
│   ├── composition-patterns/
│   ├── react-native-skills/
│   ├── web-design-guidelines/
│   └── supabase-postgres-best-practices/
├── huggingface_skills/
│   ├── hugging-face-cli/
│   ├── hugging-face-datasets/
│   ├── hugging-face-model-trainer/
│   ├── hugging-face-evaluation/
│   ├── hugging-face-jobs/
│   ├── hugging-face-trackio/
│   ├── hugging-face-paper-publisher/
│   └── hugging-face-tool-builder/
└── airesearch_skills/
    ├── 01-model-architecture/
    ├── 02-tokenization/
    ├── 03-fine-tuning/
    ├── 04-mechanistic-interpretability/
    ├── 05-data-processing/
    ├── 06-post-training/
    ├── 07-safety-alignment/
    ├── 08-distributed-training/
    ├── 09-infrastructure/
    ├── 10-optimization/
    ├── 11-evaluation/
    ├── 12-inference-serving/
    ├── 13-mlops/
    ├── 14-agents/
    ├── 15-rag/
    ├── 16-prompt-engineering/
    ├── 17-observability/
    ├── 18-multimodal/
    ├── 19-emerging-techniques/
    ├── 20-ml-paper-writing/
    └── 21-research-ideation/
```

---

## Credits

Skills in this repository are curated from:

- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — React, Next.js, mobile, web design (MIT)
- [supabase/agent-skills](https://github.com/supabase/agent-skills) — Postgres best practices (MIT)
- [huggingface/skills](https://github.com/huggingface/skills) — HuggingFace ML workflows (Apache 2.0)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) — AI research engineering (MIT)
- [WordPress/agent-skills](https://github.com/WordPress/agent-skills) — WordPress development (GPL-2.0)
- Original skills by Nghi Danh — dev.to blogging kit

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT — See [LICENSE](https://github.com/ihatesea69/HieuNghi-AI-Skills/blob/main/LICENSE) for details.

Individual skill collections may reference libraries with separate licenses. See each upstream repository for details.
