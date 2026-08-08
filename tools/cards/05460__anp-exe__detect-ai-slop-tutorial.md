---
id: tool-05460
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: detect-ai-slop-tutorial
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/anp-exe/detect-ai-slop-tutorial
created: 2026-07-18
updated: 2026-07-18
no: 5460
category: 一、去 AI 味 / Humanizer 库
repo: anp-exe/detect-ai-slop-tutorial
stars: 0
url: https://github.com/anp-exe/detect-ai-slop-tutorial
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 114ba19f48c906ba
  - methods/改稿润色指令库.md
---

# anp-exe/detect-ai-slop-tutorial

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/anp-exe/detect-ai-slop-tutorial
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-slop, ai-slop-detection, codedex, tutorial
- **GitHub 描述**：This is a project for the Codédex monthly tutorial challenge. It creates an AI slop detector to be used on Linkedin.
- **本地描述**：This is a project for the Codédex monthly tutorial challenge. It creates an AI slop detector to be used on Linkedin.
- **拉取时间**：2026-07-25 18:19:31

---

# LinkedIn Slop Detector

This repo is for the **Codédex monthly challenge**. The full tutorial can be found here: **[TUTORIAL.md](https://github.com/anp-exe/detect-ai-slop-tutorial/blob/main/TUTORIAL.md)**.

> [!NOTE]
> If you're here for the tutorial, you'll need to download two files from this repo and drop them into your project folder: the emoji font **[`NotoColorEmoji.ttf`](https://github.com/anp-exe/detect-ai-slop-tutorial/blob/main/NotoColorEmoji.ttf)** (so your card looks the same on every computer) and the card generator **[`card.py`](https://github.com/anp-exe/detect-ai-slop-tutorial/blob/main/card.py)**.

<p align="center">
  <img src="images/codedex.gif" width="150">
</p>

It's a Python tool that reads any LinkedIn post and gives it a **Slop Score /100** with a verdict, then saves it as 
a shareable card. Along the way you'll learn to use the **Hugging Face API** for zero-shot text classification and blend AI judgment with your own transparent rules.

<p align="center">
  <img src="samples/1_certified_artisanal_slop.png" width="30%">
  <img src="samples/5_an_actual_human.png" width="30%">
</p>

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv Pillow
```

Add your Hugging Face token to a `.env` file (see the [tutorial](https://github.com/anp-exe/detect-ai-slop-tutorial/blob/main/TUTORIAL.md) for how to get one):

```
HF_TOKEN=hf_your_token_here
```

Then run it:

```bash
python slop.py
```

## What's in here

| File | What it does |
|------|-----------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `slop.py` | The main detector: rule signals + Hugging Face scoring |
| `card.py` | Draws the shareable score card with Pillow |
| `NotoColorEmoji.ttf` | Emoji font so the card looks the same on every computer |
| `TUTORIAL.md` | The full step-by-step build tutorial |
| `WRITE-UP.md` | Behind the scenes: how the idea came together and the challenges I hit |
| `images/` | Screenshots and example cards used in the tutorial |

## More resources

- [Hugging Face Inference API docs](https://huggingface.co/docs/api-inference)
- [Zero-shot classification explained](https://huggingface.co/tasks/zero-shot-classification)
- [Pillow documentation](https://pillow.readthedocs.io/)
