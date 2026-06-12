---
scenario: Revising an art paper after receiving jury review comments
mode: revision
agents_used:
  - formatter_agent
  - citation_compliance_agent
  - peer_reviewer_agent
input: Original jury review comments (3 major + 4 minor)
output: Revision comparison table + Response to Reviewers letter
---

# Revision Mode Example: Responding to Art-Paper Jury Comments

## Scenario

The user has a completed practice-based art paper titled "Tide Memory: An Autonomous Generative Installation that Composes from Visitors' Breath," which has received jury comments from a SIGGRAPH Asia Art Papers review (3 major + 4 minor). The user employs art-paper's revision mode for systematic revision. This example demonstrates the complete workflow from comment parsing, ACM citation correction, review verification, to the Response to Reviewers letter.

> **AI-generated demonstration.** The artist, work, venue, jurors, and citations are fictional.

---

## Original Jury Review Comments

### Reviewer 1 (Practitioner-Researcher)

**Major Comments:**

**M1.** There are serious concerns about reception inflation. The Reflection section claims that "audiences were profoundly moved and experienced a deep sense of calm." This is not anchored to any observable evidence — it reads as the artist's wish rather than as documentation. Either anchor reception claims to what was actually observed or recorded (named venue/date plus an observable detail) or down-scope them. In a practice-based paper the artwork and its situated reception are the primary evidence, and unanchored reception claims weaken the whole contribution.

**M2.** The conceptual positioning is thin and dated. Of the precedent works and texts cited, most predate 2018, and the paper does not engage recent discourse on biosignal and somatic installation, particularly the critical writing on consent and the sensed body from the past two years. Several obvious precedents (the *Pulse* lineage; recent room-scale aggregate works) are missing. Strengthen positioning against current precedent — this is positioning, not a literature wall.

**M3.** The realization account is under-specified for its technical claims. The paper asserts the system is "fully autonomous" and that "no individual's breath can be identified," but the description of the sensing-to-composition pipeline is too vague to make either claim plausible. Clarify the aggregation method and the timescale, and define "autonomous" precisely, so a reader could in principle assess the claims.

**Minor Comments:**

**m1.** The abstract's third sentence — "the work was widely acclaimed" — is both vague and an unanchored reception claim; replace with what was actually shown/observed.

**m2.** Reference formatting is inconsistent with the ACM Reference Format: some entries use author-year inline formatting by hand, and one artwork citation invents a DOI. Citation #9 (an exhibited work) should use venue+date as its locator, not a fabricated DOI.

**m3.** Figure 2 (the breath→parameter mapping diagram) has axis labels too small to read; enlarge to 10pt or above. Figure 3 is missing a caption and an image-courtesy line.

**m4.** The last paragraph of the Realization section contains "as shown in Figure X," which appears to be a placeholder left in by mistake.

---

### Reviewer 2 (Art-Science Critic)

**Major Comments:**

