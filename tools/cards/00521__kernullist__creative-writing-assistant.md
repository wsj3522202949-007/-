---
id: tool-00521
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: creative-writing-assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/kernullist/creative-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 521
category: 二、网文 / 长篇 AI 写作系统 库
repo: kernullist/creative-writing-assistant
stars: 0
url: https://github.com/kernullist/creative-writing-assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# kernullist/creative-writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/kernullist/creative-writing-assistant
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A comprehensive tool for analyzing and enhancing creative writing with AI-powered insights.
- **本地描述**：A comprehensive tool for analyzing and enhancing creative writing with AI-powered insights.
- **拉取时间**：2026-07-23 22:54:14

---

# Creative Writing Assistant

![Screenshot](docs/screenshot.png)

A comprehensive tool for analyzing and enhancing creative writing with AI-powered insights.

## Features

1. **Style Analysis** – Analyze writing style and identify author influences
2. **Literary Depth** – Evaluate character complexity, themes, and narrative structure
3. **Genre Classification** – Identify story genres and provide genre-specific guidance
4. **Plot Development** – Generate plot suggestions based on story elements
5. **Style Simulation** – Create text in the style of 21 famous authors, in 7 languages
6. **Novel Generation** – Generate multi-chapter novels with real-time SSE progress tracking
7. **Language Selection** – Output in English, Korean, Japanese, Chinese, Spanish, French, or German
8. **Export & Library** – Export as TXT/Markdown, save to library, browse and manage saved outputs
9. **Web Interface** – Modern dark-theme UI with visual metrics, progress bars, expandable author profiles, and modal viewer
10. **REST API** – JSON endpoints for programmatic access, including SSE streaming for novel generation
11. **Interactive CLI** – Korean-language menu-driven interface with per-feature analysis toggles and language selection

## AI Model Integration

The assistant integrates with multiple AI providers:

| Provider | Models | Notes |
|---|---|---|
| **OpenAI** | gpt-3.5-turbo, gpt-4, gpt-4-turbo, gpt-4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano | Direct API |
| **Anthropic** | claude-2, claude-3-sonnet, claude-3.5-sonnet, claude-3.7-sonnet | Direct API |
| **OpenRouter** | 400+ models via unified API | Tiered: Quality / Balanced / Creative |
| **Hugging Face** | bert-base-uncased, distilbert-base-uncased | Limited classification only |

### OpenRouter Tiers

| Tier | Purpose | Example Models |
|---|---|---|
| **Tier 1 — Quality** | Best output quality, structured generation | claude-sonnet-4.6, gemini-2.5-pro, gpt-4.1, claude-opus-4.6 |
| **Tier 2 — Balanced** | Cost-performance balance | gemini-2.5-flash, mistral-medium-3.1, deepseek-v3.2, kimi-k2 |
| **Tier 3 — Creative** | Style simulation, roleplay, prompt adherence | aion-2.0, cydonia-24b-v4.1, l3.3-euryale-70b |

## Setup

### Prerequisites

1. Python 3.7+
2. Required packages (see `requirements.txt`)

### Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up API keys by creating a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```

   Only one provider key is required. The system works offline with traditional metrics when no AI key is configured.

### Usage

#### Web Interface (Recommended)

Start the web server:
```bash
python web_app.py
```

Then open your browser to **http://127.0.0.1:5000**

The web UI provides:
- **Home** – Dashboard with quick access to all features and model status
- **Analyze** – Full style, depth, and genre analysis with visual metrics
- **Style Simulation** – Generate text in famous authors' styles with language selection; expand author profile details inline
- **Plot** – Story element input with AI-generated plot suggestions
- **Novel** – Multi-chapter novel generation with streaming progress, language selection, export, and save
- **Guidelines** – Browse genre-specific writing tips and AI advice
- **Library** – Browse, view (modal viewer), download, and delete saved novels and simulations
- **Settings** – Manage AI model, parameters (max_tokens, temperature, top_p), and analysis preferences

#### Novel Generation

The novel generation feature creates a multi-chapter novel in a chosen author's style:

1. **Select an author** – Choose from 21 pre-configured author profiles with expandable style details
2. **Enter a background/premise** – Describe the story setting, characters, and key events
3. **Configure** – Choose number of chapters (3/5/8/12), chapter length (400/800/1200 words), and output language
4. **Real-time progress** – Watch the progress bar and event log update as each chapter is generated via SSE streaming
5. **Export** – Download as TXT or Markdown, or save to the Library

