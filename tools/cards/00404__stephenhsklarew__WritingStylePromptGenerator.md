---
id: tool-00404
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 需API密钥, 英文文档]
title: WritingStylePromptGenerator
summary: 小说转语音/有声书
source: https://github.com/stephenhsklarew/writingstylepromptgenerator
created: 2026-07-18
updated: 2026-07-18
no: 404
category: 二、网文 / 长篇 AI 写作系统 库
repo: stephenhsklarew/WritingStylePromptGenerator
stars: 4
url: https://github.com/stephenhsklarew/writingstylepromptgenerator
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4e6b12a5bf96550e
  - methods/最强写作方法论_全球最强综合版.md
---

# stephenhsklarew/WritingStylePromptGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/stephenhsklarew/writingstylepromptgenerator
- **Stars**：4
- **语言**：Python
- **License**：None
- **Topics**：ai-prompts, anthropic, content-creation, google-drive, openai, python, style-guide, writing-analysis, writing-style
- **GitHub 描述**：Analyze your writing samples and generate AI style prompts that capture your unique voice, tone, and patterns. Works with local files or Google Drive.
- **本地描述**：Analyze your writing samples and generate AI style prompts that capture your unique voice, tone, and patterns. Works with local files or Google Drive.
- **拉取时间**：2026-07-23 22:50:54

---

# Writing Style Prompt Generator

Analyze your writing samples (local files or Google Drive documents) and automatically generate comprehensive AI writing style prompts that capture your unique voice, tone, and patterns.

## What Does This Do?

This tool:
1. **Reads** your writing samples from local files or Google Drive
2. **Analyzes** your writing style using AI (patterns, voice, structure, etc.)
3. **Generates** a comprehensive style guide that AI tools can use to write in your voice

Perfect for:
- Content creators who want AI to write in their style
- Businesses standardizing brand voice across teams
- Authors maintaining consistent voice across projects
- Marketers creating style guides for AI-generated content

---

## Quick Start

### 1. Installation

```bash
# Navigate to the directory
cd ~/Development/Scripts/WritingStylePromptGenerator

# Install dependencies
pip install -r requirements.txt

# Copy the example environment file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or open in your text editor
```

### 2. Add Your API Key

Edit `.env` and add your API key for one of these providers:

**Option A: OpenAI** (Recommended for cost-effectiveness)
```bash
AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-your-key-here
```

**Option B: Anthropic** (Recommended for highest quality)
```bash
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Option C: Google Gemini** (Alternative option)
```bash
AI_PROVIDER=google
GOOGLE_API_KEY=your-google-key-here
```

### 3. Run the Analyzer

**Analyze local documents:**
```bash
python3 writing_style_analyzer.py --local ~/Documents/MyArticles
```

**Analyze Google Drive folder:**
```bash
python3 writing_style_analyzer.py --drive YOUR_INPUT_FOLDER_ID
```

**Analyze Drive and upload outputs back to Drive:**
```bash
python3 writing_style_analyzer.py --drive YOUR_INPUT_FOLDER_ID --drive-output YOUR_OUTPUT_FOLDER_ID
```

**Focus on a specific speaker in the Transcript section:**
```bash
python3 writing_style_analyzer.py \
    --drive YOUR_INPUT_FOLDER_ID \
    --drive-output YOUR_OUTPUT_FOLDER_ID \
    --speaker "Stephen Sklarew"
```

Only content under a “Transcript” heading is analyzed, and lines are filtered to those attributed to the named speaker.

### 4. Use the Output

Open the `output/` directory and use the generated `AI_WRITING_STYLE_PROMPT_*.md` file with ChatGPT, Claude, or any AI tool.

---

## Detailed Setup

### Prerequisites

- Python 3.9 or higher
- API key from OpenAI, Anthropic, or Google
- (Optional) Google Drive credentials if analyzing Drive documents

### Installation Steps

#### 1. Clone or Download

```bash
# If you have this as part of a larger repository
cd ~/Development/Scripts/WritingStylePromptGenerator

