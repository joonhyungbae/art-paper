# Art-Research Ethics Decision Tree — Consent, Rights & Representation

> **art-paper genre note.** This file replaces ARS's IRB / Taiwan-human-subjects decision tree. For practice-based art research the load-bearing ethics dimensions are **copyright & exhibition/display rights, collaboration credit, fair representation of depicted people, and two-channel AI disclosure** — NOT human-subjects review. The canonical references are `ethics_checklist.md`, `shared/references/creative_art_terminology_glossary.md` (§4 credit, §5 rights), and `shared/references/siggraph_acm_disclosure.md`. **Human-subjects / formal ethics-board review (§3 below) applies ONLY when the inquiry observes, records, or runs a study with audiences/participants — i.e., the art-science hybrid (Pattern 5) case. Simply exhibiting a work to an audience is NOT human-subjects research.** Used by the `ethics_review_agent` and `research_architect_agent` during methodology design.

## Purpose
A decision guide for the ethics that actually bite in practice-based art research: who/what is depicted, whose rights are engaged, who is credited, and whether any audience-facing study tips the work into formal ethics review.

---

## 1. Art-Research Ethics Determination Decision Tree

```
Does your work / paper depict, record, or reuse identifiable people,
others' works, or community/cultural material?
│
├── No → Standard art-research ethics apply
│         (collaboration credit, AI disclosure, honest reception claims)
│
└── Yes → Which kind of material?
          │
          ├── Identifiable people (performers, participants, bystanders
          │   captured in documentation, portrait/likeness)
          │   → Consent for representation + image/likeness release
          │     (see §4). If filmed in public, check local likeness law.
          │
          ├── Others' artworks / images / footage / code / datasets
          │   → Copyright + licensing + courtesy line (see §5).
          │     Fair-dealing/fair-use is jurisdiction-specific — verify.
          │
          ├── Community / Indigenous / cultural-heritage material
          │   → Community consent + cultural protocols (e.g., CARE / OCAP
          │     principles); attribution on the community's terms.
          │
          └── An audience study (you observe, survey, interview, or
              record responses as DATA for the paper)
              → This is the art-science-hybrid case → go to §3
                (formal ethics-board review may be required).
```

---

## 2. When the work IS the research vs. when there is a human-subjects study

A persistent ARS-residue error is treating every audience as "human subjects." Disambiguate:

| Situation | Human-subjects review? | What governs it |
|---|---|---|
| Exhibiting / performing the work; people experience it | **No** | Exhibition rights, duty of care, honest reception reporting |
| Quoting a named critic's review of the work | No | Citation faithfulness (ACM Reference Format) |
| Documenting the work; identifiable people appear in stills/video | No formal board, but **yes** to likeness consent | Image/likeness release (§4) |
| You collect audience responses as evidence (survey, structured interview, recorded behaviour) and analyse them as data | **Likely yes** (Pattern-5 hybrid) | §3 + your institution's ethics process |
| You run a controlled study with participants (e.g., a perception experiment around the work) | **Yes** | §3 + institutional/board review |

> Rule of thumb: review the **study**, not the **exhibition**. The artwork is primary evidence; an audience experiencing it is not a research subject. Only when responses are collected and analysed as data does the human-subjects layer engage.

---

## 3. Audience-Study (Art-Science Hybrid) Review — only if §2 triggers it

If your inquiry includes a data-collecting audience study, treat it like any empirical human-subjects work and route it through your institution's ethics body (names vary: IRB, REC, ethics committee). **Verify the specific body and process against your institution and the current SIGGRAPH Asia Art Papers CFP — do not assume a particular jurisdiction.**

### 3.1 Typical review levels (institution-dependent)

| Level | Typical conditions | Indicative timeline |
|---|---|---|
| **Exempt / minimal** | Fully anonymous, no sensitive topics, public-behaviour observation with no identifiers recorded | ~1–2 weeks |
| **Expedited** | Minimal risk, no vulnerable participants, general surveys/interviews, recording with consent | ~2–4 weeks |
| **Full board** | Greater than minimal risk, vulnerable participants, sensitive content, deception | ~4–8 weeks |

