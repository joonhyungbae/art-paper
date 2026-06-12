# art-paper

**The art-paper authoring engine.** Drafts, revises, formats, and audits art papers.

## Modes

| Mode | What it produces | When to use |
|---|---|---|
| `plan` | Section-by-section guided plan | You want to discuss the structure first |
| `full` | Full draft from inquiry artifacts | You have the inputs, want a draft |
| `outline-only` | Just the section outline | Section structure check |
| `revision` | Revised draft from reviewer feedback | After `art-reviewer` |
| `revision-coach` | Walks you through revision decisions | When you're not sure how to respond to a review |
| `abstract-only` | Structured abstract | Late-stage polish |
| `lit-review` | Section-2 literature review only | When the rest of the paper is done |
| `format-convert` | acmart LaTeX → PDF | Final stage |
| `citation-check` | Locator-anchor audit on every citation | Pre-submission integrity check |
| `disclosure` | AI-usage two-channel disclosure | Required by SIGGRAPH Asia / ACM |
| `artist-statement` | Standalone artist statement | When the venue requires one |
| `work-doc` | Standalone work documentation | When the venue requires one |

## Inputs

- Concept & Provocation Brief (from `art-inquiry`)
- Practice-Based Methodology Blueprint
- Annotated Bibliography
- Synthesis Report
- Optional: existing draft (for `revision` or `revision-coach` modes)
- Optional: reviewer feedback (for `revision`)

## Outputs (`full` mode)

A `acmart`-class LaTeX manuscript with:

- Title
- Abstract (structured per venue)
- Introduction (founding premise + scope statement + RQs + method summary)
- Related Work
- Methodology
- The Work (factual description)
- Evaluation (if applicable)
- Discussion (including reflexive position)
- Conclusion
- References (ACM Reference Format by default, wired to acmart; alternate formats for non-ACM venues: APA 7.0, Chicago, MLA 9, IEEE, Vancouver)
- AI-usage disclosure (two-channel)

## Iron rules the skill enforces

1. **No fabricated citations.** Every reference must resolve to a locator the user can verify.
2. **No fabricated reception claims.** "Audiences were moved" without an observable anchor is flagged.
3. **No fabricated novelty claims.** "First work to..." requires an anchor or hedge.
4. **No fabricated technical-capability claims.** "Real-time", "autonomous" require an anchor.
5. **Artist's reading is the artist's responsibility.** Provocation and reflection sections are marked for artist authorship; the skill scaffolds but does not author.

## Pairs with

- **Upstream**: `art-inquiry` (provides the input pack)
- **Downstream**: `art-reviewer` (for jury review of the draft)
- **Final**: `format-convert` (for camera-ready)

## Caveats

- The skill produces a draft. It does not certify the draft as ready for submission. Run `art-reviewer` and address the findings.
- `disclosure` mode produces a template; the artist must fill in actual AI usage facts.
- `format-convert` requires `acmart.cls` (CTAN or ACM). The skill does not install LaTeX dependencies.
