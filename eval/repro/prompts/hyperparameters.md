# Generation hyperparameters

| Channel | Model | Temperature | Seed |
|---|---|---|---|
| Host reconstructions (Tier 1 API path) | `claude-sonnet-4-5-20250929` | `0.7` | Anthropic API has no seed; label `42` recorded in brief_reconstructor |
| Host reconstructions (Claude Code firewalled subagent) | Claude Sonnet 4.5 via host defaults | host default (documented as default settings in manuscript; harness path uses 0.7) | n/a |
| Blind judge / alternative classifier | `gpt-5.4-pro` | suite default | n/a |
| Embedding (optional) | `BAAI/bge-small-en-v1.5` | n/a | n/a |

Sampling of the Tier 1 corpus is described in the manuscript as fixed-seed stratified on outcome-independent features; the numeric seed value was not recovered in the tracked repository and is marked UNKNOWN pending author confirmation.
