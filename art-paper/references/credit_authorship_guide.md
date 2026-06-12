# Collaboration & Contribution Credit Guide (Art Papers)

Used by `intake_agent`, `formatter_agent`, and `draft_writer_agent`.

## Overview

In a practice-based art paper, **collaboration credit** names *who did what on the work* — concept, code, fabrication, sound, performance, choreography, text, production. Describing collaborative work as solo, or omitting named contributors, is an **integrity flag** (see `shared/references/creative_art_terminology_glossary.md` §4 and `art_research_evidence_model.md`).

art-paper uses two complementary credit vocabularies; pick per the work and venue:

1. **Art-collaboration credit lines** (preferred for the work itself) — free-form named roles drawn from how the work was actually made, e.g. *"Concept and direction: X; custom electronics and firmware: Y; sound: Z; fabrication: W; performers: …"*. This is the natural form for installation, performance, and media-art credits and for festival/exhibition conventions.
2. **CRediT (Contributor Roles Taxonomy)** — a standardized 14-role taxonomy co-developed by CASRAI and NISO (2015), used by many ACM-adjacent and journal venues for the **paper's** authorship metadata. Useful for the art-science hybrid (Pattern 5) and whenever the target venue's submission system collects CRediT roles. Each author may hold one or more roles; each role may be held by one or more contributors.

> The CRediT roles below are mapped to **art-making activities**. Where a role has no natural analogue in a given work, omit it — do not force empirical-study roles (e.g., "Data curation") onto a work that has no dataset. For purely artistic works, the free-form credit lines in (1) are usually clearer than the CRediT grid; reserve CRediT for venue-required metadata and for Pattern 5 hybrids.

---

## CRediT 14 Contribution Roles

### 1. Conceptualization

**Definition**: Ideas; formulation or evolution of the work's overarching concept, provocation, and artistic direction.

**Art-Making Examples**:
- Originating the work's concept and provocation (the load-bearing idea the piece investigates)
- Setting the artistic direction and the form the work would take (e.g., a gaze-driven interactive installation)
- Framing how the work positions itself against precedent works in the lineage

### 2. Data Curation

**Definition**: For works built on a corpus/dataset — assembling, cleaning, annotating, and maintaining the source material (images, audio, sensor logs, training data) that the work draws on.

**Art-Making Examples**:
- Assembling and curating the image/audio corpus a generative work is trained or drawn on (with rights/source records)
- Cleaning and annotating sensor or capture data used by an interactive piece
- Maintaining the archive of process documentation and iterations
- *(Omit this role for works with no underlying dataset.)*

### 3. Formal Analysis

**Definition**: (Mainly Pattern 5 hybrids) Application of computational, statistical, or other formal techniques to a quantitative sub-study around the work.

**Art-Making Examples**:
- Analyzing logged audience-interaction data from an installation (Pattern 5)
- Evaluating a model/system's behaviour with a formal metric in an art-science study
- *(Omit for purely artistic works; reception evidence is usually observational, not statistical — see `art_research_evidence_model.md`.)*

### 4. Funding Acquisition

**Definition**: Acquisition of the grants, commission, residency, or production support that made the work and its exhibition possible.

**Art-Making Examples**:
- Securing an arts-council or foundation grant for the work
- Obtaining a festival/museum commission or a production residency
- Arranging in-kind fabrication or technical sponsorship
- *(Acknowledged as support — see `funding_statement_guide.md`; a funder is not a co-author.)*

### 5. Investigation

**Definition**: Carrying out the hands-on making, experimentation, and material/technical exploration that realized the work.

**Art-Making Examples**:
- Prototyping and iterating the work's behaviour and physical form
- Running material/technical experiments (sensors, projection, custom electronics, model tuning)
- Conducting studio tests and on-site installation trials

### 6. Methodology

**Definition**: Development or design of the work's method of making — its systems, processes, and the practice-based methodology.

**Art-Making Examples**:
- Designing the generative system / interaction model / signal chain
- Developing the practice-based methodology (iterative making + situated reflection)
- Devising the fabrication or performance approach

### 7. Project Administration

**Definition**: Management and coordination of the work's production and exhibition.

**Art-Making Examples**:
- Coordinating a collaborating team (engineers, fabricators, performers) and the production schedule
- Managing a commission's milestones and the install timeline
- Liaising with the venue on logistics, rights, and exhibition setup

### 8. Resources

**Definition**: Provision of materials, equipment, fabrication facilities, computing, performers, or other means of production.

**Art-Making Examples**:
- Providing a fabrication shop, AV equipment, or studio/lab space
- Providing computing/GPU resources for a generative model
- Providing performers, instruments, or specialist materials

### 9. Software

**Definition**: Programming and software development for the work; implementation of the systems, firmware, and supporting code.

**Art-Making Examples**:
- Writing the real-time interaction / generative software driving the work
- Developing custom firmware for bespoke electronics
- Building the pipeline that produces the work's output (with testing)

