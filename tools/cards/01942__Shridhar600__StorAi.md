---
id: tool-01942
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: StorAi
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shridhar600/storai
created: 2026-07-18
updated: 2026-07-18
no: 1942
category: 二、网文 / 长篇 AI 写作系统 库
repo: Shridhar600/StorAi
stars: 1
url: https://github.com/shridhar600/storai
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
content_hash: cd19da524ffdea6c
  - methods/最强写作方法论_全球最强综合版.md
---

# Shridhar600/StorAi

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shridhar600/storai
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：llm, openrouter-api, python3, twitter
- **GitHub 描述**：This project is a Twitter bot that simulates the daily work experience of a fictional junior developer named Vedant at Ai TechNova Solutions. The bot generates tweets based on a predefined character profile, project description, and a memory of past tweets. It utilizes LLM at its core to generate context aware tweets. 
- **本地描述**：This project is a Twitter bot that simulates the daily work experience of a fictional junior developer named Vedant at Ai TechNova Solutions. The bot generates tweets based on a predefined character profile, project description, and a memory of past tweets. It utilizes LLM at its core to generate context aware tweets.
- **拉取时间**：2026-07-23 23:35:37

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# StorAI

## Description

This project is a Twitter bot that simulates the daily work experience of a fictional junior developer named Vedant at Ai TechNova Solutions. The bot generates tweets based on a predefined character profile, project description, and a memory of past tweets. It uses the OpenRouter API for text generation and the Tweepy library for interacting with the Twitter API.

## Features

*   Generates tweets about a fictional junior developer's work experience.
*   Uses OpenRouter API for natural language generation.
*   Stores past tweets as memories in a JSON file.
*   Supports dry runs (generating tweets without posting).
*   Allows adding tweets as milestones (higher importance).
*   Can run in test mode without Twitter credentials.
*   Can reset all memories.
*   Can view all stored memories.
*   Loads project stages dynamically from a JSON file.
*   Uses `python-decouple` for configuration management.
*   Flexible memory file location via command-line argument.

## Prerequisites

*   Python 3.7+
*   A Twitter developer account and API keys (for posting tweets).
*   An OpenRouter API key.
*   pip

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    (Replace `<repository_url>` and `<repository_name>` with the actual URL and name of your repository.)

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file in the project's root directory.

2.  Add your API keys and other configuration settings to the `.env` file:

    ```
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET=your_twitter_api_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_SECRET=your_twitter_access_secret
    LLM_API_KEY=your_llm_api_key
    LLM_MODEL=your_llm_model  # e.g., gpt-3.5-turbo, gpt-4
    ```

    Replace `your_twitter_api_key`, `your_twitter_api_secret`, etc., with your actual API keys.

## Usage

Run the bot using the `main.py` script. The following command-line arguments are available:

*   `--dry-run`: Generate a tweet but do not post it to Twitter.
*   `--add-milestone`: Save the generated tweet as a milestone (higher importance).
*   `--test-mode`: Run in test mode without requiring Twitter credentials.
*   `--reset`: Clear all memories and start fresh.
*   `--view-memories`: View all stored memories without generating a new tweet.
*   `--memory-file <path>`: Specify a custom path to the memory file (optional).

Examples:

*   Generate and post a tweet:

    ```bash
    python main.py
    ```

*   Generate a tweet without posting (dry run):

    ```bash
    python main.py --dry-run
    ```

*   Add the current tweet as a milestone:

    ```bash
    python main.py --add-milestone
    ```
* Run in test mode:

    ```bash
    python main.py --test-mode
    ```

*   Reset all memories:

    ```bash
    python main.py --reset
    ```

*   View all stored memories:

    ```bash
    python main.py --view-memories
    ```
* Specify a custom memory file:
    ```bash
    python main.py --memory-file data/custom_memories.json
    ```

## Project Structure
```
.
├── .env
├── .gitignore
├── README.md
├── config
│   ├── project_stages.json
│   └── settings.py
├── data
│   └── memories.json
├── generation
│   ├── llm_clients.py
│   └── tweet_generator.py
├── main.py
├── memory
│   ├── models.py
│   └── storage.py
├── requirements.txt
└── twitter
    └── api_client.py
```

## Contributing (Optional)

If you'd like to contribute to this project, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear and descriptive commit messages.
4.  Submit a pull request.

## Roadmap (Optional)
* Integrate with other APIs.
* Improve prompt engineering.
* Add more sophisticated memory management.
* Implement a web interface.
* Add multiple AI agent for fully autonomous Story Telling.
