---
id: tool-05050
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanizer-ru
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/smixs/humanizer-ru
created: 2026-07-18
updated: 2026-07-18
no: 5050
category: 一、去 AI 味 / Humanizer 库
repo: smixs/humanizer-ru
stars: 108
url: https://github.com/smixs/humanizer-ru
tier: "A"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# smixs/humanizer-ru

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/smixs/humanizer-ru
- **Stars**：108
- **语言**：Python
- **License**：MIT
- **Topics**：agent-skills, ai-agents, ai-text-detection, ai-writing, claude, claude-code, claude-skills, codex, content-creation, copywriting, editing, humanizer, llm, nlp, russian, russian-language, skill, text-humanization, text-processing, writing-tools
- **GitHub 描述**：Skill для AI-агентов (Claude Code, Codex, OpenClaw, Hermes): убирает 37 признаков AI-генерации из русского текста и проверяет, писала ли его нейросеть - канцелярит, штампы ChatGPT, артефакты копипаста | Russian AI-text humanizer & detector skill for coding agents
- **本地描述**：Skill для AI-агентов (Claude Code, Codex, OpenClaw, Hermes): убирает 32 признака AI-генерации из русского текста - канцелярит, штампы ChatGPT, слоп （ Russian AI-text humanizer skill for coding agents
- **拉取时间**：2026-07-25 18:04:15

---

![Humanizer RU](https://github.com/smixs/humanizer-ru/blob/main/banner.webp)

# Humanizer RU

[![Установки на skills.sh](https://skills.sh/b/smixs/humanizer-ru)](https://skills.sh/smixs/humanizer-ru)

Скилл для AI-агентов: Claude Code, Codex, OpenClaw, Hermes и любых других, читающих SKILL.md. Берёт русский текст после нейросети и убирает всё, по чему его палят: канцелярит, «не просто X, а Y», длинные тире, штампы, воду. Факты и цифры не трогает.

Работает в три шага. Сначала ищет проблемы по справочнику из 37 паттернов, потом чинит только найденное, в конце гоняет чистовик через линтер - питоновский скрипт, который ловит жёсткие запреты. Чистый текст возвращает как есть: повторная редактура хорошего текста его портит.

## Что нового 🔥

- **[23.07.2026] v1.6** 🕵️ Скилл научился отвечать на вопрос «это писала нейросеть?»: режим проверки без правки возвращает список улик с цитатами и вердикт. Линтер ловит служебные метки копипаста из чат-ботов (`turn0search3`, `utm_source=chatgpt.com`, `[cite: 8]`) - один такой след выдаёт копипаст однозначно. Плюс три новых паттерна: деепричастия-сироты, кальки с английского и «вы не одиноки»
- **[21.07.2026] v1.5** 🚦 Скилл перестал удалять призывы к действию вместе с водой, выдумывать факты при замене штампов и приписывать себе проверки в резюме. Эвалов теперь 18, три из них - по идеям из [PR #1](https://github.com/smixs/humanizer-ru/pull/1) от [@kootik](https://github.com/kootik)
- **[19.07.2026] v1.4** 🔍 Линтер `scripts/lint.py`: жёсткие запреты ловится скриптом, а не глюками. Паттерны 33-34 - повтор глаголов и стопка абзацев, по ним живые читатели чаще всего опознают AI
- **[14.07.2026] v1.2** 📚 11 новых паттернов из вики-эссе о признаках сгенерированного текста, правила из «Пиши, сокращай»

Полная история - в [CHANGELOG.md](https://github.com/smixs/humanizer-ru/blob/main/CHANGELOG.md).

## Установка

Через [skills.sh](https://skills.sh/smixs/humanizer-ru) - ставит в любой из 70 с лишним агентов:

```bash
npx skills add smixs/humanizer-ru        # спросит, куда ставить
npx skills add smixs/humanizer-ru -g     # глобально, для всех проектов
npx skills update humanizer-ru           # обновление
```

Или руками (Claude Code):

```bash
git clone https://github.com/smixs/humanizer-ru.git ~/.claude/skills/humanizer-ru
```

## Использование

```
/humanizer-ru

[ваш текст]
```

В любом агенте достаточно попросить: «очеловечь этот текст», «убери воду», «очисти от признаков AI».

Проверка без правки: «проверь, палится ли текст на ИИ» - скилл вернёт список улик с цитатами и вердикт, не трогая текст.

## Было - стало

| Было | Стало |
|------|----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
see_also:
  - 05343__distil-labs__distil-ai-slop-detector.md
  - 07222__devswha__patina.md
  - 07225__dongbeixiaohuo__writing-agent.md
---|
| Мы осуществляем проведение мероприятий по повышению эффективности. | Мы работаем эффективнее. |
| Решение было принято руководством. | Руководство решило. |
| Запуск продукта знаменует собой ключевой этап в развитии компании. | Компания запустила новый продукт. |
| Это не просто инструмент, а целая философия работы. | Инструмент ускоряет работу. |
| Возможно, можно предположить, что это может оказать некоторое влияние. | Это влияет. |
| Скорость > красоты. Идея → прототип → продукт. | Скорость важнее красоты. Сначала идея, потом прототип, потом продукт. |
| Внимание - валюта XXI века. | Люди платят временем только за то, что им интересно. |
| Подводя итог, можно сказать, что переход включает миграцию данных и обучение команды. | Миграцию заканчиваем в марте. |

Все 37 паттернов с примерами - в [references/patterns.md](https://github.com/smixs/humanizer-ru/blob/main/references/patterns.md).

## Как это проверяется

19 eval-сценариев, 127 проверок: сохранность фактов и цифр, ловушки на замену слопа синонимами, чистые тексты, которые нельзя трогать. Мы выпускаем новую версию, только когда она проходит все проверки. Линтер `scripts/lint.py` - обычный python3 без зависимостей; без питона скилл работает по ручному чеклисту.

## Источники

- [humanizer](https://github.com/blader/humanizer) от [@blader](https://github.com/blader) - основа
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) и [русское эссе](https://ru.wikipedia.org/wiki/Википедия:Признаки_сгенерированности_текста)
- Максим Ильяхов, «Пиши, сокращай»
- [Vladimir-Human/humanizer-ru](https://github.com/Vladimir-Human/humanizer-ru) - реестр артефактов копипаста, границы ложных срабатываний (MIT)
- [no-ai-slop](https://github.com/petergyang/no-ai-slop) от [@petergyang](https://github.com/petergyang) - режим проверки без правки, правило кикера (MIT)

## Лицензия

MIT
