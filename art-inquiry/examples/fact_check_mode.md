---
scenario: Fact-checking claims about generative / new-media art history and exhibition records
mode: fact-check
agents_used:
  - source_verification_agent
input: User provides 7 claims about generative art history, precedent works, and exhibition/reception
output: Claim-by-claim verification report + verification summary
note: This example uses generative-art history as the domain. The fact-check mode works with any claims — provide statements about your research area (e.g. precedence claims like "the first artwork to use neural networks", exhibition/award claims, or technical-capability claims like "runs fully autonomously in real time"). The same per-claim verdict workflow applies.
---

# Fact-Check Mode Example: Generative-Art History & Exhibition-Claim Verification

This example demonstrates the complete workflow of `fact-check` mode using generative / new-media art history as a domain-specific case. The same workflow applies to any practice-based art-research claim — simply replace the claims with statements relevant to your work or lineage. The source_verification_agent verifies each claim against available evidence, treating precedence, exhibition, and technical-capability claims with the extra scrutiny the integrity model requires (see `shared/references/art_research_evidence_model.md`).

---

## User Request

```
Please fact-check the following claims for my art paper:

1. The 1968 exhibition Cybernetic Serendipity at the ICA London was the first
   exhibition devoted to computer-based art.
2. Harold Cohen's AARON was a fully autonomous painting system that produced
   finished works with no human involvement.
3. Vera Molnar began making computer-generated drawings in the 1960s.
4. My installation was the first artwork to use a large language model to generate
   live wall text in response to visitors.
5. The work was exhibited at Ars Electronica and received the Golden Nica.
6. Audiences at the opening were deeply moved and many were brought to tears.
7. The generative system runs in real time and never repeats an output.
```

---

## source_verification_agent Verification Report

### Claim 1

> "The 1968 exhibition Cybernetic Serendipity at the ICA London was the first exhibition devoted to computer-based art."

**Verdict:** Warning — Partially True

**Verification Basis:** *Cybernetic Serendipity* (ICA London, curated by Jasia Reichardt) did open in 1968 and is widely cited as a landmark, internationally influential survey of computer and cybernetic art. However, the strong precedence claim "the first" is contestable: earlier 1965 gallery showings of computer-generated art (e.g. by Georg Nees and Frieder Nake in Stuttgart, and A. Michael Noll / Bela Julesz in New York) predate it. *Cybernetic Serendipity* is most defensibly described as the first *large-scale international survey*, not the first exhibition of computer art.

**Source:** Exhibition record, ICA London, 1968 (venue/date locator); standard new-media art histories.

**Correction Suggestion:** Revise to "one of the earliest and most influential international surveys of computer-based art (ICA London, 1968)," and cite the 1965 gallery shows if a precedence point is needed. Precedence claims require a citation or a hedge.

---

### Claim 2

> "Harold Cohen's AARON was a fully autonomous painting system that produced finished works with no human involvement."

**Verdict:** Warning — Partially True

**Verification Basis:** *AARON* is correctly attributed to Harold Cohen and is a foundational autonomous-art system developed over decades. However, "fully autonomous … no human involvement" overstates the evidenced realization. Cohen authored, tuned, and curated *AARON* throughout its life; in many phases the physical output (e.g. coloring) involved Cohen or assistants, and Cohen selected and contextualized outputs. This is a technical/autonomy capability claim of exactly the kind the integrity model flags — the claim outruns the documented realization.

**Source:** Cohen's own writings and exhibition documentation (venue/date locators).

**Correction Suggestion:** Revise to "*AARON* generated drawings autonomously according to rules Cohen authored and continued to revise, with Cohen curating and, in some phases, realizing the output." Hedge or evidence any "fully autonomous" claim.

---

### Claim 3

> "Vera Molnar began making computer-generated drawings in the 1960s."

**Verdict:** Verified

**Verification Basis:** Vera Molnar, a pioneer of generative and algorithmic art, began working with computers and plotters in the late 1960s (commonly dated to around 1968), after earlier non-computational algorithmic experiments. This is well documented across art-historical sources and her own accounts.

**Source:** Standard generative-art histories; museum collection records (venue/date locators).

**Note:** If a precise year is stated in the paper, cite a specific source, as accounts vary between "late 1960s" and a specific year.

---

### Claim 4

> "My installation was the first artwork to use a large language model to generate live wall text in response to visitors."

**Verdict:** Unverifiable

**Verification Basis:** "First artwork to…" is a precedence/novelty claim that cannot be verified against the documented record — the field of LLM-driven installations is large, recent, and unevenly documented, and an exhaustive negative ("no prior work did this") is not provable. This is precisely the claim type the integrity gate requires to be hedged or supported with a citation.

