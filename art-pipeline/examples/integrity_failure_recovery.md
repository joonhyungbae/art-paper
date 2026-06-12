---
scenario: Stage 2.5 integrity check fails, corrections made, re-verification passes
mode: full pipeline (mid-entry at Stage 2.5)
stages_shown: Stage 2.5 (FAIL -> corrections -> PASS)
demonstrates: How the pipeline handles integrity failures and guides recovery
---

# Integrity Failure Recovery Example

This example shows what happens when Stage 2.5 (Pre-Review Integrity Check) finds serious issues in a practice-based art paper, how they are corrected, and how re-verification works. It demonstrates the pipeline's zero-tolerance integrity gate and the systematic correction workflow defined in `agents/integrity_verification_agent.md`. Note the re-scoped domain: the gate verifies **citations + artwork/realization claims** (reception, precedence/novelty, technical capability, attribution/credit, exhibition record) per `shared/references/art_research_evidence_model.md` §4 — with the **same blocking semantics** as ARS.

## Scenario

An artist submits a paper titled "Mnemonic Field: An Autonomous Generative Installation Reconstructing Collective Memory from Crowd-Sourced Images" for integrity verification. The paper has 18 references (precedent works + theory), makes a set of artwork/realization claims (reception, precedence, technical capability, exhibition record), and is entering the pipeline at Stage 2.5 after completing Stage 2 (WRITE).

**Paper details:**
- Word count: 7,200
- Structure: Practice-Based Art Paper
- Citation format: ACM Reference Format
- References: 18 entries (10 precedent artworks/exhibitions, 5 theory/criticism, 3 technical papers)

---

## Orchestrator: Stage 2 --> 2.5 Transition

```
━━━ Stage 2 (WRITE) Complete ━━━

Metrics:
- Word count: 7,200 (target: 7,000 +/-10%)    [OK]
- References: 18 (min: 12)                     [OK]
- Coverage: all sections drafted                [COMPLETE]

Deliverables:
- Paper Draft (7,200 words, Practice-Based Art Paper)
- Abstract (English, 180 words)
- Reference List (18 entries, ACM Reference Format)

Flagged: None

Next: Stage 2.5 (INTEGRITY) — Mandatory checkpoint.
This stage cannot be skipped. All references and artwork/realization
claims will be verified before the paper proceeds to jury review.

Proceeding to Stage 2.5...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Stage 2.5: Pre-Review Integrity Check (Round 1)

```
Entering Stage 2.5 (INTEGRITY) -- Mode 1 (Pre-Review)

Loading integrity_verification_agent...
Executing: Phase A (Reference Verification) + Phase B (Citation Context, 33% spot-check)
         + Phase C (Artwork/Realization Claim Verification, all) + Phase D (Originality, 33% spot-check)
         + Phase E (Claim Verification, 30% spot-check)