The generation pipeline works in three stages:
- **Outline** – AI creates a chapter-by-chapter outline with titles and summaries
- **Chapter writing** – Each chapter is generated with context from the previous chapter for continuity
- **Assembly** – All chapters are combined into a complete novel

#### Language Selection

Both Style Simulation and Novel Generation support output in multiple languages:

| Language | Code |
|---|---|
| English | `English` |
| Korean (한국어) | `Korean` |
| Japanese (日本語) | `Japanese` |
| Chinese (中文) | `Chinese` |
| Spanish (Español) | `Spanish` |
| French (Français) | `French` |
| German (Deutsch) | `German` |

#### Export & Library

Generated content can be:
- **Exported immediately** – Download as TXT or Markdown directly from the result page
- **Saved to Library** – Stored server-side as JSON with a unique ID for later retrieval
- **Browsed in Library** – View all saved outputs on the `/library` page with a modal viewer
- **Downloaded later** – Retrieve saved outputs as TXT or Markdown from the Library
- **Deleted** – Remove saved outputs from the Library

#### Genres

The system recognizes 6 built-in genres, each with keyword heuristics, writing tips, and AI-powered guidelines:

| Genre | Key | Keywords |
|---|---|---|
| Science Fiction | `science_fiction` | spaceship, robot, android, galaxy, planet, cyber, orbit, alien |
| Mystery | `mystery` | murder, detective, investigation, clue, suspect, alibi, evidence |
| Psychological Thriller | `psychological_thriller` | paranoia, obsession, unreliable, gaslighting, twist, manipulation |
| Fantasy | `fantasy` | magic, dragon, spell, kingdom, prophecy, artifact, enchanted |
| Literary Fiction | `literary_fiction` | identity, memory, alienation, redemption, symbolism, consciousness |
| Romance | `romance` | love, heart, passion, desire, kiss, embrace, longing |

#### REST API

The web app exposes a JSON API:

| Endpoint | Method | Description |
|---|---|---|
| `/api/analyze` | POST | Analyze text (see parameters below) |
| `/api/simulate-style` | POST | Generate styled text (`{"author_name", "sample_text", "output_length"?, "language"?}`) |
| `/api/generate-novel` | POST | Generate novel synchronously (`{"author_name", "background", "num_chapters"?, "chapter_length"?, "language"?}`) |
| `/api/generate-novel-stream` | POST | Generate novel with SSE progress events (same input) |
| `/api/plot-suggest` | POST | Get plot suggestions (`{"story_elements": {...}}`) |
| `/api/genre-guidelines` | POST | Get genre guidelines (`{"genre": "..."}`) |
| `/api/models` | GET | List available models |
| `/api/authors` | GET | List available authors with full profile details |
| `/api/genres` | GET | List available genres |
| `/api/settings` | GET/PUT | Get/update settings |
| `/api/settings/save` | POST | Save settings to disk |
| `/api/save-novel` | POST | Save a novel to library |
| `/api/save-simulation` | POST | Save a simulation to library |
| `/api/outputs` | GET | List all saved outputs |
| `/api/outputs/<id>` | GET | Get a single output |
| `/api/outputs/<id>` | DELETE | Delete an output |
| `/api/outputs/<id>/download` | GET | Download as `?format=txt` or `?format=md` |

**`/api/analyze`** accepts these optional boolean flags to control which analyses run:

```json
{
  "text": "Your text here...",
  "style_analysis": true,
  "depth_analysis": true,
  "genre_analysis": true
}
```

**`/api/authors`** response includes a `profiles` sub-dict mapping each author key to `{description, characteristics, ...}` with all 12 profile dimensions.

##### SSE Streaming Events (Novel Generation)

The `/api/generate-novel-stream` endpoint returns `text/event-stream` with JSON events:

| Event Type | Progress | Data Payload | Description |
|---|---|---|---|
| `start` | 0% | `{}` | Generation initiated |
| `outline` | 5-10% | `{chapters: [{title, summary, key_events}]}` | Outline generated |
| `chapter_start` | 10-95% | `{chapter_num, title}` | Starting chapter N |
| `chapter_done` | incremental | `{chapter: {number, title, content}}` | Chapter N completed |
| `done` | 100% | `{title, author, chapters: [...], full_text}` | Full novel data returned |
| `error` | – | `{error: "message"}` | Error message |

#### Interactive CLI Mode

> **Note:** The CLI interface is currently in Korean (한국어). All menu labels, prompts, and help text are in Korean.

Run the interactive menu-driven application:
```bash
python main.py
```

**CLI Features:**

