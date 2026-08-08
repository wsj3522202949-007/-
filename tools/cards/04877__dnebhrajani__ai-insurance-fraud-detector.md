---
id: tool-04877
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-insurance-fraud-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/dnebhrajani/ai-insurance-fraud-detector
created: 2026-07-18
updated: 2026-07-18
no: 4877
category: 一、去 AI 味 / Humanizer 库
repo: dnebhrajani/ai-insurance-fraud-detector
stars: 0
url: https://github.com/dnebhrajani/ai-insurance-fraud-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6eafdb8003158fc9
  - methods/改稿润色指令库.md
---

# dnebhrajani/ai-insurance-fraud-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/dnebhrajani/ai-insurance-fraud-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An AI-powered system to detect fraud in insurance claims by analyzing images and text. Built with Next.js, Python, and Vision-Language Models (CLIP, Qwen2-VL)
- **本地描述**：An AI-powered system to detect fraud in insurance claims by analyzing images and text. Built with Next.js, Python, and Vision-Language Models (CLIP, Qwen2-VL)
- **拉取时间**：2026-07-25 17:57:48

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Insurance Claim AI Fraud Detector

An advanced AI system that automates insurance claim verification by analyzing images and text to detect fraud, assess damage, and ensure claim authenticity.

## Features

- **AI-Powered Fraud Detection**: Automatically flags suspicious claims by analyzing photos for signs of tampering or AI-generated content.
- **Scene Consistency Verification**: Uses the CLIP model to ensure that all photos in a claim are from the same incident scene.
- **Damage Assessment**: Employs the Qwen2-VL Vision-Language model to analyze damage photos, cross-reference them with the user's description, and assess the severity.
- **Explainable AI Reports**: Generates transparent, easy-to-understand reports with visual evidence (like heatmaps) and confidence scores.
- **Full-Stack Application**: A complete web application for submitting and reviewing claims, built with a modern tech stack.

## Tech Stack

- **Frontend**: Next.js, React, Tailwind CSS
- **Backend**: Node.js, Python (Flask/FastAPI)
- **Database**: Supabase (PostgreSQL)
- **AI/ML**:
  - **CLIP**: For scene consistency and image classification.
  - **Qwen2-VL**: For advanced damage verification and vision-language tasks.
- **Deployment**: Vercel (Frontend), Docker (AI Services)

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.10
- 8GB RAM minimum (16GB recommended)
- 10GB free disk space

### 1. Database Setup

1. Go to your Supabase dashboard
2. Navigate to SQL Editor
3. Run the following SQL files in order:
   - `supabase-schema.sql`
   - `supabase-migration-scene-analysis.sql`
   - `supabase-migration-damage-verification.sql`

### 2. Environment Configuration

Create `.env.local` and add your Supabase credentials:

```bash
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
SCENE_API_URL=
SUPABASE_BUCKET=
DAMAGE_VERIFY_URL=
```

### 3. AI Services Setup

**Linux/Mac:**

```bash
cd scene_service
python3 setup.py
```

**Windows:**

```bash
cd scene_service
python setup.py
```

This will download:

- CLIP model (~350MB)
- Qwen2-VL model (~5GB)

_Total download: ~5.5GB • Setup time: 15-30 minutes_

### 4. Start All Services

**Terminal 1 - CLIP Service (Scene Analysis):**

```bash
cd scene_service
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
python main.py
```

**Terminal 2 - Qwen2-VL Service (Damage Verification):**

```bash
cd scene_service
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
python damage_verifier.py
```

**Terminal 3 - Frontend (Next.js):**

```bash
npm install
npm run dev
```

## Application Access

Once all services are running:

- **Frontend**: http://localhost:3000
- **CLIP Service**: http://localhost:8000
- **Qwen2-VL Service**: http://localhost:8001

## Testing the Application

### Submit a New Claim

1. Navigate to: http://localhost:3000/claim/new
2. Fill out the claim form with:
   - Incident description
   - Upload accident scene photos
   - Upload damage photos
3. Submit the claim
4. The AI will automatically:
   - Verify scene consistency using CLIP
   - Assess damage using Qwen2-VL
   - Generate verification results

## AI Models

- **CLIP**: Scene consistency verification and image classification
- **Qwen2-VL-2B-Instruct**: Advanced damage verification with vision-language understanding

## Project Structure

```
frontend/
├── app/                 # Next.js app router pages
│   ├── api/            # API routes
│   ├── claim/          # Claim management pages
│   └── page.js         # Home page
├── components/         # React components
├── scene_service/      # Python AI services
└── lib/               # Utilities and configurations
```

We propose a two-layer, explainable AI system that replicates an insurance assessor’s reasoning by integrating visual forensics, scene understanding, and language-based cross-verification. The first layer audits uploaded claim photos for tampering, AI-generated content, and scene inconsistencies using pretrained image-forgery and CLIP-based similarity models, producing heatmaps and fraud tags for transparency. The second layer employs a Vision-Language Model to analyze user-provided narratives and correlate them with detected visual evidence to extract consistencies, flag discrepancies, and estimate damage severity and repair cost. Outputs include interpretable overlays and confidence scores rendered in an explainable PDF report. Trained and validated using public datasets such as CASIA2, CompCars, and Car Damage Detection, the system emphasizes modularity, transparency, and efficiency. This architecture improves fraud detection, enhances claim accuracy, and ensures rapid, explainable assessments without relying on proprietary insurer data.
