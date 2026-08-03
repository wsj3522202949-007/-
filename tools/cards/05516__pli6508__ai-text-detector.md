---
id: tool-05516
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/pli6508/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5516
category: 一、去 AI 味 / Humanizer 库
repo: pli6508/ai-text-detector
stars: 0
url: https://github.com/pli6508/ai-text-detector
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

# pli6508/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pli6508/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：pli6508/ai-text-detector
- **拉取时间**：2026-07-25 18:21:36

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-Generated Text Detection

## Purpose of this Project

The purpose of this project is to develop a machine learning model capable of distinguishing between human-written and AI-generated text. This is particularly important in academic settings to ensure the authenticity of student submissions. The project leverages various models, including traditional machine learning techniques like Logistic Regression with TF-IDF, and advanced transformer-based models like BERT, DistilBERT, RoBERTa, and OpenAI's GPT-4o-mini.

## Steps to Run Locally

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up OpenAI API Key**:
    Ensure you have your OpenAI API key set as an environment variable:
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

5. **Run the Streamlit App**:
    ```bash
    python -m streamlit run app.py
    ```

## Description of Each File

- **app.py**: Streamlit app execution file that uses BERT-related models (including DistilBERT and RoBERTa) and ChatGPT-4o-mini to detect AI-generated text. This file sets up the user interface and handles model inference.

- **LogisticRegression.ipynb**: Focuses on Logistic Regression with TF-IDF analysis for detecting AI-generated text. This notebook includes the implementation and evaluation of the model.

- **BERT.ipynb**: Contains the basic BERT model development. It covers training and testing results for both approaches.

- **DistilBERT.ipynb**: Contains the code development for DistilBERT model, including training and testing results. It focuses on fine-tuning the DistilBERT model for the task.

- **RoBERTa.ipynb**: Contains the code development for RoBERTa model, including training and testing results. It focuses on fine-tuning the RoBERTa model for the task.

- **ChatGPT-4o-mini.ipynb**: Utilizes the ChatGPT model via API to detect AI-generated text. This notebook demonstrates how to interact with OpenAI's API and evaluate the model's performance.

- **Training_Essay_Data.csv**: The dataset used for training the models. It consists of essays labeled as human-written or AI-generated.
