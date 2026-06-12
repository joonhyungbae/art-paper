# Peer Review Report Template

This template is used by all jury agents (Jury Chair, Reviewers 1-3). Each reviewer uses the same structure but fills in review content from their respective perspectives. The artwork is the **primary evidence** — comments anchor to the work, its documentation, and its claims, not to statistical results.

> The Devil's Advocate uses a dedicated format (see `agents/devils_advocate_reviewer_agent.md`), not this template.

---

## Usage Instructions

1. Text in `[brackets]` is explanatory and needs to be replaced with actual content
2. Each reviewer must fully complete all required fields (items marked with *)
3. Detailed Comments are section-by-section commentary; only comment on sections relevant to your review focus
4. Reports are produced in English (art-paper v0.1 default; the paper itself is English-only at v0.1)

---

## Template

```markdown
# Peer Review Report

## Manuscript Information
- **Title**: [Paper title]
- **Manuscript ID**: [If available, enter manuscript ID]
- **Review Date**: [Review date]
- **Review Round**: [Round N review]

---

## Reviewer Information

### Reviewer Role *
[Jury Chair / Reviewer 1 (Practitioner-Researcher) / Reviewer 2 (Curator) / Reviewer 3 (Art-Science / Media-Art Critic)]

### Reviewer Identity *
[Identity description configured by field_analyst_agent]

### Review Focus *
[Core focus of this review, 2-3 sentences]

---

## Overall Assessment *

### Recommendation *
[Select one]
- [ ] **Accept** — Can be published directly, only minor formatting changes needed
- [ ] **Minor Revision** — Minor revisions needed, no re-review after revision
- [ ] **Major Revision** — Substantial revisions needed, re-review required after revision
- [ ] **Reject** — Not suitable for the program / venue

### Confidence Score *
[1-5]
| Score | Meaning |
|-------|---------|
| 5 | Completely within my area of expertise, I am very confident in my assessment |
| 4 | Mostly within my area of expertise, high confidence |
| 3 | Partially within my area of expertise, moderate confidence |
| 2 | Some aspects outside my expertise, somewhat uncertain about my assessment |
| 1 | Mostly outside my expertise, my opinion is for reference only |

### Summary Assessment *
[150-250 word overall assessment]

Requirements:
- Sentences 1-2: What the work and paper do (the work, its concept/provocation, its realization)
- Sentences 3-4: Overall quality assessment (from your review focus perspective)
- Sentences 5-6: Most critical strengths and weaknesses
- Final: Your recommendation rationale

---

## Strengths *

List 3-5 strengths of the paper. Each must:
- Have a specific title
- Cite passages, documentation (figures/video/diagrams/code), or section locations from the paper
- Explain why it is a strength

### S1: [Strength title] *
[Specific description. E.g., "The making is documented as research: the signal-flow diagram and pseudocode (Fig. X) make the 'real-time generative' claim plausible and, in principle, legible to another practitioner..."]

### S2: [Strength title] *
[Specific description]

### S3: [Strength title] *
[Specific description]

### S4: [Strength title]
[Optional]

### S5: [Strength title]
[Optional]

---

## Weaknesses *

List 3-5 weaknesses of the paper. Each must:
- Have a specific title
- Describe the specific problem
- Explain why it is a problem
- Provide specific improvement suggestions

### W1: [Weakness title] *
**Problem**: [Specific description of the problem, citing paper passages]
**Why it matters**: [Explain the impact of this problem]
**Suggestion**: [Specific improvement direction]
**Severity**: [Critical / Major / Minor]

### W2: [Weakness title] *
**Problem**: [...]
**Why it matters**: [...]
**Suggestion**: [...]
**Severity**: [Critical / Major / Minor]

### W3: [Weakness title] *
**Problem**: [...]
**Why it matters**: [...]
**Suggestion**: [...]
**Severity**: [Critical / Major / Minor]

### W4: [Weakness title]
[Optional, same format as above]

### W5: [Weakness title]
[Optional, same format as above]

---

## Detailed Comments *

Section-by-section commentary on the paper. Only comment on sections relevant to your review focus.

> Section labels follow the art-paper structure patterns (`shared/references/art_paper_structure_patterns.md`); the default is the Practice-Based Art Paper. For an art-science hybrid (Pattern 5) or critical/theoretical essay (Pattern 3), adapt labels accordingly. Comment only on sections relevant to your review focus.

### Title & Abstract
- [Does the title/abstract foreground the concept/contribution, not just theme + technique?]
- [Is the abstract structure and completeness adequate?]

### Concept / Provocation
- [Is the work's question or provocation clear?]
- [Is there a load-bearing concept, or only theme + technique? (glossary §7)]
- [Is the contribution to the art+tech discourse stated?]

### Conceptual Lineage / Positioning
- [Conceptual-lineage coverage; precedent works] (Primarily reviewed by Reviewer 2 — Curator)
- [Novelty / precedence claims — accurate and citable?] (Primarily reviewed by Reviewer 2 — Curator)
- [Gap / departure from precedent articulated?]

### Realization / Making-as-Research
- [Realization rigor — technical/material approach plausible and legible?] (Primarily reviewed by Reviewer 1 — Practitioner-Researcher)
- [Process integrity — iteration / failures / pivots documented as research?]
- [Technical/material claim anchoring — "real-time" / "generative" / "autonomous" anchored or asserted?]
- [Authorship / collaboration credit named where the work is collaborative?]

### Documentation (the work as primary evidence)
- [Is the work documented completely enough to evaluate (stills, video, diagrams, code, install photos)?]
- [Figure / media legibility; image credits / courtesy lines present?]
- [Do reflection or reception claims extend beyond what the documentation supports?]

### Reflection / Discussion
- [Does the reflection address the work's concept/provocation?]
- [Cultural / ethical / representational implications engaged?]
- [Reception claims anchored to a named venue/date + observable detail (no reception inflation)?]
- [Honest situated framing vs. over-generalized claims?]

### Conclusion
- [Whether claims over-reach beyond what the work demonstrates]
- [Value of stated future directions for the practice]

### References (ACM Reference Format)
- [ACM Reference Format compliance; locator anchor after each citation (L3 gate)]
- [Artwork/exhibition citations use venue+date as locator — no fabricated DOIs]
- [Quality and relevance of cited precedent works and theory]

---

## Questions for Authors *

List 2-4 questions requiring author response. These questions should:
- Not be rhetorical, but genuinely need answering
- The answer could change the paper's quality or direction
- Be specific and answerable

1. [Question 1]
2. [Question 2]
3. [Question 3] (Optional)
4. [Question 4] (Optional)

---

## Minor Issues

List minor issues that don't affect academic quality but need correction.

### Language / Grammar
- [Page X, Line Y: Specific language issue]
- [...]

### Citation Format
- [Specific citation format issues]
- [...]

### Figures and Tables
- [Figure/table improvement suggestions]
- [...]

### Layout
- [Layout issues]
- [...]

---

## Dimension Scores *

Score each dimension 0-100 using the rubrics in `references/quality_rubrics.md`. Report the range descriptor that best matches.

| Dimension | Score (0-100) | Descriptor | Notes |
|-----------|--------------|------------|-------|
| Artistic Merit & Significance (25%) | | [Exceptional/Strong/Adequate/Weak/Insufficient] | Chair / all |
| Conceptual Contribution (25%) | | [Exceptional/Strong/Adequate/Weak/Insufficient] | R2 Curator focus |
| Documentation Rigor (20%) | | [Exceptional/Strong/Adequate/Weak/Insufficient] | R1 Practitioner focus |
| Technical / Material Realization (15%) | | [Exceptional/Strong/Adequate/Weak/Insufficient] | R1 Practitioner focus |
| Contribution to Discourse (15%) | | [Exceptional/Strong/Adequate/Weak/Insufficient] | R2 / R3 focus |
| **Weighted Average** | | **[Accept/Minor/Major/Reject]** | |
```

---

## Format Guidelines

### Severity Levels

| Level | Definition | Revision Requirement |
|-------|-----------|---------------------|
| **Critical** | Cannot be accepted without fixing | Required Revision |
| **Major** | Significantly affects paper quality | Strongly Recommended |
| **Minor** | Better if fixed, acceptable if not | Suggested |

### How to Cite Paper Passages

```
# Correct
"The author states on p. 12: 'the system autonomously composes,' but the signal-flow diagram (Fig. 3) shows a fixed mapping with no decision step — 'autonomous' is not anchored..."

# Correct
"The reception claim on p. 9 ('visitors were deeply moved') has no observable anchor — no named venue/date or recorded response..."

# Incorrect (too vague)
"The realization has problems"
"Precedent positioning is not comprehensive enough"
```

### Constructive Tone Examples

```
# Good
"The author is encouraged to consider adding X analysis to strengthen the argument for Y."

# Good
"This section's argument could be clearer. Specifically, the 'real-time' claim in paragraph 2, page 8 could be anchored by describing the system's update latency."

# Bad
"The artist clearly does not understand X."

# Bad
"This realization is wrong."
```
