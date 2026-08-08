---
id: tool-00358
type: tool
area: 库
status: active
tags: [TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: uipath-invoice-reporting-automation
summary: 小说转语音/有声书
source: https://github.com/andrewphillipsjr2-0/uipath-invoice-reporting-automation
created: 2026-07-18
updated: 2026-07-18
no: 358
category: 二、网文 / 长篇 AI 写作系统 库
repo: andrewphillipsjr2-0/uipath-invoice-reporting-automation
stars: 0
url: https://github.com/andrewphillipsjr2-0/uipath-invoice-reporting-automation
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a83ec98bb9b08adb
  - methods/最强写作方法论_全球最强综合版.md
---

# andrewphillipsjr2-0/uipath-invoice-reporting-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/andrewphillipsjr2-0/uipath-invoice-reporting-automation
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：RPA workflow built in UiPath Web Studio that automates invoice data extraction and reporting. Uses Document Understanding to extract key fields from invoices and GenAI to generate purchase descriptions, writing results to Google Sheets automatically.
- **本地描述**：RPA workflow built in UiPath Web Studio that automates invoice data extraction and reporting. Uses Document Understanding to extract key fields from invoices and GenAI to generate purchase descriptions, writing results to Google Sheets automatically.
- **拉取时间**：2026-07-23 22:49:33

---

# Automation of Invoice Reporting with UiPath Web Studio

**RPA workflow built in UiPath Web Studio** that automates invoice data extraction and reporting for finance teams. Uses Document Understanding to extract key fields from PDF invoices and GenAI Content Generation to write purchase descriptions automatically — eliminating manual data entry entirely.

> **TripleTen AI Automation Program — Project 6 | May 2026**
>
> ---
>
> ## 🔗 View the Project
>
> - **Live Workflow (UiPath Cloud):** [View in UiPath Studio](https://cloud.uipath.com/triplvfhsfud/studio_/designer/d4812e7e-f6d7-4819-bcbf-3b6bc3c4f37c?solutionId=8f19b40e-a442-44d8-e8d7-08deb80f2a16&fileId=0ff6ecc2-093c-4a6a-a462-3fff06024234)
> - - **Presentation Deck:** [Google Slides](https://docs.google.com/presentation/d/1Z-PM9QrQsnHR-1VKLpVynXMug7ujc0RSXR5BrrXxpmM/edit)
>   - - **Output Spreadsheet:** [Google Sheets](https://docs.google.com/spreadsheets/d/1dqEP4exGwwaUG94ow3nTlitULoJIFgtTNWli_jH11MU/edit)
>    
>     - ---
>
> ## The Problem
>
> Finance managers had to manually open each invoice, copy four fields (Invoice Number, Supplier, Due Date, Total Amount) into a spreadsheet, and write a purchase description by hand. Done weekly across all incoming invoices, the process was slow, inconsistent, and error-prone — a textbook candidate for automation.
>
> ---
>
> ## The Solution
>
> An RPA workflow in UiPath Web Studio that handles the entire pipeline automatically:
>
> 1. **Read** invoice files from Google Drive
> 2. 2. **Extract** 4 key fields using Document Understanding (Invoice Number, Supplier, Due Date, Total Amount)
>    3. 3. **Filter** invoices due on or before September 22, 2025
>       4. 4. **Generate** a short AI purchase description using GenAI Content Generation (≤5 words)
>          5. 5. **Write** all results to Google Sheets
>             6. 6. **Flag** low-confidence extractions (Invoice Number confidence < 0.7) with a warning log for manual review
>               
>                7. ---
>               
>                8. ## Workflow Architecture
>               
>                9. ```
> Google Drive (Invoices)
>         ↓
>   [For Each File]
>         ↓
>   Document Understanding
>   (Extract: Invoice #, Supplier, Due Date, Amount)
>         ↓
>   Confidence Check (Invoice # < 0.7 → Log Warning)
>         ↓
>   Date Filter (Due Date ≤ Sept 22, 2025)
>         ↓
>   GenAI Content Generation (Purchase Description)
>         ↓
>   Google Sheets (Write Row)
> ```
>
> ---
>
> ## Key Features
>
> | Feature | Implementation |
> |--------|----------------|
> | Document Extraction | UiPath Document Understanding |
> | AI Description Generation | GenAI Content Generation Activity |
> | Confidence-Based QA | If condition on Invoice # confidence score |
> | Date Filtering | Due date comparison against Sept 22, 2025 threshold |
> | Output | Google Sheets via Write Row activity |
>
> ---
>
> ## Results
>
> - ✅ Workflow ran end-to-end without errors
> - ✅ Successfully populated 5 rows of invoice data
> - ✅ Generated AI-written purchase descriptions (≤5 words each)
> - ✅ Confidence-based warning logic triggered correctly for low-quality extractions
> - ✅ Zero manual data entry required
>
> ---
>
> ## Tools & Technologies
>
> - **UiPath Web Studio** — Workflow automation and orchestration
> - **UiPath Document Understanding** — Invoice field extraction
> - **UiPath GenAI Content Generation** — AI-powered description writing
> - **Google Drive** — Invoice file source
> - **Google Sheets** — Automated output destination
>
> ---
>
> ## Files in This Repository
>
> | File | Description |
> |------|-------------|
> | `Main.xaml` | Core UiPath workflow — invoice extraction, filtering, AI description, and Sheets output |
> | `project.json` | UiPath project configuration and dependencies |
> | `README.md` | Project documentation |
>
> ---
>
> ## What I Would Improve With More Time
>
> - Resolve the Due Date type issue so the date filter uses a real `DateTime` comparison instead of a `True` placeholder
> - Add `Try/Catch` error handling around the Write Row activity
> - Test with more diverse invoice formats to ensure the extractor generalizes across vendors
> - Add email notification for flagged low-confidence invoices
>
> related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
>
> ## About
>
> Built as part of the **TripleTen AI Automation Program** (Certificate expected 2026).
> Portfolio: [github.com/andrewphillipsjr2-0](https://github.com/andrewphillipsjr2-0)
> LinkedIn: [linkedin.com/in/andrew-phillips-jr](https://www.linkedin.com/in/andrew-phillips-jr/)
