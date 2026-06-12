# Claim Verification Protocol (Phase E)

## Purpose
Verifies that factual claims attributed to cited sources (precedent works, theory, technical papers) are accurately supported by those sources. Phase A-D verify that references exist and are original; Phase C verifies the paper's own artwork/realization claims; Phase E verifies that claims derived from cited sources are truthful.

> Phase C (artwork/realization claims: reception, precedence, technical capability, attribution, exhibition record) and Phase E (source-attributed factual claims) are complementary. A "first work to…" claim, for instance, is checked in Phase C for an evidence anchor *and* in Phase E against any precedent survey it cites.

## Scope
- All numerical/quantitative claims (counts, durations, dates, audience figures, percentages)
- All categorical assertions ("X is the largest...", "Y was the first to...")
- All trend / discourse claims ("a growing body of work", "increasingly")
- All causal/relational claims ("X influenced Y", "X led to Y")

## E1: Claim Extraction
- Scan the paper for all quantitative/factual claims
- For each claim, record: claim text, cited source(s), paper section, page/line
- Expected output: Claim Registry table

## E2: Source Tracing
- For each claim, locate the specific passage in the cited source that supports it
- Use WebSearch + DOI lookup to find the original source
- If source is behind paywall, note as UNVERIFIABLE_ACCESS

## E3: Cross-Referencing
- Compare claim text vs source text
- Check: exact numbers, dates/years, faithful attribution of an argument or position, correct description of a precedent work's approach
- Flag any discrepancies

## Verdict Taxonomy

| Verdict | Definition | Severity | Example |
|---------|-----------|----------|---------|
| VERIFIED | Claim matches source exactly or within rounding tolerance | None | Paper: "15.2%"; Source: "15.2%" |
| MINOR_DISTORTION | Claim paraphrases source but meaning is preserved | MINOR | Paper: "about 15%"; Source: "15.2%" |
| MAJOR_DISTORTION | Claim oversimplifies, exaggerates, or misrepresents source | SERIOUS | Paper: "declined sharply"; Source: "declined by 2.1%" |
| UNVERIFIABLE | Source doesn't contain the claimed information | SERIOUS | Paper cites Smith (2020) for a claim, but Smith (2020) doesn't discuss this topic |
| UNVERIFIABLE_ACCESS | Source exists but full text not accessible for verification | MEDIUM | Paywalled journal article |

## Sampling Strategy
- Mode 1 (pre-review): 30% random sample of claims (minimum 10 claims)
- Mode 2 (final-check): 100% of claims

## Output Format

### Claim Verification Report
| # | Claim | Source | Section | Verdict | Detail |
|---|-------|-------|---------|---------|--------|
| 1 | [claim text] | [source] | [section] | VERIFIED | Exact match |
| 2 | [claim text] | [source] | [section] | MAJOR_DISTORTION | Paper says X, source says Y |

### Summary
- Total claims checked: [N]
- VERIFIED: [N]
- MINOR_DISTORTION: [N]
- MAJOR_DISTORTION: [N] (must be 0 for PASS)
- UNVERIFIABLE: [N] (must be 0 for PASS)
- UNVERIFIABLE_ACCESS: [N] (noted but does not block PASS)

## Pass/Fail Criteria
- PASS: Zero MAJOR_DISTORTION + Zero UNVERIFIABLE
- FAIL: Any MAJOR_DISTORTION or UNVERIFIABLE
- PASS_WITH_NOTES: Only MINOR_DISTORTION and/or UNVERIFIABLE_ACCESS
