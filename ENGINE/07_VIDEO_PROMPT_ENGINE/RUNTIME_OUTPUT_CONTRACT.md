## Canonical Stage Identity

- Canonical workflow stage: Stage 10
- Engine implementation path: `ENGINE/07_VIDEO_PROMPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Video Prompt Runtime Output Contract

## Output

```yaml
stage: 10_VIDEO_PROMPT
status: COMPLETED
provider:
  provider_id:
  model_id:
  capability_profile_version:
  supported_generation_durations: [4, 6, 8, 10]
  selected_generation_duration_policy: EXACT_SEGMENT_COMPOSITION
scenes:
  - scene_id:
    creative_duration:
    generation_segments:
      - segment_id:
        final_start:
        final_end:
        generation_duration:
        start_state:
        primary_action:
        secondary_motion:
        camera_behavior:
        end_state:
        continuity_requirements: []
        negative_motion_constraints: []
    motion_intensity:
    dialogue_sync: []
validation:
  identity: PASS | NEEDS_REFINEMENT
  product: PASS | NEEDS_REFINEMENT
  motion: PASS | NEEDS_REFINEMENT
  timing: PASS | NEEDS_REFINEMENT
  continuity: PASS | NEEDS_REFINEMENT
  duration_feasibility: PASS | BLOCKED
unresolved_requirements: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Duration Invariant

Every generation segment must use exactly one of:

`4s | 6s | 8s | 10s`

The sum of all generation segment durations must equal the requested final duration exactly.

If exact composition is impossible, `duration_feasibility` is `BLOCKED`. Do not round or silently change the final duration.

## Ownership

- Storyboard owns creative scene intent and timing.
- Visual Prompt owns static appearance.
- Video Prompt owns motion and technical generation segmentation.
- Voice Script owns wording and delivery.

## Output Formatting

The user-facing video prompt itself must be one standalone Markdown code block. Metadata remains outside the code block.

## Invalidation

Changes to Storyboard, Visual Prompt, Creator, Product, Context, provider capability profile, or requested duration invalidate Video Prompt as STALE.


## Reference Transition Output

Every transition must declare:

```yaml
from_reference_id:
to_reference_id:
action_beats: []
primary_action:
secondary_motion: []
product_interaction:
gaze_path:
expression_behavior:
camera_behavior:
duration:
```

Every generation segment must declare `start_reference_id`, `target_reference_id`, and the transition IDs it contains. Bridge references must resolve to one immutable version across adjacent scenes.

Stage completion: process, validate, mark `COMPLETED`, then wait for `/next`. If a reference changes, all transitions touching it become `STALE`.
