---
scenario: Major Revision decision, 5 items including a DA-CRITICAL, one item marked DELIBERATE_LIMITATION
mode: revision (within pipeline Stage 4)
demonstrates: Revision tracking, Response to Reviewers, and re-review leading to Accept
---

# Revision Recovery Example

This example shows how the revision process handles a Major Revision decision with 5 revision items, including a DA-CRITICAL finding and a deliberate limitation, for a practice-based art paper. It demonstrates the complete revision workflow from the Revision Roadmap through the Response to Reviewers letter, culminating in a re-review verdict of Accept with Minor Edits.

> **AI-generated demonstration.** The artist, work, venue, jurors, and citations are fictional.

## Context

**Paper**: "Holding the Room: A Gesture-Driven Generative Installation and the Question of Audience Authorship"
**Word count**: 5,400 words (Practice-Based Art Paper, Pattern 1)
**References**: 38 entries (ACM Reference Format)
**Pipeline state**: Stage 2.5 (INTEGRITY) passed, Stage 3 (REVIEW) completed

---

## Starting Point: Stage 3 Review Decision

### Jury Configuration

```
Paper domain: Media Art / Interactive & Generative Installation
Research mode: Practice-based art research (the artwork is primary evidence)
Contribution type: Authored artwork + situated reflection on audience authorship

Jury Configuration (configured by field_analyst_agent):
  Chair:        Art Papers chair, specializing in media art and exhibition practice
  Reviewer 1:   Practitioner-researcher, specializing in interactive installation and embodied interaction
  Reviewer 2:   Curator, specializing in generative and time-based media art
  Reviewer 3:   Art-science critic, specializing in human-computer interaction and aesthetics
  Devil's Advocate: Challenges the core premise and identifies overlooked counter-positions
```

### Five-Dimension Scores (Pre-Revision)

| Dimension | Weight | R1 | R2 | R3 | DA | Weighted Avg |
|-----------|--------|----|----|----|----|-------------|
| Conceptual Originality | 20% | 72 | 78 | 70 | 65 | 71.3 |
| Practice-Based Rigor / Realization | 25% | 55 | 62 | 58 | 50 | 56.3 |
| Evidence & Reception Anchoring | 25% | 60 | 65 | 55 | 48 | 57.0 |
| Argument / Reflection Coherence | 15% | 68 | 72 | 62 | 55 | 64.3 |
| Writing & Documentation Quality | 15% | 75 | 78 | 74 | 72 | 74.8 |
| **Weighted Total** | -- | -- | -- | -- | -- | **62.4** |

Per the quality rubrics (50-64 = Major Revision), this score yields:

**Editorial Decision: Major Revision**

---

### Revision Roadmap

| # | Description | Reviewer | Type | Priority | Target Section |
|---|-------------|----------|------|----------|---------------|
| 1 | Reception claims unanchored — the Reflection states "audiences were captivated" and "the work clearly resonated" with no observable evidence (named venue/date + observable detail). This is reception inflation. | R1 | Major | must_fix | Reflection (Section 6) |
| 2 | Missing conceptual positioning: the recent discourse on agency-as-surrender for involuntary-signal work, and the consent-and-sensed-body critique, are directly relevant but absent from the Conceptual Framework. | R2 | Major | must_fix | Conceptual Framework (Section 3) |
| 3 | Core premise "interactive art must make the audience feel in control" is a strawman — no serious practitioner or theorist holds that control is the only valid model of audience agency. The paper argues against a position no one defends, which weakens the entire contribution. | DA | DA-CRITICAL | must_fix | Introduction (Section 1) + Reflection (Section 6) |
| 4 | The Realization section asserts the system is "real-time" and "fully autonomous" without a realization anchor; and Figure 3 lacks an image-courtesy line for a reproduced precedent work. | R1 | Minor | should_fix | Realization (Section 5) + Figures |
| 5 | Several paragraphs in the Reflection exceed 200 words, making them difficult to parse. | R3 | Minor | consider | Reflection (Section 6) |

---

## Revision Tracking Template (Filled)

### Paper Information

