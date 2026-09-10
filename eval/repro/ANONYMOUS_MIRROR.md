# Anonymous review mirror — checklist

Double-anonymous review artefacts live under `eval/` and `eval/repro/` only.

## Include

- `eval/` metric engine (no pilot full texts)
- `eval/repro/**` scores, prompts, DOI map, codebook, right-of-reply log, seeded-pack tally
- This file as the deposit top-level README (rename to `README.md` in the anonymous cut)

## Exclude

- Repository-root README / CHANGELOG / maintainer identity
- Any `[jhb]*` personal notes
- `eval/pilot/**` full gold / input / reconstruction texts
- Absolute filesystem paths (use paths relative to the repository root)

## Pre-flight

```sh
rg -n '/home/|Cutting Kim|KAIST' eval/repro || true
```

Expect zero identity hits in the deposit tree. Rebuild the anonymous.4open (or equivalent) mirror from this scrubbed tree before reviewers are pointed at a URL.
