"""Repository hygiene tests that do not require Isaac Lab or Isaac Sim."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _iter_source_text_files():
    roots = [REPO_ROOT / "scripts", REPO_ROOT / "source" / "leglab" / "leglab", REPO_ROOT / "docs"]
    extra = [REPO_ROOT / "README.md", REPO_ROOT / "NOTICE"]
    suffixes = {".py", ".toml", ".md", ".rst", ".yaml", ".yml"}
    for root in roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in suffixes:
                yield path
    for path in extra:
        if path.is_file():
            yield path


def test_extension_metadata_is_leglab():
    text = (REPO_ROOT / "source" / "leglab" / "config" / "extension.toml").read_text()
    assert 'name = "leglab"' in text
    assert 'author = "Minh"' in text
    assert 'title = "LegLab"' in text


def test_g1_usd_asset_exists():
    usd = REPO_ROOT / "source" / "leglab" / "leglab" / "robots" / "G1" / "g1.usd"
    assert usd.is_file(), f"missing G1 USD asset at {usd}"


def test_ppo_experiment_names_use_leglab_prefix():
    text = (
        REPO_ROOT
        / "source"
        / "leglab"
        / "leglab"
        / "tasks"
        / "locomotion"
        / "velocity"
        / "config"
        / "g1"
        / "agents"
        / "rsl_rl_ppo_cfg.py"
    ).read_text()
    assert 'experiment_name = "leglab_g1_rough"' in text
    assert 'self.experiment_name = "leglab_g1_flat"' in text


def test_no_previous_owner_footprints():
    forbidden = [
        "humarconoid",
        "humarcscripts",
        "s-choi-s",
        "sol choi",
        "solchoi",
        "kist-arc",
        "korea institute of science",
    ]
    offenders: list[str] = []
    for path in _iter_source_text_files():
        lowered = path.read_text(errors="ignore").lower()
        for needle in forbidden:
            if needle in lowered:
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {needle}")
    assert not offenders, "Found previous-owner footprints:\n" + "\n".join(offenders)
