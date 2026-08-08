---
id: tool-05373
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ai-text-detector
summary: 风格微调/文风迁移
source: https://github.com/amsa10/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5373
category: 一、去 AI 味 / Humanizer 库
repo: amsa10/ai-text-detector
stars: 0
url: https://github.com/amsa10/ai-text-detector
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c3497408bd70664d
  - methods/改稿润色指令库.md
---

# amsa10/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/amsa10/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：amsa10/ai-text-detector
- **拉取时间**：2026-07-25 18:16:11

---

# **AI Text Detector – Bulk & Single Detection**  

This project detects AI-generated text using two models:  
1️⃣ **RoBERTa-based classifier (`model1.py`)**  
2️⃣ **LoRA fine-tuned model (`model2.py`)**  

## **📌 Features**  
✅ **Single-text detection** – Quickly check if a short passage is AI-generated.  
✅ **Bulk detection** – Process large datasets (20+ essays) with CSV input.  
✅ **Choose your AI model** – Use **RoBERTa (model1)** or **Mistral LoRA (model2)**.  
✅ **Optimized for efficiency** – Uses a **progress bar** for bulk processing.  

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## **📌 Setup**  

1️⃣ **Clone the repository**  
```sh
cd ai-text-detector
pip install -r requirements.txt
python main.py --model model1
python main.py --model model2

ai-text-detector/
│── data/
│   ├── input.csv  # Your dataset with text to analyze
│   ├── processed_results.csv  # Output results after processing
│── src/
│   ├── model1.py  # RoBERTa-based classifier
│   ├── model2.py  # LoRA fine-tuned model
│── requirements.txt  # Dependencies
│── README.md  # Project description and usage guide
│── .gitignore  # Ignore large files, cache, etc.
│── main.py  # Script to run detection on a dataset



