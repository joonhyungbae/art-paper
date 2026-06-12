# Positioning

## What this is

art-paper is a **source-available art-research copilot framework** for noncommercial scholarly and artistic use. The reference distribution is a suite of Claude Code skills that assists artist-researchers through the full inquiry-to-publication pipeline for **practice-based art research papers** across art-and-technology venues. The methodology and integrity checks are venue-agnostic; default reference target is the **SIGGRAPH Asia Art Papers track** (proceedings on the ACM Digital Library; verify category/venue against the current CFP), wired to `acmart` + ACM Reference Format. Alternate venues are supported via citation-format conversion (APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver) and the five art-paper structure patterns.

art-paper is forked from [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills). The genre-neutral pipeline machinery (Material Passport handoff, integrity gates, citation-faithfulness gate, generator-evaluator contract) is inherited; the empirical-science genre layer is replaced with an art-research genre layer in which **the artwork is primary evidence**. Sibling distributions for other agent platforms follow the same workflow content, the same human-in-the-loop design philosophy, and the same license terms.

## Grounding

The art-research genre layer is not adapted to the field from outside it. Its load-bearing decisions — that the artwork is primary evidence; the evidence model that triangulates work, process, exhibition, lineage, and reflection; the jury composition (curator, practitioner-researcher, art-science critic); and the two-channel AI disclosure that separates AI used to *make* the artwork from AI used to *write* the paper — were made from inside practice. The maintainer works at once as an exhibiting artist, an author of practice-based art papers at peer-reviewed venues, and an AI researcher publishing in the field. The fork exists because that combination needs all three lenses at once, and the empirical-science genre layer it inherits was the wrong fit for art research.

> Author identity is withheld here while the accompanying methodology paper is under double-blind review. Specific venues, institutions, and works are deliberately omitted for the same reason; full attribution will be restored once review is complete.

It is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). This is not an open source license — it restricts commercial use by design, to keep the tool free for art and academic communities.

## What this is not

art-paper is not an autonomous paper-writing system, and it does not make art. It is not a replacement for the artist-researcher. It does not claim authorship or co-authorship of the artwork or the paper, and its outputs are not submission-ready without human review.

## Allowed uses

- Research assistance: precedent-work and theory search, source verification, ACM citation checking
- Artwork documentation: structuring materials, process, and exhibition records for a paper
- Teaching: demonstrating practice-based research methodology, juried review processes, art-paper writing conventions
- Method training: using Socratic modes to develop the articulation of an artistic provocation and its situated argument
- Noncommercial scholarly/artistic collaboration: studios, labs, departments, and collectives using the tool for shared workflows

## Discouraged uses

- Submitting AI-generated papers as solely human-authored without disclosing AI assistance (art-paper disclosure separates AI used to *make the artwork* from AI used to *write the paper*)
- Using the tool to produce papers without engaging with the content (the pipeline has mandatory checkpoints specifically to prevent this)
- Treating AI-generated jury feedback as a substitute for actual juried review

## Prohibited uses (per license)

- Commercial SaaS or hosted services built on art-paper
- Consulting or freelance services that package art-paper as a paid product
- Enterprise or institutional paid deployments without separate licensing
- Commercial API wrappers or resale of art-paper functionality

These reflect our policy intent. See the [CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/) for the precise legal terms. For commercial licensing inquiries, contact the maintainer.

## Design philosophy

**Assistive, not deceptive.** art-paper helps you write better, not hide that you used AI.

- Style Calibration learns your voice from past work — so the output sounds like you, not like a machine
- Writing Quality Check catches AI-typical patterns — to improve prose quality, not evade detection
- Disclosure Mode generates venue-specific AI-usage statements with two channels (artwork-making vs. paper-writing) — because transparency is the standard. Verify exact wording against the current SIGGRAPH Asia Art Papers CFP.

**Human-in-the-loop, always.** The pipeline's checkpoint system is mandatory by design:

- FULL checkpoints present all deliverables and require explicit user confirmation
- MANDATORY checkpoints at integrity gates and jury decisions cannot be skipped
- "Full mode" means full-pipeline execution, not full autonomy — the human decides at every gate
- Max 2 revision loops, after which remaining issues become "Acknowledged Limitations" rather than being silently resolved

**Failure modes are made visible, not hidden.** The 7-mode AI Research Failure Mode Checklist and Reviewer Calibration Mode (both inherited from ARS) exist so that users can see where the AI might be wrong — not so that the AI can claim it's always right. The L3 claim-faithfulness gate adds per-citation locator anchors and an opt-in audit pass that verifies whether each cited source actually supports the claim made of it. In the art context, the integrity gate is re-scoped to **artwork / realization claim verification**: reception claims need an observable anchor (named venue/date + observable detail), and novelty or technical-capability claims need an anchor or a hedge.

## Citing this tool

If you use art-paper in your research or practice, please cite it alongside its parent suite:

```
art-paper (art-paper, Version 0.1.0) [Computer software].
Forked from Academic Research Skills by Cheng-I Wu.
https://github.com/Imbad0202/academic-research-skills
```
