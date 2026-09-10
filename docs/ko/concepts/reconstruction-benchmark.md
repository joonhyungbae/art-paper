# Reconstruction benchmark

## 설정

Reconstruction benchmark는 플러그인의 동반 paper가 도입하는 평가 방법론입니다. 4부분:

1. **Input/gold firewall.** 인간 auditor가 플러그인에 주는 자료 (input)와 숨겨두는 paper (gold) 사이의 절차적 분리 강제.
2. **재구성 task.** 플러그인에 사전 자료만 (documentation, 전시 기록, 사실 기반 concept memo, bibliography) 주고 paper 재구성 요청.
3. **Inversion rule.** Held-out paper와의 유사도를 성공이 아니라 contamination 의심으로 읽음. ([Inversion rule](inversion-rule.md) 참조.)
4. **Per-layer split.** "Documentable" 층 (사실 기술, prior-work lineage, 전시 기록)과 "generative" 층 (provocation, reflection, 상황적 discussion)에 대해 유사도를 따로 측정.

## Benchmark가 측정하는 것

각 case에 대해, instrumentation이 보고:

- **Transferable-layer 유사도** `T` — 재구성된 documentable 내용이 gold와 얼마나 닮았는지
- **Generative-layer 유사도** `G` — 재구성된 generative 내용이 gold와 얼마나 닮았는지
- **Per-layer ordering** — `T > G` 인지 (예상: documentable 층이 generative 층보다 더 닮음)
- **Contamination probe** — 재구성과 gold 사이 8-gram 겹침; 잠재적 memorisation flag
- **Structural coverage** — 재구성이 gold의 섹션 구조의 몇 %를 재현했는지
- **Citation recall과 precision** — 재구성된 bibliography가 gold의 것과 얼마나 겹치는지

## Benchmark가 측정하지 **않는** 것

- AI 출력이 "좋은지"
- AI가 창의적인지
- 사용자가 출력을 유용하다고 느낄지

이것들은 설계상 out of scope. Benchmark는 specific corpus에서 documentable-vs-generative 구분이 감지 가능한지 detect하기 위해 존재 — 그 이상 아님.

## "Discriminant validity" 검증

실천 기반 예술 paper가 아닌 corpus (예: 경험적 과학 논문)에 benchmark를 돌리면 layer-split signature가 실천 기반 글쓰기에 unique한지, layer 정의의 일반 속성인지 감지하는 데 도움이 된다. Digital Creativity 동반 원고는 비예술 대조군을 보고하지 않는다.

## "Clean control" 검증

Benchmark의 더 strict한 버전은 input pack을 작품의 **독립 공개 footprint** (작가의 외부 진술, festival 페이지, 전시 카탈로그)에서 구성, gold paper 아님. Input 추출 자체가 저자 cue 가능성을 보호. 동반 paper가 evaluation corpus의 여러 case에서 보고; directional 신호 유지되나 margin 축소 — input-pack 추출이 non-zero artifact 기여한다는 것과 일관.

Clean control은 각 case의 독립 footprint이 무엇을 포함하는지에 bounded — 평가 corpus(SIGGRAPH Asia에서 추출) 내 대부분 paper가 단일 전시 venue를 listing → clean-control 확장은 effort-bound 아니라 corpus-bound.

## 플러그인에서 나타나는 곳

- `art-paper` skill의 `citation-check` 모드는 benchmark의 일부인 인용-locator audit 실행
- `art-reviewer` skill의 integrity-gate 로직은 동일한 inversion rule 사용
- 전체 instrumentation script는 동반 paper의 reproducibility mirror 내 `eval/instrumentation.py`에 위치
- 한 case에 benchmark 적용한 worked example은 [Cutting Kim 사례 연구](../examples/cutting-kim-case.md) 참조
