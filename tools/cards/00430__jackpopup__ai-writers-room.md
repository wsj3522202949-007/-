---
id: tool-00430
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 需API密钥, 英文文档]
title: ai-writers-room
summary: 小说转语音/有声书
source: https://github.com/jackpopup/ai-writers-room
created: 2026-07-18
updated: 2026-07-18
no: 430
category: 二、网文 / 长篇 AI 写作系统 库
repo: jackpopup/ai-writers-room
stars: 7
url: https://github.com/jackpopup/ai-writers-room
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# jackpopup/ai-writers-room

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jackpopup/ai-writers-room
- **Stars**：7
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI Writers Room: 12명의 AI 전문가가 협업하는 글쓰기 + 강의 제작 스킬 for Claude Code | Writing team (7 agents) + Lecture Production team (5 agents) with HITL gates, multi-draft, fact-checking, TTS scripts (KO/EN/JP), PPT prompts
- **本地描述**：AI Writers Room: 12명의 AI 전문가가 협업하는 글쓰기 + 강의 제작 스킬 for Claude Code （ Writing team (7 agents) + Lecture Production team (5 agents) with HITL gates, multi-draft, fact-checking, TTS scripts (KO/EN/JP), PPT prompts
- **拉取时间**：2026-07-23 22:51:38

---

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Skill-blueviolet?style=for-the-badge&logo=anthropic" alt="Claude Code Skill" />
  <img src="https://img.shields.io/badge/Agents-12_Specialists-orange?style=for-the-badge" alt="12 Agents" />
  <img src="https://img.shields.io/badge/Drafts-3_Versions-green?style=for-the-badge" alt="3 Drafts" />
  <img src="https://img.shields.io/badge/Gates-4_HITL-red?style=for-the-badge" alt="4 Human-in-the-Loop Gates" />
  <img src="https://img.shields.io/badge/Languages-EN_KO_JP-blue?style=for-the-badge" alt="Multilingual" />
</p>

<h1 align="center">AI Writers Room</h1>

<p align="center">
  <strong>12명의 AI 전문가가 협업하는 글쓰기 + 강의 제작 스킬 for Claude Code</strong><br/>
  <b>글쓰기팀:</b> 기자 · 편집자 · 카피라이터 · PD · 팩트체커 · 교열 · 헤드라인 디렉터<br/>
  <b>강의팀:</b> 1타 강사 · 커리큘럼 기획자 · 치프 편집자 · EN/JP 번역가
</p>

<p align="center">
  <a href="#-설치">설치</a> ·
  <a href="#-작동-방식">작동 방식</a> ·
  <a href="#-벤치마크">벤치마크</a> ·
  <a href="#-콘텐츠-템플릿">템플릿</a> ·
  <a href="#-quick-mode">Quick Mode</a>
</p>

---

## What is this?

**AI Writers Room**은 Claude Code용 스킬(Skill)입니다. 설치하면/write 명령어만으로 **글쓰기**와 **강의 제작** 두 가지 파이프라인이 자동으로 작동합니다.

### 글쓰기 모드
```
"바이브코딩이 소프트웨어 산업을 어떻게 바꾸고 있는지 블로그 써줘"
```
이 한 줄로:
- 4명이 기획 회의 → 방향 합의
- 3가지 톤으로 동시 집필 (위트 / 서사 / 팩트)
- 팩트체커 + 교열 + 편집자 3인 검수
- 헤드라인 디렉터가 제목 9개 제안
- 비교표와 함께 최종 추천

### 강의 제작 모드
```
"Claude Code 보안 설정 유튜브 강의 만들어줘"
```
이 한 줄로:
- 1타 강사 + 기획자 + 편집자 3인이 기획
- 슬라이드별 발화문 + 데모 시나리오 포함 스크립트
- 커리큘럼 기획자의 전문 검수 (난이도, 흐름, 이탈 포인트)
- 외주용 영상 편집 가이드 자동 생성
- PPT 프롬프트 + TTS 스크립트 (KO/EN/JP)

