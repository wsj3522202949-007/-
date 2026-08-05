---
id: tool-05565
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-threat-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/miki42v/ai-threat-detector
created: 2026-07-18
updated: 2026-07-18
no: 5565
category: 一、去 AI 味 / Humanizer 库
repo: miki42v/ai-threat-detector
stars: 1
url: https://github.com/miki42v/ai-threat-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# miki42v/ai-threat-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/miki42v/ai-threat-detector
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A web application that uses AI to detect threats in text, files, and URLs.
- **本地描述**：A web application that uses AI to detect threats in text, files, and URLs.
- **拉取时间**：2026-07-25 18:23:24

---

# 🤖 AI-Powered Threat Detector

A full-stack web application that leverages NVIDIA's advanced AI model (Llama 3.3 Nemotron Super 49B) to analyze text, files, and URLs for potential security threats in real-time. This tool provides a user-friendly, streaming interface to get instant, comprehensive AI-driven security analysis with proper markdown formatting.

### 🔗 **[Click Here for the Live Demo](https://ai-threat-detector-three.vercel.app/)**

> **Note:** Live demo may take 30 seconds to wake up on first request (Render free tier limitation). For deployment instructions, see `[DEPLOYMENT.md](DEPLOYMENT.md)`.

![Screenshot of the AI Threat Detector Application](https://user-images.githubusercontent.com/10284367/223212870-272a11b6-7d1c-43f0-8e7c-501f6f874d1a.png)
*(**Note:** To replace this placeholder image, simply take a screenshot of your app, upload the image file to your GitHub repository, and replace the link above with the new image's URL.)*

---

## ✨ Core Features

- **Real-Time Streaming Analysis:** Get instant, word-by-word feedback from the AI with intelligent filtering of reasoning processes for clean, professional output.
- **Multi-Faceted Input Methods:**
  - **Text Analysis:** Paste any code snippet, log file, email body, or suspicious text directly into the application.
  - **File Upload:** Upload local files (`.js`, `.py`, `.log`, `.txt`, `.html`, `.css`, `.md`, etc.) for an in-depth analysis of their contents.
  - **Live URL Scanning:** Enter any URL to have the backend fetch its live HTML content and scan it for malicious scripts, phishing indicators, XSS, CSRF, and other threats.
- **Comprehensive Security Analysis:** Identifies multiple threat categories including XSS, CSRF, SQL Injection, API exposure, CORS misconfigurations, authentication issues, and more.
- **Beautiful Markdown Output:** AI responses are formatted with proper headings, bold text, code blocks, and lists for easy readability.
- **Secure Proxy Architecture:** The Node.js backend acts as a secure intermediary, managing the NVIDIA API key and ensuring it is never exposed to the user's browser.
- **Modern & Responsive UI:** Built with React and Tailwind CSS with custom scrollable markdown containers and syntax highlighting.

---

## 🛠️ Technology Stack & Architecture

This project is a full-stack application with a clear separation of concerns between the client, server, and the external AI service, creating a robust and scalable system.

- **Frontend (Client):**
  - **Framework:** React.js
  - **Styling:** Tailwind CSS
  - **HTTP Client:** `axios` (for simple requests) & the browser's native `fetch` API (for handling streams).
  - **Markdown Rendering:** `react-markdown` to beautifully render the AI's formatted responses.

- **Backend (Server):**
  - **Runtime:** Node.js
  - **Framework:** Express.js for creating the API endpoints and handling routing.
  - **Security:** `dotenv` for managing environment variables and `cors` for secure cross-origin communication.

- **AI Service:**
  - **Provider:** NVIDIA Integrate API
  - **Model:** `nvidia/llama-3.3-nemotron-super-49b-v1.5` - An advanced model optimized for comprehensive security analysis
  - **Features:** 8192 max tokens, streaming responses, intelligent reasoning process filtering

- **Deployment:**
  - **Frontend:** Deployed on **Vercel**, configured for continuous integration from the `client` directory.
  - **Backend:** Deployed on **Render**, configured for continuous integration from the `server` directory.

---

## 🚀 Getting Started Locally

### Recent Updates & Improvements

**Latest Version (v2.0)** includes:
- ✅ Upgraded to NVIDIA Llama 3.3 Nemotron Super 49B v1.5
- ✅ Intelligent `<think>` tag filtering - hides AI reasoning for cleaner output
- ✅ Enhanced markdown formatting with custom styling
- ✅ Increased token limit (1024 → 8192) for comprehensive analysis
- ✅ Fixed buffer management for complete responses without truncation
- ✅ Improved system prompt for better structured threat analysis
- ✅ Enhanced CSS with scrollable containers and syntax highlighting
- ✅ Added debugging and stream completion logging

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or later recommended)
- [Git](https://git-scm.com/)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/miki42v/ai-threat-detector.git
   cd ai-threat-detector
   ```

2. **Set up the Backend (Server):**
   ```bash
   cd server
   npm install
   ```

3. **Configure Environment Variables:**
   - Create a `.env` file in the `server` directory:
     ```bash
     echo "NVIDIA_API_KEY=your-api-key-here" > .env
     ```
   - Get your NVIDIA API key from [https://build.nvidia.com/](https://build.nvidia.com/)

4. **Set up the Frontend (Client):**
   ```bash
   cd ../client
   npm install
   ```

5. **Configure Client Environment:**
   - Create a `.env` file in the `client` directory (for local development):
     ```bash
     echo "REACT_APP_API_URL=http://localhost:5001" > .env
     ```

### Running the Application

1. **Start the Backend Server:**
   ```bash
   cd server
   node server.js
   ```
   Server will run on `http://localhost:5001`

2. **Start the Frontend (in a new terminal):**
   ```bash
   cd client
   npm start
   ```
   Frontend will run on `http://localhost:3000`

3. **Open your browser** and navigate to `http://localhost:3000`

---

## 🌐 Deployment

For detailed deployment instructions to production (Vercel + Render), see `[DEPLOYMENT.md](DEPLOYMENT.md)`.

**Quick Summary:**
- **Backend**: Deploy to Render with `NVIDIA_API_KEY` environment variable
- **Frontend**: Deploy to Vercel with `REACT_APP_API_URL` pointing to your Render backend

---

## 🔒 Security Notes

- ⚠️ **Never commit your `.env` files** - they contain sensitive API keys
- ✅ Both `server/.env` and `client/.env` are already in `.gitignore`
- ✅ API key is only used server-side and never exposed to the browser
- ✅ CORS is configured to allow cross-origin requests
- 🔄 **Rotate your API key** if it's ever accidentally exposed

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **NVIDIA** for providing the powerful AI models through their Integrate API
- **React** and **Tailwind CSS** for the frontend framework and styling
- **Express.js** for the backend framework
- The open-source community for continuous inspiration and support

---

## 📧 Contact

Project Link: [https://github.com/miki42v/ai-threat-detector](https://github.com/miki42v/ai-threat-detector)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**⭐ If you find this project useful, please consider giving it a star!**
