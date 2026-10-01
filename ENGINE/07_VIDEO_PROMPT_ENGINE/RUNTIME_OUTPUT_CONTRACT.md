# Affilix — Video Prompt Runtime Output Contract

## Output

```yaml
stage: 08_VIDEO_PROMPT
status: REVIEW
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
  identity: PASS | REVIEW
  product: PASS | REVIEW
  motion: PASS | REVIEW
  timing: PASS | REVIEW
  continuity: PASS | REVIEW
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
