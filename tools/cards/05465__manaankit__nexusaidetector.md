---
id: tool-05465
type: tool
area: 库
status: active
tags: [去AI味, 文风迁移, Python, 协议宽松, 需API密钥, 英文文档, 改稿润色]
title: nexusaidetector
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/manaankit/nexusaidetector
created: 2026-07-18
updated: 2026-07-18
no: 5465
category: 一、去 AI 味 / Humanizer 库
repo: manaankit/nexusaidetector
stars: 1
url: https://github.com/manaankit/nexusaidetector
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: da6d37f723a43294
  - methods/改稿润色指令库.md
---

# manaankit/nexusaidetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/manaankit/nexusaidetector
- **Stars**：1
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：This project is an end-to-end pipeline for improving text humanization and training an AI-vs-human text detector. It includes a realtime editing engine, style-aware rewriting workflows, dataset synthesis utilities, and scalable model training/evaluation scripts built around Hugging Face + LoRA/QLoRA.
- **本地描述**：This project is an end-to-end pipeline for improving text humanization and training an AI-vs-human text detector. It includes a realtime editing engine, style-aware rewriting workflows, dataset synthesis utilities, and scalable model training/evaluation scripts built around Hugging Face + LoRA/QLoRA.
- **拉取时间**：2026-07-25 18:19:42

---

# AI Text Tools Suite

A comprehensive web application for **AI Text Humanization**, **Plagiarism Detection**, and **Citation Generation** powered by a fine-tuned Mistral model hosted on Hugging Face Spaces!

## 🌟 Features

### 1. AI Text Humanizer
- Transform AI-generated content into natural, human-like text
- Multiple intensity levels (Low, Medium, High)
- Real-time humanization scoring (0-100)
- Before/after comparison
- Features:
  - Sentence structure variation
  - Natural transition words
  - Formal-to-casual word replacement
  - Contraction addition
  - AI pattern removal

### 2. Plagiarism Detector
- Advanced plagiarism detection using fingerprinting algorithms
- Document database for comparison
- Similarity percentage calculation
- Exact passage matching
- Features:
  - Shingling-based text fingerprinting
  - Jaccard similarity calculation
  - Common phrase detection
  - Detailed match reporting

### 3. Citation & Reference Generator
- Multiple citation formats: APA, MLA, Chicago, Harvard, IEEE
- Automatic metadata extraction
- All formats generated simultaneously
- Copy-to-clipboard functionality

### 4. File Support
- **Upload up to 100MB files**
- **No character limit in text editor**
- Supported formats: PDF, DOCX, DOC, TXT
- Automatic text extraction

## 🚀 Technology Stack

- **Backend**: Python 3.8+ with Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI Inference**: Hugging Face Spaces via `gradio-client`
- **Text Processing**: PyPDF2, python-docx
- **Model**: Custom fine-tuned Mistral-7B LoRA adapter for multi-task sequential classification and generation

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- 500MB free disk space (for NLTK data)

## 🔧 Installation

### Step 1: Clone or Download
```bash
# Clone the repository
git clone <repository-url>
cd nexusaidetector
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Hugging Face Space Tokens
The backend natively communicates with a Hugging Face Space to perform AI Inference. You must export your Space ID and API token before running the app.

```bash
# macOS/Linux
export HF_SPACE_ID="your_huggingface_username/your_space_name"
export HF_TOKEN="your_huggingface_read_token"

