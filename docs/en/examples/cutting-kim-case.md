# Worked example — *Cutting Kim*

This walkthrough applies the plugin's reconstruction benchmark to a real practice-based art paper: **Bae, Choi, and Nam, *Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts*, SIGGRAPH Asia 2025 Art Papers.**

The published paper is held out as **gold**. The plugin receives only an **input pack** of pre-writing factual material. The plugin then reconstructs a paper, and the instrumentation compares the reconstruction to the gold layer by layer.

> **Provenance.** *Cutting Kim* is the work of Joonhyung Bae, Eunjin Choi, and Juhan Nam (KAIST). The authors contributed their own paper for use as this worked example, so no third-party copyright is implicated. The reconstruction below is this plugin's output, produced for the benchmark — it is not a competing publication.

---

## Step 1 — the input the plugin receives

The artist-researcher gives the plugin an `input/` directory of factual material. **The published paper's framing, thesis, provocation, conceptual vocabulary, participant-interview findings, and reflection are all withheld for the benchmark.**

### `concept_memo.md` (neutral topic seed)

```
An interactive VR experience for the Oculus Quest 2 in which the player's own
voice is the controller: loudness and pitch, captured through the headset
microphone, drive a game where the player wields a voice-generated "sonic sword"
to destroy food-themed enemy characters. The work was shown in public exhibition
settings (workshop, conference, festival).
```

(That is the whole memo — one paragraph, no interpretive claim.)

### `documentation.md` (factual description of the work)

Excerpt:

> Voice input is captured via the microphone of the Oculus Quest 2. **Loudness:** the system uses the Root Mean Square (RMS) of the audio signal to measure voice amplitude; attack power increases linearly with input volume in decibels. **Pitch:** fundamental frequency (F0) is detected using the YIN algorithm and mapped to the nearest pitch class and height. Pitch class maps to hue; pitch height maps to brightness, calibrated in Lab color space with the Delta E*2000 formula.

Plus the damage/scoring system (baseline + up to 4.5× pitch-match multiplier), the three-stage game flow (Story / Tutorial / Gameplay), and the HUD. No interpretive framing.

### `exhibition_record.md` (factual venue data)

The four deployments as a table: Daejeon Museum of Art workshop (2022.10), The Infinite CT conference at SFactory (2022.12), HCI Korea 2023 (2023.02), and ACT Festival 2023 at the Asia Culture Center (2023.11) — venue, event type, dates only.

### `bibliography.bib`

The 28 cited precedent works and theory, verified by the input audit as transferable factual material (voice-interaction games, pitch detection, color-synesthesia, practice-based research method, etc.).

### `LEAKAGE_AUDIT.md`

The auditor's list of what was **withheld from the input**:

- Thesis: the voice as a medium for "playful transgression"; interactive art as a "rehearsal space"; technology used "not to control but to liberate" the voice.
- Central paradox: the "publicly private" act — perceived privacy under the headset while the body/voice become a public spectacle.
- Framing vocabulary: "technologies of transgression," "permission structures," "beautiful transgression," the carnivalesque / "digital carnival."
- Provocation: "What happens when technology permits us to be loud?"
- Participant analysis: the N=5 festival-interview findings (embarrassment, catharsis, productive tension).
- Reflection / conclusion stance: the body as a "liminal object," "building new permission structures within our own."

The audit also **flags one borderline item honestly**: the bibliography includes transgressive-play (`aarseth2014fought`, `jorgensen2019transgression`) and carnivalesque (`bakhtin2020rabelais`) references, whose titles gesture toward the conceptual territory. Including them is consistent with treating the lineage as transferable, but it is this pack's strongest leakage vector — flagged so the generative-layer margin can be read against it.

---

## Step 2 — running the plugin

The user invokes:

```
/art-paper full reconstruct the paper from the materials in input/
```

The plugin reads the input pack, applies the firewall discipline (it cannot author the withheld content), and produces `reconstruction/paper.md` — a complete art paper authored from the available factual material only. The reconstruction here was run as a firewalled agent that saw the input pack and **never** the gold paper, producing a ~3,200-word Pattern-1 art paper.

