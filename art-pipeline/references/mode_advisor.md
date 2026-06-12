# Mode Advisor — Unified Cross-Skill Decision Tree

## Purpose

Helps users (and the pipeline orchestrator) select the right skill and mode for their current situation. Eliminates the most common routing mistakes by mapping user intent to the optimal entry point.

---

## Quick Decision Matrix

| What do you want? | How far along? | Time? | Skill + Mode |
|-------------------|---------------|-------|--------------|
| Explore a topic | Starting fresh | 30 min | art-inquiry quick |
| Explore a topic | Starting fresh | 2+ hr | art-inquiry full |
| Think through a research idea | Have vague idea | Any | art-inquiry socratic |
| Systematic review | Have clear PICO | 3+ hr | art-inquiry systematic-review |
| Verify claims | Have specific claims | 30 min | art-inquiry fact-check |
| Write a paper | Have research done | 2+ hr | art-paper full |
| Plan a paper step by step | Have RQ, need structure | 1+ hr | art-paper plan |
| Fix citations | Have draft | 30 min | art-paper citation-check |
| Convert format | Have final draft | 15 min | art-paper format-convert |
| Review a paper | Have paper to evaluate | 1 hr | art-reviewer full |
| Check revision quality | Have revised draft | 30 min | art-reviewer re-review |
| Full pipeline (zero to publication) | Starting fresh | 5+ hr | art-pipeline |
| Handle real reviewer feedback | Have review comments | 1+ hr | art-pipeline (Stage 4 entry) |

---

## Common Misconceptions

