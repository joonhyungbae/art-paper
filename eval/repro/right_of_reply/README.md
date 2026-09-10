# Right-of-reply invitations (Digital Creativity submission)

Status: **ready to send** — do not mark outcomes until mail is actually sent.
Window: 14 days from send date. Log replies in `outcomes.jsonl`.

## Recipients (minimum set named in §5.3)

| Case / venue | Work | Contact strategy |
|---|---|---|
| sa24-01 | AI-rays (Gao et al.) | Corresponding author via ACM DL / paper PDF |
| sa23-10 | see-saw (Morita & Kakehi) | Corresponding author via ACM DL / paper PDF |
| sa25-14 | City of Sparkles (Hu) | Corresponding author via ACM DL / paper PDF |
| dc22-01, dc24-02, dc24-03, dc24-04 | Four Digital Creativity corpus papers | Corresponding authors via T&F author pages |

Fill `contacts.csv` with emails before send. Do not invent addresses.

## Email template (English)

Subject: Right of reply — study using a short excerpt of your art paper

Dear [Name],

We are preparing a research article for *Digital Creativity* on a held-out reconstruction benchmark: an AI writing copilot is given only pre-writing documentation about a published practice-based art paper, and we compare what it writes to the published framing.

Your paper *[Title]* ([DOI]) is one of the cases. The manuscript quotes a short excerpt from your published framing (fair dealing / criticism) beside a short excerpt from the copilot's substitute reading. We do **not** release a full alternative paper, and we do **not** score your work by how closely the machine matched it.

The excerpts we propose to print are below. If you wish to correct a factual error, object to the juxtaposition, or offer a brief comment for the record, please reply within 14 days. A short comment (or a note that you decline) can be acknowledged in the camera-ready version.

Proposed gold excerpt:
"""
[EXCERPT]
"""

Proposed reconstruction excerpt (machine-generated; not attributed to you):
"""
[EXCERPT]
"""

With thanks,
[Corresponding author — after anonymity lifts / via editor if preferred during review]

## Send checklist

1. Complete `contacts.csv` from ACM/T&F pages (human verification).
2. Personalise three Table 2 emails + four DC emails.
3. BCC yourself; save `.eml` or provider sent copies under `sent/` (gitignored if needed).
4. Append one JSON line per outcome to `outcomes.jsonl`.