### 10. Supervision

**Definition**: Oversight and artistic leadership of the work's realization, including mentorship of collaborators external to the core team.

**Art-Making Examples**:
- Leading the artistic vision and overseeing collaborators' contributions
- Directing a performance/production team
- Mentoring assistant artists or technicians on the realization

### 11. Validation

**Definition**: Verifying that the work behaves and is experienced as intended; for Pattern 5, checking reproducibility of any reported technical results.

**Art-Making Examples**:
- Testing that the interactive/generative system behaves reliably under exhibition conditions
- Confirming the installed work matches the intended experience across runs
- (Pattern 5) Cross-checking reported technical/quantitative results

### 12. Visualization

**Definition**: Preparation of the work's documentation and any figures/diagrams presented in the paper.

**Art-Making Examples**:
- Producing install photography, stills, and documentation video of the work
- Drawing system / signal-flow / process diagrams for the Realization section
- (Pattern 5) Creating charts for a quantitative sub-study — see `statistical_visualization_standards.md`

### 13. Writing -- Original Draft

**Definition**: Preparation of the published work, specifically writing the initial draft of the paper (including substantive translation).

**Art-Making Examples**:
- Writing the complete initial draft of the art paper (all sections)
- Drafting specific sections (e.g., The Work, Realization, or Reflection)
- Translating a draft into the submission language

### 14. Writing -- Review & Editing

**Definition**: Critical review, commentary, or revision of the paper by those from the original team — pre- or post-publication.

**Art-Making Examples**:
- Reviewing and revising co-authors' drafts
- Revising in response to the jury/curatorial review
- Proofreading the final version for text and formatting

---

## ICMJE Authorship Criteria

The International Committee of Medical Journal Editors (ICMJE) authorship criteria are widely referenced across all academic disciplines. **All four conditions must be met** to be listed as an author:

| # | Condition | Description |
|---|------|------|
| 1 | Substantial contributions | Substantial contributions to the conception or design; or to the acquisition, analysis, or interpretation of data |
| 2 | Drafting or revising | Participation in drafting the manuscript or critically reviewing important intellectual content |
| 3 | Final approval | Approval of the final version for submission |
| 4 | Accountability | Agreement to be accountable for all aspects of the work, ensuring that questions related to the accuracy or integrity of any part are appropriately investigated and resolved |

### Contributions That Do Not Qualify for Authorship

The following contributions typically **do not qualify** for authorship and should be listed in the Acknowledgments:

- Providing funding, commission, or in-kind support only (→ acknowledge as support)
- Providing administrative support, space, or equipment only
- Language editing or translation only
- General installation/transport labour with no shaping of the work
- Holding a supervisory title only (without actual involvement in making the work)

> Note: ICMJE is a medical-journal framework adopted broadly; for art papers it is a useful sanity check on the *paper's* authorship, but the **work's** maker credits follow practice convention (free-form named roles above). A contributor who genuinely shaped the work — e.g., wrote core software, composed the sound, engineered the electronics — is a maker/collaborator even if they did not write the paper.

---

## Free-Form Art-Collaboration Credit Lines (preferred for the work)

For most practice-based works, named role lines read more clearly than the CRediT grid and match festival/exhibition convention. Name every contributor whose work shaped the piece:

```
Concept and direction: [Artist A]
Custom electronics and firmware: [B]
Generative software: [A, B]
Sound: [C]
Fabrication: [D]
Performers: [E, F]
```

> Omitting a named contributor, or presenting collaborative work as solo, is an integrity flag. In-kind/financial backers are acknowledged as **support** (`funding_statement_guide.md`), not listed as makers.

## Contribution Matrix Example (CRediT — for venue metadata / Pattern 5)

### Contributor x Role Matrix

| Role | Artist A (Corresponding) | Collaborator B | Collaborator C |
|------|:---:|:---:|:---:|
| Conceptualization | Lead | Supporting | -- |
| Methodology (system / process of making) | Lead | Supporting | -- |
| Software | Supporting | Lead | -- |
| Investigation (making / prototyping) | Lead | Supporting | Supporting |
| Resources (fabrication / equipment) | -- | Lead | -- |
| Funding acquisition (grant / commission) | Lead | -- | -- |
| Visualization (work documentation) | Supporting | Lead | -- |
| Validation (works-as-intended) | Lead | Supporting | Supporting |
| Project administration | Lead | -- | -- |
| Writing -- original draft | Lead | Supporting | -- |
| Writing -- review & editing | Lead | Supporting | Supporting |

*(Omit roles with no analogue in the work — e.g., Data curation / Formal analysis for a piece with no dataset.)*

**Label Descriptions**:
- **Lead**: Primarily responsible for this contribution
- **Supporting**: Assisting or auxiliary role
- **--**: Did not participate

---

## AI Not Listed as Author Policy

