# Training Guide

This guide walks through training the flagship `LegLab-G1-Flat` policy and updating
the README results. Requires a working Isaac Sim + Isaac Lab installation.

## 1. Train the flagship policy

From the repository root, using the Isaac Lab Python interpreter:

```bash
python scripts/rsl_rl/train.py --task LegLab-G1-Flat --headless
```

Checkpoints and TensorBoard logs are written to `logs/rsl_rl/leglab_g1_flat/`.

Monitor training:

```bash
tensorboard --logdir logs/rsl_rl/leglab_g1_flat
```

Typical flat-terrain training runs for 5 000 iterations (~several hours on a single GPU).

## 2. Play back a trained policy

```bash
python scripts/rsl_rl/play.py --task LegLab-G1-Flat-Play --num_envs 32
```

## 3. Update README results

After training, fill in the [Results](../README.md#results) table with:

| Field | Where to find it |
|-------|------------------|
| Iterations | Last checkpoint step in the log directory name or TensorBoard |
| Final mean reward | TensorBoard scalar `Train/mean_reward` |
| Training curves | Export from TensorBoard, or run `python scripts/generate_results_assets.py` as a plotting template |

Regenerate README training figures:

```bash
python scripts/generate_results_assets.py
```
