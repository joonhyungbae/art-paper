# Example: Cross-Disciplinary (Art-Science Hybrid) Paper Review

This example demonstrates how `art-reviewer` configures jury roles and handles inter-disciplinary tensions when faced with a highly cross-disciplinary work. It simulates the SIGGRAPH Asia Art Papers jury reviewing an **art-science hybrid** (Pattern 5) work titled "Mycelial Score: A Bio-Computational Installation in Which a Living Fungal Network Drives Generative Sound."

This is the one pattern where a Method/Results-style empirical lens is appropriate **for the genuine technical sub-contribution** — but the artistic-significance lens stays dominant. The jury must hold both the wet-lab claim and the artwork-as-evidence claim at once.

---

## Simulated Paper Abstract

> **Title**: Mycelial Score: A Bio-Computational Installation in Which a Living Fungal Network Drives Generative Sound
>
> **Abstract**: *Mycelial Score* couples a living *Pleurotus ostreatus* mycelial network, grown on a custom electrode substrate, to a generative sound engine: fluctuations in the network's bioelectrical activity are read by a 16-channel sensor array and mapped to a real-time granular-synthesis composition. The work proposes the fungal network as a **non-human co-author** rather than a controlled instrument. Over a four-month studio practice I developed the substrate and an empirical mapping calibration: I report a small comparison of three signal-to-sound mappings (raw, normalized, predictive) evaluated for "musical legibility" by 14 listeners, finding the normalized mapping preferred. The work was shown at the 2024 Hybrid Matter Biennale (Singapore). I argue that the empirical calibration *serves* the artistic claim of co-authorship rather than reducing the fungus to a sensor. The contribution is twofold: a practice-based concept of fungal co-authorship, and a small technical contribution (the calibration method).
>
> **Keywords**: bio-art, generative sound, non-human co-authorship, bioelectrical sensing, practice-based research
>
> **Full text approximately 7,800 words, 34 references cited (ACM Reference Format); documentation: substrate fabrication photos, signal-flow diagram, mapping-comparison table, 5-min video, listener-study protocol**

---

## Phase 0: Field Analysis & Persona Configuration

### Field Analysis Report

#### Work / Paper Basic Information
- **Title**: Mycelial Score: A Bio-Computational Installation in Which a Living Fungal Network Drives Generative Sound
- **Full text length**: Approximately 7,800 words
- **Number of references**: 34 (ACM Reference Format)
- **Documentation present**: substrate fabrication photos, signal-flow diagram, mapping-comparison table, 5-min video, listener-study protocol

#### Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Art Subfield / Medium | Bio-art / generative sound installation (dual core) |
| Secondary Art+Tech Areas | Bioelectrical sensing, real-time audio synthesis, posthumanist theory |
| Mode of Inquiry | **Art-science hybrid (Pattern 5)** — practice-based concept PLUS a small genuine technical/empirical sub-contribution |
| Realization Approach | Custom electrode substrate, 16-channel bioelectrical sensing, granular-synthesis mapping engine |
| Exhibition / Venue Context & Ambition | One biennale exhibition (Hybrid Matter 2024, Singapore); SIGGRAPH Asia Art Papers-level ambition. *Verify against current Call for Art Papers.* |
| Paper / Work Maturity | Pre-submission — complete structure, work realized and exhibited, calibration study done |

#### Suggested Venues / Programs (Top 3)
1. **SIGGRAPH Asia Art Papers** — bio-art with both a conceptual and a technical sub-contribution fits the art+tech program. *Verify against current CFP.*
2. **Leonardo (MIT Press)** — strong fit for art-science hybrid papers with a calibration sub-study
3. **ISEA Art track** — bio-art and non-human-agency works are well represented

#### Reviewer Configuration Cards

The configuration challenge here mirrors the cross-disciplinary problem: the work spans **bio-art making + bioelectrical sensing/calibration + posthumanist theory**. The jury must cover all three without collapsing into "three bio-art generalists" (who would miss the calibration rigor) or "three engineers" (who would miss the artistic and ethical stakes).

