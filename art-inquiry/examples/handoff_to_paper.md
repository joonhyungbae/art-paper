# Handoff Example: art-inquiry → art-paper

This example demonstrates how art-inquiry full mode, after completing the inquiry, hands off to art-paper to begin art-paper writing.

---

## Scenario Setup

The user has completed art-inquiry full mode on the work "Drift Lexicon: A Generative Installation that Composes a Living Language from Visitors' Discarded Words." Below is a summary of the inquiry outputs.

---

## art-inquiry Output Summary

### 1. Concept & Provocation Brief (from research_question_agent)

```markdown
### Core Provocation
What happens to language when an autonomous system continuously composes a
living vocabulary out of the words visitors choose to discard — can a machine
make a language that belongs to a crowd but to no one in particular?

### FINER Assessment (practice-based)
| Criterion   | Score | Justification |
|-------------|-------|---------------|
| Feasible    | 4/5   | Artist has prior generative-text practice; gallery sited |
| Interesting | 5/5   | Live intersection of language, authorship, and collective making |
| Novel       | 4/5   | Few works treat discarded language as generative material |
| Ethical     | 5/5   | Ephemeral, anonymous contributions; no stored personal data |
| Relevant    | 5/5   | Positions the work for an Art Papers submission |
| **Average** | **4.6/5** | |

### Sub-questions (provocation refinements)
1. How does the work differ from prior generative-text and participatory-language art?
2. What theory (collective authorship, the commons, glossolalia) best positions it?
3. How should the emergent "language" and its reception be documented honestly?
```

### 2. Practice-Based Methodology Blueprint (from research_architect_agent)

```markdown
- Inquiry stance: Practice-based (insight emerges through making + installation)
- Method: Iterative build + situated installation with observation
- Evidence strategy (triangulation; see art_research_evidence_model.md):
  - The work as encountered (the live, composing vocabulary)
  - Process & realization (system description, version history, rejected designs)
  - Exhibition & reception (venue/date + observed detail; no asserted emotion)
  - Conceptual lineage (precedent works + theory)
  - Situated reflection (what the making revealed)
- Analytical framing: collective authorship + the linguistic commons
- Rigor: each claim anchored to an evidence type; precedence/technical claims hedged or evidenced
```

### 3. Annotated Bibliography (from bibliography_agent)

```markdown
27 sources identified, 19 retained after screening:
- 8 precedent artworks (venue/date locators; generative-text + participatory-language art)
- 6 theory/criticism sources (collective authorship, the commons, language games)
- 3 art papers from SIGGRAPH/SA Art Papers + Leonardo (ACM Reference Format)
- 2 artist statements / catalogue essays

Lineage themes identified:
- Discarded/found language as material (under-occupied position)
- Collective vs distributed vs relinquished authorship
- The "language that belongs to no one" — commons framing
```

### 4. Synthesis Report (from synthesis_agent)

```markdown
## Core Findings (positioning)

1. **An under-occupied position in the lineage**:
   - Generative-text art usually authors a corpus; participatory-language art usually
     collects contributions. This work does both *and* discards — the contribution is
     treating refusal/discarding as the generative act.

2. **Authorship sits at "collective-but-anonymous"** (converging across precedents):
   - The composed language belongs to the crowd, not to named contributors or to the artist
   - This position is theorized by the commons literature but rarely realized in text art

3. **Key tension**: legibility vs strangeness
   - If the emergent language is too legible it reads as a word-cloud; too strange and it
     reads as noise. The work lives in the threshold.

4. **Documentation gap in the lineage**:
   - Reception of generative-language art is rarely documented with observable anchors

## Contradictions Identified
- Some catalogue essays call such systems "autonomous" while the documented realization
  shows heavy curation → autonomy claim must be hedged or evidenced

## Discourse Gaps
- Little prior work foregrounds *discarding* as the generative gesture
- Non-Western generative-language lineage under-documented
```

---

## Handoff Instruction

