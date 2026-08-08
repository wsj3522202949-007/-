---
id: tool-05335
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: BiasBuster
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/artem-kornilov-pro/biasbuster
created: 2026-07-18
updated: 2026-07-18
no: 5335
category: 一、去 AI 味 / Humanizer 库
repo: Artem-Kornilov-pro/BiasBuster
stars: 4
url: https://github.com/artem-kornilov-pro/biasbuster
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f92d7ea75f98a7f5
  - methods/改稿润色指令库.md
---

# Artem-Kornilov-pro/BiasBuster

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/artem-kornilov-pro/biasbuster
- **Stars**：4
- **语言**：Python
- **License**：MIT
- **Topics**：ai-safety, chrome-extension, compound-ai-system, langgraph, llm
- **GitHub 描述**：Compound AI system for detecting cognitive biases in text. 7 bias detectors. Generates counter-narratives. Built with LangGraph, FastAPI, React. Chrome Extension included.
- **本地描述**：Compound AI system for detecting cognitive biases in text. 7 bias detectors. Generates counter-narratives. Built with LangGraph, FastAPI, React. Chrome Extension included.
- **拉取时间**：2026-07-25 18:14:47

---

# BiasBuster 🔍

**Составная AI-система для обнаружения когнитивных искажений в текстах.**

BiasBuster анализирует статьи, посты и расшифровки видео, находит манипулятивные приёмы и генерирует контр-нарратив — исправленную версию текста без искажений, с сохранением фактов.

---

## 🎯 Что умеет BiasBuster

| Тип искажения | Пример |
|---------------|--------|
| 🟡 **Framing Bias** | Эмоционально заряженная лексика: «режим» вместо «правительство» |
| 🔴 **Cherry-Picking** | Ссылка на одно удобное исследование при игнорировании противоположных |
| 🟠 **False Dilemma** | «Либо мы повышаем налоги, либо больницы закроются» |
| 🟣 **Straw Man** | Упрощение и утрирование позиции оппонента |
| 🔵 **Appeal to Emotion** | Замена аргументов на эмоциональные триггеры |
| 🟤 **Loaded Question** | Вопрос со встроенным неподтверждённым предположением |
| ⚫ **Bandwagon** | «Все знают, что...» без данных |

Для каждого найденного искажения BiasBuster **генерирует контр-нарратив** — переписывает фрагмент, убирая манипуляцию и сохраняя факты.

## Пример работы

<img src="screenshots/analize.jpg" alt="Демо-скриншот" width="600">
<img src="screenshots/history.jpg" alt="Демо-скриншот" width="600">

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 Быстрый старт

```bash
git clone https://github.com/Artem-Kornilov-pro/BiasBuster.git
cd BiasBuster/backend

# Установка
make install

# Переменные окружения
cp .env.example .env

# Линтинг и тесты
make lint
make test

# Запуск
make run
