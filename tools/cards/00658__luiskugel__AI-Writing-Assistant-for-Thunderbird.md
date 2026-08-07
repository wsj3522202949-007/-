---
id: tool-00658
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Writing-Assistant-for-Thunderbird
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/luiskugel/ai-writing-assistant-for-thunderbird
created: 2026-07-18
updated: 2026-07-18
no: 658
category: 二、网文 / 长篇 AI 写作系统 库
repo: luiskugel/AI-Writing-Assistant-for-Thunderbird
stars: 3
url: https://github.com/luiskugel/ai-writing-assistant-for-thunderbird
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# luiskugel/AI-Writing-Assistant-for-Thunderbird

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/luiskugel/ai-writing-assistant-for-thunderbird
- **Stars**：3
- **语言**：JavaScript
- **License**：Apache-2.0
- **Topics**：ai, e-mail, email, gpt-4, improve, ki, llama, llm, thunderbird, thunderbird-addon, writing-tool
- **GitHub 描述**：A Thunderbird extension that helps improve your email writing using various AI models (LLMs) and customizable prompts. This extension can enhance your email's writing style, tone, and formatting while maintaining the original message.
- **本地描述**：A Thunderbird extension that helps improve your email writing using various AI models (LLMs) and customizable prompts. This extension can enhance your email's writing style, tone, and formatting while maintaining the original message.
- **拉取时间**：2026-07-23 22:58:14

---

# AI Writing Assistant for Thunderbird

A Thunderbird extension that helps improve your email writing using various AI models (LLMs) and customizable prompts. This extension can enhance your email's writing style, tone, and formatting while maintaining the original message.

## ✨ Features

![Usage](demo.gif)

### Multiple AI Models Support

| **OpenAI**        | **Groq**                | **Google**        | **Selfhosted/Other** |
| ----------------- | ----------------------- | ----------------- | -----------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| GPT-4 Turbo       | Llama 3.3 70B Versatile | Gemini 2.0 Flash  | [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#model-library) (\*) |
| GPT-4 Turbo Mini  | Llama 3.2 3B Preview    |                   |                      |
| GPT-3.5 Turbo     |                         |                   |                      |

API keys are required to use the extension with non-self-hosted models. You can obtain API keys from the respective AI service providers.

(\*) Requires to set 'OLLAMA_ORIGINS "moz-extension://*" as described [here (github.com)](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-allow-additional-web-origins-to-access-ollama).

### Customizable Settings

- **Model Selection**: Choose your preferred AI model
- **Custom Prompts**: Set your own prompt for email improvement
- **Temperature Control**: Adjust the creativity level (0-2)
  - Lower values (0-1): More focused and deterministic responses
  - Higher values (1-2): More creative and diverse responses
- **Max Tokens**: Control the maximum length of AI responses (1-4000)

Settings can be accessed from the Thunderbird add-ons list.

### Privacy & Transparency

- Your email content is only sent to the AI service when you click the "Improve Writing" button. Keep in mind that the AI service may handle and store your data according to their privacy policy. If your hardware supports it, **use self-hosted models for better privacy**.
- No data is stored locally except for your settings
- API keys are stored securely in your browser's local storage.
- The extension is **open-source** and kept **simple for transparency**. You can review the code and contribute to the project.

## 🚀 Installation

1. Download the extension '.zib' file from the releases page.
2. In Thunderbird, go to _Tools > Add-ons_
3. Click the gear icon > _Install Add-on From File_
4. Choose the downloaded file

### First-Time Setup

1. When you first install the extension, it will automatically open the settings page
2. Enter your API key for your chosen AI model
3. Configure your preferred settings:
   - Select your AI model
   - Set temperature (0-2)
   - Set max tokens (1-4000)
   - Customize the improvement prompt

### Usage

1. Draft a new email in Thunderbird
2. Click the "Improve Writing" button in the compose window
3. Wait for the AI to process your email
4. The improved version will replace your original draft - without messing up conversation history.

## ✅ Requirements

- Thunderbird 78.0+
- API key from a supported AI provider
- Internet connection

## 🛠️ Troubleshooting

- Double-check your API key
- Ensure internet access
- Use a supported Thunderbird version
- Read error messages for hints

## 🤝 Contributing

We welcome bug reports and pull requests! See our [CONTRIBUTING.md](https://github.com/luiskugel/AI-Writing-Assistant-for-Thunderbird/blob/main/CONTRIBUTING.md) for more details.

## License

This project is licensed under the [Apache License 2.0](https://github.com/luiskugel/AI-Writing-Assistant-for-Thunderbird/blob/main/LICENSE) - see the [LICENSE](https://github.com/luiskugel/AI-Writing-Assistant-for-Thunderbird/blob/main/LICENSE) file for details.

Icons adapted from [pepicons](https://github.com/CyCraft/pepicons/) (CC BY 4.0).
