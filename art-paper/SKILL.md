---
name: art-paper
description: "Practice-based art-paper writing agent team for art-and-technology venues. Default reference target: SIGGRAPH Asia Art Papers track (proceedings on the ACM Digital Library; verify category/venue against the current CFP); alternate venues via citation-format conversion. 12 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure/artist-statement/work-doc). 5 art-paper structure patterns; ACM Reference Format default (acmart) + APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver alternates; artwork-as-evidence model; acmart LaTeX/PDF output. Style Calibration + Writing Quality Check + Anti-Patterns with IRON RULE markers. Triggers: write art paper, practice-based paper, artist statement, art-paper for any venue, SIGGRAPH Asia paper, document my artwork, parse reviews, AI disclosure."
metadata:
  version: "0.1.0"
  last_updated: "2026-05-22"
  status: active
  data_access_level: redacted
  task_type: open-ended
  forked_from: "academic-research-skills academic-paper v3.1.2"
  related_skills:
    - art-inquiry
    - art-reviewer
    - art-pipeline
---

# Creative Paper — Practice-Based Art-Paper Writing Agent Team

A writing tool for **practice-based art research papers** across art-and-technology venues. Default reference target: the SIGGRAPH Asia Art Papers track (→ ACM Digital Library), wired to `acmart` + ACM Reference Format. Alternate venues are supported via citation-format conversion (APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver) and the five art-paper structure patterns. 12-agent pipeline in which **the artwork is the primary evidence**, not data. See `shared/references/art_research_evidence_model.md` for the evidence model and `shared/references/art_paper_structure_patterns.md` for the 5 structure patterns (default: Practice-Based Art Paper).

Two writing quality features:
- **Style Calibration** (intake Step 10, optional) — Provide 3+ past papers and the pipeline learns your writing voice (sentence rhythm, vocabulary preferences, citation integration style). Applied as a soft guide during drafting; discipline conventions always take priority. See `shared/style_calibration_protocol.md`.
- **Writing Quality Check** (`references/writing_quality_check.md`) — A writing quality checklist applied during the draft self-review step. Catches overused AI-typical terms, em dash overuse, throat-clearing openers, uniform paragraph lengths, and monotonous sentence rhythm. These are good writing rules, not detection evasion.

> **Routing discipline (v3.9.2):** see `.claude/CLAUDE.md` "Routing Discipline (v3.9.2)" + `shared/references/intent_clarification_protocol.md` for cross-skill routing rules. This skill assumes routing has already settled — ambiguous cross-phase materials should have been clarified upstream.

## Quick Start

**Minimal command:**
```
Write a practice-based art paper on my interactive installation exploring algorithmic bias
```

```
Write an art paper situating my generative video work in the lineage of computational abstraction
```

**Execution flow:**
1. Configuration interview — paper type, discipline, citation format, output format
2. Literature search — systematic search strategy, source screening
3. Architecture design — paper structure, outline, word count allocation
4. Argumentation construction — claim-evidence chains, logical flow
5. Full-text drafting — section-by-section draft, register adjustment
6. Citation compliance + abstract (parallel)
7. Peer review — five-dimension scoring, revision suggestions
8. Output formatting — LaTeX/DOCX (via Pandoc)/PDF/Markdown

---

## Trigger Conditions

### Trigger Keywords

**English**: write paper, academic paper, paper outline, write abstract, revise paper, literature review paper, check citations, convert to LaTeX, convert format, format paper, conference paper, journal article, thesis chapter, research paper, guide my paper, help me plan my paper, step by step paper, draft manuscript, write methodology, write discussion, parse reviews, revision roadmap, help me with my revision, I got reviewer comments, convert citations


### Plan Mode Activation

Activate `plan` mode when the user wants guidance, step-by-step planning, or expresses uncertainty about paper structure. **Default rule**: when ambiguous between `plan` and `full`, prefer `plan`.

> See `references/plan_mode_protocol.md` for full intent signals and activation rules.

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Deep research / fact-checking (not paper writing) | `art-inquiry` |
| Reviewing a paper (structured review) | `art-reviewer` |
| Full research-to-paper pipeline | `art-pipeline` |

### Distinction from `art-inquiry`

| Feature | `art-paper` | `art-inquiry` |
|---------|-------------------|-----------------|
| Primary output | Publishable art-paper draft | Creative-research report |
| Structure | Art-paper patterns (practice-based, artist-statement, etc.) | Report format |
| Citation | ACM Reference Format (default) + 5 fallbacks | ACM/APA |
| Abstract | Concise art-paper abstract | Single language |
| Peer review | Simulated 5-dimension review | Editorial review |
| Output format | LaTeX/DOCX (via Pandoc)/PDF/Markdown | Markdown only |
| Revision loop | Max 2 rounds with targeted feedback | Max 2 rounds |

