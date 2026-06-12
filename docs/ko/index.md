# Art-Paper

**실천 기반 예술 연구 논문**을 위한 [Claude Code](https://www.anthropic.com/claude-code) 플러그인 모음입니다. 작품을 만들었고 그에 대한 학술 논문을 써야 한다면 — SIGGRAPH Asia Art Papers나 유사 venue를 대상으로 — 이 플러그인이 Claude Code에 그 작업을 도울 수 있는 skill을 추가합니다.

스코프는 특정 venue가 아니라 이 *장르*입니다 — 방법론과 무결성 점검은 venue 중립적입니다. 기본 reference target은 SIGGRAPH Asia Art Papers track의 관례(acmart, ACM Reference Format)이며, 그 출력은 acmart LaTeX를 받는 다른 venue에도 minor option 변경으로 적용됩니다.

## 이 플러그인이 하는 일

플러그인은 Claude Code에 작가-연구자가 **문서화된 작품에서 방어 가능한 학술 논문으로** 이동할 때 도움이 되는 일련의 skill을 제공합니다. 작품의 읽기(reading)를 저자가 작성하는 역할은 대체하지 않습니다. Skill 구성:

| Skill | 용도 |
|---|---|
| **art-inquiry** | 실천 기반 예술 연구의 선행 엔진 — 개념 정리, 위치 잡기, 방법론, 계보(lineage) |
| **art-paper** | 예술 논문 작성 엔진 — 초안, 수정, 초록, 포맷 변환 |
| **art-reviewer** | Art Papers 심사위원 시뮬레이션 (기본값은 SIGGRAPH Asia 관례) — Chair, Curator, Practitioner-Researcher, Art-Science Critic, Devil's Advocate |
| **art-pipeline** | end-to-end 오케스트레이터 — inquiry → 쓰기 → integrity → 리뷰 → 수정 → 마무리 |

## 왜 예술 논문 전용 플러그인인가

작품을 문서화해서 범용 AI 글쓰기 도구에 넘기면 일관된 논문이 만들어지지만 — 그 논문이 advance하는 reading은 AI의 reading이지 작가의 것이 아닙니다. 만드는 행위에서 나온 문제 의식, 성찰, 상황적 해석은 작가에게서 와야 합니다. 그것을 documentable 사실과 구분하지 못하는 도구는 작가의 reading 대신 자기 것을 채워 넣습니다.

이 플러그인은 그 gap을 위해 설계되었습니다. 각 skill은 **작가의 저자 작업을 돕되 저자권을 주장하지 않도록** bounded되어 있습니다. 이론적 근거 (Schön, Polanyi, Borgdorff, Candy)는 [개념 → 실천 기반 연구](concepts/practice-based-research.md)에서 확인할 수 있습니다.

## 빠른 시작

설치와 첫 실행은 [시작하기](getting-started.md) 참조. 한 작품에 대한 전체 플러그인 walkthrough — input pack, firewalled 재구성, instrumentation — 는 [Cutting Kim 사례 연구](examples/cutting-kim-case.md) 참조.

## 상태

- **Suite 버전**: 0.1.1 (`academic-research-skills` v3.9.4.2에서 fork)
- **라이선스**: CC-BY-NC 4.0
- **최종 업데이트**: 2026-06-13

## 이 플러그인이 하지 **않는** 일

- 작품의 reading 저자권을 **대체하지 않음.** Art-paper skill은 생성적 층의 내용을 명시적으로 저자의 책임으로 표시.
- 작품 자체를 **평가하지 않음.** 예술 품질 판정 없음.
- 다른 학술 장르로 **자동 transfer되지 않음.** Skill은 실천 기반 예술 논문 작성에 bounded.