### Major Publisher and Organization Positions

| Organization/Publisher | Policy Summary | Effective Date |
|------------|---------|---------|
| **ICMJE** | AI tools do not meet the four authorship criteria (cannot be accountable, cannot approve); must not be listed as authors | 2023 |
| **APA** (American Psychological Association) | AI not listed as author; AI use must be disclosed in methods or acknowledgments | 2023 |
| **Nature/Springer Nature** | LLMs not listed as authors; must disclose usage in methods or acknowledgments | 2023 |
| **Science/AAAS** | AI-generated text cannot be presented as original work; AI use must be disclosed | 2023 |
| **Elsevier** | AI tools not listed as authors; must disclose in the manuscript | 2023 |
| **Wiley** | AI not listed as author; must describe usage in acknowledgments | 2023 |
| **Taylor & Francis** | AI not listed as author; must disclose AI use at submission | 2023 |
| **IEEE** | AI must not be listed as author or co-author | 2023 |

### AI Disclosure Best Practices

1. **Clearly state in the Realization/Acknowledgments and a dedicated disclosure** which AI tools were used and how. For art papers use the two-channel disclosure: AI used to MAKE the artwork vs. AI used to WRITE the paper (see `shared/references/siggraph_acm_disclosure.md`).
2. **Authors/artists take full responsibility** for all AI-assisted output content
3. **AI-produced text must not be directly presented as original scholarly findings**; AI-generated artwork content must be disclosed as the artistic-making channel
4. **Recommended format for citing AI tools** — default ACM Reference Format (art-paper default); APA 7th shown as the alternate:

```
ACM Reference Format (default):
  OpenAI. 2024. ChatGPT (GPT-4). Large language model. https://chat.openai.com/

APA 7th (alternate):
  OpenAI. (2024). ChatGPT (Version GPT-4) [Large language model]. https://chat.openai.com/
```

---

## Credit Conventions Across Venues

| Venue | Credit convention | Format |
|------------|------------|------|
| **SIGGRAPH Asia / SIGGRAPH Art Papers (ACM)** | Free-form maker credits expected for the work; CRediT optional in submission metadata | Named credit lines in the paper; verify against current CFP |
| ACM Creativity & Cognition / TEI | Maker credits; CRediT collected in some submission systems | Named credit lines + system metadata |
| *Leonardo* / ISEA (non-ACM) | House/venue convention; named maker credits | Per venue guidelines |
| Festival / exhibition catalogs | Free-form credit block (the dominant art-world convention) | Named roles, often with a "Courtesy" line |
| Pattern 5 / journal-style venues using CRediT | Standardized 14-role taxonomy | In-text statement or submission system |

---

## Boundary Between Maker Credit and Acknowledgment

| Credit as a Maker / Collaborator | Acknowledge (not a maker) |
|---------|---------|
| Originated the work's concept / artistic direction | Provided administrative or logistical support |
| Wrote core software / firmware for the work | Language editing / translation of the paper |
| Composed the sound, engineered the electronics, did the fabrication | General install / transport labour |
| Performed in / co-created the work | Provided funding, commission, or in-kind support only |
| Designed the system / process of making | Provided space or equipment only |
| Substantially wrote or revised the paper | Held a supervisory title without involvement |

### Acknowledgments Section Example

```
The artist thanks [Name] for installation assistance, [Name] for documentation
photography, and the anonymous jury for their constructive feedback. [Work Title]
was developed with the support of [Arts Council / Foundation] and produced during
a residency at [Lab / Studio]. Installation views courtesy of the artist and [Venue].
```

> Keep three things distinct in the front/back matter: **collaboration credit** (named makers, above), **support/acknowledgment** (grants, residencies, in-kind — `funding_statement_guide.md`), and **image courtesy / copyright lines** (per `creative_art_terminology_glossary.md` §5).

---

## CRediT Statement Template

**Author Contributions Statement**:

```
[Author A]: Conceptualization, Methodology, Funding acquisition,
Writing – original draft, Supervision, Project administration.
[Author B]: Data curation, Formal analysis, Software, Visualization,
Writing – original draft, Writing – review & editing.
[Author C]: Investigation, Validation, Writing – review & editing.
```

> art-paper v0.1 ships English-only paper output. Multi-language CRediT mappings (inherited from ARS) are deferred to a later release.

---

## Reference Resources

- Two-channel AI-usage disclosure (artwork-making vs paper-writing): `shared/references/siggraph_acm_disclosure.md` — verify against current SIGGRAPH Asia Art Papers CFP / ACM policy
- art-paper art terminology (authorship/credit, copyright/exhibition rights, reception): `shared/references/creative_art_terminology_glossary.md`
- CRediT official taxonomy: https://credit.niso.org/
- ICMJE authorship criteria (broad sanity check on paper authorship): https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html
- ACM authorship / publication policies: https://www.acm.org/publications/policies
