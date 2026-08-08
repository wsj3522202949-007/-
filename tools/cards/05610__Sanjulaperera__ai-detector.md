---
id: tool-05610
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sanjulaperera/ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5610
category: 一、去 AI 味 / Humanizer 库
repo: Sanjulaperera/ai-detector
stars: 1
url: https://github.com/sanjulaperera/ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: fd5d7db1283a3502
  - methods/改稿润色指令库.md
---

# Sanjulaperera/ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sanjulaperera/ai-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai, aidetection, open-source, python
- **GitHub 描述**：Hybrid ensemble system for detecting AI-generated text using statistical (Binoculars), neural (DeBERTa), and stylometric analysis. FastAPI backend with dynamic perplexity-based weighting.
- **本地描述**：Hybrid ensemble system for detecting AI-generated text using statistical (Binoculars), neural (DeBERTa), and stylometric analysis. FastAPI backend with dynamic perplexity-based weighting.
- **拉取时间**：2026-07-25 18:25:04

---

# AI Detector

A hybrid ensemble system for detecting AI-generated text, combining statistical analysis, neural networks, and stylometric features.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This project implements a state-of-the-art AI text detector that uses an ensemble approach combining three complementary detection methods:

1. **Statistical Analysis (Binoculars)** - Zero-shot perplexity-based detection
2. **Neural Discriminator (DeBERTa)** - Supervised transformer classification
3. **Stylometric Analysis** - Linguistic feature extraction

The ensemble fusion uses dynamic weighting based on text perplexity to optimize detection accuracy.

## Features

- 🔍 **Multi-path detection** - Three independent analysis methods for robust detection
- ⚡ **FastAPI backend** - High-performance async API with automatic documentation
- 🎯 **Dynamic weighting** - Adaptive ensemble weights based on input characteristics
- 🛡️ **Adversarial resistance** - Text sanitization against evasion attacks
- 📊 **Detailed metrics** - Comprehensive breakdown of detection signals

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Sanjulaperera/ai-detector.git
cd ai-detector

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive documentation is at `http://localhost:8000/docs`.

### API Usage

```bash
curl -X POST "http://localhost:8000/detect" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to analyze here..."}'
```

**Response:**
```json
{
  "final_score": 0.72,
  "verdict": "AI-Generated",
  "details": {
    "binoculars_score": 0.85,
    "neural_score": 0.68,
    "stylometric_score": 0.80,
    "metrics": {
      "ttr": 0.45,
      "entropy": 3.2,
      "burstiness": 0.15
    },
    "perplexity": 45.3
  }
}
```

### CLI Testing

```bash
# Run with sample texts
python test_script.py

# Analyze specific text
python test_script.py -t "Text to analyze"

# Analyze a file
python test_script.py -f document.txt
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_main.py -v
```

## Project Structure

```
ai-detector/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and endpoints
│   ├── ensemble.py          # Ensemble detector orchestration
│   ├── preprocessing.py     # Text sanitization utilities
│   └── modules/
│       ├── __init__.py
│       ├── statistical.py   # Binoculars perplexity detector
│       ├── classifier.py    # Neural discriminator (DeBERTa)
│       └── stylometry.py    # Stylometric feature extraction
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── test_main.py         # Test suite
├── test_script.py           # CLI testing tool
├── requirements.txt
└── README.md
```

---

## Technical Deep Dive

### Architecture Overview

The AI Detector uses a **3-path ensemble architecture** where each path analyzes text independently, and results are fused using adaptive weighting.

```
                    ┌─────────────────────┐
                    │    Input Text       │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Preprocessing     │
                    │  (Sanitization)     │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │   Path A:    │    │   Path B:    │    │   Path C:    │
   │  Statistical │    │   Neural     │    │ Stylometric  │
   │ (Binoculars) │    │  (DeBERTa)   │    │  (Features)  │
   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  Adaptive Fusion  │
                    │ (PPL Weighting)   │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Final Score     │
                    │    & Verdict      │
                    └───────────────────┘
```

### Path A: Statistical Detector (Binoculars)

**Algorithm**: Binoculars (Hans et al., 2024)

The Binoculars method compares how two language models of different sizes perceive the same text. AI-generated text typically shows distinctive perplexity patterns between observer and performer models.

**Formula:**
```
Score = log(PPL_observer) / log(PPL_performer)
```

**Implementation Details:**
- **Observer Model**: GPT-2 (smaller, 124M parameters)
- **Performer Model**: GPT-2 Medium (larger, 355M parameters)
- **Key Insight**: AI text has lower perplexity on larger models, creating consistent ratios

**Code Location**: `app/modules/statistical.py`

```python
class BinocularsDetector:
    def score(self, text: str) -> float:
        loss_observer = self._calculate_perplexity(text, self.observer_model, ...)
        loss_performer = self._calculate_perplexity(text, self.performer_model, ...)
        return loss_observer / loss_performer
```

### Path B: Neural Discriminator

