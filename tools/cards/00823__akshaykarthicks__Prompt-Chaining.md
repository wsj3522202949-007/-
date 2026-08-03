---
id: tool-00823
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 本地写作]
title: Prompt-Chaining
summary: 搭大纲/分卷/节拍
source: https://github.com/akshaykarthicks/prompt-chaining
created: 2026-07-18
updated: 2026-07-18
no: 823
category: 二、网文 / 长篇 AI 写作系统 库
repo: akshaykarthicks/Prompt-Chaining
stars: 1
url: https://github.com/akshaykarthicks/prompt-chaining
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# akshaykarthicks/Prompt-Chaining

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/akshaykarthicks/prompt-chaining
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：This workflow demonstrates **AI prompt chaining** in **n8n**, generating a high-quality blog post from a single input topic. It chains multiple LLM steps—outline generation, evaluation, full blog writing—and posts the final result to **Google Docs**.
- **本地描述**：This workflow demonstrates **AI prompt chaining** in **n8n**, generating a high-quality blog post from a single input topic. It chains multiple LLM steps—outline generation, evaluation, full blog writing—and posts the final result to **Google Docs**.
- **拉取时间**：2026-07-23 23:03:02

---

# 🧠 Prompt Chaining Blog Generator – n8n Workflow

This workflow demonstrates **AI prompt chaining** in **n8n**, generating a high-quality blog post from a single input topic. It chains multiple LLM steps—outline generation, evaluation, full blog writing—and posts the final result to **Google Docs**.



![image](https://github.com/user-attachments/assets/3c98ae0b-4d18-44dd-8ecd-35b60b986a5b)


---

## 📌 Features

- 📥 Accepts topic input via chat trigger
- ✍️ Generates a structured blog outline
- ✅ Evaluates and improves the outline
- 📝 Expands the refined outline into a full blog post
- 📄 Publishes to Google Docs
- 🤖 Uses the following LLMs via **OpenRouter**:
  - 🧠 **GPT-4o-mini (OpenRouter)** – Outline evaluation
  - 🧠 **GPT-4o-mini (OpenRouter)** – Blog content generation

---

## 🧩 Workflow Structure

| Step | Node Name                 | Purpose |
|------|---------------------------|---------|
| 1    | `When chat message received` | Triggered when user sends a blog topic |
| 2    | `Outline Writer`          | Creates a blog outline based on the input |
| 3    | `Outline Evaluation`      | Uses GPT-4o-mini to enhance the outline |
| 4    | `Blog Writer`             | Expands the final outline into a full blog post |
| 5    | `Post to Docs`            | Saves the generated blog to Google Docs |
| 6    | `4o mini`                 | Powers outline evaluation via OpenRouter |
| 7    | `4o mini (again)`         | Powers blog writing via OpenRouter |

---

## 🔧 Requirements

- Running instance of **n8n**
- Credentials/API keys set up for:
  - 🧠 **OpenRouter** (for GPT-4o-mini)
  - 📄 **Google Docs OAuth2**

---

## 🚀 How to Run

1. **Import** the JSON workflow into your n8n instance.
2. **Configure Credentials** for:
   - **OpenRouter** (GPT-4o-mini)
   - **Google Docs**
3. **Activate the workflow**.
4. Send a topic to the webhook/chat endpoint (e.g., “The future of AI in healthcare”).
5. The nodes will run as follows:
   - Topic → Outline → Evaluation → Blog → Google Docs

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🧪 Example Input

```json
{
  "chatInput": "How AI is transforming personal finance management"
}