# Or download directly
# (Download files to your desired location)
```

#### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

**Minimal Install** (just core features):
```bash
pip install python-dotenv anthropic openai google-generativeai
```

**Full Install** (includes PDF, Word, and Google Drive support):
```bash
pip install -r requirements.txt
```

#### 4. Configure API Keys

```bash
# Copy the example file
cp .env.example .env

# Edit with your preferred editor
nano .env
# or
open -a TextEdit .env
```

Add your API key for your chosen provider (see Quick Start section above).

### Google Drive Setup (Optional)

If you want to analyze documents from Google Drive:

1. **Get OAuth Credentials:**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a project (or use existing)
   - Enable Google Drive API and Google Docs API
   - Create OAuth 2.0 credentials (Desktop app)
   - Download as `credentials.json`
   - Place in this directory

2. **First Run Authentication:**
   ```bash
   python3 writing_style_analyzer.py --drive YOUR_FOLDER_ID
   ```

   This will:
   - Open your browser for authentication
   - Create `token.pickle` for future use
   - Proceed with analysis

---

## Usage

### Basic Usage

```bash
# Analyze local directory
python3 writing_style_analyzer.py --local /path/to/documents

# Analyze single file
python3 writing_style_analyzer.py --local /path/to/article.md

# Analyze Google Drive folder
python3 writing_style_analyzer.py --drive FOLDER_ID
```

### Advanced Options

```bash
# Specify output directory
python3 writing_style_analyzer.py --local ~/Articles --output ~/Desktop/analysis

# Include brand voice information
python3 writing_style_analyzer.py --local ~/Articles --brand brand_voice.json

# Full example
python3 writing_style_analyzer.py \
  --local ~/Documents/Blog \
  --output ~/Desktop/WritingStyle \
  --brand ~/Documents/brand_info.json
```

### Command-Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `--local PATH` | Path to local directory or file | One of --local or --drive |
| `--drive FOLDER_ID` | Google Drive folder ID | One of --local or --drive |
| `--output PATH` | Output directory (default: ./output) | No |
| `--brand PATH` | JSON file with brand information | No |

### Getting Google Drive Folder ID

1. Open the folder in Google Drive
2. Look at the URL: `https://drive.google.com/drive/folders/1A9zj-FOfDEg3nKhpjoTHeOjVf2x6I_Hv`
3. The folder ID is the last part: `1A9zj-FOfDEg3nKhpjoTHeOjVf2x6I_Hv`

---

## Supported File Formats

### Local Files
- **Text files:** `.txt`, `.md`
- **PDF files:** `.pdf` (requires `PyPDF2`)
- **Word documents:** `.doc`, `.docx` (requires `python-docx`)

### Google Drive
- **Google Docs:** All Google Docs in the specified folder
- **Recursive scanning:** Includes all subfolders

---

## Output Files

The tool generates several files in the output directory:

### 1. `AI_WRITING_STYLE_PROMPT_[timestamp].md` ⭐ **MAIN FILE**
**Your comprehensive writing style guide for AI tools.**

Contains:
- Voice & tone profile
- Structural templates
- Writing mechanics (paragraph/sentence patterns)
- Signature techniques
- Do's and don'ts
- Quality checklists
- Practical examples and templates

**How to use:** Copy and paste this into ChatGPT, Claude, or any AI tool before asking it to write content.

### 2. `WRITING_STYLE_ANALYSIS_[timestamp].md`
**Detailed analysis of your writing patterns.**

Includes:
- Opening hook strategies
- Structural patterns
- Vocabulary analysis
- Tone distribution
- Rhetorical devices
- Examples with citations

### 3. `analysis_data_[timestamp].json`
**Raw analysis data in JSON format.**

Useful for:
- Custom processing
- Integration with other tools
- Backup reference

### 4. `README.md`
**Index of all generated files with summary.**

---

## Brand Information (Optional)

You can provide brand voice information to enhance the analysis. Create a JSON file:

