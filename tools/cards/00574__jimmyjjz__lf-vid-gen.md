---
id: tool-00574
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: lf-vid-gen
summary: 小说转语音/有声书
source: https://github.com/jimmyjjz/lf-vid-gen
created: 2026-07-18
updated: 2026-07-18
no: 574
category: 二、网文 / 长篇 AI 写作系统 库
repo: jimmyjjz/lf-vid-gen
stars: 1
url: https://github.com/jimmyjjz/lf-vid-gen
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9cec5f7407667438
  - methods/最强写作方法论_全球最强综合版.md
---

# jimmyjjz/lf-vid-gen

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jimmyjjz/lf-vid-gen
- **Stars**：1
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Long-form story video generator via AI and editing automation
- **本地描述**：Long-form story video generator via AI and editing automation
- **拉取时间**：2026-07-23 22:55:48

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Long-Form Story Video Generator via AI and Editing Automation
### Introduction
This project generates long form story videos through an input script. Through editing automation as well as text to speech and text to image one can obtain results like the following:

**Comic Style** (Screenshot)
![Example 1](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/example_image_1.png)

**Youtube Roblox Story Style** (Screenshot)
![Example 2](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/example_image_2.png)

Example videos: https://www.youtube.com/@Robloxuha.

When it comes to the script one can generate it through LLM(s) or write it manually(For formatting specifications please read prompt outputted via [main.py](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/main.py)).

Customizability:
- Animations and motion can be altered(If you understand python and want to learn more visit [animateable.py](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/animateable.py)).
- Setting max vram usage.
- Switching AI models for different tasks.
- Visual images can be any images you want.
- Background can be any video you want.
- Toggleable intermission/title segment.
- Dimensions of the outputted video.
- Generated any number of videos you want.
- Any intro/watermark(animated, video, image, etc) you want.
- And more...

### Setup
1. Enter a python environment.
2. Make sure you are using python 3.11+ interpreter.
3. Install dependencies
```
pip install tortoise_tts==3.0.0 moviepy==2.1.0 diffuser==0.32.1 pydirectinput==1.0.4 faster_whisper==1.1.0
```
4. (Reccomended) Install the version of pytorch that fits your hardware. Visit https://pytorch.org/get-started/locally/ for details.

In the scenario that you are not able or refuse to then
```
pip install pytorch==2.5.1
```

### Usage
1. Setup settings, proceed through [settings.json](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/settings.json)
2. Get a adequately sized mp4(s), name them bgvid# #=1,2,3..., and then throw them into [story-video-generator folder](https://github.com/jimmyjjz/lfs-vid-gen/tree/main/story-video-generator)
3. Obtain/Create a formatted script and copy-paste it into [script.txt](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/script.txt).
4. (Reccomended) Run [script_check.py](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/script_check.py) and if necessary fix up your script.
5. Free up enough vram(Expect ~4-5gb for ~15min video on highest cost mode)
6. Run [main.py](https://github.com/jimmyjjz/lfs-vid-gen/blob/main/story-video-generator/main.py)
