---
id: tool-05461
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Bert-Toxic-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/vbookshelf/bert-toxic-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5461
category: 一、去 AI 味 / Humanizer 库
repo: vbookshelf/Bert-Toxic-Text-Detector
stars: 7
url: https://github.com/vbookshelf/bert-toxic-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5d17efdd1430a58c
  - methods/改稿润色指令库.md
---

# vbookshelf/Bert-Toxic-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vbookshelf/bert-toxic-text-detector
- **Stars**：7
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：A flask web app that demonstrates a method to use the Bert language model as an Ai microservice.
- **本地描述**：A flask web app that demonstrates a method to use the Bert language model as an Ai microservice.
- **拉取时间**：2026-07-25 18:19:33

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Bert-Toxic-Text-Detector
A flask web app that demonstrates a method to use the Bert language model as an Ai microservice.

The demo app is now offline.<br>
Demo App: http://toxic.test.woza.work/

<br>

<img src="http://toxic.test.woza.work/assets/app_pic1.png" width="350"></img>

<br>

My goal for this project was learn how to build and deploy a production-grade toxic text detection model. Users are able to send text to the model, via an API, and get back predictions. I'm not a frontend or backend expert. I tried to learn enough to get things working.

One way to commercialize a powerful language model like Bert is to deploy it as a microservice. This means that the model lives on a cloud server. Websites can send text to this server. The server responds by sending back a toxicity prediction for each piece of text. The system can also be set up to allow a user to send a file containing rows of text. The model will process this file and the server will return a new file with a prediction for each row.

A tool like this could automatically monitor large volumes of online dialogue. It could help improve the quality of online conversations, protect children from online bullying and protect a companies brand image - but it could also be used for mass surveillance.

Model AUC score: 0.88

The process used to build and train the model is described in this Kaggle kernel:<br>
https://www.kaggle.com/vbookshelf/bert-as-a-microservice-flask-app

The model was fine tuned using data made available during the Kaggle Jigsaw Multilingual Toxic Comment Classification compeition. The data is licenced for any use.<br>
https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification


### Server Deployment

I suggest that you deploy on a Linux server running Ubuntu 16.04. Start with a server that has 4GB of RAM and two CPUs. Once you get the app running you can then test it on smaller and cheaper servers.

All the frontend and backend code is available in this repo. The model is not included because it was too large to upload. It can be downloaded by following the Kaggle notebook link above. Please put the model inside the subfolder called 'flask' before uploading the entire Toxic Comment Detector folder to your server.

The code is set up to be run as a Docker container. It's based on this video tutorial:

Julian Nash docker and flask video tutorial<br>
https://www.youtube.com/watch?v=dVEjSmKFUVI

The .dockerignore file may not be visible. Please create this file if you don't see it. In this repo I've included a txt file that explains the steps for installing Docker and Docker Compose on a Linux server. 
