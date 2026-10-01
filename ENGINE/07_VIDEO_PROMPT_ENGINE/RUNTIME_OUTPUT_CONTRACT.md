# Affilix — Video Prompt Runtime Output Contract

## Stage Gate

Stage 07 Video Prompt is a production specification generated after current Stage 06 Storyboard approval. Visual Prompt approval is required for appearance continuity; Voice Script approval is not required because audio and visual specifications are parallel descendants.

## Output

```yaml
stage: 07_VIDEO_PROMPT
status: REVIEW
provider:
  provider_id:
  capability_profile_version:
  supported_generation_durations: []
  selected_generation_duration_policy:
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
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Duration Invariant

The sum of `creative_duration` equals the approved campaign duration. The sum of generation segment durations equals that same final duration. Provider limits may change segmentation, but never the approved creative duration.

## Rules

The storyboard owns scene intent and timing. Visual Prompt owns appearance. Video Prompt owns motion and technical generation segmentation. Voice Script owns wording.

Every segment must have a coherent start and end state. No filler motion may be introduced solely to consume provider duration. Provider capabilities must be explicitly supplied or marked UNKNOWN.

The artifact enters REVIEW and waits for approval before generation handoff.

## Invalidation

Changes to Storyboard, Visual Prompt, Creator, Product, Context, provider capability profile, or duration constraints invalidate Video Prompt as STALE.
