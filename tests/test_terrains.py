"""Tests for the custom terrain generators. Skipped when Isaac Lab is not installed."""

from __future__ import annotations

import pytest


def test_terrain_configs_have_subterrains():
    pytest.importorskip("isaaclab")

    from leglab.terrains import COBBLESTONE_ROAD_CFG, NOISE_TERRAINS_CFG, ROUGH_SLOPE_TERRAINS_CFG, SLOPE_TERRAINS_CFG

    for cfg in [COBBLESTONE_ROAD_CFG, NOISE_TERRAINS_CFG, ROUGH_SLOPE_TERRAINS_CFG, SLOPE_TERRAINS_CFG]:
        assert cfg.sub_terrains, "terrain configuration has no sub-terrains"
        assert cfg.size[0] > 0 and cfg.size[1] > 0
