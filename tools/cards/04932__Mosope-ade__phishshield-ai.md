---
id: tool-04932
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: phishshield-ai
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/mosope-ade/phishshield-ai
created: 2026-07-18
updated: 2026-07-18
no: 4932
category: 一、去 AI 味 / Humanizer 库
repo: Mosope-ade/phishshield-ai
stars: 0
url: https://github.com/mosope-ade/phishshield-ai
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: afdd7224b28eccf7
  - methods/改稿润色指令库.md
---

# Mosope-ade/phishshield-ai

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mosope-ade/phishshield-ai
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A free phishing and scam detector analyzing text, links, screenshots, and QR codes . Powered by AI, domain heuristics, and VirusTotal.
- **本地描述**：A free phishing and scam detector analyzing text, links, screenshots, and QR codes . Powered by AI, domain heuristics, and VirusTotal.
- **拉取时间**：2026-07-25 17:59:54

---

# HookCheck

HookCheck is a free, public, privacy-first decision-support platform designed to protect users from social engineering attacks by detecting phishing and scams instantly. The application is built for general public use, requiring no user accounts, no login, and storing no personal data.

Users can submit suspicious messages, URLs, screenshots of messages/emails, or QR codes. The platform processes the input, aggregates multi-layered security indicators, and explains its reasoning in clear, plain language.

---

## The Three-Layer Detection Architecture

A core design law of HookCheck is that no single layer of evidence ever silently overrides another. Every report displays findings separately by their source so that users can make informed security decisions.

### 1. Deterministic Heuristics Layer (Uninjectable)
The first layer runs entirely server-side without external network calls. Because it is deterministic, it cannot be bypassed or fooled by adversarial text instructions (prompt injections). It checks for:
- **Typosquatting & Homoglyphs**: Calculates edit distances (Levenshtein ≤ 2) against the top 1M domains and flags Unicode substitutions that spoof popular brand domains.
- **Brand Subdomain Impersonation**: Flags when trusted brand names appear in subdomains of untrusted registered domains (e.g., `paypal.com.login-verify.ru`).
- **TLD & URL Features**: Identifies suspicious top-level domains commonly used in phishing, excessive URL length, known shorteners, HTTP connections, and credential-harvesting keywords.

### 2. Large Language Model (LLM) Layer
A Large Language Model analyzes the semantic intent of messages, images, and page content.
- **Social Engineering Markers**: Inspects text for urgency, fear tactics, payment requests, unrealistic rewards, or tone inconsistencies.
- **Prompt-Injection Defense**: Delimits user-influenced input safely and explicitly instructs the model to treat content as data, never as commands.
- **Pydantic Validation**: All raw outputs from the LLM are strictly validated against a server-side schema before ingestion.

### 3. VirusTotal Reputation Layer
Integrates VirusTotal's public registry to check domains and file hashes against 70+ antivirus engines.
- **Corroborating Evidence**: VirusTotal is treated as supportive data — a "clean" result does not suppress strong flags raised by heuristics or AI, preventing newly registered phishing campaigns from bypassing detection.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Core Product Features

- **Unified Submission Surface**: A single interface that automatically detects input types. Paste text, paste a URL, or drop an image. No manual mode selectors.
- **QR Code & Screenshot Processing**: Decodes QR codes ("quishing" protection) and falls back to OCR text extraction for screenshots, passing the payloads through the full analysis pipeline.
- **File Hash Lookup**: Computes SHA-256 hashes of files on upload to query VirusTotal reputations without ever storing or uploading the raw file content.
- **Privacy-First Cache**: Analysis results are cached for up to 24 hours using only SHA-256 hashes of normalized inputs. Raw user submissions are never persisted.
- **Verdict-First User Interface**: Visual presentation displaying a clear threat badge (Low, Medium, High, Critical) and plain-language summary, followed by granular evidence panels and safety recommendations.
- **Security-Minded Permalinks**: Analysis reports can be shared via non-sequential, randomly generated slug URLs. All report pages are marked `noindex` to keep search engines from indexing them.
