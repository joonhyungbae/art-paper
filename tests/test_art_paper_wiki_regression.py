"""Wiki regression guards for the art-paper plugin (v0.1.1).

These tests freeze the user-facing wording fixes that landed in 0.1.1, so a
copy-paste edit cannot silently reintroduce them:

  - the suite display name is **Art-Paper**, not "Creative Research Skills"
  - bibliography format ads in user-facing wiki must not claim "Emerald Harvard"
    as a configured format (the authoritative set is ACM default + APA 7 /
    Chicago / MLA 9 / IEEE / Vancouver, per art-paper/SKILL.md)
  - commands/art-disclosure.md must not list empirical-science venues
    (ICLR / NeurIPS / Nature / Science / ACL / EMNLP) as a leftover from the
    ARS fork — the art-paper disclosure mode targets SIGGRAPH Asia / ACM
"""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# User-facing wiki surfaces only. ref/ is pristine upstream ARS and is excluded;
# eval/pilot/ is gitignored gold-paper copies and is excluded. CHANGELOG and
# docs/design entries may legitimately mention the historical name in a fork
# context — those files are excluded too.
WIKI_GLOBS = ("docs/en/**/*.md", "docs/ko/**/*.md")

EXCLUDE_REL = (
    "docs/design/",  # design docs may discuss the historical fork name
)


def _wiki_files():
    out = []
    for pat in WIKI_GLOBS:
        for p in REPO.glob(pat):
            rel = p.relative_to(REPO).as_posix()
            if any(rel.startswith(x) for x in EXCLUDE_REL):
                continue
            out.append(p)
    return out


def test_no_creative_research_skills_in_user_facing_wiki():
    """The suite is "Art-Paper". "Creative Research Skills" was a fork-period
    label, removed across the user-facing wiki in 0.1.1.
    """
    offenders = []
    for p in _wiki_files():
        text = p.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if re.search(r"creative\s*research\s*skills", line, re.IGNORECASE):
                offenders.append(f"{p.relative_to(REPO)}:{n}: {line.strip()}")
    assert not offenders, "stale 'Creative Research Skills' wording:\n" + "\n".join(offenders)


def test_no_emerald_harvard_as_configured_format():
    """The user-facing wiki must not advertise Emerald Harvard / Aslib JIM as a
    supported bibliography format — that line was an ARS-fork residue removed
    in 0.1.1. The authoritative set is in art-paper/SKILL.md.
    """
    offenders = []
    for p in _wiki_files():
        text = p.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if "emerald harvard" in line.lower():
                offenders.append(f"{p.relative_to(REPO)}:{n}: {line.strip()}")
    assert not offenders, "stale 'Emerald Harvard' wording:\n" + "\n".join(offenders)


def test_disclosure_command_targets_siggraph_acm_not_science_venues():
    """commands/art-disclosure.md must not list empirical-science venues
    (ICLR / NeurIPS / Nature / Science / ACL / EMNLP). That list was inherited
    from the ARS fork and replaced with the SIGGRAPH Asia / ACM two-channel
    wording in 0.1.1.
    """
    text = (REPO / "commands" / "art-disclosure.md").read_text(encoding="utf-8")
    forbidden = ("ICLR", "NeurIPS", "Nature", "Science", "ACL", "EMNLP")
    found = [v for v in forbidden if re.search(rf"\b{re.escape(v)}\b", text)]
    # "Science" is also a common English word ("computer science"); only flag it
    # if it shows up next to the other venue tokens, signalling the inherited
    # list pattern.
    if found == ["Science"]:
        found = []
    assert not found, (
        "stale ARS science-venue list in commands/art-disclosure.md: " + ", ".join(found)
    )


def test_disclosure_command_mentions_siggraph_or_acm():
    """Positive guard for the disclosure venue scope."""
    text = (REPO / "commands" / "art-disclosure.md").read_text(encoding="utf-8")
    assert re.search(r"SIGGRAPH\s*Asia", text, re.IGNORECASE) or re.search(
        r"\bACM\b", text
    ), "commands/art-disclosure.md no longer mentions SIGGRAPH Asia or ACM"


def test_no_fork_period_path_in_tracked_files():
    """No tracked file in THIS repo should embed the fork-period folder name
    `creative-research-skills` as a filesystem path.

    Regression guard for the `corpus_expansion/selected_corpus/cases_manifest.json`
    class of bugs found at v0.1.1: tracked JSON / config carrying
    `<repo-root>/creative-research-skills/...` paths break after the post-fork
    local rename. Path strings only — the suite name "Creative Research Skills"
    (capitalised) is guarded separately in
    `test_no_creative_research_skills_in_user_facing_wiki`. This test stays in
    place after the path bug is fixed so a future regression cannot slip in.

    Scope: only tracked files in this repo (uses `git ls-files`), so the test
    automatically ignores `.gitignore`d artefacts (eval/pilot/, .claude/
    settings.local.json, etc.) and nested separate-repo trees that show up
    as a single submodule-like entry. `ref/` (pristine upstream ARS) and
    `CHANGELOG.md` (records the rename) are excluded by name.
    """
    import subprocess
    SKIP_PREFIXES = ("ref/",)
    SKIP_FILES = {
        "CHANGELOG.md",
        "tests/test_art_paper_wiki_regression.py",
    }
    SUFFIX_OK = (
        ".md", ".tex", ".json", ".yaml", ".yml", ".toml",
        ".py", ".sh", ".cfg", ".ini", ".bib", ".txt",
    )
    result = subprocess.run(
        ["git", "-C", str(REPO), "ls-files"],
        capture_output=True, text=True, check=True,
    )
    offenders = []
    for rel in result.stdout.splitlines():
        if any(rel.startswith(x) for x in SKIP_PREFIXES):
            continue
        if rel in SKIP_FILES:
            continue
        p = REPO / rel
        if not p.is_file():
            continue
        if p.suffix.lower() not in SUFFIX_OK:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if re.search(r"creative-research-skills[/\\]", text):
            for n, line in enumerate(text.splitlines(), 1):
                if "creative-research-skills/" in line or "creative-research-skills\\" in line:
                    offenders.append(f"{rel}:{n}: {line.strip()[:120]}")
    assert not offenders, (
        "fork-period `creative-research-skills/` path in tracked file:\n"
        + "\n".join(offenders)
    )
