---
id: tool-00396
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划]
title: AI-Visual-Synthesis
summary: 搭大纲/分卷/节拍
source: https://github.com/juranhuang4399/ai-visual-synthesis
created: 2026-07-18
updated: 2026-07-18
no: 396
category: 二、网文 / 长篇 AI 写作系统 库
repo: JuranHuang4399/AI-Visual-Synthesis
stars: 0
url: https://github.com/juranhuang4399/ai-visual-synthesis
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# JuranHuang4399/AI-Visual-Synthesis

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/juranhuang4399/ai-visual-synthesis
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A lightweight tool that leverages AI to generate, structure, and refine story ideas — from plot outlines to character arcs — helping writers boost creativity and productivity.
- **本地描述**：A lightweight tool that leverages AI to generate, structure, and refine story ideas — from plot outlines to character arcs — helping writers boost creativity and productivity.
- **拉取时间**：2026-07-23 22:50:41

---

# 🎮 AI Visual Synthesis

AI-powered pixel art character generator with story creation and animation support.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Node.js 18+
- MongoDB (local or Atlas)
- PixelLab API key
- HuggingFace API token

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file:**
   ```bash
   cp .env.example .env  # Or create manually
   ```

5. **Configure environment variables in `.env`:**
   ```env
   # Flask Configuration
   FLASK_APP=app.py
   FLASK_ENV=development
   PORT=5000

   # MongoDB Configuration
   MONGODB_URI=mongodb://localhost:27017/ai-visual-synthesis

   # API Keys
   PIXELLAB_API_KEY=your_pixellab_api_key_here
   HUGGINGFACE_API_TOKEN=your_huggingface_token_here

   # Storage Configuration
   STORAGE_BASE_PATH=./storage/directories
   STATIC_URL_PREFIX=/static
   ```

6. **Start the backend server:**
   ```bash
   python app.py
   ```

   Backend will run at: **http://localhost:5000**

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create `.env` file (optional, defaults to localhost:5000):**
   ```env
   VITE_API_URL=http://localhost:5000
   ```

4. **Start the development server:**
   ```bash
   npm run dev
   ```

   Frontend will run at: **http://localhost:5173**

## 📋 For Developers

### Project Architecture

**Backend (Flask):**
- **Framework:** Flask 3.0+ with RESTful API
- **Database:** MongoDB with MongoEngine ODM
- **External APIs:** PixelLab (pixel art generation), HuggingFace (story generation)
- **Storage:** Local file system for images and GIFs
- **Structure:**
  - `app.py` - Application entry point
  - `api/v1/routes/` - API route handlers
  - `core/services/` - Business logic layer
  - `integrations/clients/` - External API clients
  - `database/models/` - MongoDB models
  - `storage/` - File management and ZIP generation
  - `utils/` - Utilities (GIF generation, validators, exceptions)

**Frontend (React):**
- **Framework:** React 19 + Vite
- **Styling:** Tailwind CSS v3 with custom cyberpunk theme
- **Routing:** React Router 6
- **Structure:**
  - `pages/` - Main page components
  - `components/` - Reusable components organized by feature
    - `common/` - Shared components (PageLayout, NavBar, BackButton, AnimatedBackground)
    - `create/` - Character creation form components
    - `character/` - Character display components
    - `result/` - Result display components
    - `home/` - Homepage components
    - `login/` - Login page components

### Key Features

**Character Generation:**
- 8-directional sprite generation (north, south, east, west, and diagonals)
- Character DNA extraction for consistency
- Master Reference Image strategy for animation consistency
- Automatic GIF generation for rotating sprites

**Animation System:**
- Support for multiple animation types (walk, run, jump, attack)
- Direction-based animation generation
- Automatic GIF creation for animation sequences
- Frame-by-frame animation management

**Story Generation:**
- AI-powered story generation using Meta Llama (HuggingFace)
- Character-based narrative creation
- Story display and management

**Download & Export:**
- Individual image downloads
- Complete character package export (images + story)
- ZIP file generation with organized folder structure

## 📅 Project Status

### ✅ Completed Features

