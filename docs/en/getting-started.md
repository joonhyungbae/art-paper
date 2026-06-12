# Getting started

## Prerequisites

- **[Claude Code](https://www.anthropic.com/claude-code)** installed and authenticated
- **A documented artwork** you have made (your own practice), with at least the following materials available:
    - A factual description of the work's form and mechanism
    - An exhibition record (venue, dates, layout) if any
    - Photographs or documentation videos if any
    - A short bibliography of precedent works and theory you find relevant

## Install

**Recommended — Claude Code plugin marketplace:**

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

Open Claude Code and verify the skills appear with `/art-` slash command completion.

**Alternative — manual clone (for hacking on the plugin itself):**

```bash
git clone https://github.com/joonhyungbae/art-paper.git
cd art-paper
```

Then register the directory as a Claude Code plugin path per `docs/SETUP.md`.

## Your first run — three possible entry points

The plugin supports three common entry points depending on how far along your project is.

### Entry point A — "I have a finished artwork and want to write the paper"

Set up an `input/` directory in your working folder. You can mirror the input pack from the [Cutting Kim case study](examples/cutting-kim-case.md):

```
my-paper/
├── input/
│   ├── concept_memo.md       # one paragraph, factual topic seed (no interpretive claims)
│   ├── documentation.md      # form + working mechanism of the work (factual)
│   ├── exhibition_record.md  # venue, dates, layout
│   ├── bibliography.bib      # precedent works + theory (BibTeX)
│   └── figures/              # photos, documentation videos (optional)
└── (provocation + reflection are elicited from you by the pipeline)
```

Example `concept_memo.md` (from the Cutting Kim case):

```markdown
An interactive VR experience for the Oculus Quest 2 in which the player's own
voice is the controller: loudness and pitch, captured through the headset
microphone, drive a game where the player wields a voice-generated "sonic sword"
to destroy food-themed enemy characters. The work was shown in public exhibition
settings (workshop, conference, festival).
```

Then invoke:

```
/art-pipeline Use the materials in input/ to write a paper about [Title].
Target venue: SIGGRAPH Asia 2026 Art Papers track (swap in your target venue).
```

The pipeline orchestrator will dispatch:

1. **art-inquiry** — to articulate the concept, positioning, and methodology
2. **art-paper** — to draft the paper
3. **art-reviewer** — to simulate jury review
4. **art-paper (revision)** — to revise per the review
5. **Final integrity check** — citation and realisation-claim audit
6. **art-paper (format-convert)** — to produce camera-ready LaTeX (`acmart` class)

### Entry point B — "I have a draft and want focused review"

Place the draft and (if available) documentation of the work side by side:

```
my-paper/
├── draft/
│   ├── paper.tex             # or paper.md / paper.docx
│   └── references.bib
└── docs/                     # optional — photos, videos, exhibition record
    ├── figures/
    └── exhibition_record.md
```

Invoke:

```
/art-reviewer Review draft/paper.tex against your target Art Papers
standards (SIGGRAPH Asia by default) as a five-perspective jury.
Artwork documentation is in docs/.
```

This returns a five-perspective jury report (Chair, Curator, Practitioner-Researcher, Art-Science Critic, Devil's Advocate) with an Editorial Decision Letter and a Revision Roadmap.

### Entry point C — "I have an idea, not yet a paper"

No paper materials needed yet — just a minimal seed:

```
my-paper/
├── concept_memo.md           # one paragraph — the work/topic seed
├── documentation.md          # optional — factual description of work or prototype
└── references/               # optional — notes on related works/theory
    └── notes.md
```

If your provocation isn't yet clear, ask for Socratic mode explicitly:

```
/art-inquiry Start a socratic-mode inquiry from concept_memo.md.
My provocation isn't clear yet — I want to work out together what
question this work is actually posing.
```

This produces a Concept & Provocation Brief, a Practice-Based Methodology Blueprint, an Annotated Bibliography of precedent works and theory, and a Synthesis Report — the materials the art-paper skill will then consume to draft the manuscript.

## What the plugin will ask you for

The plugin operates under a **firewall discipline**: it cannot author the artwork's reading from documentation alone. So it asks the artist for the parts only the artist can provide — typically a **provocation** (one paragraph stating what the work argues, asserts, or refuses) and a **reflection** (what running the practice taught you about the question). These are the *generative-layer* materials the methodology distinguishes from documentable material.

If you do not yet know your provocation, run the [Socratic inquiry mode](skills/art-inquiry.md#socratic-mode) instead of `full` mode.

## Output formats

- **Manuscript**: LaTeX targeting the `acmart` document class (`sigconf` option) → PDF
- **Bibliography**: ACM Reference Format by default (wired to acmart); alternate formats for non-ACM venues — APA 7.0, Chicago, MLA 9, IEEE, Vancouver
- **Tables/figures**: separate files per ACM convention
- **AI-usage disclosure**: produced automatically per SIGGRAPH Asia / ACM policy (two-channel — AI to MAKE the artwork vs. AI to WRITE the paper)

## Next steps

- Walk through the [Cutting Kim case study](examples/cutting-kim-case.md) — the worked example from input pack to firewalled reconstruction to instrumentation
- Read about the [skills individually](skills/index.md)
- Understand the [methodology concepts](concepts/index.md) that ground the plugin's design
