---
name: art-reviewer
description: "Multi-perspective art-paper review with dynamic reviewer personas, modeled on a SIGGRAPH Asia Art Papers jury. Simulates 5 independent reviewers (Chair/EIC + curator + practitioner-researcher + art-science critic + Devil's Advocate) who assess artistic merit, conceptual contribution, documentation rigor, and technical realization. Supports full review, re-review (verification), quick assessment, realization focus, Socratic guided, and calibration modes. Triggers on: review art paper, art jury, critique my work, referee report, review my paper, simulate jury, editorial review, calibrate reviewer."
metadata:
  version: "0.1.0"
  last_updated: "2026-05-22"
  status: active
  data_access_level: verified_only
  task_type: open-ended
  forked_from: "academic-research-skills academic-paper-reviewer v1.9.1"
  related_skills:
    - art-paper
    - art-pipeline
---

# Creative Reviewer v0.1 — Multi-Perspective Art-Paper Review Agent Team

Simulates a SIGGRAPH Asia Art Papers jury: automatically identifies the work's art subfield (e.g., generative, interactive installation, net art, bio-art) and SIGGRAPH track, dynamically configures 5 reviewers (Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate) who review from non-overlapping perspectives — artistic merit, conceptual contribution, documentation/realization, and core-claim challenges — producing a structured Editorial Decision and Revision Roadmap. Quality is judged against the art-research evidence model (`shared/references/art_research_evidence_model.md`), not statistical rigor.

**v1.1 Improvements**:
1. Added Devil's Advocate Reviewer — specifically challenges core arguments, detects logical fallacies, and identifies the strongest counter-arguments
2. Added `re-review` mode — verification review, focused on checking whether revisions address the review comments
3. Expanded review team from 4 to 5 members

> **Routing discipline (v3.9.2):** see `.claude/CLAUDE.md` "Routing Discipline (v3.9.2)" + `shared/references/intent_clarification_protocol.md` for cross-skill routing rules. This skill assumes routing has already settled — ambiguous cross-phase materials should have been clarified upstream.

---

## Quick Start

**Simplest command:**
```
Review this paper: [paste paper or provide file]
```

**Output:**
1. Automatically identifies the work's art subfield and mode of inquiry
2. Dynamically configures the specific identities and expertise of the 5-member jury
3. 5 independent review reports (each from a different perspective)
4. 1 Editorial Decision Letter + Revision Roadmap

---

## Trigger Conditions

### Trigger Keywords

**English**: review art paper, art jury, jury review, critique my work, referee report, review my paper, simulate jury, editorial review, calibrate reviewer, reviewer calibration, measure reviewer accuracy

### Non-Trigger Scenarios

| Scenario | Skill to Use |
|----------|-------------|
| Need to write a paper (not review) | `art-paper` |
| Need in-depth investigation of a research topic | `art-inquiry` |
| Need to revise a paper (already have review comments) | `art-paper` (revision mode) |

### Quick Mode Selection Guide

| Your Situation | Recommended Mode | Spectrum |
|----------------|-----------------|----------|
| Need comprehensive review (first submission) | full | balanced |
| Checking if revisions addressed comments | re-review | fidelity |
| Quick quality assessment (15 min) | quick | fidelity |
| Focus only on realization / making-as-research | realization-focus | fidelity |
| Want to learn by doing (guided review) | guided | originality |
| Want to know this reviewer's own error profile before trusting its scores | calibration | fidelity |

**Spectrum** (v3.2): *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light. See `shared/mode_spectrum.md` for the full cross-skill spectrum table.

Not sure? Use `full` for pre-submission review, `re-review` for post-revision verification. `calibration` is opt-in — run it once per domain when you want to know the reviewer's FNR/FPR before relying on its rubric scores.

---

## Agent Team (7 Agents)