**Backend:**
- ✅ Flask RESTful API with MongoDB integration
- ✅ PixelLab API integration for pixel art generation
- ✅ HuggingFace API integration for story generation
- ✅ 8-directional character sprite generation
- ✅ Animation frame generation (walk, run, jump, attack)
- ✅ GIF generation and optimization
- ✅ Character consistency system (Character DNA + Master Reference Image)
- ✅ File storage and management
- ✅ ZIP export functionality
- ✅ Error handling and retry mechanisms
- ✅ CORS configuration
- ✅ Static file serving

**Frontend:**
- ✅ React 19 + Vite + Tailwind CSS v3
- ✅ Cyberpunk/neon design theme
- ✅ React Router 6 navigation
- ✅ HomePage with hero, features, showcase, and footer
- ✅ Character creation page with form and result display
- ✅ Characters gallery page
- ✅ Character detail page with sprite preview and direction frames
- ✅ Profile page
- ✅ Login page
- ✅ Reusable components (PageLayout, FormField, etc.)
- ✅ Animated background system
- ✅ Image rotation display
- ✅ Story display component
- ✅ Download and export functionality

**Code Quality:**
- ✅ All comments translated to English
- ✅ Removed unused code and files
- ✅ Improved component reusability
- ✅ Optimized performance (GPU acceleration, lazy loading)

---

## 🏗️ Project Structure

```
AI-Visual-Synthesis/
├── frontend/                           # React Frontend
│   ├── src/
│   │   ├── pages/                     # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── CreateResultPage.jsx
│   │   │   ├── CharactersPage.jsx
│   │   │   ├── CharacterDetailPage.jsx
│   │   │   ├── ProfilePage.jsx
│   │   │   └── LoginPage.jsx
│   │   ├── components/                # Reusable components
│   │   │   ├── common/                # Shared components
│   │   │   │   ├── PageLayout.jsx     # Layout wrapper
│   │   │   │   ├── NavBar.jsx
│   │   │   │   ├── BackButton.jsx
│   │   │   │   └── AnimatedBackground.jsx
│   │   │   ├── create/                # Character creation
│   │   │   │   ├── CharacterForm.jsx
│   │   │   │   ├── FormField.jsx       # Unified form field
│   │   │   │   └── GenerateButton.jsx
│   │   │   ├── character/             # Character display
│   │   │   │   └── CharacterCard.jsx
│   │   │   ├── result/                # Result display
│   │   │   │   ├── RotatingCharacter.jsx
│   │   │   │   ├── StoryDisplay.jsx
│   │   │   │   ├── ImageGrid.jsx
│   │   │   │   └── ActionButtons.jsx
│   │   │   ├── home/                  # Homepage components
│   │   │   └── login/                 # Login components
│   │   ├── App.jsx                    # Main app component
│   │   └── index.css                  # Global styles
│   └── package.json
│
└── backend/                            # Flask Backend
    ├── app.py                         # Application entry point
    ├── config.py                      # Configuration management
    ├── requirements.txt               # Python dependencies
    ├── api/                           # API layer
    │   ├── v1/
    │   │   └── routes/                # API route handlers
    │   │       ├── character_routes.py
    │   │       ├── download_routes.py
    │   │       ├── gallery_routes.py
    │   │       └── health_routes.py
    │   └── middleware/                # Middleware
    │       ├── cors.py
    │       └── error_handler.py
    ├── core/                          # Business logic
    │   └── services/
    │       ├── generation_service.py  # Character generation
    │       ├── character_service.py   # Character CRUD
    │       └── gif_service.py         # GIF generation
    ├── database/                      # Database layer
    │   ├── models/                    # MongoDB models
    │   │   ├── character_model.py
    │   │   └── user_model.py
    │   ├── repositories/              # Data access layer
    │   └── connection.py              # DB connection
    ├── integrations/                  # External API clients
    │   └── clients/
    │       ├── pixellab_client.py     # PixelLab API
    │       └── meta_llama_client.py   # HuggingFace API
    ├── storage/                       # File management
    │   ├── file_manager.py
    │   ├── zip_generator.py
    │   └── directories/               # Generated files
    └── utils/                         # Utilities
        ├── gif_generator.py
        ├── exceptions.py
        ├── validators.py
        └── logger.py
```

---

