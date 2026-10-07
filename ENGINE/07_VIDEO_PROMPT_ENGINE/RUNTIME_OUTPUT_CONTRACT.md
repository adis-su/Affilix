## Canonical Stage Identity

- Canonical workflow stage: Stage 09
- Engine implementation path: `ENGINE/07_VIDEO_PROMPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Video Prompt Runtime Output Contract

## Output

```yaml
stage: 09_VIDEO_PROMPT
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
    video_prompt_id:
    user_facing_prompt_count: 1
    creative_duration:
    reference_trajectory:
      ordered_reference_ids: []
      critical_reference_ids: []
      protected_transitions: []
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

## Storyboard Authority

Stage 06 Storyboard is the canonical source for scene intent, action choreography, narrative timing, product causality, resulting states, and reference transitions. Video Prompt may elaborate motion and provider segmentation only within those constraints. It MUST NOT invent, remove, or semantically alter story-critical actions or states. A material mismatch requires Storyboard revision or marks this artifact STALE.

See `ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md`.

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

The user-facing Video Prompt count MUST equal the Storyboard scene count exactly.

- One Storyboard scene produces exactly one user-facing Video Prompt.
- Multiple generation segments inside one scene do not increase Video Prompt count.
- Multiple scenes must never be merged into one Video Prompt.
- `user_facing_prompt_count` is always `1` per scene.
- The final artifact contains one standalone Markdown code block for each scene, in scene order. Metadata remains outside the code blocks.

Prompt count validation:

```yaml
prompt_count_validation:
  scene_count:
  video_prompt_count:
  status: PASS | NEEDS_REFINEMENT
```

`video_prompt_count != scene_count` is `NEEDS_REFINEMENT` and blocks Stage 09 completion.

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
