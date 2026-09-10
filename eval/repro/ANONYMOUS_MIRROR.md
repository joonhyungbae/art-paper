# Anonymous review mirror — what to publish

The live GitHub README/CHANGELOG name the maintainer and the authors' own *Cutting Kim* pilot. **Do not** point double-anonymous reviewers at the full public repo root.

## Bundle for anonymous.4open (or equivalent)

Include only:

- `eval/` metric engine (no pilot full texts if gitignored)
- `eval/repro/**` (scores, prompts, DOI map, codebook, right-of-reply log, seeded-pack tally)
- This file as top-level `README.md` of the anonymous deposit

Exclude:

- Root `README.md`, `CHANGELOG.md`, maintainer identity
- Any `[jhb]*` notes
- `eval/pilot/**` full gold/input/reconstruction texts
- Wiki / apesuite links that deanonymise

Suggested anonymous README title: “Art-paper reconstruction benchmark — review artefacts (scores and protocol only)”.

Until the anonymous deposit is re-cut, Data availability in the manuscript states that only `eval/` and `eval/repro/` are in scope for review.
