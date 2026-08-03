---
id: tool-00183
type: tool
area: 库
status: active
tags: [PHP, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: nativephp-ai-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/code-mentor-alt/nativephp-ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 183
category: 二、网文 / 长篇 AI 写作系统 库
repo: code-mentor-alt/nativephp-ai-story-generator
stars: 5
url: https://github.com/code-mentor-alt/nativephp-ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# code-mentor-alt/nativephp-ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/code-mentor-alt/nativephp-ai-story-generator
- **Stars**：5
- **语言**：PHP
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：code-mentor-alt/nativephp-ai-story-generator
- **拉取时间**：2026-07-23 22:44:20

---

# Kids Story Generator - NativePHP iOS App

A Laravel + Inertia application that generates personalized stories for kids, complete with text-to-speech narration. Built as a native iOS application using NativePHP.

> ⚠️ **Important Notice**: This application is currently not functioning within NativePHP iOS due to pending storage system fixes from the NativePHP team. The web version works perfectly, and we'll update this notice once NativePHP resolves the storage system issues.

## Demo

![Demo](/docs/demo.gif)

[View full demo video (With Audio)](docs/demo.mp4)

## Features

- 🎨 Story generation using LLM (powered by Prism)
- 🗣️ Text-to-speech narration using ElevenLabs
- 📱 Native iOS experience with NativePHP
- 🎭 Customizable story elements (animals, emotions, etc.)
- 🔒 User authentication system (It exists through the VueJS Laravel Starterkit but its not being used, you can uncomment out routes in `web.php`)

## Requirements

- PHP 8.2 or higher
- Node.js & NPM
- Composer
- macOS (for iOS development)
- ElevenLabs API key
- Prism API key
- [A NativePHP Mobile license](https://nativephp.com/mobile)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install PHP dependencies:
```bash
composer install
```

3. Install Node.js dependencies:
```bash
npm install
```

4. Create environment file:
```bash
cp .env.example .env
```

5. Generate application key:
```bash
php artisan key:generate
```

6. Configure your database in `.env` file and run migrations:
```bash
php artisan migrate
```

7. Seed the database with basic story elements:
```bash
php artisan db:seed
```

8. To run on NativePHP Check out: [The Native PHP Docs](https://nativephp.com/docs/mobile/1/getting-started/introduction)

## Configuration

### Story Configuration

The application's story generation settings can be configured in `config/story.php`:

- `max_story_length`: Maximum character length for generated stories (default: 100)
- `default_llm_provider`: Default LLM provider (Groq)
- `default_llm_model`: Default model for story generation (deepseek-r1-distill-qwen-32b)
- `eleven_labs_voices`: Configuration for text-to-speech voices
  - `dutch_voice_id`: Dutch voice ID (Dirk - requires Pro subscription)
  - `english_voice_id`: English voice ID (Rachel)
- `eleven_labs_model`: Text-to-speech model version
- `eleven_labs_api_key`: Your ElevenLabs API key (set in .env)

### Environment Variables

Make sure to set the following in your `.env` file:
```
# App Configuration
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

# Database Configuration
DB_CONNECTION=sqlite

# API Keys for LLM and Voice Generation
ELEVEN_LABS_API_KEY=your_elevenlabs_key_here
GROQ_API_KEY=your_groq_key_here

# NativePHP Configuration
NATIVEPHP_AXIOS=false
```

The application requires:
- **Groq API Key**: Used by Prism for LLM story generation with the deepseek-r1-distill-qwen-32b model. Alternatively check out [PrismPHP](https://prismphp.com/getting-started/introduction.html) which allows for more model providers
- **ElevenLabs API Key**: Required for text-to-speech voice generation
- **NativePHP Axios**: Needs to be `true` is trying to run on an iOS device (replaces axios with iOS specific axios for intertia)
- **SQLite Database**: The application uses SQLite by default to allow for on device database

## Development

To start the development server:

```bash
npm run dev
```

For iOS development:

Check out: [The Native PHP Docs](https://nativephp.com/docs/mobile/1/getting-started/introduction)

## Database Seeding

The application comes with basic story elements pre-configured in the database seeder:

- Animal types (Sheep, Turtle)
- Emotion types (Happy, Sad)

You can modify or add more elements in `database/seeders/StoryElementTableSeeder.php`.

## Technologies Used

- Laravel 12
- Inertia.js
- NativePHP
- Prism PHP (for LLM integration)
- ElevenLabs (for text-to-speech)
- TypeScript
- Tailwind CSS

# License

## Sustainable Use License v1.0 (Apache 2.0-Based)

Copyright 2025 - FlowBridgeAI, Inc.

Licensed under the Apache License, Version 2.0 (the "License") with the following **limitations**:

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

### Limitations

- You may use or modify the software only for your own internal business purposes or for non-commercial or personal use.  
- You may distribute the software or provide it to others only if you do so free of charge for non-commercial purposes.  
- You may not alter, remove, or obscure any licensing, copyright, or other notices of the licensor in the software.  
- Any use of the licensor's trademarks is subject to applicable law.
