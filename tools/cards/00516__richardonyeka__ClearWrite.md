---
id: tool-00516
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ClearWrite
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/richardonyeka/clearwrite
created: 2026-07-18
updated: 2026-07-18
no: 516
category: 二、网文 / 长篇 AI 写作系统 库
repo: richardonyeka/ClearWrite
stars: 3
url: https://github.com/richardonyeka/clearwrite
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 391ff04657d706eb
  - methods/最强写作方法论_全球最强综合版.md
---

# richardonyeka/ClearWrite

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/richardonyeka/clearwrite
- **Stars**：3
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ClearWrite is a LLM prompt designed to help writer's improve the clarity,precision,and confidence of their writing using ai.
- **本地描述**：ClearWrite is a LLM prompt designed to help writer's improve the clarity,precision,and confidence of their writing using ai.
- **拉取时间**：2026-07-23 22:54:05

---

# ClearWrite
ClearWrite is a LLM prompt designed to help writer's improve the clarity,precision,and confidence of their writing using ai.

## Overview

This repository provides a straightforward prompt for reviewing blog posts using AI. The goal is to enhance the clarity and authority of your writing by identifying common issues such as unqualified conditionals, weak assertions, and unquantified comparisons.

## Usage Instructions

To use the blog post review prompt, follow these simple steps:

1. **Copy the Prompt**: Use the following prompt to guide your review:

   ```
   Please review the following blog post and identify any of the following issues:
   1. *Unqualified Conditionals* – Look for words like "may," "could," "might," "possibly," etc., and check if the conditions under which these events occur are clearly specified. Replace vague language with more precise statements.
   2. *Weak Assertions / Passive Voice* – Look for phrases like "there is no way" or "this API can be called." Replace these with stronger, more assertive statements (e.g., "it is impossible" or "[specific entity] can call this API"). Ensure the language is confident and direct.
   3. *Unquantified Comparisons* – Identify comparisons that lack specifics (e.g., "more efficient," "better," "faster"). Ensure comparisons are backed by measurable data (e.g., "X is 30% faster in terms of CPU usage" or "Y is more secure against SQL injection attacks"). If a comparison is subjective, it should be clearly labeled as such.

   [Your blog post text goes here.]
   ```

2. **Paste Your Blog Post**: Replace `[Your blog post text goes here.]` with the actual text of your blog post.

3. **Use Your LLM of Choice**: Paste the completed prompt into your preferred language model (LLM), such as GPT, to receive feedback and suggestions for improvement.

## Example

Here’s an example of how to format your input:

```
Please review the following blog post and identify any of the following issues:
1. *Unqualified Conditionals* – Look for words like "may," "could," "might," "possibly," etc., and check if the conditions under which these events occur are clearly specified. Replace vague language with more precise statements.
2. *Weak Assertions / Passive Voice* – Look for phrases like "there is no way" or "this API can be called." Replace these with stronger, more assertive statements (e.g., "it is impossible" or "[specific entity] can call this API"). Ensure the language is confident and direct.
3. *Unquantified Comparisons* – Identify comparisons that lack specifics (e.g., "more efficient," "better," "faster"). Ensure comparisons are backed by measurable data (e.g., "X is 30% faster in terms of CPU usage" or "Y is more secure against SQL injection attacks"). If a comparison is subjective, it should be clearly labeled as such.

[Your blog post text goes here.]
```

## Contributing

Contributions to improve the prompt or add new features are welcome! Please submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Feel free to reach out if you have any questions or need further assistance. Happy writing!
