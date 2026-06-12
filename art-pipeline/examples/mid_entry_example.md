# Example: Mid-Entry into Pipeline

## Scenario Description

**User type**: Practicing media artist, experienced in exhibiting but new to writing art papers
**Scenario**: Already drafted an English art paper about an existing artwork, wants a simulated jury review before submission
**Goal**: Review --> Revision --> Format conversion (acmart LaTeX)
**Language**: English (paper is in English; conversation with orchestrator in English)

---

## User Input

```
I've already written an English art paper titled "Tidal Bodies: A Real-Time
Generative Installation Responding to Coastal Sensor Data," approximately
7,000 words, about an interactive installation I exhibited last year.
I'd like a simulated jury review before submitting to SIGGRAPH Asia Art Papers.
```

---

## Pipeline Execution Log

### Orchestrator: Mid-Entry Detection

```
Detection results:
- Materials: Complete English art-paper draft (7,000 words)
- Goal: Simulated jury review + revision + submission preparation
- Entry point: Stage 2.5 (INTEGRITY) -- then Stage 3 (REVIEW)
- User type: Experienced artist, new to art-paper writing

Detected that you have a complete art paper. Note: even a mid-entry draft
must pass Stage 2.5 (INTEGRITY) before jury review -- this verifies citations
and artwork/realization claims and cannot be skipped.

Before starting, let me confirm a few things:
1. What's the paper structure? (Practice-Based Art Paper / IMRaD art-science hybrid / other)
2. What review mode would you like?
   - full: Complete 5-person jury (Chair + curator + practitioner-researcher
     + art-science critic + Devil's Advocate)
   - quick: Chair quick assessment (15-minute version)
   - guided: Socratic guided review (interactive dialogue with the artist)
3. Which track / venue are you targeting? (verify against the current CFP)
4. Will you need revision and format conversion (acmart) after the review?

If you later want to revise based on jury comments, I'll automatically guide you to Stage 4.
```

**User**: Practice-Based Art Paper structure. I'd like a quick review first to see if there are any big-picture issues. Targeting SIGGRAPH Asia Art Papers. Will decide about revision after the review.

### Orchestrator: Confirm Configuration

```
Got it. Pipeline configuration:

  Stage 1 INQUIRY     [--] Skipped (you already have the conceptual foundation)
  Stage 2 WRITE       [--] Skipped (you already have a complete paper)
  Stage 2.5 INTEGRITY [..] Mandatory -- citations + artwork/realization claims
  Stage 3 REVIEW:     quick -- Chair quick assessment first, checking the big picture
  Stage 4 REVISE:     TBD -- based on Stage 3 results
  Stage 5 FINALIZE:   TBD -- when needed

Start with Stage 2.5 (INTEGRITY), then Stage 3 (REVIEW) quick mode?

Progress: [--]Inquiry -> [--]Writing -> [..]Integrity -> [ ]Review -> [ ]Revision -> [ ]Finalization
```

**User**: Start.

---

### Stage 2.5: INTEGRITY (pre-review)

```
Entering Stage 2.5 (INTEGRITY) -- Mode 1 (Pre-Review)

Loading integrity_verification_agent...
Verifying references (ACM Reference Format) + artwork/realization claims...
```

**Integrity result (summary):**
```
Verdict: PASS WITH NOTES

- References: 12/12 verified (precedent works + theory, ACM Reference Format;
  artwork/exhibition entries carry venue+date in lieu of DOI)
- Artwork/realization claims: 1 MINOR note
  - "real-time" capability claim has a realization anchor (sensor pipeline
    described in Section 3) -- acceptable, but consider stating latency.
- No reception inflation, no unsupported precedence claims detected.

Cleared for jury review.
```

---

### Stage 3: REVIEW (quick mode)

```
Entering Stage 3 (REVIEW) -- using art-reviewer quick mode

Loading art-reviewer SKILL.md...
Receiving user-provided paper draft...
field_analyst_agent analyzing art subfield + SIGGRAPH track...
chair_agent executing quick assessment...
```

