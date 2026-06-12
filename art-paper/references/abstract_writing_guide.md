# Abstract Writing Guide

Used by `abstract_agent`.

## Abstract Types

### Structured Abstract
Contains explicit labeled sections. Required by many journals in social sciences and medicine.

**Sections**: Background, Purpose/Objective, Method, Results/Findings, Conclusion/Implications

### Unstructured Abstract
A single flowing paragraph without labels. Common in humanities and some social sciences.

**Flow**: Context → Problem → Purpose → Method → Key Findings → Implications

### Extended Abstract
Longer (500-1,000 words), used for conference submissions. May include brief literature review and preliminary results.

## English Abstract Guidelines

### Word Count
- Standard: 150-250 words (check journal requirements)
- Conference: 200-500 words (check CFP)
- Dissertation: up to 350 words

### Structure (5-Component Model)

#### Component 1: Background (1-2 sentences)
Establish context and identify the problem.

**Patterns**:
- "[Topic] has become increasingly important because..."
- "Despite growing interest in [topic], little is known about..."
- "Recent developments in [field] have raised questions about..."

**Avoid**:
- Starting with "This paper..." (too abrupt)
- Generic statements ("Education is important")
- Overly long historical context

#### Component 2: Purpose (1 sentence)
State the specific objective or research question.

**Patterns**:
- "This study examines [what] in [context]."
- "The purpose of this research is to [verb] [object]."
- "This paper proposes [framework/model] for [application]."

#### Component 3: Method (1-2 sentences)
Describe the approach, data, and analysis.

**Patterns**:
- "Using [method], this study analyzed [data] from [source]."
- "A [design] approach was employed, involving [participants/data]."
- "Data were collected through [instrument] and analyzed using [technique]."

#### Component 4: Findings (2-3 sentences)
Present the key results — be specific.

**Patterns**:
- "The results indicate that [finding 1]. Additionally, [finding 2]."
- "Three key findings emerged: (a) [finding 1], (b) [finding 2], and (c) [finding 3]."
- "The analysis revealed [main finding], with [specific metric/detail]."

**Include**:
- Specific numbers when available (percentages, effect sizes)
- The most important findings (not all findings)

**Avoid**:
- "Results will be discussed" (the abstract IS the discussion)
- Vague findings ("significant results were found")

#### Component 5: Implications (1-2 sentences)
State the significance, practical implications, or recommendations.

**Patterns**:
- "These findings have implications for [practice/policy/theory]."
- "The results suggest that [stakeholders] should [action]."
- "This research contributes to [field] by [contribution]."

### Example (English, Practice-Based Art Paper)

> Generative installation increasingly invites the audience to co-author the work, yet the felt experience of that authorship is rarely examined in the work's own terms. This paper presents *Tide Memory*, an autonomous audiovisual installation that listens to visitors' breath through an array of contact microphones and composes a slowly evolving tidal soundscape and projected light field from the aggregated breathing of everyone present. Developed over 14 months of studio iteration and exhibited for six weeks at the [Example] Media Art Biennale (2025), the work was studied through a practice-based methodology and situated observation. Across 60 logged gallery sessions and 18 visitor conversations, field notes recorded a recurring shift: once visitors became aware the work tracked breathing, many moved from a "performing" stance (testing for a gesture mapping) to a "settling" stance (slowing down, standing still). Some visitors expressed unease at the work sensing an intimate, involuntary act. The paper argues that co-authorship of a generative work keyed to involuntary physiology is felt as surrender rather than command, and that the timing of disclosure — when the audience learns what is sensed — is itself an artistic material that determines whether the work reads as wonder or as surveillance.
>
> **Keywords**: generative art, interactive installation, embodied interaction, co-authorship, media art

## Keywords Selection

1. **Core concepts** — main variables or constructs (2-3)
2. **Context** — geographical, institutional, or temporal (1-2)
3. **Method** — if distinctive (0-1)
4. **Field** — discipline or sub-field (1)

**Rules**:
- Lowercase (unless proper nouns)
- Complement the title (don't repeat title words verbatim)
- Use established terms (check the venue's keyword list if available)
- 4-6 keywords (Pattern 1 default; see `art-paper/agents/abstract_agent.md` for per-pattern targets)

## Abstract Quality Checklist

| Check | ✓ |
|-------|---|
| Covers all 5 components (work / provocation / making / insight / contribution) | |
| Word count within target (120-200 for Pattern 1; up to 300 for Pattern 5) | |
| Keywords: 4-6 (Pattern 1); 3-5 for Pattern 2 | |
| Keywords complement (not duplicate) the title | |
| No citations in the abstract | |
| No abbreviations undefined in the abstract | |
| No reception inflation ("widely acclaimed", "audiences were moved") without an observable anchor | |
| Medium label is honest (no "autonomous" for a scripted sequence; no "generative" for non-realtime) | |

> art-paper v0.1 ships English-only paper output. The bilingual-abstract machinery is inherited from ARS but is not the v0.1 default; verify language requirements against the current SIGGRAPH Asia Art Papers / ACM CFP.
