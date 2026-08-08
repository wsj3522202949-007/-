---
id: tool-07179
type: tool
area: 库
status: active
tags: [Go, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3api
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/capoverflow/ao3api
created: 2026-07-18
updated: 2026-07-18
no: 7179
category: 画龙补充 / 扩容入库 — 补充源
repo: capoverflow/ao3api
stars: 0
url: https://github.com/capoverflow/ao3api
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4abb8750be9b429a
  - methods/QUICK_START.md
---

# capoverflow/ao3api

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/capoverflow/ao3api
- **Stars**：0
- **语言**：Go
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ao3api
- **拉取时间**：2026-07-25 19:13:16

related:
  - methods/QUICK_START.md
---

### AO3 API

A Go library to fetch data from Archive of Our Own (AO3).

- Current backend: Chrome DevTools automation via `go-rod` + parsing with `goquery`.
- Roadmap backend: pure HTTP scraper using `net/http` + `go-colly` + `goquery` (no headless browser).

Project was renamed from `ao3api-rod` to `ao3api` to support multiple backends.

### Status

Early WIP. APIs can change. Use responsibly and respect AO3's Terms of Service and rate limits.

### Requirements

- Go 1.21+
- For the current `go-rod` backend:
  - A local Chrome/Chromium or a remote browser reachable via DevTools protocol
  - Optionally, an exported cookies file (parsed via `CookieMonster`)

### Install

```bash
go get github.com/capoverflow/ao3api
```

### Quick start (go-rod backend)

Initialize the browser, log in (via cookies or credentials), navigate, and scrape.

```go
package main

import (
    "log"

    "github.com/capoverflow/ao3api/internals/base"
    "github.com/capoverflow/ao3api/internals/author"
    "github.com/capoverflow/ao3api/internals/fanfic"
    "github.com/capoverflow/ao3api/internals/models"
)

func main() {
    cfg := models.RodConfig{
        Headless: true,
        // If you have a remote Chrome endpoint:
        // RemoteURL: "ws://127.0.0.1:9222/devtools/browser/<id>",
        Login: models.Login{
            // Choose ONE login method:
            // 1) Use exported cookies (JSON/SQLite supported by CookieMonster)
            CookiesPath: "/path/to/cookies", 
            // 2) Or username/password
            // Username: "user",
            // Password: "pass",
        },
    }

    base.Init(cfg)
    page := base.Page

    // Scrape a work page
    page.MustNavigate("https://archiveofourown.org/works/<WORK_ID>").MustWaitLoad()
    work := fanfic.GetFanfic(page)
    work, _ = fanfic.GetFanficChapters(work, page)
    log.Printf("Work: %+v\n", work)

    // Scrape an author's dashboard
    a := models.Author{AuthorParams: models.AuthorParams{Author: "<AO3_USERNAME>"}}
    a = author.GetAuthorDashboard(a, page)
    log.Printf("Author: %+v\n", a)
}
```

#### Alternate login methods

- Cookies file: set `Login.CookiesPath` (parsed to DevTools cookies via `utils.ConvertHTTPCookieToRodCookie`).
- Username/password: set `Login.Username`, `Login.Password`.

### What you can get today

- Fanfic metadata from a work page: title, authors, dates, language, words, chapters count, stats, tags, download links.
- Chapters list from a work: chapter IDs, names, dates.
- Author dashboard: pseuds, fandoms (with counts), works list with metadata and tags.
- Cookie helpers to convert between `net/http` and `rod` cookie types.

APIs are exposed under:

- `internals/base`: `Init(models.RodConfig)` initializes the browser and session.
- `internals/auth`: login via cookies or credentials; utilities to save cookies.
- `internals/fanfic`: `GetFanfic`, `GetFanficChapters` (comments WIP).
- `internals/author`: `GetAuthorDashboard`.
- `internals/utils`: helpers and cookie conversion.
- `internals/models`: data structures (`Work`, `Chapter`, `Author`, etc.).

### Roadmap

#### Multi-backend interaction modes

- Define a unified `Client` interface (e.g., `WorkByID`, `AuthorDashboard`, `Chapters`, `Comments`, `Search`/`Browse`).
- Implement selectable backends:
  - **RodBackend**: current `go-rod` + `goquery` implementation for JS-required flows.
  - **HTTPBackend**: `go-colly` or pure `net/http` + `goquery` for faster, headless-free scraping.
- Seamless backend selection via config flag (`Backend=rod|http`) with optional auto-fallback (`rod→http`) when JS isn’t needed.
- Shared session layer: cookie jar + login abstraction reused across backends.
- Pluggable middlewares: rate limiting, retries, proxy rotation, custom User-Agent.

#### Better client initialization

- Provide a top-level constructor and options API:
  - `ao3.NewClient(ctx, opts ...Option) (Client, error)`
  - Functional options: `WithBackend`, `WithLogin`, `WithCookiesPath`, `WithRemoteURL`, `WithHeadless`, `WithHTTPTransport`, `WithProxy`, `WithRateLimit`, `WithRetry`, `WithUserAgent`.
- Config model (illustrative):
  - `Backend` selection (rod/http),
  - `Rod` settings: `RemoteURL`, `Headless`.
  - `HTTP` settings: base URL, transport, cookie jar.
  - `Login`: `Username`, `Password`, `CookiesPath`, or preloaded cookies.
  - `RateLimit`: requests-per-second, burst, jitter.
  - `Retry`: max attempts, backoff strategy.
  - `Proxy`: static or rotating proxy list.
  - `UserAgent`: override UA string.
- Lifecycle methods: `Client.Close(ctx)` to cleanly shutdown the rod browser or flush HTTP resources.
- Session persistence: optional cookie save/load between runs.

#### Crawler system

- Queue-based crawling with dedupe and politeness controls:
  - Seeds: works, authors, tags, series, bookmarks.
  - Controls: max depth, max pages, allowed paths, per-host RPS, jitter, concurrency.
  - Robust retry/backoff for 429/5xx; respect AO3 rate limits.
  - URL and WorkID-level deduplication; checkpointing and resume.
- Fetcher/Parser separation so both backends can feed the crawler.
- Outputs via pluggable sinks: channel callbacks, JSONL writer, or user-provided interface.
- Incremental parsing for large author libraries; batched writes.

#### Milestones

- M1: Define `Client` interface and shared models; stabilize selectors.
- M2: Implement HTTP backend for read-only endpoints (works, chapters, author dashboards).
- M3: Introduce `ao3.NewClient` + functional options; unify login/session handling.
- M4: Crawler MVP with seeds, dedupe, politeness, and pluggable sinks.
- M5: Comments pagination + parsing improvements across backends.
- M6: Docs, examples, and CI tests for both backends.

### Notes

- Be mindful of scraping etiquette: add randomized delays (`utils.RandSleep`), avoid heavy concurrent requests, and cache locally.
- AO3 content and DOM can change; selectors may need updates over time.

### License

TBD
