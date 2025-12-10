"""Smoke tests for the LegLab extension. Skipped when Isaac Lab is not installed."""

from __future__ import annotations

import pytest


def test_tasks_register_expected_environments():
    pytest.importorskip("isaaclab")

    import gymnasium as gym

    import leglab.tasks  # noqa: F401

    registered = set(gym.registry.keys())
    for env_id in [
        "LegLab-G1-Flat",
        "LegLab-G1-Flat-Play",
        "LegLab-G1-Rough",
        "LegLab-G1-Rough-Play",
    ]:
        assert env_id in registered, f"environment {env_id} was not registered"
