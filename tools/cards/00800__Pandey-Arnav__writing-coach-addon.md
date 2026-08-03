---
id: tool-00800
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: writing-coach-addon
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pandey-arnav/writing-coach-addon
created: 2026-07-18
updated: 2026-07-18
no: 800
category: 二、网文 / 长篇 AI 写作系统 库
repo: Pandey-Arnav/writing-coach-addon
stars: 0
url: https://github.com/pandey-arnav/writing-coach-addon
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Pandey-Arnav/writing-coach-addon

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pandey-arnav/writing-coach-addon
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Open-source Google Docs add-on that helps improve writing clarity, tone, and style using your own AI API key.
- **本地描述**：Open-source Google Docs add-on that helps improve writing clarity, tone, and style using your own AI API key.
- **拉取时间**：2026-07-23 23:02:21

---

# writing-coach-addon
Open-source Google Docs add-on that helps improve writing clarity, tone, and style using your own AI API key.


# Writing Coach (Google Docs Add-on)

Open-source Google Docs add-on that helps improve writing clarity, tone, and style using your own AI API key.

---

## ✨ Features
- Adds a **Writing Coach** menu in Google Docs (under Extensions).
- Sidebar UI for entering text or using the current selection.
- Custom prompts (e.g., “make this more concise”).
- Secure storage of your API key & backend URL in **User Properties**.
- Inserts AI suggestions directly back into your document.
- 100% open-source — no secrets in code.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🚀 Installation

### Quick Setup (manual copy)
1. Open any Google Doc.
2. Go to **Extensions → Apps Script**.
3. Delete any existing code and copy in:
   - `Code.gs`
   - `Sidebar.html`
   - `Settings.html`
   - `appsscript.json`
4. Save the project.
5. Reload your Doc — you’ll see **Writing Coach** in the menu bar.

### Using `clasp` (Apps Script CLI)
If you want to sync this repo with Google Apps Script:
```bash
npm install -g @google/clasp
clasp login
clasp create --type docs --title "Writing Coach"
clasp push


