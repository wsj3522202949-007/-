---
id: tool-00520
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ResearchCodeSnippets
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/youvenz/researchcodesnippets
created: 2026-07-18
updated: 2026-07-18
no: 520
category: 二、网文 / 长篇 AI 写作系统 库
repo: YouvenZ/ResearchCodeSnippets
stars: 2
url: https://github.com/youvenz/researchcodesnippets
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# YouvenZ/ResearchCodeSnippets

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/youvenz/researchcodesnippets
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：agentic-ai, arxiv, automation, langchain, python, research
- **GitHub 描述**：A collection of Python snippets covering the full research workflow from arXiv search and PDF extraction to LLM-assisted writing, statistical testing, LaTeX formatting, and notebook-to-paper conversion.
- **本地描述**：A collection of Python snippets covering the full research workflow from arXiv search and PDF extraction to LLM-assisted writing, statistical testing, LaTeX formatting, and notebook-to-paper conversion.
- **拉取时间**：2026-07-23 22:54:12

---


# 🔬 ResearchKit Python Snippets

> *A curated collection of Python tools for researchers — from idea to publication, one snippet at a time.*

---

## What is this?

This repo is a personal toolkit of small, focused Python scripts built to remove friction from the research workflow. Each file does one thing well: summarize a paper, format a citation, generate a hypothesis, visualize results, or turn a notebook into a draft article. No bloated frameworks, no complex setup — just grab what you need and run it.

Whether you're writing your first paper or your fiftieth, something here will save you time.

---

## 🗂️ Contents at a Glance

The scripts are organized by what stage of research they serve:

### 📥 Literature & Discovery
Finding, fetching, and organizing papers.

| File | What it does |
|------|-------------|
| `quick_search.py` | Search papers fast from the terminal |
| `arxiv_agent.py` | Agentic arXiv search with follow-up queries |
| `arxiv_batch.py` | Bulk-fetch papers from arXiv by topic or author |
| `bulk_download.py` | Download PDFs in batch |
| `lit_database.py` | Build a local literature database |
| `lit_matrix.py` | Compare papers across key dimensions in a matrix |
| `gap_finder.py` | Identify research gaps in a set of papers |
| `interactive_paper.py` | Chat with a paper interactively |

---

### 🧠 AI-Assisted Reading & Writing
Let LLMs do the heavy lifting on reading and ideation.

| File | What it does |
|------|-------------|
| `abstract_generator.py` | Draft an abstract from notes or bullet points |
| `abstract_summary.py` | Summarize an abstract into 3-sentence TL;DR |
| `paper_qa.py` | Q&A over a PDF paper |
| `paper_reviewer.py` | Simulate a peer review of your draft |
| `code_explainer.py` | Explain research code in plain English |
| `hypothesis_gen.py` | Generate testable hypotheses from a topic |
| `experiment_suggest.py` | Suggest experiments for a hypothesis |
| `question_gen.py` | Generate research questions from a text |
| `writing_team.py` | Multi-agent writing team for drafting sections |
| `prompt_library.py` | Reusable research prompts with LangChain |

---

### 📊 Data & Statistics
Clean, test, and report your data.

| File | What it does |
|------|-------------|
| `dataset_report.py` | Auto-generate a data quality report |
| `sig_tester.py` | Run significance tests on your data |
| `sig_stars.py` | Add significance stars to results tables |
| `quick_corr.py` | Fast correlation matrix with p-values |
| `smart_split.py` | Smart train/test splitting with stratification |
| `smola_analyzer.py` | Kernel/SVM analysis helpers |
| `compare_models.py` | Side-by-side model comparison table |
| `conf_matrix.py` | Publication-ready confusion matrix |
| `__stats_____report.py__` | Full statistical summary report |

---

### 📈 Figures & Visualization
Make your plots publication-worthy.

