---
id: tool-01482
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: CoDi
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/speeditidious/codi
created: 2026-07-18
updated: 2026-07-18
no: 1482
category: 二、网文 / 长篇 AI 写作系统 库
repo: Speeditidious/CoDi
stars: 16
url: https://github.com/speeditidious/codi
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Speeditidious/CoDi

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/speeditidious/codi
- **Stars**：16
- **语言**：Python
- **License**：MIT
- **Topics**：large-language-models, multi-agent-systems, narrative-generation, story-generation
- **GitHub 描述**：[AIIDE 2025] Official code for "CoDi: A Director-Actor Framework for Goal-Driven Interactive Story Generation with LLMs"
- **本地描述**：[AIIDE 2025] Official code for "CoDi: A Director-Actor Framework for Goal-Driven Interactive Story Generation with LLMs"
- **拉取时间**：2026-07-23 23:22:19

---

# CoDi: A Director-Actor Framework for Goal-Driven Interactive Story Generation with LLMs

**CoDi** adopts a director–actor paradigm to generate stories from user input through the collaboration of planner, character, director, and editor agents. The framework focused on empowering the control capabilities of the director agent. Our paper has been accepted by AIIDE 2025.

!`[CoDi Architecture](./images/CoDi_Method_Figure.png)`

---

## 🚀 Setup

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure API Keys
Set up your API keys in `./scripts/env.sh`:
```bash
export OPENAI_API_KEY="Your API Key"
export DEEPSEEK_API_KEY="Your API Key"
export GOOGLE_API_KEY="Your API Key"
```

---

## 📖 Generate a Story

Run CoDi with:
```bash
./scripts/generate.sh
```

---

## ✍️ Use Your Own Story Prompt

By default, CoDi uses the example prompt in `./data/example.jsonl`.  
You can customize this file to create your own stories. CoDi’s agents will automatically set the story world and simulate narratives based on your input.

Example format:
```jsonl
{"example_id": "story_id_1", "inputs": "Describe the story you want in natural language."}
{"example_id": "story_id_2", "inputs": "Another story prompt."}
```

---

## ⚙️ Arguments

You can configure `./scripts/generate.sh` with the following options:

- `--planner-agent-base-model`: Backbone LLM for the planner agent. *(default: gpt-4o-2024-11-20)*  
- `--director-agent-base-model`: Backbone LLM for the director agent. *(default: gemini-2.0-flash)*  
- `--character-agent-base-model`: Backbone LLM for the character agent. *(default: gemini-2.0-flash)*  
- `--editor-agent-base-model`: Backbone LLM for the editor agent. *(default: gemini-2.0-flash)*  
- `--plan-mode`: Enable predefined 4-part plot structure theory.
- `--act-seq-mode`: Convert story objectives into a sequence of acts. This produces a more detailed structure. *(Currently available only with plan mode; not included in the paper.)*
- `--reformat-novel`: Edit the simulated story into novel format. By default, a screenplay format is used.
- `--max-turn`: Maximum number of turns. CoDi automatically concludes the story when the number of turns exceeds this value. Increase the value for longer stories. *(default: 200)* 
- `--max-turn-part`: Available with plan-mode. Maximum number of turns per part. *(default: 200)* 
- `--max-turn-act`: Available with act-seq-mode. Maximum number of turns per act. *(default: 50)*
- `--setting-file`: Path to the data for using the same initial settings (Setup, Characters, Plan, The first turn of the story).
- `--load-file`: Path to the data to load. This option allows CoDi to resume without regenerating from the beginning even though the process is interrupted.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📚 Citation
```
@inproceedings{kim2025codi,
  title={CoDi: A Director-Actor Framework for Goal-Driven Interactive Story Generation with LLMs},
  author={Kim, Honggu and Yoo, Taewoo and Cheong, Yun-Gyung},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment},
  volume={21},
  number={1},
  pages={70--80},
  year={2025}
}
```
