---
id: tool-00246
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: cockpit-ai
summary: 小说转语音/有声书
source: https://github.com/luizvb/cockpit-ai
created: 2026-07-18
updated: 2026-07-18
no: 246
category: 二、网文 / 长篇 AI 写作系统 库
repo: luizvb/cockpit-ai
stars: 0
url: https://github.com/luizvb/cockpit-ai
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# luizvb/cockpit-ai

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/luizvb/cockpit-ai
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, copilot, electron, pair-programming, react, speech-to-text, whisper-stt
- **GitHub 描述**：macOS-first Electron app for real-time AI assistance across calls, pair programming, writing, and technical prep.
- **本地描述**：macOS-first Electron app for real-time AI assistance across calls, pair programming, writing, and technical prep.
- **拉取时间**：2026-07-23 22:46:16

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Cockpit AI

macOS-first Electron app for real-time AI assistance across calls, pair programming, study sessions, writing, and technical preparation.

## What it does

Cockpit AI runs as a compact desktop cockpit that can listen to microphone/system audio, optionally inspect a selected screen, and show live AI guidance in separate panels:

- conversational guidance for what to say or ask next;
- technical planning for coding and system-design discussions;
- compact code assistance from the current plan;
- optional pair-programming voice cues;
- transcript, screen context, live feedback, and local session history.

## Stack

- Electron main process for UI orchestration, secrets, audio streaming, SQLite, IPC, and optional Obsidian export
- TypeScript ADK sidecar backend for LLM reasoning and live agent orchestration through OpenRouter
- React + Vite renderer for the cockpit UI
- Offline Whisper STT, OpenRouter STT, OpenAI Realtime, Google Cloud Speech-to-Text, and Deepgram Flux
- `sql.js` persisted to a local SQLite file under Electron `userData`

## Setup

```bash
cp .env.example .env.local
npm install
npm run dev
```

`npm run dev` builds the ADK sidecar first, then starts Vite and Electron. Electron autostarts the compiled sidecar unless `ADK_BACKEND_AUTOSTART=0` is set.

## Configuration

OpenRouter is the default LLM and STT provider:

- `OPENROUTER_API_KEY` is required for LLM-backed cockpit work and OpenRouter STT.
- `OPENROUTER_MODEL`, `OPENROUTER_TECHNICAL_MODEL`, and `OPENROUTER_CONVERSATION_MODEL` configure the main agents.
- `OPENROUTER_TRANSCRIPTION_MODEL` configures OpenRouter speech-to-text.
- `ADK_BACKEND_URL` defaults to `http://127.0.0.1:47631`.
- `ADK_BACKEND_AUTOSTART=1` starts `dist-backend/src/adk-backend/server.js` automatically.
- `ADK_BACKEND_NODE_PATH` defaults to `node`; use a Node 24+ binary when needed.

STT providers:

- `STT_PROVIDER=openrouter` uses OpenRouter speech-to-text.
- `STT_PROVIDER=whisper` uses local/offline Whisper.
- `STT_PROVIDER=openai` uses OpenAI Realtime transcription and requires `OPENAI_API_KEY`.
- `STT_PROVIDER=google` uses Google Cloud Speech-to-Text V2 streaming and requires Google Cloud credentials.
- `STT_PROVIDER=deepgram` uses Deepgram Flux streaming and requires `DEEPGRAM_API_KEY`.

Optional Obsidian/profile context:

- `OBSIDIAN_VAULT_PATH` enables export/profile-context features.
- `COCKPIT_PROFILE_CONTEXT_FILES` is a comma-separated allowlist of relative files to load, optionally with a max character limit, for example `Context/profile.md:12000,Context/examples.md:8000`.
- No profile context is loaded by default.

## Privacy Model

- API keys stay in the Electron main process and are never exposed to the renderer.
- Audio is streamed from the renderer to the Electron main process, then to the selected STT provider.
- Local Whisper writes only short-lived temp files and deletes them after transcription.
- Screen insights are opt-in. When enabled, the app captures a reduced JPEG snapshot every few seconds, deduplicates repeated images by hash, and stores only structured context plus the image hash.
- Raw screenshots are not written to disk.
- Session history is stored locally in SQLite under Electron `userData`.
- Obsidian export is disabled unless `OBSIDIAN_VAULT_PATH` is configured.

## Use Cases

- Meetings and calls: live transcript, follow-up cues, and context tracking.
- Pair programming: technical framing, implementation hints, and optional voice cues.
- Study and preparation: summarize discussion context and keep a running problem frame.
- Writing and communication: phrase suggestions, concise feedback, and next-question prompts.
- Real-time context support: screen-aware notes when the user explicitly enables screen insights.

## macOS Permissions

The first run needs microphone permission. System audio capture depends on macOS and device setup. If the native picker does not expose an audio track, install a virtual audio device such as BlackHole, Loopback, or Soundflower.

Recommended device selection:

- `Me input`: the user's real microphone.
- `Other speaker input`: a virtual/system audio input such as `BlackHole 2ch`.
- Meeting app microphone: the user's real microphone, not the virtual audio device.

## Development

```bash
npm run typecheck
npm test
npm run build
```

Electron smoke tests are available with:

```bash
npm run test:electron
```

## Project Status

This is an early desktop AI cockpit. Provider configuration, macOS audio routing, and screen permissions vary by machine. Treat cloud STT/LLM usage as sensitive and review provider policies before sending private meeting, screen, or audio content.
