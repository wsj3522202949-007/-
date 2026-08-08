---
id: tool-04366
type: tool
area: 库
status: active
tags: [RAG, 互动叙事, Java, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: Chronicle
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/psilo-hub/chronicle
created: 2026-07-18
updated: 2026-07-18
no: 4366
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: psilo-hub/Chronicle
stars: 0
url: https://github.com/psilo-hub/chronicle
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9624d0878a8ed254
  - methods/模板库.md
---

# psilo-hub/Chronicle

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/psilo-hub/chronicle
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：**Chronicle** is a Java-based desktop application that brings AI-driven RPG characters to life. Unlike standard chatbots, Chronicle uses a **RAG** system powered by Apache Lucene to give characters long-term memory. It forces the LLM to respond in a strict JSON format to drive a dynamic UI, including emotional portraits and a "thought log" window.
- **本地描述**：**Chronicle** is a Java-based desktop application that brings AI-driven RPG characters to life. Unlike standard chatbots, Chronicle uses a **RAG** system powered by Apache Lucene to give characters long-term memory. It forces the LLM to respond in a strict JSON format to drive a dynamic UI, including emotional portraits and a "thought log" window.
- **拉取时间**：2026-07-25 17:44:32

---

# Chronicle: Local RPG Companion

**Chronicle** is a Java-based desktop application that brings AI-driven RPG characters to life. Unlike standard chatbots, Chronicle uses a **Retrieval-Augmented Generation (RAG)** system powered by Apache Lucene to give characters long-term memory. It forces the LLM to respond in a strict JSON format to drive a dynamic UI, including emotional portraits and a "thought log" window.

## ✨ Features

* **Persistent Personality:** Characters maintain a consistent persona via a modular system prompt.
* **Long-Term Memory:** Uses **Apache Lucene 9** and **Vector Search (KNN)** to store and retrieve past conversations based on semantic similarity.
* **Strict JSON Interface:** Leverages Ollama's schema-constrained generation to ensure the AI never breaks the UI.
* **Dynamic UI:**
* **Main Chat:** Clean interface for role-playing.
* **Thought Log:** A secondary "developer" window to see the character's internal reasoning.
* **Emotional Portraits:** The UI updates character images (`neutral`, `happy`, `sad`) based on the AI's expressed emotion.


* **Fully Local:** No API keys required. Everything runs on your machine via **Ollama**.
* **Moddable:** A startup configuration frame allows you to point to external system prompts, schemas, and image folders.

---

## 🛠️ Tech Stack

* **Language:** Java 17+
* **LLM Engine:** [Ollama](https://ollama.com/)
* **Vector Database:** Apache Lucene 9.9.1 (KnnFloatVectorField)
* **JSON Library:** Jackson Databind
* **GUI:** Java Swing (System Look and Feel)
* **Build Tool:** Maven

---

## 🚀 Getting Started

### 1. Prerequisites

* **Java 17** or higher installed.
* **Ollama** installed and running.
* **Models:** Download the required models via terminal:
```bash
ollama pull llama3
ollama pull nomic-embed-text

```


### 2. Project Structure

Ensure your `src/main/resources` contains the following:

* `images/`: Contains `neutral.jpg`, `happy.jpg`, `sad.jpg`.
* `schema.json`: The JSON structure definition.
* `general_rules.txt`: Global AI behavior constraints.
* `character_backstory.txt`: The specific backstory for your character.

### 3. Build & Run

Clone the repository and build with Maven:

```bash
mvn clean package
java -cp target/chronicle-rpg-1.0-SNAPSHOT.jar free.svoss.rpg.app.StartupFrame
```

---

## 📖 How it Works

1. **Retrieval:** When you send a message, the app generates a vector using `nomic-embed-text`.
2. **Search:** Lucene searches the `memory_index` folder for the top 3 most relevant past exchanges.
3. **Augmentation:** The character backstory and retrieved memories are injected into the System Prompt.
4. **Generation:** Ollama generates a JSON object containing `thought`, `expression`, and `dialogue`.
5. **Persistence:** The new exchange is embedded and saved back into the Lucene index.

---

## ⚙️ Configuration

On startup, the **Configuration Frame** allows you to:

* Select from a list of installed Ollama models.
* Define a custom path for the Lucene index (perfect for multiple characters).
* Override internal prompts and images with external files for easy modding.

---

## 🛠️ Upcoming Features / Todo

* **[High Priority] Dynamic Schema Expression Sync:** * Implement an automated scanner that reads the `images/` folder and dynamically updates the JSON Schema `enum` list for "expression". This will allow users to add new emotions (e.g., `angry.jpg`, `confused.jpg`) simply by dropping a file into the folder.
* **Context Window Management:** * Add a "Memory Pruning" feature to summarize older conversations when the Lucene retrieval becomes too large, ensuring the LLM doesn't get overwhelmed by too much context.
* **Rich Text Chat:** * Replace the `JTextArea` with a `JTextPane` to support basic HTML formatting, allowing for bolded names, different colors for "thoughts," and timestamps.
* **Conversation Branching:** * Allow users to "Save and Load" different world states or timelines, creating separate Lucene indices for different storylines.
* **Visual Enhancements:** * Support for animated GIFs or Live2D models as the character portrait to make the expressions feel more alive.
* **[Low Priority] Audio Integration (TTS):** * Integrate a local Text-to-Speech engine (like Piper or a local OpenAI-compatible TTS) to let the character speak the `dialogue` text aloud.

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

## 📸 Screenshot

<p align="center">
  <img src="screenShotForReadme.jpg" alt="Chronicle Interface" width="80%">
</p>
