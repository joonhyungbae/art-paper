# Worked example — *Cutting Kim*

이 walkthrough는 플러그인의 reconstruction benchmark를 실제 실천 기반 예술 논문에 적용합니다: **Bae, Choi, Nam, *Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts*, SIGGRAPH Asia 2025 Art Papers.**

출판된 논문은 **gold**로 숨겨 둔 채, 플러그인에는 사실 자료만 담은 **input pack**만 줍니다. 플러그인이 논문을 재구성하면, instrumentation이 재구성과 gold를 레이어별로 비교해 보고합니다.

> **출처 안내.** *Cutting Kim*은 Joonhyung Bae, Eunjin Choi, Juhan Nam (KAIST)의 작품입니다. 저자들이 이 worked example용으로 자신의 논문을 직접 제공했으므로 제3자 저작권 문제는 없습니다. 아래 재구성은 benchmark 목적의 플러그인 출력이며, 경쟁 출판물이 아닙니다.

---

## Step 1 — 플러그인이 받는 input

작가-연구자가 `input/` 디렉토리에 사실 자료를 모아 플러그인에 줍니다. **논문의 framing, thesis, provocation, 개념 어휘, 참여자 인터뷰 결과, reflection은 모두 benchmark를 위해 보류(withhold).**

### `concept_memo.md` (중립 주제 seed)

```
An interactive VR experience for the Oculus Quest 2 in which the player's own
voice is the controller: loudness and pitch, captured through the headset
microphone, drive a game where the player wields a voice-generated "sonic sword"
to destroy food-themed enemy characters. The work was shown in public exhibition
settings (workshop, conference, festival).
```

(한 문단짜리 메모 전체 — 해석적 주장은 없습니다.)

### `documentation.md` (사실 기반 작품 기술)

발췌:

> 음성 입력은 Oculus Quest 2 마이크로 캡처. **Loudness:** 오디오 신호의 RMS로 음성 진폭을 측정; 공격력은 입력 볼륨(dB)에 선형 비례. **Pitch:** YIN 알고리즘으로 F0를 검출해 가장 가까운 pitch class와 height로 매핑. Pitch class → hue, pitch height → brightness (Lab color space, Delta E*2000 보정).

여기에 데미지/스코어링 시스템(기본 데미지 + pitch 일치 시 최대 4.5배 보너스), 3단계 게임 흐름(Story / Tutorial / Gameplay), HUD가 더해집니다. 해석적 framing은 없습니다.

### `exhibition_record.md` (사실 venue 데이터)

4회 전시를 venue, 행사 유형, 날짜만 표로: Daejeon Museum of Art 워크숍(2022.10), SFactory에서의 The Infinite CT 컨퍼런스(2022.12), HCI Korea 2023(2023.02), Asia Culture Center의 ACT Festival 2023(2023.11).

### `bibliography.bib`

인용된 precedent 작품 + 이론 28개. Input audit가 전이 가능한 사실 자료로 검증했습니다 (voice interaction game, pitch 검출, pitch-color synesthesia, 실천 기반 연구 방법 등).

### `LEAKAGE_AUDIT.md`

Auditor가 정리한 **input에서 보류된 항목**:

- **Thesis** — 음성을 "playful transgression"의 매체로 보는 관점; 상호작용 예술을 "rehearsal space"로 보는 관점; 기술을 통제가 아니라 음성의 해방에 쓴다는 주장.
- **중심 역설** — "publicly private" 행위: 헤드셋이 사적 공간감을 주는 동시에 신체와 목소리를 공적 spectacle로 만든다는 주장.
- **Framing 어휘** — "technologies of transgression", "permission structures", "beautiful transgression", carnivalesque / "digital carnival".
- **Provocation** — "기술이 우리에게 시끄러울 것을 허락하면 어떻게 되는가?"
- **참여자 분석** — N=5 페스티벌 인터뷰 결과(당혹감, 카타르시스, productive tension).
- **Reflection / 결론 입장** — 신체를 "liminal object"로 보는 관점, "우리 자신 안에 새 permission structure를 짓는다"는 논지.

