# Changelog

All notable changes to this project will be documented in this file.

> **Provenance note.** This project is **art-paper**, forked from **academic-research-skills (ARS)** v3.9.4.2. Only art-paper-specific entries are kept here. The full parent-suite changelog (ARS v1.0 → v3.9.4.2) is preserved verbatim at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md) and is not re-narrated here.

## [0.1.1] - 2026-05-30 — install/manifest hardening, naming, Cutting Kim worked example

**Doubt-resolution pass (post-release).** A user-driven "does it actually work" audit surfaced four remaining doubts; all four resolved.

- **MODE_REGISTRY 27 vs marketplace 25**: MODE_REGISTRY's "27 modes" claim is correct (art-inquiry 7 + art-paper 12 + art-reviewer 6 + art-pipeline orchestrator + cross-session resume = 27 entries). `.claude-plugin/marketplace.json` description aligned to "27 mode entries total" with the per-skill breakdown. `MODE_REGISTRY.md` art-pipeline trigger list edited from "creative pipeline" (fork-period leftover) to "art pipeline".
- **`art-paper/references/` orphan claim (audit false positive)**: The narrow search that flagged 8 orphans was scoped to `art-paper/SKILL.md` + `art-paper/agents/*.md` only. Wider sweep (including cross-skill agents, `shared/handoff_schemas.md`, `shared/policy_data/*.md`) shows 0 true orphans. Every reference file is reachable from some agent or schema.
- **`shared/references/` orphan claim (audit false positive)**: Same scope issue. `irb_terminology_glossary`, `protected_hedging_phrases`, `psychometric_terminology_glossary`, `word_count_conventions` are each referenced from at least one SKILL.md or agent file.
- **Stale `creative-research-skills` path in tracked config**: 23 `pdf_path` entries in `corpus_expansion/selected_corpus/cases_manifest.json` carried the pre-rename absolute path. Replaced with `/home/jhbae/art-paper/...`. PDF presence on the local filesystem unchanged (23 of 34 already on disk; the unresolved ones are an upstream corpus-acquisition matter, not a path bug).
- **`.claude/CLAUDE.md` version field**: bumped to v0.1.1, last-updated 2026-05-30.

New regression guard: `tests/test_art_paper_wiki_regression.py::test_no_fork_period_path_in_tracked_files` walks `git ls-files` and asserts no tracked file embeds `creative-research-skills/` as a filesystem path. `art-paper_paper/` (nested separate repo) and gitignored `.claude/settings.local.json` are excluded naturally because they are not tracked in this repo. Test suite total: 11 art-paper-specific tests, all passing.

Live smoke test of `/art-mark-read`: `scripts/art_paper_mark_read.py` invokes cleanly under the documented fail-fast contract (argparse rejects no-args; missing passport produces the spec-prescribed `[art-paper-MARK-READ ERROR: passport file not found at ...]` line). Its dedicated test suite (`scripts/test_art_paper_mark_read.py`) reports 14/14 pass.



**Install defect fix.** `skills/` contained four dangling symlinks (`creative-{inquiry,paper,pipeline,reviewer}` → targets that no longer exist after the post-fork rename); a fresh clone would fail to register the four core skills. Symlinks repointed to `../art-{inquiry,paper,pipeline,reviewer}`.

**Manifest / docs accuracy.**
- `marketplace.json`: replaced the incorrect claim "12 modes per skill" with the actual per-skill counts (art-inquiry 7, art-paper 12, art-reviewer 6, plus the art-pipeline orchestrator).
- `commands/art-disclosure.md`: dropped the inherited ARS science-venue list (ICLR / NeurIPS / Nature / Science / ACL / EMNLP) for the two-channel SIGGRAPH Asia / ACM disclosure wording.
- `docs/{en,ko}/skills/art-paper.md`: corrected the citation-formats line — was "ACM or Emerald Harvard", now lists the authoritative set (ACM default + APA 7.0, Chicago, MLA 9, IEEE, Vancouver) per `art-paper/SKILL.md`.
- `docs/{en,ko}/skills/index.md`: art-inquiry summary row now lists all 7 modes (was 4); added a `/art-*` slash-command reference table.

**Naming and wording.**
- Renamed the suite display name "Creative Research Skills" → **"Art-Paper"** throughout the user-facing wiki (en+ko), `mkdocs.yml` `site_name`, the naming FAQ (rewritten to "Where does the name come from?"), the citation BibTeX (`@software{art_paper_2026, title={Art-Paper: ...}}`), and the skeleton example's AI-use note. The fork-period repo folder path is unaffected.
- Korean wiki: replaced the literal upstream/downstream calque "상류/하류" with **"선행/후속"** in the art-inquiry tagline and the skill-pairing labels (en wording is idiomatic and was left as-is).

