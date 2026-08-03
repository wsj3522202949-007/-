---
id: tool-00389
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: scraperapi-n8n-automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/yhm768/scraperapi-n8n-automation
created: 2026-07-18
updated: 2026-07-18
no: 389
category: 二、网文 / 长篇 AI 写作系统 库
repo: yhm768/scraperapi-n8n-automation
stars: 1
url: https://github.com/yhm768/scraperapi-n8n-automation
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# yhm768/scraperapi-n8n-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yhm768/scraperapi-n8n-automation
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ScraperAPI + n8n Integration Guide: How to Automate Web Scraping Workflows Without Writing a Single Line of Proxy Code — Which Plan Should You Choose, How Much Does It Cost, and Is There a Free Tier? (Includes Full Plan Comparison and Setup Walkthrough)
- **本地描述**：ScraperAPI + n8n Integration Guide: How to Automate Web Scraping Workflows Without Writing a Single Line of Proxy Code — Which Plan Should You Choose, How Much Does It Cost, and Is There a Free Tier? (Includes Full Plan Comparison and Setup Walkthrough)
- **拉取时间**：2026-07-23 22:50:29

---

# ScraperAPI + n8n Integration Guide: How to Automate Web Scraping Workflows Without Writing a Single Line of Proxy Code — Which Plan Should You Choose, How Much Does It Cost, and Is There a Free Tier? (Includes Full Plan Comparison and Setup Walkthrough)

So you've been playing around with n8n, building workflows, automating your life one node at a time — and then you hit a wall. You need live web data. Real prices, real search results, real product listings. You try the built-in HTTP Request node, and half the sites you care about throw a 403 in your face. Welcome to the anti-bot wall.

This is exactly where **ScraperAPI** steps in, and honestly, the combination of ScraperAPI with n8n is one of the more underrated setups in the automation space right now.

---

**What's the Problem n8n Users Actually Run Into?**

n8n is fantastic for orchestration. It connects apps, routes data, triggers workflows — it does all that beautifully. But raw scraping is a different beast. The moment you point an HTTP node at Amazon, Google, or basically any modern e-commerce site, you're fighting:

- IP blocks and rate limiting
- JavaScript-rendered pages that return empty HTML
- CAPTCHAs and bot detection systems
- Geo-restrictions on certain content

You could spend a weekend setting up rotating proxies, configuring a headless browser, and wrestling with Puppeteer. Or you could add a single ScraperAPI node to your n8n workflow and have it working in about ten minutes.

That second option is what we're going to dig into.

---

**What Is ScraperAPI, Actually?**

ScraperAPI is a web scraping infrastructure service that abstracts away everything painful about large-scale data collection. You send it a URL. It sends you back the page content. In between, it handles:

- **Proxy rotation** — automatically switches IPs so you don't get blocked
- **CAPTCHA solving** — bypasses bot detection challenges
- **JavaScript rendering** — spins up a real browser when the page needs it
- **Geo-targeting** — lets you scrape as if you're in a specific country
- **User-agent rotation** — mimics different browsers and devices

Everything runs behind a single API endpoint. The pricing model runs on "API credits" — basically a unit system where a standard request costs 1 credit, a JS-rendered page costs 10, and more complex scenarios scale up from there.

It's been around since 2018, bootstrapped to profitability, acquired by SaaS.group, and as of 2026 it's expanded further with the acquisition of Traject Data (which added SERP and e-commerce structured data APIs to the mix). Over 10,000 companies use it. That's not a small number.

---

**ScraperAPI × n8n: The Official Integration**

This is the core of why the `scraperapi n8n` combo is worth talking about. ScraperAPI has an **official community node** built specifically for n8n — verified by the n8n team and maintained by ScraperAPI themselves. This isn't a workaround using an HTTP Request node; it's a proper first-class integration.

Installing it takes three steps on a self-hosted n8n instance:

1. Go to **Settings → Community Nodes**
2. Search for `n8n-nodes-scraperapi-official`
3. Install and restart

Once it's in, you'll find the ScraperAPI node in the node search panel.

**What the Node Can Do**

The node has two main resource types:

**1. API Resource** — Scrape any individual URL with full parameter control:
- Set the target URL
- Enable JavaScript rendering (`render=true`) for dynamic pages
- Set geo-targeting via country code (US, GB, DE, etc.)
- Choose device type (desktop or mobile)
- Toggle premium or ultra-premium proxies for hard-to-scrape sites
- Configure output format (HTML, Markdown, plain text)
- Enable `autoparse=true` to get structured JSON from supported domains

