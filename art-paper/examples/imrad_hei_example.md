# Art-Science Hybrid (IMRaD-leaning) Example — Interactive Installation

This example demonstrates a complete Pattern 5 (art-science hybrid) structure for a practice-based art paper whose contribution is both an artwork and a technical/observational one. It shows how each agent's output integrates into the final paper. IMRaD survives in art-paper only as Pattern 5 — use it when there is a genuine system/realization contribution alongside the artistic one; otherwise prefer Pattern 1 (Practice-Based Art Paper).

> **This is an AI-generated demonstration output.** All authors, venues, works, and observations are fictional. Cited references (titles, authors, DOIs, exhibition venues) are AI-generated, unverified, and may not exist. Do not cite this document as a scholarly source.

---

# Tide Memory: An Autonomous Generative Installation that Composes from Visitors' Breath, and What Its Exhibition Revealed about Embodied Co-Authorship

**Author:** [Example Artist]
**Affiliation:** [Example] Studio for Media Art, [Example Institute]
**Date:** 2026

---

## Abstract

Generative installation art increasingly invites the audience to become a co-author of the work, yet the felt experience of that authorship is rarely examined in the work's own terms. This paper presents *Tide Memory*, an autonomous audiovisual installation that listens to the breath of visitors through an array of contact microphones and synthesizes a slowly evolving tidal soundscape and projected field of light from the aggregated breathing of everyone present. The work was developed through 14 months of studio iteration and exhibited for six weeks at the [Example] Media Art Biennale (2025). Drawing on a practice-based methodology and situated observation of the exhibition, this paper reports how visitors negotiated authorship of a work that responds to an involuntary bodily act. Observation of 60 logged gallery sessions and 18 visitor conversations indicated that visitors who became aware that the work tracked breathing tended to shift from a "performing" stance to a "settling" stance, and reported the work as calming rather than as a system to be controlled. Some visitors expressed unease at the work sensing an intimate, involuntary act. These findings suggest that generative works keyed to involuntary physiology produce a distinct register of co-authorship — one of surrender rather than command — and that the design of disclosure (when and how the audience learns what is being sensed) is itself an artistic material. The paper contributes the work, an account of its autonomous generative system, and a situated reading of embodied co-authorship in interactive installation.

**Keywords**: generative art, interactive installation, embodied interaction, co-authorship, soundscape, media art

---

## 1. Introduction

### 1.1 Context and Background

Over the past two decades, interactive and generative installation has moved the audience from the position of viewer to that of participant, and in many cases co-author of the work [Edmonds 2018; Bishop 2012]. Where early interactive works responded to deliberate gestures — touch, position, voice command — a more recent strand responds to involuntary or barely-conscious bodily signals: heartbeat, gaze, galvanic skin response, breath [Schiphorst 2021]. Such works raise a question that is artistic before it is technical: when a work composes itself from something you do not consciously control, in what sense are you its author?

*Tide Memory* sits in this strand. It is an autonomous generative installation that senses the breathing of everyone in the gallery and composes a continuous tidal soundscape and a projected field of light from the aggregate. No visitor controls the work; no single breath is legible in the output. The work was made to hold a specific provocation: that co-authorship of a generative artwork can be an act of surrender rather than command.

### 1.2 Problem Statement

The discourse on interactive art has tended to frame audience agency in terms of control and feedback legibility — does the participant understand how their action maps to the work's response [Costello and Edmonds 2019]. This framing fits gesture-driven work but is ill-suited to work keyed to involuntary physiology, where legibility may be undesirable and where the relevant experience may be one of relinquishing rather than exercising control. The felt texture of that experience, and how it forms during an actual exhibition, remains under-described in the practice-based literature.

### 1.3 Research/Inquiry Questions

This paper pursues three questions, in the situated, non-generalizing sense appropriate to practice-based art research:

1. **Q1**: How does an autonomous generative system keyed to visitors' breath function as an artwork — what does it do, and how is it made?
2. **Q2**: How did visitors negotiate authorship of a work that responds to an involuntary bodily act, as observed during its exhibition?
3. **Q3**: What did the design of disclosure (when and how visitors learned what was sensed) contribute to the experience?

