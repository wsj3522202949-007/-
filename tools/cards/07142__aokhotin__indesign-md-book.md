---
id: tool-07142
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: indesign-md-book
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/aokhotin/indesign-md-book
created: 2026-07-18
updated: 2026-07-18
no: 7142
category: 画龙补充 / 扩容入库 — 补充源
repo: aokhotin/indesign-md-book
stars: 0
url: https://github.com/aokhotin/indesign-md-book
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1e1c1433229ce3ca
  - methods/QUICK_START.md
---

# aokhotin/indesign-md-book

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/aokhotin/indesign-md-book
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：adobe, automation, desktop-publishing, extend-script, generator, indesign, markdown, publishing, script
- **GitHub 描述**：Инструмент для верстальщиков и контент-менеджеров: пишете в Markdown (Obsidian, iA Writer, VS Code), скрипт создаёт готовый макет InDesign. Заголовки, списки, цитаты, таблицы — всё сразу в Paragraph Style и Character Style. Дизайнер настраивает стили один раз, скрипт переиспользует. Работает на macOS и Windows через InDesign.
- **本地描述**：indesign-md-book
- **拉取时间**：2026-07-25 19:12:07

related:
  - methods/QUICK_START.md
---

# MD Book Generator

Pipeline `Markdown -> Adobe InDesign` с runtime на ExtendScript и parser-слоем по принципу CommonMark-first.

## Состояние

- Парсер строит структурированный AST (CommonMark-first), а не regex-замены по тексту.
- Вывод в InDesign маппится через paragraph/character/object styles; прямое форматирование шрифта не используется.
- Нативные таблицы InDesign для Markdown pipe tables с подбором ширины колонок.
- Obsidian-расширения (callouts, wikilinks, frontmatter, transclusion `![[...]]`) включены по умолчанию.
- Стили вынесены в редактируемый каталог `styles/` с наследованием от `MD Base`.

## Что уже работает

- ATX-заголовки и setext-заголовки
- Параграфы
- Нумерованные и маркированные списки
- Вложенные списки
- Списки задач GFM (`- [ ]` / `- [x]`) — чекбокс вместо буллета
- Цитаты
- Fenced и indented code blocks
- Thematic breaks
- `emphasis`, `strong`, `strikethrough`, `code spans`
- Ссылки, autolinks, изображения
- **Таблицы (pipe tables)** — нативные таблицы InDesign с подбором ширины колонок под содержимое
- **Каталог стилей в файлах** — `styles/<группа>/<стиль>.json`, группы отражаются в Style Groups InDesign, все абзацные стили наследуют `MD Base`
- **Obsidian transclusion** (`![[filename]]`) — рекурсивное раскрытие embed-файлов перед парсингом
- **Obsidian extensions** (callouts, wikilinks, frontmatter) — включены по умолчанию
- Вход через выбор одного Markdown-файла
- Unit-тесты parser-слоя без Node.js

## Структура проекта

- `main.jsx` — точка входа ExtendScript для InDesign
- `src/shared/markdown-parser.jsx` — CommonMark-first AST parser
- `src/indesign/styles.jsx` — загрузчик стилей из каталога `styles/`
- `src/indesign/renderer.jsx` — renderer `AST -> InDesign`
- `styles/` — каталог стилей: подпапка = смысловая группа, один JSON = один стиль
- `tools/scaffold-styles.js` — генерирует/перегенерирует каталог `styles/`
- `tests/run-tests.js` — запуск parser-тестов через `osascript`
- `tools/build.js` — собирает `#include`-модули в `dist/md-book.jsx` и копирует `styles/` в `dist/`
- `docs/` — документация по запуску, архитектуре и ограничениям ExtendScript

## Использование

Запуск выполняется в Adobe InDesign через `main.jsx`.

При запуске скрипт открывает диалог выбора одного Markdown-файла.

Скрипт создаёт текстовый фрейм на активной странице и импортирует в него разобранный документ.

## Команды разработки

**macOS:**
- Запуск parser-тестов: `osascript -l JavaScript tests/run-tests.js`
- Сборка bundled JSX: `osascript -l JavaScript tools/build.js`
- Перегенерация каталога стилей: `osascript -l JavaScript tools/scaffold-styles.js`

**Windows:**
- Сборка bundled JSX: `node tools/build-windows.js`

## VS Code

- `F5` запускает `main.jsx` в InDesign через `ExtendScript Debugger`
- `Terminal > Run Task > test` запускает parser-тесты
- `Terminal > Run Task > build:jsx` собирает `dist/md-book.jsx`

## Стили

Стили хранятся в каталоге `styles/` — по одному JSON-файлу на стиль, подпапка задаёт смысловую группу:

```
styles/
  _base/md-base.json          # MD Base — наследуется всеми абзацными стилями
  headings/md-heading-1.json
  lists/md-bullet-list-1.json
  callouts/md-callout-note.json
  ...
```

Каждый файл описывает имя, тип (`paragraph` / `character` / `object`), необязательный `basedOn` и свойства:

```json
{
  "name": "MD Base",
  "type": "paragraph",
  "properties": { "appliedFont": "Minion Pro", "pointSize": 10.5, "leading": "AUTO" }
}
```

**Дефолты намеренно нейтральны.** Из коробки только `MD Base` несёт свойства (шрифт/кегль — единственная «ручка»), символьные стили хранят начертание (bold/italic/…), а `MD Image`/`MD Image Caption` — центрирование. Остальные абзацные стили нейтральны (`"properties": {}`) и наследуют `MD Base` — типографику (интервалы, иерархию заголовков, отступы списков) настраиваете вы под себя.

При запуске `src/indesign/styles.jsx` рекурсивно читает каталог, создаёт в InDesign Style Groups по структуре папок и стили со свойствами, затем проставляет наследование (абзацные стили без явного `basedOn` → `MD Base`). Спецключи свойств: `fillColorHex`/`strokeColorHex` (создают RGB-swatch), `leading: "AUTO"`, enum-значения как строки (`justification: "CENTER_ALIGN"`).

Чтобы изменить оформление — правьте JSON-файлы (или добавляйте новые) и перезапускайте скрипт; либо один раз настройте стили `MD *` в шаблоне InDesign — загрузчик **не перезаписывает** уже существующие стили. Порядок резолва: живое чтение `styles/` → запечённый `src/indesign/styles-catalog.jsx` (полные свойства и группы, вшит в бандл — работает при запуске из ExtendScript Debugger, где папка недоступна) → как крайний резерв голые стили по именам.

## Документация

- `docs/usage.md`
- `docs/architecture.md`
- `docs/extendscript.md`
- `docs/project-generation/README.md`

## Текущие ограничения

- Runtime по-прежнему ориентирован на классический ExtendScript, поэтому код остаётся ES3-friendly.
- Вставка изображений зависит от локальных путей относительно выбранного Markdown-источника; ненайденные изображения пропускаются с предупреждением.
- Obsidian embed (`![[file]]`) ищет файлы по индексу в директории основного документа и её подпапках — поиск по всему vault не поддерживается.
- Символы вне BMP (эмодзи, напр. `📌`) удаляются при нормализации: в JS это суррогатная пара (2 code unit), а InDesign считает их за 1 символ — иначе сбивается выравнивание символьных стилей.
- Релизный бандл `dist/md-book.jsx` самодостаточен за счёт вшитого каталога стилей; для редактирования стилей файлами нужна папка `styles/` рядом со скриптом — она есть в репозитории, в `dist/` и в релизном архиве.

## Лицензия

MIT