| Field | Value |
|-------|-------|
| Paper Title | Holding the Room: A Gesture-Driven Generative Installation and the Question of Audience Authorship |
| Revision Round | 1 |
| Date | 2026-03-06 |
| Previous Decision | Major Revision |
| Target Venue | SIGGRAPH Asia Art Papers (verify against current CFP) |
| Original Word Count | 5,400 words |
| Revised Word Count | 6,300 words |

### Revision Tracking Table

| # | Issue Description | Reviewer | Type | Section | Resolution Summary | Location of Change | Status | Reason (if not resolved) |
|---|-------------------|----------|------|---------|-------------------|-------------------|--------|--------------------------|
| 1 | Reception claims unanchored ("audiences were captivated"); reception inflation | R1 | Major | Reflection | Replaced unanchored claims with observable evidence: anchored to the [Example] Media Art Biennale (2025) run, drawing on 45 logged gallery sessions and 12 exit conversations; down-scoped to what was observed/recorded | Section 6.2 (para 1-3), Abstract (sentence 3) | RESOLVED | -- |
| 2 | Missing agency-as-surrender and consent-and-sensed-body discourse | R2 | Major | Conceptual Framework | Added a positioning subsection (Section 3.3) engaging the surrender model and the consent critique; connected both to the work's gesture-driven design; added 4 new references | Section 3.3 (new, 600 words), Section 6.3 (dialogue) | RESOLVED | -- |
| 3 | "Interactive art must make the audience feel in control" is a strawman; no one holds it | DA | DA-CRITICAL | Introduction + Reflection | Reframed from a "control vs. no-control" binary to an "agency spectrum" (command → negotiation → surrender); replaced the strawman with the genuine tension between legible control and felt agency | Section 1 (para 3-5 rewritten), Section 6.1 (para 1-2 rewritten), Section 6.4 (new synthesis paragraph) | RESOLVED | -- |
| 4 | "real-time"/"fully autonomous" without anchor; Figure 3 missing image courtesy | R1 | Minor | Realization + Figures | Defined "real-time" (sub-100ms gesture-to-response) and "autonomous" (no operator/timeline) with realization anchors; added image-courtesy line to Figure 3 | Section 5.2 (para 2-3), Figure 3 caption | RESOLVED | -- |
| 5 | Reflection paragraphs exceed 200 words; readability concern | R3 | Minor | Reflection | Most paragraphs restructured to 150-190 words. Three paragraphs retained at 210-220 words where splitting would disrupt a sustained argument integrating the work, the logs, and a precedent. | Section 6.1 (para 2: 215 words), Section 6.3 (para 4: 218 words), Section 6.4 (para 1: 212 words) | DELIBERATE_LIMITATION | These three paragraphs develop complex arguments integrating the artwork-as-evidence, the session logs, and a precedent work each. Splitting them would require artificial transitions that weaken argumentative coherence. The 200-word guideline aids readability but is not a venue rule. The 10-20 word excess is marginal; we prioritize argument integrity. Noted in the Response to Reviewers with justification. |

### Summary Statistics

| Metric | Count |
|--------|-------|
| Total items | 5 |
| Resolved | 4 |
| Deliberate Limitation | 1 |
| Unresolvable | 0 |
| Reviewer Disagree | 0 |
| Word count change | +900 words |
| New references added | 4 |
| New figures/tables added | 0 (1 figure caption corrected) |

---

## Detailed Revisions

### Item 1 (RESOLVED): Re-Anchoring Reception Claims

**R1's concern**: "The Reflection states that 'audiences were captivated' and 'the work clearly resonated.' These are unanchored reception claims — there is no named venue/date or observable detail. In a practice-based paper the situated reception is primary evidence; unanchored claims read as the artist's hope rather than as documentation."

**Changes made**:

*Section 6.2 — Before:*
> Audiences were captivated by the work, and it clearly resonated with visitors of all ages. People stayed for a long time and seemed deeply engaged.

*Section 6.2 — After:*
> Across 45 logged gallery sessions at the [Example] Media Art Biennale (2025), field notes recorded a recurring pattern: visitors who discovered that broad arm gestures shifted the light field tended to repeat and refine those gestures over several minutes before settling into smaller movements. Median dwell time across logged sessions was approximately 6 minutes (recorded from entry/exit timestamps), longer than the gallery's typical 2-3 minutes for adjacent works. In 12 exit conversations, several visitors described "finding the gesture that worked"; two said they felt the work was "playing back" at them rather than simply responding.

