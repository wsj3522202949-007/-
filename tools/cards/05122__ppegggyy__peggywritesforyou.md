---
id: tool-05122
type: tool
area: 库
status: active
tags: [去AI味, 多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: peggywritesforyou
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/ppegggyy/peggywritesforyou
created: 2026-07-18
updated: 2026-07-18
no: 5122
category: 一、去 AI 味 / Humanizer 库
repo: ppegggyy/peggywritesforyou
stars: 3
url: https://github.com/ppegggyy/peggywritesforyou
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f9a3cadff1ec6677
  - methods/改稿润色指令库.md
---

# ppegggyy/peggywritesforyou

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ppegggyy/peggywritesforyou
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：PeggyWritesForYou: A SOTA multi-agent adversarial text humanizer. It bypasses AI detection (GPTZero, Turnitin) via a Live Adversarial Feedback Loop, 4-axis prompt attacks, and multi-detector cross-validation. Running locally on consumer hardware, it restructures text to destroy AI statistical fingerprints while preserving meaning.
- **本地描述**：PeggyWritesForYou: A SOTA multi-agent adversarial text humanizer. It bypasses AI detection (GPTZero, Turnitin) via a Live Adversarial Feedback Loop, 4-axis prompt attacks, and multi-detector cross-validation. Running locally on consumer hardware, it restructures text to destroy AI statistical fingerprints while preserving meaning.
- **拉取时间**：2026-07-25 18:06:57

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# PeggyWritesForYou: SOTA Adversarial Text Humanizer

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.0.0-lightgrey.svg)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

An advanced, multi-agent adversarial pipeline designed to restructure AI-generated text to bypass modern detection systems (like GPTZero, Sapling, Turnitin, and Originality.ai). 

Unlike standard "humanizer" scripts that rely on simple paraphrasing (which modern detectors are trained to flag), this project implements a Live Adversarial Feedback Loop backed by a Multi-Detector Ensemble, running efficiently on consumer-grade hardware (4GB VRAM / 16GB RAM).

## The V2 Architecture (How It Works)

Recent NLP research indicates that blind LLM paraphrasing actually increases AI detection rates because the token probability distribution remains mathematically predictable. This system solves that using a 6-pillar SOTA architecture:

### 1. The Adversarial Feedback Loop
Instead of guessing what a detector will flag, the system queries an ensemble of detectors, extracts the specific failure scores, and feeds them directly back into the LLM prompt (e.g., "This sentence scored 87% AI. Rewrite it to disrupt contextual perplexity."). 

### 2. Multi-Detector Cross-Validation
Before text is finalized, it must survive an offline/online hybrid gauntlet:
* Local RoBERTa (`roberta-base-openai-detector`) for rapid pre-filtering.
* Sapling AI API for perplexity-based Transformer analysis.
* ZeroGPT API for burstiness variance scoring.

### 3. 4-Axis Adversarial Prompting
When a sentence fails, the system rotates through targeted mathematical attacks based on the attempt round:
* Round 1 (Token Unpredictability): Spikes token-level perplexity.
* Round 2 (Structural Disruption): Alters the syntactic tree structure.
* Round 3 (Register Shift): Forces the LLM into a different latent vocabulary space.
* Round 4 (Rhythm Attack): Breaks standard n-gram phrasing and forces burstiness.

### 4. Paragraph Escalation Protocol
If surgical sentence-level rewrites fail to drop the score (>=50% of the paragraph remains flagged), the pipeline triggers a full structural "nuke," regenerating the entire paragraph from raw semantic bullet points to destroy the original AI contextual fingerprint.

### 5. Rotating Pivot Languages
To prevent detectors from identifying a fixed "back-translation fingerprint," the pipeline randomly rotates its pivot language (DE, FR, ES, IT, PT) via NLLB-200 during the syntactic scrambling phase.

### 6. The Human-in-the-Loop UI
No automated system is perfect. Sentences that survive all 3 adversarial rounds are passed to a Needs Review panel in the Flask UI. Clicking a flagged sentence instantly opens a "Re-Roll" modal for a rapid, 30-second manual human edit—the ultimate cheat code for 0% detection.

## Tech Stack & Requirements

* Frontend: HTML5, CSS3, Vanilla JS (Retro Terminal UI)
* Backend: Python, Flask
* NLP Processing: NLTK, spaCy (`en_core_web_sm`)
* Local Inference: HuggingFace Transformers (CPU-optimized)
* Translation: `facebook/nllb-200-distilled-600M`
* LLM Engine: Groq API (Llama-3 models), OpenRouter fallbacks

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/ppegggyy/peggywritesforyou.git](https://github.com/ppegggyy/peggywritesforyou.git)
   cd peggywritesforyou
Install the dependencies:

Bash
pip install -r requirements.txt
Download the required spaCy model:

Bash
python -m spacy download en_core_web_sm
Run the application:

Bash
python app.py
The app will be available locally at http://127.0.0.1:5000.

Environment Variables
You will need API keys for the LLM providers and detectors. Configure these in the UI or export them in your environment:

GROQ_API_KEY

SAPLING_API_KEY (Free tier)

ZEROGPT_API_KEY (Free tier)

Disclaimer
This tool is built as a proof-of-concept for adversarial machine learning and NLP evasion techniques. It is intended for educational and research purposes only. Users are solely responsible for how they utilize this software.
