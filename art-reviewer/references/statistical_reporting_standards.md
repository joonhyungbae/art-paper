# Art-Research Reporting Standards — Claim-Anchoring & Documentation Reference

> **Genre replacement note:** in ARS this file held statistical-reporting standards (effect sizes, CIs, power, APA format, p-hacking red flags). For art-paper those do **not** apply as a default quality bar — a practice-based art paper is not judged by statistical rigor. This file is the art-paper equivalent: the standards by which a reviewer judges whether a **claim about an artwork is adequately reported and anchored**. It is the primary reference for Reviewer 1 (Practitioner-Researcher)'s claim-anchoring step.
>
> The only exception is **Pattern 5 (art-science hybrid)**: if a paper carries a genuine empirical/technical sub-contribution with its own evaluation, statistical-reporting conventions may apply to *that sub-part only*, framed as situated. Do not import them onto the artistic contribution.

Anchored in `shared/references/art_research_evidence_model.md`, `shared/references/creative_art_terminology_glossary.md`, and `shared/references/acm_reference_format.md`.

---

## 1. What "adequately reported" means for an art paper

A claim is adequately reported when it is **anchored to an evidence type** and that anchor is documented well enough that a reader could, in principle, verify it (evidence model §3). The five evidence types:

| Evidence type | Adequate report looks like |
|---|---|
| The work as encountered | description + stills / video / diagram / live-demo reference |
| Process & making | process notes, system/code description, fabrication record, version history |
| Exhibition & reception | named venue + date, install photos, observed/recorded response, press, curatorial framing |
| Conceptual lineage | real citations (ACM Reference Format) to precedent works / theory / criticism |
| Situated reflection | the author's reasoned account, made checkable by the above |

---

## 2. Claim-Anchoring Checklist (Reviewer 1 primary use)

For each load-bearing claim, check:

1. **Work claims** — is a claim about form/experience/materiality anchored to a figure/media reference or concrete description?
2. **Reception claims** — is a claim about audience response anchored to a named venue/date + observable detail (never "audiences loved it")?
3. **Technical/capability claims** — is "real-time" / "autonomous" / "generative" / "novel algorithm" anchored to a realization account specific enough to be plausible, and is the term used per glossary §3?
4. **Precedence/novelty claims** — is "the first work to…" backed by a citation or hedged?
5. **Materiality claims** — can the reader tell what the work physically is (medium / material / format kept distinct, glossary §6)?
6. **Authorship claims** — are contributor roles named where the work is collaborative (glossary §4)?
7. **Documentation rights** — are reproduced images / install photos accompanied by a courtesy line / permission note (glossary §5)?

**Reporting-adequacy signal** (parallel to the old completeness score):
Exemplary / Adequate / Needs Strengthening / Inadequate / Unacceptable
plus a specific list of which claims need an anchor and what documentation would supply it.

---

## 3. Over-Claim Red Flags (integrity-relevant)

These mirror the integrity-gate flags in `art_research_evidence_model.md` §4. Flag for verification:

| Red flag | What it looks like |
|---|---|
| **Reception inflation** | "widely acclaimed," "audiences were moved/amazed" with no observable anchor |
| **Capability over-claim** | "fully autonomous," "the AI understands/creates" with no realization anchor (fabricated capability) |
| **Precedence inflation** | "the first work to…" omitting obvious precedents in the lineage |
| **Documentation-as-work** | an experiential claim resting on a render/video treated as the work itself |
| **Attribution drift** | collaborative work described as solo, contributors unnamed |
| **Exhibition fabrication** | venues/dates/awards that may not be real — treated like citation faithfulness |
| **Over-generalized insight** | situated insight stated as a universal finding (worse than honest specificity) |

These flags **block** the Stage 2.5 / 4.5 integrity gate exactly as citation/data issues do in ARS (same blocking semantics, same max-3-round fix loop).

---

## 4. Citation reporting (ACM Reference Format)

Per `shared/references/acm_reference_format.md`:

- Papers/journals: standard ACM entries; DOI where available.
- **Artworks / exhibitions**: cite artist, title, year, medium, exhibition venue via `@misc` / `@online` with `note` / `url` + access date. **Do NOT invent DOIs for artworks.** The natural L3 locator is the **venue + date** or a timestamp into documentation media.
- A citation with NO locator is hard-gate-refused by the formatter (L3 gate, unchanged from ARS).
- Artwork/exhibition entries are checked for **real-venue plausibility**, not DOI resolution.