*Abstract, sentence 3 — Before:* "The work was widely praised at its exhibition."
*Abstract, sentence 3 — After:* "Exhibited for six weeks at the [Example] Media Art Biennale (2025), the work was studied through 45 logged gallery sessions and 12 exit conversations."

### Item 2 (RESOLVED): Conceptual Positioning

**R2's concern**: "The Conceptual Framework grounds the work in classic interactive-art theory but omits two directly relevant recent strands: the model of agency-as-surrender for involuntary-signal work, and the consent-and-sensed-body critique. Both are standard in current media-art discourse and their absence is a significant gap in positioning."

**Changes made**:

*Section 3.3 (new, 600 words) — Added:*
> 3.3 Positioning: Between Command and Surrender
>
> Recent discourse distinguishes a *command* model of audience agency — the participant exercises control through legible gestures whose mapping to the work's response is discoverable [Costello and Edmonds 2019] — from a *surrender* model associated with works keyed to involuntary signals, where agency is felt by yielding rather than commanding [Schiphorst 2021; Author K 2021]. *Holding the Room* is gesture-driven and therefore sits closer to the command end, but its slow generative response deliberately frustrates tight legibility, placing it in a negotiation zone between the two models. [...]
>
> A parallel strand concerns consent and the sensed body [Author N 2023]. While *Holding the Room* senses deliberate gesture rather than involuntary physiology, the consent critique still bears on its full-room camera sensing, which we address in the Realization and Reflection. [...]

*New references added:*
- Author K. 2021. Against legibility: opacity as a value in somatic installation. *Leonardo* 54, 5 (2021), 501-508. https://doi.org/10.1162/xxxxxxx
- Author N. 2023. Consent and the sensed body: ethics of biosignal art. *[Fictional] Journal of Media Art* 15, 1 (2023), 22-44. https://doi.org/10.1162/xxxxxxx
- Thecla Schiphorst. 2021. Somaesthetics and felt interaction in media art. *Leonardo* 54, 2 (2021), 134-141. https://doi.org/10.1162/xxxxxxx
- Brigid Costello and Ernest Edmonds. 2019. Directed and emergent play in interactive art. In *Proceedings of the [Fictional] Conference on Creativity and Cognition*. https://doi.org/10.1145/xxxxxxx

### Item 3 (RESOLVED): DA-CRITICAL Strawman Reframing

**Devil's Advocate finding**: "The paper's core framing — 'interactive art must make the audience feel in control' — is a strawman. No serious practitioner or theorist argues that control is the only valid model of audience agency; the surrender model and negotiated-agency models are well established. By arguing against a position no one defends, the paper's contribution is undermined: it triumphantly demonstrates that pure control is not the only goal, when no one claimed it was."

**This was the most significant revision.** The DA-CRITICAL finding required reframing the paper's central argument, affecting the Introduction and Reflection.

**Changes made**:

*Section 1, para 3-5 — Before:*
> A fundamental assumption in interactive art is that the audience must feel in control — that good interactive work makes the participant the master of the work's behavior. This paper challenges that assumption by showing that audiences can find meaning even when they are not fully in control.
>
> We argue that interactive art does not need to make the audience feel in control to be successful.

*Section 1, para 3-5 — After:*
> The discourse on audience agency in interactive art is not a debate about whether the audience must feel in control — the field has long recognized command, negotiation, and surrender as distinct, legitimate models of agency [Edmonds 2018; Schiphorst 2021]. The substantive question is *where on this spectrum* a given work places the audience, and what felt experience results. *Holding the Room* is deliberately built to sit between command and negotiation: its gestures are legible enough to invite control, but its slow generative response withholds the tight feedback that would make control complete.
>
> This paper investigates what that in-between placement does to the felt experience of authorship, drawing on the work itself and on situated observation of its exhibition.

*Section 6.1, para 1-2 — Before:*
> Our exhibition confirms that audiences do not need to feel in control to enjoy interactive art. Visitors engaged deeply even though they could not fully control the work.

