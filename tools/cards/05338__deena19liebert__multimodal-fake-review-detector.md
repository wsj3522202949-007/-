---
id: tool-05338
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: multimodal-fake-review-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/deena19liebert/multimodal-fake-review-detector
created: 2026-07-18
updated: 2026-07-18
no: 5338
category: 一、去 AI 味 / Humanizer 库
repo: deena19liebert/multimodal-fake-review-detector
stars: 1
url: https://github.com/deena19liebert/multimodal-fake-review-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: c14e8291cc72b291
  - methods/改稿润色指令库.md
---

# deena19liebert/multimodal-fake-review-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/deena19liebert/multimodal-fake-review-detector
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：First e-commerce focused AI review detector combining text, images, behavior & temporal patterns
- **本地描述**：First e-commerce focused AI review detector combining text, images, behavior & temporal patterns
- **拉取时间**：2026-07-25 18:14:53

---

# Multimodal Fake AI Review Detector for E-Commerce  
*Combining NLP, Image Forensics, Behavioral Analysis & Temporal Signals to Detect AI-Generated Fake Reviews*

##  **Core Innovation**
**First system to integrate:**  
✅ **Text Analysis** (LLM-generated text detection via fine-tuned BERT)  
✅ **Image Forensics** (GAN artifact detection in product photos)  
✅ **Behavioral Biometrics** (Reviewer activity patterns across platforms)  
✅ **Temporal Dynamics** (Detection of review bursts & unnatural timing)  

*Unlike prior work* ([Li et al. 2023](https://example.com) text-only; [Huang 2024](https://example.com) news-focused), this tool:  
- Targets **e-commerce-specific fraud patterns** (incentivized reviews, paid upvotes)  
- Uses **cross-modal consistency checks** (e.g., image metadata vs. text claims)  
- Provides **interpretable results** (e.g., "Flagged: 5 reviews in 2 mins + image GAN score=0.92")  

---

##  **Evidence of Novelty**  
| Aspect          | Existing Solutions | Our Approach |
|-----------------|--------------------|--------------|
| Modalities      | 1-2 (text/image)   | **4+ integrated** |
| Domain          | Social media/news  | **E-commerce** |
| Real-time       | Batch processing   | **Dynamic thresholds** |
| Explainability  | Black-box          | **Rule-based + ML fusion** |

**Literature gaps confirmed via:**  
- Connected Papers graph (no matches for "e-commerce + multimodal + temporal")  
- Google Scholar alerts (last checked: 31-July-2025)  

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

##  **Technical Preview**  
```python
# Pseudocode of core innovation
def detect_fake(review):
    # Multimodal feature extraction
    text_score = bert_llm_detect(review.text)
    image_score = gan_forensics(review.image)
    behavior_score = analyze_user_history(review.author)
    
    # Context-aware fusion
    if behavior_score > 0.8 and image_score > 0.7:
        return "HIGH RISK: Suspicious behavior + AI-generated image"
    elif text_score > 0.9 and time_between_reviews < 10s:
        return "MEDIUM RISK: LLM text + unnatural timing"
