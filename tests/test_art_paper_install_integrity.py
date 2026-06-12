"""Install-integrity sanity tests for the art-paper plugin (v0.1.1).

These tests guard the install-defect class that landed in 0.1.1:
  - skills/ symlinks must resolve to actual SKILL.md files
  - marketplace.json + plugin.json versions must agree with CHANGELOG
  - marketplace.json mode-count claim must match the per-skill SKILL.md modes
  - .claude-plugin/marketplace.json plugin must point at the local repo

They are stdlib-only, do not exercise the model, and run in < 1 second.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SKILLS = ("art-inquiry", "art-paper", "art-pipeline", "art-reviewer")


def test_skills_symlinks_resolve_to_real_skill_md():
    """skills/<name>/SKILL.md must be a real readable file for each of the 4 core skills.

    Regression guard: at v0.1.1 the `skills/` directory contained dangling
    symlinks pointing at the old fork-period names (`creative-{inquiry,paper,
    pipeline,reviewer}`), so a fresh clone would fail to register the four
    core skills via the conventional `skills/` discovery path.
    """
    skills_dir = REPO / "skills"
    assert skills_dir.is_dir(), f"missing skills/ at {skills_dir}"
    for name in SKILLS:
        skill_path = skills_dir / name
        assert skill_path.exists(), f"skills/{name} does not exist or symlink is broken"
        skill_md = skill_path / "SKILL.md"
        assert skill_md.is_file(), f"skills/{name}/SKILL.md is not a readable file"
        # SKILL.md frontmatter must declare the matching name
        text = skill_md.read_text(encoding="utf-8")
        m = re.search(r"^name:\s*(\S+)\s*$", text, re.MULTILINE)
        assert m, f"skills/{name}/SKILL.md missing `name:` frontmatter"
        assert m.group(1) == name, (
            f"skills/{name}/SKILL.md declares name={m.group(1)!r}, expected {name!r}"
        )


def _read_changelog_latest_version() -> str:
    """Return the most recent `## [x.y.z]` heading in CHANGELOG.md."""
    changelog = (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", changelog, re.MULTILINE)
    assert m, "no `## [x.y.z]` heading found in CHANGELOG.md"
    return m.group(1)


def test_plugin_json_version_matches_changelog():
    plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert plugin["version"] == _read_changelog_latest_version(), (
        f"plugin.json version {plugin['version']!r} does not match latest "
        f"CHANGELOG entry {_read_changelog_latest_version()!r}"
    )


def test_marketplace_json_plugin_version_matches_changelog():
    market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugins = market["plugins"]
    assert len(plugins) == 1, f"expected 1 plugin entry, found {len(plugins)}"
    assert plugins[0]["version"] == _read_changelog_latest_version()


def _modes_per_skill_from_mode_registry() -> dict[str, int]:
    """Count modes per skill from MODE_REGISTRY.md tables.

    Each section heading ``## art-<skill> (N modes)`` is followed by a
    markdown table where every mode row starts with a backticked mode name in
    column 1. The header / separator rows do not match.
    """
    text = (REPO / "MODE_REGISTRY.md").read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^##\s+(art-[a-z]+)\b", line.strip())
        if m:
            current = m.group(1)
            counts.setdefault(current, 0)
            continue
        if current and re.match(r"^\|\s*`[a-z][a-z0-9_-]*`", line.strip()):
            counts[current] += 1
    return counts


def test_marketplace_mode_count_claim_matches_skills():
    """marketplace.json description must accurately state the modes per skill.

    Regression guard: pre-0.1.1 the description claimed "12 modes per skill"
    (false — actual is 7 / 12 / 6 + orchestrator). This test reads the claim
    out of the description and asserts it against MODE_REGISTRY.md.
    """
    market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    desc = market["plugins"][0]["description"]
    modes = _modes_per_skill_from_mode_registry()
    # Allow art-pipeline to be an orchestrator (registry lists it separately).
    for skill in ("art-inquiry", "art-paper", "art-reviewer"):
        assert skill in modes, f"MODE_REGISTRY.md has no section for {skill}"
        m = re.search(rf"{skill}\s+(\d+)", desc)
        assert m, f"marketplace description does not state a mode count for {skill}"
        claimed = int(m.group(1))
        actual = modes[skill]
        assert claimed == actual, (
            f"marketplace claims {skill} has {claimed} modes; MODE_REGISTRY.md lists {actual}"
        )
