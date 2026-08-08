---
id: tool-00278
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-youtube-content-creator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/memniwael97-cmyk/ai-youtube-content-creator
created: 2026-07-18
updated: 2026-07-18
no: 278
category: 二、网文 / 长篇 AI 写作系统 库
repo: memniwael97-cmyk/ai-youtube-content-creator
stars: 0
url: https://github.com/memniwael97-cmyk/ai-youtube-content-creator
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
content_hash: 6d10d95be9e89641
  - methods/最强写作方法论_全球最强综合版.md
---

# memniwael97-cmyk/ai-youtube-content-creator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/memniwael97-cmyk/ai-youtube-content-creator
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：Developed a full-stack AI SaaS platform for YouTube creators featuring SEO title generation, script writing, thumbnail ideation, content analysis, user authentication, dashboard analytics, and multi-model AI integration via OpenRouter API.
- **本地描述**：Developed a full-stack AI SaaS platform for YouTube creators featuring SEO title generation, script writing, thumbnail ideation, content analysis, user authentication, dashboard analytics, and multi-model AI integration via OpenRouter API.
- **拉取时间**：2026-07-23 22:47:10

---

# AI YouTube Content Creator

Application SaaS full-stack permettant aux créateurs YouTube de générer automatiquement du contenu optimisé SEO grâce à l'intelligence artificielle.

## Fonctionnalités

- **Générateur de Titres** — 20 titres YouTube SEO avec scores de viralité
- **Générateur de Scripts** — Scripts complets (hook, intro, corps, conclusion, CTA)
- **Générateur de Descriptions** — Descriptions SEO, hashtags et tags YouTube
- **Idées de Miniatures** — 10 concepts visuels avec couleurs et texte overlay
- **Analyse Markdown** — Upload de fichiers `.md` pour générer du contenu YouTube
- **Dashboard** — Statistiques, historique et modèle IA utilisé
- **Multi-modèles IA** — OpenAI GPT, Claude, Gemini, DeepSeek via OpenRouter

## Stack Technique

| Couche | Technologies |
|--------|-------------|
| Frontend | HTML5, CSS3, JavaScript ES6, Tailwind CSS |
| Backend | Node.js, Express.js |
| Base de données | MongoDB, Mongoose |
| Authentification | JWT, bcrypt |
| IA | OpenRouter API |

## Prérequis

