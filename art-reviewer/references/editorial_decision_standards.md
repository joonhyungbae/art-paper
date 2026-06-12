# Editorial Decision Standards — Criteria for Editorial Decision Making

This document defines the explicit criteria for Accept / Minor Revision / Major Revision / Reject decisions, for use by `eic_agent` (Jury Chair) and `editorial_synthesizer_agent`. Decisions are judged against the art-research evidence model (`shared/references/art_research_evidence_model.md`); the dimensions are the five art-paper criteria in `review_criteria_framework.md`. The four reviewers are the Jury Chair + R1 Practitioner + R2 Curator + R3 Critic (DA handled separately).

> **Venue caveat:** verify revision timelines and the program's actual decision process against the current Call for Art Papers; the timeframes below are defaults.

---

## 1. Decision Categories

### Accept

**Definition**: The paper can be published without further review.

**Criteria**:
- Average score across all core dimensions >= 4.0
- No dimension scores below 3.0
- At least 3/4 reviewers recommend Accept or Minor Revision
- No unresolved major artistic or conceptual issues

**Conditions**:
- May include minor copyediting suggestions
- May require final formatting adjustments
- Does not need to be sent for review again

**Typical scenarios**:
- Paper has undergone multiple revision rounds, all issues resolved
- Rare first-pass acceptance (verify the program's selectivity against the current CFP)

---

### Minor Revision

**Definition**: The paper is fundamentally acceptable and can be published after limited modifications; typically does not need to be sent for review again after revision.

**Criteria**:
- Average score across all core dimensions >= 3.5
- No dimension scores below 2.5
- At least 3/4 reviewers recommend Accept or Minor Revision
- Issues can be resolved within 2-4 weeks
- Modifications do not involve restructuring the core concept or the work

**Typical revision items**:
- Supplementing a small number of precedent works / references
- Clarifying realization or process detail
- Articulating the concept more clearly
- Correcting citation format (ACM Reference Format)
- Adding discussion of limitations
- Adjusting wording to avoid over-claiming (reception inflation, autonomy/precedence over-claims)

**Response requirements**:
- Authors must respond to reviewer comments item by item
- After revision, reviewed by the Jury Chair (usually not sent for external review again)
- Revision deadline: 2-4 weeks

---

### Major Revision

**Definition**: The paper has potential but has significant issues, requiring substantial revision followed by re-review.

**Criteria**:
- Core dimension average score between 2.5-3.4
- Some dimensions may score below 2.5 (but not fatal)
- At least 2/4 reviewers recommend Major Revision or better
- Issues are serious but fixable (not fundamental design flaws)
- Revision requires 6-8 weeks of work

**Typical revision items**:
- Re-framing the concept (articulating the load-bearing idea)
- Substantially reworking the conceptual lineage / positioning (missing key precedents)
- Supplementing additional documentation (stills, video, process record, install photos)
- Reorganizing paper structure (selecting the right art-paper pattern)
- Anchoring over-claimed technical/material claims, or hedging them
- Strengthening the conceptual framing's application to the work
- Down-scoping inflated reception or precedence claims to what is documented

**Response requirements**:
- Authors must write a detailed point-by-point response letter
- After revision, sent for re-review (may go back to original reviewers or new reviewers)
- Revision deadline: 6-8 weeks
- Typically a maximum of 2 rounds of Major Revision allowed

---

### Reject

**Definition**: The work is not suitable for this program, even with revision.

**Criteria (meeting any one may trigger Reject consideration)**:
- Core dimension average score < 2.5
- Any core dimension (Conceptual Contribution, Documentation Rigor) = 1 — e.g., no load-bearing concept, or central claims that cannot be anchored
- At least 3/4 reviewers recommend Reject
- Fundamental unfixable issues exist

**Reject subtypes**:

| Subtype | Description | Suggestion |
|---------|-------------|-----------|
| **Reject — Out of Scope** | Work not within the program's character | Recommend more suitable venues / programs |
| **Reject — No Concept** | The work has only theme and technique, no articulated concept | Suggest how to find/state the concept |
| **Reject — Un-anchorable Claims** | Central claims (autonomy, reception, precedence) that cannot be anchored | Suggest what would need to be documented |
| **Reject — Premature** | Work/paper not yet mature enough | Suggest specific improvement directions |
| **Reject — Resubmit Encouraged** | Has potential but needs fundamental restructuring | Provide detailed restructuring suggestions |

**Even with Reject, must**:
- Affirm the work's merits
- Provide specific improvement suggestions
- Recommend more suitable venues / programs (if it's a fit issue)
- Maintain professional, respectful tone

---

## 2. Decision Matrix

### Decision Matrix Based on Reviewer Recommendations

| Chair | R1 | R2 | R3 | -> Recommended Decision |
|-------|----|----|-----|----------------------|
| Accept | Accept | Accept | Accept | **Accept** |
| Accept | Accept | Accept | Minor | **Accept** (with suggestions) |
| Accept | Accept | Minor | Minor | **Minor Revision** |
| Accept | Minor | Minor | Minor | **Minor Revision** |
| Minor | Minor | Minor | Minor | **Minor Revision** |
| Minor | Minor | Minor | Major | **Minor-to-Major** (depends on specific issues) |
| Minor | Minor | Major | Major | **Major Revision** |
| Minor | Major | Major | Major | **Major Revision** |
| Major | Major | Major | Major | **Major Revision** |
| Major | Major | Major | Reject | **Major Revision** (last chance) |
| Major | Major | Reject | Reject | **Reject** (resubmit encouraged) |
| Major | Reject | Reject | Reject | **Reject** |
| Reject | Reject | Reject | Reject | **Reject** |

### Special Situation Handling

**Split Decision (evenly divided)**:
- Example: Accept + Accept + Reject + Reject
- The Jury Chair (or synthesizer) needs to deeply analyze the cause of disagreement
- Lean toward conservative strategy: Major Revision, requiring the artist to respond to the Reject side's comments
- May consider inviting an additional juror

**One Outlier (one unusual opinion)**:
- Example: Minor + Minor + Minor + Reject
- Carefully examine the Reject rationale
- If the rationale is valid and others missed it, escalate to Major Revision
- If the rationale is insufficient, maintain Minor Revision but mention the opinion in the Decision Letter

---

## 3. Decision Confidence Calibration

### Impact of Reviewer Confidence Score

| Confidence | Impact on Decision |
|-----------|-------------------|
| 5 (Very High) | This reviewer's opinion carries the highest weight |
| 4 (High) | Standard weight |
| 3 (Medium) | Standard weight, but reduced in case of disagreement |
| 2 (Low) | For reference only, not used as a decisive opinion |
| 1 (Very Low) | Ignore this reviewer's recommendation (but retain specific comments) |

### Cross-Dimension Severity Assessment

| Situation | Severity | Handling |
|-----------|----------|---------|
| No load-bearing concept / un-anchorable core claim (R1 or Conceptual score = 1) | Critical | Even if other dimensions are excellent, lean toward Reject |
| Major conceptual-lineage / precedent omission (R2 score = 2) | Serious | Major Revision, require supplementation |
| Cultural/ethical stakes overlooked (R3 score = 2) | Moderate | Minor/Major, depends on other dimensions |
| Poor writing quality (score = 2) | Minor | Does not affect the artistic decision, but require language revision |

---

## 4. Revision Round Policy

### Standard Policy

| Round | Expectation | Handling |
|-------|-------------|---------|
| R1 (First revision) | Respond to all reviewer comments | Send for re-review or Jury Chair review |
| R2 (Second revision) | Respond to residual issues | Usually the Jury Chair makes final decision |
| R3 (Third revision) | Very rare, usually only handling formatting | the Jury Chair makes final decision |

### Upgrade/Downgrade Rules

- Minor Revision with incomplete revisions -> May escalate to Major Revision
- Major Revision with excellent revisions -> May downgrade to Minor Revision or Accept
- Major Revision with insufficient revisions -> May Reject (infinite revision cycles are not encouraged)
- Beyond 2 rounds of Major Revision -> Strongly recommend Accept or Reject, no further extension

---

## 5. Professional Ethics of Editorial Review

### Reviewer Ethics

1. **Confidentiality**: The review process and paper content are confidential
2. **Conflict of interest**: Recuse if there is a collaborative or competitive relationship with the author
3. **Timeliness**: Complete the review within the committed timeframe
4. **Constructiveness**: Even when recommending Reject, provide constructive feedback
5. **Impartiality**: No bias based on author's gender, race, institution, or nationality
6. **No plagiarism**: Do not use unpublished concepts or works seen during review
7. **Appropriate language**: Avoid personal attacks, sarcasm, or demeaning language

### Editor Ethics

1. **Fair decision**: Based on artistic and conceptual quality, not influenced by external pressure
2. **Transparent process**: Decision letter must clearly explain the rationale
3. **Reasonable deadlines**: Give authors sufficient revision time
4. **Appeal channel**: Authors have the right to respond to or challenge review comments
5. **Consistent standards**: Papers of similar quality should receive similar decisions

### Ethical Considerations for Special Situations

| Situation | Ethical Handling |
|-----------|-----------------|
| Artist is your student/collaborator | Must recuse or disclose the relationship |
| The work's provocation is contrary to your taste | Evaluate how well the work makes its case, not whether you endorse it |
| Work cites your own work/theory but misreads it | May point it out but cannot require citation of your own work |
| Suspected fabricated artwork / exhibition / capability claim | Report to the Jury Chair; the program initiates its verification procedure (mirrors the integrity-gate artwork & realization claim flags) |
| Work is close to your own ongoing practice | Disclose potential conflict of interest |
