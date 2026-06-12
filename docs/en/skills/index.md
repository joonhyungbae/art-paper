# Skills

The plugin ships with four skills. Each skill has its own SKILL.md spec; this page is the user-facing index.

| Skill | When to invoke | Key modes |
|---|---|---|
| [art-inquiry](art-inquiry.md) | When you have a work and a question but no draft | `socratic`, `full`, `quick`, `review`, `lit-review`, `fact-check`, `systematic-review` |
| [art-paper](art-paper.md) | When you have the inquiry materials and want to draft / revise | `plan`, `full`, `outline-only`, `revision`, `revision-coach`, `abstract-only`, `lit-review`, `format-convert`, `citation-check`, `disclosure`, `artist-statement`, `work-doc` |
| [art-reviewer](art-reviewer.md) | When you have a draft and want jury-style review | `full`, `re-review`, `quick`, `realization-focus`, `guided`, `calibration` |
| [art-pipeline](art-pipeline.md) | When you want end-to-end orchestration | (coordinates all of the above) |

## Slash commands

Each mode is also reachable as an explicit `/art-*` slash command (frontmatter pins the model — `opus` for the heavy pipeline/review work, `sonnet` for the focused single-pass modes). You can always invoke a skill in prose instead; these are the shortcuts.

| Command | Routes to | Model |
|---|---|---|
| `/art-full` | art-pipeline — full pipeline (inquiry → write → review → revise → finalize) | opus |
| `/art-reviewer` | art-reviewer — full jury review | opus |
| `/art-revision-coach` | art-paper — parse jury comments → Revision Roadmap + Response Letter | opus |
| `/art-plan` | art-paper — Socratic section-by-section planning | sonnet |
| `/art-outline` | art-paper — detailed outline + evidence map | sonnet |
| `/art-revision` | art-paper — revised draft + responses to jury | sonnet |
| `/art-abstract` | art-paper — abstract + keywords | sonnet |
| `/art-lit-review` | art-paper — conceptual-lineage / precedent-works review | sonnet |
| `/art-artist-statement` | art-paper — concept-forward artist statement | sonnet |
| `/art-work-doc` | art-paper — artwork documentation (figures, install record) | sonnet |
| `/art-format-convert` | art-paper — convert between acmart LaTeX / DOCX / PDF / Markdown | sonnet |
| `/art-citation-check` | art-paper — ACM Reference Format citation error report | sonnet |
| `/art-disclosure` | art-paper — two-channel AI-usage disclosure | sonnet |
| `/art-mark-read` / `/art-unmark-read` | art-paper — record / rescind a human-read signal for citation keys | sonnet |

There is no standalone `/art-inquiry` or `/art-paper` command — invoke those skills in prose (e.g. "draft my art paper from input/"), or enter them through `/art-full`.

## Routing discipline

If the user explicitly types a `/art-*` slash command, that takes priority. Otherwise the plugin classifies the situation and routes:

1. **Explicit clear intent** → run named skill directly
2. **Cross-phase materials, no named skill** → clarify which workflow first (no auto-routing past ambiguity)
3. **Ambiguous, no materials** → clarify

This is documented in detail in `.claude/CLAUDE.md` § Routing Discipline.