```

### integrity_verification_agent Output

**Mode**: Pre-review (Mode 1)
**Paper**: "Mnemonic Field: An Autonomous Generative Installation Reconstructing Collective Memory from Crowd-Sourced Images"

---

#### Phase A: Reference Existence Verification (18/18 checked)

| # | Reference | Status | Issue |
|---|-----------|--------|-------|
| 5 | Moreau, L. (2023). *Latent Crowds: A Generative Installation*. Exhibited at Galerie Nord, Berlin, 2023. https://doi.org/10.1145/3573012.3573099 | FAIL | DOI resolves to an unrelated SIGGRAPH technical paper on cloth simulation. No exhibition or work by this title at Galerie Nord could be confirmed. Artwork entries should carry venue+date as the locator, not a fabricated DOI. **GHOST REFERENCE** |
| 9 | Hansen, P. (2022). *Embodied Computation in Installation Art*. Leonardo, 55(1), 1-5. | ISSUE | Article exists but published in 2023 (Vol. 56, No. 1), not 2022 (Vol. 55, No. 1). Correct DOI: https://doi.org/10.1162/leon_a_02281 |
| 12 | Ars Electronica. (2022). *Prix Ars Electronica 2021 Catalogue*. Linz: Ars Electronica. | ISSUE | The catalogue exists, but the cited award year is inconsistent: the work referenced in-text won an Honorary Mention in 2020, not 2021. The 2021 catalogue documents a different cohort. |
| 14 | Okonkwo, A., & Reyes, M. (2024). Participatory memory archives in media art. *Digital Creativity*, 35(2), 88-104. https://doi.org/10.1080/14626268.2023.2287711 | FAIL | Article exists but authors are Okonkwo, A., & Reyes, **M. T.** (not M.). Published in 2023 (online first), print edition 2024, Vol. **34**(4), pp. 301-318. DOI resolves to the correct article with the corrected metadata. |
| 17 | Manovich, L. (2020). *Cultural Analytics*. MIT Press. | ISSUE | Correct title is *Cultural Analytics* but the publication year is 2020 with a 2020 hardcover — the cited page range (pp. 45-60) is attributed to a chapter that begins on p. 51 in the verified edition. ACM Reference Format page locator imprecise. |
| -- | Remaining 14/18 references | PASS | All verified against DOI records, publisher pages, museum/festival archives, or institutional listings. Bibliographic and venue+date details match. |

**Phase A Summary**: 18 checked, 14 PASS, 2 FAIL (1 ghost reference, 1 wrong metadata), 2 ISSUE (wrong year/award-year), plus 1 page-locator imprecision

---

#### Phase B: Citation Context Spot-Check (6/18 sampled = 33%)

| # | Citation | Location | Verdict | Detail |
|---|----------|----------|---------|--------|
| B1 | Ref 3 — Whitelaw (2008) | §Lineage, para 2: "Whitelaw (2008) frames generative systems as processes the artist sets in motion rather than fully controls." | PASS | Source faithfully represents the author's argument on generative-systems authorship. |
| B2 | Ref 5 — Moreau (2023) | §Lineage, para 3: "Moreau's *Latent Crowds* (2023) was the first installation to reconstruct collective memory from crowd-sourced images." | FAIL | **Cannot verify** — Ref 5 is a ghost reference (flagged in Phase A). The precedence framing has no verifiable source. |
| B3 | Ref 8 — Bishop (2012) | §Lineage, para 4: "Participatory art shifts the locus of meaning from the object to the relation between visitors and work (Bishop, 2012)." | PASS | Source (Ch. 1) supports this paraphrase of the participatory-art argument. |
| B4 | Ref 12 — Ars Electronica (2022) | §Positioning, para 1: "A comparable work received the Prix Ars Electronica in 2021 (Ars Electronica, 2022)." | ISSUE | Award year mismatch (Honorary Mention was 2020, not 2021). The catalogue citation and the in-text award year disagree. |
| B5 | Ref 14 — Okonkwo & Reyes (2024) | §Lineage, para 5: "Okonkwo and Reyes (2024) show that participatory memory archives consistently produce a shared sense of authorship among contributors." | ISSUE | Source reports this for one case study (one festival cohort), not as a general finding. The paraphrase overgeneralizes a single-context observation. |
| -- | 1 additional citation sampled | §Reflection | PASS | Context accurately reflects source content. |

**Phase B Summary**: 6 sampled, 3 PASS, 1 FAIL (ghost ref context), 2 ISSUE (award-year mismatch / overgeneralized paraphrase)

---

#### Phase C: Artwork & Realization Claim Verification (all claims checked)

Per `shared/references/art_research_evidence_model.md` §4, each artwork/realization claim is classified and checked for an evidence anchor. These block the gate exactly as citation issues do.

| # | Claim in Paper | Class | Verdict | Detail |
|---|---------------|-------|---------|--------|
| C1 | "The installation runs fully autonomously, reconstructing memory images in real time without operator intervention." (§The Work, para 1) | Technical capability | MAJOR_DISTORTION | §Realization describes a pipeline that **requires a nightly human-curated re-seeding step** (described in the build log, para 4). "Fully autonomous" overstates what the documentation supports. The work is generative + scheduled, not autonomous. |
| C2 | "*Mnemonic Field* is the first installation to reconstruct collective memory from crowd-sourced images." (§Lineage, para 3) | Precedence / novelty | UNVERIFIABLE | Rests on Ref 5 (Moreau), a ghost reference, plus no precedent survey. An unsupported "first" must be hedged or anchored to a real survey. WebSearch surfaces at least two prior crowd-sourced-memory installations. |
| C3 | "Visitors were visibly moved, and the room fell into a collective silence." (§Reception, para 2) | Reception inflation | MAJOR_DISTORTION | No observable anchor. "Visibly moved" / "collective silence" is an affective generalization. The documentation (gallery log) records dwell time and a guest-book, which support a narrower, observable statement. |
| C4 | "Shown at the Tri-City Media Biennial, 2024 (Honorary Mention)." (§Exhibition, para 1) | Exhibition record | VERIFIED | Festival archive confirms the showing and the Honorary Mention, 2024. Venue+date locator checks out. |
| C5 | "The work was made in collaboration with sound designer J. Park and the museum fabrication team." (§Acknowledgements) | Attribution / credit | VERIFIED | Internal consistency: the credit line names collaborators and matches the roles described in §The Work. No understatement detected. |

**Phase C Summary**: 5 checked, 2 VERIFIED, 2 MAJOR_DISTORTION (autonomy overclaim + reception inflation), 1 UNVERIFIABLE (precedence)

⚠️ Honest hedges already present in the paper (e.g., "in this installation, for these visitors") were preserved, not flagged — over-claiming is the worse failure.

---

#### Phase D: Originality Check (33% paragraph sample)

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | 12 | 63.2% |
| COMMON_KNOWLEDGE | 4 | 21.1% |
| PARAPHRASE | 3 | 15.8% |
| CLOSE_MATCH | 0 | 0% |
| VERBATIM | 0 | 0% |

**Phase D Summary**: 19/58 paragraphs sampled. No originality concerns detected. All paraphrased passages have proper citations.

---

#### Phase E: Claim Verification (30% spot-check)

The artwork/realization claims C1-C5 above (Phase C) were the priority targets for the claim spot-check; one additional theory-derived factual claim was sampled (a citation-anchored statement about participatory-art reception), verdict VERIFIED.

**Phase E Summary**: 6 claims checked, 3 VERIFIED, 2 MAJOR_DISTORTION, 1 UNVERIFIABLE

---

### Verdict: FAIL

**Reason**: 3 SERIOUS issues + 2 MEDIUM issues detected. PASS requires zero SERIOUS and zero MEDIUM (and zero MAJOR_DISTORTION / UNVERIFIABLE).

**Issues requiring correction (sorted by severity):**

| # | Issue | Severity | Phase | Description |
|---|-------|----------|-------|-------------|
| 1 | Ref 5: Ghost reference (fabricated artwork + fake DOI) | SERIOUS | A | "Moreau, *Latent Crowds* (2023)" could not be confirmed; DOI resolves to an unrelated technical paper. Artwork entries must use venue+date, not a fabricated DOI. The precedence claim built on it is unsupported. |
| 2 | C1: "fully autonomous" technical-capability overclaim | SERIOUS | C/E | Documentation describes a nightly human re-seeding step. "Fully autonomous" overstates the realization. |
| 3 | C2/C3: unsupported "first" + reception inflation | SERIOUS | C/E | "First installation to…" rests on a ghost ref and no survey; "visitors were visibly moved / collective silence" has no observable anchor. |
| 4 | Ref 9: Wrong year and volume | MEDIUM | A | Hansen published 2023 (Vol. 56, No. 1), not 2022 (Vol. 55, No. 1). |
| 5 | Ref 14: Wrong author initials, year, and pagination | MEDIUM | A | Author is Reyes, M. T. (not M.); year should be 2023; Vol. 34(4), pp. 301-318. |
| 6 | Ref 12 / B4: Award-year mismatch | MINOR | A/B | Honorary Mention was 2020, not 2021; in-text and catalogue disagree. |
| 7 | Ref 17: Page-locator imprecision | MINOR | A | Cited chapter begins on p. 51, not p. 45, in the verified edition. |
| 8 | B5: Okonkwo & Reyes paraphrase overgeneralization | MINOR | B | A single-cohort observation is presented as a general finding. |

---

## Correction Process

### Pipeline Orchestrator Response

```
━━━ MANDATORY CHECKPOINT: Stage 2.5 INTEGRITY ━━━