| Menu | Feature | Description |
|---|---|---|
| 1 | 전체 분석 (Full Analysis) | Run enabled analyses based on settings toggles |
| 2 | 스타일 분석 (Style Analysis) | Writing style metrics + author similarity comparison |
| 3 | 문학적 깊이 분석 (Depth Analysis) | Character, theme, symbolism, and structure evaluation |
| 4 | 장르 분류 (Genre Classification) | AI + keyword genre detection |
| 5 | 장르 가이드라인 (Genre Guidelines) | Genre-specific tips and AI advice |
| 6 | 작가 스타일 시뮬레이션 (Style Simulation) | Choose author → input text → select length → **select language** → generate |
| 7 | 플롯 개발 제안 (Plot Suggestions) | Input characters/setting/theme/conflict → AI plot ideas |
| 8 | 설정 관리 (Settings) | Model selection, parameters, UI options, analysis toggles, save/reset |
| 9 | 도움말 (Help) | Detailed feature descriptions and tips |

**CLI Options:**
```bash
# Use a specific model for this session
python main.py --model gpt-4

# Disable screen clearing between interactions
python main.py --no-clear

# Use a custom settings file
python main.py --settings /path/to/my_settings.json
```

**Settings Sub-menu (Option 8):**
- AI model selection (all providers and models)
- Generation parameters: max_tokens, temperature, top_p, frequency_penalty, presence_penalty
- UI toggle: clear screen between interactions
- Analysis toggles: enable/disable style, depth, and genre individually
- Save to `settings.json` / reset to defaults

**Text Input Tips:**
- Paste or type multi-line text; press Enter twice on a blank line to submit
- Type `s` + Enter to use the built-in sample text
- Type `q` + Enter to cancel and return to menu

> Novel generation is available via the **web interface** and **REST API** only, not the CLI.

#### Python API

```python
from src.writer_assistant import CreativeWritingAssistant

# Initialize with your preferred model
assistant = CreativeWritingAssistant("gpt-3.5-turbo")

# Analyze text (select which analyses to run)
text = "The old lighthouse stood on the cliffs..."
results = assistant.analyze_text(
    text,
    style_analysis=True,
    depth_analysis=True,
    genre_analysis=True,
)

# Generate style simulation (with language selection)
simulated_text = assistant.generate_style_simulation("ernest_hemingway", text, 300, "Korean")

# Generate a novel
result = assistant.generate_novel("stephen_king", "A haunted hotel in Colorado", 5, 800, "English")
# result contains: {"title", "author", "chapters": [...], "full_text"}

# For streaming progress, use the generator directly
for event in assistant.novel_generator.generate_novel_stream("stephen_king", "...", 5, 800, "English"):
    print(event)  # JSON string with type, message, progress, data

# Get available authors and their profiles
authors = assistant.get_available_authors()          # ["ernest_hemingway", "agatha_christie", ...]
profile = assistant.style_analyzer.AUTHOR_PROFILES   # full profile dict

# Get genre guidelines
guidelines = assistant.get_genre_guidelines("mystery")

# Suggest plot development
story_elements = {"characters": ["protagonist"], "setting": ["lighthouse"]}
suggestions = assistant.suggest_plot_development(story_elements)
```

## Project Structure

```
├── web_app.py              # Flask web application (pages + REST API)
├── main.py                 # Interactive CLI application (Korean UI)
├── requirements.txt        # Python dependencies
├── settings.json           # User configuration (auto-created)
├── .env                    # API keys (create from .env.example)
├── outputs/                # Saved novels and simulations (auto-created)
│
├── src/
│   ├── config.py           # Model configs, API keys, OpenRouter tiers
│   ├── model_client.py     # Unified AI client (OpenAI/Anthropic/OpenRouter)
│   ├── writer_assistant.py # Main entry-point class
│   ├── style_analyzer.py   # Writing style + 21 author profiles + simulation
│   ├── literary_depth.py   # Literary depth evaluation
│   ├── genre_engine.py     # Genre classification (6 genres) + guidelines
│   ├── plot_suggester.py   # Plot development suggestions
│   ├── novel_generator.py  # Multi-chapter novel generation + SSE streaming
│   └── settings_manager.py # Persistent JSON settings
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Layout shell with navigation
│   ├── index.html          # Home/dashboard
│   ├── analyze.html        # Full text analysis
│   ├── simulate.html       # Style simulation + language selector + expandable profiles
│   ├── novel.html          # Novel generation + streaming progress + language selector
│   ├── plot.html           # Plot development suggestions
│   ├── guidelines.html     # Genre guidelines
│   ├── library.html        # Saved outputs browser + modal viewer
│   └── settings.html       # Model & parameter settings
│
├── static/
│   ├── css/style.css       # Dark theme styles (+ progress, library, modal, author details)
│   └── js/app.js           # Client-side interactivity
│
└── tests/                  # pytest test suite
    ├── test_all.py
    └── test_assistant.py
```

