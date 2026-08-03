---
id: tool-01044
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-telegram-content-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tequilaphazzz/ai-telegram-content-generator
created: 2026-07-18
updated: 2026-07-18
no: 1044
category: 二、网文 / 长篇 AI 写作系统 库
repo: Tequilaphazzz/ai-telegram-content-generator
stars: 1
url: https://github.com/tequilaphazzz/ai-telegram-content-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Tequilaphazzz/ai-telegram-content-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tequilaphazzz/ai-telegram-content-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project is a self-hosted Flask web app that uses AI (GPT and DALL-E) to automatically generate, review, and publish a complete content package — consisting of a post, image, and story — directly to a Telegram channel from a single topic.
- **本地描述**：This project is a self-hosted Flask web app that uses AI (GPT and DALL-E) to automatically generate, review, and publish a complete content package — consisting of a post, image, and story — directly to a Telegram channel from a single topic.
- **拉取时间**：2026-07-23 23:09:27

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🤖 AI Telegram Content Generator

This project is a demonstrational but powerful, self-hosted web application designed to streamline and automate content creation for Telegram channels.

It takes a simple topic from you and uses AI (GPT-4o-mini and DALL-E 3) to generate a complete content package: a well-written post, a relevant image, and a matching, properly-formatted story. You get to review and approve each piece in a simple web interface before publishing it directly to your channel with a single click.

## 🚀 Key Features

  * **Interactive Web UI**: A simple, step-by-step web interface built with Flask lets you control the entire content creation process.
  * **🤖 AI Text Generation**: Uses `gpt-4o-mini` to create engaging, humorous, and well-structured Telegram posts from a single topic prompt.
  * **🎨 AI Image Generation**: Automatically generates a creative prompt from the post text and uses `dall-e-3` to create a high-definition, photorealistic image to accompany the post.
  * **📱 Automated Story Creation**: Generates a short, catchy headline for a Telegram Story. It then automatically crops the post image into a 9:16 aspect ratio and overlays the headline using the Pillow library.
  * **✈️ Direct Telegram Publishing**: Once you approve all content, the app publishes the post (text + image) and the story directly to your specified Telegram channel using the Telethon API.
  * **🔄 Iterative Control**: Not satisfied with the first draft? You can regenerate the text, image, or story headline at each step until it's perfect.

## 🛠️ Technology Stack

  * **Backend**: **Flask** (for the web app and workflow management)
  * **AI (Text)**: **OpenAI API** (`gpt-4o-mini` for post text, image prompts, and story headlines)
  * **AI (Image)**: **OpenAI API** (`dall-e-3` for post image generation)
  * **Image Processing**: **Pillow (PIL)** (for cropping and adding text to images)
  * **Telegram API**: **Telethon** (for asynchronously publishing content)
  * **Configuration**: **python-dotenv** (for managing API keys and secrets)
  * **Frontend**: Basic **HTML/CSS** (via Jinja2 template)

## 🌊 How it Works (Overview)

The application flow is managed by a Flask-based web server and broken into clear steps:

1.  **Topic Submission**: The user enters a topic (e.g., "Why cats are good programmers") into the web UI.
2.  **Text Generation**: `app.py` triggers `content_generator.py`, which queries the **OpenAI API (GPT-4o-mini)** to generate a full post text. This text is displayed to the user for approval.
3.  **Image Generation**: Once the user approves the text, the app sends the post text to **GPT-4o-mini** to create a detailed *image prompt*. This prompt is then sent to the **DALL-E 3 API**, which returns a URL for a generated image. The app downloads this image and saves it locally, displaying it for approval.
4.  **Story Generation**: Upon image approval, the app again queries **GPT-4o-mini** for a short (max 5 words) story headline. The `Pillow` library is then used to open the post image, crop it to a 9:16 story format, and draw the new headline onto it. This new story image is saved and displayed.
5.  **Final Approval**: The user reviews the post text, post image, and story image one last time.
6.  **Publishing**: When the user clicks "Publish," the app calls an asynchronous `Telethon` function. This function logs in using your bot token and sends the post (image + caption) and the story (as a separate story file) to the Telegram channel ID you specified in your configuration.

## 📁 Project Structure

```
.
├── app.py                  # Main Flask application, handles web routes and session logic
├── content_generator.py    # Core module: all AI generation, image processing, and Telegram publishing
├── requirements.txt        # Python dependencies
├── .env                    # (You must create this) Stores all your API keys
│
├── static/
│   ├── fonts/
│   │   └── arial.ttf       # Font file used for the story headline
│   └── generated/          # (Auto-created) Stores downloaded post images and generated story images
│
└── templates/
    └── index.html          # The single HTML/Jinja2 template for the web interface
```

## ⚙️ Setup and Usage Instructions

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-tg-content-gen.git
cd gemini-tg-content-gen
```

### 2\. Create a Virtual Environment & Install Dependencies

It's highly recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate
# (Windows)
# venv\Scripts\activate

# Install all required packages
pip install -r requirements.txt
```

### 3\. Configure Your Environment (`.env`)

This is the most important step. Create a file named `.env` in the root of the project directory and add your API keys.

**You will need:**

  * **Flask Secret Key**: A random string for session security. You can generate one using `python -c 'import os; print(os.urandom(24).hex())'`.
  * **OpenAI API Key**: Your key from [platform.openai.com](https://platform.openai.com/).
  * **Telegram API ID & Hash**: Get these from [my.telegram.org](https://my.telegram.org) by creating a new "app".
  * **Telegram Bot Token**: Get this from **@BotFather** on Telegram.
  * **Telegram Channel ID**: The ID of the channel you want to post to (e.g., `-100123456789`). Your bot must be an admin in this channel with permission to post.

<!-- end list -->

```ini
# .env file

# Flask
FLASK_SECRET_KEY="your_super_secret_random_string_here"

# OpenAI
OPENAI_API_KEY="sk-..."

# Telegram
TELEGRAM_API_ID="1234567"
TELEGRAM_API_HASH="your_api_hash_here"
TELEGRAM_BOT_TOKEN="1234567890:ABC..."
TELEGRAM_CHANNEL_ID="-100123456789"
```

### 4\. Run the Application

```bash
python app.py
```

The server will start (usually in debug mode).

### 5\. Use the Web Interface

Open your web browser and go to: **`http://127.0.0.1:5000`**

You will be guided through the content generation process:

1.  Enter your topic and click **Сгенерировать\!** (Generate\!).
2.  Approve the text or regenerate it.
3.  Approve the image or regenerate it.
4.  Approve the story/headline or regenerate it.
5.  Click the final **ОПУБЛИКОВАТЬ В TELEGRAM** (PUBLISH TO TELEGRAM) button.

Your new post and story will appear in your channel\!
