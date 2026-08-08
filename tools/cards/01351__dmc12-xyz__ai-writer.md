---
id: tool-01351
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai-writer
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dmc12-xyz/ai-writer
created: 2026-07-18
updated: 2026-07-18
no: 1351
category: 二、网文 / 长篇 AI 写作系统 库
repo: dmc12-xyz/ai-writer
stars: 9
url: https://github.com/dmc12-xyz/ai-writer
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4fe2ce87710782c7
  - methods/最强写作方法论_全球最强综合版.md
---

# dmc12-xyz/ai-writer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dmc12-xyz/ai-writer
- **Stars**：9
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai-writer, buildspace, buildspace-build, extension, gpt, openai, short-story
- **GitHub 描述**：A short story generator built using open ai apis
- **本地描述**：A short story generator built using open ai apis
- **拉取时间**：2026-07-23 23:18:30

---

<div align="center">
    <h2><samp>AI Writer</samp></h2>
    <samp>short story generator</samp>
    <br/><br/>
    <a href="https://github.com/dmc12-xyz/ai-writer/tree/main/extension" title="download">
      <samp>Get the Extension</samp>
    </a>|
     <a href="https://ai-writer-production.up.railway.app/" title="test">
      <samp>Test it out</samp>
    </a>
</div>

--------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

The tool generates short story based on keywords and phrases provided in the input.

### Details

- Model : text-davinci-003
- Temparature : 0.7
- Max tokens : 250
- Base prompt : "Write me a short story in as much details as possible based on the idea-"

### Steps
1. Get the OpenAI api key 
```
cp .env.example
# set the key 
```

2. Install dependencies and run
```
npm install
npm run dev
```

### Reference

* [Buildspace Project](https://buildspace.so/p/build-ai-writing-assistant-gpt3)
