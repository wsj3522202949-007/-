---
id: tool-00442
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: scraperapi-n8n-automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/fcb30928/scraperapi-n8n-automation
created: 2026-07-18
updated: 2026-07-18
no: 442
category: 二、网文 / 长篇 AI 写作系统 库
repo: fcb30928/scraperapi-n8n-automation
stars: 1
url: https://github.com/fcb30928/scraperapi-n8n-automation
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 518eb1556c9dafd1
  - methods/最强写作方法论_全球最强综合版.md
---

# fcb30928/scraperapi-n8n-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fcb30928/scraperapi-n8n-automation
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ScraperAPI + n8n: How to Automate Web Scraping Without Writing a Single Line of Code — Setup Guide, Real-World Workflows, AI Agent Integration, and Full Plan Comparison (With the Cheapest Way to Get Started)
- **本地描述**：ScraperAPI + n8n: How to Automate Web Scraping Without Writing a Single Line of Code — Setup Guide, Real-World Workflows, AI Agent Integration, and Full Plan Comparison (With the Cheapest Way to Get Started)
- **拉取时间**：2026-07-23 22:51:59

---

# ScraperAPI + n8n: How to Automate Web Scraping Without Writing a Single Line of Code — Setup Guide, Real-World Workflows, AI Agent Integration, and Full Plan Comparison (With the Cheapest Way to Get Started)

So you've been building workflows in n8n, and at some point you run into the wall every automation builder eventually hits: you need data from the web, and the website in question has absolutely no interest in giving it to you cleanly.

Maybe you're trying to track competitor prices. Maybe you want to monitor product listings, pull SERP rankings, or feed fresh market data into your AI agent. The idea is simple. The execution is a nightmare — blocked IPs, CAPTCHAs, JavaScript walls, bot detection, rotating user agents. You spend more time fighting infrastructure than building the thing you actually wanted to build.

This is exactly the problem that **ScraperAPI + n8n** solves together. And the combination is a lot more capable than most people realize.

---

## What ScraperAPI Actually Does (And Why It Matters for n8n Users)

ScraperAPI is a web scraping API that handles all the ugly infrastructure in the background — proxy rotation across 40 million+ IPs in 50+ countries, automatic CAPTCHA solving, JavaScript rendering, anti-bot bypass, and automatic retries. You hand it a URL. It gives you the page content. That's it.

What makes it especially relevant for n8n workflows is the official ScraperAPI node, built and maintained by ScraperAPI themselves, and verified by the n8n team. It plugs directly into your workflow canvas, meaning you don't have to write HTTP request code, manage authentication, or figure out header configuration. The node handles the connection; ScraperAPI handles the messy web stuff.

Behind the scenes, every time your n8n workflow sends a URL to ScraperAPI, the service is doing a significant amount of work: selecting the right proxy from its residential or datacenter pool, rotating user agents, determining whether JavaScript rendering is needed, solving CAPTCHA if it appears, and retrying if the first attempt fails. From the n8n side, it just looks like any other node that returns data.

The company serves over 10,000 brands — including Deloitte, Sony, and Alibaba — and processes 36 billion API requests per month. The scale tells you something about the reliability of the infrastructure you're connecting to.

