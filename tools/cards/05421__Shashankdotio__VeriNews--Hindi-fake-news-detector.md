---
id: tool-05421
type: tool
area: 库
status: active
tags: [文风迁移, Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: VeriNews--Hindi-fake-news-detector
summary: 风格微调/文风迁移
source: https://github.com/shashankdotio/verinews--hindi-fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 5421
category: 一、去 AI 味 / Humanizer 库
repo: Shashankdotio/VeriNews--Hindi-fake-news-detector
stars: 1
url: https://github.com/shashankdotio/verinews--hindi-fake-news-detector
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Shashankdotio/VeriNews--Hindi-fake-news-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shashankdotio/verinews--hindi-fake-news-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：VeriNews is a straightforward web app that swiftly determines whether Hindi news articles are Fake or Real using a finetuned BERT transformer for AI-based text analysis, offering a user-friendly interface for easy interaction.
- **本地描述**：VeriNews is a straightforward web app that swiftly determines whether Hindi news articles are Fake or Real using a finetuned BERT transformer for AI-based text analysis, offering a user-friendly interface for easy interaction.
- **拉取时间**：2026-07-25 18:18:00

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<p align="center">
  <img src="logo.png" alt="Logo" >
</p>

<h1 align="center">📰 VeriNews - Hindi Fake News Detection</h1>

<p align="center">
  Detect whether a Hindi news headline is <strong>Fake</strong> or <strong>Real</strong>.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Made%20with-Python-blue.svg">
  <img alt="Streamlit" src="https://img.shields.io/badge/Powered%20by-Streamlit-brightgreen.svg">
  <img alt="Transformers" src="https://img.shields.io/badge/Model%20based%20on-Transformers-orange.svg">
</p>

***VeriNews*** is a machine learning model that identifies whether Hindi news articles are **Fake** or **Real**. This project leverages **DistilBERT** for accurate classification while maintaining efficient performance on large datasets. It includes Hindi-specific pre-processing steps and a streamlined user interface for model evaluation.

### Languages:  
> Python

## 📚Features

- **🔄Multilingual Support**: Built to handle Hindi language articles.
- **⚡️Efficient Performance**: DistilBERT model provides fast and accurate results with reduced computational load.
- **📝Custom Hindi Pre-processing**: Includes steps like Hindi stop-word removal, stemming, and tokenization.
  
## 🛠️How to Use:

### Step 1: Download the Dataset
1. Go to the [dataset](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/tree/main/dataset)
2. Download the dataset and store it in the `dataset` directory of the project.

### Step 2: Install Required Dependencies
- Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
> [!TIP]  
> Make sure you have Python installed and a virtual environment activated to avoid dependency issues.

### Step 3: Run the Model
- To start the fake news detection model, run the `script.py` file and train the model (if not already).
- To run the model on terminal:
   ```bash
   python script.py
   ```
- To run it on a browser using streamlit (UI):
  ```bash
  streamlit run main.py
  ```
## 🌟Implementation/Output:

### Run the file:
![run file](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/blob/main/snapshots/home.png)

### Enter the news article from testing split:
![enter article](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/blob/main/snapshots/dataset.png)

### Fake or Legit?:
![result 0](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/blob/main/snapshots/fake.png)
![result 1](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/blob/main/snapshots/real.png)
## 📩Doubts?

### Feel free to drop a text  
<p align="left">
<a href="https://www.linkedin.com/in/shashankkamble97" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="shashankkamble97" height="30" width="40" /></a>


##
#### This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shashankdotio/VeriNews--Hindi-fake-news-detector/blob/main/LICENSE) file for details.   