**단순히 "글 잘 쓰는 AI"가 아니라, "콘텐츠를 잘 만드는 시스템"입니다.**

---

## 🚀 설치

### Option 1: .skill 파일 (가장 간단)

[Releases](../../releases) 에서 `ai-writers-room.skill` 다운로드 후:

```bash
claude install-skill ai-writers-room.skill
```

### Option 2: 이 레포에서 직접

```bash
git clone https://github.com/jackpopup/ai-writers-room.git
claude install-skill ai-writers-room/ai-writers-room.skill
```

### Option 3: SKILL.md 직접 복사

`SKILL.md` 파일을 Claude Code 프로젝트의 스킬 디렉토리에 복사해도 동작합니다.

---

## 🔄 작동 방식

### 4 Human-in-the-Loop Gates

AI가 자동으로 돌아가되, **4개의 체크포인트에서 반드시 사용자가 결정**합니다.
각 게이트에서 `.md` 파일을 먼저 저장하고, 사용자가 파일을 검토한 후 다음으로 진행합니다.

```
┌─────────────────────────────────────────────────────────┐
│                    AI Writers Room                        │
│                                                          │
│  Phase 1: PLAN          4명 병렬 기획                     │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                    │
│  │ 기자 │ │카피  │ │  PD  │ │편집자│  → 방향 합의서       │
│  └──────┘ └──────┘ └──────┘ └──────┘                    │
│                      ↓                                   │
│  Phase 2: DESIGN     구조 설계 → 구성안                   │
│                      ↓                                   │
│  🚦 GATE 1: 방향 승인                                     │
│  📄 direction-brief.md + outline.md 저장                  │
│  "이 방향이 맞나요? 톤/앵글 조정할 부분?"                   │
│                      ↓                                   │
│  Phase 4: DO         3명 병렬 집필                        │
│  ┌────────┐ ┌────────┐ ┌────────┐                       │
│  │  A안   │ │  B안   │ │  C안   │                       │
│  │ 위트풀 │ │ 서사적 │ │ 팩트형 │  → 3개 초안            │
│  └────────┘ └────────┘ └────────┘                       │
│                      ↓                                   │
│  🚦 GATE 2: 초안 선택                                     │
│  📄 draft-A.md, draft-B.md, draft-C.md 저장               │
│  "어떤 안을 발전시킬까요? 믹스할 부분은?"                    │
│                      ↓                                   │
│  Phase 5: CHECK      3명 병렬 검수                        │
│  ┌──────┐ ┌──────┐ ┌──────┐                             │
│  │팩트  │ │교열  │ │편집  │  → 검수 리포트               │
│  │체커  │ │팀장  │ │  자  │                              │
│  └──────┘ └──────┘ └──────┘                             │
│                      ↓                                   │
│  🚦 GATE 3: 수정 방향                                     │
│  📄 review-report.md 저장                                 │
│  "이 수정에 동의하시나요? 저자 의도로 유지할 부분은?"         │
│                      ↓                                   │
│  Phase 6: POLISH     헤드라인 디렉터                      │
│  ┌──────────────────────┐                               │
│  │ 제목 9개 + 리드문 3개 │  → 제목/요약                   │
│  └──────────────────────┘                               │
│                      ↓                                   │
│  🚦 GATE 4: 헤드라인 & 최종 선택                           │
│  "어떤 제목? 어떤 안? 마지막 수정사항은?"                    │
│  📄 final.md 저장                                        │
│  ┌──────────────────────┐                               │
│  │  ✅ 완성 원고         │                               │
│  └──────────────────────┘                               │
└─────────────────────────────────────────────────────────┘
```

### Why 4 Gates?

| Gate | 결정사항 | 저장 파일 |
|------|---------|----------|
| 🚦 **Gate 1** | 방향, 톤, 구조 승인 | `direction-brief.md`, `outline.md` |
| 🚦 **Gate 2** | 3개 초안 중 발전시킬 안 선택 | `draft-A.md`, `draft-B.md`, `draft-C.md` |
| 🚦 **Gate 3** | 검수 결과 반영 여부, 저자 의도 보호 | `review-report.md` |
| 🚦 **Gate 4** | 최종 헤드라인 + 원고 확정 | `final.md` |

