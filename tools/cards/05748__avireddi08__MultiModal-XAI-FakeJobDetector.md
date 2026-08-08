---
id: tool-05748
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: MultiModal-XAI-FakeJobDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/avireddi08/multimodal-xai-fakejobdetector
created: 2026-07-18
updated: 2026-07-18
no: 5748
category: 一、去 AI 味 / Humanizer 库
repo: avireddi08/MultiModal-XAI-FakeJobDetector
stars: 0
url: https://github.com/avireddi08/multimodal-xai-fakejobdetector
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
content_hash: 90c2404270781a69
  - methods/改稿润色指令库.md
---

# avireddi08/MultiModal-XAI-FakeJobDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/avireddi08/multimodal-xai-fakejobdetector
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：An XAI-powered hybrid framework for detecting fake job postings using multimodal data, including text, images, and audio. Leveraging explainable AI techniques, this project provides accurate, transparent, and interpretable predictions to identify fraudulent job listings across multiple data types.
- **本地描述**：An XAI-powered hybrid framework for detecting fake job postings using multimodal data, including text, images, and audio. Leveraging explainable AI techniques, this project provides accurate, transparent, and interpretable predictions to identify fraudulent job listings across multiple data types.
- **拉取时间**：2026-07-25 18:30:16

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MultiModal-XAI-FakeJobDetector
An XAI-powered hybrid framework for detecting fake job postings using multimodal data, including text, images, and audio. Leveraging explainable AI techniques, this project provides accurate, transparent, and interpretable predictions to identify fraudulent job listings across multiple media types.

# Frontend

# Commands

* cd frontend
* npm install
* npm run dev

# LIME Microservice

A Python Flask microservice that generates **LIME (Local Interpretable Model-agnostic Explanations)** for the Fake Job Detection application.

## Commands

cd lime-service

# Create virtual environment
python -m venv venv
<br>
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start the service
python app.py
```

The service starts on `http://localhost:5001` by default.

## Endpoints

### `POST /explain`
Generate a LIME explanation for job description text.

**Request:**
```json
{
  "text": "Work from home earn $5000 weekly no experience needed",
  "num_features": 10,
  "output_format": "json",
  "job_id": "optional-tracking-id"
}
```

**Response:**
```json
{
  "success": true,
  "job_id": "abc123",
  "explanation": [
    {"word": "earn", "weight": 0.142},
    {"word": "home", "weight": 0.098},
    {"word": "experience", "weight": -0.045}
  ],
  "num_features": 10,
  "cache_status": "MISS",
  "latency_ms": 850.2,
  "output_format": "json",
  "gcs_url": "gs://your-bucket/explanations/abc123.json"
}
```

### `GET /health`
Service health, cache statistics, and performance metrics.

### `POST /cache/clear`
Clear the in-memory LRU cache.

## Surrogate Model

Since no scikit-learn `.pkl` file is available, the service trains a **TF-IDF + Logistic Regression** surrogate model at startup on a curated dataset of real and fake job posting examples. The surrogate learns patterns typical of fake jobs (wage promises, upfront fees, vague requirements) vs. real ones. LIME then explains **this surrogate's decisions** on a per-prediction basis.

# audio-service

# commands

* cd audio-service
* pip install -r requirements.txt
* python audio_service.py

# Backend

# Commands

* Add model.pmml in path /backend/src/main/resources
* cd backend
* mvn clean install
* mvn spring-boot:run