👉 [Get started with ScraperAPI free — 1,000 credits/month, no card required](https://www.scraperapi.com/?fp_ref=coupons)

---

## Setting Up ScraperAPI in n8n: Step by Step

Getting the integration running takes about five minutes if you know what you're doing. Here's the complete process:

**Step 1: Get your ScraperAPI key**

Sign up at ScraperAPI (👉 [free plan link here](https://www.scraperapi.com/?fp_ref=coupons)) and log into your dashboard. Your API key is displayed on the main dashboard screen. Copy it.

**Step 2: Install the ScraperAPI community node in n8n**

> **Note:** The ScraperAPI community node requires a self-hosted n8n instance. If you're on n8n Cloud, you can still use ScraperAPI via the HTTP Request node with manual configuration, or through the MCP server integration described below.

For self-hosted n8n:
1. Go to **Settings → Community Nodes**
2. Search for `n8n-nodes-scraperapi-official`
3. Install and restart n8n

**Step 3: Add the ScraperAPI node to your workflow**

1. Open an existing workflow or create a new one
2. Click the **+** button on the canvas
3. Search for **ScraperAPI** in the node search bar
4. Select and add it to your workflow

**Step 4: Configure the node**

Once the node is added, you'll connect your API key as a credential and then configure the target URL and any optional parameters. The node supports:

- **URL** (required): The page you want to scrape
- **Country Code** (optional): Two-letter ISO code for geo-targeted scraping (e.g., `US`, `GB`, `DE`)
- **Device Type** (optional): Desktop or Mobile user agent
- **Render** (optional): Set to `true` for JavaScript-heavy pages
- **Premium** (optional): Residential/mobile proxy pool for harder targets
- **Ultra Premium** (optional): Advanced bypass for the most protected sites
- **Output Format** (optional): `markdown`, `text`, or `json`
- **Autoparse** (optional): Returns structured JSON for supported domains like Amazon and Google

The node returns scraped content that flows directly into the next step in your workflow.

---

## Three Workflow Patterns That Actually Work

Here's where things get interesting. The scraperapi n8n integration supports several distinct workflow modes, each suited to different use cases.

### Pattern 1: Basic Scraping Workflow

The simplest setup — trigger → ScraperAPI node → process data → send somewhere.

This works well for:
- Monitoring a specific product page for price changes and sending a Slack notification
- Scraping a news site daily and saving summaries to a Google Sheet
- Pulling job listings from a job board and filtering by keyword

The workflow executes when triggered (scheduled, webhook, or manual), sends the URL to ScraperAPI, gets the HTML or parsed content back, and feeds it into whatever comes next — an AI summarizer, a data filter, a database write, an email sender.

### Pattern 2: AI Agent Workflow with ScraperAPI as a Tool

This is where things get genuinely interesting for people building AI-powered automations.

ScraperAPI integrates with n8n's AI Agent node as a **tool**, which means an LLM (like GPT-4o or Claude) can trigger scraping dynamically based on a user prompt, rather than scraping a hardcoded URL on a schedule.

The setup:
1. Add a **Chat Message Received** trigger
2. Add an **AI Agent** node
3. Connect an **AI Chat Model** node (OpenAI, Anthropic, etc.) to the Agent's Chat Model input
4. Connect a **Simple Memory** node to the Agent's Memory input
5. Connect the **ScraperAPI** node to the Agent's Tool input
6. Add a system prompt that tells the agent how to behave

With this pattern, a user can type something like "Find me the current price of a MacBook Pro 14-inch on Amazon" and the agent will use ScraperAPI to fetch the live page and return structured data. No manual URL hardcoding needed. The AI decides what to scrape and when.

### Pattern 3: Crawler + Webhook for Bulk Site Mapping

For larger scraping jobs — like mapping an entire website, crawling all product pages from an e-commerce store, or indexing a documentation site — ScraperAPI's Crawler resource in the n8n node lets you initiate and manage full crawl jobs directly from your workflow.

Parameters you control from the n8n node:
- **Start URL**: Where the crawl begins
- **Max Depth**: How many link levels deep to follow
- **Crawl Budget**: Maximum pages to crawl
- **URL Regex Include/Exclude**: Filter which URLs to follow or skip
- **Callback Webhook URL**: Where ScraperAPI streams results as they arrive
- **Schedule Interval**: Once, hourly, daily, weekly, or monthly

The crawler runs asynchronously — it doesn't block your workflow. Results stream to your webhook endpoint as pages are processed, and you can poll job status with a Get Job Status operation.

---

## The MCP Server Option: n8n + ScraperAPI for AI Agents

If you're running n8n Cloud or prefer not to install community nodes, there's a third integration path: ScraperAPI's hosted **MCP (Model Context Protocol) server**.

The MCP server lets AI models and agents interact with ScraperAPI through a standardized protocol. In n8n, you connect it via the **MCP Client Tool** node:

- **Endpoint**: `https://mcp.scraperapi.com/mcp`
- **Server Transport**: HTTP Streamable
- **Authentication**: Bearer Auth (your ScraperAPI API key)
- **Tools to include**: All, or select specific tools

If you prefer self-hosting the MCP server, ScraperAPI maintains an open-source [scraperapi-mcp repository](https://github.com/scraperapi/scraperapi-mcp) with full setup instructions.

This path doesn't require community node installation and works on cloud-hosted n8n, making it the easier option for teams who don't manage their own n8n infrastructure.

---

## Understanding ScraperAPI's Credit System Before You Pick a Plan

Before committing to a plan, you need to understand how ScraperAPI actually bills — because "100,000 API credits" doesn't mean what it sounds like it means.

ScraperAPI uses a **credit multiplier system**. Every request costs a base number of credits depending on what type of request it is and which features you enable:

| Request Type | Credits per Request |
|---|---|
| Standard request (plain HTML) | 1 |
| `render=true` (JavaScript rendering) | 10 |
| `premium=true` (residential proxy) | 10 |
| `screenshot=true` | 10 |
| `premium=true` + `render=true` | 25 |
| `ultra_premium=true` | 30 |
| `ultra_premium=true` + `render=true` | 75 |
| Cloudflare / bot-blocker bypass | 10 |

And for certain domains, the cost is fixed regardless of other parameters:

| Domain | Credits per Request |
|---|---|
| Amazon (e-commerce) | 5 |
| Google / Bing SERP | 25 |
| LinkedIn | 30 |

The practical implication: a 100,000-credit Hobby plan gives you 100,000 plain HTML scrapes, or 10,000 JavaScript-rendered pages, or 4,000 Amazon products, or just 1,333 ultra-premium + JS-rendered requests. Real-world workflows almost always use some combination of features, so your actual monthly capacity will be somewhere in between.

The other thing to know: credits **don't roll over**. Unused credits expire at the end of each billing cycle. And Pay-As-You-Go overage (continuing after you hit your credit limit) is only available on the Scaling plan and above — Hobby, Startup, and Business users get cut off until the next billing period.

---

## Full ScraperAPI Plan Comparison

ScraperAPI offers a free forever plan plus six paid tiers (with a 10% discount on annual billing). Here's the complete breakdown:

| Plan | Monthly Price | Annual Price (per mo) | API Credits | Concurrent Threads | Geotargeting | Pay-As-You-Go | Purchase |
|---|---|---|---|---|---|---|---|
| **Free** | $0 | — | 1,000 | 5 | None | No |  [Sign Up Free](https://www.scraperapi.com/?fp_ref=coupons) |
| **Hobby** | $49/mo | ~$44/mo | 100,000 | 20 | US & EU only | No |  [Get Hobby Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Startup** | $149/mo | ~$134/mo | 1,000,000 | 50 | US & EU only | No |  [Get Startup Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Business** | $299/mo | ~$269/mo | 3,000,000 | 100 | Global (50+ countries) | No |  [Get Business Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Scaling** | $475/mo | ~$427/mo | 5,000,000 | 200 | Global | Yes |  [Get Scaling Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Professional** | $975/mo | ~$877/mo | 10,500,000 | 300 | Global | Yes |  [Get Professional Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Advanced** | $1,975/mo | ~$1,777/mo | 21,500,000 | 500 | Global | Yes |  [Get Advanced Plan](https://www.scraperapi.com/?fp_ref=coupons) |
| **Enterprise** | Custom | Custom | 22M+ | 500+ | Global + dedicated support | Yes |  [Contact Sales](https://www.scraperapi.com/?fp_ref=coupons) |

**Key differences between tiers:**
- **Geotargeting beyond US & EU** requires the Business plan ($299/mo) or higher
- **Pay-As-You-Go overage** only activates on Scaling ($475/mo) and above
- **Priority support** comes with Professional, Advanced, and Enterprise plans
- **Unlimited analytics history** starts at the Business plan (lower tiers get 30 days)
- **Annual billing saves 10%** across all paid plans

For most n8n automation builders just getting started, the **Hobby plan at $49/mo** is the natural entry point. It gives you 100,000 credits and 20 concurrent threads — more than enough for moderate-scale scraping workflows. If you're scraping JavaScript-heavy pages, budget for 10x credit burn and plan accordingly.

---

## What Real ScraperAPI Users Say

ScraperAPI has a 4.5/5 rating on Trustpilot across 42 reviews, a 4.6/5 on Capterra across 62 reviews, and a 4.4/5 on G2. The Capterra Ease of Use rating sits at an impressive 4.9/5 — which tracks with the n8n integration experience specifically, since the node abstracts away essentially all setup complexity.

The things people consistently praise:
- Simple setup and excellent documentation
- Strong performance on Amazon, Google SERP, Zillow, and Etsy
- Proxy pool reliability and CAPTCHA handling
- Responsive customer support

The things that trip people up:
- The credit multiplier system — specifically the non-obvious cost stacking when combining features (premium + render costs 25 credits, not 10+10=20)
- Credits expiring at month end with no rollover
- Zero success rates on Instagram, Twitter/X, and Booking.com
- A forced 10-minute result cache on difficult targets, which can mean stale data

For the scraperapi n8n use case specifically, the combination works very well for structured scraping tasks — market monitoring, SERP tracking, product data collection, research automation. Where it runs into trouble is social media and login-required sites, which are off-limits by design.

---

## Where ScraperAPI Performs Best (Site-Specific Success Rates)

Independent benchmarks from Scrapeway (April 2026) showed the following performance across common scraping targets:

| Target Site | Success Rate | Notes |
|---|---|---|
| Zillow | 100% | Real estate data, excellent |
| Etsy | 99% | E-commerce, very reliable |
| Amazon | 98% | Structured data endpoints available |
| LinkedIn | 95% | Works but costs 30 credits/request |
| Walmart | 93% | Good with structured endpoints |
| Indeed | 90% | Job board, solid |
| StockX | 84% | Moderate |
| Realtor.com | 12% | Struggles |
| Instagram | 0% | Doesn't work |
| Booking.com | 0% | Doesn't work |
| Twitter/X | 0% | Doesn't work |

The pattern is clear: ScraperAPI excels on e-commerce and real estate, performs reasonably on job boards, and completely fails on social media platforms with sophisticated anti-bot infrastructure. For n8n workflows targeting Amazon data, SERP monitoring, or real estate listings, it's a highly reliable choice.

---

## The 7-Day Free Trial: How to Use It Well

ScraperAPI gives new users a **7-day trial with 5,000 credits** on top of the permanent 1,000-credit free plan. That's enough to meaningfully test the integration.

Here's how to use those 5,000 trial credits strategically:

1. **Test your specific target sites first.** Don't just run generic examples — scrape the actual URLs your workflow will hit. This tells you which credit multipliers apply and what your real monthly burn rate looks like.

2. **Test with and without JavaScript rendering.** Many pages look like they load static HTML but actually need `render=true` for the content you care about. Test both and see what the response contains.

3. **Check geotargeting requirements.** If your workflow needs to scrape from specific countries, note that global geotargeting only unlocks on Business plan and above.

4. **Build one complete n8n workflow end-to-end.** Don't just ping the API standalone — connect it in an actual workflow, process the output, and make sure the data flows cleanly into whatever comes next (a Google Sheet, an AI summarizer, a Slack message, a database).

5. **Calculate your real monthly credit need.** Track exactly how many credits each run consumes, multiply by your expected run frequency, and add a 20% buffer. That's your realistic plan requirement.

👉 [Start your free trial — no credit card required](https://www.scraperapi.com/?fp_ref=coupons)

---

## ScraperAPI vs. DIY Scraping in n8n: The Honest Comparison

n8n has a built-in HTTP Request node that can technically hit any URL. So why not just use that?

The short answer: the HTTP Request node works fine for APIs and simple, static pages. It fails — predictably and often — on anything with bot protection, JavaScript rendering, IP-rate limiting, or CAPTCHA challenges.

When you route requests through ScraperAPI, you're buying:
- **Proxy rotation**: Your request comes from one of 40M+ IPs, so IP bans don't stick
- **CAPTCHA solving**: Handled automatically in the background
- **JavaScript rendering**: Headless browser spin-up without you managing any infrastructure
- **Anti-bot bypass**: Cloudflare, DataDome, PerimeterX handling built in
- **Automatic retries**: Failed requests retry automatically; you only pay for successes (200 and 404 responses)

For an n8n workflow that needs to run reliably on a schedule — not just once — that infrastructure matters a lot. A DIY approach that works 70% of the time becomes a constant source of workflow failures and debugging sessions. ScraperAPI handling the infrastructure means your n8n workflow can stay focused on what happens *with* the data, not on fighting for access to it.

---

## Frequently Asked Questions

**Can I use ScraperAPI with n8n Cloud?**

Yes, through the MCP server integration. The community node requires a self-hosted n8n instance, but the MCP Client Tool works on n8n Cloud — just configure the endpoint `https://mcp.scraperapi.com/mcp` with Bearer Auth using your ScraperAPI API key.

**Does ScraperAPI work with AI agents in n8n?**

Yes. You can connect the ScraperAPI node as a tool to n8n's AI Agent node. This lets an LLM decide which URLs to scrape based on user prompts, making it possible to build conversational data-retrieval workflows.

**How many credits does a typical n8n workflow use?**

It depends entirely on your targets and feature configuration. A simple HTML scrape costs 1 credit. A JavaScript-rendered page costs 10. An Amazon product page via the Structured Data Endpoint costs 5. A Google SERP costs 25. Build a test workflow and measure actual consumption before choosing a plan.

**What happens when I run out of credits mid-month?**

On Hobby, Startup, and Business plans, the service stops until the next billing cycle. On Scaling and above, you can continue with Pay-As-You-Go at a fixed per-credit rate. If reliable uptime matters to your workflow, the Scaling plan's PAYG overage is worth considering.

**Is there a free plan permanently?**

Yes. ScraperAPI offers a permanent free tier with 1,000 credits per month and up to 5 concurrent connections. New signups also get a 7-day trial with 5,000 additional credits to evaluate at larger scale.

**Do unused credits roll over?**

No. Credits expire at the end of each billing cycle and don't accumulate.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## The Bottom Line

The scraperapi n8n integration is one of the cleaner data-layer additions you can make to an n8n automation stack. The official node is actively maintained, the documentation is thorough, the AI Agent tool integration is genuinely useful, and the underlying proxy/rendering infrastructure handles the hard parts reliably.

The thing to go in knowing: the credit system requires a little math before you commit to a plan. Your real monthly capacity depends on which features and domains you're hitting, not just the headline credit number. Run the calculation for your specific use case — multiplied by your actual workflow frequency — and pick the plan that covers it with some buffer.

If you're building market monitoring workflows, AI research pipelines, competitive intelligence automations, or any kind of scheduled data collection in n8n, ScraperAPI is one of the most straightforward ways to make those workflows work reliably in the real web.

The free plan and 7-day trial give you everything you need to test that properly before spending anything.

👉 [Get started with ScraperAPI — free plan, no card required](https://www.scraperapi.com/?fp_ref=coupons)
