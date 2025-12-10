"""Package containing robot asset configurations."""

import os

# Path to the robots asset directory (contains USD/URDF/mesh files).
LEGLAB_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from .g1 import *  # noqa: E402, F401, F403