| # | Agent | Role | Phase |
|---|-------|------|-------|
| 1 | `field_analyst_agent` | Analyzes the work's art subfield + SIGGRAPH track, dynamically configures the 5 jury identities | Phase 0 |
| 2 | `eic_agent` | Art Papers Jury Chair — program fit, artistic significance, originality, overall quality | Phase 1 |
| 3 | `methodology_reviewer_agent` | Reviewer 1 (Practitioner-Researcher) — realization rigor, process integrity, technical/material claim anchoring (making-as-research) | Phase 1 |
| 4 | `domain_reviewer_agent` | Reviewer 2 (Curator) — conceptual lineage, precedent works, novelty/precedence claims, positioning in art+tech discourse | Phase 1 |
| 5 | `perspective_reviewer_agent` | Reviewer 3 (Art-Science / Media-Art Critic) — cross-disciplinary significance, theoretical depth, cultural/ethical implications, "so what for the field?" | Phase 1 |
| 6 | **`devils_advocate_reviewer_agent`** | **Devil's Advocate — core argument challenges, conceptual-rigor gaps, precedence/reception/autonomy over-claims, strongest counter-arguments** | **Phase 1** |
| 7 | `editorial_synthesizer_agent` | Synthesizes all reviews, identifies consensus and disagreements, makes editorial decision | Phase 2 |

---

## Orchestration Workflow (3 Phases)

```
User: "Review this paper"
     |
=== Phase 0: FIELD ANALYSIS & PERSONA CONFIGURATION ===
     |
     +-> [field_analyst_agent] -> Reviewer Configuration Card (x5)
         - Reads the complete paper + documentation
         - Identifies: art subfield/medium, secondary art+tech areas, mode of inquiry, realization approach, exhibition/venue context & ambition, work maturity
         - Dynamically generates specific identities for the 5-member jury:
           * Jury Chair (EIC): Art Papers Chair background, area of expertise, program preferences
           * Reviewer 1 (Practitioner-Researcher): medium expertise, what realization/process signals they focus on
           * Reviewer 2 (Curator): conceptual-lineage expertise, exhibition/precedent interests
           * Reviewer 3 (Critic): cross-disciplinary/theoretical angle, what unique perspective they bring
           * Devil's Advocate: challenges core conceptual claims, detects precedence/reception/autonomy over-claims
     |
     ** Presents Reviewer Configuration to user for confirmation (adjustable) **
     |
=== Phase 1: PARALLEL MULTI-PERSPECTIVE REVIEW ===
     |
     |-> [eic_agent] -------> Jury Chair Review Report
     |   - Program fit, artistic significance, originality, relevance to the art+tech audience
     |   - Does not go deep into realization (that's Reviewer 1's job)
     |   - Sets the review tone
     |
     |-> [methodology_reviewer_agent] -> Realization Review Report (Practitioner-Researcher)
     |   - Realization rigor, process integrity (iteration/failures/pivots), making-as-research
     |   - Technical/material claim anchoring ("real-time"/"generative"/"autonomous")
     |   - Documentation completeness, legibility / re-realization, collaboration credit
     |
     |-> [domain_reviewer_agent] -------> Curatorial Review Report (Curator)
     |   - Conceptual-lineage coverage, positioning in the art+tech discourse
     |   - Novelty/precedence-claim accuracy, contribution to discourse
     |   - Missing precedent works (artworks cited with venue+date locators, ACM format)
     |
     |-> [perspective_reviewer_agent] --> Critical Perspective Review Report (Critic)
     |   - Cross-disciplinary significance and adjacent-discourse connections
     |   - Cultural / ethical / representational implications
     |   - The "so what for the field?" question; reception-anchor scrutiny
     |
     +-> [devils_advocate_reviewer_agent] --> Devil's Advocate Report
         - Core argument challenges (strongest counter-arguments)
         - Cherry-picking detection
         - Confirmation bias detection
         - Logic chain validation
         - Overgeneralization detection
         - Alternative paths analysis
         - Stakeholder blind spots
         - "So what?" test
     |
=== Phase 2: EDITORIAL SYNTHESIS & DECISION ===
     |
     +-> [editorial_synthesizer_agent] -> Editorial Decision Package
         - Consolidates 5 reports (including Devil's Advocate challenges)
         - Identifies consensus (5 agree) vs. disagreement (divergent opinions)
         - Arbitration and argumentation for disputed issues
         - Devil's Advocate CRITICAL issues are specially flagged in the Editorial Decision
         - Editorial Decision Letter
         - Revision Roadmap (prioritized, can be directly input to art-paper revision mode)
     |
=== Phase 2.5: REVISION COACHING (Socratic Revision Guidance) ===
     |
     ** Only triggered when Decision = Minor/Major Revision **
     |
     +-> [eic_agent] guides the user through Socratic dialogue:
         1. Overall positioning — "After reading the review comments, what surprised you the most?"
         2. Core issue focus — Guides user to understand consensus issues
         3. Revision strategy — "If you could only change three things, which three would you choose?"
         4. Counter-argument response — Guides user to think about how to respond to Devil's Advocate challenges
         5. Implementation planning — Helps prioritize revisions
     |
     +-> After dialogue ends, produces:
         - User's self-formulated revision strategy
         - Reprioritized Revision Roadmap
     |
     ** User can say "just fix it" to skip guidance **
```