Audit는 **경계선 항목 하나를 정직하게 표시**합니다. bibliography에 transgressive-play(`aarseth2014fought`, `jorgensen2019transgression`) 및 carnivalesque(`bakhtin2020rabelais`) 참고문헌이 들어 있어 제목만으로도 개념 영역을 암시한다는 점입니다. 인용 계보는 전이 가능한 자료로 다루는 게 일관되지만, 이 pack에서 가장 강한 leakage 경로이므로 generative-layer margin은 이 표시와 함께 읽어야 합니다.

---

## Step 2 — 플러그인 실행

사용자가 호출:

```
/art-paper full input/ 자료로 paper 재구성해
```

플러그인이 input pack을 읽고, firewall 원칙(보류된 내용은 작성 불가)을 적용해 `reconstruction/paper.md`를 만듭니다. 여기서는 input pack만 보고 gold paper는 **전혀** 보지 않은 firewalled subagent로 실행해, 약 3,200단어의 Pattern-1 art paper를 생성했습니다.

---

## Step 3 — 플러그인이 만든 것

재구성된 논문은 자체 제목, 초록, 섹션 구조를 가집니다. 주목할 점은, 플러그인이 **저자의 보류된 provocation을 재현하지 않고** input만으로 도달 가능한 *다른* reading을 생성했다는 사실입니다.

### 재구성된 제목

> "Cutting Kim: The Untrained Voice as an Embodied Game Controller"

(Gold 제목과 비교: *"Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts"*.)

### 재구성된 Conceptual Framework (발췌)

> 이 작품의 가장 결정적인 디자인 결정은 플레이어에게 노래를 요구하지 않는다는 점이다. 데미지 모델은 *어떤* 발성에도 기본 효과를 부여하고, 적의 목표 pitch를 맞춘 플레이어에게만 배수 보너스를 예약한다. 우리 framing에서 시스템은 음성을 performance가 아니라 effort로 다룬다 … 우리는 이를 작품의 주장으로 읽는다: 인간의 음성은 훈련된 음악적 상태뿐 아니라 평범하고 불완전하며 노력이 담긴 상태 *그대로* 디자인할 가치가 있다.

문서만으로 만든 플러그인의 reading은 *"훈련받지 않은 음성을 정당한 일급 control surface로"*입니다. 저자의 실제 reading(playful transgression, "publicly private" 역설, carnivalesque)은 **나타나지 않습니다**. 플러그인은 일관된 해석을 제시하지만, *다른* 해석입니다. 흥미로운 점은, bibliography가 transgression 어휘를 암시했음에도 재구성이 그 어휘를 채택하지 않았다는 사실입니다.

### 재구성된 Reflection (발췌)

> … 우리는 그 참여자들이 무엇을 느끼거나 말했는지 **의도적으로 보고하지 않는다**: 그 해석적 분석은 우리가 다루는 증거 밖이며, reception을 부풀리는 것(예컨대 "관객이 기뻐했다")은 정직하지 않을 것이다.

재구성이 받지 못한 참여자 수용(reception) 결과를 *명시적으로 거부*합니다 — 방법론이 의도한 firewall 동작 그대로입니다.

---

## Step 4 — Instrumentation 보고

Instrumentation script가 재구성과 gold를 레이어별로 비교한 결과:

| Metric | 값 | 해석 |
|---|---|---|
| **Transferable 레이어 유사도 (T)** | 0.2568 | 사실 콘텐츠(작품, realization)가 gold와 수렴 |
| **Generative 레이어 유사도 (G)** | 0.1261 | Conceptual framework + reflection은 gold와 발산 |
| **T − G margin** | **+0.1307** | 방향성 reading 지지 (예상대로 T > G) |
| **Contamination probe (8-gram)** | 0.0028 | `ok` (0.10 high-warning 임계값 한참 아래) |
| **`thesis_supported`** | `True` | transferable 수렴 / generative 발산 ordering 유지 |
| **Citation set** | precision 1.0, recall 0.32 | gold precedent 28개 중 9개 surfaced; 인용한 모든 항목이 실제 gold precedent |
| **Structural coverage** | 1.0 | Pattern-1 레이어 전부 존재 |

