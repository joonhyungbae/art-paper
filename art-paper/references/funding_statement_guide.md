# Funding / Support Acknowledgment Guide (Art Papers)

Used by `intake_agent`, `formatter_agent`, and `draft_writer_agent`.

> **art-paper art-genre note.** In a practice-based art paper the "funding statement" is broader than a research grant: it acknowledges the **material support that made the artwork and its exhibition possible** — arts-council grants, foundation funding, residencies, commissions, fabrication/production support, in-kind technical support, and venue/institutional support. Place this in the **Acknowledgments** (with collaboration credit and image courtesy lines), not in a methods/COI block. Verify the exact placement and any required wording against the current **SIGGRAPH Asia Art Papers CFP / ACM** policy. Where the ACM `acmart` template provides funding metadata commands (e.g., `\thanks` / acknowledgment block), prefer those.

---

## What to acknowledge (art-research support types)

| Support type | Examples | Notes |
|---|---|---|
| **Grants** | National/regional arts councils, culture ministries, private foundations | Use the funder's official name; include a grant/reference number if one was issued |
| **Residencies** | Studio/lab residency that produced the work (e.g., a media-art lab, museum lab, university research-creation centre) | Name the host and the residency period |
| **Commissions** | Festival, museum, biennale, or private commission | Name the commissioning body and the occasion |
| **Production / fabrication support** | Fabrication shop, AV/technical provider, software/hardware sponsor, materials donor | In-kind support is acknowledged here; named technical collaborators who shaped the work belong in **collaboration credit** (`credit_authorship_guide.md`), not merely here |
| **Institutional support** | University, studio, gallery providing space, equipment, or staff time | |
| **Open-access / publication fees** | If an APC or page charge was covered by a grant, note it if the venue requires |

> Distinguish **support** (acknowledged here) from **authorship / collaboration credit** (named contributors who conceived/realized the work — see `credit_authorship_guide.md`) and from **image courtesy / copyright lines** (per `shared/references/creative_art_terminology_glossary.md` §5). A funder that only paid does not become a co-author; a person who only paid does not get a credit line.

---

## Statement templates

These are language-neutral skeletons. Match the statement language to the paper language; do not invent grant numbers or funder names — leave a placeholder and a "verify" note when unknown.

### Grant-supported (single source)

```
Acknowledgments: This work was supported by [Funder Full Name]
([Programme / Grant Type], Grant No. [Number]).
```

### Grant-supported (multiple sources)

```
Acknowledgments: This work was supported by [Funder 1] (Grant No. [Number 1]);
[Funder 2] (Grant No. [Number 2]); and [Funder 3] (Grant No. [Number 3]).
```

### Residency

```
Acknowledgments: This work was developed during a residency at
[Host Institution / Lab], [City], [Month Year – Month Year].
```

### Commission

```
Acknowledgments: [Work Title] was commissioned by [Commissioning Body]
for [Occasion / Festival / Exhibition], [Year].
```

### Production / in-kind support

```
Acknowledgments: Fabrication / technical support was provided by
[Provider]. [Hardware / software / materials] were supported by [Sponsor].
```

### No external support

```
Acknowledgments: This work received no external funding or production support.
```

---

## Funder disclaimers (when required)

Some funders require a specific disclaimer to be quoted **verbatim** (this is common for public arts-council and research-council funding). When a funder mandates a disclaimer, reproduce it exactly and do not paraphrase. Generic skeleton:

```
The views expressed are those of the author(s) and do not necessarily reflect
those of [Funder].
```

Check the funder's acknowledgment guidelines for the exact required text.

---

## International funding / arts-support bodies (illustrative)

Names and exact formats change; always verify against the funder's current guidelines. This list is illustrative, not exhaustive, and spans arts councils, foundations, and research-creation councils that fund art-and-technology practice:

| Body | Region | Kind |
|---|---|---|
| National Endowment for the Arts (NEA) | USA | Arts grant |
| Arts Council England | UK | Arts grant |
| Canada Council for the Arts | Canada | Arts grant |
| Creative Europe | EU | Arts/culture programme |
| Mondriaan Fund | Netherlands | Visual-arts fund |
| Japan Foundation / Agency for Cultural Affairs | Japan | Culture/arts support |
| National Culture and Arts Foundation | Taiwan | Arts grant |
| Prince Claus Fund | International | Arts/culture fund |
| Ars Electronica / ZKM / festival production funds | International | Commission / production |

Research-creation work that crosses into a science/engineering collaboration (Pattern 5) may also acknowledge a science/engineering research council (e.g., NSF, ERC, JSPS, a national research council); use that body's required acknowledgment wording in addition to the arts-support acknowledgment.

---

## Best practices

- [ ] All support sources listed (grants, residencies, commissions, production, in-kind, institutional)
- [ ] Funder / host / commissioner names use official full names
- [ ] Grant/reference numbers included where issued (never fabricated)
- [ ] Any funder-mandated disclaimer quoted verbatim
- [ ] Support (acknowledgment) kept distinct from authorship/collaboration credit and from image courtesy lines
- [ ] Statement language matches the paper language
- [ ] If no external support, state so explicitly
- [ ] Placement and required wording verified against the current SIGGRAPH Asia Art Papers CFP / ACM policy

---

## Reference resources

- Verify the current SIGGRAPH Asia Art Papers CFP / ACM author guidelines for the required acknowledgment placement and AI-disclosure interaction.
- Crossref Funder Registry (for canonical funder names): https://www.crossref.org/services/funder-registry/
- Each funder's own acknowledgment/credit guidelines (authoritative for required wording).