# Windows (Command Prompt)
set HF_SPACE_ID="your_huggingface_username/your_space_name"
set HF_TOKEN="your_huggingface_read_token"
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:9030`

## 🧠 Model Training

This repository includes the exact scripts used to train our multi-task Mistral-7B model for AI Text Detection and Humanization. 
While large model check-points and weights are not committed to source control, all training logic is preserved locally in `ai-text-tool/current/scripts/`.

### Training Pipeline
1. **Dataset Preparation:** Run `build_mixed_dataset.py` to organize human and AI text datasets into training splits.
2. **LoRA Fine-Tuning:** Execute `train_mistral_sft.py` to run Supervised Fine-Tuning efficiently using 4-bit `bitsandbytes` quantization and PEFT.
3. **Evaluation:** Use `select_best_checkpoint.py` and `postprod_smoke_test.py` to evaluate the generated LoRA adapters against hold-out sets.
4. **Export & Serve:** The finalized adapter is packaged using `postprod_build_release.py`. The resulting model can then be uploaded securely to Hugging Face Spaces for scalable and fast API inference.

## 📖 Usage Guide

### AI Text Humanizer

1. Navigate to the **AI Humanizer** tab
2. Either:
   - Paste text directly into the text editor, OR
   - Upload a file (PDF, DOCX, TXT)
3. Select humanization intensity:
   - **Low**: Minimal changes, maintains formal tone
   - **Medium**: Balanced approach (recommended)
   - **High**: Maximum humanization, very casual
4. Click **"Humanize Text"**
5. Review the results:
   - Original score vs. New score
   - Improvement metrics
   - Humanized text output
6. Copy the humanized text

### Plagiarism Detector

1. Navigate to the **Plagiarism Detector** tab
2. (Optional) Build your database:
   - Click **"Add to Database"**
   - Enter document title and text
   - Submit to add to comparison database
3. Paste or upload text to check
4. Click **"Check Plagiarism"**
5. Review the report:
   - Overall plagiarism percentage
   - Status (Clean, Moderate, High)
   - Matching sources with similarity scores
   - Exact matching passages
   - Web similarity score

### Citation Generator

1. Navigate to the **Citation Generator** tab
2. Enter source information:
   - Author(s)
   - Title
   - Year
   - Source/Publication
   - URL (if applicable)
3. Or use auto-extraction:
   - Paste text/URL into the extraction box
   - Click **"Extract Info"**
4. Select citation style (APA, MLA, Chicago, Harvard, IEEE)
5. Click **"Generate Citation"**
6. View results:
   - Selected format citation
   - All formats (switch tabs)
7. Copy citation(s) to clipboard

## 🎯 API Endpoints

### POST `/humanize`
Humanize AI-generated text.

**Request:**
```json
{
  "text": "Your text here",
  "intensity": "medium"
}
```

**Response:**
```json
{
  "original_text": "...",
  "humanized_text": "...",
  "original_score": 45,
  "new_score": 78,
  "improvement": 33
}
```

### POST `/check-plagiarism`
Check text for plagiarism.

**Request:**
```json
{
  "text": "Text to check"
}
```

**Response:**
```json
{
  "overall_plagiarism": 25.5,
  "web_similarity": 15.0,
  "sources_found": 2,
  "status": "Moderate",
  "detailed_results": [...],
  "total_documents_checked": 5
}
```

### POST `/add-document`
Add document to plagiarism database.

**Request:**
```json
{
  "text": "Document text",
  "title": "Document Title"
}
```

**Response:**
```json
{
  "message": "Document added successfully",
  "document_id": 0,
  "total_documents": 1
}
```

### POST `/generate-citation`
Generate citations in multiple formats.

**Request:**
```json
{
  "citation_data": {
    "authors": "Smith, J.",
    "title": "Article Title",
    "year": "2024",
    "source": "Journal Name",
    "url": "https://..."
  },
  "style": "APA"
}
```

**Response:**
```json
{
  "citation": "Smith, J. (2024). Article Title. Journal Name. https://...",
  "style": "APA",
  "all_formats": {
    "APA": "...",
    "MLA": "...",
    "Chicago": "...",
    "Harvard": "...",
    "IEEE": "..."
  }
}
```

### POST `/upload`
Upload and extract text from files.

**Request:** FormData with file

**Response:**
```json
{
  "text": "Extracted text...",
  "filename": "document.pdf",
  "character_count": 5000,
  "word_count": 850
}
```

## 🔒 Security Features

- File upload size limit: 100MB
- Secure filename handling
- Input validation
- XSS protection
- CSRF token support (configure SECRET_KEY)

## 🎨 Customization

### Change Color Scheme
Edit `/static/css/styles.css` and modify CSS variables:
```css
:root {
    --primary: #4F46E5;        /* Primary color */
    --secondary: #10B981;      /* Success/secondary color */
    --danger: #EF4444;         /* Error/danger color */
    --warning: #F59E0B;        /* Warning color */
}
```

### Adjust Humanization Algorithm
Edit `app.py` in the `AIHumanizer` class to:
- Add more transition phrases
- Modify AI pattern detection
- Adjust scoring weights
- Add custom word replacements

### Modify Plagiarism Sensitivity
Edit `app.py` in the `PlagiarismDetector` class:
```python
self.shingle_size = 5  # Increase for less sensitivity
threshold = 0.15       # Lower for stricter detection
```

## 📊 Performance

- **Processing Speed**: ~1000 words/second (humanization)
- **Max File Size**: 100MB
- **Text Limit**: Unlimited characters
- **Concurrent Users**: Depends on server setup
- **Memory Usage**: ~200-500MB (with NLTK data)

## 🐛 Troubleshooting

### NLTK Data Download Issues
```python
# Manually download NLTK data
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('stopwords')
>>> nltk.download('averaged_perceptron_tagger')
```

### File Upload Errors
- Ensure uploads folder has write permissions
- Check file size limit in app.config
- Verify file format is supported

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=8000)
```

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production (Using Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Production (Using Waitress - Windows)
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"

EXPOSE 5000
CMD ["python", "app.py"]
```

## 📝 Configuration

### Environment Variables
Create a `.env` file:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
MAX_CONTENT_LENGTH=104857600
```

### Security Hardening
1. Change SECRET_KEY in app.py
2. Enable HTTPS in production
3. Configure CORS if needed
4. Set up rate limiting
5. Use environment variables for sensitive data

## 🤝 Contributing

This is a standalone application with no external dependencies. To contribute:

1. Test all features thoroughly
2. Maintain zero external API dependencies
3. Document any new features
4. Follow Python PEP 8 style guide

## 📄 License

This project is open source and available for educational and commercial use.

## 🔮 Future Enhancements

Possible additions without external APIs:
- [ ] Grammar checking
- [ ] Readability analysis
- [ ] Keyword extraction
- [ ] Text summarization
- [ ] Language translation (offline models)
- [ ] Export to multiple file formats
- [ ] User authentication
- [ ] Document history/versioning
- [ ] Batch processing

## 💡 Tips

1. **Better Humanization**: Use "High" intensity for casual content, "Low" for professional
2. **Plagiarism Database**: Add more documents for better detection accuracy
3. **Citations**: Always verify generated citations for accuracy
4. **Large Files**: For files >50MB, consider processing in sections
5. **Performance**: Use production server (Gunicorn) for multiple users

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Review API endpoint documentation
3. Examine browser console for errors
4. Check Flask logs in terminal

## 🎓 How It Works

### AI Humanization Algorithm
1. **Tokenization**: Text split into sentences and words
2. **Pattern Detection**: Identifies AI-typical patterns
3. **Structure Variation**: Modifies sentence structures
4. **Word Replacement**: Substitutes formal words with casual alternatives
5. **Contraction Addition**: Adds natural contractions
6. **Transition Injection**: Inserts natural connectors
7. **Scoring**: Calculates humanization score based on multiple factors

### Plagiarism Detection Algorithm
1. **Fingerprinting**: Creates text fingerprint using shingling
2. **Hashing**: Converts shingles to MD5 hashes for efficient comparison
3. **Similarity Calculation**: Uses Jaccard similarity coefficient
4. **Passage Matching**: Employs difflib for exact match detection
5. **Scoring**: Combines database and web similarity metrics

### Citation Generation
Uses template-based formatting following official style guides for each citation format.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Built with Python Flask | No External APIs | 100% Local Processing**