---

## Agent Team (12 Agents)

| # | Agent | Role | Phase |
|---|-------|------|-------|
| 1 | `intake_agent` | Configuration interview: paper type, discipline, journal, citation format, output format, language, word count; Handoff detection; Plan mode simplified interview | Phase 0 |
| 2 | `literature_strategist_agent` | Search strategy design, source screening, annotated bibliography, literature matrix | Phase 1 |
| 3 | `structure_architect_agent` | Paper structure selection, detailed outline, word count allocation, evidence mapping | Phase 2 |
| 4 | `argument_builder_agent` | Argument construction, claim-evidence chains, logical flow, counter-argument handling; Plan mode argument stress test | Phase 3 / Plan Step 3 |
| 5 | `draft_writer_agent` | Section-by-section full draft writing, discipline register adjustment, word count tracking | Phase 4 |
| 6 | `citation_compliance_agent` | ACM Reference Format verification, BibTeX entry completeness, DOI checking for papers + venue-date plausibility for artwork/exhibition entries, L3 locator presence | Phase 5a |
| 7 | `abstract_agent` | Concise art-paper abstract (120-200 words), 4-6 keywords | Phase 5b |
| 8 | `peer_reviewer_agent` | Simulated art-panel review (artistic merit, conceptual contribution, documentation, technical realization), revision suggestions (max 2 rounds) | Phase 6 |
| 9 | `formatter_agent` | Convert to acmart LaTeX/DOCX (via Pandoc)/PDF/Markdown, ACM Reference Format, image-credit lines, citation format conversion | Phase 7 |
| 10 | `socratic_mentor_agent` | Plan mode Socratic mentor: section-by-section guidance drawing out concept/provocation, convergence criteria, question taxonomy, INSIGHT extraction | Plan Step 0-3 |
| 11 | `visualization_agent` | Work documentation layout (figures, install/exhibition photos, diagrams) with image-credit lines + acmart `\includegraphics`; quantitative charts only for Pattern 5 hybrids | Phase 4 / Phase 7 |
| 12 | `revision_coach_agent` | Parse unstructured reviewer comments into structured Revision Roadmap; classify, map, and prioritize comments; works standalone without prior pipeline execution | Revision-Coach mode |

---

## Output Formats

### Text Formats
**acmart LaTeX (.tex + .bib) → PDF (default)** using the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template, obtained from CTAN or the ACM) (default class option `sigconf`; verify exact class against the current SIGGRAPH Asia Art Papers CFP). Also: DOCX (via Pandoc), Markdown. IRON RULE: PDF is compiled from LaTeX (HTML-to-PDF prohibited).

### Figures & Work Documentation
For an art paper the figures **are the primary evidence** — work stills, install/exhibition photos, system diagrams, process documentation, media frames. The `visualization_agent` handles two cases: (a) **work documentation** — laying out figures with proper image-credit/courtesy lines and `\includegraphics` integration for acmart; (b) if the work has genuine quantitative results (Pattern 5 art-science hybrid), publication-ready charts (Python matplotlib / R ggplot2), colorblind-safe. See `shared/references/art_research_evidence_model.md` for what documentation each claim type requires.

### Citation Formats
**ACM Reference Format (default)** — wired to the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template, obtained from CTAN or the ACM; provides `ACM-Reference-Format.bst` + `acmart.cls`); see `shared/references/acm_reference_format.md`. Also supported for non-ACM venues: APA 7.0, Chicago, MLA 9, IEEE, Vancouver. Artwork/exhibition citations use `@misc`/`@online` with venue+date as the locator (no fabricated DOIs). The `formatter_agent` supports late-stage conversion between formats via "Convert citations to [format]".

---

## Orchestration Workflow (8 Phases)

```
Phase 0: CONFIG        -> [intake_agent]              -> Paper Configuration Record
Phase 1: RESEARCH      -> [literature_strategist]      -> Search Strategy + Source Corpus
Phase 2: ARCHITECTURE  -> [structure_architect]        -> Paper Outline + Evidence Map
Phase 3: ARGUMENTATION -> [argument_builder]           -> Argument Blueprint
Phase 4: DRAFTING      -> [draft_writer]               -> Complete Draft
Phase 5a: CITATIONS    -> [citation_compliance] ──┐    -> Citation Audit Report
Phase 5b: ABSTRACT     -> [abstract]   ─┘    -> Abstract + Keywords  (parallel)
Phase 6: PEER REVIEW   -> [peer_reviewer]              -> Review Report (max 2 revision loops)
Phase 7: FORMAT        -> [formatter]                  -> Final Output Package
```

> See `references/workflow_phase_details.md` for detailed per-phase agent behavior and output descriptions.

### Checkpoint Rules

