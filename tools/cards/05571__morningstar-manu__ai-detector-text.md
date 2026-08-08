---
id: tool-05571
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 需API密钥, 英文文档]
title: ai-detector-text
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/morningstar-manu/ai-detector-text
created: 2026-07-18
updated: 2026-07-18
no: 5571
category: 一、去 AI 味 / Humanizer 库
repo: morningstar-manu/ai-detector-text
stars: 0
url: https://github.com/morningstar-manu/ai-detector-text
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8b85d759e653afa4
  - methods/改稿润色指令库.md
---

# morningstar-manu/ai-detector-text

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/morningstar-manu/ai-detector-text
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：morningstar-manu/ai-detector-text
- **拉取时间**：2026-07-25 18:23:37

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Analyzer

Application SaaS pour detecter si un texte est genere par une IA et proposer une version humanisee.

## Architecture

- `apps/api`: backend FastAPI avec endpoints REST
- `apps/web`: frontend Next.js (React + TypeScript + TailwindCSS)

## Fonctionnalites

- Detection IA hybride (heuristiques + analyse LLM)
- Score de probabilite (0-100), classification, explication
- Humanisation du texte avec styles:
  - professionnel
  - conversationnel
  - academique
  - creatif
- Mode comparaison avant/apres
- Heatmap de score par phrase
- Suppression des caracteres invisibles (souvent utilises pour brouiller la detection IA)

## Endpoints API

### POST `/detect`

Request:

```json
{
  "text": "Votre texte ici..."
}
```

Response:

```json
{
  "score": 72,
  "classification": "IA probable",
  "explanation": "Explication...",
  "heuristics": {
    "avg_sentence_length": 19.5,
    "repetition_rate": 0.13,
    "lexical_diversity": 0.58
  },
  "sentence_scores": [
    { "sentence": "Phrase 1", "score": 80 }
  ]
}
```

### POST `/humanize`

Request:

```json
{
  "text": "Votre texte ici...",
  "style": "conversationnel"
}
```

### POST `/sanitize`

Request:

```json
{
  "text": "Texte contenant potentiellement des caracteres invisibles..."
}
```

Response:

```json
{
  "cleaned_text": "Texte nettoye...",
  "removed_count": 3,
  "found_characters": ["ZERO WIDTH SPACE (U+200B)"]
}
```

Response:

```json
{
  "humanized_text": "Texte re-ecrit...",
  "style": "conversationnel",
  "notes": "Texte re-ecrit en style conversationnel."
}
```

## Lancer le backend

```bash
cd apps/api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```

## Lancer le frontend

```bash
cd apps/web
npm install
copy .env.example .env.local
npm run dev
```

Frontend: `http://localhost:3000`  
Backend: `http://localhost:8000`

## Exemples de requetes

```bash
curl -X POST http://localhost:8000/detect -H "Content-Type: application/json" -d "{\"text\":\"Texte a analyser...\"}"
```

```bash
curl -X POST http://localhost:8000/humanize -H "Content-Type: application/json" -d "{\"text\":\"Texte a re-ecrire...\", \"style\":\"professionnel\"}"
```

## Notes

- Si `OPENAI_API_KEY` est absent, l'API fonctionne en mode degrade:
  - detection avec score LLM neutre
  - humanisation retourne le texte original

## Deploiement Heroku (backend FastAPI)

Ce repo est un monorepo. Pour Heroku, la racine contient deja:

- `requirements.txt` (redirige vers `apps/api/requirements.txt`)
- `Procfile` (demarre Uvicorn depuis `apps/api`)
- `runtime.txt` (version Python)

Commandes:

```bash
heroku create ai-text-analyzer-api
heroku config:set OPENAI_API_KEY=ton_api_key
git push heroku main
heroku open
```

Test rapide:

```bash
curl https://ai-text-analyzer-api.herokuapp.com/health
```

Si tu veux aussi deployer le frontend Next.js sur Heroku, cree une deuxieme app Heroku dediee a `apps/web` (Node.js buildpack) ou deploie le front sur Vercel.

### Deployer le frontend `apps/web` sur Heroku (app separee)

Le plus simple en monorepo est d'utiliser le buildpack monorepo + Node.js.

```bash
heroku create ai-text-analyzer-web
heroku buildpacks:clear -a ai-text-analyzer-web
heroku buildpacks:add -a ai-text-analyzer-web https://github.com/timanovsky/subdir-heroku-buildpack
heroku buildpacks:add -a ai-text-analyzer-web heroku/nodejs
heroku config:set -a ai-text-analyzer-web PROJECT_PATH=apps/web
heroku config:set -a ai-text-analyzer-web NEXT_PUBLIC_API_URL=https://ai-text-analyzer-api.herokuapp.com
git push heroku main
heroku open -a ai-text-analyzer-web
```

Notes:

- Le backend et le frontend doivent etre 2 apps Heroku distinctes.
- Dans `apps/web/package.json`, le script `start` est compatible Heroku (`next start -p $PORT -H 0.0.0.0`).

## CI/CD GitHub Actions -> Heroku (backend + frontend)

Le workflow est pret dans `.github/workflows/ci-cd-heroku.yml`.

Declenchement:

- `push` sur `main`
- execution manuelle via `workflow_dispatch`

Etapes:

1. Build checks (Python + Next.js)
2. Deploy backend Heroku (`apps/api`)
3. Deploy frontend Heroku (`apps/web`)

Secrets GitHub a ajouter dans `Settings -> Secrets and variables -> Actions`:

- `HEROKU_API_KEY`
- `HEROKU_EMAIL`
- `HEROKU_BACKEND_APP_NAME`
- `HEROKU_FRONTEND_APP_NAME`

Variables Heroku recommandees:

- app backend:
  - `OPENAI_API_KEY`
- app frontend:
  - `NEXT_PUBLIC_API_URL=https://<backend-app>.herokuapp.com`
