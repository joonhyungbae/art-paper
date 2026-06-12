# SIGGRAPH Asia / ACM AI-Usage Disclosure Reference

Replaces the ARS ML/NLP venue set (ICLR/NeurIPS/Nature/…) as the **default** disclosure target for art-paper. Consumed by `art-paper` `disclosure` mode and the `disclosure_mode_protocol`. Structured to slot into the existing `venue_disclosure_policies.md` mechanism as venue entries.

> **Verify-against-CFP discipline (inherited from ARS):** AI-usage policies drift. The fields below record what art-paper last verified and when. Before submission, the author MUST confirm against the current SIGGRAPH Asia Call for Art Papers and the ACM Policy on Authorship. If a needed venue is not listed, the disclosure mode halts and asks the author to paste the current policy — it never fabricates a policy.

---

## Venue: SIGGRAPH Asia — Art Papers track (→ ACM Digital Library)

| Field | Value |
|---|---|
| Source URL | https://asia.siggraph.org/ (Art Papers CFP) + https://www.acm.org/publications/policies/new-acm-policy-on-authorship |
| Access date | 2026-05-22 (PLACEHOLDER — re-verify before use) |
| Policy summary | ACM policy: Generative AI tools cannot be listed as authors. Authors are fully responsible for all content, including any produced with AI assistance. Use of generative AI in producing the work or the paper must be disclosed. The track's proceedings publish on the ACM Digital Library; confirm the exact disclosure wording against the current Call for Art Papers. |
| Required phrasing elements | (a) name the specific tool(s) and version if known; (b) state the specific tasks assisted (e.g., drafting, code, image generation that is part of the artwork vs. part of the paper); (c) affirm the authors reviewed and take full responsibility for all content. |
| Critical distinction (art-paper specific) | **Disclose AI used to MAKE the artwork separately from AI used to WRITE the paper.** If generative AI is a medium of the work itself, that belongs in the methods/realization section as artistic disclosure, not only in the boilerplate AI-usage statement. |
| Preferred disclosure location | Acknowledgements or a dedicated "Use of AI Tools" note before References; artwork-medium AI use also described in §Realization. |
| Prohibited uses | AI cannot be an author. AI cannot be used to fabricate references, exhibition records, or claimed capabilities of the work. |
| Authorship rule | AI tools cannot be listed as authors. |

---

## Venue: ACM (generic fallback for other ACM-published art venues)

| Field | Value |
|---|---|
| Source URL | https://www.acm.org/publications/policies/new-acm-policy-on-authorship |
| Access date | 2026-05-22 (PLACEHOLDER — re-verify) |
| Policy summary | Generative AI cannot be an author. Disclosure of generative-AI use in the work/paper is required; authors bear full responsibility. |
| Required phrasing elements | tool(s) + version + tasks + responsibility affirmation. |
| Preferred disclosure location | Acknowledgements / dedicated note before References. |
| Authorship rule | AI tools cannot be listed as authors. |

---

## Generated disclosure — template shape (art-paper aware)

The mode produces a tailored statement. Canonical shape:

> **Use of AI Tools.** In producing *this paper*, the authors used [tool, version] for [drafting/editing/code/…]. [If applicable:] As part of *the artwork itself*, [tool] was used as [medium/process], described in Section [Realization]. The authors reviewed all content and take full responsibility for it. No AI system is an author of this work.

**Iron rules (inherited):**
1. Two-channel disclosure — paper-making vs. artwork-making AI use are stated distinctly when both apply.
2. Never claim "no AI used" if the art-paper pipeline assisted; that is itself a disclosure failure.
3. Tool + task specificity; no vague "AI was used."
4. Responsibility affirmation present.
5. If venue policy is unverified, surface a "VERIFY POLICY" flag rather than asserting compliance.