### 1.4 Significance

This paper contributes to the discourse on embodied interaction in media art by reporting from an actual six-week exhibition rather than a lab study, and by treating the artwork itself — not a population of users — as the primary evidence for its claims.

---

## 2. Related Work

### 2.1 Conceptual Lineage and Positioning

This work positions itself within three overlapping bodies of practice. First, biosignal-driven installation, where the artwork is composed from a participant's body rather than their deliberate input. Lozano-Hemmer's *Pulse* series [Lozano-Hemmer 2007–2018] established heartbeat as a material that is simultaneously intimate and anonymizable in aggregate; *Tide Memory* extends this to breath, which differs from heartbeat in being partly volitional — a visitor can, but usually does not, control it. This volitional ambiguity is the conceptual hinge of the present work and distinguishes it from purely involuntary biosignal pieces.

Second, the lineage of ambient and slow generative sound, from Eno's generative music [Eno 1996] to recent gallery soundscapes, where the work's refusal to respond instantly is itself expressive. *Tide Memory* deliberately responds on the timescale of tides — minutes, not milliseconds — so that no visitor can perceive a tight action-response loop. This is a direct artistic rejection of the feedback-legibility paradigm described by Costello and Edmonds [2019].

Third, theory of audience co-authorship and participation. Bishop's [2012] critique of participatory art and Edmonds's [2018] taxonomy of interactive art frame the question of where authorship sits. Schiphorst's [2021] work on somatic and felt interaction provides the vocabulary — "attending to the body," "first-person experience" — that the present work mobilizes as a design stance rather than an evaluation method.

### 2.2 Technical Prior Art

On the realization side, the work draws on established techniques in contact-microphone sensing, real-time audio synthesis, and aggregate signal processing. Breath detection from contact microphones is well documented in the music-technology literature [Author A and Author B 2022], typically for single performers; the contribution here is not the detection of one breath but the robust aggregation of many noisy, overlapping breath signals into a single compositional driver, in an uncontrolled gallery acoustic. Prior gallery-scale biosignal installations have generally sensed visitors one at a time at a station [Author C 2020]; *Tide Memory* senses the whole room continuously, which is a meaningful difference in both the technical approach and the resulting experience of anonymity.

---

## 3. The Work / System Design

### 3.1 What the Visitor Encounters

The visitor enters a darkened 8 × 10 m gallery. Twelve slim columns, each holding a contact microphone and a thin vertical LED element, stand around the perimeter. A low, layered soundscape — resembling a distant tide — fills the room, and a field of pale blue-green light washes slowly across the floor and walls. As visitors move and breathe, the soundscape and light field shift over minutes: denser and lower when the room is full and breathing is shallow and fast, sparser and higher when the room is calm or empty. No instructions are posted at the entrance. A single wall text, encountered only on exit, states that the work composed itself from the breathing of everyone who was in the room.

### 3.2 System Architecture

The autonomous generative system comprises three layers:

- **Sensing**: 12 contact microphones capture low-frequency air movement and bodily vibration. A per-channel band-pass filter and onset detector estimate breath events; the system does not attempt to attribute a breath to a specific person.
- **Aggregation**: breath-event rates and estimated depth are pooled across channels into two slowly-smoothed room-level parameters — *density* and *agitation* — updated on a 90-second moving window. This long window is an artistic decision, not only a technical one: it guarantees that no visitor can perceive their own breath in the output.
- **Composition**: a generative audio engine maps *density* and *agitation* onto the layering, pitch register, and tidal period of the soundscape, and onto the brightness and drift speed of the light field. The mapping is autonomous and runs continuously; there is no operator and no fixed timeline.

### 3.3 Authorship and Collaboration

The work was conceived and authored by [Example Artist]. The breath-aggregation signal processing was developed in collaboration with [Example Collaborator], audio engineer, whose contribution to the aggregation method is acknowledged and is co-credited in the work's exhibition label. Fabrication of the columns was carried out with [Example Fabrication Studio]. All creative and compositional decisions were made by the author.

