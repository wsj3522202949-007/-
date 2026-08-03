---
id: tool-03391
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档]
title: AI-Gherkin-Generator
summary: 剧本/短剧脚本生成
source: https://github.com/mvsaran/ai-gherkin-generator
created: 2026-07-18
updated: 2026-07-18
no: 3391
category: 十、短剧 / 剧本 / 影视化生成 库
repo: mvsaran/AI-Gherkin-Generator
stars: 1
url: https://github.com/mvsaran/ai-gherkin-generator
tier: "B"
use_case: "剧本/短剧脚本生成"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/模板库.md
---

# mvsaran/AI-Gherkin-Generator

- **分类**：十、短剧 / 剧本 / 影视化生成 库
- **链接**：https://github.com/mvsaran/ai-gherkin-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered tool built with **Node.js**, **TypeScript**, and **OpenAI** to generate high-quality BDD Gherkin scenarios from user stories.
- **本地描述**：An AI-powered tool built with **Node.js**, **TypeScript**, and **OpenAI** to generate high-quality BDD Gherkin scenarios from user stories.
- **拉取时间**：2026-07-23 23:54:04

---

# AI Gherkin Generator 🚀

An AI-powered tool built with **Node.js**, **TypeScript**, and **OpenAI** to generate high-quality BDD Gherkin scenarios from user stories.

## 📖 Overview

This project uses **Few-Shot Prompting** to ensure that the generated Gherkin scenarios are consistent, testable, and follow industry best practices. By providing the AI with high-quality examples (Given/When/Then), we drastically improve the accuracy and relevance of the output.

### What is Gherkin?
Gherkin is a Domain Specific Language (DSL) used for writing BDD (Behavior Driven Development) test cases in a human-readable format. It uses keywords like `Feature`, `Scenario`, `Given`, `When`, and `Then`.

### Why Few-Shot Prompting?
Few-shot prompting involves providing the LLM with a few examples (shots) of the desired task before asking it to perform the task for a new input. This "teaches" the model the specific pattern, tone, and constraints we expect.

### 🧠 How Few-Shot Prompting is Used Here
In this project, the few-shot logic is centralized in `src/prompts/fewShotPrompt.ts`. 

The prompt is constructed using the following layers:
1.  **System Persona**: Defines the AI as a "Senior QA Automation Engineer".
2.  **Explicit Instructions**: Sets constraints like scenario count (2 pos, 2 neg, 1 edge) and BDD requirements.
3.  **Example 1 (Password Reset)**: Shows a complete User Story → Gherkin mapping.
4.  **Example 2 (Shopping Cart)**: Shows how to handle edge cases like "Maximum available stock".
5.  **Target Injection**: Appends the *actual* user story at the end, asking the AI to continue the pattern established by the examples.

This approach ensures that even if the AI is updated, the output remains grounded in the specific BDD style defined in our examples.

---

## 🛠 Features

- **Prompt Engineering**: Uses few-shot prompting for consistent Gherkin structure.
- **Scenario Types**: Generates Positive, Negative, and Edge Case scenarios.
- **Validation**: Automatically validates that scenarios contain required Gherkin keywords.
- **Token Tracking**: Monitors OpenAI token usage for every run.
- **CLI Support**: Input user stories via CLI arguments or markdown files.

---

## ⚙️ How Outputs are Generated

The generation workflow follows a deterministic pipeline to ensure quality:

1.  **Ingestion**: The tool reads the user story from `inputs/user-story.md` (default) or the `--story` CLI flag.
2.  **Prompt Construction**: The `Prompts/fewShotPrompt.ts` utility wraps the story in a high-context prompt containing the few-shot examples.
3.  **AI Inference**: The constructed prompt is sent to `OpenAI` (via the service in `services/openaiClient.ts`).
4.  **Validation**: Once the AI returns the Gherkin text, the `utils/validator.ts` checks:
    - Minimum of 5 scenarios.
    - Presence of `Given`, `When`, and `Then` keywords in every scenario.
5.  **Persistence**: If validation passes (or with a warning if not), the tool writes the results to the `/outputs` folder.

## 📂 Output Locations

After running `npm run generate`, you can find the results in:
- **`outputs/gherkin.md`**: The raw, high-quality Gherkin text ready to be copy-pasted into your test files.
- **`outputs/gherkin.json`**: A structured JSON object of scenarios and steps (useful for programmatic integration).
- **`outputs/token-usage.json`**: Metadata showing precisely how many `prompt` and `completion` tokens were used.

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v16+)
- An OpenAI API Key

### Installation

1. Clone the repository or navigate to the project directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up environment variables:
   - Create a `.env` file from `.env.example`.
   - Add your `OPENAI_API_KEY`.

### Running the Generator

#### Using a File Input
Place your user story in `inputs/user-story.md` and run:
```bash
npm run generate
```

#### Using CLI Argument
```bash
npm run generate -- --story "As a user, I want to filter search results by date."
```

#### Development Mode
```bash
npm run dev
```

---

## 📂 Project Structure

```text
ai-gherkin-generator/
├── src/
│   ├── prompts/          # Few-shot prompt logic
│   ├── services/         # OpenAI API integration
│   ├── utils/            # File handling & validation
│   ├── types/            # TypeScript interfaces
│   └── index.ts          # CLI entry point
├── inputs/               # Place user-story.md here
├── outputs/              # Generated Gherkin & Metadata
├── .env.example
├── package.json
├── tsconfig.json
└── README.md
```

---

## 📝 Example Output

**Feature: User Login**

**Scenario: Successful login with valid credentials**
- **Given** the user is on the login page
- **When** the user enters valid email and password
- **Then** the user should be redirected to dashboard

related:
  - methods/模板库.md
---

## 🏗 Engineering Notes
- Written in **Clean Architecture** patterns.
- Fully typed with **TypeScript**.
- Modularized for easy extension (e.g., adding more few-shot examples).
