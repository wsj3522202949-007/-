---
id: tool-00486
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 需API密钥, 英文文档]
title: InteractiveStoryGeneratingChatBot
summary: 互动叙事/聊天写故事
source: https://github.com/bocchitheprog/interactivestorygeneratingchatbot
created: 2026-07-18
updated: 2026-07-18
no: 486
category: 二、网文 / 长篇 AI 写作系统 库
repo: BocchiTheProg/InteractiveStoryGeneratingChatBot
stars: 0
url: https://github.com/bocchitheprog/interactivestorygeneratingchatbot
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# BocchiTheProg/InteractiveStoryGeneratingChatBot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bocchitheprog/interactivestorygeneratingchatbot
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Python ChatBot (Assistant) for creating (generating) stories, build with RASA framework (NLP engine), which uses a composable set of primitives for natural language understanding (NLU) and dialogue management, also using Generative AI API Groq for text generation.
- **本地描述**：Python ChatBot (Assistant) for creating (generating) stories, build with RASA framework (NLP engine), which uses a composable set of primitives for natural language understanding (NLU) and dialogue management, also using Generative AI API Groq for text generation.
- **拉取时间**：2026-07-23 22:53:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Інтерактивний чат-бот для генерації історій



## Опис проєкту



Цей проєкт розроблений для створення інтерактивного чат-бота, який генерує історії на основі запитів користувачів. Бот здатен розпочинати нові історії, продовжувати поточні та оновлювати їх за допомогою заданих користувачем параметрів. Для зберігання розмов використовується база даних MySQL. 



## Можливості бота



- Розпізнавання та відповідь на привітання користувачів.

- Генерація нових історій за запитами користувачів.

- Продовження та оновлення існуючих історій.

- Збереження розмов в базу даних після отримання дозволу від користувача.

- Відображення зображень, якщо це потрібно для відповіді бота.



## Вимоги до системи



- Python 3.7 або вище

- MySQL

- RASA

- Groq API



## Встановлення



### Крок 1: Клонування репозиторію



```bash

git clone https://github.com/BocchiTheProg/InteractiveStoryGeneratingChatBot

```



### Наступні етапи встановлення краще виконувати у віртуальному середовищі (venv)



### Крок 2: Встановлення RASA



```bash

pip3 install rasa

```



### Крок 3: Встановлення mysql-connector



```bash

pip3 install mysql-connector

```



### Крок 4: Встановлення Groq API



```bash

pip install groq

```

P.S. Не забудьте встановити змінну середовища GROQ_API_KEY з вашим ключем від Groq API



## Створення моделі (її навчання)



- Переходимо в папку Bot та в ній створюємо директорію ***models***

- Знаходячись в папці Bot, з термінала виконуємо наступну команду 



```bash

rasa train

```

- Чекаємо на завершення, після чого архів моделі з'явиться у створеній папці



## Запуск



### Крок 1: Запуск спеціальних дій



Переходимо в папку Bot проєкту та з неї в терміналі виконуємо наступну команду



```bash

rasa run actions

```



### Крок 2: Запуск RASA сервера



З іншого терміналу, з тієї ж папки, виконуємо наступну команду



```bash

rasa run --enable-api --cors "*"

```



### Крок 3: Запуск локального сервера



З іншого терміналу, повертаючись до кореневої папки проєкту (де знаходиться файл index), виконуємо наступну команду



```bash

 python -m http.server

```



### Крок 4: Спілкуємось з ботом



Заходимо в браузер та переходимо за наступною веб-адресою



```bash

 localhost:8000

```



Після цього маємо побачити діалогове вікно для розмови.



![alt-text](./screenshots/demo-photo.png)

