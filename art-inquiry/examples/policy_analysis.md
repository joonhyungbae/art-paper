# Example: Comparative Lineage Study (full mode)

> Demonstrates the same comparative-matrix mechanic the ARS pipeline used for policy
> analysis, re-cast for practice-based art research: instead of comparing policy
> regimes across countries, the inquiry compares **authorship strategies across a
> lineage of autonomous / generative artworks** to position the artist's own work.

## User Request
```
Help me position my autonomous generative artwork by comparing how authorship and
control are handled across the lineage of generative art systems
```

## Phase 1: SCOPING

### research_question_agent Output

**Primary Artistic Provocation**:
> Across the lineage of generative and autonomous artworks, how do artists distribute authorship between themselves, the system, and chance — and what does positioning my work within that spectrum reveal about its specific contribution?

**FINER Assessment**:
| Criterion | Score | Justification |
|-----------|-------|---------------|
| Feasible | 4/5 | Rich documented lineage from Cybernetic Serendipity onward |
| Interesting | 4/5 | Authorship is a live, contested question in generative + AI art |
| Novel | 3/5 | Several surveys exist; the contribution must be the *positioning move*, not a new survey |
| Ethical | 5/5 | Discourse positioning; no human subjects |
| Relevant | 5/5 | Directly grounds the contribution statement of the artist's paper |
| **Average** | **4.2/5** | |

**Sub-questions**:
1. What authorship strategies (rule-author, curator-of-output, system-collaborator, relinquished-control) appear across the lineage?
2. How is "autonomy" claimed and evidenced in each precedent work?
3. Where does the artist's own work sit, and what does that position contribute?

### research_architect_agent Output

**Inquiry Stance**: Practice-based, comparative-positioning
**Methodology**: Comparative lineage analysis across precedent artworks + theory of authorship
**Framework**: Cross-work comparison matrix (authorship strategy x autonomy claim x evidence type)
**Evidence**: Precedent artwork documentation, artist statements, exhibition records, theory/criticism
**Analysis**: Cross-work comparison matrix + thematic synthesis

### devils_advocate_agent — CHECKPOINT 1

**Verdict**: PASS
- Minor: "Autonomy" needs an operational definition — specify what observable features count as autonomous
- Observation: The choice of which precedent works to include will shape the conclusion — justify selection

## Phase 2: INVESTIGATION

### bibliography_agent Output

18 precedent artworks + 9 theory/criticism sources + 6 artist statements/catalogues = 33 sources

Key sources include (ACM Reference Format; precedent works use venue/date locators, no fabricated DOIs):
- Harold Cohen. 1973–. *AARON* (autonomous drawing program). Documented across multiple exhibitions.
- Casey Reas. 2004. *Process / Software Structures*. Generative work + artist writings.
- Margaret A. Boden. 2010. *Creativity and Art: Three Roads to Surprise*. Oxford University Press.

### source_verification_agent Output

33 sources assessed: 28 Grade A-B, 4 Grade C, 1 Grade D (included with caveat — undated catalogue essay; flagged for currency)

## Phase 3: ANALYSIS

### synthesis_agent Output

**Comparative Matrix** (8 precedent works x 4 authorship strategies x 3 evidence types)

Works analyzed: *AARON* (Cohen), Cybernetic Serendipity systems, *Process* series (Reas), evolutionary/genetic art (Sims), bot/agent art, large-model generative art, the artist's own work, and one chance-based precedent (Cage-influenced).

**Key Findings**:

1. **Strategy spread, not convergence**: Across the lineage, authorship strategies span a spectrum from rule-author (the artist writes the system, owns every output) to relinquished-control (the artist sets initial conditions and accepts whatever emerges). *AARON* sits toward system-collaborator — Cohen authored a system whose outputs he still curated for decades — while chance-based precedents push toward relinquished control. There is no convergence on a single "correct" authorship posture; the lineage is defined by the *range* of positions.

2. **"Autonomy" is claimed more than it is evidenced**: Most precedent works assert autonomy in artist statements, but the observable evidence (does the system run unattended? does the artist select outputs?) frequently contradicts the claim. Works that curate outputs heavily are often described as "autonomous" — a precedence/capability claim that should be hedged or evidenced, exactly the kind flagged by the integrity gate.

3. **Documentation strategy mirrors authorship**: Artists who claim strong system-autonomy tend to document the *system* (code, rules, process); artists who curate tend to document *outputs* (selected images, installs). The documentation choice is itself an authorship signal.

