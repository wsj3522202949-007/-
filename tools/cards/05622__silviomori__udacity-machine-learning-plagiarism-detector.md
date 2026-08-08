---
id: tool-05622
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: udacity-machine-learning-plagiarism-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/silviomori/udacity-machine-learning-plagiarism-detector
created: 2026-07-18
updated: 2026-07-18
no: 5622
category: 一、去 AI 味 / Humanizer 库
repo: silviomori/udacity-machine-learning-plagiarism-detector
stars: 4
url: https://github.com/silviomori/udacity-machine-learning-plagiarism-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8bf0486ccca3a383
  - methods/改稿润色指令库.md
---

# silviomori/udacity-machine-learning-plagiarism-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/silviomori/udacity-machine-learning-plagiarism-detector
- **Stars**：4
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：ai, artificial-intelligence, artificial-neural-networks, aws, aws-sagemaker, deep-learning, deep-neural-networks, machine-learning, plagiarism-detector, python, pytorch, sagemaker, udacity, udacity-machine-learning-nanodegree, udacity-nanodegree
- **GitHub 描述**：Build a plagiarism detector that examines a text file and performs binary classification; labeling that file as either plagiarized or not
- **本地描述**：Build a plagiarism detector that examines a text file and performs binary classification; labeling that file as either plagiarized or not
- **拉取时间**：2026-07-25 18:25:32

---

# Plagiarism Project, Machine Learning Deployment

This repository contains code and associated files for deploying a plagiarism detector using AWS SageMaker.

## Project Overview

In this project, you will be tasked with building a plagiarism detector that examines a text file and performs binary classification; labeling that file as either *plagiarized* or *not*, depending on how similar that text file is to a provided source text. Detecting plagiarism is an active area of research; the task is non-trivial and the differences between paraphrased answers and original work are often not so obvious.

This project will be broken down into three main notebooks:

**Notebook 1: Data Exploration**
* Load in the corpus of plagiarism text data.
* Explore the existing data features and the data distribution.
* This first notebook is **not** required in your final project submission.

**Notebook 2: Feature Engineering**

* Clean and pre-process the text data.
* Define features for comparing the similarity of an answer text and a source text, and extract similarity features.
* Select "good" features, by analyzing the correlations between different features.
* Create train/test `.csv` files that hold the relevant features and class labels for train/test data points.

**Notebook 3: Train and Deploy Your Model in SageMaker**

* Upload your train/test feature data to S3.
* Define a binary classification model and a training script.
* Train your model and deploy it using SageMaker.
* Evaluate your deployed classifier.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Please see the [README](https://github.com/udacity/ML_SageMaker_Studies/tree/master/README.md) in the root directory for instructions on setting up a SageMaker notebook and downloading the project files (as well as the other notebooks).

