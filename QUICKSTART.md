# Quick Start

Get from zero to your first AI-assisted art paper in 3 steps.

art-paper is a suite of Claude Code skills for **practice-based art research papers** across art-and-technology venues. Scope is the *genre*, not a single venue; the methodology and integrity checks are venue-agnostic. Default reference target: the **SIGGRAPH Asia Art Papers track** (proceedings on the ACM Digital Library; verify category/venue against the current CFP), wired to `acmart` + ACM Reference Format. Alternate venues are supported via citation-format conversion (APA 7.0 / Chicago / MLA 9 / IEEE / Vancouver) and the five art-paper structure patterns. It is forked from [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills); the genre-neutral pipeline machinery is inherited, the genre layer is re-specialized for art research.

## Step 1: Install

Inside Claude Code:

```text
/plugin marketplace add example/art-paper
/plugin install art-paper
```

That installs all four skills (`art-inquiry`, `art-paper`, `art-reviewer`, `art-pipeline`) plus the 15 `/art-*` slash commands. If you prefer the manual `git clone` + `ln -s` route, or need installation into a global `~/.claude/skills/`, see [docs/SETUP.md](docs/SETUP.md).

To compile the canonical **acmart LaTeX → PDF** output you need a LaTeX toolchain (tectonic or a full TeX distribution). Install the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template) from CTAN or the ACM. Markdown output works without it.

## Step 2: Launch

```bash
claude
```

## Step 3: Start working

Tell Claude what you want to do. It will automatically pick the right skill and mode.

### Example: Guided inquiry (Socratic mode)

```
You: "I have a vague idea about an interactive installation that responds to
      audience movement, but I'm not sure how to frame the conceptual provocation.
      Can you guide me?"
```

Claude will enter Socratic mode — asking questions to help you clarify your artistic concept and positioning, not giving you answers directly. After 5-15 rounds of dialogue, you'll have a focused provocation and a practice-based methodology direction.

### Example: Write an art paper

```
You: "Help me write a SIGGRAPH Asia art paper documenting my generative-art
      series and what the practice revealed about machine autonomy"
```

### Example: Draft an artist statement

```
You: "Draft an artist statement for my net-art piece"
```

### Example: Review an existing art paper

```
You: "Review this art paper" (then paste or attach the paper)
```

### Example: Full pipeline (inquiry → write → jury review → revise → finalize)

```
You: "I want to produce a complete SIGGRAPH Asia art paper about my bio-art
      installation and its exhibition reception"
```

This triggers the full 10-stage pipeline, ending in an acmart LaTeX → PDF manuscript. Budget a few hours of collaborative work; see [docs/PERFORMANCE.md](docs/PERFORMANCE.md) for token-cost estimates.

## Which mode should I use?

| I want to... | Use this |
|-------------|----------|
| Explore a vague artistic idea | `art-inquiry` socratic mode — just describe your interest |
| Get a quick precedent / theory summary | `art-inquiry` quick mode |
| Survey a subfield rigorously (PRISMA) | `art-inquiry` systematic-review mode |
| Write an art paper from scratch | `art-paper` full mode |
| Plan an art paper section by section | `art-paper` plan mode |
| Draft an artist statement | `art-paper` artist-statement mode |
| Document an artwork (materials, process, exhibition) | `art-paper` work-doc mode |
| Get my art paper reviewed by a simulated jury | `art-reviewer` full mode |
| Do everything end-to-end | `art-pipeline` — say "I want a complete SIGGRAPH Asia art paper" |

## What's next?

- [Full README](README.md) — all features, modes, installation options, and changelog
- [Fork design spec](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md) — how art-paper re-specializes ARS for art research
- [한국어 README](README.ko-KR.md) — Korean overview

> art-paper is English-first (a Korean README is maintained).