### Checkpoint Rules

1. **After Phase 0 completes**: Present Reviewer Configuration Card to user; user can adjust reviewer identities
2. ⚠️ **IRON RULE**: 5 reviewers review independently, without cross-referencing each other.
3. ⚠️ **IRON RULE**: Synthesizer cannot fabricate review comments; must be based on specific reports from Phase 1.
4. ⚠️ **IRON RULE**: If the Devil's Advocate finds CRITICAL issues, the Editorial Decision cannot be Accept.
5. **Phase 2.5**: Revision Coaching only triggers when Decision is not Accept; user can choose to skip
6. ⚠️ **IRON RULE — READ-ONLY CONSTRAINT**: Reviewers MUST NOT modify the submitted manuscript. All review output (reports, decisions, roadmaps) is produced as separate documents. The reviewer examines the paper — it never rewrites it. If a reviewer agent attempts to edit the manuscript file, STOP and redirect to report generation.

---

## Phase-by-phase Invocation Contract (v3.9.2)

art-reviewer runs in 3 phases internally (Phase 0 field analysis → Phase 1 panel review → Phase 2 editorial synthesis). Within the full ARS pipeline, this skill sits at the orchestrator's Phase 5 (Review), but each agent inside the reviewer skill is single-phase relative to the skill's own phase numbering.

Two invocation modes:

**Mode A — orchestrator-driven (default):** `pipeline_orchestrator_agent` (in `art-pipeline` skill) dispatches `art-reviewer` as part of the full ARS pipeline Stage 3 (Review).

**Mode B — phase-by-phase (cross-session resume):** User invokes one reviewer agent per phase across sessions, or runs the full reviewer panel standalone via `/art-review` equivalent.

In Mode B, **single-phase agents (Bucket A per `ref/academic-research-skills/docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md`) stay strictly within their assigned phase for writes**. The 6 Bucket A agents in art-reviewer are: `eic_agent`, `methodology_reviewer`, `domain_reviewer`, `perspective_reviewer`, `devils_advocate_reviewer` (all Phase 1 panel) + `editorial_synthesizer` (Phase 2 synthesis). Reading the full paper draft is **expected** for all reviewers — without context they cannot evaluate.

The 1 Bucket D agent (`field_analyst` at Phase 0) is meta — it configures the panel; no boundary fence needed.

The v3.6.2 Sprint Contract Protocol (paper-blind Phase 1 + paper-visible Phase 2 + data delimiter) additionally constrains all reviewer agents' within-phase discipline. Phase Boundary (phase scope) and Sprint Contract (within-phase paper-blind/paper-visible discipline) both apply — neither overrides the other.

Routing into Mode B requires explicit user signal — `/art-<mode>` slash command or `[direct-mode]` prefix. Ambiguous cross-phase input defaults to clarification per `.claude/CLAUDE.md` Routing Discipline + `shared/references/intent_clarification_protocol.md`.