---

## 4. Implementation / Method

### 4.1 Realization Approach

The system was implemented over 14 months across roughly 40 studio iterations, documented in a running process journal and version history. Audio synthesis and mapping were built in a real-time audio environment; the sensing and aggregation layer ran on a dedicated machine driving the column array. The 90-second aggregation window was arrived at empirically in the studio: shorter windows let attentive visitors "play" the work, which the author judged to break the intended register of surrender; longer windows made the room feel unresponsive.

### 4.2 Situated Observation Protocol

To address Q2 and Q3, the exhibition was treated as the site of inquiry. Observation was situated and qualitative, framed as practice-based reflection rather than a controlled study; no claim of statistical generalization is made. Three sources were triangulated:

- **Session logs** (n = 60): anonymized room-level parameter logs paired with the author's structured field notes for 60 gallery sessions across the six-week run.
- **Visitor conversations** (n = 18): brief, consenting post-visit conversations at the exit, recorded as notes.
- **Process record**: the studio journal and version history, used to ground claims about intent and realization.

### 4.3 Analysis

Field notes and conversation notes were read thematically following a reflexive practice-based approach [Author D and Author E 2023], with the artwork and its documentation as the primary evidence and the conversations as corroboration. No inter-rater reliability or effect-size apparatus is reported, as none is appropriate to a situated single-work inquiry.

---

## 5. Exhibition Findings

### 5.1 Stances Visitors Took Toward the Work (Q2)

Field notes across the 60 logged sessions described two recurring stances. Before any awareness that breath was sensed, many visitors adopted what the notes call a *performing* stance — moving deliberately, waving, in a few cases speaking to the columns — apparently testing for a gesture-response mapping and finding none. Visitors who came to suspect or learn that the work tracked breathing more often shifted to a *settling* stance: standing still, breathing more slowly, several lying on the floor. This shift, where observed, was the most consistent pattern in the notes.

**Table 1**

*Observed Visitor Stances by Awareness (situated counts from field notes, not a controlled measure)*

| Field-note observation | Before awareness of breath-sensing | After awareness of breath-sensing |
|---|:---:|:---:|
| Performing / testing for control | frequent | rare |
| Settling / slowing down | rare | frequent |
| Left within ~1 minute | occasional | occasional |

Counts are the author's situated tallies and are reported as documentation of the exhibition, not as evidence of a population-level effect.

### 5.2 What the Conversations Surfaced (Q2, Q3)

Of 18 exit conversations, a recurring theme was that learning the work composed from breath reframed the visit retrospectively — several visitors said they wished they had known earlier, while others valued discovering it only on exit. One visitor remarked, in notes: "I spent the first while trying to make it do something. Then I gave up, and that's when it got beautiful." This account aligns with the *settling* stance in the field notes and with the work's intended register of surrender.

Some visitors expressed unease. Three conversations recorded discomfort at the work sensing an intimate, involuntary act without prior notice. This is reported as an honest finding, not minimized: it bears directly on the ethics and the design of disclosure (Q3).

### 5.3 Disclosure as Artistic Material (Q3)

The decision to place the only explanatory text at the exit — so that visitors first encountered the work without knowing what it sensed — shaped the experience in ways the field notes make visible. Discovery on exit produced, for many, a retrospective re-reading of their own visit; for a few, it produced the unease above. The finding is that *when the audience learns what is being sensed* is not a neutral curatorial detail but a compositional choice that determines whether the experience reads as wonder or as surveillance.

---

## 6. Discussion

### 6.1 Summary

*Tide Memory* functioned as intended as an autonomous generative work, and its exhibition revealed a distinct register of co-authorship: visitors authored the work not by commanding it but by inhabiting the room and, often, by relinquishing the attempt to control it.

### 6.2 Interpretation: Co-Authorship as Surrender