Verdict: ❌ FAIL

Issues found:
  SERIOUS:  3 (must fix to proceed)
  MEDIUM:   2 (must fix to proceed)
  MINOR:    3 (recommended fix)

SERIOUS issues:
  1. Ghost reference — Ref 5 (Moreau, *Latent Crowds*) could not be confirmed; fake DOI
  2. Technical-capability overclaim — "fully autonomous" not supported by the realization
  3. Unsupported precedence ("first…") + reception inflation ("visibly moved")

MEDIUM issues:
  4. Ref 9 — wrong publication year/volume
  5. Ref 14 — wrong author initials, year, and pagination

The pipeline CANNOT proceed to Stage 3 (REVIEW) until
all SERIOUS and MEDIUM issues are resolved.

Options:
  a) "Fix all issues" — I will correct all 8 issues
  b) "Fix critical only" — I will fix the 5 SERIOUS/MEDIUM issues
  c) Review issues one by one — discuss each before fixing
  d) "Pause" — save state and return later
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### User Response

"Fix all issues."

---

### Corrections Applied

#### Issue 1 (SERIOUS): Ghost Reference — Ref 5 Replacement

**Problem**: "Moreau, L. (2023). *Latent Crowds: A Generative Installation*. … https://doi.org/10.1145/3573012.3573099" could not be confirmed; the DOI resolves to an unrelated technical paper, and artwork entries should not carry fabricated DOIs.