---

### Reviewer Configuration Card #1

**Role**: Jury Chair (EIC)
**Identity Description**: SIGGRAPH Asia Art Papers Chair with a bio-art / hybrid-media background; has chaired art-science programs and attends to whether the work belongs in the program and whether the empirical sub-contribution genuinely serves the art.
**Review Focus**:
  1. Artistic significance and fit — does fungal co-authorship contribute to the art+tech discourse?
  2. Whether the empirical calibration *serves* the artwork or whether the work has been flattened into "a fungus-driven system" (Pattern 5 risk)
  3. Originality of the co-authorship claim against precedent bio-art
**Will particularly care about**: "Whether 'co-author' is a load-bearing concept or anthropomorphic decoration; whether the listener study is reported honestly as small and situated, not over-generalized."
**Possible blind spots**: May not assess the bioelectrical-sensing details deeply.

---

### Reviewer Configuration Card #2

**Role**: Reviewer 1 — Practitioner-Researcher (methodology slot; given the Pattern-5 empirical lens)
**Identity Description**: Bio-art practitioner with wet-lab experience and a background in sensor-driven generative systems; the only reviewer carrying the empirical-evaluation lens, applied **only** to the genuine technical sub-contribution.
**Review Focus**:
  1. Realization rigor — is the electrode substrate and 16-channel sensing described specifically enough to be plausible (and safe)?
  2. The calibration sub-study — is the small listener comparison (N=14, three mappings) reported well enough to be plausible, and framed as situated rather than a generalizable finding?
  3. Capability-claim anchoring — "real-time," "the network drives," "co-author" — anchored in substrate/signal-flow, or asserted?
**Will particularly care about**: "Whether the listener study is honestly scoped (a small in-studio calibration, not a controlled experiment) and whether bio-safety/ethics of living media is noted; whether the video documents the work or substitutes for it (glossary §2)."
**Possible blind spots**: May under-weight the curatorial lineage and the posthumanist-theory stakes.

> Note: this is the **only** pattern where R1 applies a Method/Results-style lens, and only to the calibration sub-contribution. R1 must NOT demand statistical power, large-N sampling, or hypothesis testing of the *artwork* — anchoring, not sample size, remains the criterion for the practice-based claim.

---

### Reviewer Configuration Card #3

**Role**: Reviewer 2 — Curator / Exhibition Expert (domain slot, art sense)
**Identity Description**: Curator of bio-art and art-science exhibitions; deeply familiar with the living-media and non-human-agency lineage; has organized programs on biological co-authorship.
**Review Focus**:
  1. Conceptual lineage — is the work positioned against precedent bio-art and non-human-agency works (so the co-authorship claim is legible)?
  2. Novelty / precedence — is "fungal network as co-author" a citable departure from existing living-media practice, or an unsupported "first"?
  3. Exhibition framing — does the biennale presentation support the co-authorship claim?
**Will particularly care about**: "Whether key bio-art precedents are cited in ACM format with venue+date locators (no fabricated DOIs), and whether the co-authorship framing genuinely extends the lineage."
**Possible blind spots**: May focus on lineage at the expense of the calibration rigor R1 covers.

---

### Reviewer Configuration Card #4

**Role**: Reviewer 3 — Art-Science / Media-Art Critic (perspective slot, art sense; the most "different" angle)
**Identity Description**: Posthumanist / science-and-technology-studies critic researching non-human agency and the ethics of working with living organisms in art; brings the angle the practitioner and curator may not.
**Review Focus**:
  1. Theoretical depth of the co-authorship claim — is "co-author" earned, or anthropomorphism dressed as theory?
  2. Bio-ethics — what are the stakes of cultivating, instrumentalizing, and ultimately disposing of a living organism for an artwork?
  3. The "so what for the field?" — what does *Mycelial Score* say to bio-art and more-than-human practice?
