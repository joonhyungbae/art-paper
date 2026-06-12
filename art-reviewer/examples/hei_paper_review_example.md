# Example: Practice-Based Art Paper Full Review

This example demonstrates the complete Phase 0-2 workflow of `art-reviewer`, simulating the SIGGRAPH Asia Art Papers jury reviewing a practice-based art paper titled "Tidal Drift: A Generative Installation That Composts Coastal Sensor Data Into Living Soundscapes."

The work is the **primary evidence**. The jury (Chair + Practitioner-Researcher + Curator + Critic) assesses artistic merit, conceptual contribution, documentation/realization rigor, and contribution to discourse — not statistical validity.

---

## Simulated Paper Abstract

> **Title**: Tidal Drift: A Generative Installation That Composts Coastal Sensor Data Into Living Soundscapes
>
> **Abstract**: *Tidal Drift* is a room-scale generative sound installation that ingests live tide-gauge, salinity, and hydrophone data from a single estuary and "composts" it — through a custom layered-decay synthesis engine — into a slowly mutating 8-channel soundscape that never repeats. The work was developed over an 18-month studio practice and exhibited at the 2024 Estuary Futures festival (Tainan) for six weeks. This paper frames the making as practice-based research: I argue that treating environmental data as compostable material (rather than as something to be "visualized" or "sonified" transparently) opens a third position between data-art legibility and pure abstraction. I document the iterative development of the decay engine across three studio failures, position the work against precedent data-driven sound art, and reflect on how visitors lingered. The contribution is the *compost* model of data-to-form translation as a practice-based concept, demonstrated through the realized work.
>
> **Keywords**: generative sound art, environmental data, practice-based research, installation, data sonification
>
> **Full text approximately 6,500 words, 28 references cited (ACM Reference Format); documentation: 9 install photos, 1 video walkthrough (4 min), system signal-flow diagram, decay-engine pseudocode**

---

## Phase 0: Field Analysis & Persona Configuration

### Field Analysis Report

#### Work / Paper Basic Information
- **Title**: Tidal Drift: A Generative Installation That Composts Coastal Sensor Data Into Living Soundscapes
- **Abstract length**: Approximately 190 words
- **Full text length**: Approximately 6,500 words
- **Number of references**: 28 (ACM Reference Format)
- **Documentation present**: 9 install photos, 4-min video walkthrough, signal-flow diagram, decay-engine pseudocode

#### Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Art Subfield / Medium | Generative sound art / data-driven installation |
| Secondary Art+Tech Areas | Environmental media, real-time audio synthesis, interaction (ambient/non-interactive) |
| Mode of Inquiry | Practice-based (Pattern 1) — the artwork is the contribution |
| Realization Approach | Custom layered-decay synthesis engine, 8-channel spatialization, live sensor feeds |
| Exhibition / Venue Context & Ambition | One six-week festival exhibition (Estuary Futures 2024, Tainan); SIGGRAPH Asia Art Papers-level ambition. *Verify expectations against current Call for Art Papers.* |
| Paper / Work Maturity | Revised draft — structure and documentation in place; conceptual contribution stated but precedence positioning thin |

#### Suggested Venues / Programs (Top 3)
1. **SIGGRAPH Asia Art Papers** — practice-based generative work with a clear conceptual move; fits the art-and-technology discourse. *Verify against current CFP.*
2. **Leonardo (MIT Press)** — accepts artist-authored practice-based papers with conceptual framing
3. **ISEA / NIME Art track** — strong fit for generative sound art and environmental-media works

#### Reviewer Configuration Cards

---

### Reviewer Configuration Card #1

**Role**: Jury Chair (EIC)
**Identity Description**: SIGGRAPH Asia Art Papers Chair with a generative- and environmental-art background; has chaired prior art-and-technology programs and attends to whether a work belongs in the program and whether the audience would find it significant.
**Review Focus**:
  1. Artistic significance and fit — does *Tidal Drift* contribute something the art+tech audience would find new?
  2. Originality of the "compost" concept relative to the crowded field of environmental data art
  3. Overall coherence between the stated concept, the realized work, and the documentation
**Will particularly care about**: "Whether the 'compost' framing is a load-bearing concept or a re-label for ordinary sonification (glossary §7)."
**Possible blind spots**: May not be deeply familiar with the specific estuary-data ecology the work draws on.

---

### Reviewer Configuration Card #2

