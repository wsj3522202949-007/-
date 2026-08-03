---
id: tool-05233
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-TextDetector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/hnjm/ai-textdetector
created: 2026-07-18
updated: 2026-07-18
no: 5233
category: 一、去 AI 味 / Humanizer 库
repo: hnjm/AI-TextDetector
stars: 1
url: https://github.com/hnjm/ai-textdetector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# hnjm/AI-TextDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hnjm/ai-textdetector
- **Stars**：1
- **语言**：None
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：This tool uses the OpenAI API to check text if AI generated
- **本地描述**：This tool uses the OpenAI API to check text if AI generated
- **拉取时间**：2026-07-25 18:11:00

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-TextDetector

Install .NET Core SDK on your system. You can download it from https://dotnet.microsoft.com/download/dotnet-core/3.1

Create a text file with the passages you want to classify enclosed in quotations, like this:
"passage here"

Run the tool from the terminal/command line using the following command:
dotnet run

Enter the name of the text file when prompted. The file should be in the same directory where you are running the tool from.

Enter your OpenAI API authorization bearer token when prompted. You can get the token from here https://platform.openai.com/ai-text-classifier

The tool will send the passages to the OpenAI API for classification and print out the top classification result for each passage along with the confidence percentage.

The classification results will be one of the following:
very unlikely
unlikely
unclear if it is
possibly
likely

The confidence percentage indicates how confident the AI model is in the classification. Higher the percentage, higher the confidence.

You can modify the input parameters like maximum tokens, temperature, etc. in the RequestPayload class to tune the model's output. Refer to the OpenAI API documentation for more details.

Let me know if you have any other questions!
