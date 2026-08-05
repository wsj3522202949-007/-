---
id: tool-05630
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 需API密钥, 英文文档, 去AI味]
title: edu-vision-action-detection
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sanjaykshetri/edu-vision-action-detection
created: 2026-07-18
updated: 2026-07-18
no: 5630
category: 一、去 AI 味 / Humanizer 库
repo: sanjaykshetri/edu-vision-action-detection
stars: 0
url: https://github.com/sanjaykshetri/edu-vision-action-detection
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sanjaykshetri/edu-vision-action-detection

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sanjaykshetri/edu-vision-action-detection
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Computer-vision pipeline for detecting observable student actions in classroom images (e.g., hand raised, writing, looking at board) using PyTorch + ResNet. Built to explore modular ML components that can later integrate with a larger Teacher Assistant Dashboard for real-world educational analytics.
- **本地描述**：Computer-vision pipeline for detecting observable student actions in classroom images (e.g., hand raised, writing, looking at board) using PyTorch + ResNet. Built to explore modular ML components that can later integrate with a larger Teacher Assistant Dashboard for real-world educational analytics.
- **拉取时间**：2026-07-25 18:25:50

---

# 🎓 edu-vision-action-detection  
*A PyTorch–powered computer-vision model for detecting observable classroom actions*

---

## 📌 Overview

This repository contains a modular deep-learning pipeline that detects **observable student actions** from classroom images — such as:

- ✍️ writing
- 🧑‍🏫 looking at board / attention-direction
- ✋ hand raised
- 📱 device visible (phone / laptop)

**No mental-state prediction** is performed — only **objective, physically observable actions.**

The project is part of a long-term roadmap toward building data-driven educational tools and **will later integrate as a micro-service** into a larger “Teacher Assistant Dashboard” ecosystem.

---

## 🚀 What This Repo Demonstrates (Portfolio Highlights)

| Skill Area | Evidence |
|------------|----------|
| Deep Learning | ResNet-based classifier, PyTorch training pipeline |
| Computer Vision | ImageFolder dataset, transforms, augmentation |
| Engineering Maturity | Modular repo, separation of model vs. UI, scalable architecture |
| Deployment-readiness | Streamlit inference UI planned, save/load model weights |

If you're reviewing this repo as a hiring manager:
> This project showcases end-to-end ML capability: data → model → training → deployment.

---

## 🧠 Project Architecture

!`[Architecture Diagram](./diagrams/architecture.png)`

- **Modular Components:** Clear separation of data, model, and UI code
- **Scalability:** Easily add classes, augmentations, or models
- **Reproducibility:** Config files and scripts for every step

---

## 📂 Dataset Construction

- **Classes:** `hand_raised`, `writing`, `looking_board`, `device_use`
- **Data sources:** Royalty-free stock images (Pexels API), staged photos (optional)
- **Folder structure:**
  - `data/train/<class>/` — training images
  - `data/val/<class>/` — validation images
- **Automated scripts:**
  - `download_stock.py` — Download images for each class using Pexels API
  - `split_train_val.py` — Split dataset into train/validation folders
- **Augmentation:**
  - In-pipeline: Random flip, rotation, color jitter, crop, blur

Before downloading images, set `PEXELS_API_KEY` in your environment or copy `.env.example` to `.env` and fill in the key.

## 🏋️ Model Training

- **Framework:** PyTorch
- **Model:** ResNet18 (transfer learning)
- **Augmentation:** Advanced transforms in training pipeline
- **Training features:**
  - AdamW optimizer, dropout, early stopping
  - Metrics logging (loss, accuracy per epoch)
  - Confusion matrix visualization
  - Model checkpointing (best model saved)
  - Saved model metadata (`model_metadata.json`) for class mapping and preprocessing
- **Script:** `train.py`

## 📊 Evaluation & Visualization

- **Metrics:** Training loss, validation accuracy (plotted via `visualize_metrics.py`)
- **Confusion matrix:** Auto-saved for best model
- **Inference:**
  - `inference.py` — Predict class for any image

## 🌐 Streamlit Demo App

- **File:** `app.py`
- **Features:**
  - Upload an image or select from test dataset
  - See model prediction instantly
  - User-friendly interface for demo/portfolio

## 📝 How to Run

1. **Install dependencies:**
   ```
  pip install -r requirements.txt
   ```
2. **Download and split dataset:**
   ```
   python download_stock.py --class all --limit 100
   python split_train_val.py
   ```
3. **Train the model:**
   ```
   python train.py
   ```
  Or use the unified CLI:
  ```
  python cli.py train
  ```
4. **Visualize metrics:**
   ```
   python visualize_metrics.py
   ```
5. **Run Streamlit app:**
   ```
   streamlit run app.py
   ```
  Or run inference through the unified CLI:
  ```
  python cli.py predict --image path/to/image.jpg
  ```
6. **Run the test suite:**
  ```
  python -m unittest discover -s tests
  ```

## 📸 Example Results

- Add screenshots of Streamlit app and confusion matrix here.

## 📚 Credits & License

- Images: Pexels, Unsplash, Pixabay (see scripts for details)
- Code: MIT License

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*For questions or collaboration, open an issue or pull request!*

