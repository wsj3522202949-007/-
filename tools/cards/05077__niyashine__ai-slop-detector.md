---
id: tool-05077
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/niyashine/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5077
category: 一、去 AI 味 / Humanizer 库
repo: niyashine/ai-slop-detector
stars: 0
url: https://github.com/niyashine/ai-slop-detector
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
content_hash: b6da5390b07cc0cb
  - methods/改稿润色指令库.md
---

# niyashine/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/niyashine/ai-slop-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：niyashine/ai-slop-detector
- **拉取时间**：2026-07-25 18:05:16

---

# AI Slop Detector



A Flask + Machine Learning web application that analyzes text and predicts whether it is more likely to be **AI-generated** or **human-written**.



---



## Overview



AI Slop Detector uses Natural Language Processing (NLP) and a trained machine learning classifier to identify writing patterns commonly found in AI-generated and human-written text.



The application provides:



- AI/Human prediction

- Confidence score

- Explanation of the prediction

- Text statistics

- Responsive user interface



---



## Technologies Used



### Frontend



- HTML5

- CSS3

- JavaScript



### Backend



- Python

- Flask



### Machine Learning



- Scikit-learn

- Pandas

- NumPy

- Joblib



### NLP



- NLTK



---



## Folder Structure



```text

ai-slop-detector/

│

├── app.py                     ← Main Flask application

├── requirements.txt

├── README.md

│

├── dataset/                   ← Training dataset

│

├── model/

│   ├── classifier.pkl         ← Trained ML model

│   ├── feature_extractor.py   ← NLP feature extraction

│   ├── model_loader.py        ← Loads trained model

│   └── train_model.py         ← Model training script

│

├── static/

│   ├── style.css              ← Stylesheet

│   └── script.js              ← Frontend logic

│

└── templates/

    └── index.html             ← Main webpage

```



---



## Features



- Detect AI-generated and human-written text

- Machine learning-based classification

- Confidence score for every prediction

- Explainable prediction results

- Character, word and sentence statistics

- Responsive UI

- Copy results to clipboard

- Reset button for quick re-analysis



---



## Installation



### Clone the repository



```bash

git clone https://github.com/niyashine/ai-slop-detector.git

```



### Navigate to the project directory



```bash

cd ai-slop-detector

```



### Install dependencies



```bash

pip install -r requirements.txt

```



### Run the application



```bash

python app.py

```



---



## Running the Application



Open your browser and visit



```text

http://127.0.0.1:5000

```



---



## How It Works



1. User enters or pastes text.

2. The text is sent to the Flask backend.

3. NLP features are extracted.

4. The trained classifier predicts whether the text is AI-generated or human-written.

5. The application returns:

   - Prediction

   - Confidence score

   - Explanation

6. Results are displayed along with text statistics.



---



## Machine Learning Pipeline



```

Dataset

    │

    ▼

Preprocessing

    │

    ▼

Feature Extraction

    │

    ▼

Model Training

    │

    ▼

Model Serialization (Joblib)

    │

    ▼

Flask Prediction API

```



---



## Future Improvements



- Larger and more diverse training dataset

- Multiple detection models

- Improved confidence calibration

- Additional linguistic analysis

- Upload support (.txt, .pdf, .docx)

- User history

- Dark mode



---



## Team Members



- Anupama S

- Neha Maria Fathima K T

- Niya Shine



related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



## License



This project was developed as part of an academic project and is intended for educational purposes.

