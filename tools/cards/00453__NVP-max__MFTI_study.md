---
id: tool-00453
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: MFTI_study
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nvp-max/mfti_study
created: 2026-07-18
updated: 2026-07-18
no: 453
category: 二、网文 / 长篇 AI 写作系统 库
repo: NVP-max/MFTI_study
stars: 0
url: https://github.com/nvp-max/mfti_study
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 25f68c99b7bef913
  - methods/最强写作方法论_全球最强综合版.md
---

# NVP-max/MFTI_study

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nvp-max/mfti_study
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Educational project to learn:  Web scraping basics with requests and BeautifulSoup: page navigation and HTML parsing.  Task automation with schedule.  Git workflow and project organization on GitHub.  Writing and running simple unit tests with pytestю
- **本地描述**：Educational project to learn:  Web scraping basics with requests and BeautifulSoup: page navigation and HTML parsing.  Task automation with schedule.  Git workflow and project organization on GitHub.  Writing and running simple unit tests with pytestю
- **拉取时间**：2026-07-23 22:52:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# HW_3: Books Parser

## Цель проекта
Учебный проект для освоения web-scraping и автоматизации задач.  
Собирает данные о книгах с сайта [Books to Scrape](http://books.toscrape.com).

## Инструкции по запуску
1. Клонировать репозиторий:
git clone <URL_репозитория>
cd HW_3

2. Создать и активировать виртуальное окружение:
python -m venv venv
# Git Bash
source venv/Scripts/activate
# Windows CMD
venv\Scripts\activate

3. Установить зависимости:
pip install -r requirements.txt

4. Запустить скрипт:
python scraper.py

5. Запустить автотесты:
pytest tests/

### Используемые библиотеки
- requests — HTTP-запросы  
- beautifulsoup4 — парсинг HTML  
- schedule — автоматизация задач по расписанию  
- pytest — юнит-тестирование