**Cutting Kim worked example.** Added a featured reconstruction-benchmark walkthrough on the authors' own SIGGRAPH Asia 2025 art paper, *Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts* (Bae, Choi, Nam — KAIST). Pilot at `eval/pilot/sa25-ck/` (gitignored, consistent with the other pilots). A firewalled reconstruction agent (input-pack-only) reached a distinct reading ("the untrained voice as an embodied game controller") from the gold's withheld "playful transgression" thesis. Instrumentation: T = 0.2568 / G = 0.1261 (margin +0.1307), `thesis_supported = True`, 8-gram contamination 0.0028 (`ok`), citation precision 1.0 / recall 0.32, structural coverage 1.0.

**Cutting Kim clean-control variant.** Added `eval/pilot/sa25-ck-clean/` with a minimal-footprint input pack — paper-derived technical specifics (RMS, YIN, Lab/Delta E*2000, multipliers, three-stage taxonomy) removed; bibliography pruned 28 → 15 to drop transgression/carnival lineage refs. A second firewalled reconstruction reached a third distinct reading ("voice as blade"). The standard margin **+0.1307 collapses to −0.0189** under the clean-control discipline (`thesis_supported = False`), an honest signature that a substantial fraction of the standard margin was an input-extraction artifact carried by paper-derived prose. Contamination stays at 0 in both runs.

**Instrumentation: optional sentence-embedding pass.** The worked example now reports `--embed` (`BAAI/bge-small-en-v1.5`) chunk-alignment cosine alongside the lexical metrics, with the topic-saturation caveat the methodology already documents (~0.78 for both T and G — embedding is not the discriminator within one paper).

**See-saw page removed.** `docs/{en,ko}/examples/seesaw-case.md`, all references in mkdocs nav, `nav.js`, examples/index, top-level index, getting-started, and `concepts/reconstruction-benchmark.md` removed. The Cutting Kim case is the single featured walkthrough.

**Top-level doc tidy.** `README.md` had stale fork-period skill labels ("Creative Inquiry / Paper / Reviewer / Pipeline") sprinkled through the skill descriptions and section headings; replaced with `art-{inquiry,paper,reviewer,pipeline}` throughout. `README.ko-KR.md` had a historically-inaccurate changelog line claiming the skills were renamed from `creative-{...}` (the actual rename was from the ARS names `deep-research` / `academic-paper` / `academic-paper-reviewer` / `academic-pipeline`); corrected. Version badges in both README files bumped from `v0.1.0` to `v0.1.1`, and `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` plugin `version` likewise bumped to `0.1.1`.

**Sanity test suite added** at `tests/test_art_paper_*.py` (stdlib-only, runs in ~0.05 s):

- `test_art_paper_install_integrity.py` — guards the `skills/` symlink resolution (regression for the dangling-symlink class fixed above), the plugin / marketplace JSON version-vs-CHANGELOG sync, and the marketplace mode-count claim vs `MODE_REGISTRY.md`.
- `test_art_paper_wiki_regression.py` — guards "Creative Research Skills" wording in the user-facing wiki (must not reappear), "Emerald Harvard" residue (must not reappear as a configured bibliography format), and the `commands/art-disclosure.md` venue list (must target SIGGRAPH Asia / ACM, not the inherited ARS science-venue list).
- `test_art_paper_instrumentation_smoke.py` — runs `eval/instrumentation.py` on the bundled `eval/fixtures/synthetic_case/` and confirms the metric shape + the Pattern-1 layer-keyword set are stable.

These join the ~1,470 inherited ARS tests (collection clean: 1,481 tests total).