```json
{
  "brand_name": "Your Company",
  "personality": {
    "archetypes": ["Sage", "Magician", "Creator"],
    "characteristics": ["Knowledgeable", "Innovative", "Trustworthy"]
  },
  "tone_guidelines": {
    "do": [
      "Use expert, authoritative voice",
      "Incorporate data and research",
      "Be inspiring and forward-looking"
    ],
    "dont": [
      "Avoid clichés",
      "Don't be condescending",
      "Avoid hype and overpraise"
    ]
  },
  "target_audience": "Business leaders and decision makers",
  "purpose": "Educate and empower readers about AI adoption"
}
```

Then use it:
```bash
python3 writing_style_analyzer.py --local ~/Articles --brand brand_info.json
```

---

## Examples

### Example 1: Analyze Blog Articles

```bash
# You have a folder of blog posts
python3 writing_style_analyzer.py --local ~/Documents/BlogPosts

# Output will be in ./output/
```

### Example 2: Analyze Google Drive Newsletter

```bash
# Your newsletter archives are in Google Drive
python3 writing_style_analyzer.py --drive 1A9zj-FOfDEg3nKhpjoTHeOjVf2x6I_Hv

# Output will be in ./output/
```

### Example 3: Full Analysis with Brand Info

```bash
# Create brand_info.json with your brand guidelines
# Then run full analysis
python3 writing_style_analyzer.py \
  --local ~/Documents/CompanyBlog \
  --brand brand_info.json \
  --output ~/Desktop/StyleAnalysis
```

---

## How It Works

### Step 1: Document Collection
- Scans local directory or Google Drive folder
- Reads all supported file types
- Extracts text content

### Step 2: AI Analysis
- Sends documents to your chosen AI provider
- Analyzes patterns across multiple dimensions:
  - Opening hooks and conclusions
  - Structural organization
  - Paragraph and sentence rhythm
  - Vocabulary and tone
  - Rhetorical devices
  - Examples and evidence usage
  - Transitions and flow
  - Unique stylistic elements

### Step 3: Style Prompt Generation
- Creates comprehensive writing guide
- Includes specific examples from your writing
- Provides actionable templates and patterns
- Adds quality checklists

### Step 4: Output Creation
- Saves multiple formats (markdown, JSON)
- Creates index with metadata
- Organizes in timestamped output directory

---

## AI Provider Comparison

| Provider | Model | Best For | Cost (estimate) | Quality |
|----------|-------|----------|-----------------|---------|
| **OpenAI** | GPT-4o | Balance of cost & quality | ~$0.50 per analysis | ⭐⭐⭐⭐ |
| **Anthropic** | Claude Sonnet 4.5 | Highest quality analysis | ~$5 per analysis | ⭐⭐⭐⭐⭐ |
| **Google** | Gemini 1.5 Pro | Alternative option | ~$1 per analysis | ⭐⭐⭐⭐ |

*Estimates based on analyzing ~15,000-20,000 words of content*

**Recommendation:** Start with OpenAI GPT-4o for cost-effectiveness. Upgrade to Anthropic Claude for highest quality.

---

## Troubleshooting

### Common Issues

**Issue:** `OPENAI_API_KEY not found`
```bash
# Solution: Make sure you've created .env file and added your API key
cp .env.example .env
nano .env  # Add your API key
```

**Issue:** `No documents found`
```bash
# Solution: Check that your path is correct and contains supported files
ls ~/Documents/Articles  # Verify files exist
python3 writing_style_analyzer.py --local ~/Documents/Articles
```

**Issue:** `PyPDF2 not installed`
```bash
# Solution: Install PDF support
pip install PyPDF2
```

**Issue:** `Credentials file 'token.pickle' not found`
```bash
# Solution: You need to authenticate for Google Drive
# Make sure credentials.json exists, then run again
# Browser will open for authentication
```

**Issue:** Analysis fails with rate limit error
```bash
# Solution: You've hit API rate limits
# Wait a few minutes and try again
# Or consider upgrading your API plan
```