- [Node.js](https://nodejs.org/) >= 18
- [MongoDB](https://www.mongodb.com/) (local ou [MongoDB Atlas](https://www.mongodb.com/atlas))
- [Compte OpenRouter](https://openrouter.ai/) avec clé API

## Installation

### 1. Cloner et installer les dépendances

```bash
git clone <votre-repo>
cd ai-youtube-content-creator
npm install
```

### 2. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Éditez `.env` avec vos valeurs :

```env
OPENROUTER_API_KEY=sk-or-v1-votre-cle-ici
MONGODB_URI=mongodb://localhost:27017/ai-youtube-creator
JWT_SECRET=une-chaine-secrete-longue-et-aleatoire
PORT=5000
DEFAULT_AI_MODEL=openai/gpt-4o-mini
NODE_ENV=development
```

### 3. Compiler Tailwind CSS

```bash
npm run build:css
```

### 4. Démarrer MongoDB

**Local :**
```bash
mongod
```

**Ou utilisez MongoDB Atlas** — copiez l'URI de connexion dans `MONGODB_URI`.

### 5. Lancer l'application

```bash
# Mode développement (avec hot reload)
npm run dev

# Mode production
npm start
```

L'application est accessible sur **http://localhost:5000**

## Configuration OpenRouter

1. Créez un compte sur [openrouter.ai](https://openrouter.ai/)
2. Allez dans [Keys](https://openrouter.ai/keys) et créez une clé API
3. Ajoutez des crédits sur [Credits](https://openrouter.ai/credits)
4. Collez la clé dans `OPENROUTER_API_KEY` dans votre `.env`

### Modèles supportés

| Modèle | ID OpenRouter |
|--------|--------------|
| GPT-4o | `openai/gpt-4o` |
| GPT-4o Mini | `openai/gpt-4o-mini` |
| Claude 3.5 Sonnet | `anthropic/claude-3.5-sonnet` |
| Claude 3 Haiku | `anthropic/claude-3-haiku` |
| Gemini Pro 1.5 | `google/gemini-pro-1.5` |
| Gemini Flash 1.5 | `google/gemini-flash-1.5` |
| DeepSeek Chat | `deepseek/deepseek-chat` |
| DeepSeek R1 | `deepseek/deepseek-r1` |

## Configuration MongoDB

### MongoDB Local

```bash
# Windows
net start MongoDB

# macOS (Homebrew)
brew services start mongodb-community

# Linux
sudo systemctl start mongod
```

URI : `mongodb://localhost:27017/ai-youtube-creator`

### MongoDB Atlas (Cloud)

1. Créez un cluster gratuit sur [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Créez un utilisateur de base de données
3. Autorisez votre IP (ou `0.0.0.0/0` pour le dev)
4. Copiez l'URI de connexion :

```
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/ai-youtube-creator
```

## Commandes npm

| Commande | Description |
|----------|-------------|
| `npm install` | Installer les dépendances |
| `npm start` | Démarrer en production |
| `npm run dev` | Démarrer avec nodemon (dev) |
| `npm run build:css` | Compiler Tailwind CSS |

## Structure du Projet

```
project/
├── frontend/
│   ├── pages/          # Pages HTML (login, dashboard, générateurs...)
│   ├── css/            # Tailwind CSS (input.css → styles.css)
│   ├── js/             # api.js, ui.js
│   └── assets/
├── backend/
│   ├── controllers/    # authController, aiController
│   ├── routes/         # authRoutes, aiRoutes
│   ├── services/       # openrouterService, aiService
│   ├── middleware/     # auth, upload, errorHandler
│   ├── models/         # User, Generation
│   ├── config/         # database, index
│   └── server.js
├── uploads/            # Fichiers Markdown uploadés (temporaire)
├── .env
└── README.md
```

## API Endpoints

### Authentification

| Méthode | Route | Description |
|---------|-------|-------------|
| POST | `/api/auth/register` | Inscription |
| POST | `/api/auth/login` | Connexion |
| GET | `/api/auth/profile` | Profil utilisateur |
| PUT | `/api/auth/settings` | Mise à jour paramètres |
| GET | `/api/auth/dashboard` | Stats dashboard |
| GET | `/api/auth/history` | Historique générations |

### IA (authentification requise)

| Méthode | Route | Description |
|---------|-------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| GET | `/api/ai/models` | Liste des modèles |
| POST | `/api/ai/titles` | Générer titres |
| POST | `/api/ai/script` | Générer script |
| POST | `/api/ai/description` | Générer description |
| POST | `/api/ai/thumbnails` | Idées miniatures |
| POST | `/api/ai/hooks` | Hooks d'introduction |
| POST | `/api/ai/video-plan` | Plan de vidéo |
| POST | `/api/ai/markdown/analyze` | Analyser fichier .md |
| POST | `/api/ai/markdown/read` | Lire fichier .md |

## Déploiement

### Backend sur Render

1. Créez un compte sur [render.com](https://render.com)
2. **New → Web Service** → Connectez votre repo GitHub
3. Configuration :
   - **Build Command :** `npm install && npm run build:css`
   - **Start Command :** `npm start`
   - **Environment :** Node
4. Ajoutez les variables d'environnement :
   - `OPENROUTER_API_KEY`
   - `MONGODB_URI` (MongoDB Atlas)
   - `JWT_SECRET`
   - `PORT=5000`
   - `NODE_ENV=production`
5. Déployez — Render fournit une URL `https://votre-app.onrender.com`

### Frontend sur Vercel (optionnel)

Si vous séparez le frontend :

1. Créez un compte sur [vercel.com](https://vercel.com)
2. Importez le dossier `frontend/`
3. Configurez les rewrites pour proxy vers l'API Render :

```json
{
  "rewrites": [
    { "source": "/api/(.*)", "destination": "https://votre-app.onrender.com/api/$1" }
  ]
}
```

> **Note :** Ce projet sert le frontend depuis Express, donc un seul déploiement Render suffit pour tout héberger.

### MongoDB Atlas (Production)

- Utilisez un cluster M0 gratuit pour commencer
- Activez l'authentification et restreignez les IP
- Utilisez une URI avec mot de passe encodé URL

## Sécurité

- Mots de passe hashés avec bcrypt (12 rounds)
- JWT avec expiration 7 jours
- Helmet.js pour les headers HTTP
- Rate limiting (100 req/15min, 10 req/min pour l'IA)
- Validation des entrées avec express-validator
- Filtre de fichiers uploadés (.md uniquement, max 5MB)
- CORS configuré pour la production

## Licence

MIT