*Section 6.1, para 1-2 — After:*
> Our exhibition illuminates the negotiation zone between command and surrender rather than adjudicating whether control is necessary. The session logs show visitors first seeking control (repeating and refining gestures) and then, as the slow response frustrated tight legibility, shifting toward a looser, more exploratory engagement — neither full command nor full surrender. The two visitors who said the work felt like it was "playing back" describe precisely this negotiated agency: a sense of authorship that is shared with, rather than exercised over, the work.

*Section 6.4 (new synthesis paragraph) — Added:*
> The agency-spectrum framing moves the discussion beyond a control/no-control binary toward a more productive question: for a given work, where on the command-negotiation-surrender spectrum does the audience sit, and is that placement an artistic choice the maker controls? Our experience suggests that response timescale is the principal lever: fast, legible response pushes toward command; slow, aggregate response pushes toward surrender; an intermediate timescale, as here, holds the audience in negotiation. This reframes interaction design as the composition of an agency position, not the maximization of control.

### Item 4 (RESOLVED): Technical Claim Anchoring and Image Courtesy

**R1's concern**: "The Realization section asserts the system is 'real-time' and 'fully autonomous' without any anchor a reader could assess; and Figure 3, which reproduces a precedent work, lacks an image-courtesy line."

*Section 5.2 — Before:*
> The system runs in real-time and is fully autonomous.

*Section 5.2 — After:*
> The system processes the camera feed and updates the light field within approximately 80 ms of a detected gesture (measured from frame capture to projector output), which we describe as real-time for the purposes of this work. It is autonomous in the operational sense that, at exhibition time, there is no operator and no fixed timeline: the generative engine runs continuously from the live camera input. The author authored the gesture-to-light mapping; the moment-to-moment output is not scripted.

*Figure 3 caption — Before:* "Figure 3. A precedent work."
*Figure 3 caption — After:* "Figure 3. *[Precedent Work Title]* (Artist Name, 2018), gesture-driven installation. Image courtesy of the artist / [Fictional] Media Art Biennale."

### Item 5 (DELIBERATE_LIMITATION): Paragraph Length

**R3's concern**: "Several paragraphs in the Reflection exceed 200 words. While not a venue rule, shorter paragraphs improve readability and signal clear argumentative structure."

**Action taken**: 11 of 14 Reflection paragraphs were restructured to 150-190 words. Three paragraphs were deliberately retained at 210-220 words:

| Paragraph | Word Count | Justification |
|-----------|-----------|---------------|
| Section 6.1, para 2 (negotiated agency) | 215 | Integrates the artwork-as-evidence, the session-log pattern, and the two exit conversations. Splitting would sever the observation from its evidence. |
| Section 6.3, para 4 (dialogue with the surrender model) | 218 | Sustains a comparison between this work's negotiation zone and the surrender model, citing two precedents. The comparison requires continuous exposition. |
| Section 6.4, para 1 (agency-spectrum synthesis) | 212 | The new synthesis paragraph responding to the DA-CRITICAL item. It is the paper's core contribution; splitting it would dilute the argument. |

**Limitations section reference**: "We acknowledge that three Reflection paragraphs exceed the 200-word readability guideline. They were retained at 210-220 words to preserve argumentative coherence in passages that integrate the work, the session logs, and precedent."

---

## Response to Reviewers

---

**Submission No.:** SA-ART-2026-0287-R1

**Title:** Holding the Room: A Gesture-Driven Generative Installation and the Question of Audience Authorship

**Revision Date:** 2026-03-06

---

Dear Chair and Reviewers,

Thank you for your thorough and constructive review. The feedback has significantly strengthened the paper, particularly the Devil's Advocate challenge regarding our core framing, which prompted a substantive reorientation of the argument. We respond to each item below. All revisions are marked in blue in the revised manuscript.

---

### Response to Reviewer 1 (Practitioner-Researcher)

#### Comment R1-1: Reception Inflation (Major)

**Reviewer comment**: "The Reflection states that 'audiences were captivated' and 'the work clearly resonated' with no observable evidence. This is reception inflation."

**Author response**: We agree fully. We removed the unanchored claims and replaced them with observable evidence anchored to the [Example] Media Art Biennale (2025): a gesture-refinement pattern recorded across 45 logged sessions, recorded dwell times, and the content of 12 exit conversations. We have down-scoped all reception language to what was observed or recorded.