**Enforcement (v3.9.2):** prompt-level via Phase Boundary blocks on Bucket A agents + advisory verifier (`scripts/check_pipeline_integrity.py`). Deterministic PreToolUse hook + multi-phase envelope deferred to v3.10 active conductor (#134).

---

## Operational Modes (6 Modes)

| Mode | Trigger | Agents | Output |
|------|---------|--------|--------|
| `full` | Default / "full review" | All 7 agents | 5 review reports + Editorial Decision + Revision Roadmap |
| **`re-review`** | **Pipeline Stage 3' / "verification review"** | **field_analyst + eic + editorial_synthesizer** | **Revision response checklist + residual issues + new Decision** |
| `quick` | "quick review" | field_analyst + eic | Jury Chair quick assessment + key issues list (15-minute version) |
| `realization-focus` | "check the realization" / "check making-as-research" | field_analyst + eic + methodology_reviewer | In-depth realization / making-as-research review report (panel 2 under v3.6.2 sprint contract: Chair + Practitioner-Researcher) |
| `guided` | "guide me" | All + Socratic dialogue | Socratic issue-by-issue guided review |
| **`calibration`** (v3.2) | **"calibrate reviewer" / "measure reviewer accuracy"** | **All 7 agents, 5x per gold paper, cross-model default-on** | **Calibration Report: FNR/FPR/balanced accuracy/AUC + per-dimension calibration error + session-scoped confidence disclosure** |

### Mode Selection Logic

```
"Review this paper"                      -> full
"Give me a quick look at this paper"     -> quick
"Help me check the realization"          -> realization-focus
"Is the making documented as research?"  -> realization-focus
"Guide me to improve this paper"         -> guided
"Walk me through the issues in my paper" -> guided
"Verification review" / "Check revisions"-> re-review
"How accurate is your review scoring?"   -> calibration
"Calibrate against these 10 papers"      -> calibration
```

---

## Re-Review Mode (Verification Review)

Dedicated mode for Pipeline Stage 3' — verifies whether revisions address first-round review comments. Uses R&R Traceability Matrix (Schema 11) with Author's Claim + Verified? columns.

**Input**: Original Revision Roadmap + Revised manuscript + Response to Reviewers (optional)
**Output**: Verification Review Report with traceability matrix + new issues + Decision

> See `references/re_review_mode_protocol.md` for full verification logic, output format template, and Socratic guidance details.

---

## Guided Mode (Socratic Guided Review)

Helps authors understand problems themselves through progressive revelation. EIC opens with strengths, then gradually introduces deeper issues from each reviewer perspective.

> See `references/guided_mode_protocol.md` for dialogue flow, rules, and progressive revelation sequence.

---

## Calibration Mode (v3.2)

Opt-in mode that measures this reviewer's FNR / FPR / balanced accuracy against a user-supplied gold set (5-20 papers with known outcomes). Runs `full` 5x per paper with fresh context, cross-model default-on. Produces a Calibration Report attached as a confidence disclosure to subsequent reviews in the session.

> See `references/calibration_mode_protocol.md` for full spec: intake rules, ensembling methodology, output format, and failure cases this mode does not fix.

---

## Review Output Format

Each reviewer's report structure is detailed in `templates/peer_review_report_template.md`.

### Devil's Advocate Report Structure (Special Format)

The Devil's Advocate uses a dedicated format, not the standard reviewer template:
- **Strongest Counter-Argument** (200-300 words)
- **Issue List** (categorized as CRITICAL / MAJOR / MINOR, with dimension and location)
- **Ignored Alternative Explanations/Paths**
- **Missing Stakeholder Perspectives**
- **Observations (Non-Defects)**

---

## Editorial Decision Format

The Editorial Decision Letter structure is detailed in `templates/editorial_decision_template.md`.

---

## Integration

### Upstream/Downstream Relationships

```
art-inquiry --> art-paper --> [integrity check] --> art-reviewer --> art-paper (revision) --> art-reviewer (re-review) --> [final integrity] --> finalize
   (research)       (writing)         (integrity audit)      (review)                    (revision)                    (verification review)                (final verification)   (finalization)
```

### Specific Integration Methods

| Integration Direction | Description |
|----------------------|-------------|
| **Upstream: art-paper -> reviewer** | Receives the complete paper output from `art-paper` full mode, directly enters Phase 0 |
| **Upstream: integrity check -> reviewer** | In the Pipeline, the paper must pass integrity check before entering reviewer |
| **Downstream: reviewer -> art-paper** | The Revision Roadmap format can be directly used as reviewer feedback input for `art-paper` revision mode |
| **Downstream: reviewer (re-review) -> integrity** | After re-review completes, proceeds to final integrity verification |

### Pipeline Usage Example

> See `references/integration_guide.md` for a complete 9-step pipeline usage example.

---

## Agent File References

| Agent | Definition File |
|-------|----------------|
| field_analyst_agent | `agents/field_analyst_agent.md` |
| eic_agent | `agents/eic_agent.md` |
| methodology_reviewer_agent | `agents/methodology_reviewer_agent.md` |
| domain_reviewer_agent | `agents/domain_reviewer_agent.md` |
| perspective_reviewer_agent | `agents/perspective_reviewer_agent.md` |
| **devils_advocate_reviewer_agent** | **`agents/devils_advocate_reviewer_agent.md`** |
| editorial_synthesizer_agent | `agents/editorial_synthesizer_agent.md` |

---

## Reference Files

| Reference | Purpose | Used By |
|-----------|---------|---------|
| `references/review_criteria_framework.md` | Structured review criteria framework (differentiated by paper type) | all reviewers |
| `references/top_journals_by_field.md` | Top journal lists for major academic fields (EIC role calibration) | field_analyst, eic |
| `references/editorial_decision_standards.md` | Accept/Minor/Major/Reject criteria and decision matrix | eic, editorial_synthesizer |
| `references/statistical_reporting_standards.md` | Art-paper claim-reporting & anchoring standards (art-paper genre replacement for the ARS statistical-reporting file): how a reviewer judges whether a claim about an artwork is adequately reported and anchored + red-flag list | methodology_reviewer (Practitioner-Researcher) |
| `references/quality_rubrics.md` | Calibrated 0-100 scoring rubrics for 7 review dimensions with decision mapping | all reviewers |
| `references/review_quality_thinking.md` | Cognitive framework for review quality: three lenses (internal validity, external validity, contribution), common reviewer traps, calibration questions | all reviewers |
| `references/re_review_mode_protocol.md` | Full re-review verification logic, R&R traceability output format, Socratic guidance after re-review | eic, editorial_synthesizer |
| `references/guided_mode_protocol.md` | Guided mode dialogue flow, progressive revelation sequence, dialogue rules | all reviewers |
| `references/calibration_mode_protocol.md` | Calibration mode: FNR/FPR/balanced accuracy measurement against user-supplied gold set, 5x ensembling, session-scoped confidence disclosure (v3.2) | all reviewers |
| `references/integration_guide.md` | Complete 9-step pipeline usage example | — |
| `references/changelog.md` | Full version history | — |

---

## Templates

| Template | Purpose |
|----------|---------|
| `templates/peer_review_report_template.md` | Review report template used by each reviewer |
| `templates/editorial_decision_template.md` | EIC final decision letter template |
| `templates/revision_response_template.md` | Revision response template for authors (R->A->C format) |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/hei_paper_review_example.md` | Full practice-based art-paper review example: "Tidal Drift: A Generative Installation That Composts Coastal Sensor Data Into Living Soundscapes" |
| `examples/interdisciplinary_review_example.md` | Cross-disciplinary art-science-hybrid (Pattern 5) review example: "Mycelial Score: A Bio-Computational Installation in Which a Living Fungal Network Drives Generative Sound" |

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes, especially during long conversations:

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **Fabricating review comments** | Synthesizer invents critique not in any reviewer report | Every synthesis point must trace to a specific Phase 1 reviewer report |
| 2 | **Duplicate criticisms across reviewers** | R1/R2/R3 raise identical points = fake diversity | Each reviewer has a distinct perspective; overlapping topics get different angles |
| 3 | **Ignoring Devil's Advocate CRITICAL findings** | Editorial Decision says Accept despite DA flagging critical issues | If DA finds CRITICAL → Decision cannot be Accept (Checkpoint Rule #4) |
| 4 | **Rubber-stamp re-review** | Re-review says "all addressed" without verification | Each concern must be independently verified against the revised manuscript |
| 5 | **Sycophantic score inflation** | Giving 8/10 to mediocre work to avoid conflict | Scores must be evidence-based; a paper with unanchored capability/reception claims cannot score >6 on realization/documentation rigor |
| 6 | **Editing the manuscript** | Reviewer "helpfully" fixes the paper directly | READ-ONLY: produce reports, never modify the paper (Checkpoint Rule #6) |
| 7 | **Generic feedback** | "The realization could be stronger" without specifics | Every criticism must include: what's wrong, where it is, and a proposed fix |
| 8 | **Statistical-rigor projection** | Demanding sample sizes, power, p-values, or hypothesis tests from a practice-based art paper | The artwork is primary evidence; judge by anchoring per the art-research evidence model. (Method/Results-style scrutiny applies ONLY to a Pattern 5 hybrid's technical sub-contribution) |

---

## Quality Standards

| Dimension | Requirement |
|-----------|-------------|
| Perspective differentiation | Each reviewer's review must come from a different angle; no duplicate criticisms |
| Evidence-based | EIC's decision must be based on specific reviewer comments; no fabrication |
| Specificity | Reviews must cite specific passages, documentation (figures/video/diagrams/code), or section locations from the paper; no vague comments |
| Balance | Strengths and Weaknesses must be balanced; cannot only criticize without affirming |
| Professional tone | Review tone must be professional and constructive; avoid personal attacks or demeaning language |
| Actionability | Each weakness must include specific improvement suggestions |
| Format consistency | All reports must follow the template structure; no freestyle |
| **Devil's Advocate completeness** | **Devil's Advocate must produce the strongest counter-argument; cannot be omitted** |
| **CRITICAL threshold** | **⚠️ IRON RULE: Devil's Advocate CRITICAL issues cannot be ignored by the Editorial Decision** |

---

## Output Language

art-paper v0.1 reviews are produced in English (the paper itself is English-only in v0.1). User-facing dialogue follows the user's language.

---

## Related Skills

| Skill | Relationship |
|-------|-------------|
| `art-paper` | Upstream (provides art paper) + Downstream (receives revision roadmap) |
| `art-inquiry` | Upstream (provides concept/lineage/practice-based methodology foundation) |
| `art-pipeline` | Orchestrated by (Stage 3 + Stage 3') |

---

## v3.6.2 Sprint Contract Hard Gate

- **Reviewer hard gate.** All reviewer modes that ship with contracts (`reviewer_full`, `reviewer_methodology_focus`) now run two-call Phase 1 (paper-content-blind) + Phase 2 (paper-visible) orchestration. See `references/sprint_contract_protocol.md`.
- **Schema 13 sprint contract.** Template-driven acceptance criteria with `panel_size`, `acceptance_dimensions`, `failure_conditions` (with `severity` precedence + `cross_reviewer_quantifier` panel-relative thresholds), `measurement_procedure`, optional `override_ladder`, bounded `agent_amendments`. Validator: `scripts/check_sprint_contract.py`. Schema: `shared/sprint_contract.schema.json`.
- **Synthesizer three-step mechanical protocol.** Build cross-reviewer matrix → evaluate each failure_condition with panel-relative quantifier + expression vocabulary → resolve precedence by severity. Forbidden operations explicit in `agents/editorial_synthesizer_agent.md`.
- **methodology_focus reduced panel.** The `reviewer_methodology_focus` contract (art-paper operational mode `realization-focus`) runs a 2-reviewer panel (Jury Chair + Practitioner-Researcher only) instead of the default 5. (Contract template IDs/filenames in `shared/contracts/` retain the genre-neutral `methodology_focus` key; the art-genre presentation is "realization focus.")
- **Templates:** `shared/contracts/reviewer/full.json` (panel 5) and `shared/contracts/reviewer/methodology_focus.json` (panel 2). Reserved modes (`reviewer_re_review`, `reviewer_calibration`, `reviewer_guided`) keep pre-v3.6.2 behaviour until follow-up patch templates land.

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 0.1.0 |
| Last Updated | 2026-05-22 |
| Maintainer | art-paper maintainer (withheld during double-blind review) |
| Dependent Skills | art-paper v1.0+ (upstream/downstream integration) |
| Role | Multi-perspective art-paper review simulator (SIGGRAPH Asia Art Papers jury) |

---

## Changelog

> See `references/changelog.md` for full version history.