4. **The framework's discriminating axis**: The strongest differentiator across works is *who selects the final output* — the artist, the system, or chance. This axis separates the lineage more cleanly than the medium or the era does.

5. **Positioning of the artist's own work**: The artist's work sits at system-collaborator with delegated selection — the system proposes, the artist sets constraints but does not hand-pick outputs. This position is under-occupied in the lineage and is the paper's contribution.

**Key Tension**: Catalogue essays frequently call older systems "autonomous," while critical theory reads the same works as heavily authored — the disagreement is explained by whose evidence is privileged (the artist's claim vs the observable selection process).

### devils_advocate_agent — CHECKPOINT 2

**Verdict**: PASS
- Major (downgraded from Critical): The selection of 8 precedent works needs stronger justification — why not include net.art or earlier algorithmic precedents?
- Minor: "Documentation mirrors authorship" is an assertion — anchor it to specific works' documentation

## Phase 4: COMPOSITION

### report_compiler_agent Output

**Title**: Who Selects? Positioning an Autonomous Generative Work Across the Authorship Spectrum of Generative Art

**Word Count**: 6,800 words

**Structure** (Practice-Based Art Paper, Pattern 1):
1. **Introduction / Context** (600 words): authorship as the live question in generative + AI art; the work in one paragraph
2. **Conceptual Framework** (1,200 words): theory of authorship and autonomy (Boden, Reas writings, distributed-agency theory); the lineage as positioning context, not a survey
3. **The Work** (900 words): form, what the system does, what the audience encounters; authorship & collaboration (system + artist + chance)
4. **Comparative Lineage Analysis** (the comparative move):
   - 4.1 Authorship-strategy matrix across 8 precedent works
   - 4.2 The autonomy-claim vs autonomy-evidence gap
   - 4.3 Documentation-as-authorship-signal
5. **Reflection / Discussion** (900 words): where the work sits and why that position contributes; exhibition & reception (named venue/date + observed detail)
6. **Conclusion / Future Work** (400 words)
7. **References** (33 sources, ACM Reference Format)

## Phase 5: REVIEW

### editor_in_chief_agent Output

**Verdict**: Accept with Minor Revision (Score: 4.1/5.0)
- Strength: Clear comparative framework; balanced treatment of the autonomy-claim gap
- Minor: The comparison matrix needs a notes column explaining work-specific nuances
- Minor: Finding #3 (documentation-as-signal) needs supporting anchors — currently assertion-based

### ethics_review_agent Output

**Verdict**: CLEARED
- AI-usage disclosure: present and accurate (two-channel)
- Citations + artwork/exhibition claims spot-checked: 7/33 (21%) verified — all confirmed or hedged
- Dual-use risk: Low
- Fair representation: Adequate — noted absence of non-Western and net.art precedents as a limitation
- Attribution: collaboration credit for the system's open-source components named correctly

### devils_advocate_agent — CHECKPOINT 3

**Verdict**: PASS
- Observation: Finding #1 (strategy spread) is the strongest claim but the chance-based precedent has the thinnest documentation — anchor or hedge
- "So what?" test: Passed — clear contribution: an under-occupied authorship position made legible
- Counterfactual check: What if the artist's "delegated selection" is indistinguishable in practice from curation? This alternative reading is not adequately addressed

## Phase 6: REVISION

### report_compiler_agent (Revision 1)

**Changes**:
1. Comparison matrix gains a notes column explaining work-specific nuances (Minor, Editor)
2. Finding #3 anchored to *AARON* and *Process*-series documentation specifics (Minor, Editor)
3. Discussion expanded to address the "delegated selection vs curation" counter-reading (Observation, Devil's Advocate)
4. Precedent-work selection justified in the Comparative section — explicit inclusion criteria added; net.art and earlier algorithmic precedents acknowledged as excluded with rationale (Major, Devil's Advocate from Checkpoint 2)

**Final Word Count**: 6,800 words
**Revision Loops Used**: 1 of 2

---

## Final Output Summary
- Full synthesis report (Practice-Based Art Paper, Pattern 1): 6,800 words
- 33 cited sources (precedent works with venue/date locators + theory in ACM Reference Format)
- 8-work comparative authorship matrix
- 5 key findings
- The artist's work positioned at an under-occupied point in the authorship spectrum
- Ethics cleared (two-channel AI-usage disclosure)
- 1 revision loop completed
