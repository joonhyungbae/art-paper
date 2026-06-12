---
scenario: Reviewing a draft contribution/positioning passage for an art paper
mode: review
agents_used:
  - editor_in_chief_agent
  - ethics_review_agent
  - devils_advocate_agent
input: User provides an approximately 300-word contribution + reception passage from a practice-based art paper
output: Complete reports from three review agents + revision recommendation summary
---

# Review Mode Example: Art-Paper Contribution Passage Review

This example demonstrates the complete workflow of `review` mode. The user provides a previously written passage from a practice-based art paper (its contribution claim plus reception), and art-inquiry activates three review agents for multi-dimensional review against the art-research evidence model.

---

## User Request

```
Please use review mode to review the following passage from my art paper:

"This installation is the first artwork to translate live ocean-acidification data
into a walk-through generative soundscape, and in doing so it makes climate harm
viscerally felt in a way data visualization never could. Three buoy sensors stream
pH readings to a fully autonomous system that composes the sound in real time and
never produces the same composition twice. The work advances generative
environmental art by proving that sonification is more affective than visualization.
When the piece premiered, audiences were profoundly moved — many stood in silence,
and several were moved to tears, demonstrating the work's emotional power. Critics
hailed it as a landmark. The contribution is therefore twofold: a technical
breakthrough in real-time autonomous sonification, and an empirical demonstration
that sound outperforms image for environmental affect. Future artists working on
climate themes should adopt sonification over visualization, since this work has
shown it to be the more effective medium for moving audiences to act."
```

---

## Review Pipeline Activation

**Mode Detection**: User explicitly requests `review mode` and provides text to be reviewed. Activating 3 review agents:

1. `editor_in_chief_agent` — Art-paper argument quality and positioning review
2. `ethics_review_agent` — Integrity, attribution, and disclosure review
3. `devils_advocate_agent` — Counter-arguments and challenges

---

## editor_in_chief_agent Review Report

### Review Summary

| Dimension | Score | Description |
|------|------|------|
| Originality / contribution | 3/5 | A genuine work, but the contribution is framed as a proof rather than an artistic provocation |
| Rigor of evidence anchoring | 1/5 | Precedence, capability, and reception claims are all unanchored |
| Argument coherence | 2/5 | Slides from a practice-based contribution into an empirical proof the work cannot support |
| Positioning vs precedent | 2/5 | Cites no precedent works; the lineage of data sonification is ignored |
| Writing quality | 4/5 | Fluent and vivid, though the vividness inflates the claims |
| **Overall** | **2.4/5** | **Recommend Major Revision** |

### Sentence-by-Sentence Review

> "the first artwork to translate live ocean-acidification data into a walk-through generative soundscape"

Review comment: A precedence claim ("the first") with no citation and no hedge. Data sonification of environmental data has a documented lineage; an exhaustive "first" is unprovable. Either cite the closest precedents and state the precise differentiator, or hedge to "to the author's knowledge."

> "makes climate harm viscerally felt in a way data visualization never could"

Review comment: A comparative affective claim asserted without evidence. The work cannot establish what "data visualization never could." Reframe as the work's *intent* or *provocation*, not a demonstrated fact.

> "a fully autonomous system that composes the sound in real time and never produces the same composition twice"

Review comment: Bundled technical/capability claims. "Fully autonomous," "real time," and "never repeats" each need a realization anchor (system description, latency, output-space size / deduplication). As written, the claim outruns the documented realization.

> "proving that sonification is more affective than visualization … an empirical demonstration that sound outperforms image"

Review comment: This is the central error. A single practice-based artwork is *situated evidence*, not an empirical proof of a general claim across media. The art-research evidence model rewards honest specificity and punishes over-generalization. Down-scope to what this work revealed in its context.

> "audiences were profoundly moved — many stood in silence, and several were moved to tears … Critics hailed it as a landmark."

Review comment: Reception inflation. "Profoundly moved," "moved to tears," "critics hailed" need observable anchors: named venue/date, observed/recorded detail, and citable press. "Stood in silence" is observable and usable; the emotional attributions and the uncited "critics hailed" are not.

> "Future artists … should adopt sonification over visualization"

Review comment: A prescriptive generalization resting on the unsupported proof above. Remove or recast as an open question for the field.

### Editorial Verdict

**Verdict: MAJOR REVISION**

Core issues:
1. Precedence, technical, and reception claims are unanchored throughout
2. A situated practice-based contribution is mis-framed as an empirical, generalizable proof
3. No precedent works cited; the sonification lineage is ignored
4. Prescriptive conclusion exceeds what the work can support

---

## ethics_review_agent Review Report

### Integrity Review Summary

| Dimension | Verdict | Description |
|------|------|------|
| AI-usage disclosure | CONDITIONAL | Two-channel disclosure (AI in making vs AI in writing) not addressed in this passage |
| Attribution / collaboration credit | CONDITIONAL | "Three buoy sensors" — data source and any collaborators/engineers not credited |
| Exhibition/award faithfulness | CONDITIONAL | "Critics hailed," "landmark" — no citable press or venue/date |
| Reception integrity | CONDITIONAL | Affective reception asserted without observable anchor |
| **Overall Verdict** | **CONDITIONAL** | **Needs anchoring + crediting to pass** |

### Item-by-Item Analysis

