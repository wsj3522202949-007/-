---
id: tool-04828
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tanvi9882/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4828
category: 一、去 AI 味 / Humanizer 库
repo: Tanvi9882/ai-text-detector
stars: 0
url: https://github.com/tanvi9882/ai-text-detector
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
content_hash: 983cdd662395ca1c
  - methods/改稿润色指令库.md
---

# Tanvi9882/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tanvi9882/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Tanvi9882/ai-text-detector
- **拉取时间**：2026-07-25 17:55:55

---

# 🤖 AI vs. Human Text Detector (Production Grade)

> A production-ready, microservices-based application featuring a **FastAPI** backend hosting a fine-tuned **RoBERTa-base** model, and a **Streamlit** user interface with a research-grade model evaluation dashboard.

---

## 🏗️ Architecture

This project is built using a modern, decoupled microservices architecture to ensure production readiness, scalability, and ease of deployment:

```
                  ┌─────────────────────────────┐
                  │        Streamlit UI         │
                  │       (Port: 8501)          │
                  └──────────────┬──────────────┘
                                 │
                     HTTP Requests (REST API)
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │       FastAPI Backend       │
                  │        (Port: 8000)         │
                  └──────────────┬──────────────┘
                                 │
                             PyTorch
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │   RoBERTa Classifier Model  │
                  └─────────────────────────────┘
```

- **Frontend (Streamlit)**: A sleek, modern dashboard that handles user input (raw text or PDF upload), sends requests to the backend, and renders interactive performance visualizations. It does not load the heavy model files directly, allowing the container to start instantly and run on minimal memory resources.
- **Backend (FastAPI)**: Serves model inference and pre-computed evaluation metrics. Utilizes CUDA GPU acceleration if available, falling back to CPU gracefully.
- **Docker Compose**: Orchestrates the frontend and backend services in isolated networks.

---

## 🎯 Key Features

- 📄 **Document Input**: Paste plain text or upload a PDF document directly.
- ⚙️ **Weighted Chunk Inference**: Handles long-form documents by splitting them into overlapping 512-token windows and performing a token-weighted average score aggregation.
- 🔴🟡🟢 **Sentence-Level Highlighting**: Flags specific AI-generated sentences (red), mixed sentences (yellow), and human-written sentences (green).
- 🔬 **Model Evaluation Dashboard**:
  - **Metrics Cards**: Accuracy, Precision, Recall, and F1-score.
  - **Confusion Matrix**: An interactive Plotly heatmap showing True Negatives, False Positives, False Negatives, and True Positives.
  - **ROC Curve**: Receiver Operating Characteristic curve showing True Positive Rate vs. False Positive Rate with AUC calculations.
  - **Precision-Recall Curve**: Displays model performance across thresholds with Average Precision (AUC).
- 🗄️ **Detection History**: Local SQLite database storing analysis history, accessible from the sidebar.

---

## 📊 Model Performance

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 89.1%  |
| F1 Score  | 89.0%  |
| Precision | 90.3%  |
| Recall    | 89.1%  |

> Best checkpoint: **Step 1500 (~Epoch 2.6)** — EarlyStopping prevented overfitting.

---

## 🛠️ Tech Stack

| Layer       | Technology                          |
|-------------|-------------------------------------|
| Model       | RoBERTa-base (HuggingFace)          |
| Backend     | FastAPI + Uvicorn                   |
| Frontend    | Streamlit                           |
| Visuals     | Plotly                              |
| Database    | SQLite                              |
| Deployment  | Docker + Docker Compose             |

---

## 🚀 How to Run

### Option A: Running with Docker (Recommended)

Make sure you have [Docker and Docker Compose](https://docs.docker.com/engine/install/) installed.

1. **Build and start the services**:
   ```bash
   docker-compose up --build
   ```
2. **Access the applications**:
   - Streamlit Frontend: `http://localhost:8501`
   - FastAPI Backend API Docs: `http://localhost:8000/docs`
   - FastAPI Backend Healthcheck: `http://localhost:8000/health`

---

### Option B: Local Development (Without Docker)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate the Evaluation Metrics**:
   To populate the evaluation dashboard, run the evaluation script once against the test split of your dataset:
   ```bash
   python evaluate_model.py
   ```

3. **Start the FastAPI Backend**:
   ```bash
   uvicorn app:app --port 8000 --reload
   ```

4. **Start the Streamlit UI**:
   In a new terminal window:
   ```bash
   streamlit run streamlit.py
   ```
   Open `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
ai-text-detector/
├── Dockerfile.backend            # Containerizes the FastAPI model server
├── Dockerfile.frontend           # Containerizes the Streamlit client
├── docker-compose.yml            # Services orchestrator
├── app.py                        # FastAPI Backend implementation
├── streamlit.py                  # Streamlit Web App interface
├── evaluate_model.py             # Generates validation dashboard figures
├── evaluation_metrics.json       # Pre-computed evaluation stats (from test split)
├── roberta_fine_tune.py          # Training and fine-tuning pipeline
├── requirements.txt              # Unified dependencies list
├── fine_tuned_roberta_ai_detector/  # Saved model checkpoint weights (gitignored)
└── Dataset.csv                   # Training raw data (gitignored)
```

---

## 🌐 Online Deployment

This application is ready to be deployed to the cloud:

1. **FastAPI Backend (Render or Hugging Face Spaces)**:
   - Deploy as a Docker service on **Render** (free tier supports Docker Web Services).
   - Alternatively, host the model server on **Hugging Face Spaces** using their Docker template.
2. **Streamlit UI (Streamlit Community Cloud)**:
   - Deploy the frontend directly on **Streamlit Community Cloud** from your GitHub repo.
   - Point the `API_URL` environment variable to your deployed FastAPI backend URL.

### Live Demo Links
- **Streamlit Web App:** `[Insert Live Streamlit URL here]`
- **FastAPI Model API:** `[Insert Live Backend URL here]`

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📄 License

MIT License — free to use for educational and portfolio purposes.
