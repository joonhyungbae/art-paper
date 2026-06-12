# Art-Paper for Claude Code

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D77757)](https://docs.claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-v0.1.1-blue)](https://github.com/joonhyungbae/art-paper/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Wiki](https://img.shields.io/badge/wiki-EN%20%2F%20KO-blue)](https://apesuite.org/plugins/#/art-paper/en/index)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

> [한국어 README](README.ko-KR.md) · 📖 Wiki: [English](https://apesuite.org/plugins/#/art-paper/en/index) / [한국어](https://apesuite.org/plugins/#/art-paper/ko/index)

A Claude Code plugin for **practice-based art research papers** — the full pipeline from concept to a juried, publication-ready manuscript, across art-and-technology venues. Its scope is the *genre*, not a single venue; the methodology and integrity checks are venue-agnostic. Default reference target: the **SIGGRAPH Asia Art Papers track** (ACM Digital Library), wired to `acmart` + ACM Reference Format. Alternate venues are supported via citation-format conversion (APA 7.0, Chicago, MLA 9, IEEE, Vancouver) and the five art-paper structure patterns; verify venue specifics against the current CFP.

The artwork is **primary evidence**, not data. art-paper scaffolds the parts AI does well — precedent search, ACM citation formatting, structural conventions, claim anchoring — so you can focus on what only an artist-researcher can do: framing the provocation, making the work, deciding what the practice reveals.

---

## Companion plugin

**art-paper** and **art-project** are two sibling Claude Code plugins for practice-based artistic research, by the same maintainer, covering opposite ends of a project's life:

| | Plugin | Phase | What it scaffolds |
|---|---|---|---|
| | **[art-project](https://github.com/joonhyungbae/art-project)** | *before the work* | Pre-studio articulation — impulse surfacing, tradition-tagged provocations, lineage positioning, a Concept Brief, self-critique rehearsal |
| **← you are here** | **[art-paper](https://github.com/joonhyungbae/art-paper)** | *after the work* | Practice-based art-paper authoring — inquiry, drafting, ACM citation, a SIGGRAPH Asia jury, acmart LaTeX → PDF |

The arc: **art-project** articulate the concept → *make the work in your studio* → **art-paper** write the juried paper. Each stands alone; together they span concept-to-publication.

> Lineage: both descend from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu). art-paper forked the suite into the art-paper genre; art-project then pivoted from art-paper into the pre-studio phase.

---

## Install (30 seconds)

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

Then try `/art-plan` and describe your work — art-paper will walk you through the structure (context → conceptual framework → the work → realization → reflection) via Socratic dialogue. For a single-shot test instead, `/art-lit-review "your topic"`.

**👉 [Wiki — apesuite.org/plugins/#/art-paper](https://apesuite.org/plugins/#/art-paper/en/index)** — bilingual user docs (EN + 한국어): getting started, three entry points, the four skills, the methodology concepts, and the *Cutting Kim* worked example end-to-end.

**👉 [docs/SETUP.md](docs/SETUP.md)** — prerequisites (Claude Code, `ANTHROPIC_API_KEY`, optional Pandoc / LaTeX `tectonic` + ACM `acmart` for canonical PDF), API key, optional cross-model verification (`CRS_CROSS_MODEL` — inherited env-var name from the parent suite), and all install methods.

---

## What it does

Four skills covering inquiry → write → jury review → orchestrate, plus an art-research genre layer.

| Skill | Modes | What it produces |
|---|---|---|
| **art-inquiry** | full · quick · review · lit-review · fact-check · socratic · systematic-review (7) | Concept articulation, positioning, practice-based / practice-led methodology, precedent + theory lineage. Socratic mode draws out the artistic provocation; intent detection prevents premature convergence. |
| **art-paper** | full · plan · outline · revision · revision-coach · abstract · lit-review · format-convert · citation-check · disclosure · **artist-statement** · **work-doc** (12) | Art-paper draft in Pattern 1 (Practice-Based Art Paper) → **acmart LaTeX → PDF**; ACM Reference Format; dedicated artist-statement and artwork-documentation modes. |
| **art-reviewer** | full · re-review · quick · realization-focus · guided · calibration (6) | SIGGRAPH Asia Art Papers jury report — **Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate** — with 0–100 rubrics and a calibration mode that measures the jury's own FNR / FPR against a gold set. |
| **art-pipeline** | orchestrator (+ resume) | 10-stage concept→publication pipeline with two integrity gates (Stage 2.5 + 4.5) scoped to **artwork / realization claim verification**. |

The **art-research genre layer** (`shared/references/`): the artwork as primary evidence; 5 art-paper structure patterns; ACM Reference Format with venue+date locators for artwork/exhibition citations (no fabricated DOIs); **two-channel AI disclosure** (AI used to *make* the artwork vs. AI used to *write* the paper).

**Try one of:**

- `/art-plan` — *"Guide me through writing a paper about my generative-art installation."*
- `/art-reviewer` — *"Review this art paper"* (then provide it).
- `/art-full` — the full pipeline from concept to acmart PDF.
- Natural language: *"Document this artwork (materials, process, exhibition)."* The suite auto-routes by intent and announces the routing transparently.

**👉 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — flow diagram, stage-by-stage matrix, agents, quality gates. Full per-mode trigger phrases are in each `SKILL.md` and the [wiki](https://apesuite.org/plugins/#/art-paper/en/index).

---

## Design rationale

**AI as copilot, not pilot.** art-paper won't write your paper for you. It does the scaffolding — precedent search, ACM citation, claim anchoring, genre conventions — so you do the parts that require an artist-researcher. Unlike a humanizer, it does not hide your AI use: **Style Calibration** learns your voice from past work, **Writing Quality Check** catches AI-typical patterns to improve prose (not to evade detection), and the two AI-use channels (artwork-making vs. paper-writing) are disclosed separately per venue policy.

**Structural limits it handles.** Three failure modes emerge in any AI-assisted writing pipeline; the mitigations are genre-neutral and inherited unchanged from the parent suite:

1. **Frame-lock** — the AI challenges its own thesis but stays inside the frame you set. The Devil's Advocate attacks arguments, never premises.
2. **Sycophancy under pushback** — the model concedes too quickly when pressed. The **Concession Threshold Protocol** scores every rebuttal 1–5; concession only at ≥4, no consecutive concessions, with frame-lock detection at every checkpoint.
3. **Intent misdetection** — the Socratic mentor tries to converge while you are still exploring. The **Intent Detection Layer** classifies exploratory vs. goal-oriented every 3 turns and disables auto-convergence in exploratory mode.

A **Dialogue Health Indicator** runs a silent self-assessment every 5 turns for persistent agreement / conflict avoidance / premature convergence. Full 7-mode checklist: [`art-pipeline/references/ai_research_failure_modes.md`](art-pipeline/references/ai_research_failure_modes.md); the Stage 2.5 / 4.5 integrity gates run it as a blocking check.

**Citation faithfulness.** art-paper retains the L3 citation-faithfulness machinery: trust-chain provenance + locator anchors per citation, with an opt-in audit pass (`CRS_CLAIM_AUDIT=1` — env-var name inherited from the parent suite) that fetches each cited source and judges whether the claim is actually supported. Five HIGH-WARN classes gate-refuse output through the formatter (claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited). For art papers, the *rendered* format is ACM Reference Format; artwork and exhibition citations use **venue+date** as the locator, not DOIs (which would be fabricated for unindexed work).

> Motivation: Lu et al. (2026, *Nature* 651:914-919) — *The AI Scientist* showed that even autonomous-pipeline papers can pass workshop peer review carrying failure modes (implementation bugs, hallucinated results, frame-lock, citation hallucinations). Zhao et al. (2026-05, [arXiv:2605.07723](https://arxiv.org/abs/2605.07723)) audited 111M references across arXiv / bioRxiv / SSRN / PMC and estimated ~147K hallucinated citations for 2025 alone. art-paper treats this as architectural, not as a per-paper concern.

---

## Who it's for

Artist-researchers writing for art-and-technology venues — generative, interactive, net, bio, sound, and media art — where the **artwork is the primary evidence** and the paper has to make that practice legible to a juried panel. The default target is the SIGGRAPH Asia Art Papers track, but the genre layer is venue-agnostic; alternate venues are reached through citation-format conversion and the five structure patterns.

The artwork is primary evidence; structures center on the work rather than IMRaD (see [`shared/references/art_paper_structure_patterns.md`](shared/references/art_paper_structure_patterns.md)):

- **Practice-Based Art Paper** (default) — context → conceptual framework → the work → realization → reflection
- Process / Documentation paper · Conceptual / Theoretical essay · Exhibition / Curatorial case study
- IMRaD — retained only as the art-science hybrid pattern

**Not** a generator that fabricates results, a humanizer that hides AI use, or a substitute for making the work. Reception claims need an observable anchor (named venue/date + observable detail); novelty and technical-capability claims need an anchor or a hedge — reception inflation is an integrity flag, not a stylistic choice.

---

## Companion paper

A reconstruction-benchmark compliance audit of published case studies (**zero ex-nihilo fabrications across the generative-layer cells**, verified against pre-registered, hash-frozen criteria) is in submission to ***Digital Creativity*** (Routledge / Taylor & Francis, AHCI). The same reconstruction-benchmark methodology underlies art-paper's [*Cutting Kim* worked example](https://apesuite.org/plugins/#/art-paper/en/examples/cutting-kim-case) (T = 0.2568 / G = 0.1261, margin +0.13, contamination 0.003 `ok`; the clean-control variant collapses the margin to −0.019, an honest signature of the input-pack-extraction artifact size).

The plugin is released ahead of the paper and is usable on its own terms; the contribution is the evaluation framework it instantiates. The reproducibility package (input packs, gold briefs, pre-registration hash, per-case results) ships through the paper's supplementary-materials channel on acceptance. The same methodology audit is the [companion paper](https://github.com/joonhyungbae/art-project#companion-paper) shared with **art-project**.

---

## License & attribution

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Share + adapt + attribute, non-commercial use only.

```text
art-paper, forked from Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## Provenance

**Maintainer — [Joonhyung Bae](https://github.com/joonhyungbae)** (KAIST). The art-research specialization (genre layer, the SIGGRAPH Asia jury, two-channel AI disclosure, acmart output) is the work of an exhibiting artist, author of practice-based art papers at peer-reviewed venues, and AI researcher.

**Upstream — Academic Research Skills (ARS).** art-paper is forked from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 by [Cheng-I Wu (吳政宜)](https://github.com/Imbad0202). The genre-neutral pipeline machinery (Material Passport handoff, L3 citation-faithfulness gate, generator-evaluator contract, integrity gates, anti-sycophancy / DA scoring, Collaboration Depth Observer) is inherited unchanged. A pristine ARS reference is kept at `ref/academic-research-skills/` for diffing. Fork design: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

**Upstream contributors** whose ARS-era work art-paper continues to benefit from: [@aspi6246](https://github.com/aspi6246) (read-only constraint + anti-pattern codification), [@mchesbro1](https://github.com/mchesbro1) and [@cloudenochcsis](https://github.com/cloudenochcsis) (reviewer reference lists), [@eltociear](https://github.com/eltociear) and [@xpfo-go](https://github.com/xpfo-go) (upstream README translations).

---

## Repo layout

```text
art-paper/
├── art-inquiry/  art-paper/  art-reviewer/  art-pipeline/   # the 4 skills (SKILL.md + agents/ + references/)
├── skills/                            # symlinks for Claude Code skill discovery → ../art-{inquiry,paper,reviewer,pipeline}
├── shared/references/                 # art-research genre layer (structures, evidence model, ACM format, disclosure, glossary)
├── docs/                              # SETUP · ARCHITECTURE · PERFORMANCE · design/ fork spec
├── eval/  tests/                      # reconstruction-benchmark instrumentation + stdlib regression guards
├── ref/academic-research-skills/      # pristine ARS reference (for diffing)
├── .claude-plugin/{plugin,marketplace}.json
└── README{,.ko-KR}.md, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY
```

---

## Changelog (recent)

See [`CHANGELOG.md`](CHANGELOG.md) for full history. Entries below v0.1.0 are the inherited **academic-research-skills (ARS)** changelog, retained as provenance and preserved verbatim at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md).

- **v0.1.1** (2026-06-13) — *initial public release.* Install-defect fix (`skills/` symlinks repointed from broken fork-period `creative-*` names to `../art-{inquiry,paper,pipeline,reviewer}`); manifest accuracy (27 mode entries); suite-name normalisation (removed the fork-period "Creative Research Skills" label everywhere user-facing); the *Cutting Kim* worked example added; 11 stdlib-only regression guards in `tests/`.
- **v0.1.0** (2026-05-22, art-paper fork) — re-specializes the 4-skill suite from empirical scientific papers to **practice-based art research papers** targeting the **SIGGRAPH Asia Art Papers track**. Four skills renamed via `git mv`; slash commands renamed `ars-*` → `art-*` with two new modes (artist-statement, work-doc); genre layer replaced in `shared/references/`; canonical output moved to **acmart LaTeX → PDF** (IRON RULE: PDF compiled from LaTeX, never HTML-to-PDF); reviewer reframed as the SIGGRAPH Asia jury; integrity gate re-scoped to artwork / realization claim verification. Fork design: [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).

> Full inherited ARS history (v1.0 → v3.9.4.2) lives at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md) — art-paper does not re-narrate the parent suite's release history here.
