# Reproducibility package (scores, protocol artefacts — not full texts)

This folder is what Data availability points at beyond the metric engine in `eval/`.

## What is here

| Path | Contents |
|---|---|
| `tier1/*/instrumentation.json` | Per-case metric outputs for Tier 1 (+ clean controls) |
| `tier1/*/content_sha256.json` | SHA-256 of local gold/input/reconstruction files (integrity without releasing copyrighted text) |
| `tier1_table1_from_manuscript.csv` | Table 1 numbers as published (incl. input-pack baseline columns) |
| `tier1_baseline.json` + `baseline.py` | Input-pack baseline computation snapshot |
| `tier2/` | Held-out replication score JSON + cases manifest |
| `control/` | Control N=6 score JSON (**bibliographic DOIs not recovered in-repo** — see `UNRESOLVED.md`) |
| `case_to_doi.json` / `.csv` | Case/bibkey → DOI or ISEA proceedings locator |
| `prompts/` | Host reconstruction prompt excerpt + hyperparameters |

## What is intentionally not here

- Full gold papers, input packs, or reconstructions (ACM/venue copyright; ethics §5.3).
- To re-run the engine on new work: assemble `{gold,input,reconstruction}/` locally and call `python eval/instrumentation.py <case> --json`.

## Hyperparameters (harness path)

- Host model: `claude-sonnet-4-5-20250929`
- Temperature: `0.7` (API harness); Claude Code firewalled subagent runs used host defaults
- Judge / alternative classifier: `gpt-5.4-pro`
- Tier 1 sampling: fixed-seed stratified (numeric seed **not found** in tracked tree — mark UNKNOWN)

## Regenerating Tier 1 JSON

```sh
python eval/instrumentation.py eval/pilot/sa23-10 --json
```

Pilot directories under `eval/pilot/sa*/` remain gitignored; this `eval/repro/` tree is tracked.
