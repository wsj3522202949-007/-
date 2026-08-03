---
id: tool-05024
type: tool
area: 库
status: active
tags: [RAG, Java, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: ai-text-detector
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/pss2/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5024
category: 一、去 AI 味 / Humanizer 库
repo: PSS2/ai-text-detector
stars: 0
url: https://github.com/pss2/ai-text-detector
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# PSS2/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pss2/ai-text-detector
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：ai-text-detector
- **本地描述**：ai-text-detector
- **拉取时间**：2026-07-25 18:03:18

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

A Java-based AI text detection tool using statistical analysis and NLP techniques. This tool analyzes text characteristics to identify AI-generated content without requiring external vector databases or API dependencies.

## Features

- **Statistical Analysis**: Word frequency, sentence length uniformity, character diversity
- **N-gram Analysis**: Detects repetitive patterns in text
- **NLP Processing**: Chinese and English text tokenization and analysis
- **Entropy Calculation**: Measures information complexity
- **Composite Scoring**: Multi-dimensional analysis for accurate detection
- **Language Support**: Chinese, English, and mixed languages
- **Offline Operation**: No external API calls required

## Architecture

```
AITextDetector/
├── src/main/java/com/detector/
│   ├── core/              # Core detection engine
│   ├── features/          # Feature extraction modules
│   ├── analysis/          # Analysis engines
│   ├── nlp/               # NLP processing
│   ├── model/             # Data models
│   ├── api/               # Public APIs
│   └── utils/             # Utilities
├── resources/             # Resource files (stopwords, etc.)
└── tests/                 # Unit tests
```

## Quick Start

### Prerequisites
- Java 11+
- Maven 3.6+

### Installation

```bash
git clone https://github.com/PSS2/ai-text-detector.git
cd ai-text-detector
mvn clean install
```

### Basic Usage

```java
import com.detector.core.DetectionEngine;
import com.detector.model.TextAnalysisResult;

public class Main {
    public static void main(String[] args) {
        DetectionEngine engine = new DetectionEngine();
        String text = "Your text to analyze here...";
        
        TextAnalysisResult result = engine.analyze(text);
        
        System.out.println("AI Score: " + result.getAiScore());
        System.out.println("Risk Level: " + result.getRiskLevel());
        System.out.println("Details: " + result.getDetails());
    }
}
```

## Core Features (Phase 1)

### Feature Extraction
1. **Statistical Features**
   - Word frequency distribution
   - Sentence length uniformity
   - Character diversity
   - Punctuation patterns

2. **Repetition Features**
   - N-gram repetition rate
   - Short phrase repetition

3. **Linguistic Features**
   - Part-of-speech diversity
   - Sentence structure variation

4. **Complexity Features**
   - Text entropy (Shannon entropy)
   - Readability index

## Scoring System

- **0-30**: Low risk (likely original content)
- **30-60**: Medium risk (mixed or partially AI-generated)
- **60-100**: High risk (likely AI-generated)

## Development Phases

- [x] Phase 1: Basic statistical analysis
- [ ] Phase 2: NLP enhancement with HanLP
- [ ] Phase 3: Weight optimization and testing
- [ ] Phase 4: Web API and visualization (optional)

## Dependencies

- **HanLP**: Chinese NLP processing
- **Apache Commons Math**: Statistical calculations
- **Gson**: JSON processing
- **SLF4J + Logback**: Logging

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Author

PSS2

## Disclaimer

This tool is for educational and research purposes. The accuracy of AI detection depends on text characteristics and may not be 100% accurate. Use in conjunction with other methods for important decisions.
