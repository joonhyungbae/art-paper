# Anonymous review mirror — checklist

Double-anonymous review artefacts live under `eval/` and `eval/repro/` only.

## Include

- `eval/` metric engine (no pilot full texts)
- `eval/repro/**` scores, prompts, DOI map, codebook, right-of-reply drafts, seeded-pack author precode
- Deposit top-level `README.md` (this checklist may live here too)

## Exclude

- Repository-root plugin README / CHANGELOG / NOTICE / maintainer identity
- Personal notes (`[jhb]*`)
- `eval/pilot/**` full gold / input / reconstruction texts
- Absolute filesystem paths (repo-relative only)
- Wiki/docs worked examples and public marketing pages

## Pre-flight

```sh
# Expect zero hits for home directories, real names, affiliations, and public maintainer URLs
rg -n '/home/|github\\.com/.+/.+' eval/repro -g '!ANONYMOUS_MIRROR.md' || true
```

Rebuild the anonymous.4open (or equivalent) mirror from this scrubbed tree before reviewers are pointed at a URL.