**Resolution**: The ghost reference anchored a precedence claim in §Lineage. A verified precedent work was identified via WebSearch and festival archives:

| Aspect | Before | After |
|--------|--------|-------|
| Reference | Moreau, L. (2023). *Latent Crowds: A Generative Installation*. Exhibited at Galerie Nord, Berlin, 2023. https://doi.org/10.1145/3573012.3573099 | Legrady, G. (2005). *Making Visible the Invisible*. Commissioned permanent installation, Seattle Central Library, 2005. (artwork; venue+date locator, no DOI) |
| In-text (§Lineage, para 3) | "Moreau's *Latent Crowds* (2023) was the first installation to reconstruct collective memory from crowd-sourced images." | "Crowd- and archive-driven memory installations have a substantial lineage (e.g., Legrady, *Making Visible the Invisible*, 2005); *Mnemonic Field* extends this lineage by reconstructing memory images in near-real time from contributor uploads." |
| Verification | DOI invalid, work non-existent | Work and venue+date confirmed via institutional archive; widely documented precedent |
| Status | -- | **FIXED** |

#### Issue 2 (SERIOUS): Technical-Capability Overclaim — "fully autonomous"

**Problem**: §The Work claims the installation "runs fully autonomously … without operator intervention," but the build log describes a nightly human-curated re-seeding step.

| Aspect | Before | After |
|--------|--------|-------|
| Text (§The Work, para 1) | "The installation runs fully autonomously, reconstructing memory images in real time without operator intervention." | "During exhibition hours the installation reconstructs memory images in near-real time without operator intervention; the generative model is re-seeded nightly from a human-curated selection of new contributor uploads (see build log)." |
| Rationale | Capability claim narrowed to what the realization actually supports; the human-in-the-loop step is now disclosed |
| Status | -- | **FIXED** |

#### Issue 3 (SERIOUS): Unsupported Precedence + Reception Inflation

**Problem**: The "first installation to…" claim rested on the ghost reference and no precedent survey; the reception sentence ("visitors were visibly moved, collective silence") had no observable anchor.

| Aspect | Before | After |
|--------|--------|-------|
| Precedence (§Lineage, para 3) | "…the first installation to reconstruct collective memory from crowd-sourced images." | (folded into the Issue-1 rewrite: "extends this lineage by…") — the "first" claim is dropped in favor of a positioned contribution |
| Reception (§Reception, para 2) | "Visitors were visibly moved, and the room fell into a collective silence." | "At the Tri-City Media Biennial (2024), gallery logs recorded a median dwell time of 7 minutes — well above the 2-minute room average — and guest-book entries that repeatedly described the work as 'quiet' and 'haunting' (in this showing, for these visitors)." |
| Rationale | Replaced affective generalization with an observable, venue-anchored account; honest hedge preserved |
| Status | -- | **FIXED** |

#### Issue 4 (MEDIUM): Ref 9 — Hansen Year and Volume

| Aspect | Before | After |
|--------|--------|-------|
| Reference | Hansen, P. (2022). *Embodied Computation in Installation Art*. Leonardo, 55(1), 1-5. | Hansen, P. (2023). Embodied computation in installation art. *Leonardo*, 56(1), 1-5. https://doi.org/10.1162/leon_a_02281 |
| In-text citations | (Hansen 2022) [2 instances] | (Hansen 2023) [2 instances] |
| Status | -- | **FIXED** |

#### Issue 5 (MEDIUM): Ref 14 — Okonkwo & Reyes Metadata

| Aspect | Before | After |
|--------|--------|-------|
| Reference | Okonkwo, A., & Reyes, M. (2024). Participatory memory archives in media art. *Digital Creativity*, 35(2), 88-104. | Okonkwo, A., & Reyes, M. T. (2023). Participatory memory archives in media art. *Digital Creativity*, 34(4), 301-318. https://doi.org/10.1080/14626268.2023.2287711 |
| In-text citations | (Okonkwo and Reyes 2024) [2 instances] | (Okonkwo and Reyes 2023) [2 instances] |
| Status | -- | **FIXED** |