**Algorithm**: Fine-tuned DeBERTa-v3

A supervised transformer model trained to classify text as human or AI-generated by learning semantic patterns.

**Implementation Details:**
- **Base Model**: microsoft/deberta-v3-small
- **Task**: Binary sequence classification
- **Output**: Probability score [0.0 = human, 1.0 = AI]

**Code Location**: `app/modules/classifier.py`

> **Note**: For production use, replace the base model with a checkpoint fine-tuned on AI detection datasets (e.g., from Hugging Face's AI detection models).

### Path C: Stylometric Analyst

**Algorithm**: Linguistic feature extraction

Extracts interpretable writing style features that differ between human and AI text.

**Features Extracted:**

| Feature | Description | AI Indicator |
|---------|-------------|--------------|
| **Type-Token Ratio (TTR)** | Lexical diversity (unique words / total words) | Lower TTR |
| **Shannon Entropy** | Word distribution randomness | Different patterns |
| **Burstiness** | Variance of sentence complexity (σ/μ of perplexity) | Lower burstiness |

**Burstiness Formula:**
```
B = std(sentence_perplexities) / mean(sentence_perplexities)
```

Human writing naturally varies in complexity between sentences, while AI tends to produce more uniform output.

**Code Location**: `app/modules/stylometry.py`

### Ensemble Fusion

The three detection paths are combined using weighted averaging with **inverse perplexity weighting**:

**Base Weights:**
- Binoculars: 40%
- Neural: 40%
- Stylometric: 20%

**Adaptive Logic:**
When text perplexity exceeds 100 (indicating unusual/difficult text), the neural discriminator weight is reduced by 50% and Binoculars weight is increased, since statistical methods are more robust on out-of-distribution text.

```python
final_score = (
    w_binoculars * binoculars_score +
    w_neural * neural_score +
    w_stylometry * stylometric_score
)
verdict = "AI-Generated" if final_score > 0.5 else "Human-Written"
```

**Code Location**: `app/ensemble.py`

### Text Preprocessing

Before analysis, input text is sanitized to prevent adversarial evasion:

1. **Unicode NFKC Normalization** - Converts homoglyphs to canonical forms
2. **Invisible Character Removal** - Strips zero-width spaces and joiners
3. **Whitespace Trimming** - Removes leading/trailing whitespace

**Code Location**: `app/preprocessing.py`

---

## Limitations & Drawbacks

This system has several important limitations to be aware of:

### Detection Accuracy

| Limitation | Description |
|------------|-------------|
| **No ground truth** | AI detection is fundamentally probabilistic; no detector achieves 100% accuracy |
| **False positives** | Human text with uniform style (technical writing, legal docs) may be flagged as AI |
| **False negatives** | Heavily edited AI text or advanced models may evade detection |
| **Threshold arbitrariness** | The 0.5 decision threshold is not calibrated on a validation set |

### Model Constraints

- **Base models only**: The neural discriminator uses a base DeBERTa model, not one fine-tuned for AI detection. For production, replace with a specialized checkpoint.
- **GPT-2 era**: The Binoculars models (GPT-2/GPT-2-Medium) may be less effective at detecting text from newer LLMs like GPT-4 or Claude.
- **English only**: Models are trained on English; performance on other languages is untested and likely degraded.

### Input Requirements

- **Short text unreliable**: Texts under ~50 words lack sufficient signal for accurate detection
- **Context loss**: The system analyzes text in isolation without considering document context
- **512 token limit**: Neural discriminator truncates longer texts, potentially missing important signals

### Technical Limitations

- **Memory footprint**: Loads 3 transformer models (~4GB RAM minimum)
- **Latency**: First request is slow due to model loading; not suitable for real-time applications without warmup
- **Stylometric heuristics**: Uses simple threshold-based scoring rather than a trained classifier (XGBoost was planned but not implemented)

### Adversarial Robustness

While the system includes text sanitization, it may still be vulnerable to:
- Paraphrasing attacks
- Character-level perturbations beyond the sanitization scope
- Prompt injection in the source AI to produce "human-like" patterns
- Mixing human and AI-written content

### Ethical Considerations

- **Not suitable for high-stakes decisions**: Do not use as sole evidence for academic integrity, hiring, or legal matters
- **Bias potential**: May perform differently across writing styles, demographics, or domains
- **Arms race**: As detection improves, so do evasion techniques

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Requirements

- Python 3.10+
- PyTorch 2.0+
- ~4GB RAM for model loading
- GPU optional but recommended for faster inference

## License

MIT License - see LICENSE file for details.

## References

- **Binoculars**: Hans, A., et al. (2024). *Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text*. [arXiv:2401.12070](https://arxiv.org/abs/2401.12070)
- **DeBERTa**: He, P., et al. (2021). *DeBERTa: Decoding-enhanced BERT with Disentangled Attention*. [arXiv:2006.03654](https://arxiv.org/abs/2006.03654)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Love itsjv14 <3

