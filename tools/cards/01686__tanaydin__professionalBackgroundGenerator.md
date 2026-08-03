---
id: tool-01686
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: professionalBackgroundGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tanaydin/professionalbackgroundgenerator
created: 2026-07-18
updated: 2026-07-18
no: 1686
category: 二、网文 / 长篇 AI 写作系统 库
repo: tanaydin/professionalBackgroundGenerator
stars: 3
url: https://github.com/tanaydin/professionalbackgroundgenerator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tanaydin/professionalBackgroundGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tanaydin/professionalbackgroundgenerator
- **Stars**：3
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：Transform your CV into a powerful career story - generate professional background sections in seconds using AI.
- **本地描述**：Transform your CV into a powerful career story - generate professional background sections in seconds using AI.
- **拉取时间**：2026-07-23 23:28:12

---

# Professional Background Generator

A web application that generates comprehensive Professional Background sections for CVs using AI. This tool helps professionals create compelling career narratives that showcase their experience, achievements, and competencies.

## Features

- **PDF & Markdown Support**: Upload CVs in PDF or Markdown format
- **AI-Powered Generation**: Uses OpenAI GPT-3.5 to create professional background sections
- **Smart Formatting**: Automatically converts PDF text to clean Markdown
- **Copy to Clipboard**: Easy copying of generated content
- **Real-time Processing**: Fast generation with progress feedback
- **Clean Interface**: Simple, user-friendly web interface

## What is a Professional Background?

A Professional Background section is a comprehensive narrative (300-400 words) that tells the story of your career journey. It includes:

- **Career Overview**: Years of experience, industry specialization, and career level
- **Career Progression**: Key roles, companies, promotions, and responsibility evolution
- **Achievements & Impact**: Major accomplishments with quantifiable results
- **Professional Competencies**: Technical skills, methodologies, and leadership qualities

This section is perfect for senior professionals, executives, or anyone wanting to showcase their career narrative in detail.

## Architecture

### Backend (Python/Flask)

```
backend/
├── app_backend.py      # Flask application and API routes
├── cv_processor.py     # CV processing and AI operations
├── openai_client.py    # OpenAI API client wrapper
├── utils.py            # Utility functions (text processing)
├── requirements.txt    # Python dependencies
└── Dockerfile          # Backend containerization
```

### Frontend (HTML/CSS/JavaScript)

```
frontend/
├── index.html          # Main application page
├── background.js       # Application logic and API calls
├── styles.css          # Styling and layout
├── nginx.conf          # Nginx configuration
└── Dockerfile          # Frontend containerization
```

## Technology Stack

### Backend
- **Python 3.11+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **OpenAI API** - GPT-3.5 Turbo for text generation
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript (ES6+)** - Application logic
- **Marked.js** - Markdown rendering
- **Nginx** - Web server (in Docker)

## Installation

### Prerequisites

- Python 3.11 or higher
- Node.js (optional, for development)
- OpenAI API key
- Docker & Docker Compose (for containarerized deployment)

### Development and run

```bash
docker-compose up -d
```

Services:
- **Backend**: `http://localhost:5000`
- **Frontend**: `http://localhost:8181`

## API Endpoints

### Health Check
```http
GET /api/health
```
Returns service health status.

### Upload CV
```http
POST /api/upload-cv
Content-Type: multipart/form-data

file: <PDF or Markdown file>
```

**Response:**
```json
{
  "cv_text": "extracted CV content...",
  "file_type": "pdf",
  "filename": "example.pdf",
  "character_count": 5420,
  "converted_to_markdown": true,
  "message": "CV successfully uploaded from PDF file and converted to Markdown"
}
```

### Generate Professional Background
```http
POST /api/generate-professional-background
Content-Type: application/json

{
  "user_cv": "Complete CV content as text..."
}
```

**Response:**
```json
{
  "professional_background": "Generated markdown content...",
  "processing_time": 3.45,
  "message": "Professional background generated successfully"
}
```

## Usage

1. **Upload or Paste CV**
   - Click "Upload CV File" to upload PDF or Markdown
   - Or paste CV content directly in the text area

2. **Generate Background**
   - Click "Generate Professional Background"
   - Wait for AI processing (typically 3-5 seconds)

3. **Copy & Use**
   - Review the generated content
   - Click "Copy to Clipboard" or copy the raw markdown
   - Add to your CV, typically near the beginning

## Project Structure

### Code Organization

- **`app_backend.py`**: Flask routes, request handling, and validation
- **`cv_processor.py`**: AI prompt engineering and CV processing logic
- **`openai_client.py`**: OpenAI API communication wrapper
- **`utils.py`**: Reusable utility functions (text processing, formatting)

### Key Classes

- **`CVProcessor`**: Manages CV processing and AI operations
- **`OpenAIClient`**: Handles OpenAI API calls with retry logic
- **`TextUtils`**: Provides text processing utilities

## Configuration

### Backend Configuration

Edit `backend/app_backend.py` to customize:
- Server host and port
- API rate limits
- Maximum CV length (default: 25,000 characters)
- Minimum CV length (default: 100 characters)

### AI Configuration

Edit `backend/openai_client.py` to customize:
- Model selection (default: `gpt-3.5-turbo`)
- Temperature settings (creativity level)
- Token limits (response length)

## Development

### Running Tests

```bash
cd backend
pytest
```

### Code Style

The project follows PEP 8 style guidelines. Use formatters:

```bash
black backend/
flake8 backend/
```

### Adding New Features

1. Add utility functions to `utils.py`
2. Add AI operations to `cv_processor.py`
3. Add API endpoints to `app_backend.py`
4. Update frontend in `background.js`

## Troubleshooting

### Common Issues

**"OPENAI_API_KEY not found"**
- Ensure `.env` file exists with valid API key
- Check environment variable is loaded: `echo $OPENAI_API_KEY`

**"CV content is too short"**
- Provide at least 100 characters of CV content
- Include detailed experience and education information

**"Failed to process uploaded file"**
- Ensure PDF is not encrypted or password-protected
- Try converting PDF to text manually first

**CORS errors**
- Ensure backend is running on port 5000
- Check Flask-CORS is properly configured

## Performance

- **Average Generation Time**: 3-5 seconds
- **Maximum CV Length**: 25,000 characters
- **Concurrent Requests**: Supports multiple simultaneous requests
- **Rate Limiting**: Respects OpenAI API rate limits

## Security

- API keys stored in environment variables (never committed)
- Input validation and sanitization
- File upload restrictions (PDF and Markdown only)
- Content length limits to prevent abuse
- CORS configured for specific origins

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team

## Acknowledgments

- OpenAI for GPT-3.5 API
- Flask community for excellent documentation
- All contributors to this project

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Built with ❤️ for professionals looking to enhance their CVs**
