---
id: tool-00831
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: pokemon_story_generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mrsyee/pokemon_story_generator
created: 2026-07-18
updated: 2026-07-18
no: 831
category: 二、网文 / 长篇 AI 写作系统 库
repo: MrSyee/pokemon_story_generator
stars: 21
url: https://github.com/mrsyee/pokemon_story_generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: e331c6b0c8c6c0c7
  - methods/最强写作方法论_全球最强综合版.md
---

# MrSyee/pokemon_story_generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mrsyee/pokemon_story_generator
- **Stars**：21
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：양재 AI 실무자 교육 6조 프로젝트
- **本地描述**：양재 AI 실무자 교육 6조 프로젝트
- **拉取时间**：2026-07-23 23:03:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Character Story Generator with SeqGAN
=====================================
## Team Members
- [김경환(Kim Kyunghwan)](https://github.com/MrSyee)
- [김동환(Kim Donghwan)](https://github.com/hwan141592)
- [김효진(Kim Hyojin)](https://github.com/Hy000jin)
- [류원탁(Ryu Wontak)](https://github.com/rroundtable)
- [박준섭(Park junsep)](https://github.com/557mp)
- [이채원(Lee Chaewon)](https://github.com/chaewon-lee)
- [임희목(Yim Heemok)](https://github.com/heemokyim)

## 목표
- 만화나 게임 캐릭터의 배경스토리를 학습하여 **새로운 배경 스토리를 만드는 AI**를 개발한다.
- 본 프로젝트에서는 **포켓몬스터 이야기**를 데이러로 딥러닝에 학습하여 새로운 캐릭터 이야기를 생성한다.
- 포켓몬스터 속성을 추가로 이용하여 **속성에 맞는 구체적인 이야기**를 생성한다.

## 설명
- 캐릭터는 배경스토리를 통해 상품성이 올라간다. 하지만 새로운 이야기를 창작하는 것은 쉽지 않은 일이다.
- 본 프로젝트는 이러한 새로운 캐릭터 창작 활동에 도움을 줄 수 있도록 영감과 소재(문장 형태)를 제공하는 것을 목표로 한다.
- 시퀀스를 생성해내는 SeqGAN은 LSTM을 이용한 `Generator`와 문장을 구분하는 CNN으로 구성된 `Discriminator`의 경쟁을 통해 학습한다.
- SeqGAN은 일반적인 GAN과 다르게 강화학습에서 사용하는 `Policy Gradient` 방법으로 학습한다.
- SeqGAN에 포켓몬스터 이야기를 학습시켜 새로운 포켓몬스터 이야기를 생성한다.
- 다양한 속성에 맞는 이야기를 만들기 위하여 `Conditional GAN` 방법과 `TF-IDF를 적용한 키워드` 방법을 제안한다.

## 진행과정
1. web crawler
    - 포켓몬스터 나무위키의 데이터 중 포켓몬스터 이름, 속성, 이야기를 수집하였다.
2. word embedding
    - 수집한 한글 데이터를 Word2Vec을 통해 벡터화하였다.
3. SeqGAN
    - 시퀀스 데이터를 생성해내는 SeqGAN 구조의 신경망에 데이터를 학습시켰다.
4. Conditional SeqGAN
    - 속설별 이야기 생성을 위하여 SeqGAN에 Conditional GAN 구조를 활용하였다.
5. TF-IDF
    - 전체 데이터에서 속성별 키워드를 추출하여 SeqGAN의 스타팅 토큰으로 입력하여 속성별 이야기를 생성한다.
6. docs
    - 최종 발표자료 모음.

## Model Architecture
### SeqGAN  
![](https://github.com/MrSyee/pokemon_story_generator/blob/main/img/SeqGAN_00.png)
![](https://github.com/MrSyee/pokemon_story_generator/blob/main/img/SeqGAN_1.png)
![](https://github.com/MrSyee/pokemon_story_generator/blob/main/img/SeqGAN_2.png)
### SeqGAN with condtion
![](https://github.com/MrSyee/pokemon_story_generator/blob/main/img/SeqGAN_with_condition.png)

## 결과
![](https://github.com/MrSyee/pokemon_story_generator/blob/main/img/result.PNG)

## Prerequisites
- python 3.6
- tensorflow 1.7.0
- bs4 0.0.1  
- gensim 3.5.0
- pandas 0.23.3
- konlpy 0.4.4
- scikit-learn 0.19.2
- nltk 3.3

## References
- [SeqGAN: Sequential Generative Adversarial Nets with Policy Gradient, IAAA, 2017](https://arxiv.org/abs/1609.05473)
- [SeqGAN (github)](https://github.com/LantaoYu/SeqGAN)
