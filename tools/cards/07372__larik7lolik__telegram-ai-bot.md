---
id: tool-07372
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档]
title: telegram-ai-bot
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/larik7lolik/telegram-ai-bot
created: 2026-07-18
updated: 2026-07-18
no: 7372
category: 画龙补充 / 扩容入库 — 补充源
repo: larik7lolik/telegram-ai-bot
stars: 0
url: https://github.com/larik7lolik/telegram-ai-bot
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# larik7lolik/telegram-ai-bot

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/larik7lolik/telegram-ai-bot
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：ai, flux, marketing-automation, python, qwen, siliconflow, telegram-bot, vibecoding, yandex-gpt
- **GitHub 描述**：Полностью автоматизированный Telegram-бот для онлайн-школ. Генерирует премиальный контент (Qwen + FLUX) и публикует по расписанию. Стиль Маркетолога-Вайбкодера.
- **本地描述**：telegram-ai-bot
- **拉取时间**：2026-07-25 19:19:53

---

# Telegram AI-Automation: Маркетолог-Вайбкодер 🚀

Полностью автоматизированный сервис для генерации и публикации премиального контента в Telegram. Бот работает в уникальном стиле «маркетолога-вайбкодера», создавая экспертные посты для онлайн-школ и экспертов.

---

## 🌟 Что делает этот бот?
Бот берет ваш контент-план из CSV-файла и превращает его в профессиональные посты:
1.  **Текст**: Использует ваш готовый текст из контент-плана (с поддержкой **YandexGPT** для генерации новых идей).
2.  **Визуал (gpt-image-1 через ProxyAPI)**: 
    *   Промт собирается локально по заданным правилам.
    *   **gpt-image-1** создаёт вертикальное изображение (9:16) в премиальном стиле.
3.  **Публикация**: Автоматически отправляет готовый пост (фото + текст) в ваш Telegram-канал по расписанию.

---

## 🛠 Технологический стек
*   **Язык**: Python 3.11+
*   **Текстовые модели**: [YandexGPT](https://cloud.yandex.ru/services/yandexgpt) (для текстов) + **Qwen 2.5** (для промтов).
*   **Генерация изображений**: **gpt-image-1** через [ProxyAPI](https://api.proxyapi.ru/).
*   **Инфраструктура**: **Docker** + **Koyeb** (для работы 24/7).
*   **Планировщик**: Модуль `schedule` для публикации в заданное время.

---

## 📋 Инструкция по установке

### 1. Подготовка окружения
```bash
git clone https://github.com/ваш-аккаунт/название-репозитория.git
cd название-репозитория
python -m venv venv
.\venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```

### 2. Настройка ключей (.env)
Создайте файл `.env` и добавьте в него:
```env
# Telegram
TELEGRAM_BOT_TOKEN=ваш_токен
TELEGRAM_CHAT_ID=id_канала

# Yandex Cloud (для текстов)
YANDEX_API_KEY=ваш_ключ
YANDEX_FOLDER_ID=ваш_folder_id

# ProxyAPI (gpt-image-1)
PROXYAPI_OPENAI_KEY=ваш_ключ_proxyapi
SSL_VERIFY=1
```

### 3. Контент-план
Заполните `Контент план.csv`. Бот будет использовать колонки:
*   `Тема` — для поиска конкретного поста.
*   `Идея картинки` — основа для генерации визуала.
*   `Текст поста` — **именно этот текст** будет опубликован.

---

## 🚀 Запуск

### Локальный запуск (один пост):
```bash
python main.py        # Случайный пост из плана
python main.py Кейс   # Пост на конкретную тему
```

### Запуск планировщика (для сервера):
```bash
python scheduler.py
```
*По умолчанию настроено на публикацию в 09:00 и 18:00.*

---

## ☁️ Деплой на Koyeb
1.  Выложите проект на **GitHub** (файл `.gitignore` уже настроен).
2.  В **Koyeb** создайте новый сервис из репозитория.
3.  Добавьте все переменные из `.env` в раздел **Environment Variables**.
4.  Koyeb автоматически соберет проект через `Dockerfile` и запустит `scheduler.py`.

related:
  - methods/QUICK_START.md
---
*Бот создан, чтобы вы могли заниматься продуктом, пока ИИ занимается контентом.*