**2. Crawler Resource** — Launch full crawling jobs across entire domains:
- Set a start URL and let it follow links to a specified depth
- Define crawl budget (how many pages max)
- Use regex patterns to include or exclude specific URL patterns
- Configure callback webhooks to stream results back into your workflow
- Schedule recurring crawls (hourly, daily, weekly, monthly)

**3. MCP Server** — For AI agent workflows, ScraperAPI also provides a hosted MCP (Model Context Protocol) server at `https://mcp.scraperapi.com/mcp`. Connect it via n8n's MCP Client Tool node to let AI agents call ScraperAPI as a tool directly.

---

**Building a ScraperAPI Workflow in n8n: The Basic Setup**

Here's how a typical scraping workflow looks in n8n once you have the node installed:

**Simple scrape workflow:**

1. Add a trigger (Schedule, Webhook, or Manual)
2. Add the **ScraperAPI** node → select "API" resource
3. Enter your target URL
4. Configure parameters (enable render for JS-heavy sites, set country code if needed)
5. Connect to downstream nodes — Google Sheets, Airtable, a database, Slack, whatever

The node returns the scraped content directly as output, ready to be parsed, filtered, and routed by subsequent nodes.

**AI-powered scraping workflow:**

This is where it gets genuinely interesting. You can wire ScraperAPI into an AI agent loop:

1. **Chat Message Received** trigger
2. **AI Agent** node (set up a system prompt)
3. **OpenAI / Claude** connected as the chat model
4. **Simple Memory** node for context
5. **ScraperAPI** node connected as a Tool

Now you have a setup where you can chat with your workflow: *"Find me all product listings for mechanical keyboards under $150 on [site]"* — and the AI agent uses ScraperAPI to retrieve and parse the data using natural language instructions. The `'Let the model define this parameter'` option in the Crawler resource even lets the AI set crawling parameters automatically based on your prompt.

---

**Real-World Use Cases for ScraperAPI + n8n**

The combination unlocks a specific category of workflows that are otherwise incredibly annoying to maintain:

- **Price monitoring**: Track competitor pricing across e-commerce sites, pipe updates into a Google Sheet, trigger a Slack alert when prices drop
- **Lead generation**: Crawl business directories, extract contact info, push to a CRM
- **Market research**: Pull product reviews, ratings, and listing data across multiple platforms on a schedule
- **SERP tracking**: Monitor keyword rankings for your own or competitor domains (ScraperAPI handles Google SERP natively — 25 credits per request)
- **Real estate data**: Crawl property listing sites for location, price, and specs (one of the example workflows in the official docs)
- **News and content monitoring**: Watch specific pages for updates, extract new articles, summarize with AI
- **DataPipeline jobs**: ScraperAPI's DataPipeline feature lets you run large-scale, scheduled scraping projects — and as of July 2026, the 5× credit multiplier surcharge was removed, making DataPipeline requests cost exactly the same as standard API requests (up to 80% cheaper for previous users)

---

**Understanding the Credit System Before You Pick a Plan**

Before jumping to the pricing table, there's one thing that trips up almost every new ScraperAPI user: the credit multiplier.

The headline number on each plan ("100,000 credits") is not the number of pages you can scrape. Credits are spent according to request complexity:

| Request Type | Credits Used |
|---|---|
| Standard HTML request | 1 |
| JavaScript rendering (`render=true`) | 10 |
| Premium proxies | 10 |
| Screenshot | 10 |
| Premium + JS rendering | 25 |
| Ultra-premium proxies | 30 |
| Ultra-premium + JS rendering | 75 |
| Amazon pages | 5 |
| Google/Bing SERP | 25 |
| LinkedIn | 30 |

So a Hobby plan with 100,000 credits actually gets you:
- **100,000 plain HTML scrapes**, OR
- **10,000 JS-rendered pages**, OR
- **4,000 Google SERP requests**

Plan accordingly. For most automation workflows in n8n that involve modern JavaScript-heavy sites, assume you're working with the 10× multiplier at minimum.

---

**ScraperAPI Full Plan Comparison Table**

