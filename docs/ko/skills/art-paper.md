# art-paper

**예술 논문 작성 엔진.** 초안, 수정, 포맷, audit 모두 수행.

## 모드

| 모드 | 산출물 | 언제 사용 |
|---|---|---|
| `plan` | 섹션별 가이드 plan | 구조를 먼저 논의하고 싶을 때 |
| `full` | inquiry artifact로부터 full 초안 | 입력이 있고 초안 원할 때 |
| `outline-only` | 섹션 outline만 | 섹션 구조 확인 |
| `revision` | 리뷰어 feedback으로 수정한 draft | `art-reviewer` 다음 |
| `revision-coach` | 수정 결정을 가이드 | 리뷰에 어떻게 응답할지 모를 때 |
| `abstract-only` | 구조화된 초록 | 후반 polish |
| `lit-review` | 개념 계보 / 선행 작품 섹션만 | 나머지가 다 됐을 때 |
| `format-convert` | acmart LaTeX → PDF | 최종 단계 |
| `citation-check` | 모든 인용의 locator-anchor audit | 제출 전 integrity check |
| `disclosure` | AI-usage 2-channel 공개 | SIGGRAPH Asia / ACM 요구사항 |
| `artist-statement` | 독립 artist statement | venue가 요구할 때 |
| `work-doc` | 독립 작품 documentation | venue가 요구할 때 |

## 입력

- Concept & Provocation Brief (`art-inquiry`에서)
- Practice-Based Methodology Blueprint
- Annotated Bibliography
- Synthesis Report
- 선택: 기존 draft (`revision` 또는 `revision-coach` 모드)
- 선택: 리뷰어 feedback (`revision`)

## 출력 (`full` 모드)

**Practice-Based Art Paper 구조** (Pattern 1)를 따르는 `acmart`-class LaTeX manuscript:

- **제목 + 초록** (120–200단어) + 키워드 (4–6개)
- **Introduction / Context** — 작품 개요; 예술적·개념적 맥락; 작품이 추구하는 provocation; 기여 진술
- **Conceptual Framework** — 이론적·철학적 grounding; 선행 작품 및 작가와의 관계; 핵심 개념
- **The Work** — 형태, 재료, 미디어, 규모, 지속시간; 관객 경험; 저자권 및 협업 크레딧
- **Realization / Methods of Making** — 기술적 접근 (시스템, 알고리즘, 제작); 프로세스와 반복; 도구와 의존성
- **Reflection / Discussion** — 만들면서 발견한 것 (situated insight); 전시 및 수용; 개념 framework와의 관계; 한계와 열린 질문
- **Conclusion / Future Work**
- **References** (기본 ACM Reference Format, acmart 연동; 비-ACM venue용 대체 포맷: APA 7.0, Chicago, MLA 9, IEEE, Vancouver)
- **Acknowledgements + AI-usage disclosure** (2-channel) **+ 이미지 크레딧**

## Skill이 강제하는 IRON RULE

1. **인용 fabricate 금지.** 모든 reference는 사용자가 검증 가능한 locator로 resolve되어야 함.
2. **수용(reception) 주장 fabricate 금지.** 관찰 가능한 anchor 없이 "audiences were moved" 같은 표현은 flag.
3. **신규성 주장 fabricate 금지.** "First work to..." 는 anchor 또는 hedge 필요.
4. **기술적 capability 주장 fabricate 금지.** "Real-time", "autonomous" 는 anchor 필요.
5. **작가의 reading은 작가 책임.** Provocation과 reflection 섹션은 작가 저자권으로 표시; skill은 scaffold하지만 author 안 함.

## 페어링

- **선행**: `art-inquiry` (input pack 제공)
- **후속**: `art-reviewer` (초안 jury 리뷰)
- **최종**: `format-convert` (camera-ready)

## 주의

- skill은 draft를 만듭니다. 제출 준비됐다고 인증하지 않음. `art-reviewer` 실행 후 findings 처리.
- `disclosure` 모드는 template만 생성; 실제 AI 사용 사실은 작가가 채워야 함.
- `format-convert`는 `acmart.cls` 필요 (CTAN 또는 ACM). LaTeX 의존성 설치 안 해줌.
