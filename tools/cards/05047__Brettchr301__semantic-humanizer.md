---
id: tool-05047
type: tool
area: 库
status: active
tags: [去AI味, TTS, Python, 协议宽松, 需API密钥, 英文文档]
title: semantic-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/brettchr301/semantic-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5047
category: 一、去 AI 味 / Humanizer 库
repo: Brettchr301/semantic-humanizer
stars: 0
url: https://github.com/brettchr301/semantic-humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: be8450bf822ea5cf
  - methods/改稿润色指令库.md
---

# Brettchr301/semantic-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/brettchr301/semantic-humanizer
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Meaning-safe AI-text humanizer + latent-semantic writing-quality analyzer. Rewrites AI-sounding text to read human without drifting from the original meaning (deterministic semantic-similarity gate + cross-family LLM judge).
- **本地描述**：Meaning-safe AI-text humanizer + latent-semantic writing-quality analyzer. Rewrites AI-sounding text to read human without drifting from the original meaning (deterministic semantic-similarity gate + cross-family LLM judge).
- **拉取时间**：2026-07-25 18:04:09

---

# Semantic Writing-Quality Analyzer

Judge writing quality (human **or** AI-generated) by analyzing the *latent
semantics* of the text — how its sentences relate to each other in a learned
semantic space — rather than grammar rules or surface word counts.