레이어별 lexical 유사도(서술용): realization (transferable) `0.21`이 가장 정렬도가 높은 콘텐츠 레이어이고, conceptual_framework `0.13`, reflection_discussion `0.12`(둘 다 generative)이 그보다 낮습니다.

선택적인 semantic embedding 패스(`--embed`, `BAAI/bge-small-en-v1.5`): chunk-alignment 코사인은 `transferable 0.776 / generative 0.780`으로 거의 동일합니다. 이는 방법론이 경고하는 **주제 포화(topic-saturation)** 현상입니다 — 한 작품 안에서는 모든 레이어가 ~0.9 근처로 임베드되기 때문에 blob 코사인은 변별력이 거의 없습니다. 변별의 주축은 lexical n-gram 측정이며, 임베딩은 투명성을 위해 함께 보고할 뿐 "T ≈ G semantically"로 읽어서는 안 됩니다.

**해석.** 플러그인은 사실 층을 합리적으로 재구성하고(T ≈ 0.26), generative 층은 의미 있게 발산합니다(G ≈ 0.13). 8-gram contamination probe는 memorisation을 발견하지 못했습니다. 따라서 이 재구성은 **암기된 내용의 재현이 아니라 input만으로의 진정한 추론**이며, generative 층의 발산은 저자의 보류된 reading이 문서만으로는 만들어지지 않았음을 반영합니다.

> **정직한 주석 둘.** (1) *Gold heading normalization.* 이 논문은 개념 framing을 Introduction 안에 접고 논의 섹션을 고유 제목으로 달기 때문에, gold의 섹션 헤딩을 각 섹션이 수행하는 Pattern-1 레이어에 맞춰 정규화했습니다 — 다른 모든 benchmark case에 동일하게 적용된 구조 변환이며, 섹션 *내용*은 변경하지 않았습니다. (2) *Anchoring rate.* Script가 2개의 "claim"을 unanchored로 표시했지만 둘 다 false positive입니다 — 하나는 열거자("The first is how much design work…"), 다른 하나는 수용 보고를 *명시적으로 거부*하는 문장입니다. 재구성에 실제 reception inflation은 없습니다.

---

## Step 5 — Clean-control variant (더 엄격한 테스트)

더 강한 테스트는 표준 input pack(gold 논문을 보면서 추출했기 때문에 논문 기반 기술 문체를 일부 안고 있음)이 아니라, **minimal-footprint input**으로 재구성합니다 — 페스티벌 프로그램과 일반적인 미디어아트 상식만으로 정리 가능한 자료입니다. 표준 pack의 `documentation.md`는 RMS, YIN, Lab/Delta E*2000, "최대 4.5배" 배수, "3단계" 게임 분류 같은 세부를 명시하지만, clean-control은 이 모두를 뺍니다(사실이긴 해도 표준 pack에 들어간 경로가 gold의 문장이기 때문). bibliography도 28개에서 15개로 줄여, gold가 선택한 transgressive-play / carnivalesque 계보를 암시하는 참고문헌을 드랍합니다.

이 더 빈약한 pack에 대해 새로운 firewalled 재구성을 한 번 더 실행했습니다 — 역시 gold도, 앞서의 표준 재구성도 보지 않은 상태에서.

Clean-control instrumentation 보고:

| Metric | Standard | Clean control |
|---|---|---|
| T (transferable, lexical) | 0.2568 | 0.1047 |
| G (generative, lexical) | 0.1261 | 0.1236 |
| **T − G margin** | **+0.1307** | **−0.0189** |
| `thesis_supported` | True | **False** |
| Contamination (8-gram) | 0.0028 | 0.0 |
| Citation precision / recall | 1.0 / 0.32 | 1.0 / 0.54 |
| Semantic align (T / G) | 0.776 / 0.780 | 0.760 / 0.800 |

