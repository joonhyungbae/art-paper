# 시작하기

## 사전 준비

- **[Claude Code](https://www.anthropic.com/claude-code)** 설치 및 인증 완료
- **본인이 만든 문서화된 작품** (본인의 실천). 최소 다음 자료가 있어야 합니다:
    - 작품의 형태와 작동 메커니즘에 대한 사실 기반 기술
    - 전시 기록 (장소, 날짜, 배치) — 있으면
    - 사진이나 문서화 영상 — 있으면
    - 관련 있다고 판단되는 precedent 작품과 이론에 대한 짧은 참고문헌

## 설치

**권장 — Claude Code 플러그인 마켓플레이스:**

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

Claude Code를 열어 `/art-` slash command 자동완성으로 skill이 표시되는지 확인.

**대안 — 수동 clone (플러그인 자체를 해킹할 때):**

```bash
git clone https://github.com/joonhyungbae/art-paper.git
cd art-paper
```

`docs/SETUP.md`에 따라 디렉토리를 Claude Code 플러그인 경로로 등록.

## 첫 실행 — 세 가지 진입점

프로젝트 진행 단계에 따라 세 가지 일반적인 진입점이 있습니다.

### 진입점 A — "완성된 작품이 있고 논문을 쓰고 싶다"

작업 디렉토리에 `input/` 폴더를 만들고 자료를 정리하세요. [Cutting Kim 사례](examples/cutting-kim-case.md) 의 input pack 구성을 그대로 본떠도 됩니다:

```
my-paper/
├── input/
│   ├── concept_memo.md       # 한 문단, 사실 기반 주제 seed (해석적 주장 없음)
│   ├── documentation.md      # 작품의 형태 + 작동 메커니즘 (사실 기술)
│   ├── exhibition_record.md  # venue, 날짜, 배치
│   ├── bibliography.bib      # precedent 작품 + 이론 (BibTeX)
│   └── figures/              # 사진, 문서화 영상 (선택)
└── (provocation + reflection은 파이프라인이 작가에게 묻습니다)
```

`concept_memo.md` 예시 (Cutting Kim 사례에서):

```markdown
An interactive VR experience for the Oculus Quest 2 in which the player's own
voice is the controller: loudness and pitch, captured through the headset
microphone, drive a game where the player wields a voice-generated "sonic sword"
to destroy food-themed enemy characters. The work was shown in public exhibition
settings (workshop, conference, festival).
```

그리고 호출:

```
/art-pipeline input/ 의 자료로 [작품명] 에 대한 논문을 작성해줘.
대상 venue: SIGGRAPH Asia 2026 Art Papers track (대상 venue로 교체).
```

파이프라인 오케스트레이터가 다음을 순차 dispatch:

1. **art-inquiry** — 개념, 위치, 방법론 정리
2. **art-paper** — 논문 초안 작성
3. **art-reviewer** — 심사위원 시뮬레이션
4. **art-paper (revision)** — 리뷰에 따라 수정
5. **최종 integrity check** — 인용 및 실현 주장 audit
6. **art-paper (format-convert)** — camera-ready LaTeX 생성 (`acmart` class)

### 진입점 B — "초안이 있고 집중 리뷰만 원한다"

초안 파일과 (있다면) 작품 문서화를 함께 준비:

```
my-paper/
├── draft/
│   ├── paper.tex             # 또는 paper.md / paper.docx
│   └── references.bib
└── docs/                     # 선택 — 작품 사진/영상/전시 기록
    ├── figures/
    └── exhibition_record.md
```

호출:

```
/art-reviewer draft/paper.tex 를 대상 Art Papers 기준으로
(기본값 SIGGRAPH Asia) 5-perspective jury 리뷰해줘. 작품 문서화는 docs/ 참고.
```

5-perspective 심사위원 보고서 (Chair, Curator, Practitioner-Researcher, Art-Science Critic, Devil's Advocate) + Editorial Decision Letter + Revision Roadmap 반환.

### 진입점 C — "아이디어만 있고 아직 논문이 아니다"

논문 자료는 아직 없어도 됩니다. 최소한의 seed만 준비:

```
my-paper/
├── concept_memo.md           # 한 문단 — 작품/주제 seed
├── documentation.md          # 선택 — 작품 또는 prototype 사실 기술
└── references/               # 선택 — 관련 작품/이론 메모
    └── notes.md
```

provocation이 아직 명확하지 않다면 Socratic 모드를 명시:

```
/art-inquiry concept_memo.md 의 주제로 socratic 모드로 시작해줘.
아직 provocation이 명확하지 않고, 어떤 질문을 던지는 작품인지
함께 정리하고 싶어.
```

Concept & Provocation Brief, Practice-Based Methodology Blueprint, precedent 작품 및 이론 Annotated Bibliography, Synthesis Report 생성. art-paper skill이 이를 consume해서 manuscript를 작성.

## 플러그인이 사용자에게 요청하는 것

플러그인은 **firewall 원칙** 으로 작동합니다: 문서만으로는 작품의 reading을 작성할 수 없음. 그래서 작가만 제공할 수 있는 부분 — 일반적으로 **provocation** (작품이 무엇을 주장하거나 거부하는지 한 문단으로 진술)과 **reflection** (실천이 그 질문에 대해 무엇을 가르쳐주었는지) — 을 작가에게 요청합니다. 이것이 방법론이 documentable material과 구분하는 *생성적 층* 의 자료입니다.

자신의 provocation을 아직 모른다면, `full` 모드 대신 [Socratic 모드](skills/art-inquiry.md#socratic-mode) 로 inquiry를 실행하세요.

## 출력 형식

- **Manuscript**: `acmart` document class (`sigconf` option) 대상 LaTeX → PDF
- **Bibliography**: 기본 ACM Reference Format (acmart 연동); 비-ACM venue용 대체 포맷 — APA 7.0, Chicago, MLA 9, IEEE, Vancouver
- **Tables/figures**: ACM convention에 따라 별도 파일
- **AI-usage disclosure**: SIGGRAPH Asia / ACM 정책에 따라 자동 생성 (작품을 만드는 AI vs. 논문을 쓰는 AI, 2-channel)

## 다음 단계

- [Cutting Kim 사례 연구](examples/cutting-kim-case.md) — input pack → firewalled 재구성 → instrumentation 전체 walkthrough
- [개별 skill 문서](skills/index.md) 읽기
- 플러그인 설계의 근거가 되는 [방법론 개념](concepts/index.md) 이해
