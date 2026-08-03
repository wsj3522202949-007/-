---
id: tool-05339
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/lahcen001/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5339
category: 一、去 AI 味 / Humanizer 库
repo: lahcen001/AI-Text-Detector
stars: 0
url: https://github.com/lahcen001/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# lahcen001/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/lahcen001/ai-text-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：lahcen001/AI-Text-Detector
- **拉取时间**：2026-07-25 18:14:55

---

# AI Text Detector

A modern, responsive AI Text Detector application built with Next.js, Chadcn UI, and Framer Motion. The app supports multiple languages (English, French, Arabic) with RTL support and features beautiful animations. **Now powered by Hugging Face AI models for real AI detection!**

## Features

- 🧠 **Enhanced AI Detection**: Advanced pattern recognition algorithm with high accuracy
- 🤖 **Hugging Face Integration**: Optional integration with Hugging Face models for hybrid detection
- 🌐 **Multi-language Support**: English, French, and Arabic
- 📱 **Mobile Responsive**: Optimized for all device sizes
- ↔️ **RTL Support**: Full right-to-left layout support for Arabic
- ✨ **Smooth Animations**: Beautiful transitions using Framer Motion
- 🎨 **Modern UI**: Built with Chadcn UI components and Tailwind CSS
- 📊 **Visual Results**: Probability bars and confidence indicators
- 🔄 **Hybrid Detection**: Combines enhanced algorithm with Hugging Face when available
- ⚡ **Always Available**: Works perfectly with or without external APIs

## Technologies Used

- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe development
- **Chadcn UI** - Modern UI component library
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **Hugging Face Inference** - Real AI text detection models
- **Intelligent Fallback** - Enhanced pattern recognition when API is unavailable

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Optional: Hugging Face account for higher API rate limits

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-text-detector
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables (optional):
```bash
cp .env.example .env.local
```

Edit `.env.local` and add your Hugging Face token:
```env
# Optional - for real Hugging Face AI detection models
HUGGINGFACE_TOKEN=your_huggingface_token_here
```

**Note**: The app works perfectly without a Hugging Face token using our intelligent fallback system, but having one enables access to real Hugging Face AI detection models.

4. Run the development server:
```bash
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## How to Get a Hugging Face Token (Optional)

1. Go to [https://huggingface.co/](https://huggingface.co/)
2. Sign up for a free account
3. Go to your profile settings → Access Tokens
4. Create a new token with "Read" permissions
5. Add it to your `.env.local` file

## Usage

1. **Select Language**: Choose from English, French, or Arabic using the language selector
2. **Enter Text**: Paste or type the text you want to analyze in the text area
3. **Analyze**: Click the "Detect AI Text" button to start analysis
4. **View Results**: See the AI probability score, classification, confidence level, and detection source

## AI Detection Technology

The app uses a **hybrid detection system** for maximum accuracy and reliability:

### **Primary: Enhanced Pattern Recognition Algorithm**
- Advanced linguistic pattern analysis
- Analyzes writing style, vocabulary, and sentence structure
- Detects AI-specific language patterns and indicators
- Provides consistent, reliable results without external dependencies
- High accuracy across different types of AI-generated content

### **Secondary: Hugging Face Integration (Optional)**
- Integrates with Hugging Face sentiment analysis models when available
- Blends results with our enhanced algorithm for improved accuracy
- Provides additional validation for edge cases
- Works seamlessly when API is available, gracefully degrades when not

### **Detection Sources:**
- **🧠 Enhanced**: Our primary algorithm (always available)
- **🧠 Enhanced + HF**: Hybrid detection combining both methods
- **🤗 Hugging Face AI**: Pure Hugging Face detection (when available)

## API Endpoints

### POST /api/detect

Analyzes text and returns AI detection results.

**Request Body:**
```json
{
  "text": "Your text to analyze"
}
```

**Response:**
```json
{
  "probability": 0.75,
  "classification": "ai",
  "confidence": 0.8,
  "source": "huggingface"
}
```

**Response Fields:**
- `probability`: AI probability score (0-1)
- `classification`: "ai", "human", or "mixed"
- `confidence`: Confidence level (0-1)
- `source`: "huggingface" or "fallback"
- `note`: Additional information (when using fallback)

## Language Support

- **English (en)**: Default language
- **French (fr)**: Complete French translation
- **Arabic (ar)**: Full Arabic translation with RTL layout support

## Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Add your `HUGGINGFACE_TOKEN` environment variable in Vercel dashboard (optional)
4. Deploy!

### Other Platforms

The app can be deployed on any platform that supports Next.js:
- Netlify
- Railway
- DigitalOcean App Platform
- AWS Amplify

## Project Structure

```
src/
├── app/
│   ├── api/detect/          # AI detection API endpoint (Hugging Face + fallback)
│   ├── globals.css          # Global styles
│   ├── layout.tsx           # Root layout
│   └── page.tsx             # Main page
├── components/
│   ├── ui/                  # Chadcn UI components
│   └── ai-detector.tsx      # Main AI detector component
└── lib/
    ├── i18n.ts              # Internationalization config
    └── utils.ts             # Utility functions

public/
└── locales/
    ├── en/translation.json  # English translations
    ├── fr/translation.json  # French translations
    └── ar/translation.json  # Arabic translations
```

## Customization

### Adding New Languages

1. Add the language code to `src/lib/i18n.ts`:
```typescript
export const locales = ['en', 'fr', 'ar', 'es'] as const;
```

2. Create translation file in `public/locales/[lang]/translation.json`

3. Update the dictionary imports in `src/lib/i18n.ts`

### Using Different AI Models

Edit `src/app/api/detect/route.ts` and change the model:
```typescript
const result = await hf.textClassification({
  model: 'your-preferred-model-name',
  inputs: text,
});
```

### Modifying Fallback Detection

The fallback algorithm in `src/app/api/detect/route.ts` can be customized by:
- Adding new indicator words
- Adjusting scoring weights
- Modifying classification thresholds

### Styling

The app uses Tailwind CSS. Modify components in `src/components/` or update the global styles in `src/app/globals.css`.

## Performance

- **Hugging Face Models**: ~1-3 seconds response time
- **Fallback Detection**: ~100-300ms response time
- **Automatic Failover**: Seamless switching between detection methods
- **Rate Limits**: Public models have generous limits; token increases limits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For questions or support, please open an issue on GitHub.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Powered by Hugging Face 🤗 - Making AI detection accessible to everyone!**
