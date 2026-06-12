# Mode Registry

Single source of truth for all modes across the art-paper suite. **27 modes** across 4 skills.

art-paper is forked from academic-research-skills (ARS) v3.9.4.2 and re-specialized for practice-based art research papers across art-and-technology venues (default reference target: SIGGRAPH Asia Art Papers track). When adding or modifying modes, update this file first — SKILL.md files and CLAUDE.md should reference this registry.

Last updated: v0.1.0 (2026-05-22)

---

## art-inquiry (7 modes)

| Mode | Spectrum | Output | Oversight | Triggers |
|------|----------|--------|-----------|----------|
| `full` | Balanced | ACM-formatted inquiry report | High | "investigate [topic]", "deep inquiry", "art-research analysis" |
| `quick` | Fidelity | Inquiry brief | Medium | "quick brief", "precedent summary", "quick inquiry" |
| `review` | Balanced | Reviewer report on provided text | High | "review this art paper", "evaluate this work", "assess this source" |
| `lit-review` | Fidelity | Annotated bibliography + synthesis (precedent works + theory) | Medium | "literature review", "annotated bibliography" |
| `fact-check` | Fidelity | Claim-by-claim verification report | Medium | "verify claims", "fact-check", "evidence verification" |
| `socratic` | Originality | Concept & Provocation Brief + INSIGHT collection | Very High | "guide my inquiry", "help me think through the concept", "I'm not sure what the work is about" |
| `systematic-review` | Fidelity | PRISMA 2020 report | Medium | "systematic review", "meta-analysis", "PRISMA" |

## art-paper (12 modes)

| Mode | Spectrum | Output | Oversight | Triggers |
|------|----------|--------|-----------|----------|
| `full` | Balanced | Complete art-paper draft (Practice-Based Art Paper or art-pattern-appropriate) | High | "write an art paper", "SIGGRAPH Asia paper", "practice-based paper" |
| `plan` | Originality | Section Plan + INSIGHT collection (Socratic) | Very High | "guide my art paper", "help me plan", "step by step paper" |
| `outline-only` | Balanced | Detailed outline + evidence map (artwork-as-evidence) | High | "art-paper outline", "just need an outline" |
| `revision` | Fidelity | Revised draft + point-by-point jury responses | High | "revise paper", "incorporate jury feedback" |
| `revision-coach` | Balanced | Revision Roadmap + Response Letter Skeleton | Medium | "parse jury comments", "I got jury comments" |
| `abstract-only` | Fidelity | Abstract + keywords (English; art-paper v0.1 default — bilingual machinery inherited but not v0.1 default) | Medium | "write abstract" |
| `lit-review` | Fidelity | Annotated bibliography in paper format | Medium | "literature review paper", "write a lit review" |
| `format-convert` | Fidelity | Formatted document (acmart LaTeX/DOCX-via-Pandoc/PDF/MD) | Low | "convert to acmart LaTeX", "convert citations to ACM" |
| `citation-check` | Fidelity | Citation error report | Low | "check citations", "verify references" |
| `disclosure` | Fidelity | Venue-specific AI-usage disclosure (two-channel) | Low | "AI disclosure for SIGGRAPH Asia", "generate AI usage statement" |
| `artist-statement` | Originality | Artist statement for the work | High | "draft an artist statement", "write my artist statement" |
| `work-doc` | Balanced | Artwork documentation (materials, process, exhibition record) | Medium | "document this artwork", "work documentation", "process documentation" |

## art-reviewer (6 modes)

The jury simulates the SIGGRAPH Asia Art Papers panel: **Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate**.

| Mode | Spectrum | Output | Oversight | Triggers |
|------|----------|--------|-----------|----------|
| `full` | Balanced | 5 jury reports + Editorial Decision + Revision Roadmap | High | "review art paper", "jury review", "manuscript review" |
| `re-review` | Fidelity | Revision verification checklist + residual issues | Medium | "check revisions", "verification review" |
| `quick` | Fidelity | Chair quick assessment + key issues list | Low | "quick review", "quick look" |
| `realization-focus` | Fidelity | In-depth technical-realization review | Medium | "check the realization", "focus on the technical implementation" |
| `guided` | Originality | Socratic issue-by-issue dialogue | Very High | "guide me to improve", "walk me through issues" |
| `calibration` | Fidelity | Calibration Report (FNR/FPR/AUC) + confidence disclosure | Medium | "calibrate jury", "measure reviewer accuracy" |

## art-pipeline (1 orchestrator + 1 resume mode)

| Mode | Spectrum | Output | Oversight | Triggers |
|------|----------|--------|-----------|----------|
| (pipeline) | Balanced | 10-stage orchestrated workflow | Very High | "art pipeline", "inquiry to paper", "full art-paper workflow" |
| `resume_from_passport=<hash>` | Fidelity | Resume a prior pipeline run from a Material Passport reset boundary. Opt-in (`CRS_PASSPORT_RESET=1`). See `art-pipeline/references/passport_as_reset_boundary.md`. | High | "resume from passport", "continue pipeline from reset boundary" |

---

## Summary

| Metric | Count |
|--------|-------|
| Total modes | 27 |
| Fidelity | 15 |
| Balanced | 8 |
| Originality | 4 |

### Oversight levels

| Level | Meaning |
|-------|---------|
| Very High | User-led dialogue or mandatory checkpoints at every stage |
| High | User confirms key decisions (concept, outline, configuration) |
| Medium | Structured format with limited decision points |
| Low | Mechanical/template-driven, minimal human input |