(No additional major comments, but the reviewer concurs with Reviewer 1's M1 and M3.)

**Minor Comments:**

(Concurs with Reviewer 1's minor comments, and adds:)

**m5 (R2).** The Introduction should state the contribution more clearly. The transition from the encounter description to "what this paper adds to art+technology discourse" is currently too abrupt.

**m6 (R2).** The collaboration credit is unclear. The Realization section says "the system was built," but the acknowledgements thank an audio engineer for the aggregation method. If a collaborator authored a substantive part of the work, name the contribution in the body and credit it on the work, not only in the acknowledgements.

**m7 (R2).** Add an AI-usage disclosure with the two channels the venue requires: AI used to make the artwork vs. AI used to write the paper. The current draft has no disclosure section.

---

## formatter_agent Parses Revision Comments

### Revision Comment Classification

**Parsing Result:** 3 Major + 7 Minor, totaling 10 revision items.

| No. | Type | Affected Section | Revision Scope | Estimated Workload |
|-----|------|-----------------|----------------|-------------------|
| M1 | Major | Reflection, Abstract | Re-anchor or down-scope reception claims | High |
| M2 | Major | Conceptual Framework | Strengthen positioning against current precedent | Medium-High |
| M3 | Major | Realization | Specify aggregation/timescale; define "autonomous" | Medium |
| m1 | Minor | Abstract | Replace unanchored reception claim | Low |
| m2 | Minor | References | ACM Reference Format fixes; artwork locator (venue+date) | Low |
| m3 | Minor | Figures | Fix figure legibility, caption, image courtesy | Low |
| m4 | Minor | Realization | Remove placeholder "Figure X" | Low |
| m5 | Minor | Introduction | Sharpen contribution statement | Low-Medium |
| m6 | Minor | The Work / Realization | Name and credit collaborator's contribution | Medium |
| m7 | Minor | Disclosure | Add two-channel AI-usage disclosure | Low |

### Recommended Revision Strategy

The formatter_agent recommends the following revision order:

1. Address M1 (reception anchoring) first, as it affects the Reflection and the Abstract
2. Then address M3 (realization specificity), as the precise pipeline description supports both the "autonomous" and "non-attributable" claims
3. Then address M2 (positioning), as added precedent may require small updates to the Reflection's dialogue
4. Finally, batch-process all minor comments

---

## citation_compliance_agent Corrects Citation Issues

### Citation Audit Report

**Audit Scope:** Full-text citations against the ACM Reference Format (default for art-paper / SIGGRAPH Asia). The genre-neutral L3 locator gate is unchanged.

**Issues Found:**

| Issue | Count | Severity |
|-------|-------|----------|
| Hand-formatted inline citations (should use class-driven \cite) | 6 instances | Medium |
| Fabricated DOI on an artwork citation | 1 instance | High |
| Missing L3 locator anchor after a citation | 2 instances | High |
| Artwork cited without venue+date locator | 3 instances | Medium |
| Missing image-courtesy line on a reproduced figure | 1 instance | Medium |

### Specific Corrections

**Correction 1: Use class-driven citations, not hand formatting (addressing m2)**

Before correction:
```
(Costello and Edmonds, 2019) argue that interactive art...
Schiphorst, T. (2021)'s somatic framing shows...
According to Lozano-Hemmer (Pulse) ...
```

After correction:
```
Costello and Edmonds [2019] argue that interactive art...
Schiphorst's somatic framing [Schiphorst 2021] shows...
The Pulse lineage [Lozano-Hemmer 2007–2018] established heartbeat as material...
```

Rule: do not hand-format the rendered citation. The acmart class option drives numeric vs. author-year; use \cite/\citet/\citep and let the class render it.

**Correction 2: Replace fabricated DOI on an artwork (addressing m2)**

Before correction:
```
Rafael Lozano-Hemmer. 2007. Pulse Room. https://doi.org/10.1145/0000000
```

After correction:
```
Rafael Lozano-Hemmer. 2007–2018. Pulse (series). Biometric installation.
    Exhibited at [Fictional Venue], [City]. https://www.example.org/pulse
```

Rule: do NOT invent DOIs for artworks. Cite the work like a source — artist, title, year, medium, exhibition venue — and use venue+date (and/or a URL with access date) as the locator the L3 gate checks.

**Correction 3: Restore missing L3 locator anchors**

Found two citations emitted with no locator anchor. The formatter hard-gate-refuses a citation with no locator, so each `<!--ref:slug-->` must carry a locator (quote / page / section / paragraph / venue+date / none-with-reason).

Before correction:
```
The control paradigm has been challenged for somatic work <!--ref:author-k-2021-->.
```

After correction:
```
The control paradigm has been challenged for somatic work
<!--ref:author-k-2021 locator="quote: 'opacity as a value'"-->.
```

**Correction 4: Add venue+date locator to artwork citations (addressing m2)**

For the three artworks cited without a locator, the venue+date serves as the locator (the artwork analog of a page number).

Before correction:
```
A room-scale aggregate precedent <!--ref:author-l-2023-->.
```

After correction:
```
A room-scale aggregate precedent
<!--ref:author-l-2023 locator="venue: [Fictional] Media Art Biennale, 2023"-->.
```

### New References Added (addressing M2)

In conjunction with M2's positioning update, the citation_compliance_agent verifies ACM Reference Format compliance of newly added references:

```
Author M. 2024. Disclosure design in ambient sensing installation. In
    Proceedings of the [Fictional] Conference on Tangible, Embedded, and
    Embodied Interaction. https://doi.org/10.1145/xxxxxxx

Author N. 2023. Consent and the sensed body: ethics of biosignal art.
    [Fictional] Journal of Media Art 15, 1 (2023), 22–44.
    https://doi.org/10.1162/xxxxxxx

Author L. 2023. Murmur Room. Room-scale aggregate sound installation.
    Exhibited at [Fictional] Media Art Biennale, [City].
    https://www.example.org/murmur-room

Thecla Schiphorst. 2021. Somaesthetics and felt interaction in media art.
    Leonardo 54, 2 (2021), 134–141. https://doi.org/10.1162/xxxxxxx
```

Format audit result: All 4 newly added references comply with the ACM Reference Format (artwork entry uses venue+date locator; no fabricated DOI).

---

## peer_reviewer_agent Reviews the Revised Version

### Revision Adequacy Assessment

| No. | Original Comment | Revision Adequate? | Remarks |
|-----|-----------------|:------------------:|---------|
| M1 | Reception inflation | Adequate | Unanchored "profoundly moved" replaced with observable field-note evidence (performing→settling shift across 60 logged sessions; 18 exit conversations incl. 3 uneasy visitors) |
| M2 | Positioning thin/dated | Adequate | 4 recent precedents/texts added (incl. consent-and-sensed-body and room-scale aggregate work); positioning sharpened, not turned into a wall |
| M3 | Realization under-specified | Adequate | Aggregation pipeline and 90-second window now described; "autonomous" scoped to "no operator, no fixed timeline, live generation" |
| m1 | Abstract reception claim | Adequate | "widely acclaimed" replaced with what was shown/observed |
| m2 | ACM citation issues | Adequate | Inline hand-formatting removed; artwork DOI removed and replaced with venue+date locator; L3 anchors restored |
| m3 | Figure issues | Adequate | Labels enlarged; caption and image-courtesy line added |
| m4 | Placeholder "Figure X" | Adequate | Corrected to "Figure 2" |
| m5 | Contribution unclear | Adequate | Contribution statement added to the Introduction |
| m6 | Collaboration credit | Adequate | Engineer's aggregation contribution named in the body and co-credited on the work, not only in acknowledgements |
| m7 | Missing AI disclosure | Adequate | Two-channel disclosure added (AI-to-make vs. AI-to-write) |

### Post-Revision Five-Dimension Scores

> Art-genre dimensions; weights are illustrative and configured by `field_analyst_agent`.

| Dimension | Before Revision | After Revision | Change |
|-----------|----------------|----------------|--------|
| Conceptual Originality (20%) | 3.5 | 3.6 | +0.1 |
| Practice-Based Rigor / Realization (25%) | 2.6 | 3.6 | +1.0 |
| Evidence & Reception Anchoring (25%) | 2.8 | 3.8 | +1.0 |
| Argument / Reflection Coherence (15%) | 3.4 | 3.9 | +0.5 |
| Writing & Documentation Quality (15%) | 3.9 | 4.1 | +0.2 |
| **Weighted Total** | **3.18** | **3.78** | **+0.60** |

### Revision Verdict

**Verdict: ACCEPT with Minor Revision**

The paper moved from Major Revision (3.18) before revision to the Minor Revision/Accept boundary (3.78) after revision. The remaining suggestion (a further sentence distinguishing "autonomous" from "generative" in M3) can be addressed during finalization and does not affect the acceptance decision.

---

## Revision Results — Revision Comparison Table

### Major Revisions

| Reviewer Comment | Before Revision | After Revision | Location |
|------------------|----------------|----------------|-------|
| M1: Reception inflation | "Audiences were profoundly moved and experienced a deep sense of calm." | Replaced with observable evidence: "Across 60 logged gallery sessions at the [Example] Media Art Biennale (2025), field notes recorded a recurring shift from a performing stance (waving, testing for a gesture mapping) to a settling stance (standing still, slowing the breath, several visitors lying down) once visitors became aware the work tracked breathing. In 18 exit conversations, several visitors valued discovering this on exit; three reported unease at the work sensing an intimate, involuntary act." Reception claims now anchored to venue/date + observable detail; the unease is kept, not minimized. | Reflection §6.2; Abstract |
| M2: Positioning thin/dated | Most precedents pre-2018; *Pulse* lineage and recent consent discourse missing | Added 4 recent sources (Author M 2024 on disclosure design; Author N 2023 on consent and the sensed body; Author L 2023 room-scale aggregate work; Schiphorst 2021 somatic framing). Positioning sharpened against the *Pulse* lineage and the control-vs-surrender debate; kept lean (positioning, not a wall). | Conceptual Framework §3 |
| M3: Realization under-specified | "fully autonomous"; "no individual's breath can be identified" with vague pipeline | Specified the pipeline (12 contact mics → per-channel band-pass + onset detection → pooled into two room-level parameters on a 90-second window → generative audio/light mapping). Defined "autonomous" precisely: at exhibition time there is no operator and no fixed timeline; the work generates continuously from the live room signal. Grounded "non-attributable" in the room-level pooling and the 90s window. | Realization §5.2 |

### Minor Revisions

| Reviewer Comment | Before Revision | After Revision | Location |
|------------------|----------------|----------------|-------|
| m1: Abstract reception claim | "the work was widely acclaimed" | "the work was exhibited for six weeks at the [Example] Media Art Biennale (2025); observation of 60 logged sessions and 18 visitor conversations indicated a shift from performing to settling once visitors learned breath was sensed" | Abstract |
| m2: ACM citation issues | Hand-formatted inline citations; one fabricated artwork DOI; 2 missing L3 anchors | All citations class-driven; artwork DOI removed and replaced with venue+date locator; L3 anchors restored on all citations | Throughout |
| m3: Figure issues | Figure 2 labels 8pt; Figure 3 no caption/courtesy | Labels enlarged to 11pt; Figure 3 caption added ("Breath→density/agitation mapping") with image-courtesy line | Figs. 2–3 |
| m4: Placeholder | "as shown in Figure X" | "as shown in Figure 2" | Realization §5 |
| m5: Contribution unclear | Introduction jumped from the encounter to the work description | Added a contribution statement: "This paper contributes the work, an account of its autonomous generative system, and a situated reading of embodied co-authorship as surrender, reported from an actual exhibition rather than a lab study." | Introduction §1.4 |
| m6: Collaboration credit | "the system was built" (passive, uncredited) | "The breath-aggregation signal processing was developed in collaboration with [Example Collaborator], audio engineer, whose contribution to the aggregation method is co-credited on the work's exhibition label." Named in the body, not only the acknowledgements. | The Work §3.3 |
| m7: AI disclosure | None | Added a two-channel AI-usage disclosure: (a) AI to make the artwork — parametric synthesis only, no ML generation, breath-aggregation method authored by artist+collaborator; (b) AI to write the paper — AI-assisted search framing, structuring, copy-editing; all artistic decisions and interpretation directed and verified by the author. | Disclosure section |

---

## Response to Reviewers

---

**Submission No.:** SA-ART-2026-0142

**Title:** Tide Memory: An Autonomous Generative Installation that Composes from Visitors' Breath, and What Its Exhibition Revealed about Embodied Co-Authorship

**Revision Date:** 2026-02-26

---

Dear Jury and Reviewers,

Thank you for your thorough and constructive comments. We respond to each item below. All revisions are marked in blue in the revised manuscript.

---

### Response to Reviewer 1 (Practitioner-Researcher)

**M1: Reception Inflation**

Thank you for this essential comment. We agree that the original Reflection over-claimed reception with unanchored language. We have:

1. Removed "audiences were profoundly moved and experienced a deep sense of calm."
2. Replaced it with observable, anchored evidence: the performing→settling shift recorded across 60 logged sessions at the [Example] Media Art Biennale (2025), and the content of 18 exit conversations.
3. Kept, rather than minimized, the unease reported by three visitors, since it grounds our second finding about disclosure timing.

> See revised manuscript Reflection §6.2; Abstract.

**M2: Positioning Thin and Dated**

Thank you. We have strengthened the conceptual positioning:

1. Added 4 recent precedents/texts, including the consent-and-sensed-body discourse and a room-scale aggregate work.
2. Sharpened the positioning against the *Pulse* lineage and the control-vs-surrender debate, while keeping it lean (positioning, not an exhaustive review).

> See revised manuscript Conceptual Framework §3.

**M3: Realization Under-Specified**

Thank you for requesting precision. We have:

1. Specified the sensing→aggregation→composition pipeline, including the 90-second moving window.
2. Defined "autonomous" precisely (no operator, no fixed timeline, continuous live generation), so it is not read as an inflated capability claim.
3. Grounded "no individual's breath can be identified" in the room-level pooling across 12 channels and the 90-second window.

> See revised manuscript Realization §5.2.

**m1–m4:** All minor comments addressed individually; see the revision comparison table.

---

### Response to Reviewer 2 (Art-Science Critic)

**m5: Contribution Statement**

We added a contribution statement to the Introduction (§1.4) making explicit what the paper adds: the work, an account of its generative system, and a situated reading of co-authorship-as-surrender.

> See revised manuscript Introduction §1.4.

**m6: Collaboration Credit**

Thank you for catching this. We have named the audio engineer's contribution to the breath-aggregation method in the body (The Work §3.3) and co-credited it on the work's exhibition label, rather than relegating it to the acknowledgements.

> See revised manuscript The Work §3.3.

**m7: AI-Usage Disclosure**

We added a two-channel AI-usage disclosure distinguishing AI used to make the artwork (parametric synthesis only; no ML generation) from AI used to write the paper (search framing, structuring, copy-editing), per the venue policy. We note in the text that the exact disclosure requirements should be verified against the current SIGGRAPH Asia Art Papers CFP.

> See revised manuscript Disclosure section.

---

We believe these revisions have substantially strengthened the paper — particularly the re-anchoring of reception claims, which we consider the single most valuable piece of feedback. We look forward to your further evaluation.

Sincerely,

Author: [Example Artist]
Contact Email: [email]
Revision Date: 2026-02-26
