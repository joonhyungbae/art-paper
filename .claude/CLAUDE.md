# art-paper

A suite of Claude Code skills for **practice-based art research papers**, specialized for the **SIGGRAPH Asia Art Papers track** (proceedings published on the **ACM Digital Library**; verify the exact category/venue against the current CFP). Forked from academic-research-skills (ARS) v3.9.4.2; the genre-neutral pipeline machinery is inherited, the empirical-science genre layer is replaced with an art-research genre layer.

> Fork design: `docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`. Pristine ARS reference kept at `ref/academic-research-skills/` for diffing.

## Skills Overview

| Skill | Purpose | Key Modes |
|-------|---------|-----------|
| `art-inquiry` v0.1.0 | Upstream practice-based art-research engine | full, quick, review, lit-review, fact-check, socratic, systematic-review |
| `art-paper` v0.1.0 | Art-paper authoring engine | full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure, **artist-statement**, **work-doc** |
| `art-reviewer` v0.1.0 | SIGGRAPH Asia Art Papers jury (Chair + curator + practitioner-researcher + art-science critic + Devil's Advocate) | full, re-review, quick, realization-focus, guided, calibration |
| `art-pipeline` v0.1.0 | Full art-paper pipeline orchestrator | (coordinates all above) |

## Genre Layer (what makes this an art-paper suite)

The artwork is **primary evidence**, not data. The shared genre layer lives in `shared/references/`:

- `art_paper_structure_patterns.md` — 5 art-paper structures (default: Practice-Based Art Paper; IMRaD only as the art-science hybrid Pattern 5).
- `art_research_evidence_model.md` — replaces the empirical evidence hierarchy. Triangulate work / process / exhibition / lineage / reflection.
- `acm_reference_format.md` — ACM Reference Format (default), targeting the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template, obtained from CTAN or the ACM).
- `siggraph_acm_disclosure.md` — ACM / SIGGRAPH Asia AI-usage disclosure (two-channel: AI to MAKE the artwork vs. AI to WRITE the paper).
- `creative_art_terminology_glossary.md` — practice-based vs practice-led, documentation vs work, generative/interactive/autonomous, authorship/credit, copyright/exhibition-rights, reception terms.

**Output:** acmart LaTeX → PDF (default class option `sigconf`). IRON RULE: PDF compiled from LaTeX, never HTML-to-PDF.

## Routing Discipline

**Step 0 — Escape hatch:** if the user's first message begins with `[direct-mode]` (case-insensitive, byte-0 after whitespace strip), strip it and route directly per explicit intent.

Otherwise classify:
1. **Explicit clear intent** — `/art-*` slash command or an unambiguous trigger ("review my art paper", "draft an artist statement") → route directly.
2. **Cross-phase materials, no named skill** → clarify (list candidate workflows a–d in the message body, not a single-phase auto-route). See `shared/references/intent_clarification_protocol.md`.
3. **Ambiguous, no materials** → clarify per the same protocol.

## Routing Rules

1. **art-pipeline vs individual skills**: pipeline = full orchestrator (inquiry → write → integrity → jury review → revise → final integrity → finalize). For a single function (just inquiry, just write, just review), trigger that skill directly.
2. **art-inquiry vs art-paper**: complementary. inquiry = upstream (concept articulation, positioning, practice-based methodology, lineage). paper = downstream (art-paper authoring + ACM citation + acmart output). Flow: inquiry → paper.
3. **art-inquiry socratic vs full**: socratic = guided dialogue drawing out the artistic concept/provocation. full = direct production. When the concept is unclear, suggest socratic.
4. **art-paper plan vs full**: plan = section-by-section guided planning. full = direct production.
5. **art-reviewer guided vs full**: guided = Socratic review engaging the artist. full = standard multi-perspective jury report.

## Key Rules (art genre)

- The artwork is primary evidence; every claim is anchored to an evidence type per `art_research_evidence_model.md`.
- Reception claims need an observable anchor (named venue/date + observable detail) — no "audiences were moved" without anchor (reception inflation is an integrity flag).
- Novelty/precedence ("first work to…") and technical-capability claims ("real-time", "autonomous") require an anchor or a hedge.
- Collaboration credit named; copyright/exhibition rights + image courtesy lines respected.
- All literature/precedent citations use ACM Reference Format; the L3 citation-faithfulness gate (locator anchor after each citation) is unchanged from ARS. Artwork/exhibition citations use venue+date as the locator (no fabricated DOIs).
- AI-usage disclosed in two channels (artwork-making vs paper-writing) per venue policy; verify against the current SIGGRAPH Asia Art Papers CFP.
- Never fabricate venue specifics — add "verify against current CFP" notes.
- Default output language matches user input.

## Full Art-Paper Pipeline

```
art-inquiry (socratic/full)
  → art-paper (plan/full)
    → integrity check (Stage 2.5: citations + artwork/realization claims)
      → art-reviewer (full/guided jury)
        → art-paper (revision)
          → art-reviewer (re-review, max 2 loops)
            → final integrity check (Stage 4.5)
              → art-paper (format-convert → acmart LaTeX → PDF)
                → Process Summary + AI Self-Reflection Report
```

## Handoff Protocol

- **art-inquiry → art-paper**: Concept & Provocation Brief, Practice-Based Methodology Blueprint, Annotated Bibliography (precedent works + theory), Synthesis Report.
- **art-paper → art-reviewer**: complete art-paper text + documentation. `field_analyst_agent` auto-detects art subfield + SIGGRAPH track and configures the jury.
- **art-reviewer → art-paper (revision)**: Editorial Decision Letter, Revision Roadmap, per-reviewer comments.

## Version Info
- **Suite version**: 0.1.1 (forked from ARS v3.9.4.2)
- **Last Updated**: 2026-06-13
- **License**: CC-BY-NC 4.0