**Changes made**:
- Section 6.2, paragraphs 1-3: Rewritten with anchored evidence
- Abstract, sentence 3: Replaced "widely praised" with the observation basis

> See revised manuscript Section 6.2; Abstract

#### Comment R1-2: Technical Claims and Image Courtesy (Minor)

**Reviewer comment**: "'real-time' and 'fully autonomous' lack anchors; Figure 3 lacks an image-courtesy line."

**Author response**: We defined "real-time" (~80 ms gesture-to-output, measured) and "autonomous" (no operator/timeline; continuous live generation) with realization anchors, and added the image-courtesy line to Figure 3.

**Changes made**:
- Section 5.2, paragraphs 2-3: Anchored definitions
- Figure 3 caption: Added artist attribution and image courtesy

> See revised manuscript Section 5.2; Figure 3

---

### Response to Reviewer 2 (Curator)

#### Comment R2-1: Missing Conceptual Positioning (Major)

**Reviewer comment**: "The Conceptual Framework omits the agency-as-surrender model and the consent-and-sensed-body critique, both directly relevant."

**Author response**: We agree these are essential. We added Section 3.3 ("Positioning: Between Command and Surrender," ~600 words) engaging both strands and connecting them to the work's gesture-driven, slow-response design, which we argue sits in a negotiation zone between command and surrender. Four new references support this section, and we extended the Reflection's dialogue (Section 6.3) accordingly.

**Changes made**:
- Section 3.3 (new, 600 words): Positioning between command and surrender
- Section 6.3: Dialogue with the surrender model
- 4 new references: Costello & Edmonds (2019), Schiphorst (2021), Author K (2021), Author N (2023)

> See revised manuscript Section 3.3; Section 6.3

---

### Response to Devil's Advocate

#### Comment DA-1: Strawman Framing (DA-CRITICAL)

**Devil's Advocate challenge**: "The paper's core framing — 'interactive art must make the audience feel in control' — is a strawman. No serious practitioner or theorist holds that control is the only valid model of agency. By arguing against a position no one defends, the paper's contribution is undermined."

**Author response**: This is the most consequential feedback we received, and we accept it fully. Our original framing argued against a position no one holds.

We have fundamentally reframed the argument. The binary "control vs. no-control" has been replaced with an "agency spectrum" (command → negotiation → surrender). This changes the paper's contribution from the trivial claim that control is not strictly necessary to a substantive one: that *Holding the Room* deliberately holds the audience in a negotiation zone, and that response timescale is the principal lever a maker uses to compose an audience's agency position.

Specific changes:

1. **Introduction (Section 1, paragraphs 3-5)**: Completely rewritten. The new framing acknowledges the established command/negotiation/surrender models and positions the work's contribution as investigating the in-between.
2. **Reflection (Section 6.1, paragraphs 1-2)**: Rewritten to interpret the session-log pattern as negotiated agency rather than as "control is unnecessary."
3. **New synthesis paragraph (Section 6.4)**: Proposes response timescale as the lever that composes an agency position.
4. **Abstract**: Revised to reflect the agency-spectrum framing.

**Changes made**:
- Section 1, paragraphs 3-5: Complete rewrite
- Section 6.1, paragraphs 1-2: Complete rewrite
- Section 6.4: New synthesis paragraph
- Abstract: Revised
- 2 references newly load-bearing here: Edmonds (2018), Schiphorst (2021)

> See revised manuscript Section 1; Section 6.1; Section 6.4; Abstract

---

### Response to Reviewer 3 (Art-Science Critic)

#### Comment R3-1: Reflection Paragraph Length (Minor)

**Reviewer comment**: "Several Reflection paragraphs exceed 200 words; shorter paragraphs improve readability."

**Author response**: We restructured 11 of 14 Reflection paragraphs to 150-190 words. We respectfully retained three paragraphs at 210-220 words (Section 6.1 para 2, Section 6.3 para 4, Section 6.4 para 1) where splitting would disrupt sustained arguments integrating the work, the session logs, and precedent. The 200-word figure is a readability guideline, not a venue rule, and we believe the marginal excess is justified. We documented this as a deliberate limitation.

**Changes made**:
- Section 6 throughout: 11 paragraphs restructured to 150-190 words
- Section 6 limitations: Added acknowledgment of retained paragraph lengths

