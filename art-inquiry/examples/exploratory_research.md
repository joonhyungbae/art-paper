# Example: Exploratory Inquiry — Full Pipeline

## User Request
```
Develop the concept behind my generative installation that uses live air-quality
data, and position it in art-and-technology discourse
```

## Phase 1: SCOPING

### research_question_agent Output

**Topic Area**: A generative installation that sonifies and visualizes live urban air-quality data, positioned in the discourse on data-driven environmental art

**Primary Artistic Provocation**:
> Can a generative artwork driven by live air-quality data make an invisible environmental harm *felt* — shifting it from an abstract statistic to an embodied, present condition the viewer shares the room with?

**FINER Assessment** (adapted: Feasible / Interesting / Novel / Ethical / Relevant for a practice-based inquiry):
| Criterion | Score | Justification |
|-----------|-------|---------------|
| Feasible | 4/5 | Public sensor APIs accessible; artist has prior generative-systems practice |
| Interesting | 5/5 | Sits at a live intersection of climate concern and generative art |
| Novel | 3/5 | Data-driven environmental art is an established lineage; the contribution must be sharpened beyond "data as input" |
| Ethical | 4/5 | Raises questions about aestheticizing harm; no human subjects |
| Relevant | 5/5 | Directly informs the work's framing and its positioning for an Art Papers submission |
| **Average** | **4.2/5** | |

**Scope Boundaries**:
- In scope: precedent artworks in data sonification/visualization and eco-art; theory of embodiment, atmosphere, and environmental perception; the artist's own prior generative work
- Out of scope: the engineering of the sensor pipeline as an end in itself; climate-science claims the work cannot evidence; a full empirical audience study (this is practice-based, not an HCI evaluation)
- Key assumptions: the work is gallery/public-space sited; "felt" means a perceptual/affective shift, not a measured behavior change

**Sub-questions** (provocation refinements):
1. What distinguishes this work from prior data-driven environmental art — what is the specific contribution?
2. Which theoretical frames (atmosphere, embodiment, the sublime, slow violence) best position the work?
3. How should reception be framed and documented without overclaiming impact?

### research_architect_agent Output

**Inquiry Stance**: Practice-based (insight emerges *through* making the work)
**Methodology**: Reflective practice + conceptual positioning against precedent works and theory
**Evidence Strategy**: Triangulation per `shared/references/art_research_evidence_model.md` — the work as encountered, process/realization record, exhibition & reception, conceptual lineage, situated reflection
**Analytical Framework**: Thematic positioning organized by sub-questions; precedent works read as lineage, not as a literature ranking
**Rigor Criteria**: Each claim anchored to an evidence type; reception claims anchored to a named venue/date + observable detail; novelty hedged or cited

### devils_advocate_agent — CHECKPOINT 1

**Verdict**: PASS (with minor notes)
- Minor: "make harm felt" is a strong affective claim — ensure reception is framed around what was observed, not asserted
- Minor: Define the contribution sharply; "uses live data" is not in itself novel
- Observation: Watch for aestheticization critique — the work may be read as making pollution beautiful

## Phase 2: INVESTIGATION

### bibliography_agent Output

**Search Strategy**: Art/theory sources via ACM Digital Library (SIGGRAPH/SIGGRAPH Asia Art Papers, *Leonardo*), art-criticism and theory databases, exhibition catalogues, and primary artwork documentation; keywords: "data sonification" / "environmental art" / "generative installation" / "atmosphere" / "slow violence"; precedent artworks treated as primary lineage evidence.

**Corpus**: 31 candidates -> 22 retained (precedent artworks + theory + criticism)

**Annotated Bibliography** (excerpt — ACM Reference Format):
1. **Precedent work** — Natalie Jeremijenko. 2006. *Feral Robotic Dogs*. Pollution-sensing public artwork. (venue/date locator; no DOI)
   - Relevance: Foundational data-driven environmental art using sensing as civic gesture
   - Lineage note: positions sensing-as-activism; this work differs by foregrounding *perception* over data legibility
2. **Theory** — Timothy Morton. 2013. *Hyperobjects: Philosophy and Ecology after the End of the World*. University of Minnesota Press.
   - Relevance: Frames climate harm as a "hyperobject" too vast to perceive directly — directly supports the "make felt" provocation
   - Use: conceptual framework, §atmosphere/scale

