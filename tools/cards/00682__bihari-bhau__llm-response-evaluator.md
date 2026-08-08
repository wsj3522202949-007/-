---
id: tool-00682
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: llm-response-evaluator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bihari-bhau/llm-response-evaluator
created: 2026-07-18
updated: 2026-07-18
no: 682
category: 二、网文 / 长篇 AI 写作系统 库
repo: bihari-bhau/llm-response-evaluator
stars: 1
url: https://github.com/bihari-bhau/llm-response-evaluator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 14489c059c000c02
  - methods/最强写作方法论_全球最强综合版.md
---

# bihari-bhau/llm-response-evaluator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bihari-bhau/llm-response-evaluator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai, evaluation, human-feedb, llm, model-eval, nlp, post-training, python, rlhf, streamlit
- **GitHub 描述**：A Streamlit tool to evaluate and compare LLM responses across 5 RLHF-inspired quality dimensions — Instruction Following, Truthfulness, Prompt Correctness, Writing Quality, and Verbosity.
- **本地描述**：A Streamlit tool to evaluate and compare LLM responses across 5 RLHF-inspired quality dimensions — Instruction Following, Truthfulness, Prompt Correctness, Writing Quality, and Verbosity.
- **拉取时间**：2026-07-23 22:58:56

---

# 🧠 LLM Response Quality Evaluator

A lightweight tool for evaluating and comparing Large Language Model (LLM) responses across **5 quality dimensions** used in real RLHF (Reinforcement Learning from Human Feedback) post-training workflows.

Built by someone doing this work daily — inspired by hands-on experience in LLM post-training evaluation at [Ethara AI](https://ethara.ai).

---

## 🎯 What It Does

Given a prompt and two model responses (A and B), this tool helps you:

- **Score** each response across 5 dimensions (1–5 scale)
- **Compare** responses side-by-side with a dimension breakdown table
- **Generate** a recommendation for which response is better and why
- **Log** every evaluation to a local JSONL file for pattern analysis
- **Surface insights** automatically after 5+ evaluations (win rates, weakest dimensions, score degradation by turn)

---

## 📊 The 5 Evaluation Dimensions

| Dimension | Description | Weight |
|---|---|---|
| 🎯 Instruction Following | Does the response follow all instructions? | High |
| ✅ Truthfulness | Is the response factually accurate? | High |
| 🔍 Prompt Correctness | Does it correctly address what was asked? | Medium |
| ✍️ Writing Quality | Is it clear, coherent, and well-written? | Medium |
| 📏 Verbosity | Is the length appropriate for the task? | Low |

> Instruction Following and Truthfulness are weighted higher — consistent with their priority in modern RLHF evaluation frameworks.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/bihari-bhau/llm-response-evaluator.git
cd llm-response-evaluator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🌐 Live Demo
👉 [Try it here](https://llm-response-evaluator.streamlit.app)

## 🖥️ How to Use

1. Paste your **prompt** in the input field
2. Select the **turn number** (1–8) and **prompt type**
3. Paste **Response A** and **Response B**
4. Rate each response on all 5 dimensions using the sliders
5. Add optional observations in the notes field
6. Click **Generate Evaluation Report**
7. View scores, dimension breakdown, and recommendation
8. All entries are auto-saved to `evaluation_log.jsonl`

---

## 📈 Pattern Insights (Auto-generated after 5+ evaluations)

The app automatically surfaces:
- **Response win rates** (A vs B)
- **Most commonly weak dimension** across all evaluations
- **Average score by turn number** — helps identify multi-turn degradation

This is useful for identifying systematic model weaknesses across prompt types and conversation lengths.

---

## 📁 Project Structure

```
llm-response-evaluator/
├── app.py               # Main Streamlit UI
├── evaluator.py         # Scoring and recommendation logic
├── requirements.txt     # Dependencies
├── evaluation_log.jsonl # Auto-generated log (gitignored)
└── README.md
```

---

## 💡 Why I Built This

During my LLM post-training internship, I noticed that manual evaluation across multi-turn conversations produces a lot of valuable signal that often goes uncaptured. This tool is my attempt to:

1. Make the evaluation process faster and more structured
2. Automatically log patterns for later analysis
3. Surface model weaknesses across turn depth and prompt types

---

## 🔭 Roadmap

- [ ] Add CSV export for full evaluation history
- [ ] Add prompt type breakdown charts
- [ ] Support for 3+ response comparison
- [ ] Integration with Hugging Face models for automated baseline scoring

---

## 🤝 Contributing

PRs welcome. If you work in LLM evaluation or post-training and have ideas to improve the scoring framework, open an issue.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License

MIT
