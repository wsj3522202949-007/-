---
id: tool-01559
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: PromptCrafter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hari-bonthu/promptcrafter
created: 2026-07-18
updated: 2026-07-18
no: 1559
category: 二、网文 / 长篇 AI 写作系统 库
repo: Hari-bonthu/PromptCrafter
stars: 0
url: https://github.com/hari-bonthu/promptcrafter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Hari-bonthu/PromptCrafter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hari-bonthu/promptcrafter
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：This is an Web application to enhance the raw writing prompts into the well optimised AI understandable Prompt with prominent score and better Improvements to it. 
- **本地描述**：This is an Web application to enhance the raw writing prompts into the well optimised AI understandable Prompt with prominent score and better Improvements to it.
- **拉取时间**：2026-07-23 23:24:33

---

# PromptCraft Pro 🚀

An industry-grade, developer-first prompt engineering workspace. **PromptCraft Pro** allows you to structure, optimize, catalog, compare, and evaluate prompts for Large Language Models (specifically optimized for Google Gemini models) directly in your browser.

Built with a premium dark glassmorphism theme, vanilla CSS variables, React, TypeScript, and Vite.

---

## ✨ Features

### 1. 🧬 Lightweight Template Compiler
* Supports dynamic variable replacements via `{{variable}}`.
* Supports **Default Values** (e.g. `{{language=python}}`).
* Supports **Choice Enums** (e.g. `{{framework:react|vue|svelte}}`), which automatically render as select dropdowns.

### 2. 🔀 Conditional Compilation Blocks
* Supports conditional text rendering using `{% if variable %} ... {% endif %}` tags.
* Conditional keys render as interactive checkbox toggles in the variable manager.
* Compiles out or renders blocks instantly based on toggle states.

### 3. 📂 Prompt Catalog manager (Import/Export)
* A sidebar manager to save your current active drafts as reusable templates.
* Export your entire template catalog as a single backup `.json` file.
* Import catalogs to restore or share setups across environments.

### 4. ⚖️ Dual Model comparison Playground
* Side-by-side execution interface to compare prompt behaviors.
* Run prompts concurrently against `gemini-2.5-flash` and `gemini-2.5-pro`.
* Measures actual latency (ms) and estimates response token sizes.

### 5. 🧪 Interactive Test Cases (Prompt Evals)
* Maintain a test suite for each prompt.
* Add multiple test cases with distinct values for your variables.
* Batch execute the entire test suite locally (compiling all outputs) or against live LLMs concurrently to review output consistency.

---

## 🛠️ Architecture

* **Frontend**: React 19 + TypeScript + Vite.
* **Styling**: Vanilla CSS with HSL-based color tokens, dynamic animation frames, and media query breakpoint overlays.
* **API Connectivity**: Client-side direct fetches to Google Generative Language API (using your secure, locally-stored API key).
* **Storage**: LocalStorage browser persistence for raw drafts, configurations, history revisions, template catalogs, and evaluation test cases.

---

## 🚀 Getting Started

### Prerequisites
* Node.js (v18+)
* npm (v9+)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/promptcraft-pro.git
   cd promptcraft-pro
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the local development server:
   ```bash
   npm run dev
   ```

4. Build production assets:
   ```bash
   npm run build
   ```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License
Distributed under the MIT License. See [LICENSE](https://github.com/Hari-bonthu/PromptCrafter/blob/main/file:///LICENSE) for details.
