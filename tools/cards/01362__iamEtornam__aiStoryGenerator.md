---
id: tool-01362
type: tool
area: 库
status: active
tags: [Dart, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: aiStoryGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/iametornam/aistorygenerator
created: 2026-07-18
updated: 2026-07-18
no: 1362
category: 二、网文 / 长篇 AI 写作系统 库
repo: iamEtornam/aiStoryGenerator
stars: 0
url: https://github.com/iametornam/aistorygenerator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: bf30eb759dc80338
  - methods/最强写作方法论_全球最强综合版.md
---

# iamEtornam/aiStoryGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/iametornam/aistorygenerator
- **Stars**：0
- **语言**：Dart
- **License**：None
- **Topics**：ai, dart, deepgram, flutter, gemini, ghana
- **GitHub 描述**：This is a repo for my "From Blank Page to Brilliance: Generate Captivating Stories with AI" talk
- **本地描述**：This is a repo for my "From Blank Page to Brilliance: Generate Captivating Stories with AI" talk
- **拉取时间**：2026-07-23 23:18:50

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ai Story Generator

This repository was created for a talk:

### Session title
From Blank Page to Brilliance: Generate Captivating Topics with AI

### Speaker participation
In-person, Virtual

### Session abstract
This session explores a novel approach using Gemini, a powerful large language model (LLM), and Flutter, a leading mobile app framework. We'll delve into Gemini's capabilities for understanding user preferences and generating compellling stories.

Next, we'll showcase the development process of a user-centric mobile application built with Flutter. This app seamlessly integrates Gemini's suggestions to offer writers and speakers a dynamic and inspiring brainstorming tool. Finally, we'll discuss the benefits of hosting the app on Firebase, ensuring smooth deployment and accessibility.

### Speaker participation type
- In-person, Virtual

### Audience level
- Beginner, Intermediate, Advance

## Art
<p>
<tr>
    <td><img align="left" src="https://raw.githubusercontent.com/iamEtornam/aiStoryGenerator/main/screenshots/art_1.png" width="200" height="400"/></td>
    <td><img src="https://raw.githubusercontent.com/iamEtornam/aiStoryGenerator/main/screenshots/art_2.png" width="200" height="400"/></td> 
</tr>
</br>
<tr>
    <td><img align="left" src="https://raw.githubusercontent.com/iamEtornam/aiStoryGenerator/main/screenshots/art_3.png" width="200" height="400"/></td>
    <td><img src="https://raw.githubusercontent.com/iamEtornam/aiStoryGenerator/main/screenshots/art_4.png" width="200" height="400"/></td> 
</tr>
</br>
<tr>
    <td><img align="left" src="https://raw.githubusercontent.com/iamEtornam/aiStoryGenerator/main/screenshots/art_5.png" width="200" height="400"/></td>
       <td><p></p></td>
</tr>
</p>
</br>

## Getting Started

This project is a starting point for a Flutter application.

To clone this project,
open your terminal or cmd

```
cd folder/to/clone-into/
```

```
git clone https://github.com/iamEtornam/aiStoryGenerator.git
```

Then
locate the project on your system and open with android studio or Vscode or intellij IDE.

To Run:
```
 flutter pub get

```
then run:

```
 flutter run --dart-define=DEEPGRAM_API_KEY=<YOUR deepgram.com API KEY HERE> --dart-define=GOOGLE_API_KEY=<YOUR Gemini API KEY HERE>

```

## Build release version

```
run: flutter build <OS PLATFORM> e.g flutter build ios --dart-define=DEEPGRAM_API_KEY=<YOUR deepgram.com API KEY HERE> --dart-define=GOOGLE_API_KEY=<YOUR Gemini API KEY HERE>
```


## Resources

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://flutter.dev/docs/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://flutter.dev/docs/cookbook)
- [Deepgram docs](https://deepgram.com/)

For help getting started with Flutter, view our
[online documentation](https://flutter.dev/docs), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

## Prerequisites

What things you need to run the app

```
* Android Studio/Vscode/Intellij IDE
* Flutter SDK
* Android SDK
* MacBook (optional)
```

## How to contribute

- **Fork the repository and clone it locally**. Connect your local to the original “upstream” repository by adding it as a remote. Pull in changes from “upstream” often so that you stay up to date so that when you submit your pull request, merge conflicts will be less likely. (See more detailed instructions here.)
- **Create a branch** for your edits.
- **Reference any relevant issues** or supporting documentation in your PR (for example, “Closes #37.”)
- **Include screenshots of the before and after** if your changes include differences in HTML/CSS. Drag and drop the images into the body of your pull request.
- **Test your changes!** Run your changes against any existing tests if they exist and create new ones when needed. Whether tests exist or not, make sure your changes don’t break the existing project.
- **Contribute in the style of the project** to the best of your abilities. This may mean using indents, semi-colons or comments differently than you would in your own repository, but makes it easier for the maintainer to merge, others to understand and maintain in the future.

## Built With

- [Android Studio](https://developer.android.com/studio/install) - How to install Android Studio
- [Flutter](https://flutter.dev) - Flutter Official website

## Author 😊

**Etornam Sunu Bright**

- [**Twitter**](https://bit.ly/3ivb9GC)
- [**Linkedin**](https://bit.ly/3iyxOl8)
