---
id: tool-00245
type: tool
area: 库
status: active
tags: [提示词, Python, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: Style-transfer-assistant
summary: 提示词/写作工作流
source: https://github.com/al-ba22/style-transfer-assistant
created: 2026-07-18
updated: 2026-07-18
no: 245
category: 二、网文 / 长篇 AI 写作系统 库
repo: Al-ba22/Style-transfer-assistant
stars: 0
url: https://github.com/al-ba22/style-transfer-assistant
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 62e3a0b99792336e
  - methods/最强写作方法论_全球最强综合版.md
---

# Al-ba22/Style-transfer-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/al-ba22/style-transfer-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A tool that reformulates a given text into a different tone or writing style.
- **本地描述**：A tool that reformulates a given text into a different tone or writing style.
- **拉取时间**：2026-07-23 22:46:14

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Style Transfer Assistant

This project takes an input text and rewrites it in a different tone using prompt engineering. 

Currently supported tone: **Professional**

## How it Works

- Load a prompt template with `{{TEXT}}` placeholder
- Load a sample input text
- Format the prompt by inserting the text
- Output a ready-to-use prompt (for use with ChatGPT, Claude, etc.)

## File Structure

- `prompts/style_transfer_prompt.txt` – prompt template
- `samples/sample_input.txt` – text to rewrite
- `main.py` – core script

## Error Handling

The script includes basic error handling for:
- Missing input or prompt files
- Empty input text
- Fallback prompt template if none is found


## Example Output

Rewrite the following text in a more professional tone:

```
hey i just wanted to let u know that we’re not gonna make it to the meeting today, something came up
```