> See revised manuscript Section 6

---

### Summary of Changes

- Total comments addressed: 5
- Resolved: 4
- Deliberate Limitation: 1
- Word count change: +900 words (5,400 to 6,300)
- New references added: 4
- New figures/tables added: 0 (1 figure caption corrected with image courtesy)

We believe these revisions have substantially strengthened the paper — particularly the reframing prompted by the Devil's Advocate, which we consider the single most valuable piece of feedback. We look forward to your further evaluation.

Sincerely,

Author: [Example Artist]
Contact Email: [email]
Revision Date: 2026-03-06

---

## Stage 3': Re-Review Verdict

```
Entering Stage 3' (RE-REVIEW) -- Loop 1/2

Loading art-reviewer SKILL.md (re-review mode)...
Passing Revised Draft + Response to Reviewers + original Revision Roadmap...
Jury re-reviewing revision quality...
```

### Revision Response Verification

| # | Original Issue | Response Adequate? | Detail |
|---|---------------|:------------------:|--------|
| 1 | Reception claims unanchored | Adequate | Replaced with observable evidence anchored to venue/date: gesture-refinement pattern across 45 logged sessions, recorded dwell times, 12 exit conversations. Reception language down-scoped throughout. |
| 2 | Missing surrender + consent positioning | Adequate | New Section 3.3 (600 words) engages both strands and connects them to the work's negotiation-zone placement. Four new references, all genre-appropriate. Dialogue extended in Section 6.3. |
| 3 | "Control is the only valid model" strawman (DA-CRITICAL) | Adequate | Complete reframing from control/no-control binary to a command-negotiation-surrender spectrum. The new framing identifies a genuine question (where the work places the audience) and makes a substantive contribution (timescale as the agency lever). The DA-CRITICAL item is fully resolved. |
| 4 | "real-time"/"autonomous" unanchored; image courtesy | Adequate | "real-time" (~80 ms, measured) and "autonomous" (no operator/timeline) anchored; Figure 3 image-courtesy line added. |
| 5 | Reflection paragraph length | Adequate (DELIBERATE_LIMITATION) | 11/14 paragraphs restructured. Three retained at 210-220 words with documented justification. Reasonable editorial decision; does not compromise quality. |

### Five-Dimension Scores (Post-Revision)

| Dimension | Weight | Pre-Revision | Post-Revision | Change |
|-----------|--------|-------------|--------------|--------|
| Conceptual Originality | 20% | 71.3 | 80.5 | +9.2 |
| Practice-Based Rigor / Realization | 25% | 56.3 | 74.0 | +17.7 |
| Evidence & Reception Anchoring | 25% | 57.0 | 76.5 | +19.5 |
| Argument / Reflection Coherence | 15% | 64.3 | 82.0 | +17.7 |
| Writing & Documentation Quality | 15% | 74.8 | 79.3 | +4.5 |
| **Weighted Total** | -- | **62.4** | **78.0** | **+15.6** |

Per the quality rubrics: 65-79 = Minor Revision, >= 80 = Accept. Score of 78.0 is in the Minor Revision range, but all Major items and the DA-CRITICAL item are fully resolved.

### DA-CRITICAL Before/After Assessment

| Aspect | Before Revision | After Revision |
|--------|----------------|---------------|
| Core framing | "Control is the only valid model" — strawman binary | "Agency spectrum" (command-negotiation-surrender) — genuine question |
| Central question | Must audiences feel in control? (trivially answered) | Where on the spectrum does a work place the audience, and how is that composed? (substantive) |
| Conceptual depth | Classic interactive-art theory only | + surrender model + consent critique (positioned, not piled) |
| Reflection contribution | "Control is unnecessary" (obvious) | Response timescale as the lever that composes an agency position (novel) |
| DA verdict | CRITICAL — undermines entire contribution | Resolved — paper now addresses a genuine question |

### Editorial Synthesizer Assessment