The shift from *performing* to *settling* speaks directly to the discourse on audience agency. Where the feedback-legibility paradigm [Costello and Edmonds 2019] treats understanding the action-response mapping as the route to agency, this work suggests an inverse route for physiology-keyed pieces: agency is felt precisely when the visitor stops seeking a legible mapping and accepts an aggregate, anonymous authorship. This resonates with Schiphorst's [2021] somatic framing and extends the biosignal lineage of Lozano-Hemmer's *Pulse* [2007–2018] by foregrounding breath's volitional ambiguity — the fact that one *could* control it makes the choice not to a meaningful artistic act.

### 6.3 The Ethics and Craft of Disclosure

The unease some visitors reported is not a failure to be smoothed over but a finding about the material of disclosure. Sensing an involuntary, intimate act carries an ethical charge that the timing and framing of disclosure can either honor or violate. For physiology-keyed installation, disclosure design should be treated as part of the work, not as signage appended to it.

### 6.4 Limitations and Open Questions

This is a situated reading of a single work in a single venue; it does not generalize and is not intended to. The observation was conducted by the author, who is not a neutral instrument — the field-note categories are interpretive. The work's calming register may be specific to its slow timescale and to this gallery's acoustics. Open questions include how disclosure timing could be varied as a compositional parameter, and how the work would read in a busier, less contemplative venue.

---

## 7. Conclusion

*Tide Memory* is an autonomous generative installation that composes from the breath of everyone in the room. Its six-week exhibition revealed that co-authorship of such a work is felt as surrender rather than command, and that the design of disclosure — when and how visitors learn what is sensed — is itself an artistic material with an ethical charge. The paper contributes the work, an account of its generative system, and a situated reading of embodied co-authorship. Future work will treat disclosure timing as a composable parameter and exhibit the piece in contrasting venues.

---

## AI-Usage Disclosure

This work and paper involved AI in two distinct channels, disclosed separately per SIGGRAPH Asia / ACM policy (verify against the current Art Papers CFP).

- **AI to make the artwork**: the generative audio mapping used a parametric synthesis engine; no machine-learning model was used to generate audio or imagery. The breath-aggregation method was authored by the artist and collaborator.
- **AI to write the paper**: AI-assisted tools supported literature search framing, draft structuring, and copy-editing. All artistic decisions, observations, interpretation, and conclusions were directed and verified by the author, who takes full responsibility for the integrity of this work.

---

## References

*(This is an example — references are illustrative and use the ACM Reference Format. They are not real citations and exhibition venues are fictional.)*

Author A and Author B. 2022. Breath detection from contact microphones for solo performance. In *Proceedings of the [Fictional] Conference on New Interfaces for Musical Expression*. https://doi.org/10.1145/xxxxxxx

Author C. 2020. Station-based biosignal installation: a survey of practice. *[Fictional] Journal of Media Art* 12, 3 (2020), 45–67. https://doi.org/10.1162/xxxxxxx

Author D and Author E. 2023. Reflexive thematic reading in practice-based art research. *[Fictional] Journal of Artistic Research* 9, 1 (2023), 1–22. https://doi.org/10.1162/xxxxxxx

Claire Bishop. 2012. *Artificial Hells: Participatory Art and the Politics of Spectatorship*. Verso, London.

Brigid Costello and Ernest Edmonds. 2019. Directed and emergent play in interactive art. In *Proceedings of the [Fictional] Conference on Creativity and Cognition*. https://doi.org/10.1145/xxxxxxx

Ernest Edmonds. 2018. *The Art of Interaction: What HCI Can Learn from Interactive Art*. Morgan & Claypool.

Brian Eno. 1996. Generative music. *[Fictional] In Motion Magazine* (1996).

Rafael Lozano-Hemmer. 2007–2018. *Pulse* (series). Biometric installation. Exhibited at [Fictional Venue], [City]. https://www.example.org/pulse

Thecla Schiphorst. 2021. Somaesthetics and felt interaction in media art. *Leonardo* 54, 2 (2021), 134–141. https://doi.org/10.1162/xxxxxxx