| User Says | They Probably Need | Why |
|-----------|-------------------|-----|
| "Write me a paper on X" | art-inquiry first, THEN art-paper | Writing without research produces shallow papers with unsupported claims |
| "Review my paper" (but no draft exists) | art-paper plan mode | They need to write first, not review |
| "Check my citations" (but paper isn't done) | art-paper full mode | Finish writing first, then check citations as a separate pass |
| "I need a systematic review" | art-inquiry systematic-review mode | NOT art-paper lit-review structure (different methodology: PRISMA vs narrative) |
| "Just give me a quick paper" | art-inquiry quick + art-paper full | Quick research is fine, but paper writing still needs the full mode for quality |
| "Format my paper in ACM Reference Format / acmart" | art-paper format-convert mode | Not a rewrite; purely formatting transformation |
| "I got reviewer comments" | art-pipeline Stage 4 entry (External Review) | Needs structured intake + strategic coaching, not just "fix what they said" |

---

## User Archetype Recommendations

| Archetype | Recommended Workflow | Rationale |
|-----------|---------------------|-----------|
| Emerging artist (first art paper) | art-inquiry socratic -> art-paper plan -> full pipeline | Socratic mode builds the conceptual framing; plan mode structures the practice-based paper incrementally; pipeline ensures integrity gates |
| Practicing artist (SIGGRAPH Asia submission prep) | art-pipeline (full, from Stage 1 or mid-entry) | Knows the work; benefits from the automated integrity checks (citations + artwork/realization claims) and acmart finalization |
| Mentor reviewing a student's art paper | art-reviewer full | Provides structured multi-perspective feedback the mentor can use in studio crit |
| Quick precedent / discourse scan | art-inquiry quick or lit-review | Fast turnaround; no need for full pipeline overhead |
| Jury revision response | art-pipeline (Stage 4 entry with review comments) | External Review Protocol handles real reviewer feedback with strategic coaching |
| Short art paper (tight deadline) | art-inquiry quick -> art-paper full | Compressed timeline; quick inquiry + full writing on a practice-based structure |
| Single interactive installation write-up | art-inquiry full -> art-paper full (Pattern 1) | The work is the argument; full depth on the practice-based art-paper structure |
| Artist statement / project description | art-inquiry quick -> art-paper full (Pattern 2) | Concept-forward and concise; quick inquiry sufficient for the scope |

---

## Skill Capability Boundaries

Understanding what each skill can and cannot do prevents misrouting:

| Skill | Can Do | Cannot Do |
|-------|--------|-----------|
| art-inquiry | Literature search, synthesis, RQ refinement, fact-checking | Write papers, review papers, format documents |
| art-paper | Write papers, revise papers, format documents, check citations | Conduct original research, review papers (as reviewer), verify integrity |
| art-reviewer | Review papers (5-person panel), re-review revisions | Write papers, conduct research, fix issues (only identifies them) |
| art-pipeline | Orchestrate all stages, manage transitions, track state | Perform any substantive work (purely dispatching and coordinating) |
| integrity_verification_agent | Verify references, citations, artwork/realization claims, originality | Fix issues (only identifies them), review paper quality |

---

## Decision Flowchart

```
START: What does the user want?
  |
  +--> "I want to research/explore/investigate"
  |      |
  |      +--> Have specific claims to verify? --> art-inquiry fact-check
  |      +--> Have clear PICO/systematic question? --> art-inquiry systematic-review
  |      +--> Want guided exploration? --> art-inquiry socratic
  |      +--> Want direct results, have time? --> art-inquiry full
  |      +--> Want direct results, short on time? --> art-inquiry quick
  |
  +--> "I want to write a paper"
  |      |
  |      +--> Have research/literature ready? --> art-paper (plan or full)
  |      +--> No research done yet? --> art-inquiry FIRST, then art-paper
  |      +--> Want full quality assurance? --> art-pipeline (from Stage 1)
  |
  +--> "I want someone to review my paper"
  |      |
  |      +--> Have a complete draft? --> art-reviewer full
  |      +--> Want integrity check + review? --> art-pipeline (Stage 2.5 entry)
  |      +--> No draft yet? --> art-paper first
  |
  +--> "I need to revise based on feedback"
  |      |
  |      +--> From AI reviewers (pipeline)? --> Continue pipeline (Stage 4)
  |      +--> From real journal reviewers? --> art-pipeline Stage 4 entry (External Review)
  |
  +--> "I want the full treatment (research to publication)"
         |
         +--> art-pipeline (Stage 1 entry)
```

---

## Pipeline Stage Entry Points

For users entering the pipeline mid-stream, this table clarifies what materials are needed:

| Entry Point | Required Materials | What Gets Skipped | Integrity Implications |
|------------|-------------------|-------------------|----------------------|
| Stage 1 (INQUIRY) | None | Nothing | Full pipeline |
| Stage 2 (WRITE) | RQ Brief + Bibliography | Stage 1 | Full pipeline from Stage 2 |
| Stage 2.5 (INTEGRITY) | Paper draft | Stages 1-2 | Integrity check runs on provided draft |
| Stage 3 (REVIEW) | Verified paper + integrity report | Stages 1-2.5 | User must provide integrity evidence |
| Stage 4 (REVISE) | Paper + review comments | Stages 1-3 | Pipeline runs Stage 4 -> 3' -> 4' -> 4.5 -> 5 |
| Stage 5 (FINALIZE) | Paper + integrity pass report | Stages 1-4.5 | Must show Stage 4.5 passed |

---

## Anti-Patterns

These are common workflow mistakes to avoid:

| Anti-Pattern | Problem | Correct Approach |
|-------------|---------|-----------------|
| Skipping research | Paper lacks evidence depth | Always do at least art-inquiry quick |
| Writing then researching | Confirmation bias in source selection | Research first, write second |
| Reviewing before integrity check | Wasted review effort on fabricated citations | Always Stage 2.5 before Stage 3 |
| Accepting all reviewer comments blindly | May introduce inconsistencies or weaken valid arguments | Use External Review Protocol's strategic coaching |
| Running pipeline for a 1-page abstract | Overhead far exceeds benefit | Use art-paper full directly |
| Using fact-check mode for literature review | Different purpose and methodology | Use art-inquiry full or systematic-review |
