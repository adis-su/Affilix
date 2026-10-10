## Canonical Stage Identity

- Canonical workflow stage: Stage 06
- Engine implementation path: `ENGINE/05_STORYBOARD_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Storyboard Runtime Output Contract

## Output

```yaml
stage: 06_STORYBOARD
status: COMPLETED
metadata:
  storyboard_id: required stable artifact ID
  storyboard_version: required explicit artifact version, initialized to v1 and incremented on material revision
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
scenes:
  - scene_id:
    reference_plan:
      reference_density: LOW | MEDIUM | HIGH | VERY_HIGH
      target_reference_count:
      rationale:
      states:
        - reference_id:
          reference_version: v1
          source_scene_id: required owning scene ID
          sequence_index:
          reference_role: START | INTERMEDIATE | END | BRIDGE
          source_beat_id:
          state_summary:
          continuity_invariants: []
          critical_state: true | false
    action_graph:
      beats: []
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

Storyboard remains the canonical creative production blueprint for downstream Visual Prompt, Video Prompt, and Voice Script. See `DOWNSTREAM_AUTHORITY_CONTRACT.md`. Downstream artifacts may elaborate implementation detail but MUST NOT introduce new creative decisions or silently alter Storyboard state.


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
        reference_version: v1
        source_scene_id:
        sequence_index:
        reference_role: START | INTERMEDIATE | END | BRIDGE
        source_beat_id:
        state_summary:
        continuity_invariants: []
        critical_state: true | false
    reference_trajectory:
      ordered_reference_ids: []
      transitions:
        - transition_id:
          from_reference_id:
          to_reference_id:
          source_beat_id:
          causal_action:
          allowed_changes: []
          invariants: []
          resulting_state:
    bridge_reference_id:
```

Artifact identity invariants: `metadata.storyboard_id` and `metadata.storyboard_version` are required for every completed video storyboard; `source_commit_sha` is not a substitute for artifact identity. Every reference state must explicitly include `source_scene_id`, which resolves to the canonical owning scene in this artifact. Bridge invariants: Scene N END and Scene N+1 START must resolve to the exact same `reference_id` and `reference_version`; e.g. `R03@v1` at both ends, never `R03` and `R04` as independent states. The bridge is one canonical continuity anchor shared by both scenes. Every reference state must have an explicit ID, version, contiguous scene-local sequence index, role, valid source beat, frozen state summary, and continuity invariants. Every adjacent pair must have a transition record containing transition ID, source beat, causal action, allowed changes, invariants, and resulting state. Every `reference_after` must resolve to a state declared in its own scene and exact storyboard artifact version. Each scene's ordered trajectory must match its Reference Plan exactly and contain exactly n−1 transition records for n states, one per adjacent pair. Validate that the ordered trajectory matches the declared Reference Plan and reject dangling IDs, invalid source beats, duplicate sequence indices, missing transitions, or mismatched bridge ID/version pairs. Changing a bridge creates a new version and invalidates dependent transitions and downstream artifacts.

Stage completion follows `PROCESS → VALIDATE → MARK COMPLETED → WAIT FOR /next`. `/next` is progression only, not approval.


## Mode-Specific Schema Dispatch

For `content_mode = QUOTE_CONTENT`, the authoritative Stage 06 schema and applicability rules are in `QUOTE_CONTENT_STORYBOARD_CONTRACT.md`. Use that contract's output shape and explicit static-image skip. Do not force Quote Content into product-oriented Storyboard fields. For `UGC_AFFILIATE`, this existing universal output contract remains in force.


## Mandatory Complete Artifact Provenance

A completed Stage 06 video artifact MUST include all of the following; empty placeholders are invalid:

- `metadata.storyboard_id`: stable, non-empty artifact identifier.
- `metadata.storyboard_version`: explicit version for this artifact, initially `v1`.
- `source_commit_sha`: exact repository commit pinned for the active run.
- `source_artifacts`: one provenance record for every required upstream artifact actually consumed, with at minimum `stage_id`, `artifact_id`, `artifact_version`, and `content_mode`; include source commit/hash when available. Required upstream records must identify the current Stage 04 Strategy and Stage 05 Hook, plus Stage 01/02 and Stage 03 when consumed by the active mode and creative configuration. Do not fabricate unavailable IDs or versions: mark the dependency unresolved and block completion until it is resolved.
- `provenance`: field-level or artifact-level origin records sufficient to trace creative decisions to their upstream source artifact and version.

The active storyboard's `metadata.storyboard_id` + `metadata.storyboard_version` is the artifact identity. `source_commit_sha` is repository provenance only and must never substitute for artifact identity or upstream artifact provenance.

For every scene, the Reference Plan is canonical. If it declares states `R01@v1` through `R05@v1`, the scene's `reference_trajectory.ordered_reference_ids` MUST resolve to exactly `[R01@v1, R02@v1, R03@v1, R04@v1, R05@v1]` in that order. The scene MUST contain exactly four causal transition records: R01→R02, R02→R03, R03→R04, and R04→R05. Each record must state its source beat, causal action, allowed changes, invariants, and resulting state. Every action beat's `reference_after` must explicitly resolve to a declared `reference_id` and `reference_version`; missing, implicit, dangling, or guessed mappings fail validation. This five-state example is a cardinality/order rule, not permission to invent state content absent from the source beats.

Completion gate: do not mark Stage 06 `COMPLETED` if artifact identity, pinned source commit, required upstream provenance, any required state field, trajectory ordering, transition causality, or beat-to-reference mapping is missing or invalid. Generate metadata from known current artifacts where possible; otherwise mark `NEEDS_REFINEMENT` or `BLOCKED` according to the existing contract. After completion, wait for `/next`.
