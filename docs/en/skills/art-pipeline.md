# art-pipeline

**End-to-end orchestrator.** Coordinates `art-inquiry` → `art-paper` → integrity check → `art-reviewer` → `art-paper revision` → final integrity → `art-paper format-convert`.

## When to use

- You have a finished artwork and want to produce a submission-ready paper
- You want the full discipline (integrity gates, re-review, format conversion) without manually invoking each skill
- You want a documented Material Passport trail of the full pipeline state

## The full state machine

```
art-inquiry (socratic | full)
  → art-paper (plan | full)
    → integrity check (Stage 2.5: citations + realisation claims)
      → art-reviewer (full | guided jury)
        → art-paper (revision)
          → art-reviewer (re-review, max 2 loops)
            → final integrity check (Stage 4.5)
              → art-paper (format-convert → acmart LaTeX → PDF)
                → Process Summary + AI Self-Reflection Report
```

## Mandatory checkpoints

The pipeline pauses at user-confirmation points before progressing:

| Stage | Type | What you confirm |
|---|---|---|
| After inquiry | FULL | Concept/methodology/bibliography accepted |
| After draft | MANDATORY | Integrity check verdict (citations + realisation claims) |
| After review | MANDATORY | Editorial decision (accept/minor/major/reject) |
| After revision | FULL | Whether re-review or final integrity |
| Before finalisation | MANDATORY | Approve format-convert and final output |

Per `art-pipeline` v0.1.0 conventions, MANDATORY checkpoints cannot be auto-skipped even if the previous stage result is clean.

## Inputs

A topic seed and (optionally) any pre-existing materials. The pipeline detects what materials you have and picks the entry stage accordingly:

- **No materials** → Stage 1 (art-inquiry)
- **Inquiry artifacts** → Stage 2 (art-paper)
- **Draft paper** → Stage 2.5 (integrity check)
- **Verified draft** → Stage 3 (art-reviewer)
- **Reviewer feedback** → Stage 4 (revision)
- **Final draft** → Stage 5 (format-convert)

## Outputs

- All artifacts from each stage (per-stage deliverables)
- A Material Passport (state record) tracking what was decided at each checkpoint
- A final acmart PDF
- A Process Summary documenting the human-AI collaboration history
- An AI Self-Reflection Report on what the plugin did and did not author

## Pairs with

- All four skills (this is the orchestrator)

## Caveats

- The full pipeline takes longer than running individual skills; use it when discipline matters more than speed
- Each revision loop costs one API round; budget accordingly
- The re-review loop is capped at 2 by default to prevent infinite revision
- `format-convert` requires LaTeX dependencies installed locally