**Role**: Reviewer 1 — Practitioner-Researcher (methodology slot, art sense)
**Identity Description**: Practice-based artist-researcher working in real-time generative audio systems, faculty at a media-arts program; has shown 8-channel installation work and attends closely to whether the making process is documented as research.
**Review Focus**:
  1. Realization rigor — is the layered-decay engine described specifically enough to be plausible, or asserted?
  2. Process integrity — are the "three studio failures" actually documented as research, with what changed and why?
  3. Capability-claim anchoring — "never repeats," "live data," "composts" — are these anchored in the system/pseudocode or over-claimed?
**Will particularly care about**: "Whether 'generative' and 'never repeats' are precise (glossary §3) or marketing language; whether the video documents the *work* or stands in for it (glossary §2)."
**Possible blind spots**: May under-weight the curatorial/discourse positioning that is Reviewer 2's remit.

---

### Reviewer Configuration Card #3

**Role**: Reviewer 2 — Curator / Exhibition Expert (domain slot, art sense)
**Identity Description**: Curator of media-art and environmental-art exhibitions, deeply familiar with the data-sonification and eco-media lineage; has organized programs on data-as-material and attends to precedent works and exhibition framing.
**Review Focus**:
  1. Conceptual lineage — is the work positioned against the right precedent data-driven sound art and eco-media works?
  2. Novelty / precedence — does the "third position between legibility and abstraction" claim hold against existing work, and is it citable?
  3. Whether the *concept* (not just theme + technique) is articulated and contributes to discourse
**Will particularly care about**: "Whether the 'first to compost data' framing is an unsupported precedence claim (evidence model §4) and whether key precedents (e.g., established eco-sound-art practitioners) are cited in ACM format with a real venue+date locator."
**Possible blind spots**: May focus on lineage at the expense of the technical realization R1 covers.

---

### Reviewer Configuration Card #4

**Role**: Reviewer 3 — Art-Science / Media-Art Critic (perspective slot, art sense)
**Identity Description**: Media-art critic and environmental-humanities theorist; approaches from cultural and ethical angles the practitioner and curator may not, with research on the politics of representing ecological data as aesthetic experience.
**Review Focus**:
  1. Cross-disciplinary significance — what does the "compost" model say to environmental media and the broader field?
  2. Representational ethics — what is at stake in turning a specific imperiled estuary's data into ambient pleasure?
  3. The "so what for the field?" question — does the work advance discourse or aestheticize crisis?
**Will particularly care about**: "Whether reception is inflated ('visitors lingered') without an observable anchor (evidence model §4 / glossary §8), and whether the work reflects on the politics of its own beauty."
**Possible blind spots**: May not engage the technical realization deeply enough to judge the engine's claims.

---

## Phase 1: Parallel Multi-Perspective Review

### Jury Chair (EIC) Review Report

#### Reviewer Identity
SIGGRAPH Asia Art Papers Chair, generative- and environmental-art background.

#### Overall Recommendation
**Major Revision**

#### Confidence Score
4/5

#### Summary Assessment
*Tidal Drift* is a confident, well-documented practice-based work that addresses a timely concern — how to translate environmental sensor data into experience without falling into transparent "data visualization." The proposed "compost" model is the paper's most interesting move and could be a genuine contribution to the art+tech discourse. However, as written, the paper does not yet establish that "compost" is a load-bearing concept rather than an evocative re-label for layered generative synthesis. For the Art Papers audience, the work needs to (a) articulate precisely what the compost model claims that ordinary sonification does not, and (b) position itself against precedent eco-sound-art so the originality is legible. The realized work appears strong; the paper under-sells it.

#### Strengths
1. **S1: Timely, well-framed concern**: The work confronts a real problem in environmental data art — the tension between legibility and abstraction — and proposes a position, not just a piece.
2. **S2: Strong documentation**: Install photos, a video walkthrough, a signal-flow diagram, and pseudocode together let a juror evaluate the realized work, not just the artist's prose.
3. **S3: Honest process narrative**: The "three studio failures" framing signals practice-based research rather than a polished artist statement.