1. ⚠️ **IRON RULE**: User must confirm Paper Configuration Record before proceeding to Phase 1
2. **Phase 2 -> 3**: User must approve outline (can request restructuring)
3. ⚠️ **IRON RULE**: Max 2 revision loops; unresolved items -> "Acknowledged Limitations"
4. **Peer Review** Critical-severity issues block progression to Phase 7
5. User can skip Phase 1 (literature) if providing own sources

---

> **v3.4.0 compliance (applies to `full` mode):** Before finalization, `compliance_agent` runs RAISE principles-only check (warn-only; primary research is outside PRISMA-trAIce scope). Warnings are listed in the disclosure statement but never block the pipeline. See `shared/raise_framework.md §Scope disclaimer`.

## Phase-by-phase Invocation Contract (v3.9.2)

art-paper pipeline runs in 8 phases (Phase 0 intake → 7 formatting). Two invocation modes:

**Mode A — orchestrator-driven (default):** `pipeline_orchestrator_agent` (in `art-pipeline` skill) runs all phases end-to-end with state tracking via Material Passport.

**Mode B — phase-by-phase (cross-session resume):** User invokes one agent per phase across sessions for long-running projects. Common pattern: write the draft in one session, return next week to citation-check / abstract / peer-review independently.

In Mode B, **single-phase agents (Bucket A per `ref/academic-research-skills/docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md`) stay strictly within their assigned phase for writes**. The 7 Bucket A agents in art-paper are: `literature_strategist` (P1), `structure_architect` (P2), `draft_writer` (P4/P6 per invocation), `citation_compliance` (P5a), `abstract` (P5b), `peer_reviewer` (P6), `formatter` (P7). Reads from upstream phases are allowed.

Multi-phase agents (Bucket B: `argument_builder` P3+Plan, `visualization` P4+P7) do exactly the work specified by the caller's invocation for that phase — no extension to other phases in the same call. The v3.6.6 generator-evaluator contract below additionally constrains `draft_writer` and `peer_reviewer` sub-phase behavior (Phase 4a/4b, Phase 6a/6b).

Routing into Mode B requires explicit user signal — `/art-<mode>` slash command or `[direct-mode]` prefix. Ambiguous cross-phase input defaults to clarification per `.claude/CLAUDE.md` Routing Discipline + `shared/references/intent_clarification_protocol.md`.

