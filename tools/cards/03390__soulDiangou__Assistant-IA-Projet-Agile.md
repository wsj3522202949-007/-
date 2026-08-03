---
id: tool-03390
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档]
title: Assistant-IA-Projet-Agile
summary: 剧本/短剧脚本生成
source: https://github.com/souldiangou/assistant-ia-projet-agile
created: 2026-07-18
updated: 2026-07-18
no: 3390
category: 十、短剧 / 剧本 / 影视化生成 库
repo: soulDiangou/Assistant-IA-Projet-Agile
stars: 0
url: https://github.com/souldiangou/assistant-ia-projet-agile
tier: "C"
use_case: "剧本/短剧脚本生成"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/模板库.md
---

# soulDiangou/Assistant-IA-Projet-Agile

- **分类**：十、短剧 / 剧本 / 影视化生成 库
- **链接**：https://github.com/souldiangou/assistant-ia-projet-agile
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Application web complète qui assiste les équipes Agile grâce à l'IA : génération de user stories, cas de test, scripts Robot Framework et rapports de test.
- **本地描述**：Application web complète qui assiste les équipes Agile grâce à l'IA : génération de user stories, cas de test, scripts Robot Framework et rapports de test.
- **拉取时间**：2026-07-23 23:54:02

---

# Assistant IA dans projet Agile

Application web complète qui assiste les équipes Agile grâce à l'IA :
génération de user stories, cas de test, scripts Robot Framework et rapports de test.

## Fonctionnalités

| Feature | Description |
|---------|----------related:
  - methods/模板库.md
---|
| User Stories | Génération avec priorisation MoSCoW |
| Cas de test | Génération structurée (max 15 par user story) |
| Scripts Robot | Génération de fichiers `.robot` automatisés |
| Rapport de test | PV de test complet avec analyse et recommandations |
| Exports | JSON, CSV, Markdown, Texte, Jira, Xray, PDF |
| Providers IA | OpenAI, Anthropic, Azure OpenAI, Ollama (local) |

## Installation

```bash
# 1. Cloner / copier le projet
cd agile-ai-assistant

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python app.py
```

L'interface est disponible sur **http://localhost:8000**

## Configuration des providers

### OpenAI
1. Allez dans **Configuration IA** → sélectionnez **OpenAI**
2. Entrez votre clé API (`sk-...`)
3. Choisissez le modèle (GPT-4o recommandé)
4. Cliquez **Sauvegarder**, puis **Tester la connexion**

### Anthropic
1. Sélectionnez **Anthropic**
2. Entrez votre clé API Anthropic
3. Choisissez le modèle (Claude Sonnet 4.6 recommandé)

### Azure OpenAI
1. Sélectionnez **Azure OpenAI**
2. Renseignez : Clé API, Endpoint, Nom du déploiement, Version API

### Ollama (local, gratuit)
1. Installez Ollama : https://ollama.com
2. Téléchargez un modèle : `ollama pull llama3`
3. Sélectionnez **Ollama (Local)** dans l'app
4. Cliquez **Récupérer les modèles** pour lister les modèles disponibles

## Structure du projet

```
.
├── app.py                  # Point d'entrée
├── requirements.txt
├── config.json             # Config générée automatiquement
├── backend/
│   ├── llm/                # Couche d'abstraction LLM
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── openai_provider.py
│   │   ├── anthropic_provider.py
│   │   ├── azure_provider.py
│   │   └── ollama_provider.py
│   ├── routes/             # Endpoints FastAPI
│   └── exporters/          # Formatters et générateur PDF
└── frontend/
    ├── index.html
    ├── css/style.css
    └── js/                 # Logique frontend par page
```

## Exemple d'utilisation

1. **Configurer** : Renseignez votre clé OpenAI ou lancez Ollama
2. **User Stories** : Décrivez votre besoin → obtenez des user stories MoSCoW
3. **Cas de test** : Collez une user story → obtenez jusqu'à 15 cas de test
4. **Robot Framework** : Importez les cas de test → obtenez un script `.robot`
5. **Rapport** : Collez vos résultats → obtenez un PV de test complet
