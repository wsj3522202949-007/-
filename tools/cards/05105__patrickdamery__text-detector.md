---
id: tool-05105
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/patrickdamery/text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5105
category: 一、去 AI 味 / Humanizer 库
repo: patrickdamery/text-detector
stars: 0
url: https://github.com/patrickdamery/text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# patrickdamery/text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/patrickdamery/text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Text Detector AI
- **本地描述**：Text Detector AI
- **拉取时间**：2026-07-25 18:06:18

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<h1>Text Detector</h1>

Model obtains 92% accuracy. Most of the models loss is due to the datasets
including text that is bigger than the kernel size. An increase in accuracy
would be expected if these images where excluded from the training and testing datasets.

If you would like to train this model you will need to Keras with a Tensorflow backend.

You will also need to download the training and testing datasets, these can be found here: https://drive.google.com/file/d/1pCttVLUqRgdfCBYqlbyowjjXEF04RTT7/view?usp=sharing

To generate model use:
python text_detector_generator.py

If you want to run the existing scripts to utilize this model you will need opencv.

To use existing model to make a prediction use (image must be 60x100px):
python detect_text.py path/to/image

If you would like to use any image use:
python detect_draw_text.py path/to/image