**Field Analysis (quick version):**
```
Art subfield: Generative / interactive installation art (data-driven)
Practice mode: Practice-based (the installation is the primary evidence)
Target track: SIGGRAPH Asia Art Papers (verify against current CFP)

Chair Persona:
  Art Papers Chair
  Specialization: Media-art curation, computational/generative practice
```

**Chair Quick Assessment:**

```
Overall: Promising but needs work (Minor-to-Major Revision range)

Key Strengths (top 3):
1. Strong conceptual provocation -- coastal sensor data as a "tidal body"
   is a fresh framing for environmental media art
2. Clear realization account -- the sensor-to-projection pipeline is
   well-documented and the "real-time" claim is anchored
3. Compelling documentation -- installation views and video stills
   support the work as primary evidence

Key Concerns (top 3):
C1: [CRITICAL] Lineage / precedent positioning is thin. The paper does
    not situate the work against prior data-driven installation art
    (e.g., environmental-sensing and generative-projection lineages).
    A practitioner-researcher juror will name precedents you omit.
C2: [MAJOR] Reception account is under-anchored. "Visitors lingered and
    seemed moved" needs an observable anchor (named venue/date +
    observable detail), not an affective generalization.
C3: [MAJOR] The relationship between concept and realization is asserted
    but not reflected on -- how does the technical choice (real-time
    response) carry the conceptual claim (tidal embodiment)?

Quick Verdict: Major Revision
  Before full submission, address C1-C3.
  Estimated revision effort: 2-3 weeks.
```

**Stage 3 Deliverables:**
- Chair Quick Assessment Report
- 3 key issues list (priority sorted)

---

### Orchestrator: Transition Recommendation

```
Stage 3 (REVIEW) quick mode Complete!

Review result: Major Revision direction
  C1: [CRITICAL] Thin lineage / precedent positioning
  C2: [MAJOR] Reception claim lacks observable anchor (reception inflation risk)
  C3: [MAJOR] Concept-realization relationship not reflected on

This is the quick review result. You have several options:

  a) Proceed directly to Stage 4 (REVISE) to address these 3 issues
  b) Upgrade to full review (complete 5-person jury),
     to see if there are other issues
  c) Revise on your own first, come back when done

My recommendation: Since you're targeting SIGGRAPH Asia Art Papers,
fix C1-C3 first, then do a full jury review to ensure quality.

Which do you choose?
```

**User**: Fix C1-C3 first, then do full review.

### Orchestrator: Update Configuration

```
OK, updating pipeline:

  Stage 3 REVIEW (quick):  [v] Completed
  Stage 4 REVISE:          [..] Next -- fix C1-C3
  Stage 3' RE-REVIEW:      full mode -- full jury review after revision
  Stage 5 FINALIZE:        TBD

Start Stage 4 (REVISE)?

Progress: [--]Inquiry -> [--]Writing -> [v]Integrity -> [v]Review -> [..]Revision -> [ ]Re-review -> [ ]Finalization
```

**User**: Start revision.

---

### Stage 4: REVISE (revision mode, Round 1)

```
Entering Stage 4 (REVISE) -- using art-paper revision mode

Loading art-paper SKILL.md (revision mode)...
Passing Paper Draft + Quick Assessment Report...
```

**Revision Progress Tracking:**
```
C1: [v] Added Lineage & Positioning section (Section 2)
    - Situated the work in data-driven / environmental-sensing
      installation lineages
    - Distinguished the contribution from prior generative-projection works
    - Added 6 precedent citations (works + theory, ACM Reference Format)

C2: [v] Re-anchored the reception account (Section 5)
    - Replaced "visitors seemed moved" with an observable anchor:
      named venue + dates + observed behavior (dwell time, return visits)
    - Removed affective generalization; kept honest hedging
      ("in this installation, for these visitors")

C3: [v] Added Concept-Realization Reflection (Section 4)
    - Articulated how real-time response enacts "tidal embodiment"
    - Reflected on what the technical choice does and does not carry
    - Linked realization decisions back to the provocation
```