### 3.2 What to prepare

- Study protocol (what is collected, how, why it answers the question)
- Participant information sheet + consent form (§4)
- Any instruments (survey, interview guide)
- Data-handling and retention plan

> Build the review timeline into the project schedule — board review can gate the exhibition/publication date.

---

## 4. Consent & Representation (the part that almost always applies)

In art research the recurring consent issue is **representation and likeness**, not survey participation.

### 4.1 Image / likeness release — required elements

- [ ] Who is depicted and in what work/documentation
- [ ] How the documentation will be used (exhibition, paper, ACM Digital Library, promotion)
- [ ] Whether the person is named or anonymised
- [ ] Whether they may withdraw, and by when (note: published proceedings are hard to retract)
- [ ] Performer/contributor credit line, if any
- [ ] Signature + date

### 4.2 Special situations

| Situation | Additional requirement |
|---|---|
| **Minors depicted** | Guardian consent + age-appropriate assent |
| **Bystanders in public-space documentation** | Check local likeness/privacy law; blur or consent where required |
| **Community / Indigenous material** | Community consent + cultural protocols (CARE/OCAP); attribution on their terms |
| **Performers / collaborators** | Named credit per `creative_art_terminology_glossary.md` §4; agree usage in advance |
| **Audience study (Pattern 5)** | Full informed-consent form per §3, including withdrawal and data-handling |

### 4.3 Consent / release template (representation)

```
Documentation & Representation Release

1. Work / project: [                    ]
2. Artist / researcher: [      ] / Affiliation: [        ]
3. What is being recorded / depicted: [                    ]
4. Uses: exhibition, conference paper, ACM Digital Library proceedings,
   archival documentation, promotion [delete as appropriate]
5. Naming: □ named as [        ]   □ anonymised
6. Withdrawal: you may withdraw consent until [date / milestone];
   note that published proceedings cannot easily be altered after release.
7. Credit line (if any): [                    ]
8. Contact: [Name] [Email]

□ I consent to the use of my likeness / contribution as described above.

Signature: __________ Date: __________
```

---

## 5. Rights, Licensing & Courtesy Lines (reused material)

When the work or paper incorporates others' material:

| Material | What to secure | In the paper |
|---|---|---|
| Another artist's work/image | Permission or a valid license | Courtesy line: "Courtesy of [artist] / Photo: [name]" |
| Stock / dataset / model | License compatible with exhibition + publication | Note the license; check ML-model output terms |
| Footage / sound | Sync/usage rights | Credit + license note |
| Your own prior work | Self-citation; note any gallery/publisher rights | Cite, courtesy line if rights held elsewhere |

- [ ] Every reproduced image has a courtesy/credit line (see glossary §5)
- [ ] Licenses cover BOTH exhibition and ACM proceedings publication
- [ ] AI-model-generated material: training-data/output terms checked; disclosed per the two-channel rule
- [ ] Fair-dealing/fair-use claims flagged as jurisdiction-specific — "verify against current law/CFP"

---

## Quick Reference: Artist/Researcher Self-Check

Before exhibiting or submitting, answer:

1. [ ] Are identifiable people depicted? If so, do I have likeness/representation consent?
2. [ ] Does the work reuse others' works, footage, datasets, or models? Are rights/licenses + courtesy lines in place — for exhibition AND publication?
3. [ ] Does any cultural/community material need community consent or specific protocols?
4. [ ] Is every collaborator credited by named role?
5. [ ] Are reception claims anchored to observable detail (no inflation)?
6. [ ] Is AI use disclosed in two channels (making the artwork vs. writing the paper)?
7. [ ] Do I collect audience responses as DATA? If yes → route through §3 ethics review and build the timeline in.
8. [ ] Have I flagged venue/jurisdiction-specific items with "verify against current CFP / local law"?
