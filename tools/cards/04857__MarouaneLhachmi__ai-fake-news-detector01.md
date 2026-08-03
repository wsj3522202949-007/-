---
id: tool-04857
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-fake-news-detector01
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/marouanelhachmi/ai-fake-news-detector01
created: 2026-07-18
updated: 2026-07-18
no: 4857
category: 一、去 AI 味 / Humanizer 库
repo: MarouaneLhachmi/ai-fake-news-detector01
stars: 0
url: https://github.com/marouanelhachmi/ai-fake-news-detector01
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MarouaneLhachmi/ai-fake-news-detector01

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/marouanelhachmi/ai-fake-news-detector01
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered full-stack web app to detect fake news from images, URLs, and text using GPT-4o. Built with Next.js, MongoDB & NextAuth.
- **本地描述**：AI-powered full-stack web app to detect fake news from images, URLs, and text using GPT-4o. Built with Next.js, MongoDB & NextAuth.
- **拉取时间**：2026-07-25 17:57:02

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Fake News Detector

An intelligent, full-stack web application designed to combat misinformation by analyzing news content from various sources using artificial intelligence. This project provides users with detailed insights into the authenticity, bias, and tone of news articles, images, and URLs.

## Key Features

-   **Multi-Source Analysis**: Analyze news by pasting article text, uploading a screenshot, or providing a URL.
-   **Advanced AI Reporting**: Receive a comprehensive analysis report that includes:
    -   A **Confidence Score** indicating if the content is likely authentic or fake.
    -   Detection of **Political Bias** and **Emotional Tone**.
    -   Identification of potential **Logical Fallacies**.
-   **Source Verification**: Integrated with the Google Custom Search API to find and display relevant fact-checking sources.
-   **User Authentication**: Secure user sign-up and login using credentials, Google, or GitHub, powered by NextAuth.js.
-   **Live News Feed**: A real-time feed of global headlines from GNews, with an on-demand analysis feature to save API costs.
-   **Interactive News Quiz**: An AI-generated "Fact or Fiction" quiz to help users sharpen their critical thinking skills.
-   **Personal User Dashboard**: Each user has a personal dashboard to view their analysis history and track their statistics, including an activity heatmap.
-   **Full-Fledged Admin Dashboard**:
    -   Platform-wide statistics and data visualizations.
    -   A complete user management system with search, pagination, and actions to delete or promote/demote users.
    -   A "User Feedback" review panel to monitor user opinions on AI analysis quality.

## Tech Stack

-   **Framework**: [Next.js](https://nextjs.org/)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/)
-   **Authentication**: [NextAuth.js](https://next-auth.js.org/)
-   **Database**: [MongoDB](https://www.mongodb.com/) (with MongoDB Atlas)
-   **AI Analysis**: [Azure AI Services](https://azure.microsoft.com/en-us/solutions/ai/)
-   **External APIs**: Google Custom Search API, GNews API

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   [Node.js](https://nodejs.org/en/) (v18 or later recommended)
-   [npm](https://www.npmjs.com/)
-   Access to a MongoDB database (e.g., a free cluster on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register))

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-fake-news-detector.git](https://github.com/your-username/ai-fake-news-detector.git)
    cd ai-fake-news-detector
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Set up environment variables:**
    Create a new file named `.env.local` in the root of your project and add the following variables.

    ```env
    # MongoDB
    MONGODB_URI="your_mongodb_connection_string"

    # NextAuth
    NEXTAUTH_SECRET="generate_a_random_secret_string"
    NEXTAUTH_URL="http://localhost:3000"

    # NextAuth Providers
    GOOGLE_CLIENT_ID="your_google_client_id"
    GOOGLE_CLIENT_SECRET="your_google_client_secret"
    GITHUB_CLIENT_ID="your_github_client_id"
    GITHUB_CLIENT_SECRET="your_github_client_secret"

    # External APIs
    API_KEY="your_azure_ai_api_key"
    API_ENDPOINT="your_azure_ai_endpoint"
    GNEWS_API_KEY="your_gnews_api_key"
    GOOGLE_API_KEY="your_Google Search_api_key"
    GOOGLE_CSE_ID="your_google_custom_search_engine_id"
    ```

4.  **Run the development server:**
    ```bash
    npm run dev
    ```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

<!-- Updated June 2026 -->