**Will particularly care about**: "Whether agency/autonomy language is precise (glossary §3) or inflated; whether reception is anchored; whether the calibration study quietly contradicts co-authorship by treating the fungus as a controllable signal source."
**Possible blind spots**: May under-engage the technical realization.

---

## Phase 1: Parallel Multi-Perspective Review (Summary Version)

### Jury Chair (EIC) Review Report (Summary)

**Recommendation**: Major Revision | **Confidence**: 4/5

**Core view**: A genuinely ambitious art-science hybrid. The risk specific to Pattern 5 is present: the paper occasionally reads as "a fungus-driven synthesis system with a listener study attached" rather than an artwork whose empirical calibration serves the co-authorship claim. The work is significant and fits the program, but the paper must keep the artistic argument dominant and prevent the calibration from quietly reducing the fungus to a sensor — which would undercut the co-authorship concept.

**Key Strengths**:
1. Two distinct contributions (a practice-based concept + a small honest technical method) clearly delineated
2. Strong, multi-modal documentation that lets a juror evaluate the realized work
3. A timely concept (non-human co-authorship) with reach into more-than-human practice

**Key Weaknesses**:
1. Tension between the empirical calibration and the co-authorship claim is unresolved (Pattern 5 flattening risk)
2. Co-authorship concept asserted more than argued
3. Precedent bio-art positioning thin

---

### Realization Review Report — R1 (Summary)

**Recommendation**: Minor Revision | **Confidence**: 5/5

**Core view**: The making is documented as research and the realization is plausible. The small calibration sub-study is acceptable **as a situated calibration**, not as a controlled experiment — and the paper mostly frames it that way. The fixes are about anchoring capability language and adding a bio-safety/ethics note, plus keeping the listener study honestly scoped.

**Key Strengths**:
1. Electrode-substrate fabrication and 16-channel signal flow are documented with photos and a diagram — the realization is legible (evidence model §1)
2. The three-mapping comparison is a reasonable, honestly small calibration that genuinely informed the work
3. "Generative" and "granular synthesis" used precisely (glossary §3)

**Key Weaknesses**:
1. **Capability anchoring** (Major): "the network drives the composition" and "real-time" need anchoring in the signal-flow latency and mapping — currently asserted (evidence model §4.1)
2. **Listener-study scoping** (Major): N=14 in-studio is fine as calibration but must be explicitly framed as situated; the abstract's "finding the normalized mapping preferred" risks reading as a generalizable result. Scope it ("in this calibration, with these 14 listeners"). Do **not** import statistical-power language — the issue is honest framing, not sample size.
3. **Bio-safety/ethics note missing** (Minor): living-media work needs a short safety/handling/end-of-life note (evidence model — living-media practice)

**Questions for Authors**:
1. What is the end-to-end latency from bioelectrical fluctuation to audible change, and does it support "real-time"?
2. Is the substrate/sensing pipeline described well enough that another practitioner could reconstruct its gist?

---

### Curatorial Review Report — R2 (Summary)

**Recommendation**: Major Revision | **Confidence**: 5/5

**Core view**: The work sits in an active bio-art lineage (living media, non-human agency) that the paper barely engages. The co-authorship claim cannot be assessed for originality without that positioning. A few precisely chosen precedents would establish the contribution far better than the current scattered references.

**Key Strengths**:
1. The co-authorship framing is a real, current question in bio-art
2. The biennale exhibition context is coherent with the concept

**Key Weaknesses**:
1. **Precedent bio-art not engaged** (Critical): Foundational and recent living-media / non-human-agency works are absent; the implicit "first to treat a fungal network as co-author" precedence claim is unsupported (evidence model §4). Add and engage 4-6 precedents in ACM format with venue+date locators; state the departure.
2. **Co-authorship not differentiated from "biological instrument"** (Major): Prior bio-art has used organisms as signal sources; the paper must distinguish *co-authorship* from *instrumentation* or the concept collapses.
3. **Citation locators** (Minor): artwork citations lack venue+date locators; some literature citations lack page/section anchors (L3 gate).

