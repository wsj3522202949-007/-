---
id: tool-04350
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: AI-Generator
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/typoexe/ai-generator
created: 2026-07-18
updated: 2026-07-18
no: 4350
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: typoEXE/AI-Generator
stars: 1
url: https://github.com/typoexe/ai-generator
tier: "B"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 351721b7e2296584
  - methods/模板库.md
---

# typoEXE/AI-Generator

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/typoexe/ai-generator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Generator is an innovative web application designed to leverage OpenAI's API by allowing users to generate custom stories and songs. This dynamic platform combines a React-based frontend with a Python backend, ensuring efficient processing and response to user requests.
- **本地描述**：AI Generator is an innovative web application designed to leverage OpenAI's API by allowing users to generate custom stories and songs. This dynamic platform combines a React-based frontend with a Python backend, ensuring efficient processing and response to user requests.
- **拉取时间**：2026-07-25 17:43:51

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---


# AI Generator

AI Generator is a web application that allows users to create custom stories and songs by custom picked attributes tailored to what they're looking for. This application uses a React-based frontend and a Python (Flask) backend to handle requests and generate stories.

## Features

- Generate stories based on user-input criteria (genre, characters, setting).
- Generate songs based on user-input criteria (style, topic, scene).
- Animations for text display to enhance user experience.
- Responsive design for desktop and mobile users.

## Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

- Node.js
- npm (Node Package Manager)
- Python 3
- pip (Python Package Installer)

### Cloning the Repository

```bash
git clone https://github.com/yourusername/ai-generator.git
cd ai-generator
```

### Setting Up the Frontend

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

### Setting Up the Backend

```bash
# Navigate to the backend directory
cd backend

# Install required Python libraries
pip install -r requirements.txt

# Run the backend server
python app.py
```

## Usage

Once both servers are running, open your web browser and go to `http://localhost:3000` to start generating stories and songs. Select your preferred attributes then click "Generate Story" or "Generate Song" to see your custom story and/or song.

## Contributing

Contributions to the AI Story Generator are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- TypoEXE is the sole developer of this project.