> 💡 **파일 먼저, 질문은 그 다음.** 모든 게이트에서 `.md` 파일을 먼저 저장하므로, IDE에서 직접 열어보고 판단할 수 있습니다.

---

## 📊 벤치마크

동일한 글쓰기 요청에 대해 **스킬 사용 vs 미사용** 비교 테스트 결과:

| 지표 | AI Writers Room | 스킬 없음 | 차이 |
|------|:---:|:---:|:---:|
| **다중 초안** | ✅ 3가지 버전 | ❌ 1개만 | +200% |
| **팩트 체크** | ✅ 출처 검증 + 미검증 플래그 | ❌ 없음 | — |
| **헤드라인 옵션** | ✅ 9개 + 리드문 | ❌ 1개 | +800% |
| **분량 정확도** | ✅ 목표 ±10% | ❌ 2.5배 초과 | — |
| **Assertion Pass Rate** | **100%** (12/12) | 33% (4/12) | **+67%** |
| 토큰 사용량 | ~44K | ~24K | 1.8x |
| 소요 시간 | ~6분 | ~1분 | 6x |

> 💡 스킬 없이도 Claude는 글을 잘 씁니다. 이 스킬의 가치는 **글의 품질**이 아니라 **제작 프로세스**에 있습니다 — 다중 시각, 전문 검수, 선택지 제공.

---

## 📝 콘텐츠 템플릿

글 유형을 말하면 자동으로 최적 설정이 적용됩니다:

| 유형 | 톤 | 분량 | 추천 모드 |
|------|-----|------|-----------|
| **블로그** | 대화체, 접근성 | 1,200-2,000 words | Full Pipeline |
| **칼럼/사설** | 권위적, 논증적 | 800-1,500 words | Full Pipeline |
| **뉴스레터** | 친밀한, 1인칭 | 500-1,000 words | Full or Quick |
| **장문 피처** | 몰입적, 문학적 | 2,000-5,000 words | Full Pipeline |
| **보도자료** | 전문적, 팩트 중심 | 400-600 words | Quick Mode |
| **소셜 스레드** | 펀치, 스크롤 스톱 | 5-15 posts | Quick Mode |

---

## ⚡ Quick Mode

풀 파이프라인이 필요 없을 때:

```
"빨리 써줘" / "just write it" / "skip the process"
```

Quick Mode는 서브에이전트 없이 1개 초안을 바로 작성하되, 스킬의 구조적 감각(템플릿, 편집 관점, 헤드라인 옵션)은 그대로 적용합니다.

---

## 👥 The Team

| 역할 | 전문 분야 | 활약 단계 |
|------|----------|----------|
| 🗞️ **시니어 기자** | 팩트 기반 집필, 논점 구성 | Plan, Do(C안) |
| ✂️ **편집자** | 구조, 흐름, 가독성 | Plan, Check |
| ✍️ **카피라이터** | 후킹, 임팩트, 톤앤매너 | Plan, Do(A안) |
| 🎬 **PD/프로듀서** | 스토리텔링, 감정선 | Plan, Do(B안) |
| 🔍 **팩트 체커** | 출처 검증, 논리적 비약 탐지 | Check |
| 📝 **교열팀장** | 문법, 맞춤법, 문체 일관성 | Check |
| 🎯 **헤드라인 디렉터** | 제목, 리드문, 리듬감 | Polish |
| 🎨 **풍자 일러스트레이터** | 시각적 은유, AI 이미지 프롬프트 | On Request |

### 🎓 강의 제작팀

| 역할 | 전문 분야 | 활약 단계 |
|------|----------|----------|
| 🎤 **1타 강사** | 바이브코딩/AI 강의, 비유와 실습 설계 | Plan, Do |
| 📋 **커리큘럼 기획자** | 학습 목표, 난이도 곡선, 청중 분석 | Plan, Check |
| 🎬 **치프 편집자** | 컷 구성, 자막, 그래픽, 편집 가이드 | Plan, Post |
| 🌐 **IT 번역가 (EN)** | 영어 TTS 스크립트, IT 용어 현지화 | Localize |
| 🌐 **IT 번역가 (JP)** | 일본어 TTS 스크립트, 문화적 맥락 치환 | Localize |

