# Practice-based research

Practice-based art research holds a 30-year claim that information science should attend to: **the artist knows things from the making that the documentation alone cannot transfer.**

## The lineage

| Source | What they articulate |
|---|---|
| **Polanyi (1966)**, *The Tacit Dimension* | "We can know more than we can tell." Tacit knowledge sits beneath explicit description. |
| **Schön (1983)**, *The Reflective Practitioner* | Reflection-in-action: the running practice continuously makes judgements answerable to itself. The judgement does not exist independent of the doing. |
| **Frayling (1993)**, *Research in art and design* | A three-way distinction — research **into**, **for**, and **through** art. Practice-based work is "research through". |
| **Candy (2006)**, *Practice Based Research: A Guide* | Operationalises a doctoral framework for PBR: the creative outcome forms part of the contribution to knowledge. |
| **Borgdorff (2012)**, *The Conflict of the Faculties* | Defends artistic research's epistemic standing in academia. Distinguishes knowing-in-the-doing from knowing-about-the-doing. |
| **Nelson (2013)**, *Practice as Research in the Arts* | Argues for validity criteria internal to practice rather than imported from social science. |
| **Haseman (2006)**, *A Manifesto for Performative Research* | Practice as a distinct research paradigm; outputs are themselves the research, not its evidence. |

## What this means for the plugin

If practice-formed knowledge does not fully transfer through documentation, then a copilot that has only documentation cannot fully reconstruct the artist's reading. The plugin is designed around this gap:

- **The skill cannot author the artist's reading.** It can scaffold sections, surface references, audit citations, but the provocation and reflection sections require the artist's authorship.
- **The per-layer instrument distinguishes two types of layers.** Documentable layers (cited prior work, factual description of the work, exhibition record) are expected to converge when an AI rebuilds from inputs. Generative layers (provocation, reflection, situated interpretation) are expected to diverge.
- **The instrument does not test AI's capability for creativity.** It tests whether, in a specific corpus, the documentable-versus-generative split is detectable.

## What this does NOT mean

This plugin's stance is **not** that AI fundamentally lacks something humans have. The plugin acknowledges that:

- A critic who has not made the work also lacks the practice, but can produce a coherent reading legitimately
- An AI that has read the documentation can do something a reader may legitimately do (advance an interpretation)
- The plugin's claim is narrower: AI cannot reproduce the *specific reading the artist authored* from documentation alone

This is a measurement claim about reconstruction, not a metaphysical claim about creativity.

## Where it appears in the plugin

- `art-inquiry full` mode produces a **Practice-Based Methodology Blueprint** that explicitly maps the work / documentation / writing / reception as triangulating evidence per PBR norms
- `art-paper` skill enforces that provocation and reflection sections are marked as artist-authored
- `art-reviewer` Practitioner-Researcher role checks that the artist's authorial position is preserved
- The companion paper documents the methodology's grounding in PBR theory in §1 and §5
