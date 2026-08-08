---
id: tool-05127
type: tool
area: 库
status: active
tags: [去AI味, TTS, 互动叙事, 协议宽松, 本地优先, 英文文档, 本地写作]
title: russian-vector
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/osmosy/russian-vector
created: 2026-07-18
updated: 2026-07-18
no: 5127
category: 一、去 AI 味 / Humanizer 库
repo: Osmosy/russian-vector
stars: 1
url: https://github.com/osmosy/russian-vector
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2cf847561597c376
  - methods/改稿润色指令库.md
---

# Osmosy/russian-vector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/osmosy/russian-vector
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：ai-agents, bureaucratese, copula, humanize, llm, nlp, russian, skill, text-quality, typography
- **GitHub 描述**：Навык для AI-агентов: писать по-русски, а не по-русски-английски. Merges ru-text + ru-humanize: 8 AI pathologies, 9 Patina patterns, 97+ stop-words, 13-point checklist, TTS filter, always-on typography.
- **本地描述**：Навык для AI-агентов: писать по-русски, а не по-русски-английски. Merges ru-text + ru-humanize: 8 AI pathologies, 9 Patina patterns, 97+ stop-words, 13-point checklist, TTS filter, always-on typography.
- **拉取时间**：2026-07-25 18:07:07

---

<div align="center">

<img src="assets/logo.png" alt="Русский Вектор" width="200"/>

# Русский Вектор

**Навык для AI-агентов: писать по-русски, а не по-русски-английски**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Sources: ru-text + ru-humanize](https://img.shields.io/badge/Sources-ru--text%20%2B%20ru--humanize-green.svg)](#источники-и-благодарности)
[![Anti-patterns: 139+](https://img.shields.io/badge/Anti--patterns-139%2B-orange.svg)](#стоп-слова-топ-20-из-97)
[![Self-review: 13 points](https://img.shields.io/badge/Self--review-13%20points-red.svg)](#self-review-чеклист-13-пунктов)

</div>

---

Проблема: AI-агенты, начитавшись английского, пишут по-русски так, что текст отравляет сам себя. Канцелярит, copula-патология, zombie nouns, смешение языков — модель подхватывает и дальше уже невозможно вести диалог.

Решение: **удалить то, что не несёт смысла**. Если текст стал на 30% короче и содержательнее — всё правильно.

Объединяет два проверенных источника:

| Источник | Что даёт |
|---|---|
| [ru-text](https://ru-text.org) (Arseniy Kamyshev) | Типографика, инфостиль, 139 антипаттернов, шкала регистров, scoring |
| [ru-humanize](https://github.com/kvcop/ru-humanize-skill) (kvcop) | AI-патологии, Patina-адаптация, TTS-фильтр, ритм, язык mixins |

## Что внутри

- **8 AI-патологий** с примерами до/после: copula, zombie nouns, канцелярит, родительный падеж цепочки, псевдо-академические вводные, слова-усилители, смешение языков, ритм
- **9 Patina-паттернов** адаптированных на русский: Importance Inflation, AI Vocabulary, Rule of Three, Vague Attribution, Bright Future, Chatbot Phrases, Hedging, Boldface Lists, Metronomic Paragraphs
- **97+ стоп-слов** с заменами (топ-20 в SKILL.md, полный каталог — в ru-text)
- **13-пунктный self-review чеклист**: 3+ «да» = переписать абзац
- **Типографика**: кавычки-ёлочки, тире, НРСП, числа — always-on
- **TTS-фильтр**: даже короткие фразы для озвучки проходят через humanize
- **Чёткие границы**: код/JSON/YAML/log — НЕ трогать

## Быстрый пример

**❌ До:**

> Reinforcement learning представляет собой одну из наиболее перспективных парадигм машинного обучения, которая в последние годы получила широкое распространение в различных областях. В рамках данного подхода агент осуществляет взаимодействие со средой с целью максимизации совокупного вознаграждения. Несмотря на ряд имеющихся ограничений, перспективы выглядят крайне обнадёживающими.

**✅ После:**

> В RL агент учится, взаимодействуя со средой: видит состояние, выбирает действие, получает награду. За миллионы шагов нащупывает, что приносит очки.

## Установка

### Hermes Agent

Скопируйте `SKILL.md` в каталог навыков:

```bash
cp SKILL.md ~/.hermes/skills/writing/russian-vector/SKILL.md
```

Или через skill_manage:

```bash
hermes skill install --from-file SKILL.md
```

### Claude Code / Cursor / любой AI с правилами

Скопируйте содержимое `SKILL.md` в:
- `.claude/rules/russian-vector.md`
- `.cursor/rules/russian-vector.mdc`
- или любой другой файл правил вашего агента

### Как AGENTS.md / system prompt

Вставьте секции «AI-патологии» и «Self-review чеклист» в system prompt или AGENTS.md вашего проекта.

## Критерий транслитерации

| Прижившееся → кириллица | Не прижившееся → латиница |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| фича, бот, чат, релиз, деплой | MongoDB, worktree, checkpoint |
| коммит, форк, пуш, мердж, патч | callback, scope, batch, heartbeat |
| | CLI, MLflow, replay, eval |

**Не**: «мунго-схема», «воркдерево», «чекпоинт-лоадер»

## Источники и благодарности

- **ru-text** by Arseniy Kamyshev — [ru-text.org](https://ru-text.org)
- **ru-humanize** by kvcop — [github.com/kvcop/ru-humanize-skill](https://github.com/kvcop/ru-humanize-skill)
- **Patina** — оригинальные English-паттерны, адаптированные в ru-humanize на русский

PR и issue приветствуются — соберём фейл-кейсы и научим агентов разговаривать по-русски.

## Лицензия

MIT — используйте свободно, attribution приветствуется.
