# Quality Rubrics for Art Paper Review

## Purpose

Provides calibrated scoring rubrics for the review dimensions used by all reviewers (R1 Practitioner, R2 Curator, R3 Critic, DA). Ensures consistent, reproducible scoring across different art papers and review sessions. Scored against the art-research evidence model (`shared/references/art_research_evidence_model.md`), not statistical rigor.

## Known error profile (v3.2)

These rubrics define *what* to measure, not *how accurate* the measurement is. A single LLM reviewer's absolute rubric score has calibration error that depends on domain, paper type, and model version.

For users who want to know this reviewer's empirical FNR / FPR / balanced accuracy before relying on these rubric scores, run the opt-in **calibration mode** (see `calibration_mode_protocol.md`). Calibration mode compares this reviewer's decisions against a user-supplied gold set and produces a Calibration Report that attaches as a confidence disclosure to subsequent reviews in the same session.

Without calibration, treat rubric scores as *ordinally* meaningful (works scored 85 are stronger than works scored 65) but *not cardinally* interpretable (an 85 does not guarantee acceptance into the program).

## Scoring Scale

All dimensions scored 0-100. Final weighted score determines editorial decision.

## Decision Mapping

| Weighted Average | Decision |
|-----------------|----------|
| >= 80 | Accept |
| 65-79 | Minor Revision |
| 50-64 | Major Revision |
| < 50 | Reject |

---

## Dimension 1: Artistic Merit & Significance (Weight: 25%)

| Score Range | Descriptor | Behavioral Indicators |
|------------|------------|----------------------|
| 90-100 | Exceptional | A resonant, significant work with a distinct voice; meaningfully advances the art-and-technology discourse |
| 75-89 | Strong | Clearly significant; a distinct artistic position |
| 60-74 | Adequate | Competent work of modest significance |
| 45-59 | Weak | Significance unclear; does not register beyond its own description |
| < 45 | Insufficient | No discernible artistic significance |

## Dimension 2: Conceptual Contribution (Weight: 25%)

| Score Range | Descriptor | Behavioral Indicators |
|------------|------------|----------------------|
| 90-100 | Exceptional | A clearly articulated, load-bearing concept that opens something new; concept/theme/technique kept distinct (glossary §7) |
| 75-89 | Strong | A clear concept the work genuinely embodies |
| 60-74 | Adequate | A concept is present but under-articulated |
| 45-59 | Weak | Theme and technique described, but the concept is never stated |
| < 45 | Insufficient | No concept — only depiction and method |

## Dimension 3: Documentation Rigor (Weight: 20%)

| Score Range | Descriptor | Behavioral Indicators |
|------------|------------|----------------------|
| 90-100 | Exceptional | Rich, legible documentation (stills, video, diagrams, code, install photos); claims well-anchored; courtesy lines present; reception anchored to observed/recorded response |
| 75-89 | Strong | Documentation supports all major claims about the work |
| 60-74 | Adequate | Most claims anchored; some documentation gaps |
| 45-59 | Weak | Key claims about the work or its reception lack any anchor (reception inflation) |
| < 45 | Insufficient | Severe disconnect between claims and documentation |

## Dimension 4: Technical / Material Realization (Weight: 15%)

| Score Range | Descriptor | Behavioral Indicators |
|------------|------------|----------------------|
| 90-100 | Exceptional | Realization described clearly enough to be plausible and, in principle, legible to another practitioner; making documented as research; terms precise (generative/interactive/autonomous) |
| 75-89 | Strong | Sound realization account with minor gaps |
| 60-74 | Adequate | Realization conveyed but with notable omissions or imprecise terms |
| 45-59 | Weak | Technical/material claims (real-time, autonomous, novel) asserted without an anchor |
| < 45 | Insufficient | Realization claims the work cannot plausibly support (fabricated capability) |

## Dimension 5: Contribution to Discourse (Weight: 15%)

| Score Range | Descriptor | Behavioral Indicators |
|------------|------------|----------------------|
| 90-100 | Exceptional | Precisely positioned against the right precedents; a genuine new step in the art+tech conversation; precedence claims accurate/citable |
| 75-89 | Strong | Well-positioned; clear relation to precedent works |
| 60-74 | Adequate | Positioned, but precedence/novelty claims loose |
| 45-59 | Weak | Poor positioning; precedence inflation ("first to…" with uncited precedents) |
| < 45 | Insufficient | No positioning, or art-historically wrong positioning |

## Optional Sub-Lenses (reviewer-specific)

### Conceptual Lineage Depth (R2 Curator focus)

| Score Range | Descriptor |
|------------|------------|
| 90-100 | Precise coverage of canonical + recent precedents; identifies the lineage; positions the work exactly in the conversation |
| 75-89 | Good coverage; most key precedents cited; reasonable positioning |
| 60-74 | Adequate but gaps; some important precedents missing; positioning vague |
| < 60 | Significant precedent gaps; key works missing; poor positioning |

### Cultural / Ethical Stakes (R3 Critic focus)

| Score Range | Descriptor |
|------------|------------|
| 90-100 | Engages the work's cultural and ethical stakes with theoretical depth; provenance/consent/representation considered |
| 75-89 | Good engagement with cultural OR ethical stakes |
| 60-74 | Some engagement but narrowly scoped |
| < 60 | Minimal engagement; unclear why the work matters culturally |

---

## Aggregation Formula

```
Final Score = (Artistic Merit x 0.25) + (Conceptual Contribution x 0.25) + (Documentation Rigor x 0.20) + (Technical Realization x 0.15) + (Contribution to Discourse x 0.15)
```

Optional sub-lenses are reported separately and factored into the editorial synthesis narrative but do not change the numerical score.

---

## Calibration Notes

- Scores should reflect the work's quality relative to the program's character (verify against the current CFP)
- A "75" for a SIGGRAPH Asia Art Papers-level program is not equivalent to "75" for a regional festival
- When in doubt, err toward the middle of a range
- Reviewers should explicitly state which range descriptor best matches, then fine-tune within that range
- If two dimensions are at odds (e.g., excellent realization but weak conceptual contribution), do NOT average down — report both scores honestly
- Honest situated specificity is rewarded; over-claimed generalizability is penalized (evidence model §5)