[... 20 more sources — mix of precedent artworks (venue+date locators) and theory/criticism (ACM Reference Format) ...]

### source_verification_agent Output

**Sources Reviewed**: 22 | **Verified**: 20 | **Flagged**: 2 | **Rejected**: 0

**Flagged**:
1. Source #14 — Exhibition claim for a precedent work cites an award but no verifiable venue/date -> require locator or hedge
2. Source #19 — A "first artwork to use live air data" precedence claim in a catalogue essay -> treat as the essayist's claim, not fact; do not inherit it

## Phase 3: ANALYSIS

### synthesis_agent Output

**Key Themes (positioning)**:
1. **Data-as-perception vs data-as-information** (Strong lineage, 8 sources): the contribution is foregrounding embodied perception over legible readout
2. **Atmosphere & the imperceptible** (Strong, theory): Morton's hyperobject + atmosphere theory ground the "make felt" provocation
3. **The aestheticization risk** (Contested, 5 sources): critics warn that beautifying harm can defuse it; the work must hold this tension explicitly
4. **Sited reception** (Emerging): how the work behaves differs by venue (gallery vs transit hub)
5. **Authorship of generative systems** (Emerging): credit for the system vs the live data source

**Key Tension**: Sources disagree on whether aestheticizing environmental harm mobilizes or anesthetizes audiences — resolution is contextual and should be discussed, not resolved by assertion.

**Knowledge/Discourse Gaps**: Little prior work foregrounds *atmosphere/embodiment* over data legibility in this lineage; reception of data-driven eco-art is rarely documented with observable anchors.

### devils_advocate_agent — CHECKPOINT 2

**Verdict**: PASS
- Minor: Positive framing detected — give the aestheticization critique equal weight
- Observation: Most precedent works are Euro-American; note the lineage's geographic skew

## Phase 4: COMPOSITION

### report_compiler_agent Output

[Full synthesis report, Practice-Based Art Paper structure (Pattern 1), ~5,200 words]

Title: Breathing the Invisible: A Generative Air-Quality Installation and the Problem of Making Environmental Harm Felt

[Abstract, Introduction/Context, Conceptual Framework (atmosphere + data-as-perception), The Work + Realization, Reflection/Discussion (organized by the 5 themes, incl. aestheticization tension and sited reception), Conclusion/Future Work, References (22 sources, ACM Reference Format)]

## Phase 5: REVIEW

### editor_in_chief_agent Output

**Verdict**: Minor Revision (Score: 3.7/5.0)
- Strength: Sharp positioning; the contribution is clearly differentiated from prior data-driven eco-art
- Major: Reflection section needs a tighter loop back to the conceptual framework (atmosphere theory underused in interpreting the work)
- Minor: Two precedent-work citations lack venue/date locators
- Minor: Abstract exceeds the 200-word art-paper target

### ethics_review_agent Output

**Verdict**: CLEARED
- AI-usage disclosure present (two-channel: AI in making the artwork vs AI in writing the paper)
- Citations + artwork/exhibition claims spot-checked (5/22 = 23%) — all verified or hedged
- Dual-use risk: Low
- Fair representation: Adequate (noted the lineage's geographic skew)

### devils_advocate_agent — CHECKPOINT 3

**Verdict**: PASS
- Observation: The reflection claims the work "moved viewers to discuss air quality" — this is reception inflation without an observable anchor; down-scope to what was observed at the named venue
- "So what?" test: Passed — clear contribution to data-driven environmental art discourse

## Phase 6: REVISION

### report_compiler_agent (Revision 1)

**Changes**:
1. Reflection section rewritten to interpret the work through atmosphere theory (Major, Editor)
2. Two precedent-work citations given venue/date locators (Minor, Editor)
3. Abstract trimmed to 190 words (Minor, Editor)
4. Reception claim down-scoped: "at [venue, date], several visitors lingered and remarked on the shifting sound" replaces "moved viewers to discuss air quality" (Observation, Devil's Advocate — reception inflation)

**Final Word Count**: 5,450 words
**Revision Loops Used**: 1 of 2

---

## Final Output Summary
- Full synthesis report (Practice-Based Art Paper, Pattern 1): 5,450 words
- 22 cited sources (precedent works with venue/date locators + theory in ACM Reference Format)
- 5 positioning themes
- Contribution sharply differentiated from prior data-driven eco-art
- Ethics cleared (two-channel AI-usage disclosure)
- 1 revision loop completed