**Source:** No evidence base supports an exhaustive precedence claim of this kind.

**Correction Suggestion:** Revise to a hedged, defensible form: "one of the earliest installations to use an LLM to generate live wall text responsive to visitors, to the author's knowledge," or drop the precedence framing and state the specific contribution directly.

---

### Claim 5

> "The work was exhibited at Ars Electronica and received the Golden Nica."

**Verdict:** Needs source — treated as an exhibition/award claim

**Verification Basis:** Exhibition venues and awards are verifiable facts that must be anchored to a real, citable record (Ars Electronica's Prix archive lists every Golden Nica by year and category). Without the year, category, and a citable archive entry, the claim cannot be confirmed and must not be asserted. Exhibition/award claims are treated with the same faithfulness standard as citations — no fabricated specifics.

**Source:** Ars Electronica Prix archive (must be cited with year + category as the locator).

**Correction Suggestion:** State the exact festival year and award category and cite the Prix archive entry, e.g. "exhibited at Ars Electronica 2024; awarded the Golden Nica in the [category] category (Prix Ars Electronica archive)." If unconfirmed, remove the award claim.

---

### Claim 6

> "Audiences at the opening were deeply moved and many were brought to tears."

**Verdict:** Warning — Reception inflation

**Verification Basis:** This is a reception claim with no observable anchor — "deeply moved," "brought to tears" asserts an affective effect that the documentation does not support. Per the art-research evidence model, reception claims must be anchored to a named venue/date plus an observable, recorded detail, never to asserted emotion.

**Source:** No observable anchor provided.

**Correction Suggestion:** Down-scope to what was actually observed or recorded, e.g. "at the opening [venue, date], visitors lingered an average of several minutes and some returned multiple times" — or, if responses were collected, quote them with attribution. Remove unanchored affective claims.

---

### Claim 7

> "The generative system runs in real time and never repeats an output."

**Verdict:** Warning — Partially True

**Verification Basis:** Two technical-capability claims are bundled. "Real time" is plausible but requires a realization anchor (latency, hardware, what "real time" means for this work). "Never repeats an output" is a strong claim that is rarely strictly true for a finite-state generative system — without an extremely large or continuous output space and a deduplication mechanism, repeats are possible. The claim should be specified and hedged.

**Source:** Requires the work's own system documentation to verify.

**Correction Suggestion:** Revise to "the system generates outputs in real time (under [X] ms on [hardware]); the output space is large enough that repeats are not observed over a typical exhibition run," or state the deduplication mechanism if one exists. Technical claims need a realization anchor.

---

## Verification Summary Report

### Overview

| # | Claim Summary | Verdict | Severity |
|---|----------|------|--------|
| 1 | Cybernetic Serendipity was "the first" computer-art exhibition | Warning — Partially True | Medium — precedence overstated |
| 2 | AARON was "fully autonomous, no human involvement" | Warning — Partially True | Medium — capability claim outruns evidence |
| 3 | Molnar began computer drawings in the 1960s | Verified | N/A |
| 4 | "First artwork" to use an LLM for live wall text | Unverifiable | High — unprovable precedence |
| 5 | Exhibited at Ars Electronica, won Golden Nica | Needs source | High — must cite or remove |
| 6 | Audiences moved to tears | Warning — Reception inflation | High — no observable anchor |
| 7 | Real-time, never repeats | Warning — Partially True | Medium — needs realization anchor |

### Verification Statistics

- Verified: 1 claim (14%)
- Warning — Partially True / Reception inflation: 4 claims (57%)
- Needs source: 1 claim (14%)
- Unverifiable: 1 claim (14%)

### Overall Assessment

The set mixes verifiable art-history facts with the three claim types the integrity model scrutinizes hardest: **precedence/novelty** (Claims 1, 4), **technical/autonomy capability** (Claims 2, 7), and **exhibition/award + reception** (Claims 5, 6). Only one claim is fully verified. The highest-risk items are the unprovable "first artwork" precedence claim (4), the uncited award claim (5), and the unanchored reception claim (6) — each would weaken the paper's integrity if asserted as written.

### Verification Recommendations

1. Precedence/novelty claims ("first to…") require a citation or must be hedged ("to the author's knowledge")
2. Technical/autonomy claims ("real-time", "fully autonomous", "never repeats") require a realization anchor
3. Exhibition and award claims must cite a real, dated archive entry as the locator — no fabricated specifics
4. Reception claims must be anchored to a named venue/date + an observable, recorded detail — never asserted emotion