**Stage 4 Deliverables:**
- Revised Draft (9,200 words, 2,200 words more than original)
- Response to Jurors (R-A-C format, 3 items all addressed)

---

### Orchestrator: Stage 4 --> 3' Transition

```
Stage 4 (REVISE) Complete!

Revision results:
- 3/3 issues all addressed
- Paper expanded from 7,000 to 9,200 words
- Added Lineage section, re-anchored reception, added concept-realization reflection
- Added 6 new precedent citations

Next step is Stage 3' (RE-REVIEW) -- this time using full mode.
The 5-person jury will do a complete review of the revised version.
This is revision cycle 1 (max 2 cycles).

Submit for full review?

Progress: [--]Inquiry -> [--]Writing -> [v]Integrity -> [v]Review -> [v]Revision -> [..]Re-review -> [ ]Finalization
```

**User**: Submit.

---

### Stage 3': RE-REVIEW (full mode, Loop 1)

```
Entering Stage 3' (RE-REVIEW) -- full mode, Loop 1/2

Loading art-reviewer SKILL.md (full mode)...
Passing Revised Draft + Response to Jurors...
field_analyst_agent re-analyzing...
```

**Jury Configuration:**
```
Chair:                  Art Papers Chair
                        Media-art curation, computational/generative practice
Curator:                Exhibition curator
                        Installation art, environmental/data-driven media
Practitioner-Researcher: Generative-art practitioner-researcher
                        Real-time systems, sensor-driven work, practice-based methodology
Art-Science Critic:     Art-science critic
                        Environmental data, computational aesthetics, interdisciplinary rigor
Devil's Advocate:       Adversarial reader (precedent + claim scrutiny)
```

**5 Review Reports Compiled:**

```
Chair: Minor Revision
  - C1 response adequate, lineage positioning now credible
  - Recommend updating Abstract to reflect the new lineage + reflection contributions
  - Recommend a short "exhibition context" paragraph for jurors unfamiliar with the venue

Curator: Accept
  - Lineage situating is now thorough and fair to precedents
  - Documentation reads as strong primary evidence
  - Minor: one installation view would benefit from a courtesy/credit line

Practitioner-Researcher: Minor Revision
  - Concept-realization reflection greatly improved
  - Recommend Discussion engage one more time with the real-time/latency tradeoff
  - Minor: Section 2.1 precedent citation Chen (2023) should be Chen (2024)

Art-Science Critic: Accept
  - Reception account now properly anchored, no inflation
  - Environmental-data framing is rigorous and honestly hedged
  - Recommend adding a "limitations of the sensor model" reflection paragraph

Devil's Advocate: Minor Revision
  - "First real-time tidal installation" phrasing in the intro is still too strong;
    either hedge it or cite the precedent survey that supports it
```

**Editorial Decision: Minor Revision (Accept direction)**

```
Required Revisions:
R1: Update Abstract (reflect new contributions)
R2: Hedge or cite the "first real-time tidal installation" precedence claim

Suggested Revisions:
S1: Add exhibition-context paragraph
S2: Add courtesy/credit line to one installation view
S3: Fix Chen (2023) -> Chen (2024) citation year
S4: Add sensor-model limitations reflection paragraph
S5: Discussion engage once more with the latency tradeoff
```

---

### Orchestrator: Quick Revision + FINALIZE

```
Stage 3' (RE-REVIEW) Complete!

Review result: Minor Revision (Accept direction)
  - 2 out of 5 jurors Accept + 3 Minor Revision
  - 2 required items (Abstract update + hedge/cite the precedence claim)
  - 5 suggested modifications

These are all minor changes that can be handled during Stage 5 (FINALIZE).
Or would you prefer a formal Stage 4 revision before another review?

My recommendation: Since all items are minor, proceed directly to Stage 5 and handle them together.

What format do you need?
  a) acmart LaTeX (.tex + .bib) -- for SIGGRAPH Asia Art Papers submission
     (verify the class option against the current CFP)
  b) Other formats

Progress: [--]Inquiry -> [--]Writing -> [v]Integrity -> [v]Review -> [v]Revision -> [v]Re-review -> [..]Finalization
```

