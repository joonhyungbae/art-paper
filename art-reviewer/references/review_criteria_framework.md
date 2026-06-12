# Review Criteria Framework — Structured Review Criteria for Art Papers

This document defines the review criteria for **practice-based art-research papers** (SIGGRAPH Asia Art Papers track → ACM Digital Library) and pattern-specific criteria differentiated by mode of inquiry. All reviewer agents share this framework.

> **Genre note:** these criteria replace the empirical review dimensions (methodological rigor, statistical reporting, evidence sufficiency-by-source-count) used upstream. They are judged against the **art-research evidence model** (`shared/references/art_research_evidence_model.md`) — *the artwork is the primary evidence*, not statistical rigor. Do not import an evidence *ranking* or a "more citations = more rigor" assumption.

> **Venue caveat:** SIGGRAPH Asia Art Papers requirements drift year to year. Treat any venue-specific expectation as a default and **verify against the current Call for Art Papers**.

---

## 1. Core Review Dimensions

Five core dimensions applicable to all art-paper types. (Weights are defaults; the sprint contract may override.)

### Dimension 1: Artistic Merit & Significance — Weight 25%

| Level | Score | Description |
|-------|-------|-------------|
| Outstanding | 5 | A significant, resonant work that meaningfully advances the art-and-technology discourse |
| Strong | 4 | A clearly significant work with a distinct artistic voice |
| Adequate | 3 | A competent work of modest significance |
| Weak | 2 | Significance unclear; the work does not register beyond its own description |
| None | 1 | No discernible artistic significance |

### Dimension 2: Conceptual Contribution — Weight 25%

| Level | Score | Description |
|-------|-------|-------------|
| Outstanding | 5 | A clearly articulated, load-bearing concept that opens something new; concept, theme, and technique are distinct (glossary §7) |
| Strong | 4 | A clear concept that the work genuinely embodies |
| Adequate | 3 | A concept is present but under-articulated |
| Weak | 2 | Theme and technique described, but the concept is never stated |
| None | 1 | No concept — only depiction and method |

### Dimension 3: Documentation Rigor — Weight 20%

| Level | Score | Description |
|-------|-------|-------------|
| Outstanding | 5 | Rich, legible documentation (stills, video, diagrams, code, install photos) that lets a reader encounter the work; claims well-anchored; courtesy lines present |
| Strong | 4 | Documentation supports all major claims about the work |
| Adequate | 3 | Most claims anchored; some documentation gaps |
| Weak | 2 | Key claims about the work or its reception lack any anchor (reception inflation) |
| Unacceptable | 1 | Serious disconnect between claims and documentation |

### Dimension 4: Technical / Material Realization — Weight 15%

| Level | Score | Description |
|-------|-------|-------------|
| Outstanding | 5 | Realization described clearly enough to be plausible and, in principle, legible to another practitioner; making documented as research |
| Strong | 4 | Sound realization account with minor gaps |
| Adequate | 3 | Realization conveyed but with notable omissions or imprecise terms (generative/interactive/autonomous) |
| Weak | 2 | Technical/material claims (real-time, autonomous, novel) asserted without an anchor |
| Unacceptable | 1 | Realization claims that the work cannot plausibly support (fabricated capability) |

### Dimension 5: Contribution to Discourse — Weight 15%

| Level | Score | Description |
|-------|-------|-------------|
| Outstanding | 5 | Precisely positioned against the right precedents; a genuine new step in the art+tech conversation |
| Strong | 4 | Well-positioned; clear relation to precedent works |
| Adequate | 3 | Positioned, but precedence/novelty claims are loose |
| Weak | 2 | Poor positioning; precedence inflation ("the first to…" with uncited precedents) |
| Unacceptable | 1 | No positioning, or positioning that is art-historically wrong |

---

## 2. Pattern-Specific Criteria

Per `shared/references/art_paper_structure_patterns.md`.

### 2.1 Practice-Based (Pattern 1, DEFAULT)

| Additional Focus | Review Anchor |
|---|---|
| Making-as-research | Is the making documented as research, not an artist statement? |
| Situated insight | Did insight emerge through making, anchored to the process record? |
| Authorship/collaboration | Are contributor roles named (glossary §4)? |

