---
id: tool-00465
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: writers-nexus
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pioshin/writers-nexus
created: 2026-07-18
updated: 2026-07-18
no: 465
category: 二、网文 / 长篇 AI 写作系统 库
repo: Pioshin/writers-nexus
stars: 0
url: https://github.com/pioshin/writers-nexus
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Pioshin/writers-nexus

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pioshin/writers-nexus
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Novel writing tool from idea to publication
- **本地描述**：Novel writing tool from idea to publication
- **拉取时间**：2026-07-23 22:52:39

---

# Writers Nexus

Una suite per la creazione di opere letterarie, dall’idea alla pubblicazione. Ti accompagna in ogni fase — ideazione, organizzazione, scrittura e revisione — con strumenti semplici ma potenti e con il supporto dell’IA, che ti guida passo dopo passo anche se è il tuo primo progetto editoriale.

Funziona direttamente nel browser e anche offline, così puoi lavorare ovunque e in qualsiasi momento; quando desideri, puoi sincronizzare i tuoi lavori nel cloud. L’interfaccia è attualmente in italiano; il rilascio in altre lingue è previsto, a partire dall’inglese.

![GitHub Release](https://img.shields.io/github/v/release/Pioshin/writers-nexus)
![License](https://img.shields.io/badge/license-MIT-blue)
[![Discussions](https://img.shields.io/badge/Join-Discussions-4b8bbe)](https://github.com/Pioshin/writers-nexus/discussions)
[![Issues](https://img.shields.io/badge/Report-Issues-orange)](https://github.com/Pioshin/writers-nexus/issues)

## Caratteristiche principali

- Ideazione e schede dedicate per personaggi, luoghi, oggetti e sistemi
- Struttura narrativa (Viaggio dell’Eroe) con drag & drop e gestione delle scene non assegnate
- Suggerimenti assistiti dall’IA per inquadrare le scene e trovare ispirazione
- Editor di scrittura con conteggio parole e vista manoscritto a schermo intero
- Dashboard e panoramiche per orientarti nel progetto
- Temi e palette per genere, con interfaccia curata e leggibile
- Dati sempre tuoi: offline‑first con sincronizzazione remota facoltativa

## Caratteristiche (v1.0)

- Importazione testo e segmentazione in scene (senza IA di default)
- Struttura (Viaggio dell’Eroe)
  - Sezione “Scene non assegnate” + batch tagging
  - Drag & drop tra tappe
  - Riordino intra‑stage con campo `order` persistente
  - Badge stage e cambio stage in linea
  - Undo cambio stage (scorciatoia: Ctrl+Alt+Z)
- Suggerimenti IA (Viaggio dell’Eroe)
  - Prompt e parsing robusti (stadi consentiti, IDX, JSON cleaning)
  - Dedup per scena (mantiene confidenza più alta)
  - Filtro per confidenza, selezione, auto‑assegna ≥ soglia
- Scrittura
  - Editor a blocchi con conteggio parole
  - Navigator scene in ordine struttura
  - Badge stage e “Cambia” in linea (Ctrl+Shift+J)
  - Vista “Manoscritto” full screen
- UI/Temi
  - Palette per generi (sci‑fi, fantasy, thriller, romance)
  - Sfondi opachi per massima leggibilità

## Requisiti

- Node.js ≥ 18
- NPM

## Avvio locale

1. Installa le dipendenze
   ```bash
   npm install
   ```
2. Avvia il server di sviluppo
   ```bash
   npm run start
   ```
3. Apri il browser sull’URL mostrato in console (es. http://127.0.0.1:55099)

## Screenshots

> Alcune schermate dell’app (le immagini sono in `docs/screenshots/`).

- Dashboard
  
  !`[Dashboard](./docs/screenshots/dashboard.png)`

- Ideazione
  
  !`[Ideazione](./docs/screenshots/ideation.png)`

- Struttura (con "Scene non assegnate")
  
  !`[Struttura](./docs/screenshots/structure.png)`

- Suggerimenti IA (modale)
  
  !`[Suggerimenti IA](./docs/screenshots/hero-suggestions.png)`

- Scrittura
  
  !`[Scrittura](./docs/screenshots/writing.png)`

## Configurazioni opzionali

### IA
- Apri Impostazioni → sezione IA.
- Imposta Provider (OpenAI‑compatibile, Ollama, Anthropic, Google), Base URL (se richiesto), Modello, API Key.
- La funzionalità “Suggerimenti Viaggio dell’Eroe” ne farà uso quando richiesta.

### Sincronizzazione (Firebase)
- L’app funziona interamente in locale (IndexedDB). La sincronizzazione remota è facoltativa.
- Per abilitarla, inserisci in Impostazioni le credenziali Firebase (config oggetto) ed effettua login.
- Senza configurazione, l’app resta in Modalità Offline e i dati restano sul tuo dispositivo.

## Limitazioni (v1.0)

- Nessun collegamento obbligatorio al database remoto (sync Firebase opzionale)
- Editing avanzato e Analisi in via di sviluppo
- Undo batch (es. per riordino) non ancora disponibile

## Architettura dati

- Storage locale: IndexedDB (via libreria `idb`), orchestrato da `DataManager`
- Store principali: `projects`, `scenes`, `ideas`, `characters`, `locations`, `objects`, `geography`, `history`, `culture`, `plotlines`, `systems`, `settings`
- `scenes` include `stageKey` (tappa Viaggio dell’Eroe) e `order` (ordinamento intra‑stage)
- Sincronizzazione opzionale con Firestore tramite `FirebaseSync`

## Roadmap

- Migliorie undo/redo (batch, riordino)
- Analisi e editing avanzati
- Esportazione/Importazione progetto JSON

## Community & Contributi

- Partecipa alle [Discussions](https://github.com/Pioshin/writers-nexus/discussions) per idee, domande e feedback.
- Segnala bug in [Issues](https://github.com/Pioshin/writers-nexus/issues).
- Nota: al momento non accettiamo Pull Request esterne.
- Se vuoi supportare il progetto, utilizza il pulsante "Sponsor" visibile nella homepage del repository.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Copyright © 2025
