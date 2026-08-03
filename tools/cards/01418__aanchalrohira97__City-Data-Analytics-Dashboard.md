---
id: tool-01418
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: City-Data-Analytics-Dashboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/aanchalrohira97/city-data-analytics-dashboard
created: 2026-07-18
updated: 2026-07-18
no: 1418
category: 二、网文 / 长篇 AI 写作系统 库
repo: aanchalrohira97/City-Data-Analytics-Dashboard
stars: 1
url: https://github.com/aanchalrohira97/city-data-analytics-dashboard
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# aanchalrohira97/City-Data-Analytics-Dashboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aanchalrohira97/city-data-analytics-dashboard
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A decision-support tool for non-technical users — city councilmembers, journalists, and policy staff — to explore government spending data without writing queries or reading raw tables.
- **本地描述**：A decision-support tool for non-technical users — city councilmembers, journalists, and policy staff — to explore government spending data without writing queries or reading raw tables.
- **拉取时间**：2026-07-23 23:20:27

---

# City Spend Analytics Dashboard

A decision-support tool for non-technical users — city councilmembers, journalists, and policy staff — to explore government spending data without writing queries or reading raw tables.

---

## The Problem

Government spending data is public, but it is not legible. A city councilmember facing a 200,000-row Excel export cannot answer "where did the money go?" without either hiring an analyst or spending hours in pivot tables. The pain is not access — the data exists. The pain is interpretation.

I chose this direction over alternatives (a generic query builder, a raw data explorer, a SQL interface) because those alternatives shift cognitive burden onto users who did not sign up to become data analysts. A journalist on deadline or a councilmember in a budget meeting needs curated views, not a blank canvas. The insight has to come to them.

I also explicitly chose not to build a free-form chat interface over the data — even though that is the obvious AI use case. The reason: public spending data requires determinism and auditability. If an AI tells a councilmember "Agency X spent $4.2M on vendor Y," that number must be verifiable and reproducible. LLMs are probabilistic. Calculations are not. So AI explains what the deterministic code already computed — it does not compute anything itself.

---

## What Was Built

### Demo

<img width="1493" height="827" alt="Screenshot 2026-06-04 at 11 59 36 PM" src="https://github.com/user-attachments/assets/91b80398-df3c-4796-b4fe-a7eb2f90c5a5" />

### Architecture

```
Excel Upload
    ↓
parseExcelFile()          — validates columns, coerces types
    ↓
PaymentRow[]              — in-memory, typed domain objects
    ↓
aggregations.ts           — pure functions: filter, group, sum, rank
    ↓
buildOverviewSummary()    — single data contract for OverviewPage
    ↓
React components          — presentational only, no business logic
    ↓
explanationService.ts     — passes precomputed summaries to Claude API
```

No database. No backend. Everything runs in the browser. The "repository layer" described in the HLD is represented by `parseExcelFile()` — in production it would be an API call to a SQL database.

### Key Decisions

**Excel upload instead of database** — enables local testing without infrastructure. The domain model and aggregation layer are identical to what a production version would use; only the data source changes.

**AI receives summaries, not rows** — `explainOverview()` and `explainVendor()` pass precomputed aggregates to Claude. The model cannot invent totals it was never given. This is FR-2.2 from the spec, implemented as a hard architectural constraint, not a prompt instruction.

**AI logging to sessionStorage** — every AI interaction is logged with timestamp, context, input summary, output text, and token count. This satisfies FR-2.4 without requiring a backend.

**Pure aggregation functions** — `computeMonthlyTrend`, `computeTopVendors`, and `buildOverviewSummary` are pure functions with no side effects. This makes them trivially testable and replaceable.

### Explicitly Deferred

- Authentication and role-based views (FR for future, per NFR-5)
- Precomputed aggregate cache (NoSQL layer from HLD TradeOffs)
- Async aggregation pipeline for large datasets
- Export / share functionality
- Year-over-year comparison view
- Admin data refresh flow

### What Would Change in Production

- Replace `parseExcelFile()` with an API call to a read-optimized SQL database
- Add a precomputed aggregates layer (Redis or DynamoDB) for common dashboard responses
- Add AI explanation caching: same view + same data = same cached explanation
- Move AI log from sessionStorage to a persistent backend table
- Add role-based views: journalist sees different defaults than a councilmember
- Add error monitoring (Sentry) and usage analytics
- Replace `fetch("https://api.anthropic.com/v1/messages")` with a server-side proxy so the API key is not exposed client-side

---

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Framework | React + TypeScript | Type safety on domain objects; Vite for fast local dev |
| Charts | Recharts | Composable, declarative, good TypeScript support |
| Excel parsing | SheetJS (xlsx) | Best-in-class browser Excel parsing |
| AI | Anthropic Claude (Sonnet 4) | Low latency, strong instruction following |
| Styling | CSS variables + inline styles | No build-time dependency, easy theming |
| Testing | Vitest | Fast, zero-config, native ESM |

---

## Getting Started

```bash
npm install
npm run dev
```

Open `http://localhost:5173`, upload your Excel file, and explore.

**Required Excel columns:**

| Column | Type | Description |
|---|---|---|
| `FY` | number | Fiscal year (e.g. 2022) |
| `FMonth` | number | Fiscal month (1–12) |
| `Agency` | string | Agency name |
| `Category` | string | Spending category |
| `SubCategory` | string | Spending subcategory |
| `Vendor` | string | Recipient name |
| `Amount` | number | Dollar amount |

Optional but recognized: `Bien`, `Agy`, `Object`, `Subobj`

### Running Tests

```bash
npm test          # run once
npm run test:watch  # watch mode
```

28 tests across aggregation logic and formatters.

---

## AI Usage Log

**Interaction 1**  
Asked: Generate the full folder structure and component tree from the HLD/LLD docs I provided.  
Got: Correct structure matching `ReactFolderStructure.md` and `ReactComponentOverview.md`. Also added a `features/` layer with hooks and selectors.  
Kept: The folder structure exactly. Rejected the hooks/selectors abstraction for this scope — added unnecessary indirection for a single-page app with in-memory data. Kept business logic in `aggregations.ts` and called it directly from pages.

**Interaction 2**  
Asked: Implement the AI explanation service so it passes precomputed summaries to the model, not raw rows.  
Got: A service that correctly formatted summaries and called the API. Also included a retry loop and streaming support.  
Kept: The summary-first approach and logging structure. Rejected streaming — adds complexity for responses that are 3–4 sentences. Rejected the retry loop — for a demo, silent failure is fine; in production this belongs in an API gateway, not client code.

**Interaction 3**  
Asked: Write vitest unit tests for aggregation functions.  
Got: Tests that covered the happy path but used `toBe` for floating-point comparisons, which would flake on rounding differences.  
Changed: Replaced `toBe` with `toBeCloseTo` for all currency assertions. Also added edge cases for empty input, which the initial tests omitted — those are the cases that actually crash production.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Project Structure

```
src/
  domain/           — types, aggregations, formatters (pure logic)
  services/         — paymentsRepository (Excel parsing), explanationService (AI)
  components/       — layout, summary cards, charts, tables, AI panel, states
  pages/            — UploadPage, OverviewPage
  test/             — aggregations.test.ts, formatters.test.ts, fixtures.ts
```
