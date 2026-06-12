# Art-Paper for Claude Code

[![Version](https://img.shields.io/badge/version-v0.1.1-blue)](https://github.com/joonhyungbae/art-paper/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

> 🌐 [한국어 README](README.ko-KR.md)

A Claude Code plugin for **practice-based art research papers** — the full pipeline from concept to a juried, publication-ready manuscript, across art-and-technology venues. Its scope is the *genre*, not a single venue; the methodology and integrity checks are venue-agnostic. Default reference target: the **SIGGRAPH Asia Art Papers track** (ACM Digital Library), wired to `acmart` + ACM Reference Format. Alternate venues are supported via citation-format conversion (APA 7.0, Chicago, MLA 9, IEEE, Vancouver) and the five art-paper structure patterns; verify venue specifics against the current CFP.

The artwork is **primary evidence**, not data. art-paper scaffolds the parts AI does well — precedent search, ACM citation formatting, structural conventions, claim anchoring — so you can focus on what only an artist-researcher can do: framing the provocation, making the work, deciding what the practice reveals.

---

## Install in 30 seconds

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

Then try `/art-plan` and describe your work — art-paper will walk you through the structure (context → conceptual framework → the work → realization → reflection) via Socratic dialogue. For a single-shot test instead, `/art-lit-review "your topic"`.

**👉 [Wiki — apesuite.org/plugins/art-paper](https://apesuite.org/plugins/art-paper/)** — bilingual user docs (EN + 한국어): getting started, three entry points, the four skills, the methodology concepts, and the *Cutting Kim* worked example end-to-end.

**👉 [docs/SETUP.md](docs/SETUP.md)** — prerequisites (Claude Code, `ANTHROPIC_API_KEY`, optional Pandoc / LaTeX `tectonic` + ACM `acmart` for canonical PDF), API key, optional cross-model verification (`CRS_CROSS_MODEL` — inherited env-var name from the parent suite), and all install methods.

---

## What art-paper gives you

Four skills covering inquiry → write → jury review → orchestrate, plus an art-research genre layer.

- **art-inquiry** — concept articulation, positioning, practice-based / practice-led methodology, precedent works + theory. Socratic mode draws out the artistic provocation; intent detection prevents premature convergence.
- **art-paper** — art-paper drafting in Pattern 1 (Practice-Based Art Paper) by default; ACM Reference Format; **acmart LaTeX → PDF** output; dedicated `artist-statement` and `work-doc` modes for artwork documentation.
- **art-reviewer** — SIGGRAPH Asia Art Papers jury simulation: **Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate**, with 0–100 rubrics and a calibration mode that measures the jury's own FNR / FPR against a user-supplied gold set.
- **art-pipeline** — 10-stage orchestrator with two integrity gates (Stage 2.5 + 4.5) scoped to **artwork / realization claim verification**: reception claims need an observable anchor, novelty and technical-capability claims need an anchor or a hedge.

The **art-research genre layer** (`shared/references/`): the artwork as primary evidence; 5 art-paper structure patterns; ACM Reference Format with venue+date locators for artwork/exhibition citations; **two-channel AI disclosure** (AI used to *make* the artwork vs. AI used to *write* the paper).

**👉 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — flow diagram, stage-by-stage matrix, agents, quality gates.

---

## AI as copilot, not pilot

art-paper won't write your paper for you. It does the scaffolding — precedent search, ACM citation, claim anchoring, genre conventions — so you do the parts that require an artist-researcher.

Unlike a humanizer, art-paper does not hide your AI use. **Style Calibration** learns your voice from past work, **Writing Quality Check** catches AI-typical patterns to improve prose (not to evade detection), and the two AI-use channels (artwork-making vs paper-writing) are disclosed separately per venue policy.

### Structural limits art-paper handles

Three failure modes emerge in any AI-assisted writing pipeline:

1. **Frame-lock** — ask the AI to challenge its own thesis and every round stays inside the frame you set. The Devil's Advocate attacks arguments, never premises.
2. **Sycophancy under pushback** — the model concedes too quickly when pressed, treating "the user pushed back" as evidence the attack was wrong rather than as persistence.
3. **Intent misdetection** — the Socratic mentor tries to converge and produce deliverables when you are still exploring.

art-paper makes these visible and manageable (the mitigations are genre-neutral and inherited unchanged from the parent suite):

- **Concession Threshold Protocol** — DA scores every rebuttal 1–5; concession only at ≥4 (rebuttal directly addresses the core attack with evidence); no consecutive concessions; concession rate + frame-lock detection at every checkpoint.
- **Intent Detection Layer** — Socratic mentor classifies exploratory vs goal-oriented every 3 turns; exploratory mode disables auto-convergence and prohibits "want me to summarize?" prompts.
- **Dialogue Health Indicator** — silent self-assessment every 5 turns for persistent agreement / conflict avoidance / premature convergence; auto-injects challenges when agreement pattern detected.

Full 7-mode AI failure-mode checklist: [`art-pipeline/references/ai_research_failure_modes.md`](art-pipeline/references/ai_research_failure_modes.md). The Stage 2.5 / 4.5 integrity gates run this checklist as a blocking check.

### Citation faithfulness

art-paper retains the L3 citation-faithfulness machinery: trust-chain provenance + locator anchors per citation, with an opt-in audit pass (`CRS_CLAIM_AUDIT=1` — env-var name inherited from the parent suite) that fetches each cited source and judges whether the claim is actually supported. Five HIGH-WARN classes gate-refuse output through the formatter (claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited).

For art papers, the *rendered* citation format is ACM Reference Format; artwork and exhibition citations use **venue+date** as the locator, not DOIs (which would be fabricated for unindexed work).

> Motivation: Lu et al. (2026, *Nature* 651:914-919) — *The AI Scientist* showed that even autonomous-pipeline papers can pass through workshop peer review carrying failure modes (implementation bugs, hallucinated results, frame-lock, citation hallucinations). Zhao et al. (2026-05, [arXiv:2605.07723](https://arxiv.org/abs/2605.07723)) audited 111M references across arXiv / bioRxiv / SSRN / PMC and estimated ~147K hallucinated citations for 2025 alone. art-paper treats this as architectural, not as a per-paper concern.

---

## Usage

### Quick Start

```
# Full art-paper pipeline
You: "I want to write a SIGGRAPH Asia art paper about my generative-art installation"

# Socratic guidance for the concept
You: "Guide my inquiry into the conceptual provocation of my interactive net-art piece"

# Guided paper writing
You: "Guide me through writing a paper documenting my bio-art work"

# Review an existing paper
You: "Review this art paper" (then provide the paper)

# Check pipeline status
You: "status"
```

### Individual skills

#### art-inquiry (7 modes)

```
"Investigate the lineage of real-time generative art"   → full mode
"Give me a quick brief on media-art precedents for X"    → quick mode
"Do a systematic review of interactive-installation HCI" → systematic-review mode
"Guide my inquiry into the concept behind my work"       → socratic mode (guided)
"Fact-check these precedent and technical claims"        → fact-check mode
"Do a literature review on net-art theory"               → lit-review mode
"Review this art paper's research quality"               → review mode
```

#### art-paper (12 modes)

```
"Write an art paper about X"                          → full mode
"Guide me through writing my art paper"               → plan mode (guided)
"Build an art-paper outline"                          → outline-only mode
"I have a draft, here are the jury comments"          → revision mode
"Parse these jury comments into a roadmap"            → revision-coach mode
"Write an abstract for this art paper"                → abstract-only mode
"Turn this into a literature review on art + tech"    → lit-review mode
"Convert to acmart LaTeX" / "Convert citations to ACM" → format-convert mode
"Check citations"                                     → citation-check mode
"Generate an AI-usage disclosure for SIGGRAPH Asia"   → disclosure mode
"Draft an artist statement for this work"             → artist-statement mode
"Document this artwork (materials, process, exhibition)" → work-doc mode
```

#### art-reviewer (6 modes)

```
"Review this art paper"                               → full mode (Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate)
"Quick assessment of this art paper"                  → quick mode
"Guide me to improve this art paper"                  → guided mode
"Focus on the technical realization"                  → realization-focus mode
"Verify the revisions"                                → re-review mode
"Calibrate this jury against my gold set"             → calibration mode
```

#### art-pipeline (Orchestrator)

```
"I want to write a complete SIGGRAPH Asia art paper"  → full pipeline from Stage 1
"I already have an art paper, review it"              → mid-entry at Stage 2.5 (integrity first)
"I received jury comments"                            → mid-entry at Stage 4
```

> The pipeline ends with **Stage 6: Process Summary** — auto-generated creation-process record with a 6-dimension Collaboration Quality Evaluation (1–100).

### Languages

- **English** (default) and **Korean** READMEs (`README.ko-KR.md`). Socratic mode (art-inquiry) and Plan mode use **intent-based activation** that works across languages — they detect meaning, not specific keywords. If trigger matching is unreliable in your language, add keywords to the `### Trigger Keywords` block in the relevant `SKILL.md`.

### Citation formats

- **ACM Reference Format** (default; acmart `ACM-Reference-Format.bst`; biblatex `acmnumeric` / `acmauthoryear`). Artwork and exhibition entries use venue+date as the locator rather than a DOI.
- APA 7.0, Chicago (Notes & Author-Date), MLA, IEEE, Vancouver — supported alternates for non-ACM venues or art-science hybrids.

### Paper structures

The artwork is primary evidence; structures center on the work rather than IMRaD. See [`shared/references/art_paper_structure_patterns.md`](shared/references/art_paper_structure_patterns.md).

- **Practice-Based Art Paper** (default) — context → conceptual framework → the work → realization → reflection
- Process / Documentation paper
- Conceptual / Theoretical art-and-technology essay
- Exhibition / Curatorial case study
- IMRaD — retained only as the art-science hybrid pattern

---

## Skill details

Per-agent responsibilities and per-stage artifacts: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

### art-inquiry (v0.1.1)

Concept articulation, positioning, practice-based / practice-led methodology, lineage of precedent works and theory. Modes: full, quick, review, lit-review, fact-check, socratic, systematic-review. Optional cross-model Devil's Advocate; Semantic Scholar API verification (for theory / precedent literature).

### art-paper (v0.1.1)

Art-paper authoring. Output: **acmart LaTeX → PDF** (canonical; default class option `sigconf`, verify against the current Art Papers CFP) + MD + DOCX (via Pandoc when available). **IRON RULE:** PDF compiled from LaTeX, never HTML-to-PDF. Modes: full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure, **artist-statement**, **work-doc**. Style Calibration, Writing Quality Check, anti-leakage protocol, VLM figure verification for documentation images.

### art-reviewer (v0.1.1)

Multi-perspective jury review with **0–100 quality rubrics**. The jury simulates the SIGGRAPH Asia Art Papers panel: **Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate**. Modes: full, re-review, quick, realization-focus, guided, calibration. Decision mapping: ≥80 Accept, 65–79 Minor Revision, 50–64 Major Revision, <50 Reject — the final acceptance is the venue's; verify against the current CFP. Read-only constraint; concession-threshold + attack-intensity preservation; optional cross-model DA critique.

### art-pipeline (v0.1.1)

10-stage orchestrator. Every stage requires a user-confirmation checkpoint; integrity verification (Stage 2.5 + 4.5, scoped to **artwork / realization claim verification**) cannot be skipped; the Revision Traceability Matrix (Schema 11) independently verifies revision claims. The **Collaboration Depth Observer** (advisory only — never blocks) runs at FULL/SLIM checkpoints and pipeline completion. Compliance Agent (PRISMA-trAIce + RAISE) runs at the integrity gates.

---

## Performance & cost

**👉 [docs/PERFORMANCE.md](docs/PERFORMANCE.md)** — per-mode token budgets, full-pipeline cost estimate, recommended Claude Code settings (Skip Permissions; Agent Team optional). Word-allocation and the exact Art Papers length budget should be verified against the current SIGGRAPH Asia Art Papers CFP.

---

## License

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Share + adapt + attribute, non-commercial use only.

**Attribution format:**

```
art-paper, forked from Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## Provenance & contributors

**Maintainer — [Joonhyung Bae](https://github.com/joonhyungbae)** (KAIST). The art-research specialization (genre layer, the SIGGRAPH Asia jury, two-channel AI disclosure, acmart output) is the work of an exhibiting artist, author of practice-based art papers at peer-reviewed venues, and AI researcher. A companion methodology paper on the evaluation framework is in preparation; the plugin is released ahead of that paper and is usable on its own terms.

**Upstream — Academic Research Skills (ARS).** art-paper is forked from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 by [Cheng-I Wu (吳政宜)](https://github.com/Imbad0202). The genre-neutral pipeline machinery (Material Passport handoff, L3 citation-faithfulness gate, generator-evaluator contract, integrity gates, anti-sycophancy / DA scoring, Collaboration Depth Observer) is inherited unchanged. A pristine ARS reference is kept at `ref/academic-research-skills/` for diffing. Fork design: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

**Upstream contributors** whose ARS-era work art-paper continues to benefit from: [@aspi6246](https://github.com/aspi6246) (read-only constraint + anti-pattern codification patterns), [@mchesbro1](https://github.com/mchesbro1) and [@cloudenochcsis](https://github.com/cloudenochcsis) (reviewer reference lists), [@eltociear](https://github.com/eltociear) and [@xpfo-go](https://github.com/xpfo-go) (upstream README translations).

---

## Changelog

> Entries below v0.1.0 are the inherited **academic-research-skills (ARS)** changelog, retained as provenance. They describe the parent suite's history prior to the art-paper fork.

### v0.1.1 (2026-06-13) — install hardening, naming, *Cutting Kim* worked example

> Initial public release. Pre-release history collapsed to a single starting commit; the per-version detail below is preserved in [`CHANGELOG.md`](CHANGELOG.md) and continues from the upstream provenance in `ref/academic-research-skills/CHANGELOG.md`.

- **Install defect fix.** `skills/` symlinks repointed from the broken fork-period `creative-*` names to `../art-{inquiry,paper,pipeline,reviewer}`; a fresh clone now registers all four core skills via the conventional `skills/` discovery path.
- **Manifest accuracy.** `marketplace.json` description aligned to the actual count (27 mode entries: art-inquiry 7, art-paper 12, art-reviewer 6, art-pipeline orchestrator + cross-session resume = 2). `MODE_REGISTRY.md` "creative pipeline" trigger leftover replaced with "art pipeline".
- **Citation-format wiring.** Custom post-`bibtex` passes (in the `art-paper_paper` working tree, applicable elsewhere too) ensure Emerald Harvard's `pp.X-Y` full-form page ranges, italic `et al.`, and DOI URLs render correctly when `agsm.bst` drops the `doi` field.
- **Suite name normalisation.** Removed the fork-period label "Creative Research Skills" everywhere user-facing (wiki, `mkdocs` site title, FAQ, citation BibTeX, skeleton example). The plugin's name is **Art-Paper**.
- **Korean wording.** Replaced the literal upstream/downstream calque "상류/하류" with "선행/후속" in the Korean wiki.
- ***Cutting Kim* worked example.** Added a featured reconstruction-benchmark walkthrough on the authors' own SIGGRAPH Asia 2025 art paper (T = 0.2568 / G = 0.1261, margin +0.13, contamination 0.003 `ok`). Standard + clean-control variants both included; the clean-control collapses the margin to −0.019, an honest signature of the input-pack-extraction artifact size.
- **Sanity test suite.** 11 stdlib-only regression guards in `tests/` covering skills/ symlink resolution, manifest version sync, marketplace mode-count claim, "Creative Research Skills" / "Emerald Harvard" / fork-period-path wiki regressions, and a smoke test of `eval/instrumentation.py` on the bundled synthetic fixture.

### v0.1.0 (2026-05-22) — art-paper fork (art-paper specialization)

> Forked from ARS v3.9.4.2. Re-specializes the 4-skill suite from empirical scientific papers to **practice-based art research papers** targeting the **SIGGRAPH Asia Art Papers track** (proceedings on the ACM Digital Library; verify category/venue against the current CFP). The genre-neutral pipeline skeleton is inherited unchanged; the empirical-science genre layer is replaced with an art-research genre layer.

- **4 skills renamed:** `deep-research` → `art-inquiry`, `academic-paper` → `art-paper`, `academic-paper-reviewer` → `art-reviewer`, `academic-pipeline` → `art-pipeline`. History preserved via `git mv`.
- **Slash commands** renamed `ars-*` → `art-*` and extended to 15 with two new `art-paper` modes: **artist-statement** and **work-doc** (artwork documentation).
- **Genre layer replaced** in `shared/references/`: `art_paper_structure_patterns.md` (default Practice-Based Art Paper; IMRaD demoted to the art-science hybrid pattern), `art_research_evidence_model.md` (artwork is primary evidence — triangulate work / process / exhibition / lineage / reflection), `acm_reference_format.md` (ACM Reference Format default, replacing APA 7.0), `siggraph_acm_disclosure.md` (two-channel AI disclosure), `creative_art_terminology_glossary.md` (replacing the IRB + psychometric glossaries).
- **Output toolchain:** canonical output moves to **acmart LaTeX → PDF** via the ACM `acmart` document class (default class option `sigconf`, a CFP-verified setting). IRON RULE preserved: PDF compiled from LaTeX, never HTML-to-PDF.
- **Reviewer reframed** as the SIGGRAPH Asia Art Papers jury: Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate.
- **Integrity gate re-scoped:** Stage 2.5 / 4.5 verification moves from "statistical data verification" to **artwork / realization claim verification**. Gate structure and blocking semantics unchanged.
- **Venue discipline:** art-paper never hard-codes a SIGGRAPH Asia Art Papers track specific it cannot cite — page limits, anonymization rules, exact section requirements, and AI-disclosure wording all carry "verify against current CFP" notes.
- Pristine ARS reference kept at `ref/academic-research-skills/` for diffing. art-paper ships English + Korean READMEs; the ARS zh-CN / zh-TW / ja-JP READMEs were dropped.
- Fork design: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

### Inherited ARS history

Entries before v0.1.0 belong to the parent **academic-research-skills** suite. Its full changelog (v1.0 → v3.9.4.2) is preserved verbatim at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md) — art-paper does not re-narrate the parent suite's release history here.