**해석.** 가장 깨끗한 input(논문 기반 기술 문체 제거, 계보 암시 참고문헌 제거)에서 방향성 `T > G` reading은 **유지되지 않습니다** — margin이 +0.13에서 살짝 음수로 무너집니다. 이는 표준 margin의 상당 부분이 **input 추출 단계의 artifact**였다는 점과 일치합니다: 표준 pack의 `documentation.md`가 RMS / YIN / Delta E*2000 / 배수 같은 표현을 gold에서 그대로 옮겨 적었기 때문에 transferable jaccard가 끌어올려졌고, 그 문체를 빼면 transferable 층이 generative 층과 비슷한 lexical 바닥으로 내려앉습니다.

Contamination probe는 두 실행 모두 0에 머뭅니다 — 두 경우 모두 플러그인이 gold를 외우지 않았습니다. 이 결과가 보여주는 것은 방법론의 **도달 범위와 동시에 정직한 한계**입니다: per-layer instrument는 input pack 구성에 민감할 만큼 예민하고, clean-control은 그 예민함을 감추지 않고 드러냅니다. (Clean-control 재구성이 도달한 자체 reading — *"voice as blade — HMD가 장면을 사적으로 만드는 동안 음성은 플레이어를 다시 공적으로 만든다"* — 역시 일관되며, gold의 보류된 reading과 또 다릅니다; firewall은 여전히 작동합니다.)

---

## Step 6 — 이 예시가 보여주는 것

구체적으로:

1. **Firewall이 작동한다.** 플러그인은 provocation/reflection 자료 없이 자체 reading을 만들었습니다 — 저자의 것이 아닙니다. 표준과 clean-control 두 재구성 모두 서로 다른 일관된 reading을 만들었고, 어느 쪽도 gold의 "playful transgression" thesis를 재현하지 않았습니다.
2. **Per-layer instrument가 gap을 감지한다 (input이 뒷받침할 때).** 표준 pack에서 T = 0.26 / G = 0.13, margin +0.13.
3. **Inversion rule이 통과한다.** 두 실행 모두 warning 임계값 위의 contamination이 없었고, 플러그인은 외우지 않았습니다.
4. **Clean-control이 정직성의 경계를 짓는다.** 더 엄격한 input 규율에서 표준 margin이 거의 0으로 무너지며, 그 margin의 상당 부분이 input의 논문 기반 문체로부터 왔다는 점을 드러냅니다. 방법론은 이를 감추는 대신 보고합니다.
5. **저자의 reading은 저자의 것으로 보존된다.** 두 재구성 모두 *다른* 일관된 reading을 만들었고(게임 컨트롤러로서의 untrained voice; 칼날과 노출된 신체로서의 voice), 원래의 "playful transgression" reading은 유일하게 저자의 것으로 남았습니다.

이것이 방법론이 약속하는 것 — 측정이지 평결이 아닙니다.

---

## 이 예시 재현

`sa25-ck`와 `sa25-ck-clean`의 전체 input pack, 재구성, instrumentation은 동반 paper의 reproducibility mirror — 각각 `eval/pilot/sa25-ck/`와 `eval/pilot/sa25-ck-clean/` — 에 있습니다(clean-control은 `gold/`를 표준 pilot에 심볼릭 링크합니다 — gold 논문은 동일하니까요). Instrumentation script(기본 stdlib-only; `--embed`로 sentence embedding 옵션)는 `eval/instrumentation.py`입니다.

```bash
python3 eval/instrumentation.py eval/pilot/sa25-ck --json
python3 eval/instrumentation.py eval/pilot/sa25-ck-clean --json
```

출력은 Step 4와 Step 5의 표를 재현합니다.