## How Author Style Simulation Works

The system uses a **two-layer approach** — a curated author profile injected into an AI prompt — to reproduce a specific writer's voice.

### Author Profiles

Each of the 21 authors is defined by a rich profile with 12 dimensions:

| Author | Key | Core Principle |
|---|---|---|
| Ernest Hemingway | `ernest_hemingway` | Iceberg theory — concise, declarative sentences; subtext over exposition |
| Agatha Christie | `agatha_christie` | Fair-play mystery — logic-driven plots, dialogue-driven reveals, red herrings |
| Stephen King | `stephen_king` | Immersive dread — atmospheric tension, emotional character depth, colloquial voice |
| Isaac Asimov | `isaac_asimov` | Ideas-first prose — scientific precision, logical exposition, concept-driven narrative |
| Jane Austen | `jane_austen` | Social irony — sharp wit, free indirect discourse, courtship comedy |
| Charles Dickens | `charles_dickens` | Vivid caricature — larger-than-life characters, serial pacing, social realism |
| Fyodor Dostoevsky | `fyodor_dostoevsky` | Psychological excavation — inner monologue, moral crisis, existential dread |
| Mark Twain | `mark_twain` | Vernacular voice — regional dialect, tall-tale humor, satirical edge |
| Virginia Woolf | `virginia_woolf` | Consciousness streaming — interior monologue, fluid time, lyrical impressionism |
| Gabriel García Márquez | `gabriel_garcia_marquez` | Magical realism — mythic tone, circular time, lush sensory detail |
| Haruki Murakami | `haruki_murakami` | Surreal minimalism — detached narrator, dream logic, pop-culture motifs |
| George Orwell | `george_orwell` | Lucid polemic — plain language, political allegory, documentary clarity |
| J.R.R. Tolkien | `jrr_tolkien` | Mythic world-building — archaic register, epic scope, linguistic depth |
| Edgar Allan Poe | `edgar_allan_poe` | Gothic intensity — obsessive narrators, rhythmic repetition, psychological horror |
| Raymond Chandler | `raymond_chandler` | Hard-boiled lyricism — simile-rich narration, cynical wit, urban decay |
| Cormac McCarthy | `cormac_mccarthy` | Biblical starkness — minimal punctuation, sweeping landscape, existential violence |
| Margaret Atwood | `margaret_atwood` | Speculative feminism — dry irony, speculative world-building, unreliable narration |
| Arthur Conan Doyle | `arthur_conan_doyle` | Deductive plotting — logical progression, observational detail, Holmesian precision |
| Philip K. Dick | `philip_k_dick` | Paranoiac vision — reality-questioning, shifting identity, bureaucratic absurdity |
| Ursula K. Le Guin | `ursula_k_le_guin` | Anthropological SF — cultural depth, measured prose, sociological imagination |
| Toni Morrison | `toni_morrison` | Lyrical memory — mythic resonance, non-linear narrative, collective voice |

### Profile Dimensions

Each profile contains these 12 fields:

| Field | Description | Example (Hemingway) |
|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `description` | Brief prose summary | "Simple yet profound prose; concise, declarative sentences..." |
| `characteristics` | 5 key traits | `["concise sentences", "direct language", ...]` |
| `sentence_patterns` | How the author structures sentences | "Short declarative sentences averaging 10-15 words" |
| `vocabulary_register` | Word choice level and register | "Plain, everyday words. Prefers Anglo-Saxon root words." |
| `narrative_techniques` | Core storytelling methods | "Iceberg theory", "Objective correlative", "Parataxis" |
| `pacing_style` | How the story moves | "Deceptively simple, flat narration..." |
| `dialogue_style` | How characters speak | "Terse, loaded dialogue. Minimal attribution." |
| `thematic_elements` | Recurring themes | `["Masculinity and honor", "War and its aftermath", ...]` |
| `pov_tendency` | Narrative perspective | "Third-person limited, tightly bound to protagonist" |
| `signature_examples` | Representative lines | `["He was a good man...", ...]` |
| `avoidance` | What the author never does | `["Never uses adverbs ending in -ly", ...]` |
| `paragraph_structure` | How paragraphs are built | "Short paragraphs, often one or two sentences." |

### Prompt Construction

The system uses `StyleAnalyzer.build_style_prompt_section()` to construct a structured **STYLE PROFILE** block from the profile dict. When extended fields are available, the prompt includes detailed instructions across all dimensions:

