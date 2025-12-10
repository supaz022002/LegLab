# Copyright (c) 2024, Minh.
# SPDX-License-Identifier: MIT

"""Script to print all the environments registered by the LegLab extension.

The script iterates over all registered environments and prints a table with the
environment name, the entry point, and the environment config entry point.
"""

"""Launch Isaac Sim Simulator first."""

from isaaclab.app import AppLauncher

# launch omniverse app
app_launcher = AppLauncher(headless=True)
simulation_app = app_launcher.app


"""Rest everything follows."""

import gymnasium as gym
from prettytable import PrettyTable

# Import extensions to set up environment tasks
import leglab.tasks  # noqa: F401


def main():
    """Print all environments registered by the LegLab extension."""
    table = PrettyTable(["S. No.", "Task Name", "Entry Point", "Config"])
    table.title = "Available Environments in LegLab"
    table.align["Task Name"] = "l"
    table.align["Entry Point"] = "l"
    table.align["Config"] = "l"

    index = 0
    for task_spec in gym.registry.values():
        env_cfg = task_spec.kwargs.get("env_cfg_entry_point", "")
        if "leglab" in str(env_cfg):
            table.add_row([index + 1, task_spec.id, task_spec.entry_point, env_cfg])
            index += 1

    print(table)


if __name__ == "__main__":
    try:
        main()
    finally:
        # close the app
        simulation_app.close()
