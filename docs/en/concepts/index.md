# Concepts

The plugin's design rests on three concepts that explain why it is shaped the way it is. Each concept has its own page.

Several of these pages cite *the companion methodology paper* — the study that introduced and validated the reconstruction-benchmark evaluation approach — as the source of their reported figures and reproducibility materials. The instrumentation script and pilot data are available at `eval/` in the plugin repository; the paper itself is in preparation.

| Concept | What it means | Where in the plugin |
|---|---|---|
| [Practice-based research](practice-based-research.md) | The artist knows things from the making that documentation alone cannot transfer | Why the dependent variable of the per-layer instrument is grounded in Schön/Polanyi/Borgdorff |
| [Reconstruction benchmark](reconstruction-benchmark.md) | Hide the published paper, have the plugin rebuild from pre-writing inputs, measure layer-by-layer | The evaluation methodology the companion paper introduces |
| [Inversion rule](inversion-rule.md) | Read high similarity to the held-out paper as contamination suspicion, not success | The `art-reviewer` integrity gate and the `art-paper citation-check` mode |

These three concepts together explain:

1. **Why** the plugin asks the artist (not the AI) to author the provocation and reflection
2. **How** the integrity gate decides what counts as a "memorisation" warning
3. **What** the plugin will and will not claim in its outputs

Read in this order if approaching the plugin's methodology fresh: practice-based research → reconstruction benchmark → inversion rule.
