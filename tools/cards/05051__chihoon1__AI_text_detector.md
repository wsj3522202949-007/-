---
id: tool-05051
type: tool
area: 库
status: active
tags: [RAG, 文风迁移, Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 人物设定, 改稿润色, 本地写作]
title: AI_text_detector
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/chihoon1/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5051
category: 一、去 AI 味 / Humanizer 库
repo: chihoon1/AI_text_detector
stars: 0
url: https://github.com/chihoon1/ai_text_detector
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 782540171bc13fa6
  - methods/改稿润色指令库.md
---

# chihoon1/AI_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/chihoon1/ai_text_detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：chihoon1/AI_text_detector
- **拉取时间**：2026-07-25 18:04:17

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Generated Text Detector

## Dataset
I usd the dataset released in released by the GenAI Content Detection competition for cross-domain machine-generated text detection. The dataset is comprised of 
texts written by human and various AI models, covering wide range of topics. Since there is no testing data with ground truth label, I split the training data into training, validation and testing purposes.

## Model Selection Reasoning
I chose RAG model to detect AI generated text. RAG can equip the generator model background knowledge and information of the subject of the written text by retrieving the relevant documents from the vector database. This ability will add a lot of benefits to generator model to detect texts written by AI as the texts are talking about wide spectrum of subjects.

## Installation
First, make sure virtual environment is set up before installing all packages.
Run the following command in the terminal:

`pip install -r requirements.txt`

## Repository Structure
#### Experiment
Creating and tuning RAG model for AI generated text detection is done in `RAG_model_for_AI_text_detection.ipynb`

Exploratory data analysis and data processing of the dataset and visualization is also performed in the same jupyter notebook file. The jupyter notebook was run in google colab on gpu device

#### Python Files
All the functions and classes required for building a RAG model and fine tuning with LoRA and QLoRA is defined in python files under the directory `src`

#### Python Scripts
`prepare_documents.py`, `qlora_training.py`, and `rag_tuning.py` files provide python scripts to automate the vector database document preparation, Q-LoRA tunning, and RAG model creation and tuning, respectively.

For example, type the following command in the terminal to run Q-LoRA tuning from training to evaluation

`python qlora_training.py -c config/qlora.yaml`

In the above example, you can configure model and training hyperparameters in this configuration file `config/qlora.yaml`.
Please feel free to modify configuration file.


## Results
RAG model achieved approximately 98% testing accuracy and weighted f1 score to detect AI generated text in cross-domain subjects.
Please check the details in `RAG_model_for_AI_text_detection.ipynb`
