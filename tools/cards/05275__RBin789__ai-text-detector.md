---
id: tool-05275
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rbin789/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5275
category: 一、去 AI 味 / Humanizer 库
repo: RBin789/ai-text-detector
stars: 2
url: https://github.com/rbin789/ai-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 272db5ed6c4bced1
  - methods/改稿润色指令库.md
---

# RBin789/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rbin789/ai-text-detector
- **Stars**：2
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：RBin789/ai-text-detector
- **拉取时间**：2026-07-25 18:12:33

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

## Overview
AI Text Detector is a machine learning tool that analyzes documents to identify AI-generated content. The system breaks text into segments, extracts sophisticated linguistic features, and employs a trained XGBoost model to classify each segment as either human-written or AI-generated.

## Key Features
- Segment-level Analysis: Breaks documents into manageable segments for granular detection
- Advanced Feature Extraction: Utilizes 13+ linguistic and stylometric features
- Pre-trained XGBoost Model: Achieves 92.1% ROC AUC on test data
- Similarity Analysis: Identifies inconsistencies between document segments
- Interactive Visualization: Color-coded HTML reports highlight suspicious segments
- GPU Acceleration: Optional CUDA support for faster processing

## How It Works
1. Text Preprocessing: Documents are normalized and segmented into paragraphs
2. Feature Extraction: Each segment is analyzed for:
    - Lexical features (word length, sentence structure)
    - Syntactic patterns (punctuation usage, function word ratio)
    - Readability metrics (Flesch-Kincaid, Gunning Fog)
    - Semantic embeddings (using DistilBERT)
3. Classification: XGBoost model predicts probability of AI generation
4. Similarity Analysis: Detects style inconsistencies between segments
5. Visualization: Results displayed with color-coding and risk assessment




## Project Structure
```
ai-text-detector/
├── data/                  # Training and evaluation data
│   ├── raw/               # Original human and AI text samples
│   └── processed/         # Feature-extracted segments
├── features/              # Feature extraction code
├── models/                # Trained models and training scripts
├── notebooks/             # Jupyter notebooks for analysis
│   ├── data_exploration.ipynb
│   ├── process_data.ipynb
    └── evaluate_document.ipynb
├── preprocessing/         # Text normalization and segmentation
├── reports/               # Generated analysis reports
├── utils/                 # Helper functions and NLTK data
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- NLTK and spaCy for NLP processing
- HuggingFace Transformers for embeddings
- XGBoost for the classification model

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd ai-text-detector
pip install -r requirements.txt
```

## Usage
- The main usage is just running the evaluate_document.ipynb notebook if you want to train your own model you can use the provided processed data in /data/processed or if you want to implment your own data your will need to put the data in the correct format see below.
- After setting up the project, you can run the preprocessing scripts, extract features, and train models using the provided notebooks.

## Using your own data
- The data for this project was taken from the DAIGT V2 Train Dataset found here: https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset/data
- You can find the code to split the data into the correct format in /utis/split-data.py
- The format the data should be in is: {number representing which file it is in the sequence 0 to number of files}-{0 or 1 representing wheather it is human or AI}.txt example for first file which is human written 0-0.txt.