---

## Step 3 — what the plugin produced

The reconstruction has its own title, abstract, and section structure. Crucially, the plugin **does not reproduce the authors' withheld provocation**; it generates a *different* reading that the input alone can support.

### Reconstructed title

> "Cutting Kim: The Untrained Voice as an Embodied Game Controller"

(Compare the gold title: *"Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts"*.)

### Reconstructed Conceptual Framework (excerpt)

> The work's most consequential design decision is that it does not require the player to sing. The damage model grants a baseline effect to *any* vocalization, and reserves a multiplier for players who happen to match an enemy's target pitch. The system, in our framing, treats the voice as effort rather than as performance... We read this as the work's argument: that the human voice is worth designing *for* in its ordinary, imperfect, effortful state — not only in its trained, musical state.

This is the plugin's reading built from documentation alone — *the untrained voice as a legitimate, first-class control surface*. The authors' actual reading (playful transgression, the "publicly private" paradox, the carnivalesque) is **absent**. The plugin offers a coherent interpretation, but a *different* one. Notably, even though the bibliography telegraphed the transgression vocabulary, the reconstruction did not adopt it.

### Reconstructed Reflection (excerpt)

> ...we deliberately do **not** report what those participants felt or said: that interpretive analysis is outside the evidence we are working from here, and inflating reception ("audiences were delighted") would not be honest.

The reconstruction explicitly *refuses* to manufacture the participant-reception findings it was not given — exactly the firewall behavior the methodology intends.

---

## Step 4 — instrumentation report

The instrumentation script compares reconstruction to gold layer by layer:

| Metric | Value | Reading |
|---|---|---|
| **Transferable-layer similarity (T)** | 0.2568 | Documentable content (the work, realization) converges with gold |
| **Generative-layer similarity (G)** | 0.1261 | Conceptual framework + reflection diverge from gold |
| **T − G margin** | **+0.1307** | Directional reading supported (T > G, as expected) |
| **Contamination probe (8-gram)** | 0.0028 | `ok` (far below the 0.10 high-warning threshold) |
| **`thesis_supported`** | `True` | The transferable-converges / generative-diverges ordering holds |
| **Citation set** | precision 1.0, recall 0.32 | 9 of 28 gold precedents surfaced; everything cited was a real gold precedent |
| **Structural coverage** | 1.0 | All Pattern-1 layers present |

Per-layer lexical similarity (descriptive): realization (transferable) `0.21` is the highest-aligned content layer; conceptual_framework `0.13` and reflection_discussion `0.12` (both generative) sit lower.

Optional semantic-embedding pass (`--embed`, `BAAI/bge-small-en-v1.5`): chunk-alignment cosine reports `transferable 0.776 / generative 0.780`, essentially equal. This is the **topic-saturation** the methodology warns about: within one paper every layer embeds at ~0.9, so blob cosine barely discriminates. The lexical n-gram measure is the discriminator; embedding is included for transparency but should not be read as "T ≈ G semantically."

**Interpretation.** The plugin reconstructs the factual layer reasonably (T ≈ 0.26) while the generative layer diverges meaningfully (G ≈ 0.13). The 8-gram contamination probe finds no memorization. The reconstruction is therefore **genuine inference from the input, not a replay of memorized content** — and the generative-layer divergence reflects that the authors' withheld reading was not producible from documentation alone.

> **Two honest notes.** (1) *Gold heading normalization.* This paper folds its conceptual framing into the Introduction and titles its discussion section idiosyncratically, so the gold's section headings were normalized to the Pattern-1 layer each section plays — the same structural conversion applied to every other benchmark case — without altering section content. (2) *Anchoring rate.* The script flagged 2 "claims" as unanchored, but both are false positives: one is an enumerator ("The first is how much design work..."), the other is the sentence that explicitly *refuses* to report reception. There is no genuine reception inflation in the reconstruction.

---