After completing art-inquiry, the user inputs:

```
Now help me write an art paper based on this inquiry
```

---

## art-paper intake_agent Auto-Detection

**intake_agent Detection Process**:

```
Scanning available materials...

[DETECTED] Concept & Provocation Brief
  - Source: art-inquiry / research_question_agent
  - Status: Complete (FINER 4.6/5)
  - Action: SKIP art-paper Phase 1 (concept scoping)

[DETECTED] Practice-Based Methodology Blueprint
  - Source: art-inquiry / research_architect_agent
  - Status: Complete (iterative build + situated installation)
  - Action: SKIP art-paper Phase 2 (methodology design)
  - Note: Will integrate into Realization / Methods of Making section directly

[DETECTED] Annotated Bibliography (19 sources, ACM Reference Format)
  - Source: art-inquiry / bibliography_agent
  - Status: Complete, quality-screened
  - Action: SKIP art-paper precedent-works search
  - Note: Will use as foundation for the Conceptual Framework section

[DETECTED] Synthesis Report
  - Source: art-inquiry / synthesis_agent
  - Status: Complete (4 positioning findings + 1 contradiction + 2 gaps)
  - Action: SKIP art-paper analysis phase
  - Note: Will structure The Work / Reflection sections around the synthesis

Materials Assessment: COMPREHENSIVE
Recommended art-paper mode: full (with accelerated pipeline)
Estimated sections already covered: 60-70%
Remaining work: Writing, documentation, ACM formatting, argumentation, and polish
```

---

## Skipped Steps and Reasons

| art-paper Step | Normal Workflow | After Handoff | Reason |
|---------------------|---------|-----------|------|
| Phase 1: Concept Scoping | intake_agent clarifies from scratch | SKIPPED | Provocation Brief is complete |
| Phase 2: Structure Planning | structure_architect_agent designs structure | PARTIAL | Has Blueprint but needs mapping to the Practice-Based Art Paper structure (Pattern 1) |
| Phase 3: Precedent-Works Search | literature_agent searches | SKIPPED | Bibliography is complete |
| Phase 4: Conceptual Framework Writing | framework_writer_agent writes | ACTIVE | Has Synthesis but needs conversion to paper tone |
| Phase 5: Realization Writing | realization_writer_agent writes | ACTIVE | Has Blueprint but needs expansion to full paragraphs + system description |
| Phase 6: The Work Writing | work_writer_agent writes | ACTIVE | Has Synthesis but needs description + experience + authorship/credit |
| Phase 7: Reflection / Discussion Writing | discussion_writer_agent writes | ACTIVE | Needs situated insight + exhibition/reception with observable anchors |
| Phase 8: Intro + Conclusion | bookend_agent writes | ACTIVE | Needs to be written based on full text |
| Phase 9: Abstract + ACM Formatting | format_agent processes | ACTIVE | Needs full text completion first |
| Phase 10: Self-Review | review_agent reviews | ACTIVE | Must be executed |

---

## Post-Handoff art-paper Actual Workflow