#### Weaknesses
1. **W1: "Compost" concept under-articulated**: The paper asserts compost as a third position but never states precisely what it claims (what is composted, into what, and why that is different from decay-based generative synthesis in general). Suggest a dedicated paragraph defining the concept and its claim (glossary §7 — concept vs. theme).
2. **W2: Originality not established**: The "first to treat environmental data as compostable material" framing is implicit and unsupported. Either position against precedent eco-sound-art and name the genuine gap, or hedge the precedence claim (evidence model §4).
3. **W3: Title/abstract foreground technique over concept**: The contribution is the compost *model*; the abstract reads as a system description. Foreground the conceptual claim.

#### Questions for Authors
1. State the compost model in one sentence: what does it claim about data-to-form translation that sonification does not?
2. Which precedent works does *Tidal Drift* most directly extend or depart from, and how?

---

### Realization Review Report (Reviewer 1 — Practitioner-Researcher)

#### Reviewer Identity
Practice-based artist-researcher in real-time generative audio systems.

#### Overall Recommendation
**Minor Revision**

#### Confidence Score
5/5

#### Summary Assessment
From a making-as-research standpoint this is among the stronger submissions: the layered-decay engine is documented with a signal-flow diagram and pseudocode, the three studio failures are narrated with what changed and why, and the artist is candid about the system's behavior. The realization is plausible and the making is genuinely documented as research. Two claims need tighter anchoring — "never repeats" and "live data" — and the relationship between the 4-minute video and the room-scale work needs clarifying so the documentation is not mistaken for the work itself (glossary §2). None of this is fatal; these are anchoring refinements.

#### Strengths
1. **S1: Realization documented as research, not asserted**: The decay-engine pseudocode plus signal-flow diagram make the central technical claim legible and plausible (evidence model §1 — the work and its system account as primary evidence).
2. **S2: Process integrity**: The three failures (feedback runaway, over-legible mapping, sensor-dropout silence) are documented with the design change each prompted — this is making-as-research.
3. **S3: Precise generative vocabulary, mostly**: "Generative" is used correctly for an ongoing non-repeating process, not for one-shot output (glossary §3).

#### Weaknesses
1. **W1: "Never repeats" is an unanchored capability claim**:
   **Problem**: The paper states the soundscape "never repeats" but the pseudocode shows a finite parameter space; over six weeks, perceptual recurrence is plausible.
   **Why it matters**: This is exactly the kind of capability over-claim a juror will probe (evidence model §4.1).
   **Suggestion**: Anchor it — either describe the state space and decay seeding that make recurrence vanishingly unlikely, or hedge to "does not perceptibly repeat within an exhibition session."
   **Severity**: Major

2. **W2: "Live data" anchoring**:
   **Problem**: It is unclear whether the estuary feed is truly live during exhibition or replayed/cached, and what happens on sensor dropout.
   **Why it matters**: "Live" is a realization claim that affects how the work is read (evidence model §4.1).
   **Suggestion**: State the data pipeline (poll interval, buffering, dropout fallback) in one short paragraph.
   **Severity**: Minor

3. **W3: Documentation-vs-work relationship unstated**:
   **Problem**: Experiential claims rest on a 4-minute single-channel video of an 8-channel room-scale work.
   **Why it matters**: The video documents but cannot stand in for the spatial experience (glossary §2).
   **Suggestion**: Add a one-line note on what the video does and does not capture; consider a binaural or multi-angle clip.
   **Severity**: Minor

#### Questions for Authors
1. Is the estuary feed live during exhibition, or cached/replayed? What is the dropout behavior?
2. Is the decay engine released or describable in enough detail that another practitioner could reconstruct its gist?

---

### Curatorial Review Report (Reviewer 2 — Curator / Exhibition Expert)

#### Reviewer Identity
Curator of media-art and environmental-art exhibitions; data-as-material lineage.

#### Overall Recommendation
**Major Revision**

#### Confidence Score
5/5

#### Summary Assessment
The work is exhibition-ready and the concept is intriguing, but the paper's positioning within the data-sonification and eco-media lineage is the weakest part. There is a substantial body of environmental sound-art practice that *Tidal Drift* neither cites nor distinguishes itself from, which makes the originality claim hard to assess. A few precisely positioned references would do more for this paper than its current scattered citations. The "third position between legibility and abstraction" is a real curatorial question, but the paper must show it knows the field it claims to advance.

#### Strengths
1. **S1: A genuine curatorial question**: The legibility-vs-abstraction tension is one the eco-media field actively debates; the work enters a live conversation.
2. **S2: Coherent exhibition framing**: The six-week single-estuary durational framing is conceptually consistent with the compost idea.

