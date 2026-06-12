# Revision Response Template

This template helps authors systematically respond to all review comments. The format follows Reviewer Comment → Author Response → Changes Made (R→A→C format).

---

## Instructions

1. Every reviewer comment must receive a response; none may be skipped
2. If you disagree with a comment, you must explain your reasoning (not simply "disagree")
3. Change tracking: Mark all changes in the revised manuscript using tracked changes or color highlighting
4. Page cross-reference: Provide page number cross-references between the original and revised manuscripts

---

## Template

```markdown
# Response to Reviewer Comments

## Manuscript Information
- **Title**: [Paper title]
- **Manuscript ID**: [Manuscript number]
- **Original Submission Date**: [Original submission date]
- **Revision Submission Date**: [Revised manuscript submission date]
- **Review Round**: [Round N revision]

---

## Summary of Changes

[300-500 words summarizing the major changes made in this revision]

### Major Changes
1. [Major change 1 — brief description]
2. [Major change 2]
3. [...]

### Structural Changes
- [Section reorganization/additions/deletions]
- [Word count change: original X words → revised Y words]

### New Content
- [Newly added analyses/data/references]

---

## Response to Jury Chair (EIC)

### Editor Comment 1
> [Direct quote of the EIC's comment]

**Author Response**: [Response]

**Changes Made**: [Specific changes made, indicating revised manuscript page X, paragraph Y]

---

### Editor Comment 2
> [Direct quote]

**Author Response**: [Response]

**Changes Made**: [Specific changes]

---

[Repeat the above format for each EIC comment]

---

## Response to Reviewer 1 (Practitioner-Researcher)

### Strengths Acknowledged
We thank Reviewer 1 for acknowledging the following aspects:
1. [Quote Reviewer 1's positive comments]
2. [...]

### R1-W1: [Weakness title]
> [Direct quote of Reviewer 1's weakness description]

**Author Response**:
[Detailed response, which may include:]
- We agree / partially agree with the Reviewer's point
- Specific changes made to address this issue
- If disagreeing, provide rationale and evidence

**Changes Made**:
- [Revised manuscript page X, paragraph Y: specific text changes]
- [Newly added analyses/tables/figures: description]
- [Or: We maintain the original text for the following reasons...]

---

### R1-W2: [Weakness title]
> [Direct quote]

**Author Response**: [Response]

**Changes Made**: [Specific changes]

---

### R1-W3: [Weakness title]
> [Direct quote]

**Author Response**: [Response]

**Changes Made**: [Specific changes]

---

### R1 Questions

#### R1-Q1
> [Direct quote of Reviewer 1's question]

**Author Response**: [Answer]

**Changes Made**: [If applicable, indicate change location]

---

#### R1-Q2
> [Direct quote]

**Author Response**: [Answer]

**Changes Made**: [If applicable]

---

### R1 Minor Issues

| # | Reviewer Comment | Action Taken | Location |
|---|-----------------|--------------|----------|
| 1 | [Minor issue description] | [Correction/explanation] | p.X, para.Y |
| 2 | [Minor issue description] | [Correction/explanation] | p.X, para.Y |
...

---

## Response to Reviewer 2 (Curator)

[Same format as above: Strengths Acknowledged → W1-W5 → Questions → Minor Issues]

---

## Response to Reviewer 3 (Art-Science / Media-Art Critic)

[Same format as above: Strengths Acknowledged → W1-W5 → Questions → Minor Issues]

---

## Response to Required Revisions

[Respond to each Required Revision from the Editorial Decision one by one]

| # | Required Revision | Status | Response Summary | Location |
|---|------------------|--------|-----------------|----------|
| R1 | [Description] | Completed / Partially Addressed | [Summary] | p.X-Y |
| R2 | [Description] | Completed / Partially Addressed | [Summary] | p.X-Y |
| R3 | [Description] | Completed / Partially Addressed | [Summary] | p.X-Y |
...

---

## Response to Suggested Revisions

| # | Suggested Revision | Status | Response Summary |
|---|-------------------|--------|-----------------|
| S1 | [Description] | Adopted / Not Adopted (reason) | [Summary] |
| S2 | [Description] | Adopted / Not Adopted (reason) | [Summary] |
...

---

## Change Log

### Page-by-Page Changes

| Page (Original) | Page (Revised) | Section | Change Description |
|-----------------|---------------|---------|-------------------|
| p.3 | p.3-4 | Concept / Provocation | Added paragraph defining the load-bearing concept |
| p.7-8 | p.8-9 | Realization | Anchored the "real-time" claim with update-latency detail |
| p.12 | p.13 | Documentation | Added Fig. 4 (signal-flow diagram) |
| — | p.16-17 | Reflection | Added representational-ethics subsection; anchored reception claim |
| p.20-22 | p.23-25 | References | Added 6 precedent works in ACM Reference Format (venue+date locators) |

### Word Count Change
- **Original**: [X] words
- **Revised**: [Y] words
- **Net Change**: [+/- Z] words

---

## Closing Statement

We sincerely appreciate the jury's thoughtful and constructive feedback, which has significantly improved the paper and the framing of the work. We believe the revised version addresses all the concerns raised, and we hope it now meets the standards of [venue / program name — verify against current CFP].

[If any items were not fully addressed, explain the reasons and future plans here]
```

---

## Quality Standards for Responses

### Characteristics of Good Responses

1. **Direct**: Does not evade issues; addresses every comment head-on
2. **Specific**: Points to the exact location and content of changes
3. **Evidence-based**: If disagreeing with a reviewer, anchors the rebuttal in the work, its documentation, or cited precedent (ACM Reference Format)
4. **Courteous**: Thanks the reviewer for feedback, even when disagreeing
5. **Complete**: No reviewer comment is left unaddressed

### Characteristics of Poor Responses

1. **Perfunctory**: "Changed" (but does not say what was changed)
2. **Evasive**: Avoids answering difficult questions
3. **Defensive**: "The Reviewer misunderstood my paper" (but does not explain why)
4. **Over-promising**: Acknowledges all problems but provides no solutions
5. **Missing markers**: Changes were made but locations are not indicated, making it impossible for reviewers to find them

### The Correct Way to Disagree with a Reviewer

```markdown
# Correct approach
> Reviewer: Suggest reframing the work as interactive rather than calling it "autonomous"

**Author Response**: We appreciate the Reviewer's point about precision. Our reasons for retaining "autonomous" (in the specific sense defined in glossary §3) are as follows:
1. The system makes unsupervised generative decisions at runtime with no human input during exhibition, which we now document explicitly.
2. We agree the original text conflated "autonomous" with "interactive"; we have separated the two claims.
3. We have anchored the autonomy claim in the revised system account so a reader can judge it.

**Changes Made**: Anchored the autonomy claim with the decision-loop description in the Realization section (p.9, para.3) and added the signal-flow diagram (Fig. 4); clarified the autonomous-vs-interactive distinction (p.7).

# Incorrect approach
> Reviewer: Suggest using Method X instead of Method Y

**Author Response**: We disagree. Method Y is appropriate.
```
