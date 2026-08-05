---
id: tool-05220
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: AI-TEXT-DETECTOR
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/simigo-t/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5220
category: 一、去 AI 味 / Humanizer 库
repo: Simigo-T/AI-TEXT-DETECTOR
stars: 0
url: https://github.com/simigo-t/ai-text-detector
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Simigo-T/AI-TEXT-DETECTOR

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/simigo-t/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Simigo-T/AI-TEXT-DETECTOR
- **拉取时间**：2026-07-25 18:10:31

---

# # AI Text Detector — Detecting LLM-Generated Text

A machine learning classifier that distinguishes AI-generated 
text from human-written text using statistical watermarking 
techniques and Random Forest.

Built as part of a research study at Stockholm University, 
Department of Computer and Systems Sciences, 2025.

## Results

| Dataset | Accuracy |
|---------|----------|
| Original (OD) | 98.17% |
| Softly Paraphrased (SPD) | 99.22% |
| Medium Paraphrased (MPD) | 99.24% |
| Hard Paraphrased (HPD) | 96.36% |

### Robustness against AI-humanizer (Word Spinner)

| Iteration | Accuracy |
|-----------|-------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| WS0 (original) | 100% |
| WS1 | 95% |
| WS2 | 80% |
| WS3 | 80% |

## Dataset
- 28,000 essays from Kaggle (50% human-written, 50% LLM-generated)
- Four dataset variants with increasing paraphrasing difficulty
- Additional sample tested against Word Spinner AI-humanizer

## Methodology
- Random Forest classifier (80/20 train/test split)
- Four models trained on each dataset variant
- LIME explainability for model transparency and interpretability
- Black-box detection approach using statistical watermarking

## Key Findings
- Statistical watermarking is effective for detecting LLM-generated text
- ChatGPT paraphrasing had limited impact on model performance
- AI-humanizer tools are significantly more effective at evading 
  detection — accuracy dropped from 100% to 60% after three iterations
- LIME successfully visualized statistical watermarks left by LLMs

## Tech Stack
- Python (Jupyter Notebook)
- Scikit-learn (Random Forest)
- Pandas / NumPy
- LIME

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Download dataset from Kaggle and place in project folder
4. Run `main1.ipynb` for model training and evaluation
5. Run `LimeExplanation.ipynb` for LIME visualization

## Dataset
- essays from Kaggle (50% human-written, 50% LLM-generated)
- Download the dataset here: [Kaggle Dataset](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text)
- Place the file in the project folder before running the notebooks

## Research Paper
This project is based on a published research study:

**"Detection Model To Classify Human-written From 
AI-generated Text And Investigation of Its Robustness 
To Paraphrasing"**


[📄 Read the full paper](research_paper.pdf)
