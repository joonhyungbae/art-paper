# Example: Precedent-Works + Theory Review (lit-review mode)

> Demonstrates the lit-review pipeline. For practice-based art research the "literature"
> is **precedent artworks + theory/criticism**, not an empirical evidence base. The
> PRISMA-style flow and source-grading mechanics are preserved; the domain is art.
> (The full PRISMA systematic-review apparatus is reserved for Pattern 5 / art-science
> hybrids — see `shared/references/art_paper_structure_patterns.md`.)

## User Request
```
Review the precedent works and theory on interactive installations that use the
viewer's biometric signals (heartbeat, breath) as input
```

**Mode**: `lit-review` (bibliography_agent + source_verification_agent + synthesis_agent)

## bibliography_agent Output

### Search Strategy

**Sources**: ACM Digital Library (SIGGRAPH / SIGGRAPH Asia Art Papers), *Leonardo*, art-criticism databases, exhibition catalogues, museum/festival archives (Ars Electronica, ZKM), and primary artwork documentation
**Keywords**:
- Primary: "biometric art" OR "biofeedback installation" OR "heartbeat" OR "breath" OR "physiological input"
- Combined with: "interactive installation" OR "participatory art" OR "embodiment" OR "affective interface"
- Filters: documented works + peer-reviewed art papers + catalogue essays; precedent artworks treated as primary lineage evidence

**PRISMA-style flow** (adapted as a transparent screening trail, not an empirical evidence base):
```
Records identified: 412
├── ACM DL (SIGGRAPH/SA Art Papers): 96
├── Leonardo + art-theory databases: 121
├── Festival/museum archives (Ars Electronica, ZKM): 138
└── Catalogues + artist sites: 57

Duplicates removed: 88
Records screened (title/abstract/work description): 324
Records excluded: 256
  - Not biometric input (other sensing): 121
  - Not an artwork (pure HCI study): 74
  - Opinion/press only, no work documented: 41
  - Inaccessible documentation: 20
Full records assessed: 68
Excluded: 31
  - Insufficient work documentation: 16
  - Biometrics used in product, not art context: 9
  - Duplicate documentation of same work: 6
Works/sources included in synthesis: 37
```

### Annotated Bibliography (selected entries — ACM Reference Format)

1. **Precedent work** — Lygia Clark. 1960s. *Relational Objects* (incl. breath-based works). MoMA / exhibition documentation (venue/date locator; no DOI).
   - Relevance: Pre-digital precedent for using the body's involuntary signals in participatory art
   - Lineage note: grounds embodiment without computation — useful counterpoint to sensor-driven work
2. **Theory** — Mark B. N. Hansen. 2006. *Bodies in Code: Interfaces with Digital Media*. Routledge.
   - Relevance: Theorizes the body as the interface; directly frames biometric-input art
   - Use: conceptual framework, §embodiment
3. **Precedent work + art paper** — George Khut. 2012. *The Heart Library / BrightHearts* (heart-rate biofeedback artwork). Documented in art-paper venues and exhibitions.
   - Relevance: Closest contemporary precedent using heartbeat as input
   - Contribution gap: foregrounds therapeutic framing — leaves room for a non-therapeutic provocation

[... 34 more sources — precedent artworks (venue/date locators) + theory/criticism (ACM Reference Format) ...]

## source_verification_agent Output

### Source Quality Matrix

| Grade | Count | % |
|-------|-------|---|
| A | 6 | 16% |
| B | 14 | 38% |
| C | 11 | 30% |
| D | 5 | 14% |
| F | 1 | 3% |

**Flagged**:
- Source #22: Catalogue essay asserts a precedence claim ("first artwork to use live heartbeat") with no verifiable locator -> Excluded (treated like an unverifiable citation)
- Source #31: Artist statement claims a "fully autonomous biofeedback system" -> capability claim noted, included with caveat (hedge required downstream)
- Sources #8, #15, #29: Pre-2010 documentation may not reflect current sensor practice -> Currency caveat

**Final included**: 37 sources (1 excluded for an unverifiable precedence claim)

## synthesis_agent Output

### Lineage / Theme Matrix (condensed)

| Theme | Works/Sources For | Against / Critical | Contested | Strength |
|-------|------------------|--------------------|-----------|----------|
| Biometrics as intimacy/affect | 9 | 3 | 2 | Moderate |
| Involuntary signal vs deliberate gesture | 7 | 2 | 1 | Moderate-Strong |
| Therapeutic vs critical framing | 11 | 2 | 1 | Strong |
| Privacy/consent of bodily data | 8 | 4 | 3 | Contested |
| Autonomy claims of the system | 6 | 5 | 2 | Contested |

### Synthesis Narrative

**Theme 1: The Therapeutic-vs-Critical Split Defines the Lineage** (Strong)
The clearest pattern across the corpus is that biometric-input artworks cluster into a *therapeutic* framing (the work helps the viewer regulate or attend to their own body — e.g. Khut's heart-rate works) and a *critical* framing (the work exposes the surveillance and commodification of bodily data). Eleven of 37 sources address this split, with near-universal agreement that it is the lineage's defining axis (Hansen 2006; Khut 2012). A new work must choose, or deliberately hold, a position on this axis.

**Theme 2: Involuntary Signal as Aesthetic Material** (Moderate-Strong)
Works that use *involuntary* signals (heartbeat, breath) are read differently from those using deliberate gesture — the involuntary signal carries an authenticity and vulnerability that deliberate input lacks. Clark's pre-digital breath works and contemporary heartbeat installations share this, despite different media.

**Theme 3: Privacy and Consent Are Contested** (Contested)
The corpus is split on whether biometric-input art ethically requires explicit consent and data handling akin to research, or whether the gallery frame implies consent. Critics warn that capturing bodily data — even ephemerally — reproduces the logics the critical works claim to oppose. The resolution appears context-dependent: ephemeral, non-stored signals raise fewer concerns than recorded ones.

**Theme 4: Intimacy and Affect** (Moderate)
Many works claim to produce intimacy or heightened affect, but reception is rarely documented with observable anchors — most claims rest on the artist's assertion rather than a named venue/date + observed detail. This is a documentation gap, not a settled finding.

**Theme 5: System-Autonomy Claims Outrun Evidence** (Contested)
Several works describe "autonomous" or "responsive" systems whose actual behavior, on inspection of the documentation, is simple signal-to-output mapping. The capability claim frequently exceeds the evidenced realization — a pattern the integrity gate flags for hedging.

### Discourse Gaps
1. **Documented reception**: Almost no works document audience response with observable anchors
2. **Non-Western lineage**: 84% of documented works are Euro-American
3. **Non-therapeutic, non-surveillance framings**: the axis is dominated by two poles; a third framing is under-explored
4. **Ephemeral-data ethics**: little practice-based discussion of consent for non-stored bodily signals

### Contradictions
| Claim A | Claim B | Assessment |
|---------|---------|-----------|
| Biometric art deepens intimacy (9 sources) | Biometric art reproduces surveillance (4 sources) | Context-dependent: framing + whether data is stored |
| Systems are "autonomous/responsive" (6 sources) | Behavior is simple signal mapping (5 sources) | Evidence-dependent: claim often outruns documented realization |

---

## Final Output
- Annotated bibliography: 37 sources (precedent works with venue/date locators + theory in ACM Reference Format)
- Lineage/theme matrix: 5 themes x 37 sources
- Synthesis narrative: ~3,200 words
- 4 discourse gaps identified
- 2 major contradictions analyzed
- Evidence-anchoring assessment per theme (work / theory / reception)
