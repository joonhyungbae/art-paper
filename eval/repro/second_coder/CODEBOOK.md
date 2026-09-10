# Second-coder codebook — seeded-pack 2×2 (Tier 1, N=15)

## Primary judgements (YN per case)

Materials in `coding_sheet.csv`: artist-framing paraphrase, copilot-substitute paraphrase, a short **pack excerpt**, and a short **reconstruction-frame excerpt**. Answer columns are blank. Do **not** open `author_precode.csv` or `../seeded_pack_2x2.json`.

**Q1 — `pack_mentions_object` (Y/N).** Identify the object of the artist's frame from the artist paraphrase (the stake/theme/claim, not merely the mechanism). Does the **pack excerpt** name that object (including a one-line theme or association)? **Y** / **N**. When unsure, **N** and `flag_uncertain=true`.

**Q2 — `copilot_took_as_frame` (Y/N).** Does the copilot substitute (and/or recon-frame excerpt) take that **same** object as its central frame? **Y** = same object as frame; **N** = different frame or mechanism-level only.

## Secondary (optional)

Stake beyond mechanism: note in `notes` if useful; not used for primary κ.

## Rules

- Use only the sheet columns; no paper lookup; no locked author files.
- Conservative on Q1: thematic keyword of the gold frame in the pack excerpt → **Y**.
- Return the filled sheet; agreement vs `author_precode.csv` (locked from `seeded_pack_2x2.json`).
