---
id: tool-05437
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Slop-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/naman33/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5437
category: 一、去 AI 味 / Humanizer 库
repo: naman33/AI-Slop-Detector
stars: 0
url: https://github.com/naman33/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# naman33/AI-Slop-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/naman33/ai-slop-detector
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：naman33/AI-Slop-Detector
- **拉取时间**：2026-07-25 18:18:37

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-Slop-Detector
A machine learning project that detects whether a piece of text is AI-generated or human-written using a fine-tuned BERT model trained on the RAID dataset.

🚀 Overview-

With the rapid rise of AI-generated content, distinguishing between human and machine-written text has become increasingly important. This project builds a binary text classifier that analyzes linguistic patterns and predicts whether a given input is AI-generated.

The model is trained on the RAID dataset, which includes diverse domains and outputs from multiple AI models, enabling robust evaluation across different writing styles.

🏗️ System Architecture-
RAID Dataset → Preprocessing → Tokenization → BERT Fine-Tuning → Evaluation → Flask API
🧰 Tech Stack
Python – Core programming language
PyTorch – Deep learning framework
Hugging Face Transformers – BERT model & tokenizer
Pandas / NumPy – Data handling
Scikit-learn – Metrics & evaluation
Flask – API deployment
📂 Project Structure
ai-text-detector/
│
├── data/               # RAID dataset
├── scripts/            # Data processing & training scripts
├── models/             # Saved trained model
├── app/                # Flask API
├── notebooks/          # Experiments & analysis
├── requirements.txt
└── README.md
⚙️ How It Works
1. Data Preparation
Loaded RAID dataset containing:
Human-written text
AI-generated text (multiple models)
Cleaned and filtered invalid or short samples
Converted labels:
0 → Human
1 → AI
2. Tokenization
Used BERT tokenizer (bert-base-uncased)
Applied:
Padding
Truncation (max length = 512 tokens)
3. Model Training
Fine-tuned pretrained BERT for binary classification
Training setup:
Loss: CrossEntropy
Optimizer: AdamW
Epochs: 2–3
Batch size: 8–16
4. Evaluation

Evaluated model using:

Accuracy
Precision / Recall
True Positive Rate (TPR) → AI detection capability
False Positive Rate (FPR) → Misclassification of human text
