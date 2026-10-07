## Canonical Stage Identity

- Canonical workflow stage: Stage 08
- Engine implementation path: `ENGINE/07_VIDEO_PROMPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Video Prompt Runtime Output Contract

## Output

```yaml
stage: 08_VIDEO_PROMPT
status: COMPLETED
content_format_constraint:
  format_id:
  format_name:
  format_fit: eligible | conditional
  format_requirements: []
audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
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
        start_state_invariants: []
        primary_action:
        secondary_motion:
        action_causality:
        temporal_priority:
          critical_beats: []
          timing_guidance: []
        camera_behavior:
        target_state_invariants: []
        end_state:
        continuity_requirements: []
        negative_motion_constraints: []
    motion_intensity:
    dialogue_sync: []
validation:
  content_format: PASS | NEEDS_REFINEMENT
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

## Audio Mode Invariant

`audio_mode` is inherited from Campaign Intake and is authoritative.

- `SPOKEN_ON_CAMERA`: Dialogue Sync may include exact creator dialogue, lip-sync, and Voice Generation Reference.
- `VOICE_OVER`: Dialogue Sync may include canonical voice-over timing and Voice Generation Reference; do not require visible creator lip-sync.
- `NO_SPOKEN_VOICE`: Dialogue Sync must contain no spoken dialogue, no lip-sync requirement, and no Voice Generation Reference. Video Prompt must not invent or rewrite spoken content.

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

Changes to Content Format, Storyboard, Visual Prompt, Creator, Product, Context, Campaign `audio_mode`, provider capability profile, or requested duration invalidate Video Prompt as STALE.


## Reference Transition Output

Every transition must declare:

```yaml
from_reference_id:
to_reference_id:
action_beats: []
action_causality:
  trigger:
  intention:
  physical_result:
primary_action:
secondary_motion: []
temporal_priority:
  critical_beats: []
  timing_guidance: []
product_interaction:
gaze_path:
expression_behavior:
camera_behavior:
duration:
```

Every generation segment must declare `start_reference_id`, `target_reference_id`, and the transition IDs it contains. Bridge references must resolve to one immutable version across adjacent scenes.

Stage completion: process, validate, mark `COMPLETED`, then wait for `/next`. If a reference changes, all transitions touching it become `STALE`.
