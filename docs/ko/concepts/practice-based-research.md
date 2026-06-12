# 실천 기반 연구

실천 기반 예술 연구는 정보과학이 attend해야 할 30년 짜리 주장을 가지고 있습니다: **작가는 만드는 동안 형성되는 앎이 있고, 그것은 문서만으로 전달되지 않는다.**

## 계보

| 출처 | 무엇을 articulate |
|---|---|
| **Polanyi (1966)**, *The Tacit Dimension* | "우리는 말로 할 수 있는 것보다 더 알고 있다." 명시적 기술 밑에 tacit 앎이 있음. |
| **Schön (1983)**, *The Reflective Practitioner* | Reflection-in-action: 진행 중인 실천이 자기 자신에 응답 가능한 판단을 지속적으로 만든다. 판단은 doing과 독립적으로 존재하지 않음. |
| **Frayling (1993)**, *Research in art and design* | 3분법 — 예술 **into**, **for**, **through** 연구. 실천 기반 작업은 "through" 연구. |
| **Candy (2006)**, *Practice Based Research: A Guide* | PBR 박사 프레임워크 operationalise: 창작 결과물이 지식 기여의 일부. |
| **Borgdorff (2012)**, *The Conflict of the Faculties* | 학계에서 예술 연구의 인식론적 위상 옹호. Knowing-in-the-doing과 knowing-about-the-doing 구분. |
| **Nelson (2013)**, *Practice as Research in the Arts* | 사회과학에서 가져온 게 아닌, 실천 내부 validity 기준 주장. |
| **Haseman (2006)**, *A Manifesto for Performative Research* | 실천을 distinct 연구 패러다임으로; 산출물 자체가 연구이지 그 evidence가 아님. |

## 이것이 플러그인에 의미하는 것

실천에서 형성된 앎이 문서로 완전히 전달되지 않는다면, 문서만 가진 copilot은 작가의 reading을 완전히 재구성할 수 없습니다. 플러그인은 이 gap을 중심으로 설계됨:

- **Skill은 작가의 reading을 author할 수 없음.** 섹션 scaffold, reference 표면화, 인용 audit은 가능하나, provocation과 reflection 섹션은 작가의 저자권 필요.
- **per-layer instrument는 두 종류 층을 구분.** Documentable 층 (인용된 prior work, 작품 사실 기술, 전시 기록)은 AI가 input에서 재구성할 때 수렴 예상. Generative 층 (provocation, reflection, 상황적 해석)은 발산 예상.
- **Instrument는 AI의 창의성 능력을 test하지 않음.** specific corpus에서 documentable-vs-generative 분리가 감지 가능한지 test함.

## 이것이 의미하지 **않는** 것

이 플러그인의 입장은 AI가 인간이 가진 무언가를 **fundamental하게 결핍**한다는 것이 **아닙니다**. 플러그인이 인정하는 것:

- 작품을 만들지 않은 비평가도 실천이 없지만, legitimate하게 일관된 reading 가능
- 문서를 읽은 AI는 reader가 정당하게 할 수 있는 일을 할 수 있음 (해석 제시)
- 플러그인의 주장은 더 좁음: AI는 문서만으로 *작가가 author한 specific reading* 을 재현할 수 없음

이것은 재구성에 대한 측정 주장이지, 창의성에 대한 형이상학적 주장이 아님.

## 플러그인에서 나타나는 곳

- `art-inquiry full` 모드는 **Practice-Based Methodology Blueprint** 생성 — 작품 / 문서 / 글쓰기 / 수용을 PBR 규범에 따라 삼각측량 evidence로 명시 매핑
- `art-paper` skill은 provocation과 reflection 섹션이 작가-저자 표시되도록 강제
- `art-reviewer` Practitioner-Researcher 역할은 작가의 저자 position 보존 여부 확인
- 동반 paper는 §1과 §5에서 방법론의 PBR 이론 grounding 문서화