### 2.2 Practice-Led

| Additional Focus | Review Anchor |
|---|---|
| Insight into practice | Is the claimed insight about the practice itself, falsifiable against the process? |
| Artifact role | Is the artifact illustrative (vs. the contribution) — and is that owned? |

### 2.3 Critical / Theoretical Essay (Pattern 3)

| Additional Focus | Review Anchor |
|---|---|
| Conceptual definition precision | Are core concepts clearly delineated? |
| Argument structure | Is each claim anchored to a specific named work? |
| Counter-position handling | Are opposing critical positions engaged? |

### 2.4 Series / Portfolio (Pattern 4)

| Additional Focus | Review Anchor |
|---|---|
| Trajectory | Is there a real throughline across the works? |
| Cross-cutting reflection | Does the series demonstrate something the single works do not? |

### 2.5 Art-Science Hybrid (Pattern 5, IMRaD-leaning)

| Additional Focus | Review Anchor |
|---|---|
| Genuine technical/empirical sub-contribution | Is the evaluation/observation described well enough to be plausible? |
| Situated framing | Are observations framed as situated, not over-generalized? |
| Artistic lens dominant | Is the artwork still the argument, not flattened into a "system"? |
| *(Only this pattern admits a Method/Results-style empirical lens.)* | |

---

## 3. Common Review Pitfalls

### Biases Reviewers Should Avoid

| Pitfall | Description | How to Avoid |
|---------|-------------|--------------|
| **Hypercriticism** | Overblowing minor issues, ignoring the work's overall contribution | Affirm strengths first; distinguish major from minor |
| **Statistical-rigor projection** | Demanding sample sizes, power, p-values from a practice-based work | Use the art-research evidence model; the artwork is the evidence |
| **IMRaD-forcing** | Expecting a Method/Results structure | Evaluate the chosen art-paper structure on its own terms (Patterns 1-5) |
| **Taste projection** | Down-scoring because the work's provocation is not to your taste | Evaluate how well the work makes its case, not whether you endorse it |
| **Prestige bias** | Relaxing standards because of the artist's exhibition record | Focus on the work and paper themselves |
| **Novelty bias** | Over-valuing "the first to…" claims | Require precedence claims to be citable; reward precise positioning |
| **Citation-wall bias** | More references = more rigor | A few precisely positioned references beat a dense wall (evidence model §6) |
| **Documentation-as-work** | Treating a render/video as the work for an experiential claim | Distinguish the work from its documentation (glossary §2) |

### Principles of Constructive Feedback

1. **Specific, not vague**: "The 'autonomous' claim in §5 has no system description to anchor it" beats "the technical part is weak"
2. **Problem + reason + suggestion**: every criticism states what, why, and how to strengthen (often: what documentation would anchor the claim)
3. **Distinguish required from suggested**: which changes are mandatory, which are "nice to have"
4. **Acknowledge uncertainty**: "I'm not sure the documentation shows X" is more accurate than "the artist ignored X"
5. **Respect the artist**: even if the work is weak, the artist invested real making effort

---

## 4. Scoring Aggregation

### Weighted Total Score Calculation

```
Total Score =
  Artistic Merit & Significance (25%) +
  Conceptual Contribution (25%) +
  Documentation Rigor (20%) +
  Technical / Material Realization (15%) +
  Contribution to Discourse (15%)
```

### Score-to-Decision Mapping

| Weighted Total | Recommended Decision | Note |
|---------------|---------------------|------|
| 4.5-5.0 | Accept | Very few works reach this level on first pass |
| 3.5-4.4 | Minor Revision | Strong work; clarify concept / strengthen documentation |
| 2.5-3.4 | Major Revision | Has potential but needs re-framing or fuller documentation |
| 1.5-2.4 | Reject (Resubmit) | Fundamental issues, but the work has value |
| 1.0-1.4 | Reject | Not suitable for this program, or below standard |

**Important reminder**: Scores are reference only. The final decision also considers:
- Whether any single dimension is fatally low (e.g., Conceptual Contribution = 1 — no load-bearing concept — may drive Reject even if other scores pass)
- The specific content of reviewer comments matters more than the numbers
- The program's character and the current CFP (verify, do not assume a fixed bar)
