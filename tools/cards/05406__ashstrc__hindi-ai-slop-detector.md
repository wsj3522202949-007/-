---
id: tool-05406
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: hindi-ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ashstrc/hindi-ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5406
category: 一、去 AI 味 / Humanizer 库
repo: ashstrc/hindi-ai-slop-detector
stars: 0
url: https://github.com/ashstrc/hindi-ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: a62b6ea97bbbfe9a
  - methods/改稿润色指令库.md
---

# ashstrc/hindi-ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ashstrc/hindi-ai-slop-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ashstrc/hindi-ai-slop-detector
- **拉取时间**：2026-07-25 18:17:24

---

# Hindi AI Detector 🇮🇳🤖

An end-to-end pipeline to detect AI-generated Hindi text using a custom dataset and transformer models.

---

## 🚀 Project Overview

This project builds a dataset of **human-written Hindi text** and **AI-generated text**, then trains a model to classify whether a given text is AI-generated or human-written.

---

## 📁 Project Structure

```
hindi-ai-detector/
│
├── data/
│   └── processed/
│       ├── dataset.jsonl          # Human dataset
│       └── ai_batches/            # AI-generated batches
│
├── src/
│   ├── fetch_wiki.py              # Data collection (Wikipedia API)
│   ├── generate_ai_batches.py     # AI data generation (local model)
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
└── README.md
```

---

## 🧠 Dataset

### Human Data

* Collected from Wikipedia (Hindi)
* Stored in `dataset.jsonl`
* Format:

```json
{"text": "Some Hindi paragraph...", "label": 0}
```

### AI Data

* Generated using local model (`phi-2`)
* Stored in `ai_batches/`
* Format:

```json
{"text": "AI rewritten paragraph...", "label": 1}
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd hindi-ai-detector
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 📥 Step 1: Collect Data

```
python src/fetch_wiki.py
```

This creates:

```
data/processed/dataset.jsonl
```

---

## 🤖 Step 2: Generate AI Data (Batch Processing)

Edit inside `generate_ai_batches.py`:

```python
START_INDEX = 0
MAX_SAMPLES = 5000
BATCH_OFFSET = 0
```

Run:

```
python src/generate_ai_batches.py
```

This creates:

```
data/processed/ai_batches/batch_1.jsonl
batch_2.jsonl ...
```

---

### 🔁 Continue Next Batches

For next run:

```python
START_INDEX = 5000
BATCH_OFFSET = 10
```

---

## ⚠️ Notes

* Do NOT modify `dataset.jsonl`
* AI batches are generated separately
* Use batching to avoid system overload

---

## 🧪 Next Steps

* Merge all batches into a final dataset
* Train classification model
* Build Chrome Extension for detection

---

## 💡 Tech Stack

* Python
* Transformers (HuggingFace)
* PyTorch
* Wikipedia API

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👨‍💻 Author

Ashmit Kumar
Vikash Kumar
