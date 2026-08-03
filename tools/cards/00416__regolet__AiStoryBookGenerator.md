---
id: tool-00416
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AiStoryBookGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/regolet/aistorybookgenerator
created: 2026-07-18
updated: 2026-07-18
no: 416
category: 二、网文 / 长篇 AI 写作系统 库
repo: regolet/AiStoryBookGenerator
stars: 1
url: https://github.com/regolet/aistorybookgenerator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# regolet/AiStoryBookGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/regolet/aistorybookgenerator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：automating children's book
- **本地描述**：automating children's book
- **拉取时间**：2026-07-23 22:51:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI StoryBook Generator 🎨📚

Transform your stories into beautifully illustrated storybooks using AI! This application analyzes your text, breaks it into scenes, and generates stunning illustrations for each scene using multiple AI services.

## Features

- **Story Analysis**: Uses Google AI Studio (Gemini) to analyze stories and extract visual elements
- **Scene Detection**: Automatically breaks stories into illustrated scenes
- **Character Recognition**: Automatically detects character gender and assigns consistent names (Nave for male, Lia for female)
- **Smart Character Mode**: Enhances prompts with character information for consistent illustrations
- **Visual Direction**: Extracts facial expressions, colors, lighting, poses, and composition
- **Reference Images**: Generates initial reference images using Google AI Studio
- **High-Quality Illustrations**: Creates final images using Replicate.com models (Ideogram V3 Turbo default)
- **Multiple Art Styles**: Supports realistic, cartoon, anime, watercolor, and oil painting styles
- **Flexible Aspect Ratios**: Support for various aspect ratios (square, landscape, portrait, etc.)
- **Web Interface**: User-friendly interface for story input and storybook viewing
- **HTML Export**: Generates beautiful HTML storybooks for easy sharing

## Prerequisites

- Node.js 16+ and npm
- API Keys (only 2 required!):
  - Google AI Studio API Key
  - Replicate API Token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AiStoryBookGenerator.git
cd AiStoryBookGenerator
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file from the example:
```bash
cp .env.example .env
```

4. Add your API keys to the `.env` file:
```env
GOOGLE_AI_STUDIO_API_KEY=your_google_ai_studio_api_key_here
REPLICATE_API_TOKEN=your_replicate_api_token_here
PORT=3000
```

## Getting API Keys

### Google AI Studio API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Go to API Keys section
4. Generate a new API key

### Replicate API Token
1. Go to [Replicate](https://replicate.com/)
2. Create an account or sign in
3. Navigate to Account Settings
4. Find your API token

## Usage

1. Start the development server:
```bash
npm run dev
```

2. Open your browser and navigate to:
```
http://localhost:3000
```

3. Use the web interface to:
   - Paste your story text
   - Select art style and target audience
   - Configure advanced settings (optional)
   - Click "Generate StoryBook"

4. View your generated storybook in the browser or download the HTML file

## Project Structure

```
AiStoryBookGenerator/
├── src/
│   ├── server.ts           # Express server setup
│   ├── routes/
│   │   └── storyRoutes.ts  # API endpoints
│   ├── services/
│   │   ├── storyAnalyzer.ts      # OpenAI GPT integration
│   │   ├── googleAIStudio.ts     # Google AI Studio integration
│   │   ├── replicateService.ts   # Replicate.com integration
│   │   └── storyBookGenerator.ts # Main generation logic
│   └── types/
│       └── index.ts        # TypeScript type definitions
├── public/
│   ├── index.html          # Main web interface
│   ├── css/
│   │   └── style.css       # Styling
│   └── js/
│       └── app.js          # Frontend JavaScript
├── output/                 # Generated storybooks
├── uploads/                # Temporary file uploads
└── package.json
```

## API Endpoints

- `POST /api/generate-storybook` - Generate a complete storybook
- `POST /api/analyze-story` - Analyze story without generating images
- `GET /api/storybooks` - List all generated storybooks
- `GET /api/storybook/:id` - Get specific storybook details
- `GET /api/health` - Check API keys status

## Configuration Options

### Story Analysis
- **Style**: realistic, cartoon, anime, watercolor, oil-painting
- **Target Audience**: children, young-adult, adult

### Image Generation
- **Use Google Reference**: Enable/disable reference image generation
- **Image Dimensions**: 512-2048 pixels
- **Inference Steps**: 20-100 (higher = better quality, slower)
- **Guidance Scale**: 1-20 (higher = more prompt adherence)

### Replicate Models
- **Ideogram V3 Turbo** (default) - Fast, high-quality, text-capable
- **Smart Character Mode** - Auto-detects character gender and uses consistent naming (Nave/Lia)
- **SDXL** - Traditional diffusion model
- **Stable Diffusion 2.1** - Classic option
- **OpenJourney** - Artistic style

### Character System
The application includes an intelligent character recognition system:
- **Automatic Gender Detection** - Analyzes story content to identify main character gender
- **Consistent Naming** - Uses "Nave" for male characters, "Lia" for female characters
- **Enhanced Prompts** - Automatically enhances image generation prompts with character information
- **Character Continuity** - Ensures consistent character appearance across all scenes

## Development

### Run in development mode:
```bash
npm run dev
```

### Build for production:
```bash
npm run build
```

### Start production server:
```bash
npm start
```

## Example Story Input

```
Title: The Brave Little Robot

Once upon a time, in a futuristic city filled with towering skyscrapers and neon lights, there lived a small robot named Beep. Beep had bright blue eyes that glowed in the dark and silver metallic body that sparkled under the city lights.

One day, Beep discovered that the city's main power source was failing. The giant crystal that powered everything was losing its glow. Beep knew he had to help.

Despite being the smallest robot in the city, Beep ventured into the dangerous underground tunnels. There, he found the problem - a massive tangle of broken cables.

Working through the night, Beep carefully repaired each cable with his tiny tools. As the sun rose, the crystal began to glow again, brighter than ever.

The city celebrated Beep as a hero, proving that even the smallest among us can make the biggest difference.
```

## Troubleshooting

### API Key Issues
- Ensure all API keys are correctly set in the `.env` file
- Check the Settings tab in the web interface to verify API status
- Restart the server after adding API keys

### Image Generation Failures
- Check your Replicate account has sufficient credits
- Verify Google AI Studio API is enabled
- Try reducing image dimensions or inference steps

### Memory Issues
- Reduce the number of scenes by writing shorter stories
- Lower image resolution in advanced settings
- Process one story at a time

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

ISC License

## Acknowledgments

- OpenAI for GPT story analysis
- Google AI Studio for reference generation
- Replicate for high-quality image generation
- All the AI models and services that make this possible

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