### Development Workflow

1. **Start MongoDB** (if using local instance):
   ```bash
   mongod
   ```

2. **Start Backend:**
   ```bash
   cd backend
   source venv/bin/activate
   python app.py
   ```

3. **Start Frontend** (in a new terminal):
   ```bash
   cd frontend
   npm run dev
   ```

4. **Access the application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:5000
   - API Health Check: http://localhost:5000/api/v1/health

### Available Pages

- `/` - Home page with hero, features, and showcase
- `/create` - Character creation form and result display
- `/characters` - Gallery of all saved characters
- `/characters/:id` - Character detail page with sprite preview and direction frames
- `/profile` - User profile page
- `/login` - Login page

---

## 🎨 Design Theme

**Cyberpunk / Neon Style**

- Dark backgrounds: `#0a0e27`, `#1a1a2e`
- Neon pink: `#ff006e`
- Neon cyan: `#00d9ff`
- Neon purple: `#bd00ff`
- Grid background pattern
- Glow effects on hover

---

## 🛠️ Development Guidelines

### Code Style

- **Backend:** Follow PEP 8 Python style guide
- **Frontend:** Use ESLint and Prettier for code formatting
- **Comments:** All code comments should be in English
- **Naming:** Use descriptive, camelCase for variables, PascalCase for components

### Component Reusability

- Use `PageLayout` component for consistent page structure
- Use `FormField` component for all form inputs (text and textarea)
- Extract common patterns into reusable components
- Keep components focused and single-purpose

### API Integration

- All API calls should include proper error handling
- Use retry mechanisms for external API calls (rate limits)
- Implement loading states for async operations
- Provide user feedback for all actions

### File Organization

- Group related components in feature folders
- Keep utility functions in `utils/` directory
- Store API clients in `integrations/clients/`
- Maintain clear separation between layers (routes → services → repositories)

---

## 📡 API Endpoints

### Character Management

```
POST   /api/v1/characters/generate
  Body: {
    name: string,
    characterClass: string,
    personality: string,
    appearance: string,
    specialFeatures: string,
    selectedAnimations?: string[],
    selectedDirections?: object
  }
  Response: {
    id: string,
    name: string,
    images: [{url: string, direction: string, angle: string}],
    story: string,
    status: string
  }

GET    /api/v1/characters              # Get all characters (with filters)
GET    /api/v1/characters/:id          # Get specific character
PUT    /api/v1/characters/:id          # Update character
DELETE /api/v1/characters/:id          # Delete character
POST   /api/v1/characters/:id/save     # Save character to gallery
```

### Animation Management

```
POST   /api/v1/characters/:id/animations/:type/directions/:direction/generate
  Response: {
    frames: [{url: string, frame_index: int, gif_url?: string}],
    gif_url: string
  }

DELETE /api/v1/characters/:id/animations/:type
DELETE /api/v1/characters/:id/animations/:type/directions/:direction
```

### Download & Export

```
GET    /api/v1/characters/:id/download/images      # Download images ZIP
GET    /api/v1/characters/:id/download/gif         # Download GIF
GET    /api/v1/characters/:id/download/all         # Download all (images + GIF + story)
GET    /api/v1/characters/:id/download/export      # Complete export package
GET    /api/v1/characters/:id/images/direction/:direction  # Download single direction image
```

### Gallery

```
GET    /api/v1/gallery                    # Get gallery characters
GET    /api/v1/gallery/user/:user_id      # Get user's gallery
```

### Health Check

```
GET    /api/v1/health                     # API health check
GET    /api/v1/health/db                  # Database health check
```

---

## 🗄️ Data Models

### User Model

```python
{
  username: String,
  email: String,
  password: String (hashed),
  createdAt: DateTime,
  updatedAt: DateTime
}
```

### Character Model

