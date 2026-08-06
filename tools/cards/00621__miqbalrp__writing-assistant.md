---
id: tool-00621
type: tool
area: 库
status: active
tags: [校对, Python, 协议宽松, 需API密钥, 英文文档, 改稿润色]
title: writing-assistant
summary: 错别字/语法/风格校对
source: https://github.com/miqbalrp/writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 621
category: 二、网文 / 长篇 AI 写作系统 库
repo: miqbalrp/writing-assistant
stars: 0
url: https://github.com/miqbalrp/writing-assistant
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# miqbalrp/writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/miqbalrp/writing-assistant
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A streamlined writing enhancement tool that helps improve your text with grammar corrections, clarity improvements, and tone adjustments.
- **本地描述**：A streamlined writing enhancement tool that helps improve your text with grammar corrections, clarity improvements, and tone adjustments.
- **拉取时间**：2026-07-23 22:57:11

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Writing Assistant 📝

A streamlined writing enhancement tool that helps improve your text with grammar corrections, clarity improvements, and tone adjustments.

## Features ✨

- **Grammar Correction**: Fixes spelling, punctuation, and grammatical errors
- **Clarity Enhancement**: Makes text more concise and easier to understand
- **Tone Adjustment**: Adapts writing style to match desired tone (formal, casual, professional, etc.)
- **Real-time Preview**: See changes with color-coded differences
- **Educational Feedback**: Learn from detailed suggestions and improvements

## Getting Started 🚀

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for AI functionality)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/writing-assistant.git
cd writing-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### Running the App

Launch the application using Streamlit:
```bash
streamlit run app.py
```

## Usage 💡

1. Select the improvements you want to apply:
   - Grammar fixing
   - Clarity improvement
   - Tone adjustment

2. If tone adjustment is selected, choose your desired tone:
   - Formal
   - Casual
   - Professional
   - Friendly
   - Technical
   - Simple

3. Enter or paste your text
4. Click "✨ Improve Writing"
5. Review the improvements:
   - Original vs. improved text
   - Detailed changes with color coding
   - Learning points and suggestions

## Project Structure 📁

```
writing-assistant/
├── app.py           # Main application file
├── agents.py        # AI agents implementation
├── requirements.txt # Project dependencies
└── .env            # Environment variables (not in repo)
```

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/miqbalrp/writing-assistant/blob/main/link-to-issues).

## License 📄

This project is licensed under the MIT License - see the [LICENSE](https://github.com/miqbalrp/writing-assistant/blob/main/LICENSE) file for details.
