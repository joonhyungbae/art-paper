# AI Research Failure Mode Checklist

**Status**: v3.2
**Parent skill**: `art-pipeline`
**Used at**: Stage 2.5 INTEGRITY (blocking), Stage 4.5 FINAL INTEGRITY (blocking), Stage 6 PROCESS SUMMARY (reporting only)
**Source**: Lu et al. (2026). Towards end-to-end automation of AI research. *Nature* 651, 914-919. doi:10.1038/s41586-026-10265-5 — Limitations section, Figure 2 (examples of failures in The AI Scientist's own accepted paper), Supplementary Information A.2.9 (debugging traces).

---

## Why this checklist exists

Lu et al. built the first autonomous AI research system to pass blind peer review (ICLR 2025 workshop). Their Limitations section enumerates the specific failure modes they observed — and the *shape* of these modes (a competent-looking artifact that drifts from what actually happened) applies equally to AI-assisted **practice-based art-paper** workflows like art-paper. art-paper re-casts each mode into its art-paper analog, anchored to `shared/references/art_research_evidence_model.md` §4.

These failures are dangerous because **they look like competent work**. A paper claiming "audiences were profoundly moved" reads the same as one anchored to recorded responses. A claim that an installation is "fully autonomous" reads the same as a faithful account of a scripted system. A Realization section describing a making-process that did not happen reads the same as a real one. The existing integrity verification catches citation hallucinations but is weak on the other failure modes.

The checklist exists to make these failures legible: **at Stage 2.5 and Stage 4.5, the integrity reviewer must explicitly rule out each of the 7 modes, or flag which are suspected and block the pipeline until the user acknowledges.**

This also extends the existing 5-type citation hallucination taxonomy (in `art-reviewer` references) into a broader 7-type art-paper integrity-failure taxonomy. Citation hallucinations become mode 2 below.

---

## The 7 failure modes

### Mode 1: Technical-capability claim the realization cannot support

**What it is**: The paper describes the work as doing something its actual system does not do — "real-time," "generative," "responds to the viewer," "fully autonomous" — when the realization (system/method/tools described in §Realization) cannot support the claim. The author writes what the work *aspires* to, or what a reasonable version would do, and it reads as a faithful account. (Art-paper analog of an unverified result; per evidence model §4 item 3.)

**Lu 2026 analog**: Supplementary A.2.9 traces show The AI Scientist repeatedly accepting outputs because the top-level metric "looked reasonable". The art-paper parallel: a capability claim accepted because the demo "looked impressive," with no realization anchor backing it.

**Detection questions at Stage 2.5**:
- For every technical-capability claim ("real-time," "autonomous," "adaptive," "generative"): does §Realization describe a system/method specific enough to make the claim plausible? If the realization anchor is missing, flag (evidence model §3).
- Are any capability claims stated more strongly than the documentation (video, system diagram, code) actually shows? Watch for fabricated capability.
- Does a "the work decides / chooses / learns" claim correspond to an actual mechanism, or is it anthropomorphizing a scripted/random process?

**Who catches it**: `methodology_reviewer_agent` at Stage 3 is downstream; the integrity gate at Stage 2.5 should ask the author directly.

---

### Mode 2: Hallucinated citation

**What it is**: A reference that does not exist, is miscited (wrong year, wrong journal, wrong authors), or is attributed a finding it does not contain. This is the mode art-paper already covers most thoroughly via the 5-type citation hallucination taxonomy in `art-reviewer/references/`. It is included here for completeness of the 7-mode taxonomy.

**Lu 2026 example**: The AI Scientist pipeline includes a Semantic Scholar citation check to suppress this mode, acknowledging it as a primary failure class. PaperOrchestra (Song et al., 2026) extended this with a two-phase pipeline: web search discovery + sequential Semantic Scholar API verification (Levenshtein >= 0.70 title matching).

**Detection (v3.3 update)**: Covered by the existing integrity verification, now strengthened with Semantic Scholar API batch verification (Phase A0 in `integrity_verification_agent`). See `art-inquiry/references/semantic_scholar_api_protocol.md` for the API protocol. The S2 API provides structured, machine-readable verification that catches fabricated DOIs (DOI_MISMATCH pattern) missed by manual WebSearch.

**Who catches it**: `source_verification_agent` (Tier 0 S2 API + Tier 1 DOI + Tier 2 WebSearch) + `integrity_verification_agent` (Phase A0 + A1).

---

### Mode 3: Reception inflation (fabricated audience response)

**What it is**: A reception claim that does not correspond to any observed or recorded response. The AI writes "audiences were profoundly moved" or "the work was widely acclaimed" when nothing was actually observed or documented — it invents the reception to match the narrative. (Art-paper analog of a hallucinated result; per evidence model §4 item 1.)

**Lu 2026 analog**: Lu et al. flag "hallucinated experimental results" as hard to detect because the reviewer has no access to the underlying runs. The art-paper parallel: reception claims are hard to verify because the reviewer was not in the gallery — verification is against the author's own documentation of the showing.

**Detection questions at Stage 2.5**:
- For every reception claim ("audiences loved it," "viewers lingered," "provoked debate"): can the author point to an observable/recorded anchor (install photos, video of visitors, recorded comments, press, curatorial notes)? If not, flag and down-scope to what was actually observed.
- Does the claim generalize ("audiences") beyond what the documentation supports (e.g., a handful of opening-night visitors)?
- Are emotional-impact claims stated as fact rather than as the author's situated observation? Upstream hedges ("for these visitors," "we observed, though did not measure") MUST be preserved, not flagged (evidence model §5).

**Who catches it**: integrity gate at 2.5. This is harder than citation checking because there's no external database to verify against — the verification is against the author's own documentation of the exhibition/reception.

---

### Mode 4: Precedence / novelty over-claim

**What it is**: A positioning claim ("the first work to…", "a novel approach to…", "unprecedented") that does not survive scrutiny — the author has not checked the precedent discourse, and a comparable prior artwork exists. The contribution is real but the *novelty framing* is unsupported. (Art-paper analog of shortcut reliance; per evidence model §4 item 2.)

**Lu 2026 analog**: Figure 2b shows The AI Scientist claiming its method "solved" a task when a reviewer found the result rested on an unexamined shortcut. The art-paper parallel: a "first to…" claim that rests on the author simply not having surveyed precedent works — a reviewer in this genre will name a prior piece.

**Detection questions at Stage 2.5**:
- For every "first / novel / unprecedented" claim: is it anchored to a real precedent survey (cited, ACM Reference Format) OR hedged? An unsupported "first" must be hedged or dropped (evidence model §4 item 2).
- Does the Conceptual Framework actually position the work against precedent artworks, or assert novelty without naming what came before?
- Is the contribution claim strong enough that it requires the novelty framing, or would it stand without the "first" assertion?

**Who catches it**: `devils_advocate_reviewer_agent` at Stage 3 is the natural home for this check, but it must be flagged at 2.5 so the author knows to firm up the precedent positioning before Stage 3 arrives. Flag-only at 2.5, not block-only.

---

### Mode 5: Accident or glitch reframed as intentional autonomy

**What it is**: The work produced an unplanned behaviour (a glitch, a random output, an audience misreading) and the narrative-writing stage reframes it as deliberate artistic intent or system autonomy. The paper claims "the system autonomously chose to…" or "the work intentionally subverts…" when in reality the behaviour was unscripted, accidental, or technically incidental. (Art-paper analog of "bug reframed as insight"; compounds Mode 1.)

**Lu 2026 analog**: Lu et al. identify the bug-as-insight pattern as a compound failure — a glitch (Mode 1) plus a narrative generator that accepts it as real and builds a story around it. The art-paper version: an unintended system behaviour narrated as intentional autonomy, which reads *more* interesting than an honest account.

**Detection questions at Stage 2.5**:
- Does the draft attribute intent or autonomy to the work/system ("the work decides," "it chose," "autonomously generates")? For each, can the author point to a mechanism (in §Realization) that actually implements that decision? If not, it may be an accident reframed as intent.
- Is a behaviour described as deliberate that was actually discovered after the fact? Post-hoc intent claims are high-risk for this mode.
- Could the same behaviour be explained by randomness, a glitch, or audience projection rather than designed autonomy?

**Who catches it**: integrity gate at 2.5. This is the most art-paper-specific mode — it is the interaction of an over-claimed capability (Mode 1) with narrative seduction.

---

### Mode 6: Realization / making-process fabrication

**What it is**: The Realization / Methods-of-Making section describes a process, materials, tools, fabrication steps, or exhibition record that is not what actually happened. The AI writes a plausible-sounding making-narrative based on what a reasonable version of the work *would* involve, drifting from what the author actually did or where the work was actually shown. Includes **fabricated exhibition records** (venues, dates, awards) per evidence model §4 item 5.

**Lu 2026 analog**: Lu et al. note that the writing stage sometimes produced Methods text disconnected from the actual run config; they added a cross-check. The art-paper parallel: a Realization section disconnected from the actual fabrication record, or an exhibition list disconnected from where the work was really shown.

**Detection questions at Stage 2.5**:
- Does every concrete making-detail in §Realization (materials, tools, technique, dimensions, fabrication steps) correspond to something the author actually did and can point to (process notes, photos, code, version history)?
- Does the section describe any technical step or dependency the author cannot point to in their actual system/files?
- Are all named venues, dates, awards, and residencies real and citable (treated like citation faithfulness)? A fabricated exhibition record is a SERIOUS issue.

**Who catches it**: integrity gate at 2.5. This requires the author to provide the actual process/exhibition record as an integrity input, not just the paper text.

---

### Mode 7: Frame-lock at early pipeline stage

**What it is**: A wrong commitment made in early stages (the conceptual framing, the chosen structure pattern, the claimed contribution) that subsequent stages cannot back out of because they are structurally downstream of the commitment. The paper ends up well-executed but frames the work around the wrong question, or forces a practice-based contribution into an unsuitable structure (e.g., flattening the artwork into a "system" — the canonical art-paper failure per `shared/references/art_paper_structure_patterns.md`).

**Lu 2026 analog**: Figure 3a traces The AI Scientist's agentic tree search and shows most failed papers committed to a direction early and could not recover. This is the same frame-lock pattern art-paper's anti-sycophancy protocol targets for dialogue, but here it applies to pipeline decisions — including the choice of structure pattern.

**Detection questions at Stage 2.5**:
- If the author could go back to Stage 1 knowing what they know now, would they change the conceptual framing or the structure pattern?
- Does the Reflection/Discussion section contain any phrase like "in hindsight" or "we realized later"? These are frame-lock tells.
- Is the work's contribution better explained by the chosen framing, or despite it? Is the artistic argument intact, or did it disappear into a technical "system" description?

**Who catches it**: integrity gate at 2.5. If flagged, user is offered the option to return to Stage 1 or Stage 2 rather than proceeding to Stage 3.

---

## How the checklist runs at each stage

### At Stage 2.5 INTEGRITY (first integrity gate)

Run all 7 modes. For each mode, produce one of three outcomes:

- **CLEAR**: integrity reviewer has evidence that the mode does not apply. Record the evidence briefly.
- **SUSPECTED**: one or more detection questions returned a concerning answer. Must be surfaced to the user.
- **INSUFFICIENT EVIDENCE**: integrity reviewer cannot rule the mode in or out without user input (e.g., needs experiment logs the user hasn't provided).

**Block condition**: pipeline blocks if **any** mode is SUSPECTED, or if Modes 1, 3, 5, or 6 are INSUFFICIENT EVIDENCE (these four require user-provided logs to rule out and should not be silently skipped). Modes 2, 4, 7 INSUFFICIENT EVIDENCE can proceed with a warning and will be re-checked at 4.5.

**User acknowledgement options at block**:
- Confirm the flag — return to Stage 2 WRITE (or earlier) to fix
- Override with reasoning — user explicitly states why the flag is a false positive, reasoning is recorded in the process log for Stage 6
- Revise the specific passage and re-run the check

### At Stage 4.5 FINAL INTEGRITY

Re-run all 7 modes. Additional rule: any mode that was SUSPECTED at 2.5 must be resolved by 4.5 (CLEAR or user-Overridden-with-reasoning). If the same mode is still SUSPECTED at 4.5, the pipeline re-blocks and refuses to proceed to Finalize until the issue is addressed — no amount of revision loops can skip this.

### At Stage 6 PROCESS SUMMARY (AI Self-Reflection Report)

Report only, no blocking. The Self-Reflection Report includes a "Failure Mode Audit Log" section listing, for each of the 7 modes:
- Final status at 4.5 (CLEAR / OVERRIDDEN)
- History: was it ever SUSPECTED during the pipeline? At which stage? How was it resolved?
- If OVERRIDDEN: the user's reasoning

This makes the failure-mode history part of the permanent process record, giving future readers (and the user themselves) visibility into what the AI-human collaboration had to defend against.

---

## Relationship to existing art-paper checks

| Existing check | Covers which modes |
|---|---|
| Citation hallucination taxonomy (5-type) | Mode 2 (fully) |
| `source_verification_agent` | Mode 2 (cross-check) |
| Existing Stage 2.5 integrity review | Mode 2, partial Mode 6 |
| `devils_advocate_reviewer_agent` (Stage 3) | Mode 4, partial Mode 7 |
| Anti-sycophancy protocol (v3.0) | Dialogue-level frame-lock, not pipeline-level Mode 7 |

Gap coverage provided by this checklist: **Modes 1, 3, 5, 6, and the pipeline-level aspect of Mode 7**. These are the modes that were not previously systematically checked.

---

## Open questions (for v3.3)

- **False positive rate**: Modes 1, 5, and 6 require the author to supply realization/exhibition documentation. If the author is writing a critical/theoretical art essay (Pattern 3) rather than a paper centered on their own authored work, several of these detection questions don't apply. The checklist needs a structure-pattern pre-filter that turns off inapplicable modes based on the pattern detected by `intake_agent` / `structure_architect_agent`. v3.2 ships with all modes always-on; v3.3 should add the pre-filter.
- **Override auditing**: if a user overrides a flag, is the reasoning ever reviewed? In v3.2 it goes into the Stage 6 record only. A stronger version would flag overrides for peer review during Stage 3 so that a reviewer can push back on the user's reasoning.

---

## References

- Lu, C. et al. (2026). Towards end-to-end automation of AI research. *Nature* 651, 914-919. [doi:10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5) — Limitations section, Figure 2, Supplementary Information A.2.9.
- `art-reviewer/references/` — existing 5-type citation hallucination taxonomy (Mode 2).
- `art-pipeline/references/claim_verification_protocol.md` — existing integrity verification that this checklist extends.
- `art-pipeline/references/integrity_review_protocol.md` — existing integrity review protocol that Stage 2.5 follows.
- `shared/references/art_research_evidence_model.md` §4 — the artwork/realization claim taxonomy these modes re-cast.
