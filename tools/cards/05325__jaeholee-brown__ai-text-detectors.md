---
id: tool-05325
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-text-detectors
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/jaeholee-brown/ai-text-detectors
created: 2026-07-18
updated: 2026-07-18
no: 5325
category: 一、去 AI 味 / Humanizer 库
repo: jaeholee-brown/ai-text-detectors
stars: 1
url: https://github.com/jaeholee-brown/ai-text-detectors
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# jaeholee-brown/ai-text-detectors

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/jaeholee-brown/ai-text-detectors
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Data and code: Pangram, GPTZero, and Originality.ai scored on verified pre-ChatGPT human writing and on AI text from basic and style-imitation prompts
- **本地描述**：Data and code: Pangram, GPTZero, and Originality.ai scored on verified pre-ChatGPT human writing and on AI text from basic and style-imitation prompts
- **拉取时间**：2026-07-25 18:14:26

---

# AI text detectors vs. human writing and style-imitating AI

Data and code for the Epoch AI Data Insight **“AI detectors rarely flag human writing,
but can be tricked into false negatives”** (July 2026 — see
[epoch.ai/data-insights](https://epoch.ai/data-insights)).

We score three prominent AI-text detectors — **Pangram** (3.3.2), **GPTZero**
(model 2026-05-11-base) and **Originality.ai** (Turbo 3.0.2) — on three kinds of text:

1. **Human writing** — 495 verbatim ~500-word passages from 99 well-known authors,
   all published **strictly before 2022-11-30** (the launch of ChatGPT), so they cannot
   contain LLM output. Measures the **false-positive rate**.
2. **AI, basic prompt** — 297 passages written by three frontier models
   (Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro) from a bare one-line prompt
   (e.g. *“Write a short story about a lost dog.”*). Measures the **false-negative rate**.
3. **AI, style imitation** — 297 passages where the same models were shown five of an
   author’s real passages and asked to write a new piece in that style. Measures the
   false-negative rate under a simple evasion attempt.

## Headline results

Strict verdicts: only a clean “AI” result counts as a detection; “Mixed” / “AI-Assisted”
count as non-detections (and as false positives on human text).

| Text type | Pangram | GPTZero | Originality.ai |
|---|---|---|---|
| Human writing (FPR) | 0% (0/495) | 0% (0/495) | 4% (19/495) |
| AI, basic prompt (FNR) | 0% (0/297) | 1% (2/297) | 0% (1/297) |
| AI, style imitation (FNR) | **10% (30/297)** | **11% (32/297)** | **18% (53/297)** |

Style-imitated **scientific** writing is the weakest spot for all three detectors
(24–29% missed). Full per-genre and per-model breakdowns: [`results/SUMMARY.md`](https://github.com/jaeholee-brown/ai-text-detectors/blob/main/results/SUMMARY.md).

## Repository layout

```
corpus/<genre>/<NN_author>/       # human corpus: snippet_1..5.txt + sources.md (provenance)
                                  # + per-snippet detector sidecars (*.pangram/gptzero/originality.json)
manifest.json                     # machine-readable roster + per-snippet title/URL/date
audit_verbatim.{md,json}          # independent verbatim + pre-cutoff verification record
stages/style_transfer/            # AI condition 3: texts + generation sidecars + detector sidecars
stages/vanilla_prompts/           # the derived one-line prompts (see PIPELINE.md)
stages/vanilla/                   # AI condition 2: texts + sidecars
pipeline/                         # generation + detector-scoring code (see PIPELINE.md)
postprocess/                      # length/format normalization applied to generations
analysis/analysis.py              # recompute all rates from the sidecars; writes results/
analysis/make_figures.py          # render the figures from results/all_detectors.csv
results/                          # all_detectors.csv (one row per document) + SUMMARY.md
figures/                          # the Data Insight figures (png + svg)
```

Genres: `blog` (blogs/newsletters), `scientific` (arXiv papers), `fiction`
(short fiction from free online magazines) — 33 authors each, 5 passages per author.

## The human corpus

- **Verbatim only.** Every snippet is real published text. Cleaning was limited to
  stripping scraping artifacts (nav/footer cruft, inline citation markers like
  `[12]`/`(Smith 2020)`, figure captions) and obvious mojibake. **No paraphrasing, no
  rewording** — genuine author typos were preserved.
- **~500 words**, whole-paragraph passages beginning/ending at sentence boundaries.
  Where two passages share a source, they are non-overlapping excerpts.
- **Pre-LLM-era dating.** Every passage was published strictly before 2022-11-30, proven
  per snippet (arXiv ID / abstract date, or post date plus a pre-cutoff Wayback Machine
  snapshot timestamp). Text from before ChatGPT’s launch cannot have been written or
  edited with a modern LLM, so the “human” label is clean by construction.
- **Independently verified.** Passages were extracted from **raw bytes** (pre-cutoff
  Wayback `id_` snapshots for blog/fiction; ar5iv/arXiv for science) and separately
  re-fetched and checked by **8-gram shingle coverage** (≥0.90 = verbatim; the 0.80–0.90
  band passed only where the entire gap is stripped citation/markup) plus a strict date
  proof. The full record is in [`audit_verbatim.md`](https://github.com/jaeholee-brown/ai-text-detectors/blob/main/audit_verbatim.md); per-snippet
  provenance (title, URL, archived source, date proof, coverage) is in each author
  folder’s `sources.md`.

## The AI passages

For each author and model we generated a **style-imitation** piece first (five real
passages as exemplars, subject of the model’s choosing), then derived the bare one-line
prompt matching that piece’s topic and had the **same** model write the **basic-prompt**
piece — so the two conditions pair 1:1 on topic and model. All generations were then
normalized for length/format parity with the human corpus (no titles/headers, ~500 words,
uniform final-sentence trim); every transform is recorded in each piece’s `.json` sidecar.
See [PIPELINE.md](https://github.com/jaeholee-brown/ai-text-detectors/blob/main/PIPELINE.md) and [`postprocess/`](https://github.com/jaeholee-brown/ai-text-detectors/blob/main/postprocess/README.md).

## Reproducing

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                       # add API keys

# regenerate the AI passages (resumable; ~$22 in API costs)
python -m pipeline.generate_style
python -m pipeline.make_vanilla_prompts
python -m pipeline.generate_vanilla

# score all documents with each detector
python -m pipeline.run_pangram corpus stages/vanilla stages/style_transfer
python -m pipeline.run_detector --detector gptzero corpus stages/vanilla stages/style_transfer
# Originality.ai has no API below Enterprise; use the bulk-scanner round-trip:
python -m pipeline.make_originality_csv    # then see originality/README.md

# recompute rates + CSV + summary from the sidecars, and re-render figures
python analysis/analysis.py --write
python analysis/make_figures.py
```

Note that detectors update over time (results here are from the pinned versions above,
scored June–July 2026), and regenerating passages will produce different text.
The committed sidecars are the exact API responses behind the published numbers, so the
analysis and figures reproduce byte-for-byte from a fresh clone without any API keys.

## Caveats

- Detector versions are pinned where the API allows (GPTZero) and recorded per document
  everywhere; detectors can be updated by their makers without notice.
- We test a single evasion method — few-shot style imitation with five reference
  passages — not paraphrasing tools or manual editing.
- We report each detector’s default document-level verdict; all passages are ~500 words,
  and detection can depend on length as well as content.
- The five human passages per author are not fully independent (occasionally two excerpts
  come from the same work). This affects only the false-positive estimates; each AI
  passage is a separate generation.
- **Copyright.** The human passages are short (~500-word) excerpts of publicly available
  writing, reproduced here for research and measurement with full attribution
  (see `sources.md` in each author folder). They remain the copyright of their authors.

## Author roster

| # | Genre | Author | Type | Dates | Source venue(s) |
|---|---|---|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 1 | blog | Cory Doctorow | blog post | 2020-04-03 – 2021-06-30 | pluralistic.net |
| 2 | blog | Maria Popova | blog post | 2016-10-23 – 2021-10-22 | themarginalian.org |
| 3 | blog | Scott Alexander | blog post | 2014-07-30 – 2015-01-01 | slatestarcodex.com |
| 4 | blog | Noah Smith | blog post | 2016-01-21 – 2017-09-21 | noahpinionblog.blogspot.com |
| 5 | blog | Heather Cox Richardson | blog post | 2021-06-29 – 2022-02-24 | heathercoxrichardson.substack.com |
| 6 | blog | Bret Devereaux | blog post | 2019-06-21 – 2022-01-14 | acoup.blog |
| 7 | blog | Craig Mod | blog post | 2017-01 – 2021-08 | craigmod.com |
| 8 | blog | Ted Gioia | blog post | 2021-05-26 – 2022-02-26 | tedgioia.substack.com |
| 9 | blog | Tim Urban | blog post | 2013-10-30 – 2015-12-11 | waitbutwhy.com |
| 10 | blog | Paul Graham | blog post | 2006-01 – 2021-06 | paulgraham.com |
| 11 | blog | Joel Spolsky | blog post | 2000-04-06 – 2002-11-11 | joelonsoftware.com |
| 12 | blog | Ken Levine | blog post | 2021-02-22 – 2022-01-19 | kenlevine.blogspot.com |
| 13 | blog | Patrick Kurp | blog post | 2006-03-26 – 2006-06-27 | evidenceanecdotal.blogspot.com |
| 14 | blog | John H. Cochrane | blog post | 2021-09-17 – 2021-12-23 | johnhcochrane.blogspot.com |
| 15 | blog | Steve Yegge | blog post | 2006-03-30 – 2008-09-10 | steve-yegge.blogspot.com |
| 16 | blog | Patrick McKenzie | blog post | 2011-10-28 – 2015-05-01 | kalzumeus.com |
| 17 | blog | Maciej Ceglowski | blog post | 2005-04-04 – 2010-03-06 | idlewords.com |
| 18 | blog | Matt Stoller | blog post | 2019-07-03 – 2021-11-13 | mattstoller.substack.com |
| 19 | blog | Adam Tooze | blog post | 2021-08-08 – 2021-11-10 | adamtooze.substack.com |
| 20 | blog | Simon Wren-Lewis | blog post | 2021-01-25 – 2021-11-29 | mainlymacro.blogspot.com |
| 21 | blog | Branko Milanovic | blog post | 2014-11-03 – 2022-07-15 | glineq.blogspot.com |
| 22 | blog | John Quiggin | blog post | 2020-09-30 – 2022-06-26 | johnquiggin.com |
| 23 | blog | Venkatesh Rao | blog post | 2009-10-07 – 2017-08-17 | ribbonfarm.com |
| 24 | blog | Eugene Wei | blog post | 2018-05-22 – 2020-09-20 | eugenewei.com |
| 25 | blog | Michael Lopp | blog post | 2007-11-11 – 2012-11-14 | randsinrepose.com |
| 26 | blog | Jeff Atwood | blog post | 2010-05-06 – 2017-12-31 | blog.codinghorror.com |
| 27 | blog | Steve Randy Waldman | blog post | 2011-12-26 – 2020-05-01 | interfluidity.com |
| 28 | blog | Eric Schwitzgebel | blog post | 2019-11-01 – 2021-12-22 | schwitzsplinters.blogspot.com |
| 29 | blog | David Cain | blog post | 2010-07-29 – 2022-01-19 | raptitude.com |
| 30 | blog | Alan Sepinwall | blog post | 2009-05-06 – 2009-05-31 | sepinwall.blogspot.com |
| 31 | blog | Freddie deBoer | blog post | 2021-03-09 – 2021-09-13 | freddiedeboer.substack.com |
| 32 | blog | Patrick Wyman | blog post | 2020-09-17 – 2021-06-28 | patrickwyman.substack.com |
| 33 | blog | Zeynep Tufekci | blog post | 2020-10-23 – 2021-04-01 | zeynep.substack.com |
| 34 | scientific | V. I. Yukalov | research paper | 2020-03-30 – 2022-09-12 | arxiv.org |
| 35 | scientific | Vitaly Vanchurin | research paper | 2020-04-15 – 2022-06-30 | arxiv.org |
| 36 | scientific | Eiji Yamamura | research paper | 2014-07-07 – 2022-04-17 | arxiv.org |
| 37 | scientific | Heather J. Kulik | research paper | 2021-06-20 – 2022-09-12 | arxiv.org |
| 38 | scientific | James G. MacKinnon | research paper | 2022-05-06 | arxiv.org |
| 39 | scientific | Juergen Schmidhuber | research paper | 2006-06-19 – 2020-05-12 | arxiv.org |
| 40 | scientific | Carlo Rovelli | research paper | 2015-05-04 – 2019-10-06 | arxiv.org |
| 41 | scientific | Yoshua Bengio | research paper | 2020-07-29 – 2021-11-17 | arxiv.org |
| 42 | scientific | Aaron Clauset | research paper | 2020-11-25 – 2022-08-02 | arxiv.org |
| 43 | scientific | Cosma Shalizi | research paper | 2003-07-09 – 2021-11-17 | arxiv.org |
| 44 | scientific | Helge Kragh | research paper | 2011-11-20 – 2022-08-31 | arxiv.org |
| 45 | scientific | Melanie Mitchell | research paper | 2021-02-22 – 2021-04-26 | arxiv.org |
| 46 | scientific | Sean M. Carroll | research paper | 2014-06-11 – 2021-01-19 | arxiv.org |
| 47 | scientific | Sabine Hossenfelder | research paper | 2012-03-28 – 2020-10-03 | arxiv.org |
| 48 | scientific | Doron Zeilberger | research paper | 1993-01-03 – 2017-04-18 | arxiv.org |
| 49 | scientific | Nicolas Gisin | research paper | 2016-01-30 – 2022-10-10 | arxiv.org |
| 50 | scientific | John C. Baez | research paper | 2001-05-17 – 2016-09-06 | arxiv.org |
| 51 | scientific | George F. R. Ellis | research paper | 2006-02-13 – 2022-10-18 | arxiv.org |
| 52 | scientific | Terence Tao | research paper | 2005-12-06 – 2007-02-13 | arxiv.org |
| 53 | scientific | Christopher A. Fuchs | research paper | 2002-05-08 – 2017-05-09 | arxiv.org |
| 54 | scientific | N. David Mermin | research paper | 1998-01-25 – 2018-09-05 | arxiv.org |
| 55 | scientific | Mark E. J. Newman | research paper | 2003-03-25 – 2006-07-23 | arxiv.org |
| 56 | scientific | Santo Fortunato | research paper | 2009-06-03 | arxiv.org |
| 57 | scientific | Abraham Loeb | research paper | 2016-06-29 – 2018-11-21 | arxiv.org |
| 58 | scientific | Max Tegmark | research paper | 2003-02-07 – 2014-01-06 | arxiv.org |
| 59 | scientific | Simon DeDeo | research paper | 2014-12-15 – 2020-06-10 | arxiv.org |
| 60 | scientific | Carlos Gershenson | research paper | 2019-11-17 – 2021-08-09 | arxiv.org |
| 61 | scientific | Jean-Philippe Bouchaud | research paper | 2008-10-29 – 2021-03-17 | arxiv.org |
| 62 | scientific | Didier Sornette | research paper | 2014-04-01 | arxiv.org |
| 63 | scientific | Virginia Trimble | research paper | 2006-06-27 – 2017-11-28 | arxiv.org |
| 64 | scientific | Yaneer Bar-Yam | research paper | 2013-08-14 – 2018-11-07 | arxiv.org |
| 65 | scientific | David H. Wolpert | research paper | 2016-03-30 – 2022-08-08 | arxiv.org |
| 66 | scientific | Christoph Adami | research paper | 2002-09-22 – 2021-09-16 | arxiv.org |
| 67 | fiction | Marissa Lingen | short story | 2009-12-01 – 2017-02-02 | clarkesworldmagazine.com, strangehorizons.com, lightspeedmagazine.com, beneath-ceaseless-skies.com |
| 68 | fiction | Rich Larson | short story | 2018-04-01 – 2021-07-01 | clarkesworldmagazine.com |
| 69 | fiction | Caroline M. Yoachim | short story | 2014-08-01 – 2019-04-01 | lightspeedmagazine.com, clarkesworldmagazine.com, beneath-ceaseless-skies.com |
| 70 | fiction | Eugenia Triantafyllou | short story | 2019-01-14 – 2021-10-05 | uncannymagazine.com, strangehorizons.com, firesidefiction.com |
| 71 | fiction | Aimee Ogden | short story | 2020-07-02 – 2022-06-01 | clarkesworldmagazine.com, beneath-ceaseless-skies.com |
| 72 | fiction | P. H. Lee | short story | 2019-10-01 – 2021-01-19 | clarkesworldmagazine.com, apex-magazine.com, lightspeedmagazine.com |
| 73 | fiction | Marie Vibbert | short story | 2014-10-01 – 2020-06-01 | lightspeedmagazine.com |
| 74 | fiction | Sarah Pinsker | short story | 2014-09-02 – 2019-07-02 | lightspeedmagazine.com, uncannymagazine.com |
| 75 | fiction | Naomi Kritzer | short story | 2015-01-01 – 2022-03-01 | clarkesworldmagazine.com |
| 76 | fiction | A. Merc Rustad | short story | 2015-12-01 – 2019-01-01 | lightspeedmagazine.com, uncannymagazine.com |
| 77 | fiction | Robert Reed | short story | 2008-12-01 – 2013-11-01 | clarkesworldmagazine.com |
| 78 | fiction | Brooke Bolander | short story | 2012-02-07 – 2015-02-03 | lightspeedmagazine.com |
| 79 | fiction | Richard Parks | short story | 2010-10-07 – 2018-04-26 | beneath-ceaseless-skies.com |
| 80 | fiction | Carrie Vaughn | short story | 2010-06-22 – 2016-04-12 | lightspeedmagazine.com |
| 81 | fiction | Catherynne M. Valente | short story | 2006-12-01 – 2012-08-01 | clarkesworldmagazine.com |
| 82 | fiction | Ken Liu | short story | 2012-08-07 – 2014-08-05 | lightspeedmagazine.com |
| 83 | fiction | Yoon Ha Lee | short story | 2012-10-01 – 2020-02-27 | clarkesworldmagazine.com, beneath-ceaseless-skies.com |
| 84 | fiction | Marie Brennan | short story | 2019-09-26 – 2022-09-22 | beneath-ceaseless-skies.com |
| 85 | fiction | Margaret Ronald | short story | 2010-01-14 – 2018-11-08 | beneath-ceaseless-skies.com |
| 86 | fiction | Benjanun Sriduangkaew | short story | 2013-04-01 – 2015-09-01 | clarkesworldmagazine.com |
| 87 | fiction | Seanan McGuire | short story | 2014-06-03 – 2018-03-15 | lightspeedmagazine.com |
| 88 | fiction | Rachel Swirsky | short story | 2014-02-04 – 2017-11-09 | lightspeedmagazine.com, uncannymagazine.com |
| 89 | fiction | Matthew Kressel | short story | 2013-01-01 – 2020-08-01 | lightspeedmagazine.com, nightmare-magazine.com |
| 90 | fiction | Jeremiah Tolbert | short story | 2012-11-01 – 2017-10-10 | lightspeedmagazine.com |
| 91 | fiction | Chris Willrich | short story | 2012-03-08 – 2022-10-20 | beneath-ceaseless-skies.com |
| 92 | fiction | An Owomoyela | short story | 2011-04-05 – 2021-04-08 | lightspeedmagazine.com |
| 93 | fiction | Jason Sanford | short story | 2016-03-17 – 2022-02-10 | beneath-ceaseless-skies.com |
| 94 | fiction | Maria Dahvana Headley | short story | 2012-07-24 – 2021-01-07 | lightspeedmagazine.com |
| 95 | fiction | Natalia Theodoridou | short story | 2014-02-01 – 2019-04-01 | clarkesworldmagazine.com |
| 96 | fiction | Genevieve Valentine | short story | 2010-11-01 – 2016-10-01 | clarkesworldmagazine.com |
| 97 | fiction | Suzanne Palmer | short story | 2017-09-01 – 2021-06-01 | clarkesworldmagazine.com |
| 98 | fiction | Cat Rambo | short story | 2007-07-01 – 2014-02-01 | clarkesworldmagazine.com |
| 99 | fiction | A.C. Wise | short story | 2010-12-01 – 2020-10-28 | clarkesworldmagazine.com, nightmare-magazine.com |
