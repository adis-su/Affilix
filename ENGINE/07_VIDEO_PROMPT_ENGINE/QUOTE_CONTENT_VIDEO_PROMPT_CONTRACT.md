# Affilix Quote Content Video Prompt Contract

## Canonical Identity

- Canonical workflow stage: Stage 09 — Video Prompt
- Content mode: `QUOTE_CONTENT`
- Universal implementation: `ENGINE/07_VIDEO_PROMPT_ENGINE/`

This contract is for editorial quote-led videos. It does not invoke product-demo logic and does not alter the UGC video branch.

## Applicability

Required for `CINEMATIC_QUOTE_REELS`, `RELATABLE_STORY_REELS`, `POV_RELATIONSHIP_REELS`, and `MINI_STORYTELLING_REELS`. `QUOTE_IMAGE` must skip Stage 09 with `STATIC_IMAGE_FORMAT`. Unsupported formats block with `QUOTE_CONTENT_FORMAT_UNSUPPORTED`.

## Dependencies

Current Stage 06 Storyboard and Stage 07 Visual Prompt are required. Stage 08 Voice Script is required only when the selected audio mode requires authored spoken or external dialogue. For silent/no-spoken output, do not invent dialogue or Voice Generation Reference.

## Count Invariant

The number of user-facing Video Prompts must equal the number of Storyboard scenes exactly. Emit exactly one standalone `VIDEO PROMPT` Markdown code block per scene, in scene order. Multiple references or generation segments inside a scene never create extra user-facing Video Prompts.

`video_prompt_count = storyboard_scene_count`

A mismatch blocks Stage 09 completion.

## Prompt Structure

Each scene's standalone code block must include:

```text
VIDEO PROMPT

SCENE
START REFERENCE
ACTION BEATS
PRIMARY ACTION
SECONDARY NATURAL MOTION
PRODUCT INTERACTION
GAZE & EXPRESSION
CAMERA BEHAVIOR
TARGET REFERENCE
END STATE
DIALOGUE SYNC
CONTINUITY
NEGATIVE MOTION CONSTRAINTS
FINAL VIDEO GENERATION INSTRUCTION
```

For editorial-only formats, `PRODUCT INTERACTION: NOT APPLICABLE` unless a relevant non-product prop is part of the storyboard. Do not fabricate a product role or force affiliate-style demonstrations.

## Motion and Editorial Causality

Every scene prompt must implement the storyboard's ordered action beats and reference trajectory. Explain trigger → intention → action → physical/emotional consequence → target state. Include motivated body movement, hand motion where relevant, gaze, restrained expression changes, bounded micro-motion, and camera response. “Move naturally” is never sufficient.

Do not add a new event, quote, personal confession, threat, reconciliation, or emotional conclusion that is absent from the storyboard. Do not turn coercion or abuse into a harmless communication misunderstanding. On-screen text must follow storyboard timing and remain readable; no unrequested text should appear.

Bridge references are immutable. A segment's start and target references must resolve to the same versions as the canonical reference graph. If a reference changes, affected transitions become stale.

## Exact Duration Composition

Supported generation segment durations are `[4, 6, 8, 10]` seconds under `EXACT_SEGMENT_COMPOSITION`. The sum of all segment durations must equal the requested final duration exactly. No rounding, truncation, extension, or filler. If impossible, set `duration_feasibility: BLOCKED` and do not produce a falsely complete video plan.

Generation segments are technical subparts of a scene, not additional scenes or prompts. Each segment must declare start reference, target reference, contained transitions, primary action, action causality, timing guidance, camera behavior, and continuity constraints.

## Output Shape

```yaml
stage: 09_VIDEO_PROMPT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT
audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
scenes:
  - scene_id:
    video_prompt_id:
    user_facing_prompt_count: 1
    creative_duration:
    reference_trajectory:
      ordered_reference_ids: []
      critical_reference_ids: []
      protected_transitions: []
    final_prompt:
    generation_segments:
      - segment_id:
        generation_duration: 4 | 6 | 8 | 10
        start_reference_id:
        target_reference_id:
        transition_ids: []
        action_causality:
          trigger:
          intention:
          physical_or_emotional_result:
        primary_action:
        secondary_motion: []
        gaze_path:
        expression_behavior:
        camera_behavior:
        dialogue_sync: []
        continuity_requirements: []
        negative_motion_constraints: []
validation:
  format_mechanism: PASS | NEEDS_REFINEMENT | BLOCKED
  scene_prompt_count: PASS | NEEDS_REFINEMENT
  reference_fidelity: PASS | NEEDS_REFINEMENT | BLOCKED
  motion_causality: PASS | NEEDS_REFINEMENT | BLOCKED
  dialogue_sync: PASS | NEEDS_REFINEMENT | NOT_REQUIRED
  timing: PASS | NEEDS_REFINEMENT
  duration_feasibility: PASS | BLOCKED
unresolved_requirements: []
source_artifacts: []
provenance: []
source_commit_sha:
```

## Invalidation

Changes to strategy, hook, storyboard, visual references, duration, audio mode, or voice script when required invalidate affected video prompts. Complete and wait for `/next` only after validation.
