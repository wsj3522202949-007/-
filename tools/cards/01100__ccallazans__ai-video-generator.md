---
id: tool-01100
type: tool
area: 库
status: active
tags: [TTS, Go, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-video-generator
summary: 小说转语音/有声书
source: https://github.com/ccallazans/ai-video-generator
created: 2026-07-18
updated: 2026-07-18
no: 1100
category: 二、网文 / 长篇 AI 写作系统 库
repo: ccallazans/ai-video-generator
stars: 183
url: https://github.com/ccallazans/ai-video-generator
tier: "A"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ccallazans/ai-video-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ccallazans/ai-video-generator
- **Stars**：183
- **语言**：Go
- **License**：None
- **Topics**：docker, generative-ai, golang, llm, ollama, python, video-processing
- **GitHub 描述**：Automate Creation of Story-Based Videos.
- **本地描述**：Automate Creation of Story-Based Videos.
- **拉取时间**：2026-07-23 23:11:06

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 📽️ AI Video Story Generator

This project utilizes Ollama LLM to create video text ideas based on user prompts. It takes a prompt from the user and generates a story, which is then converted into audio using AI. Subsequently, captions are generated from the audio, and finally, these captions are merged into a video.

## 🚀 How It Works

1. **Prompt Input**: Users provide a prompt to the system.
2. **Text to Text**: AI generates a story based on the provided prompt.
3. **Text to Speech**: The story is converted into audio using AI text-to-speech technology.
4. **Caption Generation**: AI generates captions from the audio.
5. **Video Creation**: Captions are merged into a video.

## 🛠️ How to Run

### Prerequisites
- Docker installed on your system
- At least ~5.5GB of RAM to run all applications and llm models

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ccallazans/ai-video-generator.git
    cd ai-video-generator
    ```
2. Start the Docker containers:
    ```sh
    make start
    ```

Once the containers are up and running, you can access the AI video story generator through its provided interface or API endpoints. The first time may be slow because it has to download the Ollama model and Python Torch requirements, but subsequent runs will be faster because Docker keeps it in cache.

### Usage

#### Send a POST request with the content you want to be generated
```sh
curl --location 'http://localhost:8080/api/v1/generate' \
--header 'Content-Type: application/json' \
--data '{
    "message": "Tell me a story about Bahia"
}'
```

The generated videos are saved on the "generated" folder.

## 🖥️ To Run Locally
1. Install Ollama:
    Instructions on: https://ollama.com/download

2. Create a Python 3 environment and install its dependencies:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the Golang application:
    ```sh
    go run cmd/*
    ```

## 📂 Additional Notes
- To add more background videos, put it inside resources/videos folder. The video is random selected, so change on code if want.
- Ensure that Docker is properly configured and running on your system.
- Adjust any necessary configurations in the Dockerfile or docker-compose.yml file according to your requirements.
- For production use, ensure proper security measures and scalability considerations are implemented.
- Fell free to change the ollama model. Choose one from https://ollama.com/library. Im using orca-mini on this project

Feel free to explore and modify the project according to your needs! If you encounter any issues or have suggestions for improvement, please don't hesitate to open an issue or submit a pull request.
