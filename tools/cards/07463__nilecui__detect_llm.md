---
id: tool-07463
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: detect_llm
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/nilecui/detect_llm
created: 2026-07-18
updated: 2026-07-18
no: 7463
category: 画龙补充 / 扩容入库 — 补充源
repo: nilecui/detect_llm
stars: 0
url: https://github.com/nilecui/detect_llm
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# nilecui/detect_llm

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/nilecui/detect_llm
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：detect_llm
- **拉取时间**：2026-07-25 19:22:40

related:
  - methods/QUICK_START.md
---

# LLM Text Detection System

A full-stack web application that detects AI-generated text from multiple Large Language Models (GPT, Gemini, Qwen, etc.) and provides sentence-level annotation showing which parts of long texts are AI-generated.

## Features

- **Sentence-Level Detection**: Analyze text and highlight each sentence based on AI-generation confidence
- **Color-Coded Visualization**: Intuitive green-to-red gradient showing confidence levels
- **Multiple LLM Support**: Detects text from GPT, Gemini, Qwen, and other language models
- **Confidence Scores**: Per-sentence and overall document confidence percentages
- **Real-Time Analysis**: Fast processing using GPU-accelerated RoBERTa models
- **Open Source**: Self-hosted, no API costs, works offline

## Technology Stack

### Backend
- **Python FastAPI**: Modern, fast web framework
- **PyTorch**: Deep learning framework
- **Hugging Face Transformers**: Pre-trained RoBERTa detection models
- **NLTK**: Natural language processing for sentence tokenization

### Frontend
- **React + TypeScript**: Component-based UI with type safety
- **Vite**: Fast build tool and dev server
- **Axios**: HTTP client for API communication

### Model
- **RoBERTa-base-openai-detector**: Pre-trained model for GPT-2/GPT-3 style text detection

## Project Structure

```
detect_llm/
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── main.py             # Application entry point
│   │   ├── api/endpoints/      # API route handlers
│   │   ├── core/               # Configuration
│   │   ├── models/             # ML model wrapper
│   │   ├── services/           # Business logic
│   │   └── schemas/            # Request/response models
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── hooks/              # Custom React hooks
│   │   ├── services/           # API client
│   │   ├── types/              # TypeScript types
│   │   └── utils/              # Utility functions
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
├── CLAUDE.md
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (optional, for containerized deployment)

### Local Development Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"

# Copy environment file
cp .env.example .env

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

API documentation at `http://localhost:8000/docs`

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Run development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

The application will be available at:
- Frontend: `http://localhost`
- Backend API: `http://localhost:8000`

## Usage

1. **Enter Text**: Paste or type text into the input area
2. **Analyze**: Click the "Analyze Text" button
3. **Review Results**:
   - Overall AI confidence score
   - Classification (Human/Mixed/AI)
   - Color-coded sentence highlighting
   - Per-sentence confidence scores (hover over sentences)

### Color Legend

- 🟢 **Green** (0-30%): Human-written
- 🟡 **Yellow** (30-50%): Possibly AI
- 🟠 **Orange** (50-70%): Likely AI
- 🔴 **Red** (70-100%): AI-generated

## API Endpoints

### POST /api/v1/detect

Analyze text for AI-generated content.

**Request:**
```json
{
  "text": "Text to analyze...",
  "model": "roberta-base"
}
```

**Response:**
```json
{
  "overall_score": 45.3,
  "overall_label": "mixed",
  "sentence_count": 10,
  "ai_sentence_count": 4,
  "sentences": [
    {
      "text": "First sentence.",
      "confidence": 15.2,
      "start_index": 0,
      "end_index": 15,
      "label": "human"
    }
  ],
  "model_used": "roberta-base-openai-detector",
  "processing_time": 0.234
}
```

### GET /api/v1/models

Get available detection models.

### GET /api/v1/health

Check API health status.

## Configuration

### Backend Environment Variables

```env
# Server settings
HOST=0.0.0.0
PORT=8000
DEBUG=True

# Model settings
MODEL_NAME=roberta-base-openai-detector
MODEL_CACHE_DIR=./model_cache
USE_GPU=True
BATCH_SIZE=16

# API settings
MAX_TEXT_LENGTH=50000
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Confidence thresholds
AI_HIGH_THRESHOLD=70.0
AI_MEDIUM_THRESHOLD=50.0
AI_LOW_THRESHOLD=30.0
```

### Frontend Environment Variables

```env
VITE_API_URL=http://localhost:8000
VITE_API_VERSION=v1
```

## Performance

Expected processing times:
- **Short text** (100 words): ~0.5 seconds
- **Medium text** (500 words): ~1.5 seconds
- **Long text** (2000 words): ~5 seconds

GPU acceleration provides 5-10x speedup over CPU.

## Development Commands

### Backend

```bash
# Run tests
pytest

# Run specific test
pytest tests/test_detector.py

# Code formatting
black app/

# Linting
flake8 app/

# Type checking
mypy app/
```

### Frontend

```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Linting
npm run lint

# Formatting
npm run format
```

## Troubleshooting

### Model Download Issues

If the Hugging Face model fails to download:

```bash
# Set cache directory
export TRANSFORMERS_CACHE=/path/to/cache
```

### NLTK Data Not Found

```python
import nltk
nltk.download('punkt')
```

### CORS Errors

Ensure `CORS_ORIGINS` in backend `.env` includes your frontend URL.

### Out of Memory (GPU)

Reduce batch size in `backend/app/core/config.py`:

```python
BATCH_SIZE = 8  # Instead of 16
```

## Architecture

### Detection Pipeline

1. **Text Input** → User submits text via frontend
2. **Sentence Tokenization** → NLTK splits text into sentences
3. **Batch Processing** → Sentences grouped for efficient GPU processing
4. **Model Inference** → RoBERTa model predicts AI probability for each sentence
5. **Score Calculation** → Convert probabilities to percentages, calculate overall score
6. **Classification** → Assign labels (human/ai-low/ai-medium/ai-high)
7. **Results Display** → Frontend renders color-coded visualization

### Model Details

- **Model**: `roberta-base-openai-detector` from Hugging Face
- **Architecture**: RoBERTa (Robustly Optimized BERT Approach)
- **Training**: Fine-tuned on GPT-2/GPT-3 generated text
- **Performance**: ~85-90% accuracy on diverse datasets

## Contributing

Contributions are welcome! Please see CLAUDE.md for development guidelines.

## License

MIT License

## Acknowledgments

- Hugging Face for pre-trained models
- OpenAI for detection model training
- FastAPI and React communities

## Support

For issues and questions, please open an issue on GitHub.
