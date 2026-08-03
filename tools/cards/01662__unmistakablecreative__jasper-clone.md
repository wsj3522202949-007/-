---
id: tool-01662
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: jasper-clone
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/unmistakablecreative/jasper-clone
created: 2026-07-18
updated: 2026-07-18
no: 1662
category: 二、网文 / 长篇 AI 写作系统 库
repo: unmistakablecreative/jasper-clone
stars: 0
url: https://github.com/unmistakablecreative/jasper-clone
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

# unmistakablecreative/jasper-clone

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/unmistakablecreative/jasper-clone
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Writing Assistant - 20 minute wrapper replacing $49/mo tools for ~$0.002/generation
- **本地描述**：AI Writing Assistant - 20 minute wrapper replacing $49/mo tools for ~$0.002/generation
- **拉取时间**：2026-07-23 23:27:31

---

# Jasper Clone

**AI Writing Assistant** - Built in 20 minutes. Does what $49/mo writing tools do for ~$0.002 per generation.

## Quick Start

```bash
curl -sL https://raw.githubusercontent.com/orchestrate-os/jasper-clone/main/setup.sh | bash
```

That's it. The script will:
1. Ask you to choose Anthropic (Claude) or OpenAI (GPT-4)
2. Open the API key page in your browser
3. Prompt you to paste your key
4. Start the local server
5. Open the interface in your browser

## Manual Setup

```bash
git clone https://github.com/orchestrate-os/jasper-clone.git
cd jasper-clone
python3 -m venv venv
source venv/bin/activate
pip install anthropic  # or: pip install openai
```

Edit `config.json`:
```json
{
    "provider": "anthropic",
    "api_key": "your-key-here"
}
```

Run:
```bash
python3 server.py
```

Open http://localhost:8765

## Templates

- **Blog Post** - Engaging, well-structured blog content
- **Email** - Clear, concise emails that get responses
- **Social Media** - Platform-optimized posts that drive engagement
- **Product Description** - Benefit-focused copy that converts
- **Freestyle** - Write whatever you need

## Cost Comparison

| This Clone | Jasper |
|------------|-----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| ~$0.002 per generation | $49/month |
| Your own API key | Locked to their platform |
| Runs locally | Cloud-dependent |
| 100% open source | Proprietary |

## The Point

This is a wrapper. The entire "product" is:
- A textarea
- A system prompt
- An API call

That's what you're paying $49/month for. Now you know.

## License

MIT - Do whatever you want with this.
