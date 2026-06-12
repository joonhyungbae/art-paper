# Reconstruction benchmark

## The setup

The reconstruction benchmark is the evaluation methodology the plugin's companion paper introduces. It has four parts:

1. **Input/gold firewall.** A human auditor enforces a procedural separation between materials given to the plugin (inputs) and the published paper held back (gold).
2. **Reconstruction task.** The plugin is given only the pre-writing inputs (documentation, exhibition record, factual concept memo, bibliography) and asked to rebuild the paper.
3. **Inversion rule.** Similarity to the held-out paper is read as contamination suspicion, not success. (See [Inversion rule](inversion-rule.md).)
4. **Per-layer split.** Similarity is measured separately for "documentable" layers (factual description, prior-work lineage, exhibition record) and "generative" layers (provocation, reflection, situated discussion).

## What the benchmark measures

For each case, the instrumentation reports:

- **Transferable-layer similarity** `T` — how close the rebuilt documentable content is to the gold
- **Generative-layer similarity** `G` — how close the rebuilt generative content is to the gold
- **Per-layer ordering** — whether `T > G` (expected: the documentable layer reconstructs more closely than the generative layer)
- **Contamination probe** — 8-gram overlap between reconstruction and gold; flags potential memorisation
- **Structural coverage** — what proportion of the gold's section structure the reconstruction reproduces
- **Citation recall and precision** — how the rebuilt bibliography overlaps with the gold's

## What the benchmark does NOT measure

- Whether the AI's output is "good"
- Whether the AI is creative
- Whether a user would find the output useful

These are out of scope by design. The benchmark exists to detect, in a specific corpus, whether the documentable-versus-generative distinction is detectable — nothing more.

## The "discriminant validity" check

Running the benchmark on a corpus other than practice-based art papers (e.g., PLOS ONE empirical research) helps detect whether the layer-split signature is unique to practice-based writing or is a general property. If the signature appears in non-practice-based corpora too, the signature is a property of the layer definitions, not of practice-based research per se. (The companion paper reports this for N=6 PLOS ONE papers; the signature does appear but with high contamination, distinguishing the corpora at the contamination axis.)

## The "clean control" check

A stricter version of the benchmark constructs the input pack from the artwork's **independent public footprint** (artist's external statements, festival pages, exhibition catalogs) rather than from the gold paper. This protects against the possibility that the input extraction itself carries authorial cues. The companion paper reports this on 3 cases (sa23-10, sa24-18, sa24-12); the directional signal survives but margins shrink, consistent with input-pack extraction contributing a non-zero artifact.

Clean control is bounded by what each case's independent footprint contains — most papers in the evaluation corpus (drawn from SIGGRAPH Asia) list a single exhibition venue, so the clean-control extension is corpus-bound rather than effort-bound.

## Where it appears in the plugin

- The `art-paper` skill `citation-check` mode runs the citation-locator audit that is one part of the benchmark
- The `art-reviewer` skill's integrity-gate logic uses the same inversion rule
- The full instrumentation script lives in the `eval/instrumentation.py` of the companion paper's reproducibility mirror
- A worked example of the benchmark applied to a single case is in [the Cutting Kim case study](../examples/cutting-kim-case.md)
