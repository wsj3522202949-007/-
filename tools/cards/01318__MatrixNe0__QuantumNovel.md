---
id: tool-01318
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: QuantumNovel
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/matrixne0/quantumnovel
created: 2026-07-18
updated: 2026-07-18
no: 1318
category: 二、网文 / 长篇 AI 写作系统 库
repo: MatrixNe0/QuantumNovel
stars: 0
url: https://github.com/matrixne0/quantumnovel
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MatrixNe0/QuantumNovel

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/matrixne0/quantumnovel
- **Stars**：0
- **语言**：JavaScript
- **License**：MPL-2.0
- **Topics**：local-first, manuscript, nodejs, novelist, open-source, privacy, writing
- **GitHub 描述**：A safe and local-first, focused manuscript bridge that keeps writers in control. I've spent over 120 hours perfecting this tool. It is now fully versed as a codex skill as well.
- **本地描述**：A safe and local-first, focused manuscript bridge that keeps writers in control. I've spent over 120 hours perfecting this tool. It is now fully versed as a codex skill as well.
- **拉取时间**：2026-07-23 23:17:33

---

# QuantumNovel

> **Use QuantumNovel as a Codex skill:** the included skill teaches Codex how to analyze, review, back up, import, and verify a manuscript while keeping every decision under the writer's control.

> **Alpha software:** QuantumNovel is ready for careful testing, but it is not yet a stable release. Keep independent backups and review every planned change.

## The Heart of QuantumNovel

At its heart, QuantumNovel is about giving writers freedom without asking them to surrender control. It bridges the tools that help shape a manuscript with the place where that manuscript lives, preserving the author's original words, structure, and intent along the way.

QuantumNovel was created from a simple belief: writers should be able to use powerful creative tools without risking their work, compromising their privacy, or losing ownership of the process. Your manuscript remains yours. You see what will change, decide what happens, and stay in control from beginning to end.

When this repository is open in Codex, invoke the checked-in skill with `$quantumnovel`. Codex can also select it automatically for matching manuscript and Novelist tasks.

QuantumNovel is a guarded bridge between manuscript files and the Novelist web app. It connects to a local Chrome session, plans scene changes, creates a complete safety backup, writes only when explicitly approved, and verifies the result.

It is designed for AI-assisted and traditional editing workflows where manuscript preservation matters more than fast, blind replacement.

## Independent Project

QuantumNovel is an independent open-source project. It is not affiliated with, endorsed by, or supported by Novelist or Return True. Novelist and related names and trademarks belong to their respective owners.

## Safety Model

- Every injection is a dry run unless `--apply` is present.
- Live scenes must match one exact title and optional key.
- The hidden IndexedDB primary key is preserved.
- Apply mode creates and validates a complete database backup first.
- The write is refused if the scene changed after planning.
- Apply mode verifies the visible book title before writing.
- Batch manuscript updates run in one IndexedDB transaction.
- Every applied scene is read back and compared byte-for-byte.
- Guided imports create only author-accepted scenes and entries.
- Existing exact-title scenes, items, and relationships are reused instead of duplicated.
- A changed manuscript or live Novelist catalog invalidates the planned import.

## Guided Manuscript Import

QuantumNovel can guide the process without Codex. It first asks what you want identified, then analyzes the manuscript locally and proposes:

- scenes and events;
- goals and themes;
- characters and locations;
- props and extras;
- direction notes;
- evidence-backed relationships among them.

Start the wizard:

```powershell
.\QuantumNovel.cmd guided-import --file .\examples\guided-manuscript.md
```

The wizard creates a local `*.quantumnovel-plan.json` file and does not connect to or change Novelist. Review the suggestions interactively:

```powershell
.\QuantumNovel.cmd review-plan --plan .\examples\guided-manuscript.quantumnovel-plan.json
```

Or accept a deliberate set in one command:

```powershell
.\QuantumNovel.cmd review-plan `
  --plan .\examples\guided-manuscript.quantumnovel-plan.json `
  --accept characters,locations,props,themes
```

With a separate test book visible in the dedicated Novelist window, inspect the exact proposed database operations:

```powershell
.\QuantumNovel.cmd import-plan `
  --plan .\examples\guided-manuscript.quantumnovel-plan.json `
  --book "QuantumNovel Test"
```

Only after reviewing that dry run, apply it:

```powershell
.\QuantumNovel.cmd import-plan `
  --plan .\examples\guided-manuscript.quantumnovel-plan.json `
  --book "QuantumNovel Test" `
  --apply
```

Apply mode verifies the exact book, creates a complete local backup, rechecks the unchanged live catalog, performs one atomic transaction, and reads every changed record back exactly. Goals default to Novelist's **Extra** category; direction defaults to the relevant scene synopsis. The wizard lets you change or skip either mapping.

## Privacy

- QuantumNovel runs locally and has no telemetry or analytics.
- It does not upload manuscripts to QuantumNovel, its maintainers, or a project-operated service.
- Backups remain on the user's computer and are ignored by Git by default.
- Bug reports must never include private manuscript text, manuscript backups, credentials, or personal configuration files.

See `[PRIVACY.md](PRIVACY.md)` for the complete privacy statement.

## Requirements

- Windows, macOS, or Linux with Node.js 22 or newer.
- Google Chrome running Novelist with a remote-debugging port.
- A visible, fully loaded `https://web.novelist.app/` tab containing the intended book.

