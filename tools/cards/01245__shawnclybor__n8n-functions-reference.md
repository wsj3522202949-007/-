---
id: tool-01245
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: n8n-functions-reference
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shawnclybor/n8n-functions-reference
created: 2026-07-18
updated: 2026-07-18
no: 1245
category: 二、网文 / 长篇 AI 写作系统 库
repo: shawnclybor/n8n-functions-reference
stars: 5
url: https://github.com/shawnclybor/n8n-functions-reference
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 34850bcdcac82501
  - methods/最强写作方法论_全球最强综合版.md
---

# shawnclybor/n8n-functions-reference

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shawnclybor/n8n-functions-reference
- **Stars**：5
- **语言**：None
- **License**：CC0-1.0
- **Topics**：—
- **GitHub 描述**：This repository provides a structured reference for writing JavaScript functions in n8n Code nodes. It includes built-in variables, data structures, item linking strategies, working with binary data, debugging tips, and performance optimizations for efficient workflow automation.
- **本地描述**：This repository provides a structured reference for writing JavaScript functions in n8n Code nodes. It includes built-in variables, data structures, item linking strategies, working with binary data, debugging tips, and performance optimizations for efficient workflow automation.
- **拉取时间**：2026-07-23 23:15:24

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**n8n Code Node Reference & AI-Assisted Function Writing Guide**

Overview

This repository provides a comprehensive reference for writing JavaScript functions in n8n Code nodes. It includes:
	•	A breakdown of built-in variables available in n8n.
	•	Best practices for data transformations and manipulations within workflows.
	•	Guidance on handling JSON and binary data in n8n.
	•	Debugging strategies to troubleshoot errors efficiently.
	•	Performance optimizations to ensure smooth execution of functions.

This reference is designed for both beginners and experienced users looking to streamline their n8n automation workflows by leveraging custom JavaScript functions.

How to Use This File

Option 1: AI-Assisted Function Writing (Recommended)

Leverage an LLM (Large Language Model) such as ChatGPT or Claude to assist with writing your n8n functions:
	1.	Upload this file to ChatGPT or another LLM.
	2.	Describe your use case in detail.
	•	Include your node’s input data.
	•	Describe the expected output in detail.
	•	(Optional but highly recommended) Provide a sample expected output to guide the AI.
	3.	Ask the LLM to generate a JavaScript function based on your requirements.
	4.	Copy the generated function into your n8n Code node and run a test.
	5.	If an error occurs, copy the error message back into the LLM and ask it to debug the function.
	6.	Iterate until the function executes successfully.

This method allows for rapid function prototyping and error resolution.

Option 2: Using the Cline Extension with VS Code

For users who prefer a more dynamic code-writing experience, you can use this file with VS Code and the Cline extension.

Steps to Use Cline for n8n Code Writing:
	1.	Install the Cline extension in VS Code.
	2.	Open this file in VS Code as a reference.
	3.	Use Cline to interact with an AI model directly inside VS Code.
	4.	Write and refine your n8n JavaScript functions dynamically.
	5.	Test your functions in n8n, iterating as needed.

This approach allows for faster testing and refining, minimizing back-and-forth copy-pasting between applications.

Troubleshooting & Debugging

If your function throws an error:
	•	Copy the error message and paste it into ChatGPT (or another LLM).
	•	Ask it to analyze and fix the issue.
	•	Test the revised function and repeat if needed.

Common debugging strategies include:
✅ Checking input data structure.
✅ Handling undefined values properly.
✅ Using console.log() for in-node debugging.
✅ Validating JSON parsing and array manipulations.
✅ Ensuring proper item linking within the workflow.

For common error fixes and performance optimization tips, refer to the “Best Practices & Debugging” section in this document.

Why Use This File?
	•	✅ Saves Time – No need to manually look up n8n’s documentation every time.
	•	✅ AI-Assisted Coding – Quickly generate, debug, and optimize functions with LLMs.
	•	✅ Flexible Workflow – Use in ChatGPT, VS Code, or directly in n8n.
	•	✅ Improves Automation – Helps refine complex data transformations and API handling.

Contributing

If you have improvements or additional insights:
	1.	Fork the repository.
	2.	Make changes and submit a PR.
	3.	Share useful AI-generated function examples to improve this reference.

License

This reference is open-source and can be freely used, modified, and shared.

Let me know if you’d like any tweaks!
