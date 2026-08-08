---
id: tool-00302
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: evergit
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ianskelskey/evergit
created: 2026-07-18
updated: 2026-07-18
no: 302
category: 二、网文 / 长篇 AI 写作系统 库
repo: IanSkelskey/evergit
stars: 0
url: https://github.com/ianskelskey/evergit
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
content_hash: b96d77007fd22083
  - methods/最强写作方法论_全球最强综合版.md
---

# IanSkelskey/evergit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ianskelskey/evergit
- **Stars**：0
- **语言**：TypeScript
- **License**：NOASSERTION
- **Topics**：ai, assistant, commit-message, evergreen, evergreen-ils, generative-ai, launchpad
- **GitHub 描述**：A CLI tool for writing commit messages for the Evergreen ILS project.
- **本地描述**：A CLI tool for writing commit messages for the Evergreen ILS project.
- **拉取时间**：2026-07-23 22:47:52

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# EverGit

![Version](https://img.shields.io/badge/version-0.3.1-blue)

![TypeScript](https://img.shields.io/badge/typescript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-00A79D?style=for-the-badge&logo=openai&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logoColor=white)
![Launchpad](https://img.shields.io/badge/Launchpad-F8C300?style=for-the-badge&logo=launchpad&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)

An AI-powered Git helper for the Evergreen ILS project. Evergit uses OpenAI or Ollama models to generate commit messages that adhere to specific standards, streamlining the commit process while reducing manual input.

## Features

-   Generate commit messages using OpenAI's LLM models or local Ollama models.
-   Support for multiple AI providers with configurable defaults.
-   Automatically reference Launchpad bugs in commit messages.
-   Automatically sign off commits with the user's name and email.
-   Select files to stage for commit.
-   Use different models by specifying the model name as an argument.
-   Manage user-specific configuration for name, email, and AI provider settings.

## Requirements

-   `Node.js`, `npm`, and `Git` must be installed on your system.
-   For OpenAI: OpenAI API key (stored in the `OPENAI_API_KEY` environment variable)
-   For Ollama: Ollama running locally or accessible via network (optional: `OLLAMA_API_KEY` for authenticated instances)
-   A launchpad account is required to reference bugs in commit messages.

## Installation

Install `evergit` globally using npm:

```bash
npm install -g evergit
```

## Usage

`evergit` needs to be run in a git repository. It will automatically detect the repository and branch you are on. If run without any arguments, it will display the help message.

## Commands

#### `evergit commit`

Generates a commit message using a LLM model that follows the Evergreen ILS commit message format.

```bash
evergit commit  # Uses the default provider/model and prompts the user to select files to stage
```

-   Prompts the user to select files to stage.
-   Prompts the user for a Launchpad bug number.
    -   References the bug name, description and conversation when generating the commit message using the Launchpad API.
-   Automatically signs off the commit with the user's name and email from the git configuration.

##### Options

-   `-m, --model <model-name>`: Use a specific model to generate the commit message.

    ```bash
    evergit commit --model <model-name> # Uses a specific model
    ```

-   `-a, --all`: Stage all modified files for commit.

    ```bash
    evergit commit --all    # Stages all modified files
    ```

-   `-p, --provider <provider>`: Use a specific AI provider (openai or ollama).

    ```bash
    evergit commit --provider ollama    # Uses Ollama instead of default provider
    ```

#### `evergit config`

Manage user-specific configuration options for name, email, and AI provider settings. If no name and/or email is set, evergit defaults to using the git configuration.

##### Options

-   `--setup-provider`: Interactive setup for AI provider configuration.

    ```bash
    evergit config --setup-provider
    ```

-   `--set <key>`: Set a configuration option. Valid keys are `name`, `email`, `provider`, `openaiModel`, `ollamaModel`, and `ollamaBaseUrl`.

    ```bash
    evergit config --set name "Your Name"
    evergit config --set email "your.email@example.com"
    evergit config --set provider "ollama"
    evergit config --set ollamaModel "llama3.2"
    evergit config --set ollamaBaseUrl "http://localhost:11434"
    ```

-   `--get <key>`: Get a configuration option.

    ```bash
    evergit config --get provider
    evergit config --get ollamaModel
    ```

-   `--clear <key>`: Clear a configuration option.

    ```bash
    evergit config --clear provider
    ```

-   `--get-all`: Get the entire configuration.

    ```bash
    evergit config --get-all
    ```

-   `--edit`: Edit the configuration file manually in the default editor.

    ```bash
    evergit config --edit
    ```

## AI Provider Configuration

### OpenAI (Default)

Evergit uses OpenAI by default. Ensure you have the `OPENAI_API_KEY` environment variable set.

### Ollama

To use Ollama models:

1. Install and run Ollama locally (see [ollama.ai](https://ollama.ai))
2. Configure evergit to use Ollama:
    ```bash
    evergit config --setup-provider
    # Select "ollama" and follow the prompts
    ```
3. Or set manually:
    ```bash
    evergit config --set provider ollama
    evergit config --set ollamaBaseUrl "http://localhost:11434"
    evergit config --set ollamaModel "llama3.2"
    ```
