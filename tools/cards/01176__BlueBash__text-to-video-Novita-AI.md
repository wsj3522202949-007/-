---
id: tool-01176
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: text-to-video-Novita-AI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bluebash/text-to-video-novita-ai
created: 2026-07-18
updated: 2026-07-18
no: 1176
category: 二、网文 / 长篇 AI 写作系统 库
repo: BlueBash/text-to-video-Novita-AI
stars: 7
url: https://github.com/bluebash/text-to-video-novita-ai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: fbf0c9b9fe166313
  - methods/最强写作方法论_全球最强综合版.md
---

# BlueBash/text-to-video-Novita-AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bluebash/text-to-video-novita-ai
- **Stars**：7
- **语言**：Python
- **License**：None
- **Topics**：gpt-4, langchain, novita-ai, openai, streamlit
- **GitHub 描述**：The Video Generator App uses OpenAI to generate story scripts from user-provided topics and NovitaAI to convert these scripts into videos. It's an intuitive Streamlit-based tool for creating engaging video content.
- **本地描述**：The Video Generator App uses OpenAI to generate story scripts from user-provided topics and NovitaAI to convert these scripts into videos. It's an intuitive Streamlit-based tool for creating engaging video content.
- **拉取时间**：2026-07-23 23:13:20

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Video Generator App

The Video Generator App is a Streamlit-based application that allows users to generate story summaries and scripts based on provided topics using the OpenAI API, and then convert these scripts into videos using the NovitaAI API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generate story summaries and scripts based on user-defined topics.
- Convert the generated scripts into videos using the NovitaAI API.
- Display and download the generated videos directly from the app.

## Requirements

- Python 3.8+
- Streamlit
- OpenAI
- Requests

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/video-generator-app.git
   cd video-generator-app
   ```

2. Install the required Python packages:

  ```sh
  pip install -r requirements.txt
  ```

## Usage

1. Run the Streamlit application:

	```sh
	streamlit run app.py
	```
2. Open your web browser and go to http://localhost:8501.

3. Enter the story topic and click "Generate Story" to get the story summary and script.

<img width="1435" alt="Screenshot 2024-05-21 at 1 25 15 PM" src="https://github.com/langchain-tech/text-to-video-musicgen/assets/100914015/4f7384ab-e43e-458a-aaad-3c9e967374f2">

4. Copy the generated Task ID and use it to download the video.

### Configuration
  In the sidebar, configure your API keys:

    - Enter your OpenAI API key.

    - Enter your NovitaAI API key.

### Contributing

  - Contributions are welcome! Please fork the repository and submit a pull request.


### License

  - This project is licensed under the MIT License.

