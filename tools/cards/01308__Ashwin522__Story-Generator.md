---
id: tool-01308
type: tool
area: 库
status: active
tags: [多Agent, 大纲规划, Python, 协议未明, 需API密钥, 英文文档]
title: Story-Generator
summary: 多 Agent 协作自动产文
source: https://github.com/ashwin522/story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1308
category: 二、网文 / 长篇 AI 写作系统 库
repo: Ashwin522/Story-Generator
stars: 0
url: https://github.com/ashwin522/story-generator
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Ashwin522/Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ashwin522/story-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Story Generator AI Agent
- **本地描述**：Story Generator AI Agent
- **拉取时间**：2026-07-23 23:17:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🌙 Bedtime Story Generator with LLM Judge

An AI-powered bedtime story generator that creates age-appropriate, engaging stories for children ages 5-10. Features a sophisticated LLM judge system that ensures quality through multi-criteria evaluation and iterative refinement.

## ✨ Features

- **Intelligent Story Categorization**: Automatically identifies story type (adventure, fairy tale, animal story, bedtime, educational) and applies tailored generation strategies
- **LLM Judge Quality Assurance**: Multi-criteria evaluation system scores stories on 5 dimensions:
  - Age appropriateness (vocabulary, concepts, content safety)
  - Engagement (how captivating and interesting)
  - Story structure (clear beginning, middle, end)
  - Educational value (positive messages and life lessons)
  - Language clarity (simple, understandable for ages 5-10)
- **Iterative Refinement Loop**: Stories are automatically improved based on judge feedback (up to 2 iterations)
- **User Feedback Integration**: Request changes and regenerate stories with your specific guidance
- **Beautiful CLI Interface**: Rich terminal interface with formatted output and easy interaction

## 🏗️ System Architecture

The system uses a multi-agent approach with four specialized components:

1. **Categorizer**: Analyzes requests and identifies story category/themes
2. **Storyteller**: Generates stories using category-specific strategies
3. **Judge**: Evaluates quality on 5 criteria and provides actionable feedback
4. **Refiner**: Converts judge feedback into improvement instructions

See `[system_diagram.md](system_diagram.md)` for detailed architecture and flow diagrams.

## 📋 Requirements

- Python 3.11+
- OpenAI API key
- Dependencies: `openai`, `pydantic`, `rich`

## 🚀 Setup

1. **Install dependencies** (if not already installed):
```bash
pip install openai pydantic rich
```

2. **Set your OpenAI API key**:
```bash
export OPENAI_API_KEY='your-openai-api-key-here'
```

**Important**: Never commit your API key to version control!

## 🎮 Usage

Run the story generator:
```bash
python story_generator.py
```

### Example Interactions

**Adventure Story**:
```
Story request: A brave little mouse who goes on an adventure in the big city

The system will:
1. Categorize as "adventure"
2. Apply adventure-specific generation strategy (quest, obstacles, triumph)
3. Generate story with clear arc
4. Evaluate with judge (scores on 5 criteria)
5. Refine if needed based on feedback
6. Present final story with quality scores
```

**Bedtime Story**:
```
Story request: A bedtime story about the stars and moon

The system will:
1. Categorize as "bedtime"
2. Apply calming, soothing strategy
3. Use peaceful imagery and gentle rhythm
4. Ensure appropriate wind-down pacing
```

**Fairy Tale**:
```
Story request: A fairy tale about a kind princess and a friendly dragon

The system will:
1. Categorize as "fairy_tale"
2. Include magical elements and classic patterns
3. Use "once upon a time" openings
4. Create satisfying "happily ever after" ending
```

### User Feedback

After each story, you can:
- Request specific changes ("Make it funnier" or "Add more animals")
- Regenerate with your feedback
- Create a completely new story

## 🎯 Design Highlights

### Category-Based Generation Strategies

Each story category uses tailored prompting:
- **Adventure**: Quest structure, obstacles, bravery, problem-solving
- **Fairy Tale**: Magic, repetition (rule of 3), transformations
- **Animal Story**: Relatable personalities, cooperation, nature themes
- **Bedtime**: Calming rhythm, peaceful imagery, gentle resolution
- **Educational**: Natural learning, discovery, non-preachy lessons
- **General**: Universal themes, emotional balance, relatable characters

