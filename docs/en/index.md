# Art-Paper

A [Claude Code](https://www.anthropic.com/claude-code) plugin suite for **practice-based art research papers**. If you have made an artwork and need to write a scholarly paper about it — for SIGGRAPH Asia Art Papers or a comparable venue — this plugin gives Claude Code the skills to help you do that.

Its scope is the *genre*, not a single venue: the methodology and integrity checks are venue-agnostic. It defaults to the SIGGRAPH Asia Art Papers track's conventions (acmart, ACM Reference Format) as its reference target, and its output adapts to other venues that accept acmart LaTeX with minor option changes.

## What it does

The plugin gives Claude Code a set of skills that help an artist-researcher move from a documented artwork to a defensible scholarly paper, without replacing the artist's role in authoring the work's reading. The skills are:

| Skill | Purpose |
|---|---|
| **art-inquiry** | Upstream practice-based art-research engine — concept articulation, positioning, methodology, lineage |
| **art-paper** | Art-paper authoring engine — drafting, revision, abstract, format conversion |
| **art-reviewer** | Art Papers jury simulation (defaults to SIGGRAPH Asia conventions) — Chair, Curator, Practitioner-Researcher, Art-Science Critic, Devil's Advocate |
| **art-pipeline** | End-to-end orchestrator — inquiry → write → integrity → review → revise → finalise |

## Why a separate plugin for art papers

When you document a work and hand that documentation to a general AI writing tool, it produces a coherent paper — but the reading it advances is the AI's reading, not yours. The provocation, the reflection, the situated interpretation that came from making: those come from you, and a plugin that doesn't distinguish them from the documentable facts will substitute its own.

This plugin is designed for that gap. Each skill is bounded to assist your authoring without claiming to author on your behalf. The theoretical grounding (Schön, Polanyi, Borgdorff, Candy) is in [Concepts → Practice-based research](concepts/practice-based-research.md).

## Quick start

See [Getting started](getting-started.md) for installation and your first run. For a complete walkthrough of the plugin on a single artwork — input pack, firewalled reconstruction, and instrumentation — see [the Cutting Kim case study](examples/cutting-kim-case.md).

## Status

- **Suite version**: 0.1.1 (forked from `academic-research-skills` v3.9.4.2)
- **License**: CC-BY-NC 4.0
- **Last updated**: 2026-06-13

## What this plugin does NOT do

- It does **not** replace the artist's authorship of the work's reading. Art-paper skills explicitly mark generative-layer content as the artist's responsibility.
- It does **not** evaluate the artwork itself. There is no quality verdict on the art.
- It does **not** transfer automatically to other scholarly-writing genres. The skills are bounded to practice-based art-paper authoring.
