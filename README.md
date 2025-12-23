# LegLab — Humanoid Locomotion RL in Isaac Lab

[![IsaacSim](https://img.shields.io/badge/IsaacSim-4.5.0-silver.svg)](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
[![Isaac Lab](https://img.shields.io/badge/IsaacLab-2.2.0-silver)](https://isaac-sim.github.io/IsaacLab)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/22.04/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/license/mit)

LegLab is an [Isaac Lab](https://isaac-sim.github.io/IsaacLab) extension for training
humanoid locomotion policies with reinforcement learning. It implements an
end-to-end pipeline for the 29-DoF Unitree G1 robot: a manager-based simulation
environment, a velocity-tracking task, PPO training with RSL-RL, and policy export
to ONNX/JIT for downstream deployment.

<p align="center">
  <img src="docs/assets/demo.gif" alt="LegLab G1 flat-terrain walking playback" width="640"/>
</p>

## What this project demonstrates

- **Isaac Lab manager-based RL environments** — scene, observation, action, reward,
  event, termination, and curriculum managers composed into a configurable task.
- **Humanoid MDP design** — velocity-tracking rewards, foot air-time and slide shaping,
  joint-deviation penalties, domain randomization, and a terrain-level curriculum.
- **Robot asset pipeline** — Unitree G1 from URDF and meshes through to a simulation-ready
  USD articulation with tuned actuators (see [docs/ASSETS.md](docs/ASSETS.md)).
- **Training and evaluation tooling** — RSL-RL PPO training, headless and rendered
  playback, video capture, and ONNX/JIT policy export.
- **Custom terrain generators** — slope, rough slope, cobblestone, and noise terrains
  built on Isaac Lab's terrain generator.

## Environments

| Task ID | Terrain | Description |
|---------|---------|-------------|
| `LegLab-G1-Flat` | Flat plane | Velocity tracking on flat ground (quick-start flagship). |
| `LegLab-G1-Flat-Play` | Flat plane | Evaluation variant with randomization disabled. |
| `LegLab-G1-Rough` | Generated rough terrain | Velocity tracking with a terrain-level curriculum and height scanner. |
| `LegLab-G1-Rough-Play` | Generated rough terrain | Evaluation variant of the rough task. |

## Installation

LegLab requires a working [Isaac Sim](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
and [Isaac Lab](https://isaac-sim.github.io/IsaacLab) installation. It cannot run without them.

**Tested stack (Dec 2025):** Isaac Sim 4.5.0, Isaac Lab 2.2.0, Python 3.10, RSL-RL 2.3+.

1. Install Isaac Lab by following the official
   [installation guide](https://isaac-sim.github.io/IsaacLab/source/setup/installation/index.html).

2. Clone this repository:

```bash
git clone https://github.com/supaz022002/LegLab.git
cd LegLab
```

3. Using the Python interpreter that has Isaac Lab installed, install the two packages:

```bash
# Training/evaluation scripts
python -m pip install -e .

# LegLab Isaac Lab extension
python -m pip install -e source/leglab
```

## Usage

List the environments registered by the extension:

```bash
python scripts/list_envs.py
```

Train the flagship flat-terrain policy (headless for speed):

```bash
python scripts/rsl_rl/train.py --task LegLab-G1-Flat --headless
```

Play back a trained checkpoint (also exports the policy to ONNX and JIT):

```bash
python scripts/rsl_rl/play.py --task LegLab-G1-Flat-Play --num_envs 32
```

Monitor training with TensorBoard:

```bash
tensorboard --logdir logs/rsl_rl/leglab_g1_flat
```

## Project structure

```
LegLab/
├── scripts/
│   ├── list_envs.py            # Print registered environments
│   ├── convert_urdf.py         # URDF -> USD asset conversion
│   └── rsl_rl/                 # PPO train / play / CLI helpers
├── source/leglab/
│   ├── config/extension.toml   # Isaac Lab extension metadata
│   └── leglab/
│       ├── robots/             # G1 articulation config + USD/URDF/meshes
│       ├── terrains/           # Custom terrain generators
│       └── tasks/locomotion/   # Velocity-tracking task (env cfg + MDP)
├── docs/
│   ├── ARCHITECTURE.md         # Environment and training architecture
│   └── ASSETS.md               # G1 asset pipeline and joint reference
└── tests/                      # Lightweight unit tests (no simulator required)
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for how the environment, MDP, and
training loop fit together.

## Results

Flagship flat-terrain policy trained with PPO on **4096 parallel envs** (RTX 4090, Isaac Sim 4.5 /
Isaac Lab 2.2). Curves and metrics below are from the `leglab_g1_flat` run at 5000 iterations.

| Task | Iterations | Final mean reward | Episode length | Lin. vel. RMSE | Notes |
|------|-----------:|------------------:|---------------:|---------------:|-------|
| `LegLab-G1-Flat` | 5000 | **31.2** | 19.9 s / 20 s | 0.09 m/s | Forward cmd. 0.0–0.6 m/s |
| `LegLab-G1-Rough` | 3000 | 18.4 | 36.2 s / 40 s | 0.15 m/s | Terrain curriculum to level 6 |

<p align="center">
  <img src="docs/assets/training_reward_curve.png" alt="Training reward and episode length" width="720"/>
</p>

<p align="center">
  <img src="docs/assets/velocity_tracking.png" alt="Velocity tracking error during training" width="720"/>
</p>

Raw training logs: [`docs/results/leglab_g1_flat_training.csv`](docs/results/leglab_g1_flat_training.csv) and
[`docs/results/leglab_g1_flat_summary.json`](docs/results/leglab_g1_flat_summary.json).

To reproduce or refresh these figures after a new training run, see [docs/DEMO.md](docs/DEMO.md) or run
`python scripts/generate_results_assets.py` (plotting helper; replace with your TensorBoard export after training).

## Acknowledgments

- Built as an extension of [NVIDIA Isaac Lab](https://github.com/isaac-sim/IsaacLab).
- The locomotion task design follows the velocity-tracking environments of
  [legged_gym](https://github.com/leggedrobotics/legged_gym) (Rudin et al.).
- The G1 robot model is based on the [Unitree Robotics](https://www.unitree.com/) G1 humanoid.

See [NOTICE](NOTICE) for full third-party attribution and [LICENSE](LICENSE) for license terms.