```python
{
  user_id: ObjectId (ref: User, optional),
  name: String (required),
  description: String,
  status: String (pending/generating/completed/failed),
  input_params: Dict {
    name: String,
    characterClass: String,
    personality: String,
    appearance: String,
    specialFeatures: String,
    selectedAnimations: List,
    selectedDirections: Dict
  },
  metadata: Dict {
    character_dna: String,              # Fixed character DNA prompt
    master_reference_path: String,       # Master reference image path
    master_reference_direction: String   # Usually "south"
  },
  images: List[Dict] {
    url: String,
    path: String,
    direction: String,
    angle: String,
    index: Integer
  },
  story: Dict {
    content: String,
    generated_at: DateTime,
    prompt: String
  },
  gif: Dict {
    url: String,
    path: String,
    duration: Integer,
    frame_count: Integer,
    created_at: DateTime
  },
  animations: Dict {
    "walk": {
      "south": [{
        url: String,
        path: String,
        frame_index: Integer,
        gif_url: String (optional)
      }],
      ...
    },
    "run": {...},
    "jump": {...},
    "attack": {...}
  },
  created_at: DateTime,
  updated_at: DateTime,
  view_count: Integer
}
```

---

## 🔧 Environment Variables

### Frontend (.env)

```env
VITE_API_URL=http://localhost:5000
```

### Backend (.env)

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
PORT=5000

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/ai-visual-synthesis

# API Keys
PIXELLAB_API_KEY=your_pixellab_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here

# Storage Configuration
STORAGE_BASE_PATH=./storage/directories
STATIC_URL_PREFIX=/static
IMAGES_DIR=generated/images
GIFS_DIR=generated/gifs

# CORS Configuration
FRONTEND_URL=http://localhost:5173
```

### Required API Keys

1. **PixelLab API Key:**
   - Sign up at https://pixellab.ai
   - Get your API key from the dashboard
   - Used for pixel art generation and animation

2. **HuggingFace API Token:**
   - Sign up at https://huggingface.co
   - Create an access token with read permissions
   - Used for story generation via Meta Llama

---

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check MongoDB is running
- Verify all environment variables are set in `.env`
- Ensure virtual environment is activated
- Check port 5000 is not in use

**Frontend can't connect to backend:**
- Verify backend is running on port 5000
- Check `VITE_API_URL` in frontend `.env`
- Check CORS configuration in backend

**Character generation fails:**
- Verify PixelLab API key is valid and has credits
- Check API rate limits
- Review backend logs for detailed error messages

**Images not displaying:**
- Check static file serving is configured correctly
- Verify image paths in database
- Check browser console for 404 errors

**GIF generation issues:**
- Ensure Pillow is installed correctly
- Check file permissions for storage directory
- Verify GIF frames are properly sorted

## 📚 Technical Details

### Character Consistency Strategy

The system uses a "Character DNA" approach to maintain consistency:

1. **Character DNA Extraction:** Fixed prompt extracted from initial generation
2. **Master Reference Image:** South-facing standing pose used as reference
3. **Locked Parameters:** 
   - `image_guidance_scale=2.2`
   - `init_image_strength=300.0`
   - `image_size=64x64`
4. **Consistent Prompts:** All animations use the same Character DNA with action-specific additions

### Animation Generation Flow

1. User selects animation type and directions
2. System retrieves Master Reference Image from character metadata
3. For each direction:
   - Generate 4 frames using PixelLab `animate_with_text` API
   - Use fixed Character DNA + action description
   - Apply locked consistency parameters
4. Automatically generate GIF from frames
5. Store frames and GIF in character animations data

### File Storage Structure

```
storage/directories/
├── generated/
│   ├── images/
│   │   └── {character_id}/
│   │       ├── {direction}_{index}.png
│   │       └── {animation_type}/
│   │           └── {direction}/
│   │               ├── frame_{index}.png
│   │               └── {animation_type}_{direction}.gif
│   └── gifs/
│       └── {character_id}.gif
```

## 🔗 Useful Links

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5000
- **API Health Check:** http://localhost:5000/api/v1/health
- **PixelLab API:** https://pixellab.ai
- **HuggingFace:** https://huggingface.co

## 📝 Notes

- Character images are stored locally (can be migrated to cloud storage, eg.Cloudinary)
- GIF generation uses Pillow with optimized settings to prevent ghosting
- The system includes retry mechanisms for API rate limits
- All API responses include proper error handling

---

**Last Updated:** December 2025  
**Frontend Status:** ✅ Complete and optimized  
**Backend Status:** ✅ Complete and production-ready

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
