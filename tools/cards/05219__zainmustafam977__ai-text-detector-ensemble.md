---
id: tool-05219
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector-ensemble
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/zainmustafam977/ai-text-detector-ensemble
created: 2026-07-18
updated: 2026-07-18
no: 5219
category: 一、去 AI 味 / Humanizer 库
repo: zainmustafam977/ai-text-detector-ensemble
stars: 1
url: https://github.com/zainmustafam977/ai-text-detector-ensemble
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1e5fe7e36d072033
  - methods/改稿润色指令库.md
---

# zainmustafam977/ai-text-detector-ensemble

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/zainmustafam977/ai-text-detector-ensemble
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai-detection, ai-text-detector-ensemble, claude, gpt-2, gpt-5, gradio, huggingface-spaces, llama, llama3, llm-detector, llm-detector-gradio, llm-text-detector, machine-learning, nlp, python, roberta, text-classification
- **GitHub 描述**：An ensemble AI text detector that uses RoBERTa, GPT-2 perplexity, and sentence burstiness to reliably distinguish human writing from AI-generated text. llm-text-detector. llm-detector-gradio. 
- **本地描述**：An ensemble AI text detector that uses RoBERTa, GPT-2 perplexity, and sentence burstiness to reliably distinguish human writing from AI-generated text. llm-text-detector. llm-detector-gradio.
- **拉取时间**：2026-07-25 18:10:29

---

---
title: LLM Text Detector
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

<div align="center">
  <h1>🔍 AI Text Detector Ensemble</h1>
  <p><em>A powerful, multi-model ensemble system for detecting LLM-generated text.</em></p>
  
  [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
  [![Gradio](https://img.shields.io/badge/UI-Gradio-orange.svg)](https://gradio.app/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  
  <p>
    Built for academic research in AI/NLP.<br />
    No GPU required • No API keys • Fully open-source
  </p>
</div>

---

## 🌟 Overview

As Large Language Models (LLMs) become increasingly sophisticated, distinguishing between human-written and machine-generated text is a critical challenge. This project tackles this by utilizing an **ensemble of three independent detection methods** to provide a highly accurate, robust, and transparent verdict.

Designed to detect text from frontier models including **GPT-4, Claude 3.5, Gemini, Llama 3, and DeepSeek**.

---

## ✨ Key Features

- **🧠 Ensemble Architecture:** Combines RoBERTa, GPT-2 Perplexity, and Statistical Burstiness.
- **📊 Confidence Scoring:** Computes a confidence metric based on the agreement between the three independent signals.
- **✂️ Automatic Chunking:** Intelligently splits long texts (>380 words) into overlapping windows to analyze the *entire* document, not just the introduction.
- **⚡ Fast & Local:** Runs entirely on CPU. Models are cached locally on first run.

---

## 🛠️ How It Works (The Ensemble)

| Method | What It Measures | Weight |
| :--- | :--- | :---: |
| **1. RoBERTa Classifier** | A fine-tuned transformer (`Hello-SimpleAI/chatgpt-detector-roberta`) trained on the HC3 dataset. It recognizes learned patterns from millions of human vs. AI text pairs. | **60%** |
| **2. GPT-2 Perplexity** | Measures predictability. AI text is highly predictable to other language models (low perplexity), while human text is surprising and varied (high perplexity). | **25%** |
| **3. Sentence Burstiness** | Pure statistical analysis. Measures the variation in sentence length. Humans write with rhythm (high variation); AI tends to be uniformly structured. | **15%** |

> **💡 Note on Confidence:** If all three models strongly agree, confidence is High. If signals conflict (e.g., formal human writing triggering low perplexity), confidence is Low, and the verdict is flagged for caution.

---

## 🚀 Getting Started

Follow these steps to run the AI Text Detector on your local machine.

### Prerequisites
*   **Python 3.10+** (Ensure you check "Add Python to PATH" during installation)
*   **Memory:** 8 GB RAM minimum (16 GB recommended)
*   **Storage:** ~2 GB free space (for caching Hugging Face models)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/zainmustafam977/ai-text-detector-ensemble.git
cd ai-text-detector-ensemble
```

**2. Create a Virtual Environment (Recommended)**
Open your terminal/PowerShell in the project directory:
```bash
python -m venv venv
```
Activate it:
*   **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
    *(Note: If you get a policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*
*   **Mac/Linux:** `source venv/bin/activate`

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```
*Note: The first launch will automatically download the required ML models (~500 MB). This is a one-time process.*

Once loaded, the application will open automatically in your browser at `http://localhost:7860`.

---

## 📖 Usage Guide

1. **Input:** Paste your text into the main textbox (minimum 20 words required for a reliable signal).
2. **Analyze:** Click the **"Analyse Text"** button.
3. **Review:** 
   - View the overall **Verdict** and **AI vs. Human Probabilities**.
   - Check the **Confidence Score**.
   - Navigate through the detailed tabs (`RoBERTa`, `Perplexity`, `Burstiness`) to see exactly *why* the system made its decision.

---

## ⚠️ Limitations

*Please keep these in mind when evaluating the results:*

- **Evolving Models:** Frontier models produce highly human-like text that can sometimes bypass detection.
- **Length Constraint:** Texts shorter than 50 words significantly reduce accuracy.
- **False Positives:** Highly technical, academic, or formal human writing can sometimes trigger false positives due to naturally low perplexity and low burstiness.
- **Language:** The models are explicitly optimized for **English**. A UI warning will appear if non-English input is detected.

---

## 📚 Academic References

The methodology in this project is inspired by and builds upon the following research:

1. **Guo et al. (2023)** — *How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection.* arXiv:2301.07597
2. **Mitchell et al. (2023)** — *DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.* ICML 2023.
3. **Bao et al. (2024)** — *Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.* ICLR 2024.
4. **Hans et al. (2024)** — *Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text.* ICML 2024.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
<div align="center">
  <i>Built for university AI/NLP coursework under the supervision of MAM Nitasha Arooj. All models are open-source.</i><br/>
  <b>Authors:</b> Muhammad Zain & Muhammad Umar
</div>
