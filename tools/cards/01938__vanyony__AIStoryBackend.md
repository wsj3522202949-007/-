---
id: tool-01938
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AIStoryBackend
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/vanyony/aistorybackend
created: 2026-07-18
updated: 2026-07-18
no: 1938
category: 二、网文 / 长篇 AI 写作系统 库
repo: vanyony/AIStoryBackend
stars: 0
url: https://github.com/vanyony/aistorybackend
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# vanyony/AIStoryBackend

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/vanyony/aistorybackend
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Story Generator Backend
- **本地描述**：AI Story Generator Backend
- **拉取时间**：2026-07-23 23:35:29

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AIStoryBackend
AI Story Generator Backend
[package.json](https://github.com/user-attachments/files/23689276/package.json)
{
  "name": "aistorybackend",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "module",
  "dependencies": {
    "axios": "^1.13.2",
    "cors": "^2.8.5",
    "express": "^5.1.0"
  }
}
[server.js](https://github.com/user-attachments/files/23689297/server.js)
import express from "express";
import axios from "axios";
import cors from "cors";

const app = express();
app.use(express.json());
app.use(cors()); // 允许小程序访问

app.post("/api/ai", async (req, res) => {
  const { text } = req.body;

  try {
    const aiRes = await axios.post(
      "https://api.deepseek.com/v1/chat/completions",
      {
        model: "deepseek-chat",
        messages: [
          { role: "system", content: "你是一个故事续写助手，请简洁、有创意地续写用户输入。" },
          { role: "user", content: text }
        ]
      },
      {
        headers: { Authorization: `Bearer ${process.env.DEEPSEEK_API_KEY}` }     
      }
    );

    res.json({
      reply: aiRes.data.choices[0].message.content
    });

  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "AI请求失败" });
  }
});

const PORT = 3000;
app.listen(PORT, () => console.log(`🚀 后端运行在 http://localhost:${PORT}`));
