# Art Paper Structure Patterns — Practice-Based Art Research

Used by `art-paper` (`structure_architect_agent`, `intake_agent`) and `art-inquiry` to select the appropriate structure for a **SIGGRAPH Asia Art Paper** (proceedings on the ACM Digital Library; verify category/venue against the current CFP) and adjacent practice-based art-research venues.

> **Genre note:** these patterns replace IMRaD as the *default* for art-paper. IMRaD survives only as Pattern 5 (art-science hybrid) for work whose contribution is genuinely empirical. The defining move of an art paper is that **the artwork is the argument** — structure serves the work, not a fixed Method/Results contract.

> **Venue caveat:** SIGGRAPH Asia Art Papers section requirements, length, and anonymization rules drift year to year. Treat the word-allocation tables below as defaults and verify against the current Call for Art Papers before submission.

---

## Pattern 1: Practice-Based Art Paper (DEFAULT)

**Best for:** A paper centered on one (or a tight series of) the author's own artwork(s), where insight emerges *through* making.
**Typical length:** 3,000–6,000 words + figure-rich documentation.
**Lineage:** Candy & Edmonds practice-based research; *Leonardo* art paper conventions.

### Structure
```
1. Title + Abstract (120–200 words) + Keywords (4–6)
2. Introduction / Context
   2.1 The work in one paragraph (what the reader will encounter)
   2.2 Artistic & conceptual context (movements, precedent works, discourse)
   2.3 The question or provocation the work pursues
   2.4 Contribution statement (what this paper adds to art+technology discourse)
3. Conceptual Framework
   3.1 Theoretical / philosophical grounding
   3.2 Relationship to precedent artworks and artists (positioning, not lit-review)
   3.3 Key concepts and their definitions
4. The Work
   4.1 Description: form, materials, media, scale, duration
   4.2 Experience: what the audience perceives / does
   4.3 Authorship & collaboration (credit, roles)
5. Realization / Methods of Making
   5.1 Technical approach (systems, algorithms, fabrication, materials)
   5.2 Process and iteration (decisions, failures, pivots)
   5.3 Tools and dependencies
6. Reflection / Discussion
   6.1 What the making revealed (situated insight)
   6.2 Exhibition & reception (where shown, how encountered, observed responses)
   6.3 Relation back to the conceptual framework
   6.4 Limitations and open questions
7. Conclusion / Future Work
8. References (ACM Reference Format)
9. Acknowledgements + AI-usage disclosure + image credits
```

### Word Allocation (5,000-word example)
| Section | % | Words |
|---|---|---|
| Introduction / Context | 18% | 900 |
| Conceptual Framework | 22% | 1,100 |
| The Work | 18% | 900 |
| Realization | 20% | 1,000 |
| Reflection / Discussion | 17% | 850 |
| Conclusion | 5% | 250 |

---

## Pattern 2: Artist Statement / Project Description

**Best for:** Shorter submissions, gallery/exhibition catalog texts, or the `artist-statement` mode. Single work, concept-forward.
**Typical length:** 800–2,500 words.

### Structure
```
1. Title + one-line work descriptor
2. The provocation (why this work exists)
3. The work (form, experience, media)
4. Concept (the idea the work embodies; key references woven in)
5. Making (the essential technical/material gesture)
6. Significance (what it opens up)
7. Credits + references
```

---

## Pattern 3: Critical / Theoretical Art Essay

**Best for:** Papers whose contribution is a *concept, framework, or critique* in art-and-technology, not a single authored artwork. The author may discuss others' works as primary material.
**Typical length:** 4,000–8,000 words.

### Structure
```
1. Abstract + Keywords
2. Introduction: the problem in the discourse + thesis
3. Background: the discourse this enters (precedent positions)
4. Argument
   4.1 Claim 1 — grounded in artwork(s) as evidence
   4.2 Claim 2 — ...
   4.3 Claim 3 — ...
5. Synthesis: the proposed concept / framework / critique
6. Implications for practice
7. Conclusion
8. References
```

---

## Pattern 4: Series / Portfolio Paper

**Best for:** A body of work developed over time; the contribution is the *trajectory* and what it reveals across iterations.
**Typical length:** 4,000–7,000 words.

### Structure
```
1. Abstract + Keywords
2. Introduction: the throughline of the series + research interest
3. Conceptual & technical lineage
4. Work 1 → insight → Work 2 → insight → Work 3 (chronological or thematic)
5. Cross-cutting reflection: what the series as a whole demonstrates
6. Conclusion + future trajectory
7. References
```

---

## Pattern 5: Art-Science Hybrid (IMRaD-leaning)

**Best for:** Work with a genuine empirical or technical contribution alongside the artistic one (e.g., a new interactive system evaluated with users, a novel generative method).
**Typical length:** 5,000–8,000 words.
**Note:** This is the bridge to ARS's original IMRaD. Use only when there is a real Method/Results contribution; otherwise prefer Pattern 1.

### Structure
```
1. Abstract + Keywords
2. Introduction (artistic + technical motivation)
3. Related Work (artistic precedents + technical prior art)
4. The Work / System Design
5. Implementation / Method
6. Evaluation / Exhibition Findings (may include user observation, but framed as situated)
7. Discussion (artistic significance + technical contribution)
8. Conclusion
9. References
```

---

## Selection Heuristics (for `intake_agent` / `structure_architect_agent`)

| Author has… | Recommend |
|---|---|
| one authored artwork, insight from making | **Pattern 1** |
| short concept-forward text, single work | Pattern 2 |
| a concept/critique, discussing others' works | Pattern 3 |
| a multi-work body developed over time | Pattern 4 |
| a real technical/empirical contribution + artwork | Pattern 5 |

When unsure, default to **Pattern 1** and confirm with the author. Never force IMRaD onto a practice-based contribution — that is the canonical art-paper failure mode (the work gets flattened into a "system" and the artistic argument disappears).
