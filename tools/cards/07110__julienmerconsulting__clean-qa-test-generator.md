---
id: tool-07110
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档]
title: clean-qa-test-generator
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/julienmerconsulting/clean-qa-test-generator
created: 2026-07-18
updated: 2026-07-18
no: 7110
category: 画龙补充 / 扩容入库 — 补充源
repo: julienmerconsulting/clean-qa-test-generator
stars: 3
url: https://github.com/julienmerconsulting/clean-qa-test-generator
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# julienmerconsulting/clean-qa-test-generator

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/julienmerconsulting/clean-qa-test-generator
- **Stars**：3
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Generate professional automated tests from User Stories — 10 frameworks, 7 AI providers — PySide6 desktop app
- **本地描述**：Generate professional automated tests from User Stories — 10 frameworks, 7 AI providers — PySide6 desktop app
- **拉取时间**：2026-07-25 19:11:10

---

# 🧪 Clean QA Test Generator

**Génère des tests automatisés professionnels à partir de User Stories en quelques secondes.**

Une application desktop PySide6 qui transforme vos User Stories en code de test prêt à l'emploi, en utilisant les meilleures pratiques Clean QA.

<img src="screenshots/app_screenshot.png" width="800">

---

## ✨ Features

- 🚀 **Génération en 2 temps** : Page Object + Tests séparés puis mergés
- 🎯 **10 frameworks supportés** : Playwright, Cypress, Appium (Java/JS), Katalon, Selenium, Robot Framework, Karate, Cucumber
- 🔑 **Multi-providers IA** : OpenAI, Anthropic, Mistral, Groq, Cerebras, Gemini, Ollama (local)
- 💾 **Clés API depuis ENV** : Charge automatiquement vos clés depuis les variables d'environnement
- 🎨 **UI moderne** : Dark theme One Dark, coloration syntaxique
- ⚙️ **Paramétrable** : Température, max tokens, modèle personnalisable
- 📋 **Export facile** : Copier ou sauvegarder le code généré

---

## 🖥️ Frameworks supportés

| Framework | Langage | Type |
|-----------|---------|------|
| Playwright | TypeScript | Web |
| Cypress | JavaScript | Web |
| Selenium | Java | Web |
| Robot Framework | Robot | Web |
| Karate | Karate DSL | API/Web |
| Cucumber | Gherkin | BDD |
| Katalon | Groovy | Web/Mobile |
| Appium (Java) | Java | Mobile |
| Appium (JavaScript) | JS/WebdriverIO | Mobile |

---

## 📦 Installation

### Prérequis

- **Python 3.12+** (requis pour PySide6)
- Une clé API (OpenAI, Anthropic, Mistral, Groq, Cerebras, ou Gemini)

### Installation

```bash
# Cloner le repo
git clone https://github.com/julienmerconsulting/clean-qa-test-generator.git
cd clean-qa-test-generator

# Installer les dépendances
pip install -r requirements.txt

# Configurer vos clés API (optionnel - peut être fait dans l'app)
cp .env.example .env
# Éditer .env avec vos clés
```

### Lancer l'application

```bash
python clean_qa_generator.py
```

---

## 🔑 Configuration des clés API

L'application charge automatiquement les clés depuis vos variables d'environnement :

| Provider | Variable d'environnement |
|----------|--------------------------|
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Mistral | `MISTRAL_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Cerebras | `CEREBRAS_API_KEY` |
| Gemini | `GEMINI_API_KEY` |
| Ollama | Pas de clé nécessaire |

Vous pouvez aussi entrer la clé directement dans l'interface.

---

## 📝 Comment écrire une bonne User Story

Plus votre User Story est détaillée, meilleur sera le code généré.

### Exemple Web (SauceDemo)

```
En tant qu'utilisateur de saucedemo.com
Je veux me connecter avec mes identifiants
Afin d'accéder au catalogue produits

Critères d'acceptation:
- Username: standard_user
- Password: secret_sauce
- Redirection vers /inventory.html si OK
- Message "Username and password do not match" si KO
- Bouton LOGIN désactivé si champs vides
```

### Exemple Mobile (App bancaire)

```
En tant qu'utilisateur de l'app mobile BankApp
Je veux me connecter avec mon email et code PIN
Afin d'accéder à mes comptes

Application: BankApp.apk
Package: com.mybank.app

Sélecteurs (accessibility IDs):
- ~input_email
- ~input_pin  
- ~btn_login
- ~txt_error
- ~screen_dashboard

Critères d'acceptation:
- Email valide format xxx@xxx.xx
- Code PIN 4 chiffres
- Message "Email ou PIN incorrect" si KO
- Message "Email requis" si email vide
- Message "PIN requis" si PIN vide
- Redirection vers dashboard si OK
```

---

## 🎯 Résultat généré

L'application génère du code **prêt à l'emploi** avec :

✅ **Page Object Pattern** - Structure propre et maintenable  
✅ **Fluent Interface** - Chaînage des méthodes (`return this`)  
✅ **Waits explicites** - Pas de `sleep()`, vrais waits  
✅ **Helpers privés** - `waitAndClear()`, `waitAndClick()`  
✅ **Tests par règle métier** - Commentaires `// Testing rule #X - happy/unhappy`  
✅ **Setup/Teardown** - `beforeEach`, `afterEach` appropriés  

---

## 🏗️ Architecture

```
User Story + Framework choisi
        ↓
[Détection terminologie framework]
        ↓
[Appel 1] → Prompt Page Object → LLM → Page Object généré
        ↓
[Appel 2] → Prompt Tests + Page Object → LLM → Tests générés
        ↓
[Merge] → Code complet retourné
```

---

## 💡 Tips

- **Soyez précis** : Incluez les vrais sélecteurs CSS/XPath/Accessibility IDs si vous les connaissez
- **Listez les critères** : Chaque critère d'acceptation = un test généré
- **Précisez les messages** : Les messages d'erreur exacts seront utilisés dans les assertions
- **Pour mobile** : Ajoutez les accessibility IDs avec le préfixe `~`

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amazing-feature`)
3. Commit vos changements (`git commit -m 'Add amazing feature'`)
4. Push sur la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

---

## 📄 License

MIT License - voir `[LICENSE](LICENSE)` pour plus de détails.

---

## 👨‍💻 Auteur

**Julien Mer** - Clean QA Academy

- 🌐 Newsletter : [Bonnes Pratiques QA](https://www.linkedin.com/newsletters/bonnes-pratiques-qa-6878703775620636672/)
- 💼 LinkedIn : [Julien Mer](https://www.linkedin.com/in/julienmer/)
- 🏢 Consulting : JMer Consulting - Top Partner Katalon Europe

---

## ⭐ Support

Si ce projet vous aide, pensez à lui donner une ⭐ sur GitHub !

related:
  - methods/QUICK_START.md
---

*Built with ❤️ and 20+ years of QA experience*