**1. Reception integrity (anchoring)**

> "audiences were profoundly moved … several were moved to tears, demonstrating the work's emotional power"

Per the art-research evidence model, reception claims require a named venue/date plus an observable, recorded detail. "Stood in silence" is observable; "profoundly moved," "tears," and "emotional power" are unanchored inferences and must be down-scoped or supported with collected responses (quoted, attributed).

**2. Attribution and collaboration credit**

The live data feed comes from buoy sensors (presumably a third-party monitoring network), and a real-time audio system implies technical collaboration. The passage credits neither. Collaboration credit must be named, and the data source acknowledged with any usage rights.

**3. Disclosure**

If AI tools contributed to composing the soundscape or to writing the paper, both channels must be disclosed per the SIGGRAPH Asia / ACM two-channel policy (verify against the current CFP).

### Integrity Verdict

**Verdict: CONDITIONAL**

Conditions for passing:
1. Anchor or remove all reception claims (keep observable details only)
2. Name collaborators and credit the buoy-data source + usage rights
3. Add two-channel AI-usage disclosure
4. Cite or remove the "critics hailed / landmark" claim

---

## devils_advocate_agent Review Report

### Counter-Argument Challenges

**Challenge 1: Does one artwork prove sound "outperforms" image?**

Original claim:
> "proving that sonification is more affective than visualization"

Counter-argument: A single situated work cannot establish a cross-medium general law. There is no control, no comparison condition, no measurement — and that is *fine*, because this is a practice-based art paper, not an experiment. The error is claiming empirical proof. Recast as: "in this installation, sonification opened an affective register that the artist's earlier visualization work did not" — a situated, defensible claim.

**Challenge 2: Is the system actually "fully autonomous"?**

Original claim:
> "a fully autonomous system that composes the sound in real time and never produces the same composition twice"

Counter-argument: "Fully autonomous" usually means "the artist authored the rules and chooses not to intervene live" — that is authored autonomy, not absence of authorship. And "never repeats" is rarely strictly true without a very large output space and deduplication. State the realization precisely instead of reaching for the strongest words.

**Challenge 3: The aestheticization problem is unaddressed.**

Counter-argument: Turning ocean acidification into a beautiful, moving soundscape risks the very critique leveled at environmental art — that it consoles rather than mobilizes. The passage treats "moving audiences to tears" as a success metric, but a critic could read tears as catharsis that *defuses* action. The work should hold this tension, not claim victory over it.

**Challenge 4: "Should adopt sonification over visualization" is an overreach.**

Counter-argument: This prescription tells the entire field what medium to use based on one work. Even if the situated insight is real, the generalization is not earned. Reduce to an open question: "whether sonification generalizes beyond this work is an open question for the field."

### Challenge Summary

| Challenge | Severity | Recommendation |
|------|--------|------|
| "Proves sound outperforms image" | Critical | Recast as situated insight; remove empirical-proof framing |
| "Fully autonomous / never repeats" | High | State the realization precisely; hedge capability |
| Aestheticization tension ignored | Medium | Address the consolation-vs-mobilization critique |
| Prescriptive medium generalization | Medium | Reduce to an open question |

---

## Revision Recommendation Summary

### Consensus Issues Across All Three Agents

The following issues were raised by all three review agents:

1. **Unanchored claims**: precedence ("first"), technical ("fully autonomous", "real time", "never repeats"), and reception ("moved to tears", "critics hailed") all need an anchor or a hedge
2. **Genre mis-framing**: a situated practice-based contribution is dressed up as an empirical, generalizable proof
3. **Over-generalization**: the prescriptive conclusion exceeds what one work can support

### Priority Revision Items (by severity)

| Priority | Revision Item | Source |
|--------|----------|------|
| 1 | Remove the "proves sound outperforms image" empirical-proof framing; recast as situated insight | editor + devil's advocate |
| 2 | Anchor or remove all reception claims (keep "stood in silence"; drop "tears"/"profoundly moved"); cite or drop "critics hailed" | editor + ethics + devil's advocate |
| 3 | State the technical realization precisely; hedge "fully autonomous" / "never repeats" | editor + devil's advocate |
| 4 | Hedge or cite the "first artwork" precedence claim; cite the sonification lineage | editor |
| 5 | Name collaborators, credit the buoy-data source + rights, add two-channel AI-usage disclosure | ethics |
| 6 | Address the aestheticization (consolation-vs-mobilization) tension | devil's advocate |
| 7 | Reduce the "should adopt sonification" prescription to an open question | devil's advocate |

### Revised Passage Suggestion (for reference)

> "This installation translates live ocean-acidification data from three monitoring buoys (data courtesy of [network], used with permission) into a walk-through generative soundscape. Building on the lineage of environmental data sonification [cite precedents], it asks whether sound can open an affective register that the artist's earlier data-visualization work did not. The system, whose composition rules the artist authored, runs unattended and generates sound in real time (under [X] ms on [hardware]) from an output space large enough that repeats were not observed over the exhibition run. At its premiere ([venue, date]), many visitors stood still for the full duration and several returned more than once. The work does not claim that sound is generally more powerful than image — that remains an open question for the field; rather, it offers a situated account of what this sonification revealed, while holding open the risk that an affecting soundscape may console as much as it mobilizes. AI tools were used in [making / writing] as disclosed in the Acknowledgements."