### 강의 파이프라인

```
┌───────────────────────────────────────────────────────┐
│                 Lecture Production                      │
│                                                        │
│  Phase 1: PLAN        3명 병렬 기획                     │
│  ┌──────┐ ┌──────┐ ┌──────┐                           │
│  │1타강사│ │기획자│ │편집자│  → 강의기획서               │
│  └──────┘ └──────┘ └──────┘                           │
│                     ↓                                  │
│  🚦 GATE 1: 방향 승인                                   │
│  📄 강의기획서.md 저장                                   │
│  "이 방향이 맞나요? 구성/난이도 조정할 부분?"              │
│                     ↓                                  │
│  Phase 2: DO        1타 강사 집필                       │
│  ┌────────────────────────┐                           │
│  │ 강의 스크립트 (발화문    │                           │
│  │ + 슬라이드 + 데모)      │  → 강의스크립트             │
│  └────────────────────────┘                           │
│                     ↓                                  │
│  Phase 3: CHECK     기획자 검수                         │
│  ┌────────────────────────┐                           │
│  │ 학습목표/흐름/난이도    │  → 검수리포트               │
│  │ /이탈포인트 점검        │                            │
│  └────────────────────────┘                           │
│                     ↓                                  │
│  Phase 4: POST      치프 편집자                        │
│  ┌────────────────────────┐                           │
│  │ 컷 리스트, 자막, BGM,   │  → 영상편집가이드           │
│  │ 썸네일, 인트로/아웃트로  │                            │
│  └────────────────────────┘                           │
│                     ↓                                  │
│  🚦 GATE 2: 최종 승인                                   │
│  📄 모든 산출물 저장                                     │
│  "승인? TTS/PPT 프롬프트 필요?"                          │
│                     ↓                                  │
│  Phase 5: EXTRAS (선택)                                │
│  ┌──────┐ ┌──────┐ ┌──────┐                           │
│  │ TTS  │ │ PPT  │ │EN/JP │  → 추가 산출물             │
│  │스크립트│ │프롬프트│ │번역  │                           │
│  └──────┘ └──────┘ └──────┘                           │
└───────────────────────────────────────────────────────┘
```

### 강의 산출물

| 파일 | 설명 | 단계 |
|------|------|------|
| `강의기획서.md` | 주제, 구성, 타깃, 러닝타임 | Plan |
| `강의스크립트.md` | 발화문 + 슬라이드 노트 + 데모 | Do |
| `검수리포트.md` | 학습목표 달성도, 흐름, 난이도 점검 | Check |
| `영상편집가이드.md` | 외주 편집자용 가이드 | Post |
| `genspark-ppt-prompt.md` | Remotion 애니메이션용 PPT 프롬프트 | Extras |
| `TTS-스크립트-final.md` | 한국어 TTS 녹음용 | Extras |
| `TTS-EN-script.md` | 영문 TTS 녹음용 | Extras |
| `TTS-JP-script.md` | 일본어 TTS 녹음용 | Extras |

---

## 🌏 다국어 지원

- 한국어, 영어로 트리거 가능
- 선택적 번역 단계 (Localize): EN, JP 병렬 번역 지원
- 문화적 맥락 치환 포함 (예: 카카오톡 → LINE for JP)

---

## 🔧 요구사항

- **Claude Code** (Claude Code CLI 또는 VS Code Extension)
- **Claude Opus 4** 이상 권장 (서브에이전트 병렬 실행 지원)
- 별도 플러그인/라이브러리 **불필요** (독립 스킬)

---

## 📄 License

MIT License — 자유롭게 사용, 수정, 배포하세요.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  Made with ❤️ by <a href="https://github.com/jackpopup">POPUP STUDIO AI</a>
</p>
