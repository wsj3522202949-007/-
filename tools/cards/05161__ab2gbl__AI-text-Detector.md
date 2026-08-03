---
id: tool-05161
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ab2gbl/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5161
category: 一、去 AI 味 / Humanizer 库
repo: ab2gbl/AI-text-Detector
stars: 1
url: https://github.com/ab2gbl/ai-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ab2gbl/AI-text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ab2gbl/ai-text-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ab2gbl/AI-text-Detector
- **拉取时间**：2026-07-25 18:08:22

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI text Detector 
this is an application web for the model we trained to detect text is it AI-generated or Human-written.

# setup 
first you need to download [the trained model](https://www.kaggle.com/models/abdessamiguebli/ai_detection_model_200k/) and extract it inside this repo
then you should install the requirements on your virtual environment ( search how to create virtual environment, it's not hard )

```bash
  virtualenv env                    # create virtual eniveronement
  source ./env/bin/activate         # or ".\env_name\Scripts\activate" for windows
  pip install -r requirements.txt   # install the requirement
```
after installing the requirement , we need to download the next 2 Corpus by nltk, so first change the download path to your environment, on terminal, execute the next:
```bash
export NLTK_DATA=./env/nltk_data 
```
then python, tun the next code to download the 2 corpus: 

```bash
python ./install_corpus.py
```
there is a problem on *wordnet* corpus , so we need to unzip it too , so we should execute the next command:

```bash
unzip ./env/nltk_data/corpora/wordnet.zip -d ./env/nltk_data//corpora/   # or the path to your zip file 
```
now we ready to run the website
```bash
python manage.py runserver
```
<div align="center">
  <img width="100%" alt="screenshot" src="./screenshot.png"  />
</div>

