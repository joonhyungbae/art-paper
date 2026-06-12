# Art-Paper Venue Submission Guide

Used by `formatter_agent` and `intake_agent`.

> **art-paper default venue: the SIGGRAPH Asia Art Papers track** (proceedings on the ACM Digital Library; verify the exact category/track against the current CFP). This guide covers art-and-technology venue selection, the acmart submission package, and how to respond to a jury/curatorial decision. Non-ACM art venues (e.g., *Leonardo*, ISEA, a local exhibition catalog) are supported alternates. **Always verify specifics against the current CFP — never fabricate venue details.**

## Pre-Submission Checklist

### 1. Venue selection criteria
- [ ] Track fit: does the venue accept practice-based art papers where the **artwork is the primary contribution** (not a data study)?
- [ ] Format fit: art-paper structure (Pattern 1) vs. art-science hybrid (Pattern 5 / IMRaD) — does the venue expect one?
- [ ] Documentation support: can you submit the work documentation (video, install stills, demo) the venue requires?
- [ ] Exhibition / presentation: some art-paper tracks expect or offer an exhibition slot — check what is required at submission vs. on acceptance
- [ ] Anonymity: is review double-blind? Art papers are hard to anonymize (the work is often identifiable) — check the venue's anonymization expectations
- [ ] Rights: does submission/publication require you to hold or clear copyright and exhibition rights for the work and all reproduced images?
- [ ] Timeline and AI-disclosure policy: review turnaround and the venue's AI-usage disclosure requirements

### 2. Manuscript preparation (acmart default)
- [ ] Use the ACM `acmart` document class with the CFP-verified class option (`sigconf` default; journal-style art venues may use `acmsmall`) — see `latex_template_reference.md` and `shared/references/acm_reference_format.md`
- [ ] Page/length limit within the CFP's stated limit
- [ ] ACM Reference Format for all citations; artwork/exhibition entries use venue+date (`@misc`/`@online`), never fabricated DOIs
- [ ] Work documentation (figures/video) meets the venue's resolution/format requirements; every figure has a caption and an image courtesy/credit line where required
- [ ] Anonymized to the degree the venue requires (note: the work itself may be identifiable)
- [ ] ACM CCS concepts and keywords supplied if the venue requires them
- [ ] PDF compiled from LaTeX (IRON RULE — never HTML-to-PDF)

### 3. Required components

| Component | Usually Required | Notes |
|-----------|:---------------:|-------|
| Title + author/affiliation block | ✓ | acmart metadata; respect anonymization mode |
| Abstract | ✓ | The work, its provocation, how it was made, what its exhibition revealed (check word limit) |
| Keywords + ACM CCS concepts | ✓ | Per acmart / venue requirements |
| Main text | ✓ | Art-paper structure (Pattern 1 default) |
| Work documentation (figures) | ✓ | Stills, install photos, system/process diagrams; high-resolution |
| Supplementary video / demo | Often | Documentation of the work; check format and length limits |
| References | ✓ | ACM Reference Format; artwork entries = venue+date |
| Collaboration / contribution credit | Often | Named roles (concept, code, fabrication, sound, performance) — `credit_authorship_guide.md` |
| Image courtesy / copyright clearance | ✓ | Courtesy lines for all reproduced images; rights cleared |
| Acknowledgments (support) | ✓ | Grants, residencies, commissions, production support — `funding_statement_guide.md` |
| AI-usage disclosure | ✓ (verify CFP) | **Two channels**: AI to MAKE the artwork vs. AI to WRITE the paper — `shared/references/siggraph_acm_disclosure.md` |

## Art-and-Technology Venues

### Primary (art-paper default) and adjacent ACM venues

| Venue | Track | Citation Style | Notes |
|---|---|---|---|
| **SIGGRAPH Asia — Art Papers** | Practice-based art paper | ACM Reference Format | **art-paper default**; ACM Digital Library — verify category/track against current CFP |
| SIGGRAPH — Art Papers / Art Gallery | Practice-based art paper | ACM Reference Format | ACM Digital Library |
| ACM Creativity & Cognition | Practice-based / research-creation | ACM Reference Format | ACM Digital Library |
| ACM TEI (Tangible, Embedded, Embodied) | Art/design + technical | ACM Reference Format | Often has an arts track |
| ACM Multimedia — Art exhibition / Interactive Art | Media art | ACM Reference Format | ACM Digital Library |

