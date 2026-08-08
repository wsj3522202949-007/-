---
id: tool-01721
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: aws-serverless-ai-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/victoralin10/aws-serverless-ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1721
category: 二、网文 / 长篇 AI 写作系统 库
repo: Victoralin10/aws-serverless-ai-story-generator
stars: 1
url: https://github.com/victoralin10/aws-serverless-ai-story-generator
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
content_hash: 33f6675372af42ad
  - methods/最强写作方法论_全球最强综合版.md
---

# Victoralin10/aws-serverless-ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/victoralin10/aws-serverless-ai-story-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Victoralin10/aws-serverless-ai-story-generator
- **拉取时间**：2026-07-23 23:29:12

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


# Implementando una aplicación de generación de historias serverless, basada en eventos con ChatGPT

Inspirado en https://aws.amazon.com/pt/blogs/compute/implementing-an-event-driven-serverless-story-generation-application-with-chatgpt-and-dall-e/


## Prerequisitos

1. NodeJS 16 o superior

2. Docker

3. AWS CDK: `npm install -g aws-cdk`

4. AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

5. Configurar AWS CLI: `aws configure`

6. OpenAI ApiKey: https://platform.openai.com/account/


## Pasos para desplegar

1. Clonar este repositorio

2. Ejecutar: `npm run install:all`

3. Compilar frontend: `npm run frontend:build`

4. Crear archivo de configuracion a partir de config.json.example: `cp config.json.example config.json`

5. Inicializar cdk: `npm run bootstrap`

5. Desplegar: `npm run deploy`

7. Guarda la api key de openai en el secret creado en secretsmanager.

8. Eliminar: `npm run destroy`
