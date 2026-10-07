## Canonical Stage Identity

- Canonical workflow stage: Stage 07
- Engine implementation path: `ENGINE/05_STORYBOARD_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Storyboard Runtime Output Contract

## Output

```yaml
stage: 06_STORYBOARD
status: COMPLETED
metadata:
  storyboard_id:
  campaign_id:
  creator_id:
  product_id:
  platform:
  requested_duration:
  creative_duration:
  generation_segmentation_plan: []
  aspect_ratio:
  scene_count:
  primary_content_format:
  content_format_fit: eligible | conditional
  content_format_requirements: []
  primary_content_angle:
  primary_message:
  hook_id:
scenes: []
validation:
  content_format: PASS | NEEDS_REFINEMENT
  narrative: PASS | NEEDS_REFINEMENT
  identity: PASS | NEEDS_REFINEMENT
  product: PASS | NEEDS_REFINEMENT
  timing: PASS | NEEDS_REFINEMENT
  production: PASS | NEEDS_REFINEMENT
  duration_feasibility: PASS | BLOCKED
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Timing Invariant

Creative scene durations must sum exactly to requested_duration.

When video generation is required, generation segments must use only 4s, 6s, 8s, or 10s and must sum exactly to requested_duration.

If exact composition is impossible, duration_feasibility is BLOCKED and the requested duration is not changed silently.

Storyboard remains the canonical scene sequence for downstream Visual Prompt, Video Prompt, and Voice Script.


## Action and Reference Graph

The storyboard output must include an action graph and reference graph. A scene may contain multiple references.

```yaml
scenes:
  - scene_id:
    action_graph:
      beats:
        - beat_id:
          trigger:
          intention:
          action:
          resulting_state:
          body_motion:
          hand_motion:
          product_interaction:
          gaze:
          expression:
          camera_behavior:
          micro_motion:
          reference_after:
    reference_states:
      - reference_id:
        sequence_index:
        role: START | INTERMEDIATE | END | BRIDGE
        version:
        state: {}
        continuity_critical: []
    bridge_reference_id:
```

Bridge invariants: Scene N END and Scene N+1 START must resolve to the same reference version. Changing a bridge creates a new version and invalidates dependent downstream transitions.

Stage completion follows `PROCESS → VALIDATE → MARK COMPLETED → WAIT FOR /next`. `/next` is progression only, not approval.
