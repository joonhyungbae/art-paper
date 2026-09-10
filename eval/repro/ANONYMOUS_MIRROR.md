# Anonymous review mirror — checklist

Double-anonymous review artefacts live under `eval/` and `eval/repro/` only.

## Include

- `eval/` metric engine (no pilot full texts)
- `eval/repro/**` scores, prompts, DOI map, codebook, right-of-reply drafts, seeded-pack author precode
- This file as the deposit top-level README (rename to `README.md` in the anonymous cut)

## Exclude

- Repository-root README / CHANGELOG / maintainer identity
- Any `[jhb]*` personal notes
- `eval/pilot/**` full gold / input / reconstruction texts
- Absolute filesystem paths (use paths relative to the repository root)
- `art-paper-anon-*.zip` / `_anonymous_cut/` packaging scratch (rebuild fresh)

## Pre-flight

```sh
rg -n '/home/jhbae|Cutting Kim|KAIST' eval/repro || true
```

Expect zero identity hits in the deposit tree (checklist command lines in this file alone may match the pattern text).

## Build cut (2026-09-10 Path B)

```sh
# Example: produce /tmp/art-paper-anon-YYYYMMDD then zip
rsync -a --exclude 'pilot' --exclude '__pycache__' --exclude 'art-paper-anon-*.zip' \
  eval/ /tmp/art-paper-anon-YYYYMMDD/eval/
cp eval/repro/ANONYMOUS_MIRROR.md /tmp/art-paper-anon-YYYYMMDD/README.md
```

Refresh `https://anonymous.4open.science/r/art-paper-BD19/` from that cut before reviewers are pointed at the URL. A packaged zip may sit at `eval/repro/art-paper-anon-*.zip` (gitignored) for editor handoff if the public mirror lags.
