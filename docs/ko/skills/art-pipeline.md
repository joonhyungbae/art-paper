# art-pipeline

**End-to-end 오케스트레이터.** `art-inquiry` → `art-paper` → integrity check → `art-reviewer` → `art-paper revision` → final integrity → `art-paper format-convert`를 조정.

## 언제 사용

- 완성된 작품이 있고 제출 가능한 paper를 만들고 싶을 때
- 각 skill을 수동 호출 없이 full discipline (integrity gate, re-review, format conversion) 원할 때
- 전체 파이프라인 상태의 Material Passport trail 원할 때

## Full state machine

```
art-inquiry (socratic | full)
  → art-paper (plan | full)
    → integrity check (Stage 2.5: 인용 + 실현 주장)
      → art-reviewer (full | guided jury)
        → art-paper (revision)
          → art-reviewer (re-review, 최대 2 loop)
            → final integrity check (Stage 4.5)
              → art-paper (format-convert → acmart LaTeX → PDF)
                → Process Summary + AI Self-Reflection Report
```

## Mandatory 체크포인트

파이프라인은 진행 전 사용자 확인 시점에서 일시정지:

| Stage | Type | 확인 사항 |
|---|---|---|
| Inquiry 후 | FULL | Concept/methodology/bibliography 승인 |
| 초안 후 | MANDATORY | Integrity check 평결 (인용 + 실현 주장) |
| 리뷰 후 | MANDATORY | Editorial decision (accept/minor/major/reject) |
| 수정 후 | FULL | Re-review 또는 final integrity |
| 마무리 전 | MANDATORY | Format-convert와 final output 승인 |

`art-pipeline` v0.1.0 관례에 따라, MANDATORY 체크포인트는 이전 stage 결과가 깨끗해도 auto-skip 안 됨.

## 입력

주제 seed와 (선택) 기존 자료. 파이프라인이 보유 자료를 감지해서 진입 stage 선택:

- **자료 없음** → Stage 1 (art-inquiry)
- **Inquiry artifact** → Stage 2 (art-paper)
- **Draft paper** → Stage 2.5 (integrity check)
- **검증된 draft** → Stage 3 (art-reviewer)
- **리뷰어 feedback** → Stage 4 (revision)
- **Final draft** → Stage 5 (format-convert)

## 출력

- 각 stage의 모든 artifact (per-stage 산출물)
- Material Passport (state record) — 각 체크포인트에서 결정된 사항 추적
- 최종 acmart PDF
- 인간-AI 협업 history를 문서화한 Process Summary
- 플러그인이 무엇을 author했고 안 했는지에 대한 AI Self-Reflection Report

## 페어링

- 4개 skill 전부 (이것이 오케스트레이터)

## 주의

- Full 파이프라인은 개별 skill 실행보다 오래 걸림; 속도보다 discipline이 중요할 때 사용
- 각 수정 loop는 API 호출 1라운드 소비; budget 고려
- Re-review loop는 기본 2회 cap (무한 수정 방지)
- `format-convert`는 로컬에 LaTeX 의존성 설치 필요
