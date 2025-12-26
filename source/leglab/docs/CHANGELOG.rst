Changelog
---------

0.1.2
~~~~~

Changed
^^^^^^^

* Verified compatibility with Isaac Sim 4.5.0 and Isaac Lab 2.2.0.
* Updated RSL-RL minimum version check for distributed training (``rsl-rl-lib>=2.3.1``).
* Refreshed extension metadata and setup classifiers for the 4.5 / 2.2 toolchain.

0.1.1
~~~~~

Changed
^^^^^^^

* Compatibility pass for Isaac Sim 4.5.0 and Isaac Lab 2.1.0.

0.1.0
~~~~~

Added
^^^^^

* Initial release of LegLab: an Isaac Lab extension for humanoid locomotion
  reinforcement learning with the Unitree G1 robot.
* ``LegLab-G1-Flat`` and ``LegLab-G1-Rough`` velocity-tracking environments.
* RSL-RL PPO training and evaluation scripts with ONNX/JIT policy export.
* Custom terrain generators (slope, rough slope, cobblestone, noise).