#### Weaknesses
1. **W1: Precedent works not engaged**:
   **Problem**: Foundational and recent eco-sound-art and data-as-material practices are absent from the references; the paper positions itself in a vacuum.
   **Why it matters**: Without precedent positioning the originality claim ("third position," implicit "first to compost data") is unsupported (evidence model §4 — novelty/precedence).
   **Suggestion**: Add and engage 4-6 precedent works/practitioners in ACM Reference Format, each with a real venue+date locator for the artworks (no fabricated DOIs), and state what *Tidal Drift* does differently.
   **Severity**: Critical

2. **W2: Concept not differentiated from prior decay-based generative practice**:
   **Problem**: Decay and entropy as compositional logics have precedent; the paper does not distinguish "compost" from these.
   **Why it matters**: The contribution rests entirely on this distinction.
   **Suggestion**: One paragraph contrasting compost (data as nutrient that transforms into new material) with decay-as-erosion in prior generative sound work.
   **Severity**: Major

3. **W3: Citation format and locators**:
   **Problem**: Several citations lack the page/section or venue+date locator the L3 citation gate requires; artwork citations give no exhibition venue+date.
   **Why it matters**: Citation faithfulness is a hard gate; artwork citations use venue+date as the locator.
   **Suggestion**: Add locators throughout; for cited artworks give "Artist, *Title*, venue, year."
   **Severity**: Minor

#### Missing Key Precedents (illustrative — verify before citing)
- Establish and cite the foundational data-sonification-as-art lineage the work extends.
- Cite recent estuary/coastal sound-art works for direct comparison (venue+date locators).
- Cite the legibility-vs-abstraction debate in eco-media criticism.

#### Questions for Authors
1. Which two precedent works is *Tidal Drift* in closest dialogue with, and what is the precise departure?
2. Can you support or hedge the implicit "first to compost environmental data" claim?

---

### Critical Perspective Review Report (Reviewer 3 — Art-Science / Media-Art Critic)

#### Reviewer Identity
Media-art critic and environmental-humanities theorist.

#### Overall Recommendation
**Major Revision**

#### Confidence Score
4/5

#### Summary Assessment
The compost model is conceptually rich and the work is clearly accomplished, but the paper does not yet reckon with the politics of its own beauty. Turning the sensor data of a specific imperiled estuary into a pleasurable, never-resolving ambient soundscape is an aesthetic and ethical choice that the paper treats as neutral. The most interesting version of this paper would ask whether composting crisis into ambience risks anaesthetizing the very concern it draws on. Separately, the reception claim ("visitors lingered") needs an observable anchor or it reads as inflation.

#### Strengths
1. **S1: A concept with reach**: "Compost" as a data-to-form logic could travel beyond sound art into eco-media practice generally — a real "so what for the field."
2. **S2: Situated honesty**: The work draws on one estuary rather than a generic "the environment," which grounds it.

#### Weaknesses
1. **W1: Representational ethics unexamined**:
   **Problem**: The paper does not reflect on what it means to render a threatened estuary's data as soothing, endless ambience.
   **Why it matters**: This is the work's central cultural stake and the field will expect engagement; ignoring it weakens the contribution.
   **Suggestion**: Add a reflective section on the politics of aestheticizing ecological data — does compost dignify the material or pacify the viewer?
   **Severity**: Major

2. **W2: Reception inflation**:
   **Problem**: "Visitors lingered" is stated with no observable anchor.
   **Why it matters**: Reception claims require a named venue/date + observable detail; otherwise it is inflation (evidence model §4 / glossary §8 — integrity flag).
   **Suggestion**: Anchor it (e.g., "at Estuary Futures 2024, dwell times observed by gallery staff commonly exceeded X minutes; visitor-book entries noted Y") or remove it.
   **Severity**: Major

3. **W3: Over-generalized claim risk**:
   **Problem**: The "third position" is stated as a general truth rather than as demonstrated *in this work, in this estuary*.
   **Why it matters**: Honest situated insight is stronger than over-generalization (evidence model — situated framing).
   **Suggestion**: Scope the claim to what *Tidal Drift* demonstrates and frame the general model as a proposition for the field.
   **Severity**: Minor

#### Cross-Disciplinary Reading Recommendations (illustrative)
- Environmental-humanities work on aestheticizing ecological crisis.
- Critical writing on data sonification and the ethics of "making data feelable."
- Posthumanist / more-than-human approaches to non-human co-authorship of generative work.

