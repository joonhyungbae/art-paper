# 예시

플러그인이 실제 case에 적용된 worked example입니다. 각 예시는 입력 자료에서 최종 artifact까지 완전한 파이프라인과 플러그인이 실제 생성한 출력을 보여줍니다.

## 가능한 walkthrough

| Case | 무엇을 보여주는가 |
|---|---|
| [Cutting Kim — Bae, Choi, Nam (2025) VR 음성 상호작용 작품](cutting-kim-case.md) | 저자들이 직접 제공한 SIGGRAPH Asia 2025 Art Paper에 대한 전체 reconstruction-benchmark walkthrough: input pack, firewalled 재구성, instrumentation 결과, 그리고 minimal-footprint clean-control variant |

## 예시 생성 방식

모든 예시는 이미 출판된 실천 기반 예술 paper의 실제 input 자료에 대해 actual 플러그인 (Claude Code의 `art-paper` skill, Anthropic API `claude-sonnet-4-5` 모델)을 실행해서 만들어졌습니다. Held-out gold paper들은 원 출판사 기준으로 인용되며, 재구성은 firewall된 input pack에서 이 플러그인이 만든 출력입니다.

Instrumentation 숫자 (T, G, contamination probe, structural coverage)는 동반 paper의 reproducibility mirror에 있는 `eval/instrumentation.py` script가 계산합니다. Script는 stdlib-only (네트워크 없음, 모델 의존성 없음); 누구나 input/reconstruction/gold trio에서 재실행 가능.
