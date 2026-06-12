# art-reviewer

**실천 기반 Art Papers 심사위원 시뮬레이션.** 5명 심사위원처럼 multi-perspective 리뷰 보고서 생성. 기본값은 SIGGRAPH Asia Art Papers 관례이며, 다른 실천 기반 예술 venue에도 적응.

## 심사위원단

| 역할 | 무엇을 검토 |
|---|---|
| **Chair** | Venue fit, scope, evidence에 sized된 contribution 주장 |
| **Curator** | Reception 주장, 전시 맥락, 현재 큐레이터 담론에서 작품 위치 |
| **Practitioner-Researcher** | 실천 내부 방법론, validity 기준, 작가의 저자 position |
| **Art-Science Critic** | 기술적 capability 주장, 신규성 주장, 과학-예술 인터페이스 |
| **Devil's Advocate** | 다른 4명이 놓친 것 — 일반화 과잉, 미공개 한계, anchor fabricate |

## 모드

| 모드 | 산출물 |
|---|---|
| `full` | 5명 reviewer 보고서 + Chair Editorial Decision Letter + Revision Roadmap |
| `re-review` | 수정 후 검증 리뷰 (각 수정 항목 확인) |
| `quick` | 통합 보고서 하나, 덜 상세 |
| `realization-focus` | 기술/실현 주장만 focus |
| `guided` | Socratic 모드 — 작가와 대화 |
| `calibration` | jury 평결을 venue의 실제 accept 기준과 비교 |

## 입력

- Complete art-paper 텍스트
- 선택: documentation, 전시 기록, 작품 이미지 (Curator + Practitioner에 도움)
- 선택: 이전 리뷰어 feedback (`re-review` 모드)

## 출력 (`full` 모드)

1. 5명 per-reviewer 보고서
2. Editorial Decision Letter (Accept / Minor revision / Major revision / Reject) with reasoning
3. Revision Roadmap — 우선순위 매긴 수정 목록 + effort estimate
4. R&R Traceability Matrix (Schema 11) — 각 수정을 source 리뷰 우려와 매핑

## 일반 리뷰어 skill과 다른 점

`art-reviewer`는 실천 기반 예술 논문 관례로 설정됨 (기본값 SIGGRAPH Asia Art Papers; 다른 venue에도 적응 가능):

- Reception 주장은 관찰 가능 anchor 필요 (이름 있는 venue/날짜 + 관찰 가능 디테일)
- 신규성 주장은 anchor 또는 hedge 필요
- 기술적 capability 주장은 anchor 또는 hedge 필요
- 공동작업 credit 명시 필요
- 저작권 / 전시권 / 이미지 출처 존중 필요
- AI-usage disclosure는 2-channel
- field-analyst agent가 subfield 자동 탐지 (kinetic, generative, bio-art, interactive installation, mixed reality, sound, photographic) 후 jury 구성

## 페어링

- **선행**: `art-paper` (리뷰할 draft 제공)
- **후속**: `art-paper revision` (Roadmap 따라 수정)
- **최종**: `art-reviewer re-review` (수정 적정성 검증)

## 주의

- Jury 평결은 시뮬레이션, 실제 리뷰어 아님. skill은 **제출 전 내부 리허설용**.
- `calibration` 모드는 근사치 — 발표된 venue 기준과 비교, 실제 accept committee 심의 아님.
- Devil's Advocate는 패스당 최소 3개 우려 찾도록 설정; severity 등급은 절대치 아니라 가이드.
