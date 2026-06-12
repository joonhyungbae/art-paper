# art-reviewer

**Practice-based Art Papers jury simulation.** Produces multi-perspective review reports as a five-reviewer jury would. It defaults to SIGGRAPH Asia Art Papers conventions and adapts to other practice-based art venues.

## The jury

| Role | What they check |
|---|---|
| **Chair** | Venue fit, scope, contribution claim sized to evidence |
| **Curator** | Reception claims, exhibition context, the work's place in current curatorial conversations |
| **Practitioner-Researcher** | Methodology internal to practice, validity criteria, artist's authorial position |
| **Art-Science Critic** | Technical-capability claims, novelty claims, science-art interface |
| **Devil's Advocate** | What the other four missed — over-generalization, undisclosed limitations, fabricated anchors |

## Modes

| Mode | What it produces |
|---|---|
| `full` | All five reviewer reports + Chair's Editorial Decision Letter + Revision Roadmap |
| `re-review` | Verification review after revision (checks each revision item) |
| `quick` | Single integrated report, less detailed |
| `realization-focus` | Focused review on technical/realisation claims only |
| `guided` | Socratic mode — engages the artist in dialogue |
| `calibration` | Compares the jury verdict against the venue's actual acceptance criteria |

## Inputs

- Complete art-paper text
- Optional: documentation, exhibition record, work images (helps Curator + Practitioner)
- Optional: prior reviewer feedback (for `re-review` mode)

## Outputs (`full` mode)

1. Five per-reviewer reports
2. Editorial Decision Letter (Accept / Minor revision / Major revision / Reject) with reasoning
3. Revision Roadmap — prioritised list of revisions with effort estimates
4. R&R Traceability Matrix (Schema 11) — maps each revision back to the source review concern

## How it differs from a generic reviewer skill

`art-reviewer` is configured for practice-based art-paper conventions (SIGGRAPH Asia Art Papers by default; adaptable to other venues):

- Reception claims require observable anchors (named venue/date + observable detail)
- Novelty claims require anchor or hedge
- Technical-capability claims require anchor or hedge
- Collaboration credit must be named
- Copyright / exhibition rights / image courtesy must be respected
- AI-usage disclosure must be two-channel
- Field-analyst agent auto-detects subfield (kinetic, generative, bio-art, interactive installation, mixed reality, sound, photographic) and configures jury accordingly

## Pairs with

- **Upstream**: `art-paper` (provides the draft to review)
- **Downstream**: `art-paper revision` (revises per the Roadmap)
- **Final**: `art-reviewer re-review` (verifies revision adequacy)

## Caveats

- Jury verdicts are simulations, not the real reviewers. The skill is for **internal pre-submission rehearsal**.
- `calibration` mode is approximate — it compares against published venue criteria, not actual acceptance committee deliberation.
- Devil's Advocate is configured to find at least three concerns per pass; treat severity ratings as guides, not absolutes.
