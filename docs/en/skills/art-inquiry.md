# art-inquiry

**The upstream practice-based art-research engine.** Use this when you have a work and a question but no draft yet.

## Modes

| Mode | What it produces | When to use |
|---|---|---|
| `socratic` | Guided dialogue drawing out concept and provocation | You haven't yet articulated what the work argues |
| `full` | Concept & Provocation Brief + Methodology Blueprint + Annotated Bibliography + Synthesis Report | You know the question; need the structured artifacts |
| `quick` | Lightweight version of `full` | Time-pressed first pass |
| `review` | Critical review of an existing inquiry | Validate someone else's brief |
| `lit-review` | Annotated bibliography only | You need just the references survey |
| `fact-check` | Verify factual claims in an inquiry artifact | Pre-submission audit |
| `systematic-review` | Systematic-review article-type artifact | If your contribution is a literature paper, not a work paper |

## Inputs

- A short topic seed (1-3 sentences)
- Optional: factual documentation of the work (form, mechanism, exhibition record)
- Optional: a draft provocation if you have one

## Outputs (full mode)

1. **Concept & Provocation Brief** — what the work argues, why it matters, how it positions against prior work
2. **Practice-Based Methodology Blueprint** — how the work, the documentation, the writing, and the reception triangulate as evidence
3. **Annotated Bibliography** — precedent works + theory, with annotations on what each contributes
4. **Synthesis Report** — the inquiry's findings ready for the art-paper skill to consume

## Socratic mode {#socratic-mode}

When you don't know your provocation yet, `socratic` mode runs a guided dialogue:

```
/art-inquiry socratic I made [Work]. I want to write about it but I don't know what I'm arguing.
```

The skill asks short, targeted questions one at a time, surfacing the artist's own framing without imposing one from the outside.

## Pairs with

- **Downstream**: `art-paper` consumes the synthesis report as input pack
- **Cross-check**: `art-reviewer` in `guided` mode can review the inquiry artifacts before writing begins

## Caveats

- Provocation, reflection, and situated interpretation remain the artist's authorial responsibility — the inquiry articulates the question, not the answer.
- Lit-review mode searches public bibliographic sources but does not verify accessibility; verify locators before citing.
- Systematic-review mode produces an article-type artifact, but the standard of evidence inside that artifact is your own.
