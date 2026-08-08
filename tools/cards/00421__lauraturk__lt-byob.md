---
id: tool-00421
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: lt-byob
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lauraturk/lt-byob
created: 2026-07-18
updated: 2026-07-18
no: 421
category: 二、网文 / 长篇 AI 写作系统 库
repo: lauraturk/lt-byob
stars: 0
url: https://github.com/lauraturk/lt-byob
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2968639df7e78d09
  - methods/最强写作方法论_全球最强综合版.md
---

# lauraturk/lt-byob

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/lauraturk/lt-byob
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Turing School of Software and Design Mod4 Build Your Own Backend Project - building a madlib api sourced from Amazon's editors picks for Romance Novels
- **本地描述**：Turing School of Software and Design Mod4 Build Your Own Backend Project - building a madlib api sourced from Amazon's editors picks for Romance Novels
- **拉取时间**：2026-07-23 22:51:23

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Build Your Own Backend - BYO-MadLib

#### A practice RESTful API that collects and parses book blurbs culled from Amazon's *Best of the Month* Romance Novel Section and Good Reads Romance novels. Every text sample is parsed and every word is tagged with its part of speech using textprocessing.com's API. This API gives you access to text samples and their corresponding four major categories of parts of speech: Nouns, Adverbs, Adjectives, and Verbs. Might there be a heaving bosom or a rakish cad to stir your heart? 



[Original Assignment](http://frontend.turing.io/projects/build-your-own-backend.html)



## End Points



### GET

* '/api/v1/text_samples' : returns a json response of all the original book blurb and book title

* '/api/v1/words' : returns a json response of all words

* '/api/v1/text_samples/:id' : returns a json response a specific text_sample

* '/api/v1/words/:id' : returns a json response of a single word

* '/api/v1/verbs' : returns a json response of all words labeled as Verbs

* '/api/v1/adverbs' : returns a json response of all words labeled as Adverbs

* '/api/v1/adjectives' : returns a json response of all words labeled as Adjectives

* '/api/v1/nouns' : returns a json response of all words labeled as Nouns

* '/api/v1/:text_samples/:id/words' : returns a json response of all the words for a given text sample by text sample id



## Resources



#### Word Type Key:

##### Adjectives

* JJ - Adjective

* JJR - Adjective, comparative

* JJS - Adjective, superlative

##### Nouns

* NN - Noun, singular or mass

* NNS - Noun, plural

* NNP - Proper noun, singular

* NNPS - Proper noun, plural

##### Adverbs

* RB - Adverb

* RBR - Adverb, comparative

* RBS - Adverb, superlative

##### Verbs

* VB - Verb, base form

* VBD - Verb, past tense

* VBG - Verb, gerund or present participle

* VBN - Verb, past participle

* VBP - Verb, non-3rd person singular present

* VBZ - Verb, 3rd person singular present



##### More Resources

* [Amazon Books](https://www.amazon.com/books-used-books-textbooks/b/ref=nav_shopall_bo_t3?ie=UTF8&node=283155)

* [Text Processing.com(API)](http://text-processing.com/docs/tag.html)

* [Penn Treebank Tags](http://web.mit.edu/6.863/www/PennTreebankTags.html#ADJP)

* [Tutorial for setting up TDD test environment](http://mherman.org/blog/2016/04/28/test-driven-development-with-node/#.WWQ1M2RKXEY)

* [References for testing, knex, express](http://frontend.turing.io/lessons/)

