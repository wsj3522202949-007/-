---
id: tool-05477
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AIGC_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/husuuux/aigc_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5477
category: 一、去 AI 味 / Humanizer 库
repo: husuuux/AIGC_text_detector
stars: 2
url: https://github.com/husuuux/aigc_text_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# husuuux/AIGC_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/husuuux/aigc_text_detector
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：For Mathematics Modeling 
- **本地描述**：For Mathematics Modeling
- **拉取时间**：2026-07-25 18:20:09

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Logistic Regression and Feature Extraction-based Model for Detection of AI-Generated Texts



The codes of our paper "Logistic Regression and Feature Extraction-based Model for Detection of AI-Generated Texts", prepared for Mathematics Modeling Competition of SWU 2024.



## Detector Models



We have open-sourced detector models in the paper as follows.



## About the Dataset



Here we provide the dataset, which contains around 400 abstracts from essays of MIT. We also provide the original documents and their chat4.0-variants for your ease of use. 



#### Data Preprocessing



Here we provide a divided version of the abstract of MIT essays. In this version, all answers are cleaned. However, please use the original version of essays for all experiments in our paper, as we have used the variants of essays in the model training.



##  Preparation



- Install requirement packages:



```shell

pip install -r requirements.txt

```



- Download nltk package punct (This step could be done by ```nltk``` api: ```nltk.download('punkt')```)



- Download pretrained models (This step could be automatically done by ```transformers```)



- Prepare a certain model to compare with, and put it in the folder ```models```, so that you can test the accuracy of the model.



- Split the data files into txt files for training and testing.



- Change the directory of the nltk_data in the utils.py file.



Before running, the directory should contain the following files:



```

├── data

│   ├── chat4.0 Economicspilot

│   │   ├── text1.txt

│   │   ├── text2.txt

│   │   ├── ……

│   │   └── text126.txt

│   ├── Chat4.0 MIT physics pilot

│   │   ├── text1.txt

│   │   ├── text2.txt

│   │   ├── ……

│   │   └── text100.txt

│   ├── MIT physics pilot

│   │   ├── text1.txt

│   │   ├── text2.txt

│   │   ├── ……

│   │   └── text103.txt

│   ├── MIT_Dept. of Economicspilot

│   │   ├── text1.txt

│   │   ├── text2.txt

│   │   ├── ……

│   │   └── text103.txt

│   ├── demo1.txt

│   ├── demo2.txt

│   └── Data interpretation

├── models

│   ├── trained_model

│   │   ├── logistic_regression_model.pkl

│   │   └── tfidf_vectorizer.pkl

├── English_v2

│   ├── model files

│   └── ……

├── README.md

├── utils.py

├── init.py

├── test.py

├── othermodel_test.py

├── requirements.txt

├── train.py

└── demo.py

```



## Training



The script for training is ```train.py```.