**Wiki deploy mechanics now documented in this changelog for the record.** The wiki source lives in two manually-synced copies — `docs/{en,ko}/` (MkDocs source in this repo) and `apesuite/plugins/content/art-paper/{en,ko}/` (the React+Vite site under `joonhyungbae/apesuite`, deployed to **apesuite.org/plugins/** via `gh-pages`). There is no sync script; changes must be mirrored to both, and the live site only updates when `npm run deploy` is run from the apesuite repo (pushing `main` is not enough). The MkDocs site under `joonhyungbae.github.io/art-paper/` returns 404 (private-repo + Pages-not-configured); the live surface is apesuite.

## [0.1.0] - 2026-05-22 — art-paper fork (art-paper specialization)

**Fork:** Re-specializes the ARS 4-skill suite from empirical scientific papers to **practice-based art research papers**, targeting the **SIGGRAPH Asia Art Papers track** (proceedings on the ACM Digital Library; verify category/venue against the current CFP). The genre-neutral pipeline skeleton (10-stage state machine, Material Passport handoff, integrity gates, L3 citation-faithfulness gate, generator-evaluator contract, anti-sycophancy / Devil's Advocate discipline, Collaboration Depth Observer) is inherited unchanged. Only the **genre layer** is replaced. Fork design: `docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`. A pristine ARS reference is kept at `ref/academic-research-skills/` for diffing.

**Skill rename (history-preserving `git mv`):**

- `deep-research/` → `art-inquiry/` — upstream practice-based art-research engine (concept articulation, positioning, practice-based / practice-led methodology, lineage of precedent works and theory).
- `academic-paper/` → `art-paper/` — art-paper authoring engine (structure, drafting, ACM citation, acmart output).
- `academic-paper-reviewer/` → `art-reviewer/` — SIGGRAPH Asia Art Papers jury simulation.
- `academic-pipeline/` → `art-pipeline/` — 10-stage orchestrator (skeleton unchanged).

**Plugin packaging:** plugin name `academic-research-skills` → `art-paper`; slash commands `ars-*` → `art-*`, extended to 15 with two new `art-paper` modes: **artist-statement** and **work-doc** (artwork documentation). Model routing preserved (opus for `full` / `revision-coach`, sonnet otherwise; no Haiku).

**Genre layer replaced (`shared/references/`):**

- `art_paper_structure_patterns.md` — 5 art-paper structures; default **Practice-Based Art Paper** (context → conceptual framework → the work → realization → reflection). IMRaD is demoted to the art-science hybrid pattern only.
- `art_research_evidence_model.md` — replaces the empirical evidence hierarchy. The **artwork is primary evidence**; triangulate work / process / exhibition / lineage / reflection. Defines what "a claim must be supported" means when the claim is about an artwork.
- `acm_reference_format.md` — **ACM Reference Format** default (replacing APA 7.0), wired to the acmart package's `ACM-Reference-Format.bst` + the acmart `acmart.cls`; documents the biblatex `acmnumeric` / `acmauthoryear` options. Artwork and exhibition citations use venue+date as the locator (no fabricated DOIs).
- `siggraph_acm_disclosure.md` — ACM / SIGGRAPH Asia AI-usage disclosure, two-channel (AI to MAKE the artwork vs. AI to WRITE the paper).
- `creative_art_terminology_glossary.md` — practice-based vs practice-led, documentation vs work, generative/interactive/autonomous, authorship/credit, copyright/exhibition-rights, reception terms. Replaces the IRB + psychometric glossaries as the active glossary set.

**Output toolchain:** canonical output is **acmart LaTeX → PDF** via the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template, obtained from CTAN or the ACM) (default class option `sigconf`, a CFP-verified setting). IRON RULE preserved: PDF compiled from LaTeX, never HTML-to-PDF. APA/IEEE/Chicago/MLA/Vancouver formats remain available for art-science hybrids.

**Reviewer jury:** the review panel is reframed as the SIGGRAPH Asia Art Papers jury — **Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate**. `methodology-focus` mode is reframed as `realization-focus` (technical realization).

**Integrity gate re-scoped:** Stage 2.5 / 4.5 verification moves from "statistical data verification" to **artwork / realization claim verification** — reception claims need an observable anchor (named venue/date + observable detail); novelty / precedence and technical-capability claims need an anchor or a hedge. Gate structure and blocking semantics unchanged.

**Citation-faithfulness machinery retained as-is** (hallucinated citations are a cross-genre hazard): L3 three-layer emission, contamination signals, cross-index triangulation. Only the *rendered* citation format changes (ACM, not APA).

**Venue discipline:** art-paper never hard-codes a SIGGRAPH Asia Art Papers track specific it cannot cite. Page/word limits, anonymization rules, exact section requirements, and AI-disclosure wording all carry "verify against current CFP" notes. Open questions (exact acmart class for the track, anonymization requirement, length budget, default-on bilingual abstracts) tracked in fork spec §9.

**Out of scope (v0.1):** full ARS test parity (only genre-critical lints ported), non-Art-Paper SIGGRAPH tracks, auto-submission. Chinese-language support (zh-TW / zh-CN — bilingual abstracts, CJK LaTeX, Chinese citation guides) dropped in stage 1 (commit `27aa0da`, 2026-05-23) + stage 2 content polish (commit `23f1fb5`, 2026-05-23): art-paper v0.1 ships English-only. Multi-language paper output may return in a later version.