---

## Tips for Best Results

### 1. Provide Diverse Samples
- Include 5-10 documents minimum
- Cover different topics
- Include various lengths (short and long pieces)

### 2. Use Quality Writing
- Use your best, most representative work
- Avoid drafts or unedited pieces
- Include pieces that reflect your desired voice

### 3. Add Brand Context
- Create a brand_info.json file with your guidelines
- This helps the AI understand intentional style choices
- Particularly useful for business/brand writing

### 4. Review and Refine
- The generated prompt is a starting point
- Review the analysis for accuracy
- Edit the style prompt to emphasize key elements
- Test with your AI tool and refine

---

## Use Cases

### Content Creators
Generate blog posts, articles, and social media content in your authentic voice.

### Businesses
Ensure consistent brand voice across all AI-generated marketing materials.

### Authors
Maintain character voice consistency when using AI for fiction writing assistance.

### Agencies
Create client-specific style guides for AI content generation.

### Personal Knowledge Management
Train AI assistants to write notes, summaries, and documents in your style.

---

## FAQ

**Q: How many documents do I need?**
A: Minimum 3-5 documents, but 10-20 provides better analysis. Total word count of 10,000-30,000 words is ideal.

**Q: What file formats are supported?**
A: `.txt`, `.md`, `.pdf` (with PyPDF2), `.doc`/`.docx` (with python-docx), and Google Docs.

**Q: Can I analyze someone else's writing?**
A: Yes! This is great for studying writing styles you admire or creating team style guides.

**Q: How accurate is the analysis?**
A: Very accurate with 10+ diverse samples. Quality improves with more content and better AI models (Claude Sonnet 4.5 is most accurate).

**Q: Can I edit the generated style prompt?**
A: Absolutely! The generated prompt is a starting point. Edit it to emphasize what's most important to you.

**Q: Does this work for fiction writing?**
A: Yes! It works for any writing style. Provide character dialogue, narrative samples, etc.

**Q: What if I want to combine multiple writers' styles?**
A: Analyze each writer separately, then manually combine the prompts to create a hybrid style.

**Q: How often should I regenerate the prompt?**
A: Regenerate when:
- Your writing style evolves significantly
- You want to analyze new content
- You're refining brand voice guidelines

**Q: Can this replace a human editor?**
A: No. It's a tool to help AI write in your style, but human review and editing are still essential.

---

## Advanced Usage

### Custom Analysis Prompts

You can modify the analysis prompts in `writing_style_analyzer.py`:

```python
def _create_analysis_prompt(self, documents: List[Dict], brand_info: Dict = None) -> str:
    # Customize the analysis sections here
    # Add your own analysis dimensions
```

### Integration with Other Tools

The JSON output can be integrated with:
- Content management systems
- Writing automation pipelines
- Custom AI tools

### Batch Processing

```bash
# Process multiple folders
for folder in Blog Newsletter Articles; do
    python3 writing_style_analyzer.py \
      --local ~/Documents/$folder \
      --output ~/StyleAnalysis/$folder
done
```

---

## Credits

**Original Analysis:** Created for Synaptiq's "Raise Your AIQ" newsletter
**Tool Author:** Generated using Claude Code
**AI Providers:** OpenAI, Anthropic, Google

---

## License

MIT License - Use freely for personal or commercial purposes.

---

## Support & Contributing

Found a bug or have a feature request?
1. Check existing issues
2. Create a new issue with details
3. Or submit a pull request

---

## Changelog

### v1.0.0 (2025-01-07)
- Initial release
- Support for local and Google Drive documents
- Multi-provider AI analysis (OpenAI, Anthropic, Google)
- Comprehensive style prompt generation
- Support for .txt, .md, .pdf, .doc/.docx, Google Docs
- Brand information integration
- Quality output with multiple formats

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Ready to analyze your writing style?**

```bash
python3 writing_style_analyzer.py --local ~/Documents/YourWriting
```

*Your AI writing assistant is about to learn your voice!* 🎯