#### Issue 6 (MINOR): Award-Year Mismatch (Ref 12 / B4)

| Aspect | Before | After |
|--------|--------|-------|
| Text (§Positioning, para 1) | "A comparable work received the Prix Ars Electronica in 2021 (Ars Electronica, 2022)." | "A comparable work received a Prix Ars Electronica Honorary Mention in 2020 (Ars Electronica, 2020)." |
| Reference | Ars Electronica. (2022). *Prix Ars Electronica 2021 Catalogue*. | Ars Electronica. (2020). *Prix Ars Electronica 2020 Catalogue*. Linz: Ars Electronica. |
| Status | -- | **FIXED** |

#### Issue 7 (MINOR): Ref 17 — Page Locator

| Aspect | Before | After |
|--------|--------|-------|
| Reference / locator | Manovich, L. (2020). *Cultural Analytics*. MIT Press. (in-text pp. 45-60) | Manovich, L. (2020). *Cultural Analytics*. MIT Press. (in-text corrected to pp. 51-66) |
| Status | -- | **FIXED** |

#### Issue 8 (MINOR): Okonkwo & Reyes Paraphrase Overgeneralization

| Aspect | Before | After |
|--------|--------|-------|
| Text (§Lineage, para 5) | "Okonkwo and Reyes (2024) show that participatory memory archives consistently produce a shared sense of authorship among contributors." | "In one festival cohort, Okonkwo and Reyes (2023) observed a shared sense of authorship among contributors to a participatory memory archive (p. 311)." |
| Rationale | Narrowed from a general claim to the single-context observation the source supports |
| Status | -- | **FIXED** |

---

## Stage 2.5: Re-Verification (Round 2)

```
Stage 2.5 Re-verification -- Round 2 (focused on 8 corrected items)

integrity_verification_agent re-checking corrected items only...
```

### integrity_verification_agent Re-Verification Output

| # | Original Issue | Correction Applied | Re-verification | Status |
|---|---------------|-------------------|-----------------|--------|
| 1 | Ghost reference (Ref 5: Moreau) | Replaced with Legrady, *Making Visible the Invisible* (2005), venue+date locator; precedence claim rewritten as positioned contribution. | Work + venue+date confirmed via institutional archive. In-text now reflects a real lineage, no "first" claim. | PASS |
| 2 | "fully autonomous" overclaim | Narrowed to "near-real time during exhibition hours" + disclosed nightly human re-seeding. | Matches build log. Capability claim now supported by the realization account. | PASS |
| 3 | Unsupported "first" + reception inflation | "First" dropped; reception re-anchored to venue+date + observable detail (dwell time, guest-book) with honest hedge. | Gallery logs confirm dwell-time and guest-book detail. No inflation remaining. | PASS |
| 4 | Hansen wrong year/volume (Ref 9) | Changed to 2023, Vol. 56(1), added DOI. | DOI resolves correctly. Publisher confirms 2023 publication. | PASS |
| 5 | Okonkwo & Reyes metadata (Ref 14) | Changed to Reyes, M. T.; year 2023; Vol. 34(4), pp. 301-318. | DOI resolves to correct metadata. Publisher page confirms all fields. | PASS |
| 6 | Award-year mismatch (Ref 12) | Changed to 2020 Honorary Mention; catalogue year aligned. | Festival archive confirms 2020 Honorary Mention. In-text and reference now agree. | PASS |
| 7 | Page-locator imprecision (Ref 17) | Corrected to pp. 51-66. | Verified edition confirms chapter begins p. 51. | PASS |
| 8 | Paraphrase overgeneralization (B5) | Narrowed to single-cohort observation with page reference. | Matches source p. 311. Paraphrase now faithful. | PASS |

### Re-Verification Verdict: PASS

```
Integrity Verification Report — Round 2

Verification Mode: Pre-Review (Mode 1), Re-verification of corrected items
Verdict: ✅ PASS

Verification Summary:
| Category                       | Total | Passed | Issues |
|--------------------------------|-------|--------|--------|
| Reference Existence            | 18    | 18     | 0      |
| Bibliographic / venue+date     | 18    | 18     | 0      |
| Ghost Citations                | --    | --     | 0 orphan / 0 dangling |
| Citation Context               | 6     | 6      | 0      |
| Artwork/Realization Claims (C) | 5     | 5      | 0 (autonomy/precedence/reception resolved) |
| Internal Consistency           | --    | Pass   | 0      |
| Originality (D1)               | 19    | 19     | 0 CLOSE_MATCH / 0 VERBATIM |
| Self-Plagiarism (D2)           | N/A   | N/A    | Author name not provided |

Issue Summary:
  SERIOUS:  0 (was 3, all resolved)
  MEDIUM:   0 (was 2, both resolved)
  MINOR:    0 (was 3, all resolved)

All 8 issues from Round 1 have been verified as resolved.
Paper is cleared for jury review.
```

