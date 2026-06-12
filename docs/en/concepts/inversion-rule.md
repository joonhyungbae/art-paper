# Inversion rule

## The rule, in one sentence

> Read high similarity to the held-out paper as contamination suspicion, not success.

## Why the rule is needed

A naive evaluation compares an AI-generated paper to the original, expecting high similarity to mean "AI did well". For practice-based art papers (and more generally, any small openly-published specialised genre), this is broken:

- The corpus is small enough that the original is plausibly memorised by the model
- Reference-based metrics reward memorisation under contamination, not authoring
- The people building the tool are also the people evaluating it — high-similarity-as-success would let any tool "win" by memorising

The inversion rule responds: **flip the reading direction.** High similarity to the held-out paper, especially in generative layers, is a memorisation warning.

## How the rule operates in the plugin

The contamination probe computes an 8-gram containment metric — the fraction of 8-token sequences in the reconstruction that appear verbatim in the gold paper. The probe has three sub-flags:

| Range | Sub-flag | Action |
|---|---|---|
| `< 0.03` | `ok` | No memorisation concern |
| `[0.03, 0.10)` | `elevated` | **Investigate** — content-preserving paraphrase or shared boilerplate |
| `>= 0.10` | `high-warning` | Memorisation flag — the inversion rule refuses to read the result as success |

The companion paper reports that for N=38 practice-based art papers, no case crossed the 0.10 threshold; for the F1 deliberate firewall-violation case (provocation injected into input), the probe rose to 0.0431 (`elevated`) as designed.

## What the rule does NOT do

- **It does not detect creative AI.** It detects verbatim or near-verbatim reproduction; semantic memorisation without lexical reproduction would not trigger the probe.
- **It does not score quality.** A reconstruction can pass the probe and still be poor; the probe is a contamination filter, not a quality measure.
- **It does not certify originality.** Passing the probe means "no detectable memorisation at the 8-gram level". Higher-order originality is a separate question the plugin does not answer.

## The combined verdict

The inversion rule alone is not sufficient. The plugin combines it with the **per-layer split**:

- Low contamination AND `T > G` → directional reading supported (the documentable layer converges more than the generative layer, as expected when the firewall holds)
- Low contamination AND `T ≤ G` → unusual; investigate the layer definitions or input-pack composition
- Elevated/high contamination, any `T-G` → contamination warning takes precedence; layer reading is unreliable

This is what the companion paper calls the "joint package" — firewall + inversion rule + per-layer instrument working together.

## Where it appears in the plugin

- `art-reviewer` integrity-gate logic applies the rule to a draft compared against any prior versions
- `art-paper citation-check` mode applies a citation-level analog (every citation must resolve to a verifiable locator)
- The full contamination probe and per-layer instrumentation live in the companion paper's `eval/instrumentation.py`