#### Questions for Authors
1. Does composting crisis into ambience risk pacifying the concern? How does the work guard against this?
2. What observable evidence supports the claim that visitors lingered?

---

## Phase 2: Editorial Synthesis & Decision

### Editorial Decision Package

#### Decision: **Major Revision**

#### Reviewer Summary

| Reviewer | Role | Recommendation | Confidence |
|----------|------|---------------|------------|
| Chair | Art Papers Chair (generative/eco-art) | Major Revision | 4/5 |
| Reviewer 1 | Practitioner-Researcher (generative audio) | Minor Revision | 5/5 |
| Reviewer 2 | Curator (eco-media / data-as-material) | Major Revision | 5/5 |
| Reviewer 3 | Critic (environmental humanities) | Major Revision | 4/5 |

#### Consensus Analysis

**[CONSENSUS-4]** (All reviewers agree):
1. The realized work is strong and well-documented
2. The "compost" concept is promising but under-articulated as a load-bearing concept
3. The contribution would be clearer with sharper conceptual definition and positioning

**[CONSENSUS-3]** (3/4 reviewers agree):
1. Originality/precedent positioning is insufficient (Chair + R2 + R3)
2. The paper foregrounds technique over the conceptual contribution (Chair + R2 + R3)

**Disagreement 1: Severity of realization issues**
- **R1 view**: Realization is sound; only Minor Revision (anchor "never repeats" / "live data," clarify video-vs-work)
- **R2/R3 view**: No major realization concerns (their Major comes from positioning and ethics)
- **Editor's Resolution**: Adopt R1's anchoring fixes as P1/P2 items, but they do not by themselves escalate severity. R1's confidence is 5/5 and the realization opinion is within their expertise — respected.

**Disagreement 2: Weight of representational-ethics concern**
- **R3 view**: The unexamined politics of aestheticizing crisis is a Major gap
- **R1 view**: Outside the realization remit; does not affect making rigor
- **Editor's Resolution**: R3's concern is a recognized core question in eco-media discourse and bears directly on the work's "so what." Listed P1, addressed by adding a reflective section — not by altering the work.

#### Decision Rationale
*Tidal Drift* is an accomplished, well-documented practice-based work whose realization the jury trusts. The barrier to acceptance is not the artwork but the paper's argument about it: the compost concept must be defined precisely, positioned against precedent eco-sound-art, and reckoned with ethically. Two realization claims ("never repeats," "live data") need anchoring, and the reception claim must be anchored or removed. These revisions are substantial (conceptual definition + lineage positioning + ethics reflection) but do not require remaking the work — hence Major Revision.

#### Revision Roadmap

**Priority 1 — Conceptual & Positioning Revisions (Estimated effort: 8-12 days)**
- [ ] R1: Define the compost model precisely — what is composted, into what, and what it claims that sonification does not (Source: Chair-W1, Major; concept vs. theme, glossary §7)
- [ ] R2: Position against 4-6 precedent eco-sound-art works in ACM Reference Format with venue+date locators; state the genuine departure, support or hedge the precedence claim (Source: R2-W1, Critical)
- [ ] R3: Add a reflective section on the representational ethics of aestheticizing ecological data (Source: R3-W1, Major)
- [ ] R4: Anchor or remove the "visitors lingered" reception claim with an observable anchor (Source: R3-W2, Major; reception inflation flag)

**Priority 2 — Realization Anchoring (Estimated effort: 3-5 days)**
- [ ] S1: Anchor or hedge "never repeats" against the engine's state space (Source: R1-W1, Major)
- [ ] S2: Describe the live-data pipeline and dropout behavior (Source: R1-W2)
- [ ] S3: Differentiate compost from prior decay-based generative practice (Source: R2-W2, Major)
- [ ] S4: Clarify what the video documents vs. the room-scale work (Source: R1-W3)

**Priority 3 — Text and Formatting (Estimated effort: 2 days)**
- [ ] Foreground the conceptual contribution in title and abstract (Source: Chair-W3)
- [ ] Scope the "third position" claim to what the work demonstrates (Source: R3-W3)
- [ ] Add ACM-format locators throughout; artwork citations use venue+date, no fabricated DOIs (Source: R2-W3)

**Revision Deadline**: Recommended 6-8 weeks. *Verify resubmission timeline against the current SIGGRAPH Asia Art Papers CFP.*
