---
id: tool-00194
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: groq-storyteller
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rekkitcwts/groq-storyteller
created: 2026-07-18
updated: 2026-07-18
no: 194
category: 二、网文 / 长篇 AI 写作系统 库
repo: rekkitcwts/groq-storyteller
stars: 1
url: https://github.com/rekkitcwts/groq-storyteller
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# rekkitcwts/groq-storyteller

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rekkitcwts/groq-storyteller
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：artificial-intelligence, flask, flask-sqlalchemy, groq, groq-ai, groq-ai-api, groq-api, python, sqlite, story-generation
- **GitHub 描述**：An AI-powered high school-themed story generator, using the Groq API. Allows saving to a database for easy reading.
- **本地描述**：An AI-powered high school-themed story generator, using the Groq API. Allows saving to a database for easy reading.
- **拉取时间**：2026-07-23 22:44:41

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Groq-Storyteller

Groq-Storyteller is a self-hosted AI story generator made with Python and Groq API. Requires Python 3.9 or above, and an Internet connection. You will also need your Groq API key.

## Installation

- Assuming you have Python, use the following command first:

```bash
pip install -r requirements.txt
```

- Create a .flaskenv file and add the following variables:

```
FLASK_APP=everglen_web.py
GROQ_API_KEY=(please use your Groq API key)
```

## Usage

* When not running on a WSGI server, use the following command:

```bash
flask run --host=0.0.0.0
```

* Open a web browser and enter the IP address and port number shown on the terminal, e.g. 192.168.1.13:5000

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `[LICENSE](LICENSE)` file for details.