**User**: Go straight to finalize, acmart LaTeX format.

---

### Stage 5: FINALIZE (format-convert mode)

```
Entering Stage 5 (FINALIZE) -- format-convert mode

Simultaneously handling minor revision items:
R1: [v] Abstract updated
R2: [v] "first real-time tidal installation" hedged ("among the first...")
S1: [v] Exhibition-context paragraph added
S2: [v] Courtesy/credit line added to installation view
S3: [v] Chen citation year corrected
S4: [v] Sensor-model limitations paragraph added
S5: [v] Latency tradeoff paragraph added to Discussion

formatter_agent executing acmart LaTeX conversion...
- Using ACM acmart class (\documentclass[sigconf]{acmart})
  -- verify class option against current CFP
- \bibliographystyle{ACM-Reference-Format}
- Producing .tex + .bib + figures/
- IRON RULE: PDF compiled from LaTeX via tectonic (never HTML-to-PDF)
```

**Stage 5 Deliverables:**
- `tidal_bodies_installation.tex` (acmart LaTeX main text)
- `references.bib` (BibTeX file; artwork/exhibition entries use venue+date)
- `figures/` (installation views, system diagram, video stills with courtesy lines)
- `tidal_bodies_installation.pdf` (compiled via tectonic)

---

### Orchestrator: Pipeline Complete

```
+=========================================+
|   Creative Pipeline Status              |
+=========================================+
| Work: Tidal Bodies -- Real-Time         |
|       Generative Installation           |
+-----------------------------------------+

  Stage 1 INQUIRY     [--] Skipped
  Stage 2 WRITE       [--] Skipped
  Stage 2.5 INTEGRITY [v] Completed
    Verdict: PASS WITH NOTES
  Stage 3 REVIEW      [v] Completed
    Mode: quick
    Decision: Major Revision (3 items)
  Stage 4 REVISE      [v] Completed
    Round: 1, Addressed: 3/3
  Stage 3' RE-REVIEW  [v] Completed
    Mode: full, Loop: 1/2
    Decision: Minor Revision (Accept)
  Stage 5 FINALIZE    [v] Completed
    Format: acmart LaTeX -> PDF

+-----------------------------------------+
| Materials:                              |
|   [--] Concept & Provocation Brief      |
|        (skipped)                        |
|   [--] Methodology Blueprint (skipped)  |
|   [--] Annotated Bibliography (skipped) |
|   [--] Synthesis (skipped)              |
|   [v] Paper Draft (user-provided)       |
|   [v] Integrity Report (PASS w/ notes)  |
|   [v] Review Reports (quick + full)     |
|   [v] Revision Roadmap                  |
|   [v] Revised Draft (9,500 words)       |
|   [v] Response to Jurors                |
|   [v] Final Paper (acmart PDF)          |
+-----------------------------------------+
| Revision History:                       |
|   Round 1: Major -> 3/3 addressed       |
|   RE-REVIEW: Minor (Accept direction)   |
|   Final minor fixes in FINALIZE         |
+-----------------------------------------+
| Pipeline Complete!                      |
+=========================================+

Your art paper is ready for submission to SIGGRAPH Asia Art Papers.

Final deliverables:
1. tidal_bodies_installation.tex (acmart main text)
2. references.bib (citations; venue+date for artwork/exhibition entries)
3. figures/ (installation views, system diagram, with courtesy lines)
4. tidal_bodies_installation.pdf (compiled from LaTeX via tectonic)

Pre-submission recommendations:
- Confirm the acmart class option, page/length limit, and anonymization
  requirements against the current SIGGRAPH Asia Art Papers CFP
- Confirm image rights / exhibition rights and courtesy lines for all documentation
- Verify the two-channel AI-usage disclosure (AI to MAKE the work vs.
  AI to WRITE the paper) matches current venue policy
```
