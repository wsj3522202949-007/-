---
id: tool-05346
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: slopshield-engine
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/chknlittle/slopshield-engine
created: 2026-07-18
updated: 2026-07-18
no: 5346
category: 一、去 AI 味 / Humanizer 库
repo: chknlittle/slopshield-engine
stars: 0
url: https://github.com/chknlittle/slopshield-engine
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# chknlittle/slopshield-engine

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/chknlittle/slopshield-engine
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：YouTube AI snippet detector: transcript text pick + XLSR-SLS audio spoof score
- **本地描述**：YouTube AI snippet detector: transcript text pick + XLSR-SLS audio spoof score
- **拉取时间**：2026-07-25 18:15:11

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# SlopShield Engine

Score a browser-supplied YouTube transcript for AI-written narration, download
only the selected segment, and corroborate it with synthetic-speech detection.

The repository lives on **tabitha**. A persistent FastAPI service runs on
**helga**, where the text and audio models remain loaded on the GPU.

## Built with OpenAI Codex and GPT-5.6

We used OpenAI Codex with GPT-5.6 throughout Build Week.

Codex helped turn a single script into a persistent FastAPI service.

It helped make GPU model loading and unloading explicit.

It helped build a labeled benchmark runner and threshold-search tools.

It helped develop transcript scoring across 10, 20, 40, and 80-second windows.

The context thresholds scored 12 of 12 analyzable reference videos.

The earlier single-threshold baseline scored 10 of 12.

Codex helped move session-bound caption retrieval into the browser extension.

It helped remove more than 500 lines of obsolete proxy and transcript code.

GPT-5.6 helped trace behavior across the extension, API, and engine.

It checked assumptions against the code and benchmark results.

## Pipeline

1. Accept a YouTube URL and timestamped transcript from SlopShield API.
2. Parse the video ID and transcript.
3. Build 10-second leaves and score 10/20/40/80-second text contexts with
   `gouwsxander/slop-detector-bert`.
4. Require agreement at 20 seconds (**0.125%**) and 40 seconds (**0.102%**).
5. Map the strongest contextual signal back to a 10-second leaf.
6. Download that selected segment with `yt-dlp` — on **every** verdict path,
   not just positives.
7. Corroborate the transcript against the segment audio with
   `faster-whisper base.en` (deterministic decoding: beam 1, temperature 0,
   VAD, no fallback). If normalized word-sequence similarity falls below
   **0.5**, the request fails with HTTP 400 `transcript mismatch` — the
   verdict is never produced, so SlopShield API records a failed analysis
   instead of caching a poisoned result.
8. Score the segment's first 64,600 audio samples with XLSR-SLS.
9. Flag `ai_suspect` when contextual text agrees and audio spoof is at least
   **1%**.

The transcript check exists because the API trusts browser-supplied
transcripts: without it, anyone could POST a human-looking transcript for a
slop video (or an AI-looking one for a human video) and poison the shared
verdict cache. Verifying that the audio we download actually says what the
transcript claims closes that hole for the sampled window. Text-gate
negatives previously returned without downloading anything (~0.34s); they now
cost a snippet download plus warm Whisper (~2.7s) on cache misses only.

Transcript acquisition belongs to the browser extension. The engine does not
contact YouTube for captions or maintain transcript/proxy state.

The thresholds are empirical decision boundaries from the reference benchmark;
they are not calibrated probabilities. Separate context thresholds score 12/12
of the currently analyzable reference videos, compared with 10/12 for the
single-threshold baseline.

## Server control

From tabitha:

```bash
python3 script.py --serve
python3 script.py --restart
python3 script.py --stop
```

`--serve` recursively deploys the server package to `~/slopshield-engine` on helga,
installs/starts the manual `slopshield-engine.service`, and waits for both models
to load. `--stop` stops that service and unloads VRAM. The service is deliberately
not enabled, so it does not start after a reboot or compete with an LLM unless
you start it manually.

You can also control it directly on helga:

```bash
systemctl --user start slopshield-engine.service
systemctl --user stop slopshield-engine.service
systemctl --user status slopshield-engine.service
journalctl --user -u slopshield-engine.service -f
```

Analyze a video through the CLI with a browser-fetched timestamped transcript:

```bash
python3 script.py --transcript-file transcript.txt \
  'https://www.youtube.com/watch?v=UKSCtJRkEKg'
```

Add `--keep` to retain the extracted WAV on helga.

## HTTP API

The API is available on the local network at `http://192.168.0.129:8765`.
Helga's firewall restricts port 8765 to the LAN. Deployment and service control
use SSH at `rin@192.168.191.60`.

```bash
curl -sS http://192.168.0.129:8765/health | jq

curl -sS http://192.168.0.129:8765/analyze \
  -H 'Content-Type: application/json' \
  -d '{
    "url":"https://www.youtube.com/watch?v=UKSCtJRkEKg",
    "transcript":"[0.00 -> 3.20] Example timestamped caption"
  }' | jq
```

`POST /analyze` accepts:

```json
{
  "url": "https://www.youtube.com/watch?v=UKSCtJRkEKg",
  "transcript": "[0.00 -> 3.20] Example timestamped caption",
  "keep": false,
  "force": false
}
```

`force` is intended for benchmarking. It bypasses the production text gate and
the Whisper transcript check so both raw model signals can be collected.

## Runtime state

Per-request video and WAV files use isolated `/tmp/yt-ai-*` directories and are
removed in a `finally` block. `--keep` copies the final WAV to
`/tmp/slopshield-engine-keep/` before cleanup.

## Benchmark

The reference set contains 14 unique hand-labeled videos, balanced between AI
and not-AI examples.

```bash
python3 benchmarks/run_reference.py --transcript-dir /path/to/transcripts
python3 benchmarks/evaluate_thresholds.py benchmarks/latest-results.json
python3 benchmarks/evaluate_pyramid.py benchmarks/latest-results.json
```

See [`benchmarks/README.md`](https://github.com/chknlittle/slopshield-engine/blob/main/benchmarks/README.md) for details and limitations.

## Source layout

```text
server/
├── api.py                 # HTTP routes and lifecycle
├── config.py              # environment-backed configuration
├── domain.py              # transcript chunking and selection
├── service.py             # analysis orchestration
├── schemas.py             # request and response models
├── models/                # text/audio models and shared GPU lifecycle
└── youtube/               # URL parsing, media download, and ffmpeg
```

Heavy dependencies run in helga's `~/deepfake-audio/.venv`. The tabitha client
uses only the Python standard library.
