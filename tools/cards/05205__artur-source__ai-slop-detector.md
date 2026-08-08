---
id: tool-05205
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/artur-source/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5205
category: 一、去 AI 味 / Humanizer 库
repo: artur-source/ai-slop-detector
stars: 0
url: https://github.com/artur-source/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 475af66916150a76
  - methods/改稿润色指令库.md
---

# artur-source/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/artur-source/ai-slop-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A web app that detects AI-generated text using DistilBERT fine-tuned on the HC3 dataset
- **本地描述**：A web app that detects AI-generated text using DistilBERT fine-tuned on the HC3 dataset
- **拉取时间**：2026-07-25 18:09:59

---

# ai-slop-detector

Detect AI-generated text using fine-tuned DistilBERT + OpenAI API

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-black)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![License MIT](https://img.shields.io/badge/License-MIT-green)
![pytest](https://img.shields.io/badge/tests-pytest-blue)

## What I built

This project is a Flask web app that runs two AI-text detectors side by side.
The local detector uses DistilBERT fine-tuned on the HC3 dataset, comparing human answers against ChatGPT answers.
The OpenAI detector uses `gpt-4o-mini` as a reference comparison.
Users can paste direct text or submit a URL, which is scraped automatically before analysis.

## How it works

```text
User input (text or URL)
       |
       v
   Scraper (BeautifulSoup)        [if URL]
       |
       v
   Text validation & cleanup
       /              \
Local DistilBERT    OpenAI gpt-4o-mini
       \              /
   Side-by-side results page
```

## Model Performance

| Metric    | Local DistilBERT | OpenAI gpt-4o-mini |
|-----------|------------------|-----------------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Accuracy  | TBD              | TBD                |
| Precision | TBD              | TBD                |
| Recall    | TBD              | TBD                |
| F1        | TBD              | TBD                |

Results will be updated after full training on Google Colab (T4 GPU).

## Project Structure

```text
ai-slop-detector/
+-- app/
|   +-- __init__.py              # Flask application factory
|   +-- routes.py                # Web routes for form submission and results
|   +-- detector.py              # Local DistilBERT and OpenAI detection engine
|   +-- scraper.py               # URL scraping and text cleanup utilities
|   +-- templates/
|       +-- index.html           # Main input form
|       +-- result.html          # Side-by-side detection results page
+-- model/
|   +-- train_classifier.py      # HC3 loading and DistilBERT fine-tuning script
|   +-- evaluate.py              # Evaluation metrics and confusion matrix script
+-- data/
|   +-- README.md                # HC3 dataset download notes
+-- assets/                      # Generated charts and visual assets
+-- tests/
|   +-- test_detector.py         # Unit tests for detection behavior
|   +-- test_scraper.py          # Unit tests for scraping and text extraction
+-- config.py                    # Shared project configuration
+-- requirements.txt             # Python dependencies
+-- .gitignore                   # Ignored secrets, caches, checkpoints, and saved models
+-- .env.example                 # Environment variable template
+-- README.md                    # English documentation
+-- README.pt.md                 # Portuguese documentation
+-- run.py                       # Local Flask entrypoint
```

## How to Run

### Local

```bash
git clone https://github.com/SEU_USUARIO/ai-slop-detector
cd ai-slop-detector
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your OPENAI_API_KEY
python model/train_classifier.py   # train the local model first
python run.py
```

### Tests

```bash
pytest tests/ -v
```

## Key Design Decisions

- Dual detection: comparing a local model against an API exposes cost and accuracy trade-offs.
- Lazy model loading: DistilBERT loads only on the first request instead of at import time.
- Scraper with realistic headers: helps avoid blocking on common websites.

## References

- HC3 Dataset: https://huggingface.co/datasets/Hello-SimpleAI/HC3
- DistilBERT: https://arxiv.org/abs/1910.01108
- Hello, GPT-4o-mini: https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/

Built by Artur as a portfolio project - Systems Analysis and Development, UniPiaget
