---
id: tool-00783
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Co-Regulatory-Model-AI-Writing
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pegi1727/co-regulatory-model-ai-writing
created: 2026-07-18
updated: 2026-07-18
no: 783
category: 二、网文 / 长篇 AI 写作系统 库
repo: Pegi1727/Co-Regulatory-Model-AI-Writing
stars: 0
url: https://github.com/pegi1727/co-regulatory-model-ai-writing
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Pegi1727/Co-Regulatory-Model-AI-Writing

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pegi1727/co-regulatory-model-ai-writing
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Official repository for the "Co-Regulatory Model of AI-Assisted Writing" study. Featuring datasets on iterative prompting, prompt literacy, and human-AI interaction in L2 academic contexts.
- **本地描述**：Official repository for the "Co-Regulatory Model of AI-Assisted Writing" study. Featuring datasets on iterative prompting, prompt literacy, and human-AI interaction in L2 academic contexts.
- **拉取时间**：2026-07-23 23:01:51

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20609870.svg)](https://doi.org/10.5281/zenodo.20609870)

# Co-Regulatory-Model-AI-Writing

Official repository for the *Co-Regulatory Model of AI-Assisted Writing* study. This project features datasets on iterative prompting, prompt literacy, and human-AI interaction in L2 academic contexts.
## 📂 Repository Structure
- `/data`: Anonymized datasets containing linguistic indices (MTLD, MSL, LSA) across three text versions (V1, V2, V3).
- `/notebooks`: Python scripts (Jupyter Notebooks) used for statistical analysis, including Repeated Measures ANOVA and developmental trend visualizations.
- `/figures`: 
    - **Graphical Abstract:** 
      ![Graphical Abstract](figures/ga.png)
    - **Key Visualizations:**
      ![Standardized Z-scores](figures/Figure_1.png)
      ![ANOVA Results](figures/Figure_2.png)
      ![Regression Path Diagram](figures/Figure_5.png)
      *(Note: Figures 3-4 also available in this directory)*
- `/appendices`: Supplementary documentation, including the Prompt Quality Rubric (PQR) and categorized examples of prompts.
- `README.md`: Project documentation and theoretical summary.


## Project Overview

This study investigates how L2 learners engage in iterative interaction with Generative AI systems. We propose a Co-Regulatory Model that views writing improvement as an emergent outcome of shared regulation between the learner and the AI. A key contribution of this work is the conceptualization of *Prompt Literacy* as an emerging dimension of multilingual digital competence.

### Theoretical Framework: The Co-regulation Model

The research shifts the paradigm from AI as a "text generator" to a "co-regulatory learning partner." Development occurs through:

- **Iterative loops:** A recursive process of
  $\text{Planning} \rightarrow \text{Interaction} \rightarrow \text{Feedback} \rightarrow \text{Evaluation} \rightarrow \text{Revision}$
- **Prompt evolution:** The transition from functional prompts (e.g., grammar checks) to metalinguistic prompts (e.g., structuring complex syntax), which acts as the primary engine for linguistic growth.

## Key Empirical Findings

Our analysis demonstrates a significant upward trajectory across all linguistic dimensions:

| Metric | Version 1 (M ± SD) | Version 3 (M ± SD) | Effect Size ($\eta^2_p$) |
| :--- | :---: | :---: | :---: |
| Lexical Diversity (MTLD) | 62.56 ± 8.15 | 118.31 ± 11.55 | .83 |
| Syntactic Complexity (MSL) | 14.33 ± 2.45 | 26.61 ± 4.04 | .68 |
| Semantic Coherence (LSA) | 0.32 ± 0.08 | 0.65 ± 0.11 | .48 |
| Human Expert Rating | 6.03 ± 0.74 | 7.82 ± 1.12 | .72 |

*Crucial insight:* Multiple linear regression revealed that the Process Quality Rating (PQR) ($\beta = .42$) is a significantly stronger predictor of final writing success than the learner's initial L2 Proficiency ($\beta = .31$).

## 📂 Repository Structure
- `/data`: Anonymized datasets containing linguistic indices (MTLD, MSL, LSA) across three text versions (V1, V2, V3).
- `/notebooks`: Python scripts (Jupyter Notebooks) used for statistical analysis, including Repeated Measures ANOVA and developmental trend visualizations.
- `/figures`: 
  - `ga.png`: *Graphical Abstract* (Visualizing the co-regulatory loop).
  - `Figure_1.png` to `Figure_5.png`: Standardized Z-scores, ANOVA results, and Regression path diagrams.
- `/appendices`: Supplementary documentation, including the Prompt Quality Rubric (PQR) and categorized examples of prompts.
- `README.md`: Project documentation and theoretical summary.

## 🎓 Pedagogical Implications

- **Beyond Prompting:** Instruction should shift from "prompt engineering" to teaching critical evaluation and reflective decision-making.
- **Structured Iteration:** Curriculum developers should incorporate multiple, structured AI-supported revision cycles rather than single-pass editing.
- **Preserving Agency:** The model emphasizes maintaining learner agency, ensuring AI is a partner in cognition rather than a substitute for it.

## ⚠️ Limitations & Future Research
- **Sample & Duration:** Further research is needed with larger, more diverse cohorts and longitudinal designs to test the durability of gains.
- **Process Data:** Future iterations should incorporate keystroke logging, interaction logs, and think-aloud protocols to unveil the cognitive "black box" of the interaction.

## Analysis Tools

The linguistic analysis in this study was conducted using:
- **Coh-Metrix 3.0:** For multilevel analysis of text characteristics.
- **Python (Pingouin & Pandas):** For inferential statistics and data visualization.

## 🗝️ Keywords
`Generative AI` · `Human-AI Co-regulation` · `L2 Academic Writing` · `Metalinguistic Awareness` · `CALL` · `Socio-cognitive Theory` · `Self-Regulated Learning`

## Citation

If you use this data or the Co-Regulatory framework in your research, please cite the manuscript as follows:

> Merrikhi, P. (2026). *The Co-regulatory Model of AI-Assisted L2 Academic Writing: Investigating the Impact of Iterative Prompting on Textual Development*. [Manuscript submitted for publication].

## License

This project is licensed under the *Creative Commons Attribution 4.0 International (CC BY 4.0)* license.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Contact**

For inquiries regarding the data or methodology, please contact Dr. Pegah Merrikhi.

- 📧 `Deniz.qizi@gmail.com` | `Pegah.merrrikhiii@gmail.com`
- 📱 `+905369574614` (WhatsApp)
