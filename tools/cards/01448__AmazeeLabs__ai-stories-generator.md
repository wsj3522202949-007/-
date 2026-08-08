---
id: tool-01448
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-stories-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/amazeelabs/ai-stories-generator
created: 2026-07-18
updated: 2026-07-18
no: 1448
category: 二、网文 / 长篇 AI 写作系统 库
repo: AmazeeLabs/ai-stories-generator
stars: 1
url: https://github.com/amazeelabs/ai-stories-generator
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
content_hash: 578927fe97c7fb5c
  - methods/最强写作方法论_全球最强综合版.md
---

# AmazeeLabs/ai-stories-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/amazeelabs/ai-stories-generator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：[Experimental]: Storybook stories generator
- **本地描述**：[Experimental]: Storybook stories generator
- **拉取时间**：2026-07-23 23:21:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

This repository provides a Node.js CLI application that leverages OpenAI to automatically generate Storybook stories from your component code.

### Features

  * Reads your component source code (TypeScript currently supported).
  * Generates comprehensive stories.ts files for Storybook.
  * Integrates with existing stories.ts files in the same directory for context.
  * Offers robust error handling and informative messages.

### Installation

1.  **Prerequisites:**

  * Node.js and npm installed on your system ([https://nodejs.org/](https://www.google.com/url?sa=E&source=gmail&q=https://nodejs.org/))

### Usage

1.  **Obtain OpenAI API Key:**

      * Create an OpenAI account and access your API Keys ([https://beta.openai.com/account/api-keys](https://www.google.com/url?sa=E&source=gmail&q=https://beta.openai.com/account/api-keys)).

      * Create a `.env` file in the project root directory and add the following line, replacing `YOUR_OPENAI_API_KEY` with your actual key:

        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```

2.  **Run the script:**

    **Using npx (without installing globally):**

    ```bash
    npx github:AmazeeLabs/ai-stories-generator [path/to/your/component/ts]
    ```

    **Replace `path/to/your/component.ts` with the actual path to your component source code file (e.g., `example.ts`).**

3.  **(Optional) Install Globally:**

    Clone the repo and then:

    ```bash
    npm install -g .
    ```

    This allows you to run the script from anywhere using `ai-story-creator path/to/your/component.ts`.

### Output

The script generates a new `stories.ts` file in the same directory as your component code file, containing the automatically generated Storybook stories.

### Existing Stories Integration

The script reads existing `.stories.ts` files in the same directory and provides snippets of the first 10 lines to OpenAI for context. This can help the model generate more consistent stories that align with existing behavior.

### Additional Notes

  * The script currently supports TypeScript component code.
  * Consider adding comments and descriptions to the generated stories.ts file for better maintainability.

### Contributing

We welcome contributions to this project\! Please see the CONTRIBUTING.md file for guidelines.

### License

This project is licensed under the MIT License (see LICENSE.md).
