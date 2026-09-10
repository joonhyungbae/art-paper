"""Smoke test for `eval/instrumentation.py` on the bundled synthetic fixture.

Confirms the harness still runs end-to-end and produces a result with the
expected shape after the v0.1.1 changes (which did not touch the harness
itself, only added pilot data and worked-example wiki). stdlib-only — no API,
no model. < 1 second.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "eval"))


def test_instrumentation_runs_on_synthetic_fixture():
    """Importable use of the engine produces the documented metric set."""
    from instrumentation import instrument_case

    case = REPO / "eval" / "fixtures" / "synthetic_case"
    assert case.is_dir(), f"synthetic fixture missing at {case}"

    result = instrument_case(case)

    # Top-level discipline markers (the harness "does NOT score quality").
    assert result["instrumentation_only"] is True
    assert result["quality_scored"] is False
    assert result["case"] == "synthetic_case"

    metrics = result["metrics"]
    for key in (
        "citation_set_pr",
        "anchoring_rate",
        "structural_coverage",
        "contamination_probe",
        "per_layer_similarity",
    ):
        assert key in metrics, f"missing metric {key!r}"
        # Every metric carries a `does_not_license` field by harness contract.
        assert "does_not_license" in metrics[key]

    # Contamination probe must produce a valid flag.
    cont = metrics["contamination_probe"]
    assert cont["flag"] in {"ok", "ELEVATED", "HIGH-CONTAMINATION-WARNING"}
    assert 0.0 <= cont["ngram8_containment_recon_in_gold"] <= 1.0

    # Per-layer similarity reports either a comparable T/G pair or explicit None
    # (the latter when one side is empty); thesis_supported is the same shape.
    pls = metrics["per_layer_similarity"]
    for slot in ("transferable_similarity", "generative_similarity"):
        v = pls[slot]
        assert v is None or 0.0 <= v <= 1.0


def test_layer_split_is_keyword_driven():
    """The Pattern-1 layer split keys are present in the public LAYERS table.

    Regression guard: the [worked example withheld] worked example depends on the layer
    keyword list (`introduction`, `conceptual framework`, `the work`,
    `realization`, `reflection`, `discussion`, `conclusion`) staying stable.
    """
    from instrumentation import LAYERS

    expected_keys = {
        "introduction_context",
        "conceptual_framework",
        "the_work",
        "realization",
        "reflection_discussion",
        "conclusion",
        "other_work",
    }
    actual_keys = {key for key, _kw, _kind in LAYERS}
    assert actual_keys == expected_keys, (
        f"LAYERS keys drifted: missing {expected_keys - actual_keys}, "
        f"unexpected {actual_keys - expected_keys}"
    )