**Missing Key Precedents (illustrative — verify before citing)**:
- The foundational living-media / bio-art lineage the work extends
- Recent fungal/plant-signal art works for direct comparison (venue+date locators)
- Curatorial/critical writing on non-human agency in art

---

### Critical Perspective Review Report — R3 (Summary)

**Recommendation**: Major Revision | **Confidence**: 3/5

**Core view**: This is where the paper is most exposed. The co-authorship claim is philosophically interesting but, as written, risks anthropomorphism — and the calibration study quietly undercuts it by treating the fungus as a tunable signal source. The bio-ethics of cultivating and disposing of a living organism for an artwork are unexamined. The strongest version of this paper would make the tension between "co-author" and "calibrated signal source" its subject rather than its blind spot.

**Key Strengths**:
1. The concept reaches into more-than-human and STS discourse — real "so what for the field"
2. Working with a specific living organism (not a generic "nature") grounds the claim

**Key Weaknesses**:
1. **Co-authorship vs. instrumentation contradiction** (Critical): The empirical calibration optimizes the fungus's signal for *human* musical legibility — which is closer to instrumentation than co-authorship. The paper does not address this. Either reframe co-authorship to accommodate calibration, or acknowledge the tension as a finding. (agency/autonomy precision, glossary §3)
2. **Bio-ethics unexamined** (Major): cultivating, instrumentalizing, and disposing of a living organism for art carries ethical stakes the paper ignores; add a reflective section.
3. **Reception anchoring** (Major): any claim about how audiences responded at the biennale needs a named-venue/date + observable anchor, not "the work resonated" (evidence model §4 / glossary §8 — reception inflation flag).

**Cross-Disciplinary Reading Recommendations (illustrative)**:
- STS / more-than-human writing on non-human agency and co-production
- Bio-art criticism on the ethics of living media
- Posthumanist accounts of authorship and agency

**Questions for Authors**:
1. If you calibrate the fungus's signal for human legibility, in what sense is it a co-author rather than an instrument?
2. What is the organism's end-of-life in the work, and how do you frame that ethically?

---

## Phase 2: Editorial Synthesis & Decision (Summary Version)

### Decision: **Major Revision**

### Consensus Analysis

**[CONSENSUS-4]**:
1. The work is ambitious and fits the art+tech program
2. The empirical calibration must clearly *serve* the artwork, not flatten it (Pattern 5 risk)
3. The co-authorship concept needs to be argued and positioned, not asserted

**[CONSENSUS-3]**:
1. Precedent bio-art positioning is insufficient (Chair + R2 + R3)
2. Capability/agency language needs precise anchoring (Chair + R1 + R3)

**Disagreement 1: Severity of the calibration-vs-concept tension**
- **R3**: The contradiction between calibrating-for-human-legibility and claiming co-authorship is Critical
- **R1**: The calibration is a sound, honestly-scoped sub-study; not a defect in itself (Minor on that axis)
- **Resolution**: Both are right about different things. R1 is correct that the *study* is methodologically fine for a situated calibration (R1 confidence 5/5, within expertise). R3 is correct that the study's *implication* for the co-authorship concept is unaddressed. Listed P1 as a conceptual revision — the author must resolve or own the tension — without requiring the study be redone.

**Disagreement 2: Weight of bio-ethics**
- **R3**: Unexamined living-media ethics is Major
- **R1**: A short safety/ethics note suffices (Minor)
- **Resolution**: R3's framing is the recognized standard for living-media art and bears on the work's significance. Listed P1 (reflective section), which subsumes R1's safety-note request.

### Decision Rationale
*Mycelial Score* is a strong art-science hybrid whose realization the jury trusts and whose calibration sub-study is honestly small. The barriers to acceptance are conceptual and discursive: the co-authorship claim must be argued and positioned against precedent bio-art; the tension between calibrating the organism's signal and calling it a co-author must be resolved or owned; and the living-media ethics must be engaged. The Pattern-5 lens applies only to the calibration sub-contribution and the jury did not import statistical-rigor demands onto the artwork. Revisions are substantial but do not require remaking the work or rerunning the study — hence Major Revision.

