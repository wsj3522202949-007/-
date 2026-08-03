---
id: tool-05708
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: paraphrase-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/muhammadrafay1/paraphrase-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5708
category: 一、去 AI 味 / Humanizer 库
repo: MuhammadRafay1/paraphrase-text-detector
stars: 1
url: https://github.com/muhammadrafay1/paraphrase-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MuhammadRafay1/paraphrase-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/muhammadrafay1/paraphrase-text-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：ROBUST AI TEXT DETECTOR AGAINST PARAPHRASING ATTACKS
- **本地描述**：ROBUST AI TEXT DETECTOR AGAINST PARAPHRASING ATTACKS
- **拉取时间**：2026-07-25 18:28:40

---

# Robust AI Text Detector

A machine learning system designed to detect AI-generated text **even when paraphrased**, using a hybrid architecture that combines transformer-based semantic embeddings, stylometric features, contrastive learning, and adversarial augmentation.

## 🚀 Key Features

* **Hybrid Detection Model**: Combines RoBERTa embeddings with stylometric (statistical/linguistic) features.
* **Paraphrase-Invariant**: Uses contrastive loss and on-the-fly adversarial augmentation (Back-translation, Neural Paraphrasing, Synonyms) to robustly detect paraphrased AI text.
* **Dual Data Strategy**: Supports both modular local data collection (Wikipedia, Reddit, News) and High-Performance Kaggle datasets (HC3, DAIGT).
* **Streamlit UI**: User-friendly interface for real-time inference and analysis.

---

## 🛠️ Workflows

This project supports two distinct workflows for Data Generation and Training.

### 1. Data Generation

#### Option A: Kaggle High-Performance (Recommended for Production)

Uses the `gen-project-datageneration.ipynb` notebook to combine high-quality datasets:

* **Sources**: HC3 (Human ChatGPT Comparison Corpus), DAIGT V2 (Detecting AI Generated Text).
* **Method**: Pre-calculated dataset generation optimized for Kaggle's environment.
* **Output**: Large-scale `.parquet` files for robust training.
* **Location**: `kaggle_data_generation/`

#### Option B: Local Modular Generation

Uses the local script configuration for flexible, custom data collection.

* **Sources**: Configurable via `config/data_config.yaml` (News, Essays, Reddit, Wikipedia).
* **Method**: dynamic scraping and generation using `src.data.dataset_builder`.
* **Command**:

    ```bash
    python scripts/prepare_data.py --config config/data_config.yaml
    ```

### 2. Training

#### Option A: Kaggle Cloud Training (GPU Accelerated)

 Optimized for Kaggle's T4 x2 GPUs.

* **Setup**: Upload project to Kaggle Datasets.
* **Execution**: Use `kaggle_deployment/kaggle_train.ipynb`.
* **Features**: Automatic environment setup, GPU acceleration, and dataset integration.

#### Option B: Local Development Training

For debugging and smaller scale experiments.

* **Config**: `config/training_config.yaml`.
* **Command**:

    ```bash
    python scripts/train.py --config config/training_config.yaml
    ```

---

## 💻 User Interface (Streamlit)

Interact with the trained model using the local web interface.

1. **Setup**:
    Ensure you have a trained model checkpoint (e.g., `checkpoints/best_model.pt`).

2. **Run the App**:

    ```bash
    streamlit run app/main.py
    ```

3. **Features**:
    * Real-time text analysis.
    * Probability visualization (AI vs Human).
    * Detailed feature breakdown (Stylometric stats).

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📂 Project Structure

```
robust-ai-text-detector/
├── app/                       # Streamlit UI application
├── config/                    # Configuration files (Data, Model, Training)
├── kaggle_data_generation/    # Kaggle-specific data notebooks (HC3/DAIGT)
├── kaggle_deployment/         # Kaggle training deployment files
├── scripts/                   # CLI Scripts (Train, Eval, Prepare Data)
├── src/                       # Core Source Code
│   ├── data/                  # Dataset builders and collectors
│   ├── features/              # Stylometry & Embedding extractors
│   ├── models/                # FusionModel architecture & Losses
│   ├── paraphrasing/          # Adversarial attack engines
│   └── training/              # Trainer & Augmentation logic
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## ⚙️ Installation

```bash
# Clone the repository
git clone <repo-url>
cd paraphrase-text-detector

# Install dependencies
pip install -r requirements.txt

# Download required spaCy model
python -m spacy download en_core_web_sm
```
