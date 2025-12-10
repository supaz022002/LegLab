# G1 Robot Assets

LegLab uses the 29-DoF Unitree G1 humanoid (with dexterous hands). The simulation
articulation is defined in
[`source/leglab/leglab/robots/g1.py`](../source/leglab/leglab/robots/g1.py) as `G1_CFG`.

## Files

| File | Role |
|------|------|
| `robots/G1/g1.usd` | Simulation-ready USD articulation loaded by `G1_CFG` (self-contained). |
| `robots/G1/g1.urdf` | Source URDF used to generate the USD. |
| `robots/G1/meshes/` | Visual and collision meshes referenced by the URDF. |

The USD is the only asset required at runtime; the URDF and meshes are kept so the
conversion can be reproduced.

## URDF to USD pipeline

The USD is produced from the URDF with Isaac Lab's URDF importer, wrapped by
[`scripts/convert_urdf.py`](../scripts/convert_urdf.py). Paths are resolved relative to
`source/leglab/leglab/robots/`:

```bash
python scripts/convert_urdf.py G1/g1.urdf G1/g1.usd --merge-joints --make-instanceable
```

After conversion, `G1_CFG` adds physics properties, initial joint angles, and actuator
groups on top of the imported articulation.

## Actuator groups

`G1_CFG` splits the joints into three actuator groups (see `g1.py` for exact gains):

- **legs** — hip (yaw/roll/pitch), knee, and torso joints; high stiffness for support.
- **feet** — ankle pitch/roll joints; low stiffness for compliant contact.
- **arms** — shoulder, elbow, and finger joints; moderate stiffness.

## Joint and body reference

Body links (43): `pelvis`, `torso_link`, `head_link`, `imu_link`, `logo_link`,
`pelvis_contour_link`, and left/right pairs of `hip_pitch_link`, `hip_roll_link`,
`hip_yaw_link`, `knee_link`, `ankle_pitch_link`, `ankle_roll_link`,
`shoulder_pitch_link`, `shoulder_roll_link`, `shoulder_yaw_link`, `elbow_pitch_link`,
`elbow_roll_link`, `palm_link`, and the finger links `zero/one/two/three/four/five/six`.

Joint groups:

- **Legs (per side):** `hip_pitch_joint`, `hip_roll_joint`, `hip_yaw_joint`,
  `knee_joint`, `ankle_pitch_joint`, `ankle_roll_joint`
- **Torso:** `torso_joint`
- **Arms (per side):** `shoulder_pitch_joint`, `shoulder_roll_joint`,
  `shoulder_yaw_joint`, `elbow_pitch_joint`, `elbow_roll_joint`
- **Hands (per side):** `zero/one/two/three/four/five/six_joint`

The locomotion task primarily actuates the legs and torso; arm and finger joints are
regularized toward their default pose via joint-deviation penalties.