| Plan | Monthly Price | API Credits | Concurrent Threads | Geo-targeting | Pay-As-You-Go | Best For | Get Started |
|---|---|---|---|---|---|---|---|
| Free | $0 | 1,000/mo | 5 | — | No | Testing & exploration |  [Start Free](https://www.scraperapi.com/?fp_ref=coupons) |
| Hobby | $49/mo | 100,000 | 20 | US & EU | No | Small projects, personal workflows |  [Get Hobby](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Startup | $149/mo | 1,000,000 | 50 | US & EU | No | Low-volume scraping workflows |  [Get Startup](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Business | $299/mo | 3,000,000 | 100 | Global | No | Production-grade moderate scale |  [Get Business](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Scaling ⭐ | $475/mo | 5,000,000 | 200 | Global | ✅ Yes | Scaling operations, most popular |  [Get Scaling](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Professional | $975/mo | 10,500,000 | 300 | Global | ✅ Yes | High-volume recurring pipelines |  [Get Professional](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Advanced | $1,975/mo | 21,500,000 | 500 | Global | ✅ Yes | Continuous multi-source data pipelines |  [Get Advanced](https://www.scraperapi.com/pricing/?fp_ref=coupons) |
| Enterprise | Custom | 22M+ | 500+ | Global | ✅ Yes | Enterprise-scale, dedicated support |  [Contact Sales](https://www.scraperapi.com/?fp_ref=coupons) |

> **Save 10%** on any paid plan by switching to annual billing. The 7-day free trial includes 5,000 credits — no credit card required.

**Key differences between tiers:**
- **Free → Hobby**: 20× more credits, 4× more concurrent threads
- **Business** is the first tier with global (country-level) geo-targeting and unlimited analytics
- **Scaling** is the first tier with Pay-As-You-Go overage (no hard stop when credits run out)
- **Professional and Advanced** include priority support and routing

---

**Which Plan Actually Makes Sense for n8n Users?**

For most people reading this who are building n8n automation workflows:

**If you're just starting out or prototyping**, the free trial (5,000 credits for 7 days) is enough to validate whether the integration works for your specific targets. The permanent free tier (1,000 credits/month) is honestly quite limited — enough to test, not enough to run a real workflow.

**Hobby ($49/mo)** makes sense if your n8n workflow scrapes plain HTML sites and you're not hitting JS-heavy pages frequently. 100,000 standard requests is solid for a personal dashboard or price tracker.

**Startup ($149/mo)** is the sweet spot for solo developers or small teams running a handful of automated pipelines. 1 million credits covers a reasonable volume of mixed plain + rendered requests.

**Business ($299/mo)** is where you want to be if you need global geo-targeting — if your workflows need to scrape content as if from specific countries outside the US/EU, this is the minimum. Also unlocks unlimited analytics history, which matters for debugging pipelines.

**Scaling ($475/mo)** is the "most popular" tier for a reason — it's the first plan where you get Pay-As-You-Go safety net, meaning your n8n workflows won't just fail when you hit your credit limit. For production workflows that need reliability, this is where the guarantee kicks in.

---

**Practical Tips for Using ScraperAPI in n8n Workflows**

A few things that save you from burning credits unnecessarily:

**Test before you scale.** Use ScraperAPI's API Playground in the dashboard to check actual credit cost for any specific URL before you run a batch job. Every response also includes an `sa-credit-cost` header so you can see exactly what each request consumed.

**Don't enable rendering by default.** Only set `render=true` for pages that actually need it. Static news sites, simple product pages — those work fine without JS rendering. The 10× credit cost adds up fast on high-volume workflows.

**Use the urlcost endpoint.** There's a programmatic endpoint (`https://api.scraperapi.com/account/urlcost?api_key=...&url=...`) that returns the credit cost for a given URL before you scrape it. Useful for building cost-aware n8n workflows.

**Set spending caps.** If you're on a Pay-As-You-Go tier, configure a monthly spending cap in your dashboard. The system won't exceed it unless you change the setting — protects against runaway workflows.

**Use DataPipeline for recurring large jobs.** As of July 2026, ScraperAPI removed the 5× credit surcharge from DataPipeline, making it cost-neutral compared to standard API requests. If you have a recurring crawl you run daily or weekly, DataPipeline handles scheduling and parallelization natively — you can set it up and let it run without even involving n8n for the scheduling logic.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**The Verdict**

The `scraperapi n8n` combination genuinely delivers on what it promises. n8n handles the orchestration, routing, and integration with the rest of your stack; ScraperAPI handles the actual web access without getting blocked. The official community node makes the setup frictionless, the MCP server option opens up natural-language-driven scraping for AI workflows, and the credit-based pricing model is predictable enough to budget around once you understand the multiplier system.

The main thing to watch: don't read the headline credit numbers at face value. Calculate your effective scrapes based on the request types you'll actually be making. For a typical n8n workflow hitting modern JS-heavy sites, divide the plan's credit count by 10 to get your real page budget. Price it from there, and most plans look quite reasonable.

👉 [Start your free trial — 5,000 credits, no credit card required](https://www.scraperapi.com/?fp_ref=coupons)
