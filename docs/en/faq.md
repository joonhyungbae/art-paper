# FAQ

## Where does the name come from?

The plugin is **Art-Paper**. It was forked from the upstream [`academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) and specialised down to a single scope: practice-based art-paper authoring.

## Why must I author the provocation? Can't the AI just write it?

The plugin can generate a provocation from the documented facts — and it will, if you don't supply one. But the provocation it generates is **the plugin's** reading of the work, not the artist's. For a practice-based paper, the artist's reading is the contribution; substituting another reading changes what is being published. The plugin can scaffold a provocation, but the artist is on the hook for whether to keep it.

## Does this plugin work for other genres beyond art papers?

It is bounded to practice-based art-paper authoring. The skills' prompts, references, and integrity checks are tuned for this scope. They may produce output for other genres, but the produced output is no longer warranted by the plugin's design — the dependent variable (documentable/generative split) loses its theoretical grounding outside practice-based research.

If you want a general scholarly-writing plugin, the upstream [`academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) is closer.

## How do I cite the plugin?

Cite the plugin as a software release:

```bibtex
@software{art_paper_2026,
  author       = {[author withheld]},
  title        = {Art-Paper: A Claude Code plugin suite for practice-based art research papers},
  year         = {2026},
  version      = {0.1.1},
  url          = {https://example.com/art-paper},
  note         = {CC-BY-NC 4.0}
}
```

## Can I use this plugin for venues other than SIGGRAPH Asia?

Yes — the plugin's scope is the *genre* (practice-based art research papers), not a single venue. Its defaults target SIGGRAPH Asia Art Papers convention (acmart class `sigconf` option, ACM Reference Format) as a reference, and SIGGRAPH (the main conference) Art Papers uses similar conventions. The methodology and integrity checks are venue-agnostic, and the `format-convert` mode produces acmart LaTeX that other venues accepting that class take with minor option changes. Always verify the current year's CFP for the venue you target; for venues that do not use acmart, treat the LaTeX output as a starting point rather than a camera-ready file.

## Does the plugin use my data to train the underlying model?

The plugin runs on the Anthropic Claude API. Whether your inputs and outputs are used for training depends on your Anthropic API agreement and account settings. The plugin itself does not record, archive, or transmit your inputs beyond what the Claude Code client does as part of normal operation.

## How do I report a bug or request a feature?

GitHub Issues on the [repository](https://example.com/art-paper/issues). Please specify your skill (`art-inquiry` / `art-paper` / `art-reviewer` / `art-pipeline`), mode, and the input materials' general shape (no need to share the actual artwork or paper unless you want to).

## License?

The plugin is licensed under **CC-BY-NC 4.0**. You may share and adapt for non-commercial purposes with attribution. Commercial use requires separate permission.
