---
id: tool-01391
type: tool
area: 库
status: active
tags: [RAG, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: governance-knowledge-assistant
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/damitechprojects/governance-knowledge-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1391
category: 二、网文 / 长篇 AI 写作系统 库
repo: damitechprojects/governance-knowledge-assistant
stars: 0
url: https://github.com/damitechprojects/governance-knowledge-assistant
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9cceff62ec1687dd
  - methods/最强写作方法论_全球最强综合版.md
---

# damitechprojects/governance-knowledge-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/damitechprojects/governance-knowledge-assistant
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：How I built a RAG-based AI governance research assistant using Microsoft Copilot Studio, without writing any code.
- **本地描述**：How I built a RAG-based AI governance research assistant using Microsoft Copilot Studio, without writing any code.
- **拉取时间**：2026-07-23 23:19:41

---

# How I Built a Governance AI Research Assistant (Without Writing Any Code)

I'm a Governance Professional, not a developer. This is my first GitHub repository, and I'm sharing it because when I was trying to figure out how to build this, I couldn't find anyone in the governance or company secretarial space who had documented their experience with AI agents. So here it is: what I built, why, and what I learned along the way.

---

## Why I Built This

I work in a Company Secretarial team of three people. We support a company governed by both UK company law (Companies Act 2006) and Spanish securities regulation (CNMV rules, Código de Buen Gobierno), as it is listed in Spain.

That dual-jurisdiction setup means that almost every governance question requires checking two sets of rules. "Does our Board composition comply with both UK and Spanish diversity requirements?" sounds like one question, but it means pulling out the Board Regulations, mapping against the UK Companies Act provisions, then cross-referencing with the CNMV's Good Governance Code recommendations, and finally checking whether our Articles of Association add any additional requirements on top. That's three or four documents across two legal frameworks for a single query.

We were spending somewhere between 80 and 120 hours a year just on routine governance research, the kind of queries where the answer is sitting in a document somewhere, but finding the right document and the right clause takes time. On top of that, we were spending between €4k and €12k a year asking external lawyers questions we could have answered ourselves if we'd had faster access to our own governance library. Bear in mind that these figures are approximative estimates.

I wanted to see if I could build an AI assistant that could search our governance documents and give me a grounded, cited answer in seconds instead of minutes.

---

## What I Used

I built this in **Microsoft Copilot Studio**, which is Microsoft's low-code platform for building AI agents. I chose it because our company already uses Microsoft 365, so the integration with SharePoint (where our governance documents live) and Teams (where my team works every day) was built in. No APIs, no Python, no infrastructure to manage.

The underlying model is **GPT-5 Chat** (Generally Available). I'll explain why I chose that specific model later, as it was actually one of the more important decisions.

---

## How It Works

The basic idea is something called Retrieval-Augmented Generation, or RAG. In plain English:

1. I type a governance question in Teams
2. The agent searches the team's SharePoint document library for relevant passages
3. It also checks three specific regulatory websites (more on that below)
4. GPT-5 Chat reads the retrieved passages and writes an answer
5. The answer includes citations so I can verify it myself

The agent doesn't make things up from its general training data. I disabled that. It can only answer from the documents and websites I've pointed it at. If it can't find an answer, it says so.

---

## The Documents

I set up a SharePoint document library with our core governance documents organised into folders:

- **Constitutional Documents**: Articles of Association, Board Regulations
- **Policies & Codes**: Share Dealing Code, Disclosure Policy
- **Regulatory Frameworks**: Good Governance Code compliance mapping
- **Delegation & Authority**: Approval Matrix

As I was building this solution, there were a few things I learned the hard way about the document library:

- **Use descriptive filenames.** The agent's search is only as good as the documents you give it. "ToR_v3_FINAL.docx" is useless. "Audit_Risk_Committee_Terms_of_Reference_2025.docx" works much better.
- **Remove old versions.** The agent doesn't know which version of a document is current. If you leave a superseded Terms of Reference in the library, it might cite the old quorum requirement instead of the new one.
- **Text-based files only.** Scanned PDFs that are just images won't work because the semantic search can't read them. Make sure everything is proper text-based PDF or DOCX.
- **Expect a 24 to 48 hour delay.** After you upload documents to SharePoint, the agent needs time to index them. Don't upload your documents and immediately start testing. You'll think the agent is broken when it's just not finished indexing.

---

## What I Deliberately Left Out

This was as important as what I put in.

**Board and Committee minutes.** I didn't include these, even though they're one of the most frequently referenced governance documents. The risk was too high for a first version of the agent. Minutes contain commercially sensitive Board deliberations, and different users should have access to different committees' minutes. I didn't want the agent accidentally surfacing something a user shouldn't see, even within our small team. This is planned for a later phase once I've validated the access controls.

**Full legislation.** I didn't upload the entire Companies Act 2006 or Spanish Royal Decrees. These are massive documents where very similar language appears thousands of times. If you ask about director duties, the agent pulls back dozens of passages that mention "director" and "duty" but aren't the ones you actually need. That noise makes the answers worse, not better. Instead, I rely on curated summaries in our governance documents and scoped web search to the official legislation websites when needed.

**The model's own knowledge.** Copilot Studio lets the agent fall back on GPT-5 Chat's general training data when it can't find an answer in the documents. I turned this off. For governance work, an AI that confidently answers a question about Spanish securities law from its training data (which might be outdated or wrong) is more dangerous than one that says "I don't know." The honest "I couldn't find this" is the feature.

---

## Web Search: Scoped, Not Open

This was one of the decisions I thought hardest about. I wanted the agent to be able to check the latest regulatory content (CNMV publishes new circulars regularly, for example) but I didn't want it pulling in random governance blog posts or AI-generated legal commentary.

The solution was to enable web search but restrict it to exactly three websites:

| Domain | What It Is |
|--------|-----------|
| legislation.gov.uk | UK primary and secondary legislation |
| cnmv.es | Spanish securities regulator |
| boe.es | Spanish Official Gazette |

The system prompt then tells the agent: search internal documents first, only use web search for external regulation, and always cite the source URL. This way, every web-sourced claim links back to an official regulatory body, not someone's blog.

---

## Why I Chose GPT-5 Chat

Copilot Studio gives you a choice of models. When I was setting this up, the options were:

| Model | Status | Why I Didn't Pick It (or Did) |
|-------|--------|-------------------------------|
| GPT-4.1 | Generally Available | Solid and stable, but previous generation. GPT-5 Chat is meaningfully better at following complex instructions. |
| **GPT-5 Chat** | **Generally Available (EU & US)** | **This is what I chose.** Best combination of improved reasoning with production stability. Processes data within the EU. |
| GPT-5 Auto | Preview | Clever concept: it routes between a fast model and a reasoning model automatically. But "preview" means it's not recommended for production, can have variable quality and latency spikes, and might process data outside your region. |
| GPT-5 Reasoning | Preview | Deep reasoning model, but same preview limitations. Also overkill for most of my queries, which are straightforward lookups. |
| RL FineTuned O4 Mini | Experimental | The least mature option. Experimental models can be discontinued at any time. Not what you want for a governance tool people rely on. |

The key insight: **for a governance agent, reliability matters more than capability.** GPT-5 Chat is "good enough" for every query type I need, and it won't randomly time out or give inconsistent results. I can always upgrade to GPT-5 Auto once it reaches GA.

---

## The System Prompt

The system prompt is doing most of the heavy lifting. Here's the logic behind how I structured it:

1. **Role definition**: "You are a specialist governance research assistant for a dual-jurisdiction company." This stops the agent from behaving like a general chatbot.
2. **Search hierarchy**: "Search internal documents first. Only use web search for external regulation." This prevents the agent from going to the web when the answer is already in our documents.
3. **Mandatory citations**: "Every factual claim must cite the source document name and section, or the source URL." This is the main defence against hallucination. If the agent cites "Board Regulations, Section 12.3" and that section doesn't say what the agent claims, I catch it immediately.
4. **Never fabricate**: "Never fabricate or infer information that is not in your knowledge sources." Explicit and non-negotiable, in my first medium post I talk about the risks of AI models hallucinating, so this step was very important to mitigate that risk.

---

## Testing

Copilot Studio has a built-in evaluation feature. I created a test set of 10 governance queries pulled from real scenarios our team deals with mixed levels of complexity. You can import these as a CSV and the platform grades the agent's responses automatically for relevance, completeness, and whether the answer is grounded in actual sources.

One thing that caught me out: **you have to publish the agent before running evaluations.** Evaluations run against the published version, not the draft. I spent a while troubleshooting errors on every test question before realising the agent simply wasn't published yet.

---

## How I'm Measuring Impact

I'm being honest here. I'm early in deployment, so I don't have months of data yet. But here's how I'm tracking things practically:

- **Before and after timing.** I noted how long common queries take manually (10 to 15 minutes for a quick lookup, 30 to 60 minutes for a medium one, half a day for complex cross-jurisdictional analysis). When the agent answers the same question in 15 seconds, the time saving speaks for itself.
- **Thumbs up/down.** Every response in Teams has a feedback button. Copilot Studio aggregates this automatically. My target is 80% positive over time.
- **Built-in analytics.** Copilot Studio tracks conversations, users, query themes, and satisfaction automatically from the moment you publish. No setup required.

---

## Responsible AI: The Agent Card

I created an "Agent Card" for this project, a document adapted from the AWS Model Card framework (a concept I learned during my AWS Certified AI Practitioner exam prep) that records everything about the agent in one place: what it does, what model it uses and why, what knowledge sources are connected (and which ones were deliberately excluded), the guardrails, known limitations, bias considerations, and how it's governed over time.

I did this for two reasons. First, it forces you to think through risks you'd otherwise miss. Writing down "this agent cannot access Board minutes" alongside the reason and the future plan is very different from just not including them and hoping nobody asks. Second, if you're working in a regulated environment, this is exactly the kind of documentation that governance committees and auditors want to see. 

---

## Lessons I'd Pass On

1. **The documents matter more than the model.** You can have the most advanced model available, but if your SharePoint library is a mess of duplicate files with vague names, the agent will give bad answers. I spent more time cleaning up documents than configuring the agent.

2. **Decide what to leave out.** It's tempting to throw everything into the knowledge bank. Don't. Every document you add is another place for retrieval noise. Be deliberate about what goes in and document what you excluded and why.

3. **"I don't know" is the most important answer.** Disabling general knowledge felt limiting at first. But the first time the agent says "I could not find this in the available sources," you realise that's exactly the behaviour you want from a governance tool.

4. **Pick a GA model for production.** Preview and experimental models are fun to test with, but for an agent your team relies on daily, you need something that won't time out, give inconsistent results, or get discontinued. You can always upgrade later.

5. **Publish before you test.** Evaluations in Copilot Studio run against the published version. I wasted time debugging "errors" that were just the agent not being published yet.

6. **Start measuring from day one.** Even if it's just noting how long a query takes manually before you have the agent. That baseline is what makes your impact story credible later.

7. **You don't need to be a developer.** I built this entire agent (the knowledge sources, the system prompt, the evaluation framework, the responsible AI documentation) without writing any code. If you understand your domain deeply, that's the hard part. The tooling is the easy part.

---

## What's In This Repository

```
├── README.md                          # This file
├── docs/
│   ├── UC03_Build_Guide.docx          # Step-by-step build guide (8 phases)
│   ├── UC03_Agent_Card.docx           # Responsible AI documentation
│   └── UC03_How_To_Use_Guide.pptx     # 2-slide infographic for team onboarding
├── evaluation/
│   └── UC03_Governance_Test_Set.csv   # 16 test cases for agent evaluation
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## A Note on This Being My First Repository

If you're a developer reading this, you'll probably notice this isn't structured like a typical code repository. There's no source code, no CI/CD pipeline, no package.json. This is a documentation repository for a no-code AI agent, and I'm sharing it because I think the governance and company secretarial community needs more people documenting what they're building with AI, not fewer.

If you're a governance professional reading this and thinking about building something similar, feel free to use anything here as a starting point. And if you have questions, open an issue. I'm still learning how GitHub works, but I'll do my best to respond.
