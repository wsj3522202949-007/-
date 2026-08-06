---
id: tool-07270
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档]
title: book-recommender
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/gitgautamhub/book-recommender
created: 2026-07-18
updated: 2026-07-18
no: 7270
category: 画龙补充 / 扩容入库 — 补充源
repo: gitgautamhub/book-recommender
stars: 0
url: https://github.com/gitgautamhub/book-recommender
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# gitgautamhub/book-recommender

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/gitgautamhub/book-recommender
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：book-recommender
- **拉取时间**：2026-07-25 19:16:09

related:
  - methods/QUICK_START.md
---

# Book Recommender

Book Recommender is a Streamlit web application that helps users find the best book in a specific genre based on their query. The application fetches books from the Google Books API, narrows down the top 10 books by ratings and reviews, and uses a Hugging Face transformer model to find the best match book.

![Book Image](https://github.com/gitgautamhub/book-recommender/blob/main/book.jpg)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GitGautamHub/book-recommender.git
   cd Book-Recommender
   

2. Create a `.env` file in the project root and add your API key:
   ```bash
   GOOGLE_BOOKS_API_KEY=your_api_key_here

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the application:
   ```bash
   streamlit run "BookRecommender.py"

## Usage
- Enter a genre in the input field.
- Enter your specific query.
- Click on the "Find Books" button.
- The application will display the top 100 books, narrow down to the top 10, and finally show the best match book based on your query.
