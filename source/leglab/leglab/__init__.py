"""LegLab: an Isaac Lab extension for humanoid locomotion reinforcement learning."""

import os

# Register Gym environments.
from .tasks import *  # noqa: F401, F403

# Absolute path to the repository root directory.
LEGLAB_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