> **Looking for the humanizer?** [`humanize.py`](#humanizing-ai-text-humanizepy)
> rewrites AI-sounding text to read human **without letting it drift from the
> original meaning** — guarded by a deterministic semantic-similarity gate plus a
> cross-family LLM judge. Jump to [Humanizing AI text](#humanizing-ai-text-humanizepy).

```
python semantic_quality.py essay.txt
python semantic_quality.py a.txt b.txt c.txt     # compare + rank
echo "some text" | python semantic_quality.py -
python semantic_quality.py essay.txt --json
```

First run, fetch the semantic model (~66 MB, one time):

```
python semantic_quality.py --download
```

`--download` fetches two models: 50-d GloVe (~66 MB) and the Brysbaert
concreteness norms (~1.6 MB), cached under `models/`.

Setup:

```
pip install -r requirements.txt   # numpy + openai (the humanizer's LLM client)
```

Requirements: Python 3.9+, `numpy` (analyzer) and `openai` (humanizer LLM client).
Optional extras (commented in `requirements.txt`): `sentence-transformers` for the
`--backend embeddings` path; `torch`+`transformers` for the `--surprisal` module.

---

## The core idea — and its important catch

Your hypothesis was: *the more semantically related the language, the better the
writing.* That's **true locally but not monotonically**, and the research backs
up both halves:

- **Connected sentences = coherence = quality.** Foltz, Kintsch & Landauer
  (1998) measured textual coherence as the mean cosine similarity between
  *adjacent* sentences in an LSA space, and it predicted reader comprehension at
  r = .93. So yes — relatedness between neighboring sentences is a strong quality
  signal. This is our `flow_coherence`.

- **But maxed-out relatedness = repetition = *bad* writing.** If every sentence
  means nearly the same thing, you don't have great prose — you have padding.
  That's also the fingerprint of low-effort AI text: low *burstiness*
  (human ≈ 0.61 vs AI ≈ 0.38 in sentence-length variation) and low lexical
  diversity.

So great writing hits a **sweet spot**: sentences flow coherently *while still
introducing new ideas*. This tool measures both sides and rewards the balance:

```
   coherence (sentences connect)  +  progression (ideas advance)
   −  redundancy (near-duplicate sentences = looping/padding)
```

A repetitive-but-on-topic essay scores high on coherence yet gets capped by the
redundancy penalty and flagged by the AI-pattern heuristic — which is exactly
what happened to the `ai_slop.txt` sample.

---

## Patent & research grounding

The engine is built directly on the prior art you asked me to look into:

| Source | What we borrow |
|---|---|
| **US 4,839,853** — Deerwester, Dumais, Furnas, Harshman, Landauer, *Latent Semantic Indexing* | The core engine: term×context matrix → **truncated SVD** → compare meaning in the reduced "latent" space. This is the `lsa` backend. |
| **US 6,356,864 B1** — *Analysis of semantic content of a writing based on vector length* (an LSA essay-grader) | Two metrics: the **latent vector length** = "amount of important ideas present" (our `concept_richness` / `raw_vector_length`) and **cosine similarity** for relevance/coherence. |
| **US 7,644,047 B2** — Google, *Semantic similarity based document retrieval* | Reinforces using *contextual* relatedness (a word-replaceability matrix) instead of literal word overlap — i.e. meaning, not string match. |
| **US 11,694,034 B2** — Google, ML-predicted semantic similarity between documents | Modern direction: learned embeddings. Maps to our optional `embeddings` backend. |
| Foltz/Kintsch/Landauer 1998; Arora/Liang/Ma 2017 (SIF) | Adjacent-sentence cosine = coherence; SIF weighted-average + common-component removal = strong sentence embeddings from word vectors. |
| Brysbaert, Warriner & Kuperman 2014 | Concreteness norms for 37k words (1=abstract..5=concrete) → the `imagery_density` craft signal. |

---

## Humanizing AI text (`humanize.py`)

Turns the analyzer from a *judge* into a *coach + verifier loop* that rewrites
AI-sounding text to read human — **without letting it drift from the original
meaning** (the dangerous failure mode of "humanizers").

```
python humanize.py draft.txt               # full loop via DeepSeek
python humanize.py draft.txt --rounds 4
python humanize.py draft.txt --brief-only  # NO API: emit diagnosis + prompts
echo "text" | python humanize.py -
```

Pipeline: **diagnose → rewrite → verify → loop**

1. **Diagnose** — the metrics flag concrete AI tells (uniform sentence rhythm,
   redundancy, abstract/low-imagery wording, cliche openers, low diversity).
2. **Rewrite** — an LLM (DeepSeek `deepseek-v4-pro` by default) rewrites under a
   system prompt that injects the tells and *hard-constrains* it: preserve every
   fact, invent nothing, don't over-correct into purple prose, keep the register.
3. **Verify — two independent checks it must BOTH pass:**
   - **Deterministic gate** (pure math, can't be flattered): meaning_similarity
     to the original ≥ 0.82, AI-pattern down (perplexity-based when surprisal is
     on), coherence not collapsed.
   - **Cross-family LLM judge** (adversarial rubric): meaning preserved?
     fabrication? sounds human? over-corrected? — must quote evidence per
     criterion and **defaults to FAIL on uncertainty**.

**Verifier choice & self-preference bias.** The research on LLM-as-judge shows a
model rates its own family's output more leniently. The rewriter is DeepSeek, so
`--verifier-provider auto` prefers a *different* family for the judge:
`gemini` → `ollama` (local Gemma) → `deepseek` (with a printed self-preference
warning). Schema drift from lighter local judges is tolerated. For maximum rigor
use a strong cross-family judge (Gemini, when billing is available); the local
Gemma fallback errs strict, and the deterministic gate is the hard backstop
regardless.
4. **Loop** — on failure, the judge's specific complaints feed the next rewrite
   (always from the *original*, so drift can't compound), up to `--rounds`.

**Why both checks?** Observed live on the abstract-slop sample: round 1's rewrite
passed the math gate (meaning_sim 0.965) but the DeepSeek judge caught a silently
dropped concluding sentence → rejected. Round 2 fixed it (sim 0.991, AI-pattern
54→23) → accepted. The math gate can't be sweet-talked; the LLM judge catches
nuance the math misses. Neither alone is enough — the harness requires consensus.

`--brief-only` uses no API: it prints the diagnosis plus the rewrite and verify
system prompts, so the *calling agent itself* can be the rewriter (useful for an
agent making its own output sound human). Needs `DEEPSEEK_API_KEY` for the full
loop; `DEEPSEEK_BASE_URL` optional.

---

## Backends (how the latent space is built)

| `--backend` | How meaning is represented | Notes |
|---|---|---|
| `glove` *(default if model present)* | SIF sentence embeddings over 50-d GloVe word vectors | Knows real-world relatedness ("river"≈"canyon"), so coherence is meaningful **on a single short text**. Recommended. |
| `lsa` | TF-IDF term×sentence matrix → SVD (true LSA) | Pure-numpy, no download. **Caveat:** LSA learns relatedness from co-occurrence, so a lone short document is too sparse — it under-rates coherence. Best when you adapt it to score against a reference corpus (as US 6,356,864 does). |
| `embeddings` | `sentence-transformers` (MiniLM) | Best quality if installed; heavier (PyTorch). |

`auto` picks `glove` when the model is downloaded, otherwise `lsa` (with a
warning).

---

## What the metrics mean

**Headline (three axes)**
- `overall_score` (0–100) — blend (0.55 semantic + 0.45 craft).
- `quality_score` (0–100) — **semantic** quality: coherence + structure.
- `style_score` (0–100) — **craft/style**, from four signals:
  *word sophistication* (rare/specific words via GloVe frequency rank),
  *syntactic variety* (sentence-opener diversity + length variation),
  *clause complexity*, and *imagery density* (mean concreteness of content words
  from the Brysbaert norms — concrete, sensory language vs. abstract vagueness).
  This is the axis that distinguishes vivid prose from a flat-but-coherent
  rewrite, and hollow abstract waffle from grounded writing — which the semantic
  axis alone cannot (see below).
- `ai_pattern_score` (0–100) — *heuristic*, higher = more AI-like (redundant,
  uniform sentence lengths, low lexical diversity, idea-looping). **Not a
  detector** — a structural smell test.

**Semantic sub-scores (0–1, higher = better)**
- `coherence_flow` — adjacent-sentence relatedness, rescaled to the realistic
  range (~0.45 unrelated → ~0.85 well-connected).
- `topic_unity` — how tightly every sentence sits around the document's centroid.
- `referential_cohesion` — *literal* lexical overlap + entity continuity between
  adjacent sentences (Coh-Metrix style; complements the semantic cosine).
- `deep_cohesion` — density of causal/logical reasoning connectives
  ("because", "therefore", "however") — Coh-Metrix's "situation model" cohesion.
- `idea_richness` — semantic *progression*, gated by coherence (a pile of
  unrelated sentences does **not** count as rich).
- `lexical_diversity` — MATTR (length-robust type-token ratio).
- `sentence_rhythm` — burstiness; rewards human-like sentence-length variation.
- `flow_consistency` — smoothness of the coherence curve.

**Craft/style sub-scores (0–1, higher = better)**
- `word_sophistication` — mean word rarity (GloVe frequency rank).
- `syntactic_variety` — sentence-opener diversity + length variation.
- `clause_complexity` — subordination/connective density, rewarded in a band.
- `imagery_density` — mean concreteness of content words (Brysbaert norms).
- `word_maturity` — mean age-of-acquisition (Kuperman norms). *Optional* — only
  appears if `models/aoa.csv` is present (no stable public mirror; see download).

**Information-density (`--surprisal`, optional; uses GPT-2 via torch)**
- Replaces the heuristic `ai_pattern_score` with a real **perplexity**-based
  AI signal (low perplexity = predictable = AI-like; the GPTZero approach).
  Example: abstract AI slop scores perplexity ~9 → AI-pattern ~80, while vivid
  human prose scores ~85 → AI-pattern ~9.
- Reports **UID** (uniform information density): `surprisal_uniformity` and an
  `info_quality` band (rewards human-range surprisal — not formulaic, not
  word-salad). Note: incoherent random text has *high* perplexity, so it is
  correctly **not** flagged as AI — the coherence axis catches it instead.

**Raw measures** (for auditing) are printed too: `flow_coherence`,
`semantic_diversity`, `concept_richness`, `raw_vector_length` (the US 6,356,864
vector length), `sentence_length_cv`, `redundancy`.

---

## Calibration on the bundled samples

```
1. overall:86.2 (sem:92.8 style:78.1) AI:19.6  good_human.txt   (flowing, vivid, on-topic)
2. overall:77.0 (sem:94.2 style:55.9) AI:17.7  flat_rewrite.txt (same content, plain prose)
3. overall:58.4 (sem:51.3 style:67.1) AI:34.2  incoherent.txt   (random disconnected sentences)
4. overall:57.8 (sem:61.2 style:53.6) AI:54.4  ai_slop.txt      (coherent but hollow -> AI flag)
```

The ordering is what you'd want: vivid writing on top, plain rewrite below it,
and the hollow/abstract and incoherent texts at the bottom — with the AI-pattern
flag highest on the looping slop.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Does it score *writing style*?

The **semantic** axis does **not** capture craft — proof: the same content
written vividly vs. plainly scores nearly identically there (it even slightly
preferred the flat version's even rhythm):

```
                       overall   semantic   craft/style
good_human (vivid)       86.2      92.8         78.1
flat_rewrite (plain)     77.0      94.2         55.9   <- same content, flat prose
ai_slop (abstract)       57.8      61.2         53.6   <- low imagery_density (0.16)
```

The **craft/style** axis is what separates them, and the blended `overall` then
ranks the vivid prose first. A second case: the abstract "communication is
important" slop scores low on `imagery_density` (~0.16) because its words are
vague, dragging its craft score down where coherence alone wouldn't. Style is
still measured by *proxies* (word rarity, syntactic variety, clause complexity,
concreteness) — it does not judge voice, the *quality* of an image, or
rhetorical effect the way a human editor would.

## Honest limitations

- The semantic axis scores **structure**, not truth or insight. A fluent,
  coherent, but factually empty paragraph can still score "Strong" there — which
  is exactly why the `style` and `ai_pattern` axes exist alongside it.
- Style is proxy-based (see above), not a true craft judge. For deeper style,
  add concreteness/imagery norms (Brysbaert) or a syntactic parser.
- `ai_pattern_score` is heuristic. Modern LLM prose can mimic human burstiness;
  treat it as a signal, not a verdict.
- 50-d GloVe is a compact model. For production, swap in `--backend embeddings`
  or larger GloVe/word2vec vectors.
- Thresholds were calibrated on a small sample set; tune the weights in
  `analyze()` for your own corpus.
