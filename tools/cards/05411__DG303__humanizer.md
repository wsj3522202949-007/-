---
id: tool-05411
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/dg303/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5411
category: 一、去 AI 味 / Humanizer 库
repo: DG303/humanizer
stars: 0
url: https://github.com/dg303/humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# DG303/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/dg303/humanizer
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Remove signs of AI-generated writing from text. Fork of blader/humanizer with an LLM-judge eval harness.
- **本地描述**：Remove signs of AI-generated writing from text. Fork of blader/humanizer with an LLM-judge eval harness.
- **拉取时间**：2026-07-25 18:17:35

---

# Humanizer

A portable agent skill that removes signs of AI-generated writing from text, making it sound more natural and human. It is plain Markdown, so it can run in any harness that supports skill-style instructions.

This is a fork of [blader/humanizer](https://github.com/blader/humanizer) that adds an LLM-judge eval harness and eval-driven prompt improvements.

## Installation

### Skills CLI

Install with the cross-agent skills CLI:

```bash
npx skills add DG303/humanizer
```

Update an existing install:

```bash
npx skills update humanizer
```

To install into every supported agent harness:

```bash
npx skills add DG303/humanizer --agent '*'
```

To target one configured harness, pass its agent name:

```bash
npx skills add DG303/humanizer --agent <agent-name>
```

### Claude Code plugin

Claude Code users can also install Humanizer as a plugin:

```
/plugin marketplace add DG303/humanizer
/plugin install humanizer@humanizer
```

The skills are then invoked as `/humanizer:humanizer` (rewrite) and `/humanizer:ai-check` (score without editing).

### Manual

Any agent harness can use the skill directly because the runtime artifact is `SKILL.md`. Install it wherever your harness expects skill directories, or copy `skills/humanizer/SKILL.md` into an existing skill folder.

For example:

```bash
git clone https://github.com/DG303/humanizer.git /tmp/humanizer
cp -r /tmp/humanizer/skills/humanizer /path/to/your/skills/humanizer
```

Or, if you already have this repo cloned:

```bash
mkdir -p /path/to/your/skills/humanizer
cp skills/humanizer/SKILL.md /path/to/your/skills/humanizer/
```

## Usage

Invoke the skill however your agent harness exposes installed skills. Common forms include a slash command or a direct request:

```
/humanizer

[paste your text here]
```

```
Please humanize this text: [your text]
```

### Voice Calibration

To match your personal writing style, provide a sample of your own writing:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

The skill will analyze your sentence rhythm, word choices, and quirks, then apply them to the rewrite instead of producing generic "clean" output.

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.

The skill also includes a final "obviously AI generated" audit pass and a second rewrite, to catch lingering AI-isms in the first draft.

### Key Insight from Wikipedia

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 42 Patterns Detected (with Before/After Examples)

### Content Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | "was established in 1989 to collect regional statistics" |
| 2 | **Notability name-dropping** | "cited in NYT, BBC, FT, and The Hindu" | "In a 2024 NYT interview, she argued..." |
| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Remove or expand with actual sources |
| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |
| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Specific facts about actual challenges |

### Language Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 7 | **AI vocabulary** | "Actually... additionally... testament... landscape... showcasing" | "also... remain common" |
| 8 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |
| 9 | **Negative parallelisms / tailing negations** | "It's not just X, it's Y", "..., no guessing" | State the point directly |
| 10 | **Rule of three** | "innovation, inspiration, and insights" | Use natural number of items |
| 11 | **Synonym cycling** | "protagonist... main character... central figure... hero" | "protagonist" (repeat when clearest) |
| 12 | **False ranges** | "from the Big Bang to dark matter" | List topics directly |
| 13 | **Passive voice / subjectless fragments** | "No configuration file needed" | Name the actor when it helps clarity |

### Style Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 14 | **Em/en dashes** | "institutions—not the people—yet this continues—" | Cut them: periods, commas, colons, or parentheses |
| 15 | **Boldface overuse** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 16 | **Inline-header lists** | "**Performance:** Performance improved" | Convert to prose |
| 17 | **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 18 | **Emojis** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |
| 19 | **Curly quotes** | `said “the project”` | `said “the project”` |
| 26 | **Hyphenated word pairs** | “cross-functional, data-driven, client-facing” | Drop hyphens on common word pairs |
| 27 | **Persuasive authority tropes** | "At its core, what matters is..." | State the point directly |
| 28 | **Signposting announcements** | "Let's dive in", "Here's what you need to know" | Start with the content |
| 29 | **Fragmented headers** | "## Performance" + "Speed matters." | Let the heading do the work |
| 30 | **Diff-anchored writing** | "This function was added to replace..." | Describe what it does, not what changed |
| 31 | **Manufactured punchlines / staccato drama** | "It had no preference. No prior. No nostalgia." | Use varied sentence lengths and concrete claims |
| 32 | **Aphorism formulas** | "Symmetry is the language of trust" | Replace the formula with the actual claim |
| 33 | **Conversational rhetorical openers** | "Honestly? It depends..." | Remove the fake-candid setup |

### Communication Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 20 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |
| 21 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |
| 22 | **Sycophantic tone** | "Great question! You're absolutely right!" | Respond directly |

### Filler and Hedging

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 23 | **Filler phrases** | "In order to", "Due to the fact that" | "To", "Because" |
| 24 | **Excessive hedging** | "could potentially possibly" | "may" |
| 25 | **Generic conclusions** | "The future looks bright" | Specific plans or facts |

### Artifact Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 34 | **Placeholder text and template leftovers** | "[Company Name]... since [year]" | "Acme Robotics... since 2014" |
| 35 | **Chatbot citation and markup artifacts** | "gained enterprise adoption citeturn0search2" | Remove the token; cite only a verifiable source |
| 36 | **AI-tool URL tracking parameters** | "launch?utm_source=chatgpt.com" | Strip the tracking parameter |

### Rhythm and Register Patterns

| # | Pattern | Before | After |
|---|---------|--------|----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 37 | **Sudden register shift** | "gonna push the fix tonight... It is imperative to note, however" | "gonna push the fix tonight... still want to test more before we ship it though" |
| 38 | **Question-format headings** | "Why is connection pooling important?" | "Connection pooling" |
| 39 | **Uniform sentence length** | "The migration finished ahead of schedule last quarter. The team documented every step of the process." | "The migration finished early. The team documented every step, and..." |
| 40 | **Interchangeable paragraphs** | "Caching improves response times... Monitoring provides visibility into system behavior." | "Caching improves response times... That load reduction only helps if you can see it working: monitoring gives teams..." |
| 41 | **"Whether" paragraph closers** | "Whether you're building a small script or a large distributed system, it has the tools you need." | Cut the closer |
| 42 | **Low information density** | "In other words, reviewing code helps find bugs early... Essentially, review is a pre-production quality gate." | Cut the restatements |

## Full Example

**Before (AI-sounding):**
> I recently spent five unforgettable days in Lisbon, and let me tell you — this city completely stole my heart. From the moment I arrived, I knew I was somewhere truly special.
>
> Nestled along the banks of the Tagus River, Lisbon stands as a vibrant testament to Portugal's enduring spirit, where rich history and modern energy intertwine at every turn. Yes, the famous hills are challenging — my legs certainly felt it! — but every climb rewards you with breathtaking, panoramic views that make it all worthwhile.
>
> No trip would be complete without riding the iconic Tram 28, winding through the city's most historic neighborhoods. And the food? Simply divine. The original pastéis de nata at Pastéis de Belém are a beloved national treasure, and savoring one still warm was a moment I will never forget.
>
> But what truly makes Lisbon special isn't just the sights — it's the feeling. Wander a few steps off the main squares and you'll discover a quieter, more authentic side: sun-drenched alleys, charming tiled facades, and friendly locals going about their daily lives, inviting you to slow down and savor every moment.
>
> Of course, the must-see São Jorge Castle offers stunning views over the rooftops below. The queues can be long, but the experience is absolutely worth it for any history buff or curious traveler.
>
> Would I go back? Absolutely. Lisbon isn't just a place to visit — it's a place to fall in love with, again and again. If you're dreaming of your next getaway, this is one destination that promises memories to last a lifetime. ✨

**After (Humanized):**
> I spent five days in Lisbon last October and still have mixed feelings about it. Beautiful, yes. Also harder on the knees than anyone warned me.
>
> The hills are the whole story and somehow never make the brochures. My hotel was up in Alfama, which photographs beautifully and translates, in practice, to climbing what felt like a six-story staircase every time I wanted coffee. By the second day my calves had opinions. I started planning each walk around which way was downhill, which is a strange way to see a city but probably an honest one.
>
> Everyone says to ride Tram 28, so I did, wedged against a stranger's backpack for forty minutes while three tour groups filmed the same corner. I would walk the route next time, or go before breakfast. The custard tarts, though, earn the fuss. I had one at a plain little place in Graça, still warm, and for about thirty seconds I understood why people build trips around pastry.
>
> What I did not expect was how quiet the city gets away from the main squares. Two blocks uphill from any plaza it turns into laundry lines, chipped tile, open windows, and old men watching football with the sound turned up. That is the Lisbon I keep thinking about, not the castle.
>
> The castle is fine. The view is great, the queue is long, and I spent more time shuffling toward the entrance than looking at anything once I got inside. If I had only two days, I would trade it for an afternoon of getting lost.
>
> I would go back, but in spring and with better shoes. Lisbon does not bend over backward to make things easy for you. I think I liked that, even when my legs disagreed.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization

## How it works

The skill applies a catalog of 42 named patterns, each with trigger phrases and a rewrite rule. The patterns map onto the signals detection research measures: word-choice fingerprints (overrepresented vocabulary), sentence rhythm (uniform length, low burstiness), rhetorical scaffolding (rule of three, negative parallelism, signposting), formatting fingerprints (em dashes, bolding, curly quotes, tool artifacts), and discourse structure (interchangeable paragraphs, treadmill restatement). The companion ai-check skill scores the same catalog without editing.

## Known limitations

- This skill makes text read more naturally to human readers. It does not, and cannot, guarantee any outcome against statistical AI detectors (GPTZero, Turnitin, Originality, etc.). Prompt-based rewriting has a documented ceiling: the rewriting model shares the statistical profile detectors measure.
- Detectors also produce false positives on fully human text, particularly from non-native English speakers and formal registers. A low ai-check score is not proof of human authorship, and a high one is not proof of AI authorship.
- Aggressive de-telling can flatten a writer's real voice. The iterate loop is capped at two passes for exactly this reason.

## Credits

- Base skill and original 33-pattern catalog: [blader/humanizer](https://github.com/blader/humanizer) (MIT), itself grounded in Wikipedia's "Signs of AI writing".
- Patterns 34-42 adapted (rewritten, not copied) from concepts in [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) (MIT); see docs/pattern-mapping.md for the full disposition table.
- Two-skill split, signal taxonomy, and limitations framing inspired by [harshaneel/humanize](https://github.com/harshaneel/humanize) (MIT).

## Version History

- **3.0.0** - Two-skill suite. Catalog grows 33 → 42: artifact patterns (placeholders, chat citation markup, AI-tool UTM parameters), rhythm/register patterns (register shifts, question headings, uniform sentence length), structural patterns (interchangeable paragraphs, "whether" closers, treadmill writing); trigger extensions to patterns 1, 11, 15, 23. New: named voice profiles (neutral default), detect mode, bounded iterate loop (max 2 passes, guards against over-editing), ai-check scoring skill with artifact band floor, README limitations section replacing any detector-outcome implication. Pattern concepts adapted with credit from Aboudjem/humanizer-skill and framing from harshaneel/humanize (both MIT). Eval record (2026-07-05): five iterations of eval-driven prompt tightening eliminated draft/preamble output pollution, narrator invention, and fabricated specifics; judge-scored meaning preservation now averages 4.2 vs the 2.8.2 baseline's 3.8 on the same fixtures. The zero-leak pass criterion proved unstable under a single strict judge scoring against the enlarged 42-pattern rubric (0-1/5 passes on both baseline and candidate, different residual patterns each run); gate redesign (leak budget, multi-vote judging, rubric parity) is tracked as follow-up work.
- **2.8.2** - Replaced the full before/after example with a first-person Lisbon trip recap. The after now keeps the same topic, perspective, and rough length as the before while removing the AI tells without becoming clipped or slogan-like. No change to the 33 patterns.
- **2.8.1** - Added cross-agent installation docs, optional Claude Code plugin packaging, and a compact secondhand-text false-positive guard. No change to the 33 patterns.
- **2.8.0** - Added style/cadence patterns #31-33 for manufactured punchlines, aphorism formulas, and conversational rhetorical openers; expanded #20 to catch offer-to-continue chatbot closers. 33 patterns total.
- **2.7.0** - Added pattern #30 (diff-anchored writing); made em/en dashes a hard cut rather than "overuse"; expanded #21 to cover speculative gap-filling ("maintains a low profile"). 30 patterns total.
- **2.6.0** - Cleanup pass: consolidated the duplicated workflow sections, gated the personality guidance to content where voice is wanted, removed the model-fingerprinting subsection, and condensed the worked example. No change to the 29 patterns.
- **2.5.1** - Added a passive-voice / subjectless-fragment rule, raising the total to 29 patterns
- **2.5.0** - Added patterns for persuasive framing, signposting, and fragmented headers; expanded negative parallelisms to cover tailing negations; tightened wording around em dash overuse; fixed frontmatter wording to use "filler phrases"
- **2.4.0** - Added voice calibration: match the user's personal writing style from samples
- **2.3.0** - Added pattern #25: hyphenated word pair overuse
- **2.2.0** - Added a final "obviously AI generated" audit + second-pass rewrite prompts
- **2.1.1** - Fixed pattern #18 example (curly quotes vs straight quotes)
- **2.1.0** - Added before/after examples for all 24 patterns
- **2.0.0** - Complete rewrite based on raw Wikipedia article content
- **1.0.0** - Initial release

## License

MIT