The Windows launcher automatically uses Codex's bundled Node runtime when it is installed.

## Open Novelist

Double-click `Open Novelist for QuantumNovel.cmd`, or use an existing stable Novelist debug profile. The included launcher defaults to port `9244` and stores its Chrome profile under `%USERPROFILE%\.quantumnovel\novelist-profile`.

To use an existing profile:

```powershell
powershell -File .\scripts\Open-NovelistDebug.ps1 `
  -Port 9244 `
  -ProfilePath "C:\path\to\novelist-profile"
```

Opening a profile never restores or imports a backup.

## First Connection

```powershell
.\QuantumNovel.cmd status
.\QuantumNovel.cmd scenes
.\QuantumNovel.cmd inspect --title "Chapter Seven"
```

Create an explicit backup at any time:

```powershell
.\QuantumNovel.cmd backup --out backups
```

## Inject One Chapter

Dry run:

```powershell
.\QuantumNovel.cmd inject-scene `
  --title "Chapter Seven" `
  --file ".\chapters\mirrors-dimension.md" `
  --mode replace
```

Review the reported scene key, primary key, block counts, word counts, and hashes. Then apply:

```powershell
.\QuantumNovel.cmd inject-scene `
  --title "Chapter Seven" `
  --file ".\chapters\mirrors-dimension.md" `
  --mode replace `
  --book "Sample Manuscript" `
  --apply
```

Use `--reload` only when the visible Novelist page should refresh immediately after verification.

## Supported Injection Modes

- `replace`: replace the complete scene text.
- `append`: add blocks to the end.
- `prepend`: add blocks to the beginning.
- `insert-after`: insert after one unique anchor block.
- `insert-before`: insert before one unique anchor block.

Anchor example:

```powershell
.\QuantumNovel.cmd inject-scene `
  --title "Chapter Seven" `
  --file ".\inserts\breakfast.md" `
  --mode insert-after `
  --anchor "The harbor bell rang" `
  --apply
```

An anchor that is missing or appears in multiple blocks is rejected.

## Inject A Manuscript Batch

Create a manifest:

```json
{
  "bookTitle": "Sample Manuscript",
  "chapters": [
    {
      "title": "Opening Scene",
      "file": "chapters/opening-scene.md",
      "mode": "replace"
    },
    {
      "title": "Chapter Seven",
      "file": "inserts/harbor-arrival.md",
      "mode": "insert-after",
      "anchor": "The harbor bell rang"
    }
  ]
}
```

Plan every chapter without writing:

```powershell
.\QuantumNovel.cmd inject-manuscript --manifest .\manuscript.json
```

Apply only after reviewing the complete plan:

```powershell
.\QuantumNovel.cmd inject-manuscript --manifest .\manuscript.json --apply
```

All changed scenes are backed up, validated, written atomically, and read back.

## Manuscript Formats

Markdown is the default. QuantumNovel:

- skips the first Markdown heading unless `--include-heading` is used;
- converts paragraphs into Novelist text blocks;
- preserves simple `*italic*` and `**bold**` spans;
- centers italicized attribution-marker paragraphs such as `-NOTE`;
- converts a paragraph containing only `related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---` into a Novelist break block.

For exact formatting, supply Novelist block JSON:

```powershell
.\QuantumNovel.cmd inject-scene `
  --title "Opening Scene" `
  --file .\opening-scene.blocks.json `
  --format novelist-json
```

Accepted JSON shapes are a block array or `{ "blocks": [...] }`.

## Configuration

Copy `quantumnovel.config.example.json` to `quantumnovel.config.json` to change defaults. The local config is ignored by Git. Setting `expectedBookTitle` removes the need to repeat `--book` on every apply command.

Environment variables:

- `NOVELIST_DEBUG_PORT`
- `QUANTUMNOVEL_CONFIG`

## Tests

```powershell
npm test
```

The application has no third-party runtime dependencies.

## Support and Security

- For safe troubleshooting guidance, see `[SUPPORT.md](SUPPORT.md)`.
- For security reporting, see `[SECURITY.md](SECURITY.md)`.
- Contributions are welcome under `[CONTRIBUTING.md](CONTRIBUTING.md)`.

## Sponsor QuantumNovel

QuantumNovel is free and open source. Sponsorship helps fund compatibility testing, safety improvements, documentation, and future adapters for other writing tools.

Use the **Sponsor** button at the top of the GitHub repository or see `[SPONSORSHIP.md](SPONSORSHIP.md)`.

## License

QuantumNovel is licensed under the `[Mozilla Public License 2.0](LICENSE)`. Modifications to MPL-licensed files must remain available under the MPL, while the project may still be combined with separately licensed software.