| File | What it does |
|------|-------------|
| `pub_plots.py` | Publication-quality matplotlib presets |
| `plot_saver.py` | Save figures in multiple formats at once |
| `auto_figures.py` | Auto-generate figures from a dataframe |

---

### 📝 LaTeX & Document Export
From dataframe to paper, the formatting layer.

| File | What it does |
|------|-------------|
| `csv_to_latex.py` | Convert CSV to a clean LaTeX table |
| `df_latex.py` | DataFrame → LaTeX table (simple) |
| `df_to_latex_pro.py` | DataFrame → LaTeX table with booktabs styling |
| `multi_export.py` | Export tables to LaTeX, HTML, Markdown at once |

---

### 📚 Citations & Bibliography
Keep your references in order.

| File | What it does |
|------|-------------|
| `bib_formatter.py` | Format and clean .bib files |
| `doi_to_bib.py` | Convert a DOI to a BibTeX entry |
| `citation_manager.py` | Manage and deduplicate citations |
| `citation_count.py` | Fetch citation counts for a paper |
| `citation_suggest.py` | Suggest missing citations based on context |
| `extract_keywords.py` | Extract keywords for indexing |
| `keyword_extract.py` | Keyword extraction with TF-IDF / LLM |

---

### 📓 Notebooks → Papers
Turn Jupyter notebooks into something shareable.

| File | What it does |
|------|-------------|
| `extract_notebook.py` | Extract clean code and markdown from .ipynb |
| `nb_to_article.py` | Convert notebook to article draft |
| `notebook_to_paper.py` | Full notebook → paper pipeline |
| `nb_slides.py` | Notebook → presentation slides |
| `equation_extract.py` | Extract equations from a notebook or PDF |
| `pdf_extract.py` | Extract text, tables, figures from PDF |

---

## 🚀 Getting Started

Most scripts are self-contained. Clone the repo and install the common dependencies:

```bash
git clone https://github.com/yourusername/researchkit-snippets
cd researchkit-snippets
pip install langchain ollama arxiv pandas matplotlib scipy scikit-learn
```

Then run any script directly:

```bash
python abstract_generator.py
python paper_reviewer.py
python doi_to_bib.py
```

Each file has a usage example at the bottom under `# Usage` — just open it and run.

---

## 🧩 A Typical Workflow

Here's how these scripts fit together in practice:

```
1. Search & fetch papers     →  quick_search.py, arxiv_batch.py
2. Read & summarize          →  abstract_summary.py, paper_qa.py
3. Find gaps & ideas         →  gap_finder.py, hypothesis_gen.py
4. Run experiments           →  sig_tester.py, compare_models.py
5. Create figures            →  pub_plots.py, conf_matrix.py
6. Format for publication    →  df_to_latex_pro.py, bib_formatter.py
7. Draft & review            →  writing_team.py, paper_reviewer.py
```

---

## 🛠️ Design Philosophy

These scripts are intentionally small and direct. Each one:

- **Does one thing** — no god-classes or over-engineered abstractions
- **Shows its work** — every file has a usage example at the bottom
- **Uses local models where possible** — privacy-friendly, works offline via Ollama
- **Is easy to modify** — under 150 lines, readable by a human in 5 minutes

---

## 📦 Common Dependencies

| Package | Used by |
|---------|---------|
| `langchain` + `ollama` | All LLM-powered scripts |
| `arxiv` | arXiv search and fetch scripts |
| `pandas` | Data and table scripts |
| `matplotlib` / `seaborn` | Visualization scripts |
| `scipy` / `sklearn` | Statistics and ML scripts |
| `PyMuPDF` / `pdfplumber` | PDF extraction scripts |
| `nbformat` | Notebook conversion scripts |

---

## 🤝 Contributing

Found a bug? Have a snippet that fits? Open a PR. Keep it small, keep it focused, and add a usage example at the bottom.

---

## 📄 License

MIT — use freely, credit appreciated.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Built for researchers who would rather spend their time thinking than formatting.*
