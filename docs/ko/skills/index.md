# 스킬

플러그인에는 4개 skill이 포함되어 있습니다. 각 skill에는 자체 SKILL.md spec이 있고, 이 페이지는 사용자용 인덱스입니다.

| Skill | 언제 사용 | 주요 모드 |
|---|---|---|
| [art-inquiry](art-inquiry.md) | 작품과 질문은 있지만 초안이 없을 때 | `socratic`, `full`, `quick`, `review`, `lit-review`, `fact-check`, `systematic-review` |
| [art-paper](art-paper.md) | inquiry 자료가 있고 작성/수정하고 싶을 때 | `plan`, `full`, `outline-only`, `revision`, `revision-coach`, `abstract-only`, `lit-review`, `format-convert`, `citation-check`, `disclosure`, `artist-statement`, `work-doc` |
| [art-reviewer](art-reviewer.md) | 초안이 있고 심사위원 스타일 리뷰가 필요할 때 | `full`, `re-review`, `quick`, `realization-focus`, `guided`, `calibration` |
| [art-pipeline](art-pipeline.md) | 처음부터 끝까지 오케스트레이션 원할 때 | (위 모두 조정) |

## Slash command

각 모드는 명시적 `/art-*` slash command로도 호출할 수 있습니다 (frontmatter에 모델 고정 — 무거운 파이프라인/리뷰는 `opus`, 집중 단일 패스 모드는 `sonnet`). 산문으로 skill을 직접 불러도 됩니다; 아래는 단축 명령입니다.

| 명령 | 연결 대상 | 모델 |
|---|---|---|
| `/art-full` | art-pipeline — 전체 파이프라인 (inquiry → write → review → revise → finalize) | opus |
| `/art-reviewer` | art-reviewer — 전체 jury 리뷰 | opus |
| `/art-revision-coach` | art-paper — jury 코멘트 파싱 → Revision Roadmap + Response Letter | opus |
| `/art-plan` | art-paper — Socratic 섹션별 계획 | sonnet |
| `/art-outline` | art-paper — 상세 outline + evidence map | sonnet |
| `/art-revision` | art-paper — 수정 초안 + jury 응답 | sonnet |
| `/art-abstract` | art-paper — 초록 + 키워드 | sonnet |
| `/art-lit-review` | art-paper — 개념 계보 / precedent 작품 리뷰 | sonnet |
| `/art-artist-statement` | art-paper — 개념 중심 artist statement | sonnet |
| `/art-work-doc` | art-paper — 작품 문서화 (figure, 설치 기록) | sonnet |
| `/art-format-convert` | art-paper — acmart LaTeX / DOCX / PDF / Markdown 변환 | sonnet |
| `/art-citation-check` | art-paper — ACM Reference Format 인용 오류 보고 | sonnet |
| `/art-disclosure` | art-paper — 2-channel AI 사용 disclosure | sonnet |
| `/art-mark-read` / `/art-unmark-read` | art-paper — 인용 키의 human-read 신호 기록 / 취소 | sonnet |

독립 `/art-inquiry`, `/art-paper` 명령은 없습니다 — 이 둘은 산문으로 호출하거나(예: "input/ 자료로 내 art paper 작성해줘") `/art-full` 로 진입하세요.

## 라우팅 원칙

사용자가 명시적으로 `/art-*` slash command를 입력하면 그것이 우선. 아니면 플러그인이 상황을 분류 후 라우팅:

1. **명시적 명확한 의도** → 지정된 skill 직접 실행
2. **Cross-phase 자료, 명시 skill 없음** → 어떤 워크플로우인지 먼저 명확화 (애매한 채로 auto-routing 안 함)
3. **자료도 없이 애매함** → 명확화

자세한 사항은 `.claude/CLAUDE.md` § Routing Discipline 참조.
