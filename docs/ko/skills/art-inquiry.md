# art-inquiry

**실천 기반 예술 연구의 선행 엔진.** 작품과 질문은 있지만 아직 초안이 없을 때 사용.

## 모드

| 모드 | 산출물 | 언제 사용 |
|---|---|---|
| `socratic` | 개념과 provocation을 끌어내는 가이드 대화 | 작품이 무엇을 주장하는지 아직 articulate 안 됨 |
| `full` | Concept & Provocation Brief + Methodology Blueprint + Annotated Bibliography + Synthesis Report | 질문은 알지만 구조화된 artifact 필요 |
| `quick` | `full` 의 경량 버전 | 시간 압박 첫 패스 |
| `review` | 기존 inquiry의 비판적 리뷰 | 타인 brief 검증 |
| `lit-review` | annotated bibliography만 | 참고문헌 survey만 필요 |
| `fact-check` | inquiry artifact의 사실 주장 검증 | 제출 전 audit |
| `systematic-review` | systematic-review article-type artifact | 작품 paper 아니라 문헌 paper인 경우 |

## 입력

- 짧은 주제 seed (1-3 문장)
- 선택: 작품의 사실 문서 (형태, 메커니즘, 전시 기록)
- 선택: 이미 있는 draft provocation

## 출력 (full 모드)

1. **Concept & Provocation Brief** — 작품이 무엇을 주장하는지, 왜 중요한지, prior work에 대해 어디 위치하는지
2. **Practice-Based Methodology Blueprint** — 작품 / 문서 / 글쓰기 / 수용이 어떻게 evidence로 triangulate되는지
3. **Annotated Bibliography** — precedent 작품 + 이론, 각각이 무엇을 기여하는지 주석
4. **Synthesis Report** — inquiry의 findings, art-paper skill이 consume할 준비 완료

## Socratic 모드 {#socratic-mode}

자신의 provocation을 아직 모를 때 `socratic` 모드가 가이드 대화 실행:

```
/art-inquiry socratic [작품] 을 만들었어. 그것에 대해 쓰고 싶은데 무엇을 주장하는지 모르겠어.
```

skill이 짧고 targeted한 질문을 하나씩 던져 외부에서 framing을 강요하지 않고 작가 본인의 framing을 표면화.

## 페어링

- **후속**: `art-paper`가 synthesis report를 input pack으로 consume
- **교차 검증**: `art-reviewer`의 `guided` 모드가 글쓰기 시작 전 inquiry artifact 리뷰 가능

## 주의

- Provocation, reflection, 상황적 해석은 작가의 저자 책임. inquiry는 질문을 articulate, 답을 하지 않음.
- Lit-review 모드는 공개 bibliographic 소스 검색하나 접근성 확인 안 함; locator는 인용 전 확인 필요.
- Systematic-review 모드는 article-type artifact 생성하나, 그 안 evidence 표준은 작가 본인 책임.
