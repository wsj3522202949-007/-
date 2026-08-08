---
id: tool-01665
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hatemfaheem/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1665
category: 二、网文 / 长篇 AI 写作系统 库
repo: hatemfaheem/ai-story-generator
stars: 11
url: https://github.com/hatemfaheem/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: feb54957b899e802
  - methods/最强写作方法论_全球最强综合版.md
---

# hatemfaheem/ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hatemfaheem/ai-story-generator
- **Stars**：11
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Generate stories using AI
- **本地描述**：Generate stories using AI
- **拉取时间**：2026-07-23 23:27:36

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">
<br/>
<img src="docs/poster-ai-story.jpg" alt="drawing" width="200"/>

# AI Story Generator

<p>Generate stories using AI. From text to story (pdf and video)..</p>

<a href="https://youtu.be/xURG3wQ0Jtg" target="_blank">
    <img src="https://www.logo.wine/a/logo/YouTube/YouTube-Icon-Full-Color-Logo.wine.svg" width="50">
</a>

<a href="https://dev.to/hatemelseidy/series/24743" target="_blank">
    <img src="https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png" width="40">
</a>

</div>

## Overview

Generate stories using AI. From text to story (pdf and video).

Example videos can be found here: https://www.youtube.com/@ai-story

A sample story can be found under _stories dir. The sample contains raw content (image, text and audio) alongside `final_video.mp4` and `final_story.pdf`.

## High Level Diagram

![Alt text](https://github.com/hatemfaheem/ai-story-generator/blob/main/docs/high-level-diagram.png?raw=true%20"Title")

## Prerequisites

Install `requirements.txt`.

## Try it with a pre-generated story

```
python3 main.py --help
```

Process a pre-generated story.

```
python3 main.py --pickle ./_stories/2023_01_06_17_38_47-Five_Little_Monkeys/story_content.pickle
```

## Generate a new Story

### Open AI Credentials

1. Register with open AI beta: https://beta.openai.com/
2. Get organization and api key.
3. Create a local file named `openai_creds.json` with the below format and put it root dir of the project.

```
{
  "organization":  "xxx-XXXXXXXX",
  "api_key":  "xx-XXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

### Pass a prompt instead of a pickle file

Replace "The Friendly Panda" with your favorite story title/prompt.

```
python3 main.py --prompt "The Friendly Panda"
```

## Using AWS Polly

1. Go to AWS console.
2. Create an IAM User.
3. Attach existing policy `AmazonPollyFullAccess`
4. Under `./credentials` create a new file called `polly-creds.json` and add the below content.

```
{
  "access_key": "xxxxxxxx",
  "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxx"
}
```

## Check Results

Results can be found under _stories directory with a new dir prefixed with date and time of run.

## Important Note

Open AI has limitations/restrictions on what kind of content you can create. So, it may fail to generate text or images for specific words and sentences. 

https://openai.com/dall-e-2/