```
=== art-paper: Accelerated Pipeline ===

Step 1: STRUCTURAL MAPPING
  [structure_architect_agent]
  - Input: Provocation Brief + Methodology Blueprint + Synthesis Report
  - Output: Complete paper outline (Practice-Based Art Paper, Pattern 1), each section
    tagged with corresponding art-inquiry materials
  - Output example:

    I. Introduction / Context
       - The work in one paragraph (from Synthesis)
       - Artistic & conceptual context (precedent works from Bibliography)
       - The provocation [directly cite Provocation Brief]
       - Contribution statement (discarding as the generative act)

    II. Conceptual Framework
       - 2.1 Collective authorship + the commons (from Blueprint + theory)
       - 2.2 Positioning against precedent works (from Bibliography themes)
       - 2.3 Key concepts (the "language that belongs to no one")

    III. The Work
       - 3.1 Description: form, media, the live composing vocabulary
       - 3.2 Experience: what the visitor does (discards words)
       - 3.3 Authorship & collaboration (crowd / system / artist; credit)

    IV. Realization / Methods of Making
       - 4.1 System + generative-text approach (from Blueprint)
       - 4.2 Process, iteration, rejected designs
       - 4.3 Tools and dependencies

    V. Reflection / Discussion
       - 5.1 What the making revealed (from Synthesis)
       - 5.2 Exhibition & reception (venue/date + observed detail)
       - 5.3 The legibility-vs-strangeness tension
       - 5.4 Limitations and open questions (from Synthesis gaps)

    VI. Conclusion / Future Work

Step 2: SECTION WRITING (Parallel)
  [framework_writer_agent] → Conceptual Framework
    - Based on Annotated Bibliography and Synthesis, position the work against precedent
      works and theory — positioning, not a literature ranking

  [realization_writer_agent] → Realization / Methods of Making
    - Expand the Blueprint into a legible system + process description
    - Include rejected designs and pivots (the making as evidence)

  [work_writer_agent] → The Work
    - Describe form, experience, and authorship; name collaborators and credit the crowd's role
    - Address the autonomy claim flagged in the Synthesis (hedge or evidence)

Step 3: REFLECTION + BOOKENDS
  [discussion_writer_agent] → Reflection / Discussion
    - Situated insight: what making the work revealed
    - Exhibition & reception anchored to venue/date + observable detail (no asserted emotion)
    - Integrates Synthesis discourse gaps as future work

  [bookend_agent] → Introduction + Conclusion
    - Introduction: the work, its context, the provocation, the contribution
    - Conclusion: no new claims; echoes the provocation and looks ahead

Step 4: ABSTRACT + FORMAT
  [format_agent]
    - Abstract: 120-200 words (art-paper target)
    - acmart LaTeX formatting (default class option sigconf)
    - Reference list in ACM Reference Format (precedent works use venue/date locators; no fabricated DOIs)
    - Two-channel AI-usage disclosure (AI in making vs AI in writing)

Step 5: SELF-REVIEW
  [review_agent]
    - Internal consistency check (Provocation → Framework → Work → Realization → Reflection)
    - Evidence anchoring (every claim anchored to an evidence type)
    - Integrity check (precedence / technical / reception / attribution claims)
    - ACM format compliance
    - Verdict: Ready for submission / Needs revision
```

---

## User-Facing Handoff Experience

**art-paper's Opening Message**:

> I've read your complete outputs from the art-inquiry stage, including:
> - Concept & Provocation Brief (FINER 4.6/5)
> - Practice-Based Methodology Blueprint (iterative build + situated installation)
> - Annotated Bibliography (19 quality-screened sources, ACM Reference Format)
> - Synthesis Report (4 positioning findings + 2 discourse gaps)
>
> Based on these materials, I've completed a preliminary plan for the paper outline, using the Practice-Based Art Paper structure (Pattern 1). Here is the planned structure:
> [Display outline]
>
> I have two questions that need your confirmation:
> 1. What is your target venue? (SIGGRAPH Asia Art Papers, or another — this affects length, anonymization, and formatting; verify against the current CFP)
> 2. Should I assume the default acmart output (sigconf), or do you need a different template?
>
> Once confirmed, I'll begin writing. Because the inquiry foundation is already comprehensive, I can skip the early exploration stages and proceed directly to paper writing.

---

## Notes

1. **Not copy-paste**: art-paper does not directly copy art-inquiry outputs, but transforms them into the tone and ACM format of an art paper
2. **May discover new issues**: During writing, art-paper agents may discover points missed by art-inquiry (e.g. an unhedged autonomy claim) and will proactively flag them
3. **Still requires user confirmation**: Target venue, template, and specific documentation/figure requirements still require user input
4. **Review recommendation auto-connects**: After paper completion, the user can continue with `art-reviewer` for the SIGGRAPH Asia Art Papers jury review
```