## Step 5 — Clean-control variant (a stricter test)

A stronger test reconstructs not from the standard input pack (which was extracted with the gold paper in hand and therefore carries paper-derived technical prose) but from a **minimal-footprint input** — material a viewer with a festival programme and generic media-art knowledge could compile. The standard pack's `documentation.md` names RMS, YIN, Lab/Delta E*2000, the "up to 4.5×" multiplier, and the "three-stage" gameplay taxonomy; the clean-control omits all of these (they are factual, but their inclusion in the standard pack came from the gold's prose). The bibliography is also pruned from 28 to 15 entries, dropping the references that telegraph the gold's transgressive-play / carnivalesque lineage.

A second firewalled reconstruction was run on this leaner pack, again with no access to the gold or to the standard reconstruction.

Clean-control instrumentation reports:

| Metric | Standard | Clean control |
|---|---|---|
| T (transferable, lexical) | 0.2568 | 0.1047 |
| G (generative, lexical) | 0.1261 | 0.1236 |
| **T − G margin** | **+0.1307** | **−0.0189** |
| `thesis_supported` | True | **False** |
| Contamination (8-gram) | 0.0028 | 0.0 |
| Citation precision / recall | 1.0 / 0.32 | 1.0 / 0.54 |
| Semantic align (T / G) | 0.776 / 0.780 | 0.760 / 0.800 |

**Interpretation.** Under the cleanest available input (no paper-derived technical prose; lineage-telegraphing references removed), the directional `T > G` reading **does not hold** — the margin collapses from +0.13 to slightly negative. This is consistent with a substantial fraction of the standard margin being an **input-extraction artifact**: the standard pack's `documentation.md` reuses the gold's wording for RMS / YIN / Delta E*2000 / multiplier numbers, which boosts transferable jaccard. When that input prose is held out, the transferable layer collapses to roughly the same lexical floor as the generative layer.

The contamination probe stays at zero in both runs — the plugin did not memorize the gold in either case. What this demonstrates is the methodology's reach **and** its honest limit: the per-layer instrument is sensitive enough to register the input-pack composition, and the clean-control surfaces that sensitivity rather than hiding it. (The clean-control reconstruction's own reading, *"voice as blade — the HMD privatizes the scene while the voice re-publicizes the player,"* is also coherent and again differs from the gold's withheld reading; the firewall continues to function.)

---

## Step 6 — what this example shows

Concretely:

1. **The firewall works.** The plugin received no provocation/reflection material and produced its own — not the authors'. Both reconstructions (standard and clean-control) authored distinct coherent readings; neither reproduced the gold's "playful transgression" thesis.
2. **The per-layer instrument detects the gap (when input supports it).** The standard pack yields T = 0.26 / G = 0.13, margin +0.13.
3. **The inversion rule passes.** No contamination above the warning threshold in either run; the plugin did not memorize.
4. **The clean-control bounds honesty.** Under stricter input discipline, the standard margin collapses to near-zero, exposing how much of it was carried by paper-derived prose in the input. The methodology reports this rather than hiding it.
5. **The authors' reading is preserved as theirs.** Both reconstructions produced *different* coherent readings (the untrained voice as game controller; voice as blade and exposed body); the original "playful transgression" reading remains uniquely the authors'.

This is what the methodology promises — measurement, not a verdict.

---

## Reproducing this example

The full input packs, reconstructions, and instrumentation for `sa25-ck` and `sa25-ck-clean` live in the companion paper's reproducibility mirror under `eval/pilot/sa25-ck/` and `eval/pilot/sa25-ck-clean/` (the clean-control symlinks `gold/` to the standard pilot — the gold paper is the same). The instrumentation script (stdlib-only by default; optional sentence-embedding via `--embed`) is at `eval/instrumentation.py`.

```bash
python3 eval/instrumentation.py eval/pilot/sa25-ck --json
python3 eval/instrumentation.py eval/pilot/sa25-ck-clean --json
```

The outputs reproduce the tables in Step 4 and Step 5.
