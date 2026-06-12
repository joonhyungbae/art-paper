# Examples

Worked examples of the plugin applied to real cases. Each example shows the complete pipeline from input materials to final artifacts, with the actual outputs the plugin produced.

## Available walkthroughs

| Case | What it demonstrates |
|---|---|
| [Cutting Kim — VR voice-interaction artwork by Bae, Choi & Nam (2025)](cutting-kim-case.md) | Full reconstruction-benchmark walkthrough on a SIGGRAPH Asia 2025 Art Paper contributed by its authors: input pack, firewalled plugin reconstruction, instrumentation, and a minimal-footprint clean-control variant |

## How the examples were generated

All examples use the actual plugin (Claude Code with `art-paper` skill, Anthropic API claude-sonnet-4-5 model) running on real input materials from previously-published practice-based art papers. The held-out gold papers are cited per their original publishers; the reconstructions are this plugin's outputs from the firewalled input packs.

The instrumentation numbers (T, G, contamination probe, structural coverage) are computed by the `eval/instrumentation.py` script in the companion paper's reproducibility mirror. The script is stdlib-only (no network, no model dependencies); anyone can re-run it on the input/reconstruction/gold trio.
