---
id: tool-04865
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: fake-data-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/adides3/fake-data-detector
created: 2026-07-18
updated: 2026-07-18
no: 4865
category: 一、去 AI 味 / Humanizer 库
repo: Adides3/fake-data-detector
stars: 0
url: https://github.com/adides3/fake-data-detector
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

# Adides3/fake-data-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/adides3/fake-data-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered fake data detector built with Python, Streamlit, and scikit-learn, featuring text classification, model evaluation, and explainable predictions. Using a hotel review data set taken from kaggle. 
- **本地描述**：AI-powered fake data detector built with Python, Streamlit, and scikit-learn, featuring text classification, model evaluation, and explainable predictions. Using a hotel review data set taken from kaggle.
- **拉取时间**：2026-07-25 17:57:20

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Deceptive Review Detector

An AI-augmented Python project for detecting deceptive hotel reviews from text.

## What it does

- Trains on the bundled deceptive-opinion review dataset.
- Uses train, validation, and test splits for honest evaluation.
- Tunes the decision threshold on the validation set.
- Exposes AI-style explanations for individual reviews.
- Includes a polished Streamlit dashboard with metrics and top terms.
- Provides a CLI for training, inspection, and batch predictions.

## Tech Stack

- Python
- pandas
- scikit-learn
- Streamlit
- Plotly
- joblib

## Portfolio Highlights

- Clean `src/` layout and editable install support.
- Real review dataset with a clearly defined classification target.
- Proper model evaluation with accuracy, precision, recall, F1, and ROC AUC.
- Top-terms export for interpretability.
- Optional OpenAI-powered explanation layer with offline fallback.
- Streamlit UI with dashboard cards, charts, and risk summaries.

## Do You Need To Provide A CSV?

No, not for the default project workflow.

- If you run `fake-review-detector train` with no arguments, the project uses the bundled dataset automatically.
- Training, validation, and test sets are split inside the code.
- You only need to provide a CSV if you want to train on your own labeled review dataset.
- For your own CSV, the training file must include a text column named `text`.
- The label column is `deceptive` by default, and it should contain `truthful` and `deceptive` values, or `0` and `1`.
- For prediction, your CSV only needs a `text` column.

## Project Structure

```text
fake_data_detector/
├── artifacts/
├── data/
├── src/fake_data_detector/
│   ├── ai_explainer.py
│   ├── cli.py
│   ├── config.py
│   ├── dataset.py
│   ├── model.py
│   └── __init__.py
├── streamlit_app.py
├── tests/
└── requirements.txt
```

## Quick Start

1. Create and activate a virtual environment.
2. Install the project:

```bash
pip install -e .
```

3. Train the model:

```bash
fake-review-detector train
```

4. Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

## CLI Usage

Train the model with the bundled dataset:

```bash
fake-review-detector train
```

Train on your own labeled CSV:

```bash
fake-review-detector train --data path/to/your_training.csv --label-column deceptive
```

Predict from a CSV file:

```bash
fake-review-detector predict --input path/to/input.csv --output artifacts/predictions.csv
```

## AI Augmentation

The project includes an explanation layer that:

- highlights suspicious numeric patterns,
- surfaces missing or inconsistent values,
- generates a human-readable risk summary,
- optionally calls an LLM if `OPENAI_API_KEY` is set.

If no API key is present, the app falls back to local explanations so the project still works offline.

## Notes

- The model is meant for learning and portfolio work, not for forensic or legal decisions.
- The project is self-contained by default because the dataset is already included in `data/`.

## Step-by-Step Run Guide

1. Open PowerShell in the project folder:

```powershell
cd C:\Aditya\Projects\Fake_data_detector
```

2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install the project:

```powershell
python -m pip install --upgrade pip
pip install -e .
```

5. Train the model:

```powershell
fake-review-detector train
```

6. Run the dashboard:

```powershell
streamlit run streamlit_app.py
```

## How to Upload to GitHub

1. Create a new repository on GitHub.
2. In this folder, initialize Git if needed:

```powershell
git init
```

3. Add your files and commit:

```powershell
git add .
git commit -m "Initial fake data detector project"
```

4. Connect your GitHub repository:

```powershell
git remote add origin https://github.com/<your-username>/<your-repo>.git
```

5. Push the code:

```powershell
git branch -M main
git push -u origin main
```

If Git asks for authentication, use a GitHub personal access token or the GitHub CLI.
