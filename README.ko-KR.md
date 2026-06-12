# Art-Paper for Claude Code (한국어)

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D77757)](https://docs.claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-v0.1.1-blue)](https://github.com/joonhyungbae/art-paper/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![위키](https://img.shields.io/badge/wiki-KO%20%2F%20EN-blue)](https://apesuite.org/plugins/#/art-paper/ko/index)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

> 영어판(권위 있는 정본): [README.md](README.md) · 📖 위키: [한국어](https://apesuite.org/plugins/#/art-paper/ko/index) / [English](https://apesuite.org/plugins/#/art-paper/en/index)

**실천 기반 예술 연구 논문(practice-based art research paper)** 작성을 위한 Claude Code 플러그인입니다 — 창작적 탐구부터 심사를 거친 출판 준비 원고까지 전 과정을 art-and-technology venue 전반에서 지원합니다. 스코프는 특정 venue가 아니라 이 *장르*이며, 방법론과 무결성 점검은 venue 중립적입니다. 기본 reference target은 **SIGGRAPH Asia Art Papers 트랙**(논문집은 ACM Digital Library에 게재) — `acmart` + ACM Reference Format으로 wired. 비-ACM venue는 인용 포맷 전환(APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver)과 5가지 art-paper 구조 패턴으로 지원합니다. venue 특정값은 현행 CFP로 확인하세요.

작품이 **1차 증거**이지 데이터가 아닙니다. art-paper는 AI가 잘하는 부분 — 선행 작품 검색, ACM 인용 포맷팅, 구조 관례, 주장 앵커링 — 을 스캐폴딩해, 예술가-연구자만 할 수 있는 일(프로보케이션 설정, 작품 제작, 실천이 무엇을 드러내는지 판단)에 집중하도록 돕습니다.

---

## 동반 플러그인

**art-paper**와 **art-project**는 같은 메인테이너가 만든, 실천 기반 예술 연구를 위한 두 자매 Claude Code 플러그인으로, 프로젝트 생애의 양 끝을 담당합니다:

| | 플러그인 | 단계 | 스캐폴딩하는 것 |
|---|---|---|---|
| | **[art-project](https://github.com/joonhyungbae/art-project)** | *작품 이전* | 스튜디오 진입 전 언어화 — 충동 surfacing, 전통-태그 도발, 계보 위치잡기, Concept Brief, 자기비평 리허설 |
| **← 현재 위치** | **[art-paper](https://github.com/joonhyungbae/art-paper)** | *작품 이후* | 실천 기반 아트페이퍼 집필 — 탐구, 초안, ACM 인용, SIGGRAPH Asia 심사단, acmart LaTeX → PDF |

흐름: **art-project** 개념 언어화 → *스튜디오에서 작품 제작* → **art-paper** 심사용 논문 집필. 각각 독립적으로 쓸 수 있고, 함께 쓰면 개념-투-출판 전 구간을 잇습니다.

> 계보: 둘 다 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)(Cheng-I Wu)에서 내려옵니다. art-paper가 이 스위트를 아트페이퍼 장르로 포크했고, art-project가 다시 art-paper에서 스튜디오 진입 전 단계로 피봇했습니다.

---

## 30초 설치

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

설치 후 `/art-plan`으로 작업을 설명하면 소크라테스식 대화를 통해 구조(맥락 → 개념 틀 → 작품 → 구현 → 성찰)를 함께 잡아줍니다. 단발성 테스트는 `/art-lit-review "주제"`.

**👉 [위키 — apesuite.org/plugins/#/art-paper](https://apesuite.org/plugins/#/art-paper/ko/index)** — 이중 언어(EN + 한국어) 사용자 문서: 시작하기, 세 가지 진입점, 네 개 스킬, 방법론 개념, *Cutting Kim* worked example 전체 walkthrough.

**👉 [docs/SETUP.md](docs/SETUP.md)** — 사전 요건(Claude Code, `ANTHROPIC_API_KEY`, 정본 PDF용 선택 항목 Pandoc / LaTeX `tectonic` + ACM `acmart`), API 키, 선택적 교차모델 검증(`CRS_CROSS_MODEL` — 상위 스위트에서 상속한 환경변수명), 전체 설치 방법.

---

## 무엇을 하나

탐구 → 집필 → 심사 → 오케스트레이션을 담당하는 네 개 스킬, 그리고 예술 연구 장르 레이어.

| 스킬 | 모드 | 산출물 |
|---|---|---|
| **art-inquiry** | full · quick · review · lit-review · fact-check · socratic · systematic-review (7) | 개념 정리, 포지셔닝, 실천 기반 / 실천 주도 방법론, 선행작 + 이론 계보. socratic 모드가 프로보케이션을 끌어내고, 의도 감지가 조기 수렴을 막습니다. |
| **art-paper** | full · plan · outline · revision · revision-coach · abstract · lit-review · format-convert · citation-check · disclosure · **artist-statement** · **work-doc** (12) | Pattern 1(실천 기반 아트페이퍼) 초안 → **acmart LaTeX → PDF**; ACM Reference Format; 전용 artist-statement · 작품 documentation 모드. |
| **art-reviewer** | full · re-review · quick · realization-focus · guided · calibration (6) | SIGGRAPH Asia Art Papers 심사단 보고서 — **의장 + 큐레이터 + 실기연구자 + art-science 비평가 + Devil's Advocate** — 0–100 루브릭, gold set 대비 심사단 자체 FNR / FPR을 측정하는 calibration 모드. |
| **art-pipeline** | 오케스트레이터 (+ 재개) | 개념→출판 10단계 파이프라인, **작품 / 구현 주장 검증**으로 스코프된 두 무결성 게이트(Stage 2.5 + 4.5). |

**예술 연구 장르 레이어**(`shared/references/`): 작품이 1차 증거; 5가지 아트페이퍼 구조 패턴; 작품/전시 인용에 venue+date locator를 쓰는 ACM Reference Format(DOI 날조 금지); **2채널 AI 공시**(작품을 *만드는* 데 쓴 AI vs 논문을 *쓰는* 데 쓴 AI).

**예시로 하나 실행:**

- `/art-plan` — *"내 제너러티브 설치 작업에 대한 논문을 함께 써줘."*
- `/art-reviewer` — *"이 아트페이퍼를 심사해줘"* (이후 논문 제공).
- `/art-full` — 개념부터 acmart PDF까지 전체 파이프라인.
- 자연어: *"이 작품을 문서화해줘 (재료, 과정, 전시)."* 스위트가 의도로 자동 라우팅하고 결정을 투명하게 announce.

**👉 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — 흐름도, 단계별 행렬, 에이전트, 품질 게이트. 모드별 전체 트리거 문구는 각 `SKILL.md`와 [위키](https://apesuite.org/plugins/#/art-paper/ko/index)에 있습니다.

---

## 설계 근거

**AI는 부조종사이지 조종사가 아닙니다.** art-paper는 논문을 대신 써주지 않습니다. 선행 작품·이론 검색, ACM 인용, 주장 앵커링, 장르 관례 같은 스캐폴딩을 처리해 예술가-연구자가 해야 할 부분에 집중하도록 합니다. 휴머나이저와 달리 AI 사용을 숨기지 않습니다: **Style Calibration**이 과거 작업에서 당신의 목소리를 학습하고, **Writing Quality Check**가 AI 특유 패턴을 잡아 산문을 개선하며(탐지 회피가 아니라), 두 AI 사용 채널(작품 제작 vs 논문 작성)은 venue 정책에 따라 분리 공시됩니다.

**구조적 한계 대응.** 모든 AI 보조 집필 파이프라인에서 세 가지 실패 모드가 나타나며, 완화책은 장르 중립적이고 상위 스위트에서 변경 없이 상속됩니다:

1. **Frame-lock** — AI가 자기 논지를 비판하지만 당신이 설정한 틀 안에 머뭅니다. Devil's Advocate는 전제가 아니라 논거를 공격합니다.
2. **압박 하 sycophancy** — 밀어붙이면 너무 빨리 양보합니다. **Concession Threshold Protocol**이 모든 반론을 1–5로 채점하고, ≥4에서만 양보, 연속 양보 금지, 매 체크포인트 frame-lock 감지.
3. **의도 오탐** — 아직 탐색 중인데 소크라테스 멘토가 수렴하려 합니다. **Intent Detection Layer**가 3턴마다 탐색적 vs 목표지향을 분류하고 탐색 모드에서 자동 수렴을 끕니다.

**Dialogue Health Indicator**가 5턴마다 지속적 동의 / 갈등 회피 / 조기 수렴에 대해 조용히 자기점검을 돌립니다. 전체 7모드 체크리스트: [`art-pipeline/references/ai_research_failure_modes.md`](art-pipeline/references/ai_research_failure_modes.md); Stage 2.5 / 4.5 무결성 게이트가 이를 차단형 점검으로 실행합니다.

**인용 충실성.** art-paper는 L3 인용 충실성 기계장치를 유지합니다: 인용별 trust-chain provenance + locator 앵커, 그리고 각 인용 출처를 가져와 주장이 실제로 뒷받침되는지 판단하는 opt-in 감사 패스(`CRS_CLAIM_AUDIT=1` — 상위 스위트 상속 환경변수명). 다섯 HIGH-WARN 클래스(claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited)는 포매터에서 출력을 게이트-거부합니다. 아트페이퍼에서 *렌더링되는* 포맷은 ACM Reference Format이고, 작품·전시 인용은 DOI가 아니라 **venue+date**를 locator로 씁니다(미색인 작업의 DOI는 날조가 됨).

> 동기: Lu et al.(2026, *Nature* 651:914-919) — *The AI Scientist*는 자율 파이프라인 논문조차 구현 버그·환각 결과·frame-lock·인용 환각 같은 실패 모드를 안은 채 워크숍 동료심사를 통과할 수 있음을 보였습니다. Zhao et al.(2026-05, [arXiv:2605.07723](https://arxiv.org/abs/2605.07723))은 arXiv / bioRxiv / SSRN / PMC 1억 1천만 참고문헌을 감사해 2025년에만 약 14.7만 건의 환각 인용을 추정했습니다. art-paper는 이를 논문별 문제가 아니라 아키텍처 차원으로 다룹니다.

---

## 누구를 위한 것인가

**작품이 1차 증거**이고, 그 실천을 심사단이 읽어낼 수 있게 만들어야 하는 art-and-technology venue용 예술가-연구자 — 제너러티브·인터랙티브·넷·바이오·사운드·미디어 아트. 기본 타겟은 SIGGRAPH Asia Art Papers 트랙이지만 장르 레이어는 venue 중립적이며, 다른 venue는 인용 포맷 전환과 다섯 구조 패턴으로 닿습니다.

작품이 1차 증거이므로 구조는 IMRaD가 아니라 작품을 중심에 둡니다([`shared/references/art_paper_structure_patterns.md`](shared/references/art_paper_structure_patterns.md)):

- **실천 기반 아트페이퍼**(기본) — 맥락 → 개념 틀 → 작품 → 구현 → 성찰
- 과정 / 문서화 논문 · 개념 / 이론 에세이 · 전시 / 큐레이토리얼 사례연구
- IMRaD — art-science 하이브리드 패턴으로만 유지

작품을 날조하는 생성기, AI 사용을 숨기는 휴머나이저, 작품 제작을 대신하는 도구가 **아닙니다**. 수용(reception) 주장에는 관찰 가능한 앵커(특정 venue/날짜 + 관찰 내용)가, 신규성·기술 역량 주장에는 앵커 또는 헤지가 필요합니다 — reception inflation은 문체 선택이 아니라 무결성 플래그입니다.

---

## 동반 논문

출판된 사례에 대한 재구성-벤치마크 준수 감사(**generative-layer 셀에 걸쳐 ex-nihilo 날조 0건**, 사전등록된 hash-frozen 기준으로 검증)가 ***Digital Creativity***(Routledge / Taylor & Francis, AHCI)에 투고 단계입니다. 같은 재구성-벤치마크 방법론이 art-paper의 [*Cutting Kim* worked example](https://apesuite.org/plugins/#/art-paper/ko/examples/cutting-kim-case)을 뒷받침합니다(T = 0.2568 / G = 0.1261, margin +0.13, contamination 0.003 `ok`; clean-control variant는 margin을 −0.019로 무너뜨려 input-pack 추출 아티팩트 크기를 정직하게 드러냅니다).

플러그인은 논문보다 먼저 공개되며 그 자체로 사용 가능합니다; 기여는 플러그인이 인스턴스화하는 평가 프레임워크입니다. 재현성 패키지(input pack, gold brief, 사전등록 hash, 케이스별 결과)는 게재 확정 시 논문 supplementary 채널로 공개됩니다. 이 방법론 감사는 **art-project**와 공유하는 [동반 논문](https://github.com/joonhyungbae/art-project#companion-paper)입니다.

---

## 라이선스 & 인용

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 공유·수정·표기 가능, 비상업 사용 한정.

```text
art-paper, forked from Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## 출처

**메인테이너 — [Joonhyung Bae](https://github.com/joonhyungbae)** (KAIST). 예술 연구 특화(장르 레이어, SIGGRAPH Asia 심사단, 2채널 AI 공시, acmart 출력)는 전시 작가이자 peer-reviewed venue의 실천 기반 아트페이퍼 저자이며 AI 연구자인 메인테이너의 작업입니다.

**상위 — Academic Research Skills (ARS).** art-paper는 [Cheng-I Wu (吳政宜)](https://github.com/Imbad0202)의 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2에서 포크했습니다. 장르 중립 파이프라인 기계장치(Material Passport 핸드오프, L3 인용 충실성 게이트, generator-evaluator 계약, 무결성 게이트, anti-sycophancy / DA 채점, Collaboration Depth Observer)는 변경 없이 상속됩니다. diff용 pristine ARS는 `ref/academic-research-skills/`에 보관. 포크 설계: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

**상위 기여자** — art-paper가 계속 혜택을 받는 ARS 시기 작업: [@aspi6246](https://github.com/aspi6246)(read-only 제약 + anti-pattern 코드화), [@mchesbro1](https://github.com/mchesbro1)·[@cloudenochcsis](https://github.com/cloudenochcsis)(리뷰어 참고문헌), [@eltociear](https://github.com/eltociear)·[@xpfo-go](https://github.com/xpfo-go)(상위 README 번역).

---

## 저장소 구조

```text
art-paper/
├── art-inquiry/  art-paper/  art-reviewer/  art-pipeline/   # 4개 스킬 (SKILL.md + agents/ + references/)
├── skills/                            # Claude Code 스킬 디스커버리용 심볼릭 링크 → ../art-{inquiry,paper,reviewer,pipeline}
├── shared/references/                 # 예술 연구 장르 레이어 (구조·증거 모델·ACM 포맷·공시·용어집)
├── docs/                              # SETUP · ARCHITECTURE · PERFORMANCE · design/ 포크 spec
├── eval/  tests/                      # 재구성-벤치마크 instrumentation + stdlib 회귀 가드
├── ref/academic-research-skills/      # pristine ARS 참조 (diff용)
├── .claude-plugin/{plugin,marketplace}.json
└── README{,.ko-KR}.md, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY
```

---

## 변경 이력 (최근)

전체 이력은 [`CHANGELOG.md`](CHANGELOG.md). v0.1.0 미만 항목은 상속된 **academic-research-skills (ARS)** 변경 이력으로, [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md)에 그대로 보존됩니다.

- **v0.1.1** (2026-06-13) — *초기 공개 릴리즈.* 설치 결함 수정(`skills/` 심볼릭 링크를 fork 시기 깨진 `creative-*` → `../art-{inquiry,paper,pipeline,reviewer}`로 재연결); manifest 정합화(27 mode entries); 명칭 정규화(fork 시기 "Creative Research Skills" 라벨을 user-facing 전반에서 제거); *Cutting Kim* worked example 추가; `tests/`에 11개 stdlib 회귀 가드.
- **v0.1.0** (2026-05-22, art-paper 포크) — 4-스킬 스위트를 실증 과학 논문에서 **실천 기반 예술 연구 논문**(**SIGGRAPH Asia Art Papers 트랙** 타겟)으로 재특화. 4개 스킬 `git mv` 개명; 슬래시 커맨드 `ars-*` → `art-*` + 새 모드 2개(artist-statement, work-doc); `shared/references/` 장르 레이어 교체; 정본 출력을 **acmart LaTeX → PDF**로 이동(IRON RULE: PDF는 LaTeX에서 컴파일, HTML-to-PDF 금지); 리뷰어를 SIGGRAPH Asia 심사단으로 재구성; 무결성 게이트를 작품 / 구현 주장 검증으로 재스코프. 포크 설계: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

> 상속된 ARS 전체 이력(v1.0 → v3.9.4.2)은 [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md)에 있습니다 — art-paper는 상위 스위트 릴리즈 이력을 여기서 다시 서술하지 않습니다.