```
All jury members concur: revision quality is strong.

Key improvements:
1. The DA-CRITICAL strawman reframing is the most significant improvement.
   The paper now makes a substantive contribution rather than arguing
   against a position no one defends.
2. The re-anchoring of reception claims to observable evidence at a named
   venue resolves the integrity concern raised by R1.
3. The surrender/consent positioning adds conceptual depth that was missing.
4. The DELIBERATE_LIMITATION on paragraph length is reasonable and
   well-documented.

Residual suggestions (non-blocking):
S1: Consider adding a figure depicting the "agency spectrum"
    concept to strengthen the contribution visually.
S2: The transition between Section 3.2 and the new Section 3.3 could
    be smoother — currently the reader meets the surrender model without
    a clear signpost for why it appears at that point.

Editorial Decision: Accept with Minor Edits
  - The two residual suggestions are editorial improvements,
    not substantive concerns.
  - Score moved from 62.4 (Major Revision) to 78.0 (upper Minor Revision).
  - All SERIOUS/CRITICAL items resolved.
  - Paper is cleared for finalization after minor edits.
```

---

## Pipeline Continues: Stage 3' --> Stage 4.5

```
━━━ MANDATORY CHECKPOINT: Stage 3' RE-REVIEW ━━━

Review Result: Accept with Minor Edits

Revision assessment:
  - 5/5 items addressed (4 RESOLVED, 1 DELIBERATE_LIMITATION)
  - DA-CRITICAL item fully resolved (strawman → agency spectrum)
  - Weighted score: 62.4 → 78.0 (+15.6 points)
  - 2 residual suggestions (non-blocking, can be addressed in finalization)

Since the decision is Accept (not Major Revision), the paper
proceeds directly to Stage 4.5 (FINAL INTEGRITY) — skipping Stage 4'.

The 2 minor editorial suggestions will be handled during
Stage 5 (FINALIZE).

Continue to Stage 4.5?

Progress: [v]Inquiry -> [v]Writing -> [v]Integrity -> [v]Review
       -> [v]Revision -> [v]Re-review -> [..]Final Integrity
       -> [ ]Finalization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**User**: Continue!

---

## Key Takeaways

### 1. DA-CRITICAL Findings Drive the Most Valuable Revisions

The Devil's Advocate challenge — that the paper's core premise was a strawman — prompted the most significant improvement. The original framing ("control is the only valid model") was a binary that no one defends. The revised framing ("agency spectrum") introduces a genuine contribution. This is precisely the value of the DA-CRITICAL designation: it forces makers to confront foundational weaknesses rather than polishing surface-level issues.

### 2. Reception Anchoring Is an Art-Genre Integrity Gate

Item 1 shows the art-specific integrity move: reception claims must be anchored to a named venue/date plus an observable detail, never "audiences were captivated." Re-anchoring to logged sessions, dwell times, and exit conversations turned a hope into documentation — and the artwork plus its situated reception remain the primary evidence.

### 3. DELIBERATE_LIMITATION Is a Legitimate Status

Not every reviewer suggestion must be accepted. Item 5 (paragraph length) was acknowledged as a deliberate choice with documented justification. The key is that DELIBERATE_LIMITATION requires (a) a principled reason (argumentative coherence > readability guideline), (b) an acknowledgment in the Limitations section, and (c) a transparent explanation in the Response to Reviewers. The re-reviewers accepted this status as reasonable.

### 4. Response to Reviewers Uses R-A-C Format

Each response follows the Reviewer comment - Author response - Changes made structure. For accepted feedback, the response explains *what was done* and *why*. For the DELIBERATE_LIMITATION, the response explains *what was done* (11/14 paragraphs restructured), *what was not done* (3 paragraphs retained), and *why* (argumentative coherence justification).

### 5. Score Improvements Track to Specific Revisions

The quality rubrics score increased from 62.4 (Major Revision threshold) to 78.0 (upper Minor Revision). The largest gains were in Practice-Based Rigor / Realization (+17.7, driven by the anchored technical claims and positioning) and Evidence & Reception Anchoring (+19.5, driven by re-anchored reception). Conceptual Originality gained +9.2 primarily from the DA-CRITICAL reframing.

### 6. The Revision Tracking Template Provides Accountability

Each of the 5 items has a clear status (RESOLVED or DELIBERATE_LIMITATION), a specific location of changes, and a resolution summary. The re-review process uses this tracking table as its checklist, verifying each item against the Response to Reviewers and the actual manuscript changes. This creates a verifiable audit trail.
