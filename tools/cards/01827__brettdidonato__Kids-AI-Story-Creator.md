---
id: tool-01827
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Kids-AI-Story-Creator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/brettdidonato/kids-ai-story-creator
created: 2026-07-18
updated: 2026-07-18
no: 1827
category: 二、网文 / 长篇 AI 写作系统 库
repo: brettdidonato/Kids-AI-Story-Creator
stars: 8
url: https://github.com/brettdidonato/kids-ai-story-creator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 86c6b9afde559c89
  - methods/最强写作方法论_全球最强综合版.md
---

# brettdidonato/Kids-AI-Story-Creator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/brettdidonato/kids-ai-story-creator
- **Stars**：8
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：classroom, cloudrun, dalle-3, gemini-pro, google-cloud, image-generation, llm, storybook, streamlit, text-generation
- **GitHub 描述**：Kid safe short story and related image generator. Good for a classroom setting.
- **本地描述**：Kid safe short story and related image generator. Good for a classroom setting.
- **拉取时间**：2026-07-23 23:32:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Kids-AI-Story-Creator
Kid safe short story and related image generator. Good for a classroom setting.

<img src="storybook.webp" alt="storybook" width="300"/>

# About

This repo was created to support a class to teach 2nd graders about AI. It uses Google Gemini to create the story and OpenAI DALL-E 3 to generate a story based image. Students can create two characters and select a story location and story style. This pre-defined input combined with LLM safety filters makes it more suitable for the classroom versus more open ended LLM interactions.

Here is an example input and output:

<img src="create-story.png" alt="create story form" width="500" />

<br>

> <img src="carrot-spaceship.png" alt="carrot spaceship" width="300"/>

> In the vast expanse of outer space, two unlikely friends embarked on an unforgettable adventure. Ada, a curious 7-year-old guinea pig, and Nina, a playful 7 -year-old dog, found themselves stranded on a distant planet.
>
> Ada's tiny paws scurried across the strange rocks, her whiskers twitching with excitement. Nina barked cheerfully, her tail wagging like a propeller. As they explored, they came across a peculiar spaceship shaped like a giant carrot.
>
> With a squeak of delight, Ada hopped inside, followed by Nina. Buttons and dials sparkled all around them, inviting them to play. They pushed and pulled levers, sending the spaceship zooming through the stars.
>
> Suddenly, the spaceship began to shake violently. Ada and Nina squealed in fear as they were tossed about. They crashed into walls and bumped into each other, their laughter mixing with their panicked cries.
>
> Finally, the spaceship came to a stop with a loud thunk. Ada and Nina tumbled out, giggling uncontrollably. They had survived their wild ride through outer space and returned safely to their newfound friendship.

<br>

# Safety Filtering

The LLM safety filtering is enabled via the built in Gemini controls:

```
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}
```

<br>

# Usage

Install required packages:

```
pip install -r requirements.txt
```

Set your environment variables for Google Cloud and OpenAI:

```
export GCP_PROJECT=
export GCP_REGION=
export OPENAI_API_KEY=
```

This application is deployed as a streamlit web interface. Deploy locally as follows:

```
streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

To deploy on GCP Cloud Run, update the variables in the script **gcp_cloud_run_deploy.sh** and execute:

```
./gcp_cloud_run_deploy.sh
```