---

## Pipeline Continues: Stage 2.5 --> Stage 3

```
━━━ MANDATORY CHECKPOINT: Stage 2.5 INTEGRITY ━━━

Verdict: ✅ PASS (Round 2, after corrections)

Integrity verification complete:
  - Round 1: FAIL (3 SERIOUS, 2 MEDIUM, 3 MINOR)
  - Corrections applied: 8/8
  - Round 2: PASS (all issues resolved)

Corrections summary:
  - 1 ghost reference removed and replaced with a verified precedent work (venue+date)
  - 1 technical-capability overclaim narrowed ("fully autonomous" → near-real-time + disclosed human step)
  - 1 unsupported "first" claim dropped; reception re-anchored to observable detail
  - 2 bibliographic metadata errors fixed
  - 3 precision/recency improvements applied

The paper is now cleared for jury review.

Next: Stage 3 (REVIEW) — Full 5-reviewer jury
  (Chair + Curator + Practitioner-Researcher + Art-Science Critic + Devil's Advocate)

Continue?

Progress: [v]Inquiry -> [v]Writing -> [v]Integrity -> [..]Review -> [ ]Revision -> [ ]Finalization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**User**: Continue!

---

## Key Takeaways

### 1. Ghost References Are the Most Dangerous Integrity Failure

Reference 5 (Moreau, *Latent Crowds*) looked entirely plausible — a believable artist name, a real-sounding gallery, a formatted DOI. But the DOI resolved to an unrelated technical paper, and no record of this work or exhibition existed. In an art paper this is doubly dangerous: the ghost reference also propped up a precedence claim ("the first installation to…"). Artwork/exhibition entries must be anchored by a real venue+date locator, never a fabricated DOI. Without integrity verification, this would have entered jury review and potentially publication.

### 2. Over-Claimed Capability and Reception Are the Art-Specific Failure Modes

The "fully autonomous" claim (Issue 2) and the "visitors were visibly moved" claim (Issue 3) are the artwork/realization analogues of empirical data distortion. "Fully autonomous" overstated a system that actually relied on a nightly human-curated step; "visibly moved / collective silence" was affect with no observable anchor. The integrity gate down-scopes both to what the documentation (build log, gallery logs, guest-book) actually supports — and preserves the author's honest hedge ("in this showing, for these visitors").

### 3. Corrections Must Be Verifiable, Not Just Plausible

Each correction includes a verification trail: DOI resolution, page numbers, festival/museum archive confirmations, venue+date checks, and build-log references. The replacement precedent (Legrady, *Making Visible the Invisible*, 2005) was selected not just because it is topically adjacent, but because it is a widely documented, archive-confirmable work with a real venue+date locator — maximizing verifiability.

### 4. Re-Verification Is Focused, Not Redundant

Round 2 only re-checks the 8 corrected items, not the entire paper. The 14 references that passed in Round 1 are not re-verified at Stage 2.5. (Stage 4.5, the final gate, re-verifies everything from scratch.) This keeps re-verification efficient while ensuring corrections actually resolve the original issues without introducing new ones.

### 5. The Integrity Gate Is Non-Negotiable

The pipeline cannot proceed to Stage 3 (REVIEW) until the integrity check returns PASS. This is a MANDATORY checkpoint — the user cannot skip it, override it, or request an exception. The maximum retry is 3 rounds; after that, unverifiable items are listed and the user must make an explicit decision about whether to proceed with acknowledged limitations. These blocking semantics are unchanged from ARS; only the verified domain (citations + artwork/realization claims) is re-scoped.

### 6. MINOR Issues Are Worth Fixing Too

While only SERIOUS and MEDIUM issues block the pipeline, fixing MINOR issues (the award-year mismatch, the page locator, the overgeneralized paraphrase) strengthens the paper before it reaches the jury. A practitioner-researcher or Devil's Advocate juror will notice these small inaccuracies, and fixing them preemptively removes easy targets for criticism.
