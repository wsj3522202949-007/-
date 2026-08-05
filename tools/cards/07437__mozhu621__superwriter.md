---
id: tool-07437
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: superwriter
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/mozhu621/superwriter
created: 2026-07-18
updated: 2026-07-18
no: 7437
category: 画龙补充 / 扩容入库 — 补充源
repo: mozhu621/superwriter
stars: 36
url: https://github.com/mozhu621/superwriter
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# mozhu621/superwriter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/mozhu621/superwriter
- **Stars**：36
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：superwriter
- **拉取时间**：2026-07-25 19:21:50

---

<!-- Project Logo (replace with your file in `Fig/` as needed) -->
<p align="center">
  <img src="Fig/SuperWriter.png" width="600px" alt="SuperWriter Logo">
</p>

# 📚 SuperWriter: Reflection-Driven Long-Form Generation with Large Language Models

### Language/语言: `[English](./README.md)` | `[中文](./README_zh.md)`

<p align="center">
  📄 <a href="https://arxiv.org/abs/2506.04180">Paper</a> • 🤗 <a href="https://huggingface.co/mozhu/SuperWriter-Qwen2.5-7B/tree/main">Model&nbsp;(coming&nbsp;soon)</a>
</p>

**SuperWriter-agent** is an intelligent writing agent framework for **long-form text generation**, inspired by the human workflow of *think first, write later*.  
Through a three-stage **Plan → Write → Refine** process and **Hierarchical DPO** training, the resulting SuperWriter-LM (7 B parameters) matches or surpasses substantially larger models.

---

## 🚀 Paper at a Glance
1. **SuperWriter-Agent** explicitly injects *Thinking* and *Reflection* signals.  
2. **Hierarchical DPO + MCTS** back-propagates quality from final outputs.  
3. Scores **8.51 on WritingBench**, ranking 2 nd overall—only behind DeepSeek-R1 (671 B).

---

## 🛠️ Method Overview
<p align="center">
  <img src="Fig/Agent (1).png" width="800px" alt="SuperWriter Agent Framework">
</p>

| Stage | Roles / Sub-steps | Goal | Key Mechanisms |
|-------|-------------------|------|----------------|
| **1️⃣ Plan**   | *AI Commentators ↔ Writer*<br/>Plan Checker | • Distill topic & structure<br/>• Produce paragraph-level outline | Story-Workshop dialogue • Word-budgeting • Consistency check |
| **2️⃣ Write**  | *Thinker → Writer* | • Draft each section<br/>• Preserve chapter coherence | **Thinker Step:** bullet ideas & logic • **Writer Step:** write with previous context |
| **3️⃣ Refine** | Checker → Editor | • Polish draft<br/>• Improve language & logic | **Checker:** locate weak paragraphs • **Editor:** targeted rewrite / merge |

### Hierarchical DPO
<p align="center">
  <img src="Fig/DPO (1).png" width="800px" alt="Hierarchical DPO">
</p>

A Monte-Carlo Tree Search builds a three-layer tree *(Plan _i_, Draft _j_, Refine _k_)*.  
Leaf scores are discretized to **+2 … −2** and averaged bottom-up to create preference pairs, trained with a single DPO loss.

---

## 📈 Experimental Results

### 1. WritingBench Overall
<p align="center">
  <img src="Fig/WritingBench.png" width="600px" alt="WritingBench Results">
</p>

SuperWriter-LM tops **Academic & Engineering, Finance & Business, Politics & Law, Education** domains and is #1 among models of the same size.

### 2. User Query Win-Rate
<p align="center">
  <img src="Fig/winrate_plots.png" width="600px" alt="Win-Rate Donuts">
</p>

*Scoring*: Win = 1, Tie = 0.5, Loss = 0. Eight donut charts (the 8 th is human evaluation) show SuperWriter-LM dominating the 7 B class and remaining competitive against larger models.

---

## 🧑‍💻 Code Guide

### 1. Agent Data Generation
* `Agent/Super_write_agent.py` and `Agent/Super_write_agent_cn.py` generate three-stage (Plan / Write / Refine) SFT data for English and Chinese queries.

### 2. SFT Post-processing
* `Agent/SFT-Process.py` cleans raw agent outputs and produces unified JSONL files.

---

### 🔄 Hierarchical DPO Data Construction
1. Deploy an evaluation service for SFT models (e.g., **SGLang** or a custom HTTP API).  
2. `DPO/MCTS_inference.py` explores Plan → Write → Refine combinations via MCTS.  
3. `DPO/Step_1_query_evaluation_stand.py` creates per-query evaluation rubrics.  
4. `DPO/Step_2_LLM_judge.py` scores all MCTS leaves through the evaluation service.  
5. `DPO/create_dpo_pair.ipynb` selects good vs. bad samples to form final DPO pairs.

---

### ▶️ Inference Pipeline
Run three successive prompts—Plan, Write, Refine—using the templates in `Inference/superwrite_gen.py` to obtain the final output.

---

### 🏋️‍♂️ Training
Fine-tune with **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** and **[360-LLaMA-Factory](https://github.com/Qihoo360/360-LLaMA-Factory)**.  
Many thanks to these projects!

related:
  - methods/QUICK_START.md
---

## 🤝 Citation
```bibtex
@misc{wu2025superwriterreflectiondrivenlongformgeneration,
      title={SuperWriter: Reflection-Driven Long-Form Generation with Large Language Models}, 
      author={Yuhao Wu and Yushi Bai and Zhiqiang Hu and Juanzi Li and Roy Ka-Wei Lee},
      year={2025},
      eprint={2506.04180},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.04180}, 
}
