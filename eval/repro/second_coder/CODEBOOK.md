# Second-coder codebook — RQ2 provocation pairs (Tier 1, N=15)

## Binary question (one judgement per case)

Given (i) a short paraphrase of the artist's published framing, (ii) a short paraphrase of the copilot's substitute provocation, and (iii) a one-line note on whether the input pack named the artist's frame object:

**Q:** Does the artist's framing commit to a stake that is not recoverable as mere description of the documented mechanism (fiction authored, debate entered, cost cared about in the making, etc.)?

Code `1` = yes (commitment/stake), `0` = no (mechanism-level or descriptive only).

Secondary (optional): Does the copilot's substitute take that same stake as its frame? `1`/`0`.

## Rules

- Judge from the provided text only; do not look up the paper.
- Commitment is about accountable stake-taking, not about which text sounds more eloquent or critical.
- If unsure, code `0` and mark `flag_uncertain=true`.

## Sheet

See `coding_sheet.csv`. Return filled sheet; we compute percent agreement / Cohen's κ against the authors' pre-codes in `author_precode.csv` once both exist.
