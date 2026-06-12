# 자주 묻는 질문

## 이름은 어디서 왔나?

이 플러그인은 **Art-Paper** 입니다. upstream [`academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) 에서 fork되어 실천 기반 예술 논문 작성이라는 하나의 scope으로 특화됐습니다. (로컬 작업 디렉토리에는 fork 시기의 폴더명이 남아 있을 수 있으나, 플러그인과 저장소는 *art-paper* 입니다.)

## Provocation은 왜 작가가 작성해야 하나? AI가 그냥 쓰면 안 되나?

플러그인은 기록된 사실에서 provocation 생성 가능 — 작가가 안 주면 그렇게 함. 그러나 생성한 provocation은 **플러그인의** reading이지 작가의 것이 아님. 실천 기반 paper에서 작가의 reading이 contribution; 다른 reading으로 대체하면 출판되는 내용 자체가 바뀜. 플러그인은 provocation을 scaffold할 수 있으나, 유지 여부는 작가 책임.

## 이 플러그인이 예술 논문 외 다른 장르에도 작동하나?

실천 기반 예술 논문 작성에 bounded. Skill의 프롬프트, reference, integrity check가 이 scope에 tuned. 다른 장르에서 출력 produce 가능하나, 플러그인 설계에 의해 warranted되지 않음 — 종속변수 (documentable/generative split)가 실천 기반 연구 밖에서 이론적 grounding 상실.

일반 학술 글쓰기 플러그인 원하면 upstream [`academic-research-skills`](https://github.com/Imbad0202/academic-research-skills)가 더 가까움.

## 플러그인 인용 방법?

플러그인을 software release로 인용:

```bibtex
@software{art_paper_2026,
  author       = {Bae, Joonhyung},
  title        = {Art-Paper: A Claude Code plugin suite for practice-based art research papers},
  year         = {2026},
  version      = {0.1.1},
  url          = {https://github.com/joonhyungbae/art-paper},
  note         = {CC-BY-NC 4.0}
}
```

## SIGGRAPH Asia 외 다른 venue에 쓸 수 있나?

네 — 플러그인 스코프는 특정 venue가 아니라 *장르*(실천 기반 예술 연구 논문)입니다. 기본값은 reference로서 SIGGRAPH Asia Art Papers 관례 (acmart class `sigconf` option, ACM Reference Format)를 target하며, SIGGRAPH (메인 conference) Art Papers도 비슷한 관례입니다. 방법론과 무결성 점검은 venue 중립적이고, `format-convert` 모드는 해당 class를 받는 다른 venue도 minor option 변경으로 받아주는 acmart LaTeX를 생성합니다. Target하는 venue의 당해년 CFP는 항상 확인하세요; acmart를 쓰지 않는 venue라면 LaTeX 출력을 camera-ready가 아니라 출발점으로 취급하세요.

## 플러그인이 내 데이터로 모델 학습시키나?

플러그인은 Anthropic Claude API 위에서 동작. 사용자 입력/출력이 학습에 사용되는지는 Anthropic API 계약과 계정 설정에 따름. 플러그인 자체는 Claude Code 클라이언트의 정상 작동 외에 사용자 입력을 기록/보관/전송하지 않음.

## 버그 신고나 기능 요청은?

[리포지토리](https://github.com/joonhyungbae/art-paper/issues) 의 GitHub Issues. Skill (`art-inquiry` / `art-paper` / `art-reviewer` / `art-pipeline`), 모드, input 자료의 일반 형태 명시 (실제 작품이나 paper 공유는 원할 때만).

## 라이선스?

플러그인은 **CC-BY-NC 4.0** 라이선스. Attribution 하에 비상업적 목적으로 공유와 adapt 가능. 상업적 사용은 별도 허가 필요.
