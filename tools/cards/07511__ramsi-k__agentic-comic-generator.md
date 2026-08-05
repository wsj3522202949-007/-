---
id: tool-07511
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: agentic-comic-generator
summary: 多 Agent 协作自动产文
source: https://github.com/ramsi-k/agentic-comic-generator
created: 2026-07-18
updated: 2026-07-18
no: 7511
category: 画龙补充 / 扩容入库 — 补充源
repo: ramsi-k/agentic-comic-generator
stars: 3
url: https://github.com/ramsi-k/agentic-comic-generator
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/QUICK_START.md
---

# ramsi-k/agentic-comic-generator

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ramsi-k/agentic-comic-generator
- **Stars**：3
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A multi-agent system that turns text prompts into illustrated comic panels using LLMs, dialogue agents, and image generation.
- **本地描述**：agentic-comic-generator
- **拉取时间**：2026-07-25 19:24:07

---

# 🎨 The Agentic Comic Generator: Bayko & Brown

![Python](https://img.shields.io/badge/language-python-blue)
![LlamaIndex](https://img.shields.io/badge/orchestrator-LlamaIndex-9cf)

## Status

🛑 Archived — Hackathon project, not under active development.

---

## ⚙️ Overview

Bayko & Brown is an experimental system where two agents collaborate:

- **Agent Brown (orchestrator)**  
  Validates prompts, manages workflow, critiques outputs, and coordinates tools.

- **Agent Bayko (generator)**  
  Uses Modal functions to run Hugging Face SDXL for image generation.

Together they generate short comic strips from a single user prompt.

---

## 🏗️ Architecture

- **Dual-agent setup** → Brown (reasoning) and Bayko (generation).
- **LlamaIndex workflows** → custom event-driven workflows with `ComicGeneratedEvent`, `CritiqueStartEvent`, `WorkflowPauseEvent`etc.
- **ReAct pattern** → Thought / Action / Observation cycle for transparency.
- **Modal functions** → serverless endpoints for SDXL generation.
- **Memory buffer** → simple history store so Brown can critique and revise Bayko’s outputs.
- **Unified memory service** → combines in-memory logs with SQLite persistence for debugging and replay.

### 🎨 **Creative AI Pipeline**

- **Prompt Enhancement**: Brown intelligently expands user prompts with narrative structure
- **Style-Aware Generation**: Automatic tagging and style consistency across panels
- **Quality Assessment**: Brown critiques Bayko's output with approval/refinement cycles
- **Multi-Format Output**: Images, subtitles, and interactive code generation

---

## 🚧 Hackathon Outcome

### What worked

- Agent architecture and workflows implemented end-to-end.
- Custom events and memory integration in LlamaIndex.
- Data capture / logging pipeline functional.

### What didn’t

- **API limits** → OpenAI caps caused failures during multi-step agent runs.
- **ReAct agent loop** → Brown sometimes looped without triggering Bayko.
- **Modal deployment** → too complex to fully stabilize during hackathon.
- **Library churn** → days after submission, LlamaIndex released new memory + orchestration features that made major parts of the custom code obsolete.

---

## 📸 Example Prompt

> “A moody K-pop idol finds a puppy. Studio Ghibli style. 4 panels.”

**What happens:**

1. Brown validates the prompt and tags it with style metadata.
2. Brown uses LlamaIndex tools to call Bayko.
3. Bayko generates 4 images + optional(future) TTS/subtitles.
4. Brown reviews and decides to approve/refine.
5. Output is saved in `storyboard/session_xxx/`.

---

## 📂 Repo Structure

```yaml
agents/
├── brown.py           # AgentBrown core class
├── brown_tools.py     # LlamaIndex tool wrappers
├── brown_workflow.py  # ReActAgent setup and toolflow
├── bayko.py           # AgentBayko executor
services/
├── agent_memory.py    # LlamaIndex memory wrapper
├── simple_evaluator.py # Refinement logic
├── session_manager.py # Handles session IDs and state
demo_pipeline.py       # Run full Brown→Bayko test
app.py                 # Gradio interface
requirements.txt
```

---

## 🔮 Reflections / Post-Mortem

This was my **first hackathon project**. I learned more about _how to hackathon_ than about shipping production code.

### Key lessons

- **Library choices matter** → LlamaIndex agents weren’t ideal for long-term memory orchestration. A cleaner design would separate agents and add a RAG memory layer, rather than force everything through LlamaIndex agents.
- **APIs are a bottleneck** → ReAct agents made too many calls; local models would have been better for testing loops.
- **Hackathon ≠ production** → I optimized for survival and demo, not maintainability.
- **Churn is real** → The week after the Hackathon ended, LlamaIndex had added memory blocks and orchestration primitives that replaced much of my custom work.

## Future

I still care about multi-agent memory and orchestration, but I’ll explore it differently in future projects (separate agent design, RAG-driven memory). This repo remains as a record of the experiment.

---

## 🎬 **Demo & Documentation**

- **Architecture Deep Dive**: `[Memory Handling Guide](./memory_handling.md)`
- **Test Suite**: Comprehensive tests in `tests/` directory
- **Modal Functions**: Production-ready SDXL and code execution in `tools/`

related:
  - methods/QUICK_START.md
---

_Let Bayko cook. Let Brown judge. Let comics happen._

📫 [LinkedIn](https://www.linkedin.com/in/ramsikalia/)  
🔗 [GitHub](https://github.com/Ramsi-K)