### Judge Evaluation System

Stories are approved only if:
- Overall score ≥ 7.5/10
- Age appropriateness ≥ 8/10 (critical for safety)
- No individual criterion < 6/10

The judge provides:
- Detailed scores for each criterion
- List of strengths to maintain
- Specific, actionable improvements
- Approval decision

### Iterative Refinement

- Maximum 2 iterations (balances quality vs. API cost)
- Refinement preserves original story concept
- Targeted improvements address specific weaknesses
- Strengths are maintained across iterations

## 🔧 Technical Details

- **Model**: `gpt-4o-mini` (as required by assignment)
- **Structured Outputs**: Pydantic models for type-safe evaluation
- **Story Length**: 400-600 words (optimal for bedtime reading)
- **Temperature**: 0.8 for creative generation, default for analysis
- **Safety**: Age-appropriate content filtering built into all prompts

## 📊 Quality Metrics

Every story is scored on:
1. **Age Appropriateness** (1-10): Suitable vocabulary and concepts for ages 5-10
2. **Engagement** (1-10): How interesting and captivating
3. **Story Structure** (1-10): Clear arc with beginning, middle, end
4. **Educational Value** (1-10): Positive messages and life lessons
5. **Language Clarity** (1-10): Simple, understandable language

Plus overall score (average of all criteria).

## 🎨 Example Output

```
┌─────────────────────────────────────────────────┐
│           ✨ Your Bedtime Story ✨              │
└─────────────────────────────────────────────────┘

[Story text with markdown formatting]

┌── Story Evaluation ──────────────────────────────┐
│ Quality Score: 8.4/10                            │
│                                                  │
│ Age Appropriateness: 9/10 | Engagement: 8/10    │
│ Structure: 9/10                                  │
│ Educational Value: 8/10 | Language Clarity: 8/10│
└──────────────────────────────────────────────────┘
```

## 🧪 Testing

Try these diverse requests:
- "A story about a curious robot learning about friendship"
- "An adventure with a brave squirrel and a treasure map"
- "A calming bedtime story about clouds"
- "A fairy tale with a dragon who loves to bake cookies"
- "An educational story about how plants grow"

## 📝 Code Structure

```
story_generator.py          # Main application
├── StoryCategory          # Enum for story types
├── CategoryAnalysis       # Pydantic model for categorization
├── JudgeEvaluation        # Pydantic model for evaluation
└── StoryGenerator         # Main class
    ├── categorize_request()      # Identify story category
    ├── get_generation_prompt()   # Category-specific prompts
    ├── generate_story()          # Story generation
    ├── judge_story()             # Quality evaluation
    ├── create_refinement_notes() # Convert feedback to instructions
    └── generate_with_judge()     # Full pipeline with iteration
```

## 🎓 Assignment Requirements Checklist

- ✅ Takes bedtime story requests
- ✅ Stories appropriate for ages 5-10
- ✅ LLM judge to improve quality
- ✅ Block diagram of system (see system_diagram.md)
- ✅ Uses gpt-4o-mini (unchanged)
- ✅ API key from environment (not committed)
- ✅ Advanced prompting strategies (category-based, structured outputs)
- ✅ Agent design (multi-agent: categorizer, storyteller, judge, refiner)
- ✅ Story arcs (clear beginning, middle, end)
- ✅ User feedback integration
- ✅ Categorization with tailored strategies

## 💡 Future Enhancements

Potential improvements:
- Multi-turn conversational storytelling (child influences direction)
- Persistent story history with favorites
- AI-generated illustrations
- Voice narration for read-aloud
- Web interface for easier access
- Character customization (name, appearance, traits)
- Story continuation feature (chapters/series)
- Multi-language support

## 📄 License

This is a coding assignment submission for Hippocratic AI. Feel free to use and modify as needed.

## 🙏 Acknowledgments

Built using:
- OpenAI GPT-4o-mini for story generation and evaluation
- Pydantic for structured data validation
- Rich for beautiful terminal interfaces