```
STYLE PROFILE:
- Voice: Plain, everyday words. Avoids Latinate vocabulary.
  Prefers Anglo-Saxon root words. Concrete nouns over abstract ones.
- Sentence structure:
  * Short declarative sentences averaging 10-15 words
  * Coordinate clauses linked by 'and' rather than subordinate clauses
  * Minimal use of semicolons or em-dashes
  * Frequent use of parataxis
- Narrative technique:
  * Iceberg theory: 1/8 on the surface, 7/8 implied underneath
  * Objective correlative: emotions expressed through actions and objects,
    never stated directly
  * Parataxis: clauses placed side by side without explicit logical connectors
  * Reportorial detachment: narrator observes without interpreting
- Dialogue: Terse, loaded dialogue. Characters speak in short bursts.
  Attribution is minimal—he said/she said, never exclaimed/whispered/mused.
- Pacing: Deceptively simple, flat narration that lets tension build
  in the gaps between sentences.
- Themes: Masculinity and honor under pressure, War and its aftermath,
  Grace under pressure, Nature as a testing ground
- POV: Third-person limited, tightly bound to the protagonist's perceptions.
- Paragraph: Short paragraphs, often one or two sentences. Scene breaks
  marked by white space.
- NEVER:
  * Never uses adverbs ending in -ly
  * Never explains what a character is feeling
  * Never uses flowery metaphor or purple prose
  * Never uses semicolons in narrative prose
- SIGNATURE LINES:
  * "He was a good man. He had come from nothing and made something of it."
  * "The rain came down. It always rained in Milan at that time of year."
```

The key elements of the full prompt:

1. **Direct style instruction** — The prompt explicitly names the author and asks the AI to write in their style.
2. **Structured STYLE PROFILE** — Multi-dimensional profile covering voice, sentence structure, narrative technique, dialogue, pacing, themes, POV, paragraph structure, avoidance rules, and signature examples. This gives the AI detailed, actionable constraints.
3. **Avoidance rules (NEVER)** — Explicit negative constraints ("Never uses adverbs ending in -ly") are especially effective at preventing the model from drifting into generic voice.
4. **Signature examples** — Representative lines that anchor the model on the author's exact rhythm and vocabulary.
5. **Language directive (IMPORTANT)** — Reinforced at the end of every prompt: `You MUST write the ENTIRE passage in {language}`. This prevents the model from drifting to English when the requested language is different.
6. **Reference text** — The user's sample text is included with the instruction to *use it for context but not copy it*.

### Novel Generation Context

For multi-chapter novels, the same prompt pattern is extended with:

- **Chapter outline** — Each chapter gets a title, summary, and key events from a previously generated outline, giving the AI narrative direction.
- **Running context** — The previous chapter's text (truncated to 3000 characters) is injected into each subsequent chapter prompt so the narrative remains coherent.
- **Outline-first pipeline** — The system first generates a structured outline, then iterates through chapters. This prevents chapters from drifting or contradicting each other.
- **Language reinforcement** — The language directive is placed at the prompt's end to prevent the model from drifting to the language of the previous chapter's context.

```
Chapter 3 title: The Discovery
Chapter summary: Sarah finds the hidden room beneath the library...
Key events: Sarah discovers the archive, the cat disappears, Mark calls

Previous chapter context (for continuity):
<last 3000 chars of Chapter 2>

Write chapter 3 of a novel in the style of Stephen King.
Language: Write the entire chapter in English.
...
Write approximately 800 words.
```

### Why This Works

Large language models are trained on vast corpora that include millions of words from each of these authors. When the prompt names "Stephen King" and lists his core characteristics, the model:

1. **Activates relevant patterns** — Recognizes King's syntax (short punchy sentences mixed with long descriptive ones), vocabulary (colloquialisms, sensory words), and thematic tendencies (small-town America, ordinary people in extraordinary situations).
2. **Constrains the output space** — The multi-dimensional profile acts as multiple soft constraints, reducing the chance of drifting into a generic voice. The 12-dimension profile (sentence patterns, vocabulary register, narrative techniques, dialogue style, pacing, POV, avoidance rules, etc.) provides far more specific guidance than a simple description.
3. **Uses reference text as rhythm calibration** — The sample text teaches the model the user's preferred cadence and register, which it then filters through the author profile.
4. **Enforces language consistency** — The reinforced `IMPORTANT: You MUST write the ENTIRE passage in {language}` directive at the end prevents the model from drifting into English or the language of the previous chapter's context.

The result is not a copy of any existing work, but a statistically plausible continuation of what the author *might* write, shaped by both their known style features and the user's content.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

MIT License
