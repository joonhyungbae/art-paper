# Inversion rule

## 한 문장

> Held-out paper와의 높은 유사도를 성공이 아니라 contamination 의심으로 읽어라.

## 왜 이 규칙이 필요한가

순진한 평가는 AI 생성 paper를 원본과 비교, 높은 유사도가 "AI가 잘했다"는 뜻으로 봅니다. 실천 기반 예술 paper (그리고 일반적으로 작고 공개된 specialised 장르)에서는 broken:

- Corpus가 작아서 원본이 모델에 plausibly memorise됨
- Reference-based metric은 contamination 하에서 authoring 아니라 memorisation에 보상
- 도구 만든 사람이 평가도 함 — 높은-유사도-=-성공이면 어느 도구든 외워서 "이김"

Inversion rule의 응답: **읽는 방향을 뒤집어라.** Held-out paper와의 높은 유사도, 특히 생성적 층에서, memorisation 경고.

## 플러그인에서 규칙 작동 방식

Contamination probe는 8-gram containment metric 계산 — 재구성에서 gold paper에 verbatim 나타나는 8-token sequence 비율. 3개 sub-flag:

| 범위 | Sub-flag | 조치 |
|---|---|---|
| `< 0.03` | `ok` | Memorisation 우려 없음 |
| `[0.03, 0.10)` | `elevated` | **조사** — 내용 보존 paraphrase 또는 공유 boilerplate |
| `>= 0.10` | `high-warning` | Memorisation flag — inversion rule이 성공으로 읽기 거부 |

동반 paper가 보고: evaluation corpus의 여러 실천 기반 예술 paper에서 0.10 임계값 넘긴 case 0; F1 의도적 firewall 위반 case (provocation을 input에 주입)에서 probe가 elevated 대역으로 상승 (0.03 elevated와 0.10 high-warning 사이), 설계대로.

## 규칙이 **하지 않는** 것

- **창의적 AI 감지 안 함.** Verbatim 또는 near-verbatim 재현 감지; lexical 재현 없는 의미적 memorisation은 probe trigger 안 함.
- **품질 점수 안 매김.** 재구성이 probe를 통과해도 빈약할 수 있음; probe는 contamination 필터, 품질 측정 아님.
- **독창성 인증 안 함.** Probe 통과는 "8-gram 수준에서 감지 가능한 memorisation 없음" 의미. 더 높은 차원 독창성은 플러그인이 답하지 않는 별개 질문.

## 결합 평결

Inversion rule만으로는 부족. 플러그인은 **per-layer split** 과 결합:

- 낮은 contamination AND `T > G` → directional reading 지지 (documentable 층이 generative 층보다 더 수렴, firewall 유지될 때 예상되는 대로)
- 낮은 contamination AND `T ≤ G` → 특이; layer 정의나 input-pack 구성 조사
- Elevated/high contamination, 어떤 `T-G` → contamination 경고 우선; layer reading 신뢰 불가

이것이 동반 paper에서 "joint package"라고 부르는 것 — firewall + inversion rule + per-layer instrument가 함께 작동.

## 플러그인에서 나타나는 곳

- `art-reviewer` integrity-gate 로직이 draft에 규칙 적용 (이전 버전과 비교)
- `art-paper citation-check` 모드는 citation 수준 analog 적용 (모든 인용은 verifiable locator로 resolve되어야 함)
- 전체 contamination probe와 per-layer instrumentation은 동반 paper의 `eval/instrumentation.py`에 위치
