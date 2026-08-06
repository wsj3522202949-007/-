---
id: tool-07459
type: tool
area: 库
status: active
tags: [互动叙事, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: open-dungeon
summary: 互动叙事/聊天写故事
source: https://github.com/newideas99/open-dungeon
created: 2026-07-18
updated: 2026-07-18
no: 7459
category: 画龙补充 / 扩容入库 — 补充源
repo: newideas99/open-dungeon
stars: 212
url: https://github.com/newideas99/open-dungeon
tier: "S"
use_case: "互动叙事/聊天写故事"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# newideas99/open-dungeon

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/newideas99/open-dungeon
- **Stars**：212
- **语言**：TypeScript
- **License**：MIT
- **Topics**：gemma, image-generation, interactive-fiction, local-llm, nextjs, ollama, on-device-ai, roleplay
- **GitHub 描述**：Open Dungeon — the first easy-to-use, fully local AI roleplay app. Story and inline scene images generated 100% on your machine (Gemma 4 QAT via Ollama(and others) + FLUX). No accounts, no API keys, no cloud.
- **本地描述**：open-dungeon
- **拉取时间**：2026-07-25 19:22:32

---

# Open Dungeon

The first **easy-to-use, fully local** AI roleplay app. The story and the
**inline scene images** are both generated on your own machine — no accounts,
no API keys, no cloud, no GPU rig. Your stories never leave your computer.

![A story scene with an inline generated image](https://github.com/newideas99/open-dungeon/blob/main/docs/hero.png)

- **Local text generation** via [Ollama](https://ollama.com) (Gemma 4 QAT),
  or **Connect a server** to any OpenAI-compatible backend — llama.cpp,
  LM Studio, vLLM, a remote Ollama, OpenRouter. Narration **streams in real
  time** as the model writes.
- **Local image generation** — the narrator calls a `generate_image` tool and
  scenes render inline: FLUX.2-klein on Apple Silicon / NVIDIA / supported
  AMD Radeons, or point the app at your own **ComfyUI** instance.
- **Full play controls** — Do / Say / Story input, Continue, Retry, Erase,
  and inline Edit on any passage. Quick-start presets write a custom opening.
- **Long-story memory** — history fills the model's context window
  (128K–256K), and older passages compact into a rolling "story so far"
  summary instead of being forgotten.
- **Characters with visual continuity** — saved portraits feed both the
  narrator (vision context) and the image generator (reference images).
- **Private by design** — everything lives in a local SQLite database and
  folders on your disk. Play from your phone over Tailscale.

<table>
  <tr>
    <td><img src="docs/prose.png" alt="Serif story prose" /></td>
    <td><img src="docs/modal.png" alt="New story dialog with setting presets" /></td>
  </tr>
</table>

## Quick start

**Mac (Apple Silicon):** grab the DMG from
[Releases](https://github.com/newideas99/open-dungeon/releases), drag
**Open Dungeon** to Applications, and open it (right-click → Open the first
time — it's unsigned). It walks you through everything, including choosing
Ollama or your own server as the narrator.

**Windows:** download the release zip (or clone), then double-click
`Launch-Windows.bat`. It checks Node.js, builds the app, and starts
http://localhost:3000. Ollama and image generation are optional prompts —
see the [Windows guide](https://github.com/newideas99/open-dungeon/blob/main/docs/windows.md).

**From a clone (any OS):**

```bash
git clone https://github.com/newideas99/open-dungeon && cd open-dungeon
npm install

# optional, only if you want the bundled Ollama provider
ollama pull gemma4:12b-it-qat

npm run dev
```

Open http://localhost:3000 and start writing. Node.js 22+ required; text
play needs no other setup.

## Playing

The composer has three input modes — **Do** (a player action), **Say**
(dialogue), and **Story** (write narration yourself) — plus **Continue**,
**Retry**, and **Erase** above it. Hover any message and hit **Edit** to
rewrite it in place. Everything saves to the local database as you go.

## Guides

| Guide | Covers |
|---|related:
  - methods/QUICK_START.md
---|
| [Text backends](https://github.com/newideas99/open-dungeon/blob/main/docs/text-backends.md) | Gemma 4 model choices and benchmarks, Connect a server, long-story memory |
| [Image generation](https://github.com/newideas99/open-dungeon/blob/main/docs/image-generation.md) | FLUX worker setup, ComfyUI backend, AMD GPUs, the story image tool |
| [Windows](https://github.com/newideas99/open-dungeon/blob/main/docs/windows.md) | Launcher details, image smoke tests, diagnostics, tuning |
| [Configuration](https://github.com/newideas99/open-dungeon/blob/main/docs/configuration.md) | Environment variables, playing from your phone, local data |

## Content note

This app is built for private, local fiction. The default narrator prompt
permits consensual adult content between adults; everything is generated and
stored only on your machine. Edit the system prompt in
`src/lib/story-prompt.ts` if you want different defaults.

## Support the project

Open Dungeon is free and MIT-licensed, and it always will be. If it earns a
spot on your machine and you want to help with development, a tip goes a
long way:

- **[Sponsor on GitHub](https://github.com/sponsors/newideas99)**
- **[Buy me a coffee on Ko-fi](https://ko-fi.com/opendungeon)**

Starring the repo and sharing it helps too.

## License

MIT
