---
id: tool-00166
type: tool
area: 库
status: active
tags: [Claude插件, HTML, 协议未明, 本地优先, 英文文档, 本地写作]
title: Academic_Research_Skills
summary: Claude Code 插件式写作流
source: https://github.com/lerlerchan/academic_research_skills
created: 2026-07-18
updated: 2026-07-18
no: 166
category: 二、网文 / 长篇 AI 写作系统 库
repo: lerlerchan/Academic_Research_Skills
stars: 1
url: https://github.com/lerlerchan/academic_research_skills
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# lerlerchan/Academic_Research_Skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/lerlerchan/academic_research_skills
- **Stars**：1
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A practical compilation of academic research skills mapped to AI‑assisted CLI workflows for Claude Code, Copilot CLI, Gemini CLI, OpenCode CLI, and Codex CLI—bridging traditional research methods with modern AI tools for literature review, analysis, writing, and reproducibility.
- **本地描述**：A practical compilation of academic research skills mapped to AI‑assisted CLI workflows for Claude Code, Copilot CLI, Gemini CLI, OpenCode CLI, and Codex CLI—bridging traditional research methods with modern AI tools for literature review, analysis, writing, and reproducibility.
- **拉取时间**：2026-07-23 22:43:52

---

# Academic Research Skills

Curated research skills for Claude Code, compiled from leading researchers and practitioners.

**Website:** https://lerlerchan.github.io/Academic_Research_Skills/

## Skills Included

1. **🔍 Systematic Literature Review — PRISMA 2020** (By Chuah Kee Man)  
   Guide users through writing systematic reviews following PRISMA 2020. Produces Word documents, flow diagrams, and APA citations.  
   [Repo](https://github.com/lerlerchan/slr-prisma)

2. **🌐 English to Bahasa Melayu Translator** (By Chuah Kee Man)  
   Translate English to Malaysian Malay following DBP conventions. Handles formal documents and technical content.  
   [Repo](https://github.com/keemanxp/dbp-translator-claude)

3. **📚 APA 7th Edition Referencing & Citation** (By Chuah Kee Man)  
   Format, verify, and convert references. Supports 20+ source types with web verification.  
   [Repo](https://github.com/keemanxp/apa-referencing-skill)

4. **✍️ Remove AI Writing Patterns** (By blader)  
   Detect and fix AI writing patterns. Makes text sound natural and human-written.  
   [Repo](https://github.com/blader/humanizer)

5. **🧠 Claude Scholar: Research Ecosystem** (By Galaxy-Dawn)  
   Full research lifecycle support: ideation, development, analysis, writing, publication. 47 embedded skills.  
   [Repo](https://github.com/Galaxy-Dawn/claude-scholar)

6. **💡 Uncommon Prompting Tips for Students** (By Chuah Kee Man)  
   20 creative prompting techniques for learning and retention.  
   [Repo](https://github.com/keemanxp/uncommon-prompting-tips)

---

## Site Architecture

This site is built with **Jekyll** and hosted on **GitHub Pages**.

### Key Features
- ✅ Search-first grid layout (Layout B)
- ✅ Real-time client-side filtering by title and category
- ✅ Individual pages for each skill
- ✅ SEO-friendly static HTML
- ✅ Mobile responsive (works on all devices)
- ✅ Auto-deploys on commit via GitHub Actions

### Directory Structure
```
academic_research_skills/
├── _config.yml              # Jekyll configuration
├── _data/skills.yml         # Skills catalog (single source of truth)
├── _layouts/                # Page templates
│   ├── default.html         # Base layout
│   ├── home.html            # Homepage (search grid)
│   └── skill.html           # Individual skill detail pages
├── assets/                  # CSS and JavaScript
│   ├── css/style.css
│   └── js/search.js
├── skills/                  # Generated skill pages
├── index.md                 # Homepage
├── Gemfile                  # Ruby dependencies
├── DESIGN.md                # Design documentation
└── README.md                # This file
```

---

## Local Development

### Prerequisites
- Ruby 3.0+
- Bundler

### Setup

1. **Clone and navigate:**
   ```bash
   cd academic_research_skills
   ```

2. **Install dependencies:**
   ```bash
   bundle install
   ```

3. **Build and serve:**
   ```bash
   bundle exec jekyll serve
   ```

4. **Visit:** http://localhost:4000/Academic_Research_Skills

### Making Changes

- **Update skills:** Edit `_data/skills.yml`
- **Change homepage layout:** Edit `_layouts/home.html`
- **Modify styling:** Edit `assets/css/style.css`
- **Change site title:** Edit `_config.yml`

All changes auto-reload when you save.

---

## Deployment

**Automatic:** Push to `main` branch → GitHub Actions builds and deploys to GitHub Pages  
**Manual:** Run `bundle exec jekyll build` and push to `gh-pages` branch

---

## Adding New Skills

To add a new skill:

1. Open `_data/skills.yml`
2. Add an entry with:
   - `id` — URL slug
   - `name` — Display name
   - `emoji` — Representative emoji
   - `category` — One of: Literature Review, General, Writing, Methods
   - `description` — 100-150 word summary
   - `repository` — GitHub repo link
   - `asset_url` — Raw `.md` file URL
   - `asset_type` — md, md+references, or system
   - `author` — Creator name
   - `tags` — Search keywords

3. Run `bundle exec jekyll build` to generate the new skill page

---

## Design Documentation

See `[DESIGN.md](DESIGN.md)` for:
- Complete architecture overview
- Design decisions and trade-offs
- Search implementation details
- Styling and responsive design specs
- Future scalability notes

---

## Contributing

To contribute skills or improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Update `_data/skills.yml` or templates
4. Test locally (`bundle exec jekyll serve`)
5. Push and open a pull request

---

## License

Each skill retains its original license. This site framework is provided as-is for educational and research purposes.

---

## Credits

- **Site Design & Build:** Academic Research Skills contributors
- **Skills Curated By:** Chuah Kee Man, Galaxy-Dawn, blader, and others
- **Built With:** Jekyll, Tailwind CSS, Lunr.js

---

## Sponsor

<p align="center">
  <a href="https://github.com/cyysky" target="_blank">
    <strong>CHONG YOE YAT (cyysky)</strong><br>
    Software development · System integration<br>
    Computer vision automation product development
  </a>
</p>

---

## Support

- 📧 Email: [Your email if applicable]
- 🐛 Issues: [GitHub Issues](https://github.com/lerlerchan/academic_research_skills/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/lerlerchan/academic_research_skills/discussions)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Last updated: {{ site.time | date: "%Y-%m-%d" }}