### Non-ACM art venues (supported alternates)

| Venue | Form | Citation Style | Notes |
|---|---|---|---|
| *Leonardo* (MIT Press) | Journal | Often house style / author-date | Art-science-technology |
| *Leonardo Music Journal* | Journal | House style | Sound / music art |
| ISEA (Int'l Symposium on Electronic Art) | Conference proceedings | Venue style | Electronic / media art |
| *Digital Creativity* | Journal | Author-date | Practice-led research |
| Ars Electronica / festival catalogs | Catalog / archive | Catalog convention | Exhibition documentation |

> For a non-ACM venue, the ACM default may be overridden to the venue's required style (APA / Chicago / MLA / house style) — see `citation_format_switcher.md`. The default remains ACM.

## Submission Cover / Statement of Contribution

Many art-paper tracks ask for a short statement of the work's **contribution to art-and-technology discourse** rather than a journal-style cover letter. Skeleton:

```markdown
[Date]

[Track Chairs / Jury]
[Venue Name — Art Papers track]

Dear [Chairs],

RE: Submission — "[Work Title]: [Paper Title]"

I am submitting this practice-based art paper for the [Venue] Art Papers track.

**The work:** [1–2 sentences — what the artwork is, medium, where/when shown]

**Its provocation / contribution:** [1–2 sentences — the concept it investigates and
what it adds to art-and-technology discourse, positioned against precedent works]

**Documentation:** [what is included — figures, supplementary video, demo]

**Confirmations:**
- The work and this paper have not been published in this form previously.
- I/we hold or have cleared copyright and exhibition rights for the work and all
  reproduced images (courtesy lines included).
- [If applicable: collaboration credit is stated in the paper.]
- AI usage is disclosed in two channels (artwork-making and paper-writing) per the CFP.

Sincerely,
[Artist / Corresponding Author], [Studio / Institution], [Email], [ORCID]
```

## Collaboration / Contribution Credit

Art papers name **who did what** on the work (concept, code, fabrication, sound, performance) — not the empirical CRediT taxonomy. See `credit_authorship_guide.md` and `credit_statement_template.md`. Describing collaborative work as solo, or omitting named contributors, is an integrity flag.

## Image / Rights Statement

Every reproduced image needs a courtesy/credit line, and the work's copyright and exhibition rights must be held or cleared:

```
Image courtesy of the artist [and Venue]. Photo: [Name].
Installation view, [Exhibition], [Venue], [City], [Date].
```

## AI-Usage Disclosure (two-channel)

Per `shared/references/siggraph_acm_disclosure.md` — disclose separately:

```
AI-Usage Disclosure:
(1) Artwork-making: [which AI systems/models were part of MAKING the work, and how].
(2) Paper-writing: [which AI tools assisted WRITING this paper, and how].
The author(s) reviewed and take full responsibility for all content.
```

Verify the exact required wording and placement against the current CFP.

## Post-Decision: Responding to the Jury / Curatorial Review

### Response letter structure

```markdown
Dear Chairs and Reviewers,

Thank you for the jury's feedback on "[Work Title]: [Paper Title]"
(Submission ID: XXX). We have addressed each point and revised accordingly.

---

## Reviewer 1
**Comment 1**: [Quote]
**Response**: [What we did]
**Changes**: [Specific changes, with section references]

## Reviewer 2
[Same format]

---

We believe the revisions strengthen the paper's articulation of the work's
contribution and hope it is now suitable for the program.

Sincerely,
[Author(s)]
```

### Response best practices
1. Respond to EVERY comment (even where you disagree)
2. Be respectful; engage the curatorial/practitioner perspective on its own terms
3. If you disagree, explain why with reference to the work and its lineage
4. Reference specific sections for changes
5. Provide both a clean and a tracked-changes copy if requested
6. Distinguish revisions to the **paper** from any changes to the **work** itself