### Revision Roadmap

**Priority 1 — Conceptual, Positioning & Ethics Revisions (Estimated effort: 10-14 days)**
- [ ] R1: Engage 4-6 precedent bio-art works in ACM format with venue+date locators; support or hedge the co-authorship precedence claim; distinguish co-authorship from instrumentation (Source: R2-W1/W2, Critical/Major)
- [ ] R2: Resolve or explicitly own the calibration-vs-co-authorship tension as part of the argument (Source: R3-W1, Critical)
- [ ] R3: Add a reflective section on living-media bio-ethics (cultivation, instrumentalization, end-of-life) (Source: R3-W2 + R1-W3, Major)
- [ ] R4: Anchor any biennale reception claim with named-venue/date + observable detail, or remove it (Source: R3-W3, Major; reception inflation flag)

**Priority 2 — Realization Anchoring (Estimated effort: 4-6 days)**
- [ ] S1: Anchor "real-time" and "the network drives" in latency + signal-flow detail (Source: R1-W1, Major)
- [ ] S2: Explicitly scope the listener study as a situated calibration, not a generalizable result — no statistical-power framing (Source: R1-W2, Major)
- [ ] S3: Clarify what the 5-min video documents vs. the installed work (Source: glossary §2)

**Priority 3 — Text and Formatting (Estimated effort: 2 days)**
- [ ] Add ACM-format locators throughout; artwork citations use venue+date, no fabricated DOIs (Source: R2-W3)
- [ ] Foreground the dual contribution (concept + method) clearly in title/abstract, keeping the artistic claim dominant
- [ ] Standardize ACM Reference Format

**Revision Deadline**: Recommended 8 weeks. *Verify resubmission timeline against the current SIGGRAPH Asia Art Papers CFP.*

---

## Pedagogical Value of This Example

### 1. Challenges of Cross-Disciplinary Jury Configuration

This work spans bio-art making + bioelectrical sensing/calibration + posthumanist theory. The `field_analyst_agent`'s configuration strategy was:
- **R1 (Practitioner-Researcher)**: bio-art practitioner carrying the **Pattern-5 empirical lens** — because the calibration sub-study needs someone who can judge it, but applied *only* to that sub-contribution
- **R2 (Curator)**: bio-art lineage expert — because positioning the co-authorship claim against precedent living-media work is crucial
- **R3 (Critic)**: posthumanist/STS critic — because the conceptual and ethical stakes are the aspect most likely to be the work's blind spot

If all three were bio-art generalists, the calibration's honest scoping would be missed; if all three were engineers, the co-authorship concept and the living-media ethics would be overlooked.

### 2. Unique Value of Reviewer 3

R3 raised the issue no other reviewer reached: that the empirical calibration (optimizing the fungus's signal for human legibility) quietly contradicts the co-authorship concept, and that the living-media ethics are unexamined. This is precisely the design value of `perspective_reviewer_agent` — it represents a discourse the artist may not have engaged.

### 3. Disagreement Handling Example

R3 considers the calibration-vs-concept tension Critical; R1 considers the calibration study itself sound (Minor on its own axis). The `editorial_synthesizer_agent`'s arbitration distinguished the two claims: the *study* is methodologically fine (R1, 5/5, within expertise), but its *implication for the concept* is unaddressed (R3). Both were honored without forcing the author to redo the study.

### 4. The Pattern-5 Discipline

This work's distinguishing feature is that it carries a genuine empirical sub-contribution (the mapping calibration). The reviewer applied a Method/Results-style lens **only** to that sub-study — and explicitly refused to import statistical-power, large-N sampling, or hypothesis-testing demands onto the *artwork*. For a practice-based art paper the criterion is anchoring, not sample size; Pattern 5 narrows, but does not remove, that discipline.
