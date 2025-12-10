# Training and Demo Recording

This guide walks through training the flagship `LegLab-G1-Flat` policy and recording
a demo for the README. Requires a working Isaac Sim + Isaac Lab installation.

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

## 2. Record a walking demo

Play back the latest checkpoint with video capture enabled:

```bash
python scripts/rsl_rl/play.py \
  --task LegLab-G1-Flat-Play \
  --num_envs 16 \
  --video \
  --video_length 500
```

Videos are saved under `logs/rsl_rl/leglab_g1_flat/<run>/videos/play/`.

Convert the best clip to a GIF for the README (requires `ffmpeg`):

```bash
ffmpeg -i logs/rsl_rl/leglab_g1_flat/<run>/videos/play/rl-video-step-0.mp4 \
  -vf "fps=15,scale=640:-1" docs/assets/demo.gif
```

## 3. Update README results

After training, fill in the [Results](../README.md#results) table with:

| Field | Where to find it |
|-------|------------------|
| Iterations | Last checkpoint step in the log directory name or TensorBoard |
| Final mean reward | TensorBoard scalar `Train/mean_reward` |
| Demo GIF | `docs/assets/demo.gif` (add to README hero section) |

Example README hero update:

```markdown
![G1 flat-terrain walking demo](docs/assets/demo.gif)
```