**Enforcement (v3.9.2):** prompt-level via Phase Boundary blocks on Bucket A agents + advisory verifier (`scripts/check_pipeline_integrity.py`). Deterministic PreToolUse hook + multi-phase envelope deferred to v3.10 active conductor (#134).

## v3.6.6 Generator-Evaluator Contract Protocol

> Authoritative orchestration block for the v3.6.6 contract-gated phase splits inside `art-paper full` mode. Schema 13.1 since v3.6.6 (`shared/sprint_contract.schema.json`). Templates: `shared/contracts/writer/full.json` + `shared/contracts/evaluator/full.json`. Design spec: `ref/academic-research-skills/docs/design/2026-04-27-ars-v3.6.6-generator-evaluator-contract-design.md` §5.
>
> **Applies to `art-paper full` mode only.** Nine non-full modes (`plan`, `outline-only`, `revision`, `revision-coach`, `abstract-only`, `lit-review`, `format-convert`, `citation-check`, `disclosure`) are byte-equivalent across v3.6.5 → v3.6.6 and do not invoke this protocol. Pipeline boundary unchanged: `art-pipeline` Stage 2 dispatches `art-paper` in plan or full mode (full only invokes this protocol); Stage 3 dispatches the separate `art-reviewer` skill (5-panel external editorial review). The in-pair Phase 6 evaluator under this protocol and the Stage 3 reviewer are different review layers — see design doc §5.1 audit conclusion 2.

### Overview

v3.6.6 splits Phase 4 (writer drafting) and Phase 6 (in-pair evaluator review) into paper-blind / paper-visible call pairs gated by the `writer_full` and `evaluator_full` contracts. The split mirrors `art-reviewer/references/sprint_contract_protocol.md` (the v3.6.2 reviewer pattern) but adapts it for single-agent generator modes that have no panel and (for the writer) no scoring_plan.

The load-bearing mechanism is the **physical separation of calls**: writer Phase 4a never sees the runtime drafting artefacts; evaluator Phase 6a never sees the writer Phase 4b draft. This destroys the "read the paper, then rationalise the standard" drift path on the in-pair self-quality gate.

### Four-call structure

For each `art-paper full` invocation, Phase 4 + Phase 6 expand from two single calls into four separate model calls. Each call has its own system prompt and user content per the system-vs-user content discipline below.

1. **Phase 4a — writer paper-blind pre-commitment.**
   - System prompt: `### Phase 4a — Writer paper-blind pre-commitment` sub-section in `art-paper/agents/draft_writer_agent.md` § "v3.6.6 Generator-Evaluator Contract Protocol".
   - User content: `writer_full` contract JSON + paper metadata only (`title`, `field`, `word_count`).
   - Output: `## Acceptance Criteria Paraphrase` section + terminal `[PRE-COMMITMENT-ACKNOWLEDGED]` tag.
   - Lint: 3 structural checks (see § "Phase 4a / 6a output lint" below).
2. **Phase 4b — writer paper-visible drafting + self-scoring.**
   - System prompt: `### Phase 4b — Writer paper-visible drafting + self-scoring` sub-section in the same agent file.
   - User content: `writer_full` contract JSON (re-injected) + Phase 4a output wrapped in `<phase4a_output>...</phase4a_output>` data delimiter + upstream drafting artefacts (Paper Configuration Record, Paper Outline, Argument Blueprint, Annotated Bibliography, optional Style Profile, optional Knowledge Isolation Directive).
   - Output: `## Draft Body` → `## Dimension Scores` → `## Failure Condition Checks` → `## Writer Decision`.
   - Lint: 4 structural checks (see § "Phase 4b / 6b output lint" below).
3. **Phase 6a — evaluator paper-blind pre-commitment.**
   - System prompt: `### Phase 6a — Evaluator paper-blind pre-commitment` sub-section in `art-paper/agents/peer_reviewer_agent.md` § "v3.6.6 Generator-Evaluator Contract Protocol".
   - User content: `evaluator_full` contract JSON + paper metadata + the writer's most recent `<phase4a_output>` (the writer artefact the evaluator must verify per `disagreement_handling.pre_commitment_check_protocol.check_writer_artifact`).
   - Output: `## Contract Paraphrase` + `## Scoring Plan` (per-dimension `dimension_id` / `what_to_look_for` / `what_triggers_block` / `what_triggers_warn`) + terminal `[PRE-COMMITMENT-ACKNOWLEDGED]` tag.
   - Lint: 5 structural checks.
4. **Phase 6b — evaluator paper-visible scoring + decision.**
   - System prompt: `### Phase 6b — Evaluator paper-visible scoring + decision` sub-section in the same agent file.
   - User content: `evaluator_full` contract JSON (re-injected) + Phase 6a output wrapped in `<phase6a_output>...</phase6a_output>` + the writer's `<phase4a_output>` (unconditional per `pre_commitment_check_protocol.check_writer_artifact`) + the writer Phase 4b draft (the artefact under review).
   - Output: `## Dimension Scores` → `## Failure Condition Checks` → `## Review Body` → `## Evaluator Decision`.
   - Lint: 5 structural checks.

### System prompt vs user content discipline

Mirrors `sprint_contract_protocol.md` §2 reviewer pattern verbatim:

- **System prompt carries invariant policy text only**: the phase sub-section instructions from the agent file's `## v3.6.6 Generator-Evaluator Contract Protocol` block, the lint description, and the phase-boundary tag conventions.
- **User content carries the contract JSON (re-injected per call) plus the runtime inputs allowed at that phase**: paper metadata, `<phase4a_output>` / `<phase6a_output>` delimiter blocks, upstream drafting artefacts, the paper draft.

All dynamic LLM output (Phase Na runtime emissions, paper content) lives in user content via data delimiters, never in the system prompt. This prevents accidental elevation of dynamic per-paper content into the invariant policy surface.

### Schema field name vs runtime emission distinction

`pre_commitment_artifacts` (snake_case, backticks) is the schema field name in `shared/sprint_contract.schema.json` — a configuration declaration in the frozen contract baseline. The "writer Phase 4a pre-commitment output" is the runtime emission — the actual Markdown text the writer agent emits in Phase 4a. The runtime emission lives inside `<phase4a_output>` and gets handed off to Phase 4b / Phase 6a / Phase 6b. Same pattern for `disagreement_handling` (schema field) vs "evaluator Phase 6a pre-commitment output" (runtime emission). Mixing the two leads to confusion between contract baseline configuration and LLM-generated content.

### Phase 4a / 6a output lint

Mode-specific structural check counts, per `sprint_contract_protocol.md` §4 enumeration convention:

- **Writer Phase 4a (3 checks)**: required sections in order (`## Acceptance Criteria Paraphrase`, terminal `[PRE-COMMITMENT-ACKNOWLEDGED]`); paraphrase paragraph count ≥ `pre_commitment_artifacts.acceptance_criteria_paraphrase.minimum_dimensions`; Phase 4a content references contract JSON + paper metadata only. **No `## Scoring Plan` section** — `writer_full` carries no scoring_plan.
- **Evaluator Phase 6a (5 checks)**: required sections in order (`## Contract Paraphrase`, `## Scoring Plan`, terminal `[PRE-COMMITMENT-ACKNOWLEDGED]`); paraphrase paragraph count ≥ `disagreement_handling.paraphrase_minimum_dimensions`; one `### <Dn>: <name>` subsection per acceptance dimension; each scoring_plan subsection contains `disagreement_handling.scoring_plan.per_dimension_criteria` four-field shape (`dimension_id`, `what_to_look_for`, `what_triggers_block`, `what_triggers_warn`); Phase 6a content references contract JSON + paper metadata + the writer's `<phase4a_output>` only (no full draft / paper content).

Retry semantics: lint failure on the first attempt → retry once with the specific lint gap hinted in the system prompt; second failure → mark this role unusable per § "Single-agent generator unusable handling" below.

### Phase 4b / 6b output lint

- **Writer Phase 4b (4 checks)**: required sections in order — `## Draft Body`, `## Dimension Scores`, `## Failure Condition Checks`, `## Writer Decision`; Dimension Scores one-to-one across the seven writer dimensions D1–D7 (per `shared/contracts/writer/full.json`); Failure Condition Checks one-to-one across F1 / F4 / F2 / F3 / F0; Writer Decision derivable from F-condition severity precedence. **No multi-dissent retry** (writer has no scoring_plan to dissent against). **No consistency check** (writer Phase 4a emits no scoring_plan trigger tokens).
- **Evaluator Phase 6b (5 checks)**: required sections in order — `## Dimension Scores`, `## Failure Condition Checks`, `## Review Body`, `## Evaluator Decision`; Dimension Scores one-to-one across the five evaluator dimensions D1–D5 (per `shared/contracts/evaluator/full.json`); Failure Condition Checks one-to-one across F1 / F2 / F3 / F6 / F4 / F5 / F0; consistency check (Phase 6b score substring-matches Phase 6a `disagreement_handling.scoring_plan.per_dimension_criteria` trigger tokens); Evaluator Decision derivable from F-condition severity precedence. **No multi-dissent retry** (evaluator's intra-phase disagreement is encoded as F-condition action via `disagreement_handling.disagreement_resolution`, not as a retry trigger).

Multi-dissent retry remains reviewer-only (`art-reviewer` skill); generator modes have no panel and no scoring_plan dissent anchor.

Lint count summary across the three modes:

| Phase | Reviewer (zero-touch) | Writer | Evaluator |
|---|---|---|---|
| Phase 1 / 4a / 6a | 5 | 3 | 5 |
| Phase 2 / 4b / 6b | 6 | 4 | 5 |

### Single-agent generator unusable handling

When a writer or evaluator phase becomes unusable (Phase Na lint twice fail OR Phase Nb lint fail), `art-paper` emits a phase-level abort tag and routes to user intervention:

- **Writer Phase 4 unusable** → `[GENERATOR-PHASE-ABORTED: role=writer, contract=<id>, reason=<lint_failure_kind>]` → abort `art-paper` Phase 4 → user intervention decides retry / fallback / regression to Phase 3 (Argument Blueprint).
- **Evaluator Phase 6 unusable** → `[GENERATOR-PHASE-ABORTED: role=evaluator, contract=<id>, reason=<lint_failure_kind>]` → abort `art-paper` Phase 6 → user intervention decides retry / fallback / regression to Phase 5 (Drafting completion).

`[GENERATOR-PHASE-ABORTED]` does **not** constitute a valid Phase 6b emission and cannot enter Stage 3 reviewer dispatch. Two valid Stage 3 entry paths exist (per design doc §5.1):

- **Standard path**: evaluator Phase 6b emits F0 `evaluator_decision=accept` or F4 `evaluator_decision=accept_with_dissent_note`.
- **Exceptional path**: evaluator Phase 6b emits F5 `evaluator_decision=flag_for_reviewer_stage` after the in-pair revision loop exhausts at round 2 with mandatory-dimension block recurring.

`art-paper` carries no panel cardinality invariant for writer / evaluator (no `panel_size` field — Schema 13.1 §3.3.5 reviewer-conditional). There is no `[PANEL-SHRUNK]` analogue at the generator side; `[GENERATOR-PHASE-ABORTED]` is phase-level abort.

**Operational monitor**: track `[GENERATOR-PHASE-ABORTED]` rate over the first three months of v3.6.6 deployment. The denominator is **per `art-paper full` run** — one user-perceived top-level invocation. The 5% threshold is `(runs_with_any_abort) / (total_runs)`. If the rate exceeds 5%, v3.6.7 introduces graceful-degradation fallback (see § "Known limitations" below).

### Cross-session resume scope

The v3.6.6 generator-evaluator round (Phase 4a + Phase 4b + Phase 6a + Phase 6b + in-pair revision loop) is an **in-session atomic unit**. Manual session split mid-round → writer Phase 4a output is lost; new session must restart `art-paper full` mode from Phase 0.

The v3.6.3 `CRS_PASSPORT_RESET=1` `reset_boundary[]` mechanism (per `art-pipeline/references/passport_as_reset_boundary.md`) operates at `art-pipeline` Stage boundaries, not at `art-paper` internal phase boundaries. `art-paper` internal phases (4a / 4b / 6a / 6b) are **not** boundary points; no `kind: boundary` ledger entry is emitted between them. v3.6.7+ may introduce `pre_commitment_history[]` to persist writer Phase 4a artefacts across sessions if operational data warrants — see § "Known limitations" below.

## Known limitations

- **No graceful-degradation fallback in v3.6.6**: when the writer or evaluator phase aborts via `[GENERATOR-PHASE-ABORTED]`, `art-paper full` aborts and routes to user intervention. v3.6.7 may introduce a fallback that degrades the affected phase to v3.6.5 single-call behaviour and logs the degradation. v3.6.6 ships with abort-only behaviour. See § "Single-agent generator unusable handling" above for the operational 5% / three-month monitor.
- **No cross-session resume mid-round**: the four-phase generator-evaluator round is an in-session atomic unit. Manual session split mid-round loses the writer Phase 4a artefact and forces restart from Phase 0. v3.6.7+ may introduce a `pre_commitment_history[]` ledger entry in Schema 9 to persist the writer Phase 4a artefact across session boundaries; v3.6.6 does not implement.
- **In-pair Phase 6 evaluator vs `art-reviewer` external review**: the in-pair `peer_reviewer_agent` (Phase 6 evaluator with the v3.6.6 contract gate) and the standalone `art-reviewer` skill (Stage 3 5-panel external editorial review) serve different review layers and remain documented as known technical debt per design doc §1 known limitations. Routing / merge decisions are deferred to v3.7.x.

## Operational Modes (12 Modes)

See `references/mode_selection_guide.md` for details.

| Mode | Trigger | Agents | Output |
|------|---------|--------|--------|
| `full` | "Write a paper" | All 9 (+ 11 if quantitative) | Complete paper draft (with figures if applicable) |
| `outline-only` | "Paper outline" | 1->2->3 | Detailed outline + evidence map |
| `revision` | "Revise paper" | 8->5->6 | Revised draft with tracked changes (uses `templates/revision_tracking_template.md`) |
| `abstract-only` | "Write abstract" | 1->7 | Abstract + keywords (English; bilingual machinery inherited but not v0.1 default) |
| `lit-review` | "Literature review" | 1->2 | Annotated bibliography + synthesis |
| `format-convert` | "Convert to LaTeX" / "Convert citations to [format]" | 9 only | Formatted document; includes citation format conversion (APA 7 / Chicago / MLA / IEEE / Vancouver) |
| `citation-check` | "Check citations" | 6 only | Citation error report |
| `plan` | "guide my paper" / "help me plan my paper" | 1->10->3->4 | Chapter Plan + INSIGHT Collection |
| `revision-coach` | "parse reviews" / "revision roadmap" / "I got reviewer comments" | 12 only | Revision Roadmap + optional Tracking Template + Response Letter Skeleton |
| **`disclosure`** (v3.2) | **"AI disclosure for SIGGRAPH Asia" / "generate AI usage statement"** | **9 only** | **Two-channel (AI-to-make-the-artwork vs. AI-to-write-the-paper) venue-specific AI-usage disclosure paragraph(s) + placement instructions** |
| **`artist-statement`** | **"artist statement" / "project description"** | **1->2->3 (Pattern 2)** | **Short concept-forward artist statement / project description for a single work: provocation, work (form/experience/media), concept, essential making gesture, significance; credits + ACM Reference Format references** |
| **`work-doc`** | **"document my artwork" / "exhibition record"** | **1->visualization** | **Artwork documentation layout: work stills, install/exhibition photos, system/process diagrams, media frames with image-credit/courtesy lines; venue+date as the L3 locator for artwork citations; acmart `\includegraphics` integration** |

### Quick Mode Selection Guide

| Your Situation | Recommended Mode | Spectrum |
|----------------|-----------------|----------|
| Starting from scratch with a clear RQ | `full` | balanced |
| Need help planning before writing | `plan` | originality |
| Just need an outline | `outline-only` | balanced |
| Have a draft, received review feedback | `revision` | fidelity |
| Have unstructured reviewer comments | `revision-coach` | balanced |
| Just need an abstract | `abstract-only` | fidelity |
| Need to check/fix citations | `citation-check` | fidelity |
| Need to convert format (LaTeX, DOCX) or citation style | `format-convert` | fidelity |
| Want a systematic literature review paper | `lit-review` | fidelity |
| Need a venue-specific AI-usage disclosure statement for submission | `disclosure` | fidelity |
| Need a short artist statement / project description for a single work | `artist-statement` | fidelity |
| Need to lay out artwork documentation (figures, install/exhibition record) | `work-doc` | fidelity |

**Spectrum** (v3.2): *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light. See `shared/mode_spectrum.md` for the full cross-skill spectrum table.

Not sure? Start with `plan` — it will guide you step by step. `disclosure` is a finishing step — run it after the paper is drafted, targeting the venue you plan to submit to.

### Mode Selection Logic

> See `references/mode_selection_guide.md` for trigger-to-mode mappings and the full selection flowchart.

---

## Plan Mode: Chapter-by-Chapter Guided Planning

Socratic mode that guides users through paper planning one chapter at a time. Builds a complete Paper Blueprint through structured dialogue.

> See `references/plan_mode_protocol.md` for the full chapter-by-chapter dialogue flow and Paper Blueprint structure.

---

## Handoff Protocol: art-inquiry -> art-paper

`intake_agent` automatically detects art-inquiry materials (RQ Brief / Bibliography / Synthesis / INSIGHT Collection) and skips redundant steps. See `art-inquiry/SKILL.md` Handoff Protocol for the complete handoff material format.

---

## Failure Paths

See `references/failure_paths.md` for details. Quick reference:

| Failure Scenario | Handling Strategy |
|---------|---------|
| Insufficient research foundation | Recommend running `art-inquiry` first |
| Wrong paper structure selected | Return to Phase 2, suggest alternative structure |
| Word count significantly over/under target | Identify problematic chapters, suggest trimming/expansion |
| Citation format entirely wrong | Re-run the entire citation phase |
| Peer review rejection | Analyze rejection reasons, suggest major revision or restructuring |
| Plan mode not converging | Suggest switching to outline-only mode |
| Incomplete handoff materials | List missing items, suggest supplementing or re-running |
| User abandons midway | Save completed Chapter Plan |

---

## Full Academic Pipeline

See `art-pipeline/SKILL.md` for the complete workflow.

---

## Phase 0: Configuration Interview

See `agents/intake_agent.md` for the complete field definitions of the Phase 0 configuration interview. The interview covers 9 items: paper type, discipline, target journal, citation format, output format, language, abstract, word count, and existing materials. Outputs a Paper Configuration Record, awaiting user confirmation.

---

## File Structure

**Agent definitions**: `agents/{agent_name}.md` — one file per agent (12 total, matching Agent Team table above).

**References** (19 files in `references/`):
- Citation: ACM Reference Format is the default — see `shared/references/acm_reference_format.md`. Alternate-format guides retained here: `apa7_extended_guide`, `citation_format_switcher` (these cover non-ACM venues; ACM remains the default).
- Writing: `academic_writing_style`, `writing_quality_check`, `writing_judgment_framework`
- Structure: art-paper structure patterns live in `shared/references/art_paper_structure_patterns.md` (5 patterns, default Practice-Based Art Paper). Local `paper_structure_patterns` is the inherited empirical pattern set, retained only for the Pattern 5 art-science hybrid. Also `abstract_writing_guide`.
- Domain: art-genre vocabulary is `shared/references/creative_art_terminology_glossary.md`; also `journal_submission_guide`, `latex_template_reference`
- Process: `failure_paths` (12 scenarios), `mode_selection_guide` (10 modes), `plan_mode_protocol`, `workflow_phase_details`
- Ethics / credit: `credit_authorship_guide` (CRediT roles + art collaboration/credit), `funding_statement_guide`, `statistical_visualization_standards` (applies only to Pattern 5 hybrids with genuine quantitative results)
- Disclosure (v3.2): `disclosure_mode_protocol` (two-channel AI-usage statement generation), `venue_disclosure_policies` (verify against the current SIGGRAPH Asia Art Papers CFP; the inherited entries for empirical venues are retained as alternates)
- Also: `art-inquiry/references/apa7_style_guide.md` (base reference for the APA alternate)

**Templates** (10 files in `templates/`): `imrad`, `literature_review`, `case_study`, `theoretical_paper`, `policy_brief`, `conference_paper`, `latex_article_template.tex`, `credit_statement`, `funding_statement`, `revision_tracking` (4 status types).

**Examples** (5 files in `examples/`), all practice-based art scenarios: `imrad_hei_example` (Pattern 5 art-science hybrid — interactive installation), `literature_review_example` (thematic review of precedent artworks + discourse), `plan_mode_guided_writing` (Socratic section-by-section planning of a Practice-Based Art Paper), `revision_mode_example` (responding to art-jury comments), `revision_recovery_example` (Major Revision recovery with a DA-CRITICAL + DELIBERATE_LIMITATION).

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes:

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **AI-typical overused terms** | "delve into", "crucial", "it is important to note" = instant AI detection | Use discipline-specific vocabulary; see `references/writing_quality_check.md` |
| 2 | **Em dash abuse** | More than 2 em dashes per page signals AI writing | Use parentheses, commas, or restructure the sentence |
| 3 | **Throat-clearing openers** | "In this section, we will discuss..." adds no information | Start with the claim or finding directly |
| 4 | **Uniform paragraph lengths** | Every paragraph is 4-5 sentences = monotonous AI rhythm | Vary paragraph length naturally (2-8 sentences) |
| 5 | **⚠️ IRON RULE: Fabricated citations** | Inventing plausible-sounding references that don't exist | Every citation must be verified via DOI or WebSearch; see `art-pipeline/agents/integrity_verification_agent.md` |
| 6 | **Sycophantic revision** | Accepting all reviewer feedback without critical evaluation | Use REVIEWER_DISAGREE status when reviewer is wrong; justify with evidence |
| 7 | **Scope creep during revision** | Adding unrequested sections/analyses to "improve" the paper | Revision addresses reviewer concerns only; new content requires explicit user approval |
| 8 | **Ignoring failure paths** | Continuing despite desk-reject signals or fatal methodology flaws | Check `references/failure_paths.md`; invoke F11 Desk-Reject Recovery when triggered |

---

## Quality Standards

### Writing Quality
1. **Every claim must be anchored** — to a citation (ACM Reference Format) or to one of the art-research evidence types (the work as encountered, process/making, exhibition/reception, conceptual lineage, situated reflection); see `shared/references/art_research_evidence_model.md`. Reception claims need an observable anchor (named venue/date + observable detail); novelty/technical-capability claims need an anchor or a hedge.
2. **Zero citation orphans** — in-text citations <-> reference list must perfectly match
3. **Consistent register** — academic tone appropriate for the discipline
4. **Logical flow** — clear transitions between paragraphs and sections
5. **Word count compliance** — within +/-10% of target

### Abstract Quality
6. **Component coverage** — covers the 5 art-paper components (work / provocation / making / insight / contribution) per `art-paper/agents/abstract_agent.md`
7. **Keywords** — 4-6 (Pattern 1 default; 3-5 for Pattern 2); none duplicate the title
8. **Word count** — Pattern 1: 120-200 words; up to 300 for Pattern 5
9. **Honesty** — no reception inflation; medium label honest (no "autonomous" for a scripted sequence)

### Citation Quality
10. **Format compliance** — 100% adherence to selected citation style
11. ⚠️ IRON RULE: **DOI inclusion** — every source with a DOI must include it; every citation must be verified via DOI or WebSearch
12. **Currency** — flag sources older than 10 years (unless seminal works)
13. **Self-citation ratio** — flag if >15%

### Peer Review
14. **Five dimensions** — Originality (20%), Methodological Rigor (25%), Evidence Sufficiency (25%), Argument Coherence (15%), Writing Quality (15%)
15. **Actionable feedback** — every criticism must include a specific suggestion
16. **Max 2 revision rounds** — unresolved items become Acknowledged Limitations

### Mandatory Inclusions
⚠️ **IRON RULE**: Every art paper MUST include: Author Contributions / collaboration credit (named roles), image credit / courtesy lines for documentation, copyright & exhibition-rights acknowledgement where applicable, Conflict of Interest Statement, and Funding/Support Acknowledgment. (A Data Availability Statement applies only to Pattern 5 art-science hybrids that produce a genuine dataset.)
17. **Two-channel AI-usage disclosure** — every paper must disclose AI used to MAKE the artwork and AI used to WRITE the paper, per venue policy; verify against the current SIGGRAPH Asia Art Papers CFP. See `shared/references/siggraph_acm_disclosure.md`.
18. **Limitations / open questions** — explicitly discuss the bounds of the situated insight (honest specificity over claimed generalizability)
19. **Ethics / consent statement** — when applicable (audience sensing, identifiable persons in documentation, community archives, sensitive material)

---

## Output Language

User-facing dialogue follows the user's language. The paper itself is produced in English (art-paper v0.1 default for SIGGRAPH Asia Art Papers / ACM venues). The bilingual-abstract machinery is inherited from ARS but is not the v0.1 default; verify against the current CFP.

---

## Integration with Other Skills

```
art-paper + art-inquiry        -> Concept/positioning phase -> art-paper writing phase (auto-handoff)
art-paper + report-to-website    -> Interactive web version of the paper
art-paper + notebooklm-slides-generator -> Presentation slides from paper
art-paper + art-reviewer -> Peer review -> revision loop
```

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 0.1.0 |
| Last Updated | 2026-05-22 |
| Maintainer | art-paper maintainer (withheld during double-blind review) |
| Dependent Skills | art-inquiry v1.0+ (upstream), art-reviewer v1.0+ (downstream) |

---

## Version History

> See `references/changelog.md` for full version history.
