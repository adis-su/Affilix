# Affilix Quote Content Storyboard Contract

## Canonical Identity

- Canonical workflow stage: Stage 06 — Storyboard
- Content mode: `QUOTE_CONTENT`
- Universal implementation: `ENGINE/05_STORYBOARD_ENGINE/`
- Stage registry: `ENGINE/WORKFLOW.md`

This contract extends the universal Storyboard engine for quote-led editorial video. It does not create a new stage and must not alter the existing UGC branch.

## Applicability

- `QUOTE_IMAGE`: Stage 06 is `SKIPPED` with reason `STATIC_IMAGE_FORMAT`. Do not invent a temporal storyboard.
- `CINEMATIC_QUOTE_REELS`, `RELATABLE_STORY_REELS`, `POV_RELATIONSHIP_REELS`, `MINI_STORYTELLING_REELS`: Stage 06 is required.
- Unknown or unregistered formats: `BLOCKED` with `QUOTE_CONTENT_FORMAT_UNSUPPORTED`.

## Required Inputs

Current Stage 01 editorial brief, Stage 02 editorial context, Stage 04 Quote Content Strategy, and Stage 05 Hook when required. Creator is optional unless the strategy explicitly requires a visible persona. No product or product interaction is required.

## Default Direct-to-Camera Talking-Head Treatment

All Quote Content video formats default to `DIRECT_TO_CAMERA_TALKING_HEAD`. The creator speaks directly to the lens as the primary storytelling channel; format differences are expressed through the spoken narrative, gaze, expression, gestures, and motivated timing, not by automatically switching to montage or acted scenes. Preserve this treatment across scenes unless the user explicitly requests a different visual treatment.

Storyboard every beat as a causal performance process: trigger/intention for the line → visible delivery/action → emotional or informational result → resulting reference state. Specify the creator's body posture, purposeful hand gesture, gaze to lens or brief motivated gaze break, expression progression, micro-motion, and restrained camera behavior. A speaker may pause, breathe, glance briefly away to recall a thought, then return gaze to the lens when motivated; avoid constant motion, exaggerated acting, random gestures, and unexplained camera movement. Keep the creator visually present and speaking on camera when `audio_mode = SPOKEN_ON_CAMERA`. When `VOICE_OVER` or `NO_SPOKEN_VOICE` is explicitly selected, preserve the direct-to-camera composition by default but do not require visible lip-sync.

## Editorial Story Mechanism

Preserve the selected format's mechanism. A relationship or reflective story must not be turned into a product-demo structure. Under the default talking-head treatment, communicate that mechanism through the creator's direct spoken delivery, expressions, gestures, and controlled changes of state rather than unrelated cutaways.

| Format | Required scene progression |
|---|---|
| `CINEMATIC_QUOTE_REELS` | central statement/question → visual/emotional development → readable takeaway |
| `RELATABLE_STORY_REELS` | recognizable trigger → escalating but plausible moment → emotional recognition or grounded reframe |
| `POV_RELATIONSHIP_REELS` | clearly established POV → interpersonal action/reaction → specific communication insight or unresolved realistic beat |
| `MINI_STORYTELLING_REELS` | concrete trigger → consequential action/reaction → meaningful resulting state |

These are story functions, not mandatory scene counts. The storyboard determines scene count from the requested duration and creative need.

## Action Choreography

Each scene is a process of action over time, not a sequence of unrelated poses. For every meaningful beat specify:

- trigger and intention
- primary action and physical/emotional consequence
- body and hand movement where applicable
- gaze path and expression change
- bounded secondary micro-motion
- camera behavior and motivation
- resulting state
- dialogue/text anchor when relevant
- transition into the next beat

Use causal progression: `TRIGGER → INTENTION → ACTION → RESULTING STATE`. Do not invent abuse, coercion, threats, personal testimony, or specific biographical facts. Sensitive relationship dynamics must not be reframed as ordinary miscommunication.

## Reference Graph

Every video scene declares an ordered Reference Plan and Reference Trajectory. Use as many meaningful states as action complexity warrants. High-complexity scenes should target six references when justified; this is not a quota and never changes scene count.

A bridge reference is immutable. If Scene N END and Scene N+1 START use the same reference, both must point to the same reference ID and version. A changed bridge version invalidates every dependent transition and downstream prompt.

Reference states are not generation segments. One scene can have multiple reference states and multiple technical generation segments, but it remains one scene.

## Duration

The requested final duration is authoritative. Creative scene durations must sum exactly to it. Video generation segment durations may only be 4, 6, 8, or 10 seconds and must sum exactly to the requested final duration. No rounding, truncation, extension, or filler. If exact composition is impossible, set `duration_feasibility: BLOCKED`.

## Output Shape

```yaml
stage: 06_STORYBOARD
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT
metadata:
  strategy_id:
  hook_id:
  format_id:
  delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD | USER_OVERRIDE
  requested_duration:
  creative_duration:
  scene_count:
  source_commit_sha:
scenes:
  - scene_id:
    scene_purpose:
    delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD | USER_OVERRIDE
    duration:
    hook_continuation:
    action_graph:
      beats:
        - beat_id:
          trigger:
          intention:
          action:
          resulting_state:
          body_motion:
          hand_motion:
          gaze:
          expression:
          camera_behavior:
          micro_motion:
          text_or_dialogue_anchor:
          reference_after:
    reference_plan:
      target_reference_count:
      rationale:
      states:
        - reference_id:
          reference_role: START | INTERMEDIATE | END | BRIDGE
          reference_version:
          source_beat_id:
          state_summary:
    transitions: []
    continuity_invariants: []
validation:
  format_mechanism: PASS | NEEDS_REFINEMENT | BLOCKED
  narrative_causality: PASS | NEEDS_REFINEMENT | BLOCKED
  sensitivity: PASS | NEEDS_REFINEMENT | BLOCKED
  reference_graph: PASS | NEEDS_REFINEMENT | BLOCKED
  timing: PASS | NEEDS_REFINEMENT | BLOCKED
  duration_feasibility: PASS | BLOCKED
unresolved_requirements: []
provenance: []
source_artifacts: []
```

## Validation and Invalidation

Complete only when the format mechanism, causal story progression, sensitivity, timing, and reference graph pass. Mark `NEEDS_REFINEMENT` for a feasible but underspecified story; mark `BLOCKED` for unsupported or unsafe framing, impossible continuity, missing critical dependencies, or infeasible exact duration.

Changes to brief, editorial context, strategy, hook, creator identity when used, duration, or a reference state invalidate affected storyboard elements and all dependent downstream artifacts. After validation, mark the stage complete and wait for `/next`.
