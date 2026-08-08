---
id: tool-05651
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/jasp-nerd/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5651
category: 一、去 AI 味 / Humanizer 库
repo: jasp-nerd/ai-text-detector
stars: 0
url: https://github.com/jasp-nerd/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2bcd00fad4d0941d
  - methods/改稿润色指令库.md
---

# jasp-nerd/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/jasp-nerd/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Fine-tuned DistilBERT classifier for detecting AI-generated text
- **本地描述**：Fine-tuned DistilBERT classifier for detecting AI-generated text
- **拉取时间**：2026-07-25 18:26:38

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

A fine-tuned DistilBERT model that classifies text as human-written or AI-generated. Comes with a Gradio web interface for easy testing.

I built this as part of my work on AI literacy at VU Amsterdam. Detecting AI-generated text is a real and growing problem in education, and I wanted to see how well a simple transformer classifier could do.

## How it works

The model is a [DistilBERT](https://huggingface.co/distilbert-base-uncased) (66M params) fine-tuned on the [GPT-wiki-intro](https://huggingface.co/datasets/aadityaubhat/GPT-wiki-intro) dataset, which contains ~150k pairs of human-written and GPT-generated Wikipedia introductions. After 3 epochs of training it gets around 98% accuracy on the validation set.

Obviously this won't catch everything. It's trained on Wikipedia-style text and older GPT output, so newer models like GPT-4 or Claude will be harder to detect. But it's a solid demo of how transfer learning works for this kind of task.

## Setup

```bash
git clone https://github.com/jasp-nerd/ai-text-detector.git
cd ai-text-detector

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Training

The dataset downloads automatically from Hugging Face when you first run training.

```bash
python train.py
```

Takes about 30-60 min on a GPU, or 2-3 hours on CPU. The trained model gets saved to `./model/`.

## Usage

**Web interface:**
```bash
python app.py
# opens at http://localhost:7860
```

**Command line:**
```bash
python predict.py
```

**In your own code:**
```python
from predict import TextDetectorPredictor

p = TextDetectorPredictor('./model')
result = p.predict("Some text to check...")
print(result['prediction'], result['confidence'])
```

## Limitations

- Trained on Wikipedia text, so it may underperform on other domains (tweets, essays, code, etc.)
- Older GPT-2 style output, newer models are harder to detect
- Short texts (<100 chars) are unreliable
- Binary classification only, doesn't tell you *which* AI wrote it
