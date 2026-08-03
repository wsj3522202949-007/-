---
id: tool-05546
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: slop_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/divpreeet/slop_detector
created: 2026-07-18
updated: 2026-07-18
no: 5546
category: 一、去 AI 味 / Humanizer 库
repo: divpreeet/slop_detector
stars: 0
url: https://github.com/divpreeet/slop_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# divpreeet/slop_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/divpreeet/slop_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：an ai code detector made purely in python
- **本地描述**：an ai code detector made purely in python
- **拉取时间**：2026-07-25 18:22:41

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# slop detector


> [!NOTE]
> slop_detector is a ai code detector purely made in python, from the model training to the UI! currently this project supports rust, ts, js, and python, i dont really plan to extend it anymore. 

# how it works 
it's actually pretty simple, at first i gathered datasets for ai code and human written code, from claude, gpt, gemini, hc api, and github respectively, then i extract specific numeric features like ind_len, comment ratio, etc, from the code, i tried my best to keep the features vast and specific to the language it self. after getting features, i export them to a csv, and then use ```scikit-learn``` to train that data and make a model, the model's use the ```RandomForest Classifier``` and a ```TFid Vectorizer```. after that, i made a simple prediction script, which is really just extracting features from the code provided, and then runs it to the model using ```joblib``` and then the model provides an output!

i decided to make a flask app, since it would be more accessible, for that, i just made a simple flask function, which is essentially the same as the prediction code, but it just returns the prediction as a string, which i access through the flask app.

if you're interested, you can also check out the notes.md!

# try it out
the flask app is hosted on [nest](https://slop.divpr.hackclub.app)

