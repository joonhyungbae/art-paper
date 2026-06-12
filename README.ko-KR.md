# art-paper for Claude Code (한국어)

[![Version](https://img.shields.io/badge/version-v0.1.1-blue)](https://github.com/joonhyungbae/art-paper/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)

> 영어판(권위 있는 정본): [README.md](README.md). 이 문서는 한국어 요약본이며, 세부 변경 이력은 영어판을 따릅니다.

**실천 기반 예술 연구 논문(practice-based art research paper)** 작성을 위한 Claude Code 스킬 모음입니다. 창작적 탐구부터 심사를 거친 출판 준비 원고까지 전 과정을 다루며, **SIGGRAPH Asia Art Papers 트랙**(논문집은 ACM Digital Library에 게재; 카테고리/게재처는 현행 CFP로 확인)에 특화되어 있습니다.

> **[academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2에서 포크.** 장르 중립적 파이프라인 기계장치 — Material Passport 핸드오프, L3 인용 충실성 게이트, generator-evaluator 계약, 무결성 게이트 — 는 그대로 상속합니다. 실증과학 장르 레이어(증거 위계, IMRaD, APA, 방법론 심사)를 예술 연구 장르 레이어(작품-as-증거, 실천 기반 구조, ACM Reference Format, 큐레이터·실기연구자 심사)로 교체했습니다. 포크 설계: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

**30초 설치** (Claude Code CLI / VS Code / JetBrains):

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

설치 후 `/art-plan`으로 소크라테스식 대화를 통해 논문 구조를 잡아보거나, 아래 [빠른 설치](#빠른-설치)에서 사전 요건과 전통적 symlink 방식을 확인하세요.

**👉 [위키 — apesuite.org/plugins/art-paper](https://apesuite.org/plugins/art-paper/)** — 이중 언어(EN + 한국어) 사용자 문서: 시작하기, 세 가지 진입점, 네 개 스킬, 방법론 개념, *Cutting Kim* worked example 전체 walkthrough.

> **AI는 부조종사이지 조종사가 아닙니다.** 이 도구는 논문을 대신 써주지 않습니다. 스캐폴딩 — 선행 작품·이론 정리, ACM 인용 포맷팅, 작품·구현 주장이 관찰 가능한 증거에 닻 내려 있는지 점검, 장르 관례 준수 — 을 처리해, 정작 예술가-연구자가 해야 할 일(프로보케이션 설정, 작품 제작, 실천이 무엇을 드러내는지 판단, "이 작업은 ~을 주장한다" 다음 문장 쓰기)에 집중하도록 돕습니다.
>
> 작품을 *만드는 데* 쓴 AI와 논문을 *쓰는 데* 쓴 AI는 venue 정책에 따라 **두 채널로 분리 공시**됩니다.

---

## 아키텍처 & 파이프라인

전체 단계별 행렬(에이전트·산출물·게이트)은 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)를 참고하세요.

```
art-inquiry (socratic/full)        # 창작 탐구: 개념·프로보케이션, 포지셔닝, 실천 기반 방법론, 선행작
  → art-paper (plan/full)          # 아트페이퍼 집필
    → 무결성 점검 (Stage 2.5: 인용 + 작품/구현 주장)
      → art-reviewer (full/guided) # SIGGRAPH Asia Art Papers 심사단
        → art-paper (revision)
          → art-reviewer (re-review, 최대 2회)
            → 최종 무결성 점검 (Stage 4.5)
              → art-paper (format-convert → acmart LaTeX → PDF)
                → 프로세스 요약 + AI 자기성찰 보고서
```

## 빠른 설치

**플러그인 방식(권장):**
```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```
> 참고: marketplace 엔드포인트는 art-paper 자체 저장소 `joonhyungbae/art-paper`입니다. 전통적 symlink 방식은 [`docs/SETUP.md`](docs/SETUP.md)를 참고하세요.

## 성능 & 비용

전체 파이프라인 1회 실행 ≈ Opus 4.7 기준 약 $4–6. 자세한 토큰 예산·장시간 세션 가이드는 [`docs/PERFORMANCE.md`](docs/PERFORMANCE.md).

## 한눈에 보는 특징

- **작품이 1차 증거** — 데이터·통계가 아니라 작품 자체와 그 제작·전시·수용을 삼각검증.
- **ACM Reference Format** 기본 인용, **acmart LaTeX → PDF** 출력(기본 클래스 `sigconf`; 정확한 클래스는 현행 CFP 확인).
- **SIGGRAPH Asia Art Papers 심사단** 시뮬레이션: 의장 + 큐레이터 + 실기연구자 + art-science 비평가 + Devil's Advocate.
- **L3 인용 충실성 게이트** 상속 — 모든 인용에 locator 앵커, 작품/전시 인용은 venue+date를 locator로 사용(DOI 날조 금지).
- **2채널 AI 공시** — 작품 제작용 AI vs 논문 작성용 AI 분리.

## 사용법

### 빠른 시작
```text
# 전체 아트페이퍼 파이프라인
내 인터랙티브 설치 작업에 대한 아트페이퍼를 SIGGRAPH Asia에 제출하려고 해

# 소크라테스식 안내
내 제너러티브 작업의 개념을 함께 정리해줘

# 기존 논문 심사
이 아트페이퍼를 심사해줘
```

### 15개 슬래시 커맨드
`/art-full` `/art-plan` `/art-outline` `/art-revision` `/art-revision-coach` `/art-abstract` `/art-lit-review` `/art-reviewer` `/art-format-convert` `/art-citation-check` `/art-disclosure` `/art-artist-statement` `/art-work-doc` `/art-mark-read` `/art-unmark-read`.

### 지원 인용 포맷
**ACM Reference Format(기본)**. 비-ACM venue용으로 APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver도 지원(비-default).

### 지원 논문 구조
[`shared/references/art_paper_structure_patterns.md`](shared/references/art_paper_structure_patterns.md) — 기본 **실천 기반 아트페이퍼**(Pattern 1), 그 외 artist-statement / 비평·이론 에세이 / 시리즈·포트폴리오 / art-science 하이브리드. IMRaD는 art-science 하이브리드(Pattern 5)로만 존재.

## 스킬 상세

| 스킬 | 역할 |
|---|---|
| **art-inquiry** v0.1.1 | 실천 기반 예술 연구의 선행 엔진 (개념 정리, 포지셔닝, 실천 기반 방법론, 선행작·이론) |
| **art-paper** v0.1.1 | 아트페이퍼 집필 엔진 (구조, 초안, ACM 인용, acmart 출력) |
| **art-reviewer** v0.1.1 | SIGGRAPH Asia Art Papers 심사단 (의장+큐레이터+실기연구자+art-science 비평가+DA) |
| **art-pipeline** v0.1.1 | 10단계 파이프라인 오케스트레이터 (상태기계 그대로 상속) |

## 핵심 규칙 (예술 장르)

- 작품이 1차 증거 — 모든 주장은 [증거 모델](shared/references/art_research_evidence_model.md)의 증거 유형에 닻 내림.
- 수용(reception) 주장은 관찰 가능한 앵커(특정 venue/날짜 + 관찰 내용)가 필요 — "관객이 감동했다" 식의 무근거 진술(reception inflation)은 무결성 플래그.
- 신규성/선행성("최초의 작업…"), 기술 역량("실시간", "자율적") 주장은 앵커 또는 헤지 필요.
- 협업 크레딧 명시, 저작권·전시권·이미지 courtesy line 준수.
- AI 사용은 2채널(작품 제작 vs 논문 작성)로 공시; **venue 특정값은 반드시 현행 SIGGRAPH Asia Art Papers CFP로 확인** — art-paper는 확인 불가한 수치를 지어내지 않음.

## AI의 구조적 한계, 그리고 art-paper의 대응

frame-lock, 압박 하 sycophancy, 의도 오탐 등 — 상위 ARS 스위트(v3.0)에서 발견된 장르 중립적 현상과 그 완화책(Devil's Advocate 양보 임계값, 의도 감지, 대화 건강도 점검)을 그대로 상속합니다. 자세한 내용은 영어판 README 및 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) 참고.

## 라이선스

CC BY-NC 4.0. 상위 academic-research-skills(저자: Cheng-I Wu)에서 포크.

## 변경 이력

### v0.1.1 (2026-06-13) — 초기 공개 릴리즈

> 공개 릴리즈 직전 사전 history를 단일 시작 commit으로 압축했습니다. 상세 항목은 [`CHANGELOG.md`](CHANGELOG.md)에 보존, 상위 포크 계보는 `ref/academic-research-skills/CHANGELOG.md`에 그대로 유지.

- **설치 결함 수정**: `skills/`의 fork 시기 깨진 심볼릭 링크(`creative-*` → 없는 대상)를 실제 `../art-{inquiry,paper,pipeline,reviewer}`로 재연결. fresh clone에서 네 개 핵심 skill 모두 정상 등록.
- **manifest 정합화**: `marketplace.json` 설명을 실제 모드 수(27 entries: art-inquiry 7 + art-paper 12 + art-reviewer 6 + art-pipeline orchestrator + 재개 = 2)에 맞춤. MODE_REGISTRY의 "creative pipeline" 트리거 잔재를 "art pipeline"으로 교체.
- **명칭 정규화**: fork 시기 명칭 "Creative Research Skills"를 위키·mkdocs 사이트 제목·FAQ·인용 BibTeX·skeleton 예시 전반에서 제거. 플러그인 이름은 **Art-Paper**.
- **한국어 워딩**: 영어 upstream/downstream의 직역 "상류/하류"를 "선행/후속"으로 교체.
- ***Cutting Kim* worked example 추가**: 저자의 SIGGRAPH Asia 2025 art paper로 reconstruction-benchmark walkthrough (T = 0.2568 / G = 0.1261, margin +0.13, contamination 0.003 `ok`) + clean-control variant.
- **sanity 테스트 11개** 추가 (`tests/`): skills 심볼릭 링크 해석, manifest 버전 동기, marketplace mode 수치, 위키 회귀 가드(Creative Research Skills/Emerald Harvard/fork-시기 path), instrumentation smoke.

### v0.1.0 (2026-05-22) — art-paper 포크 (아트페이퍼 특화)
- 4개 스킬을 `art-{inquiry,paper,reviewer,pipeline}`로 재특화 (ARS의 `deep-research`/`academic-paper`/`academic-paper-reviewer`/`academic-pipeline`에서 history-preserving `git mv` 적용).
- shared 예술 연구 장르 레이어 5종 신설(구조 패턴·증거 모델·ACM 인용·SIGGRAPH/ACM 공시·예술 용어집).
- 전 SKILL.md + ~33개 에이전트를 예술 장르로 변환(작품-as-증거, ACM 인용, acmart 출력, SIGGRAPH Asia 심사단).
- 패키징 리브랜딩(15개 `art-*` 커맨드, 매니페스트, hooks, announce, 영어 문서 일체).
- 장르 중립 기계장치(Material Passport, L3 게이트, generator-evaluator 계약, 무결성 게이트) 그대로 상속.

상속된 ARS 전체 변경 이력(v1.0 → v3.9.4.2)은 [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md) 참고.
