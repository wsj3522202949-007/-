---
id: tool-05481
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ykovlevia23/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5481
category: 一、去 AI 味 / Humanizer 库
repo: YkovlevIA23/ai-text-detector
stars: 0
url: https://github.com/ykovlevia23/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# YkovlevIA23/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ykovlevia23/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：YkovlevIA23/ai-text-detector
- **拉取时间**：2026-07-25 18:20:18

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Локальный детектор ИИ-текстов на основе дообучения модели ruBERT

**Студент:** Яковлев Илья Александрович
**Группа:** КБ-231

## Описание

Локальное оконное приложение для определения, написан текст человеком или сгенерирован ИИ (GPT-4, DeepSeek).
Модель: дообученный ruBERT (fine-tuning).
Точность на тестовой выборке: **99%**.

## Как запустить

### Требования
- Python 3.9+

### 1. Клонировать репозиторий
git clone https://github.com/YkovlevIA23/ai-text-detector.git

cd ai-text-detector

### 2. Установить зависимости
pip install -r requirements.txt

### 3. Обучить модель(занимает время)
python train.py

### 4. Запустить приложение
python app.py

## Результаты
- Accuracy: 99.0%
- Precision: 100.0%
- Recall: 98.0%
- F1-score: 98.99%
