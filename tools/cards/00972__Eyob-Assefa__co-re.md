---
id: tool-00972
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: co-re
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/eyob-assefa/co-re
created: 2026-07-18
updated: 2026-07-18
no: 972
category: 二、网文 / 长篇 AI 写作系统 库
repo: Eyob-Assefa/co-re
stars: 0
url: https://github.com/eyob-assefa/co-re
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
content_hash: 28517db50aae6f00
  - methods/最强写作方法论_全球最强综合版.md
---

# Eyob-Assefa/co-re

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/eyob-assefa/co-re
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：co-re (Co-writer / Rewrite) - writing assistant tool. 
- **本地描述**：co-re (Co-writer / Rewrite) - writing assistant tool.
- **拉取时间**：2026-07-23 23:07:23

---

# Co-Re: Writing Assistant

**co-re** (Co-writer / Rewrite) is a web application that helps you improve your writing.
User type their text on the left, and the AI gives better version on the right. It highlights changes, scores the draft, and automatically saves new vocabularies.


## Necessary tools
* **Python**
* **Node.js** and **npm**
* An **OpenAI API Key**

## How to Set Up and Run

You need to run two parts: the backend (Python) and the frontend (React). You will need two terminal windows open.

### Step 1: Start the Backend (Terminal 1)

1. Open a terminal and go to the backend folder:
```bash
cd backend

```
2. Create and start a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

3. Install the required tools:
```bash
pip install -r requirements.txt
```

4. Add your API key:
* Create a file named `.env` inside the `backend` folder.
* Add this line to the file: `OPENAI_API_KEY=your-actual-api-key`


5. Run the server:
```bash
uvicorn server:app --reload

```

*Leave this terminal window running.*

### Step 2: Start the Frontend (Terminal 2)

The frontend is the web page you interact with.

1. Open a new terminal and go to the frontend folder:
```bash
cd frontend

```

2. Install the React packages:
```bash
npm install

```

3. Start the website:
```bash
npm run dev

```

*Leave this terminal window running.*

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## How to Use

1. Open your web browser and go to the link shown in Terminal 2 (usually `http://localhost:5173`).
2. Type or paste a draft into the left panel.
3. Click **Improve Writing**.
4. Read your new text and check your score on the right.
5. Click **My Vocabulary** at the top to see the words along with their definition.
