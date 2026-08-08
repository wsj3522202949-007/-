---
id: tool-01521
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: writing-assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nathanstrauss13/writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1521
category: 二、网文 / 长篇 AI 写作系统 库
repo: nathanstrauss13/writing-assistant
stars: 0
url: https://github.com/nathanstrauss13/writing-assistant
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
content_hash: 04a87b0db73354a3
  - methods/最强写作方法论_全球最强综合版.md
---

# nathanstrauss13/writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nathanstrauss13/writing-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A companion app to the media analysis tool that assists with writing for communications professionals
- **本地描述**：A companion app to the media analysis tool that assists with writing for communications professionals
- **拉取时间**：2026-07-23 23:23:27

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Writing Assistant

A companion app to the media analysis tool that assists communications professionals with writing tasks using the Anthropic API.

## Features

- **Multiple File Upload Areas**:
  - **Writing Style Examples**: Upload samples that demonstrate the desired writing style (e.g., CEO's previous communications)
  - **Past Examples**: Upload previous examples of similar content (e.g., past shareholder letters)
  - **Competitive Examples**: Upload examples from competitors or similar organizations for inspiration

- **Customizable Content Generation**:
  - Detailed brief input
  - Multiple format options (speeches, letters, blog posts, etc.)
  - Custom word count option

- **Content Management**:
  - Copy to clipboard
  - Download as TXT
  - (Future feature: Download as DOCX)

## Technical Details

- Built with Flask
- Uses Anthropic's Claude API for content generation
- Supports PDF, DOCX, and TXT file uploads
- Automatic file cleanup after 7 days

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd writing-assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the example:
   ```
   cp .env.example .env
   ```

5. Edit the `.env` file and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Flask development server:
   ```
   flask run
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000/
   ```

3. Fill in the writing brief, select a format, and optionally upload reference files.

4. Click "Generate Content" to create your content.

## File Upload Limits

- Maximum 3 files per category
- Maximum 10MB total upload size
- Supported formats: PDF, DOCX, TXT
- Files are automatically deleted after 7 days

## Development

### Project Structure

```
writing-assistant/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
├── .env.example            # Environment variables template
├── static/                 # Static assets
├── templates/              # HTML templates
│   ├── index.html          # Main application page
│   └── result.html         # Results display page
├── utils/                  # Utility functions
│   ├── file_processor.py   # File handling and text extraction
│   ├── prompt_builder.py   # Claude prompt construction
│   └── cleanup.py          # File retention management
└── uploads/                # Temporary file storage (gitignored)
```

### Adding New Format Types

To add a new format type, edit the `FORMAT_DETAILS` dictionary in `utils/prompt_builder.py`:

```python
FORMAT_DETAILS = {
    'new_format_key': {
        'description': 'Description of the format',
        'word_count': 1000,  # Default word count
        'characteristics': 'Characteristics of the format'
    },
    # ... existing formats
}
```

Then update the format dropdown in `templates/index.html` to include the new option.

## License

[MIT License](https://github.com/nathanstrauss13/writing-assistant/blob/main/LICENSE)

## Acknowledgements

- [Anthropic](https://www.anthropic.com/) for the Claude API
- [Flask](https://flask.palletsprojects.com/) web framework
- [Tailwind CSS](https://tailwindcss.com/) for styling
- [Dropzone.js](https://www.dropzonejs.com/) for file uploads
