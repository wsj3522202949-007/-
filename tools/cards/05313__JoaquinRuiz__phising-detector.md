---
id: tool-05313
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: phising-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/joaquinruiz/phising-detector
created: 2026-07-18
updated: 2026-07-18
no: 5313
category: 一、去 AI 味 / Humanizer 库
repo: JoaquinRuiz/phising-detector
stars: 1
url: https://github.com/joaquinruiz/phising-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 01d255a7a2b79f67
  - methods/改稿润色指令库.md
---

# JoaquinRuiz/phising-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/joaquinruiz/phising-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A simple Python script that uses AI to detect phishing attempts in SMS or email text.
- **本地描述**：A simple Python script that uses AI to detect phishing attempts in SMS or email text.
- **拉取时间**：2026-07-25 18:13:58

---

# Phishing Detector

Código fuente del video **"SE ACABÓ el Autocompletado: Crea Agentes IA Locales Gratis con OpenCode + MCP + Ollama"** de Joaquin Ruiz (jokioki).

▶️ [Ver el video en YouTube](https://youtu.be/IBW5ksm9oqQ?si=lRrnboxke41sBoX6)

---

Script Python que usa machine learning para detectar intentos de phishing en SMS o emails. El proyecto incluye la configuración completa de **OpenCode** con agentes personalizados, skills y un servidor MCP propio.

## Contenido del proyecto

### `.opencode/`
Configuración completa para trabajar con OpenCode:
- **`opencode.jsonc`** — Configuración principal con el servidor MCP local
- **`agents/pytest.md`** — Agente personalizado para ejecutar tests con pytest
- **`skills/classify-message`** — Skill para clasificar mensajes

### `mcp/`
Servidor MCP (Model Context Protocol) local que se lanza con `uv run mcp/servidor.py`.

### Script principal
- **`ia_or_true.py`** — Detector de phishing usando el modelo `mshenoda/roberta-spam` de Hugging Face

## Requisitos

- Python 3.9 o superior
- [OpenCode](https://opencode.ai) instalado
- [Ollama](https://ollama.com) con un modelo local descargado
- Conexión a internet para la primera descarga del modelo de HuggingFace

## Instalación

Crea y activa un entorno virtual, luego instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso del script

### Línea de comandos
```bash
python ia_or_true.py "Tu mensaje sospechoso aquí"
```

### Modo interactivo
```bash
python ia_or_true.py
```
Pega mensajes uno a uno. Pulsa Enter en línea vacía para salir.

## Output

- 🟢 LEGÍTIMO: Mensaje legítimo
- 🔴 PHISHING: Intento de phishing detectado

---

## Mis libros

Si quieres aprender más sobre Inteligencia Artificial:

📙 [El motor de la Inteligencia Artificial](https://amzn.eu/d/083CTN3U)

📘 [Programar con Inteligencia Artificial](https://amzn.eu/d/eK4f73N)

📙 [Explora la Inteligencia Artificial](https://amzn.eu/d/dSwYhue)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Hecho con ❤️ por [JokiRuiz](https://jokiruiz.com)
