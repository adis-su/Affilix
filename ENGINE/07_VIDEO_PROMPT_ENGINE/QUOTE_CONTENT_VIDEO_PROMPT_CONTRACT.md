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

## Cross-Stage Source Integrity

Stage 09 must verify that Stage 06, Stage 07, and (when required) Stage 08 are current artifacts for the same campaign and compatible repository snapshot. The Stage 07 artifact must identify the exact Stage 06 storyboard artifact/version it rendered. The Stage 08 artifact must identify the exact Stage 06 storyboard artifact/version whose dialogue anchors it followed. Compare these upstream references before prompt generation; do not infer compatibility solely from matching scene names or visually similar states.

If any required artifact is missing, stale, tied to a different storyboard artifact/version, or generated from an incompatible pinned source snapshot, block Stage 09 with a dependency validation failure and identify the mismatched artifact. Do not repair mismatches by rewriting dialogue, silently substituting reference states, or regenerating only one branch against an older storyboard.

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

## Default Direct-to-Camera Generation Behavior

For every Quote Content video format, the default `delivery_mode` is `DIRECT_TO_CAMERA_TALKING_HEAD`. The creator remains the primary on-screen subject and addresses the lens in a vertical 9:16 medium close-up or close-up. Use stable, eye-level framing and only motivated subtle reframing. Do not generate montage, unrelated B-roll, cinematic cutaways, extra characters, or acted relationship scenes as a substitute for the creator speaking directly to the viewer unless the user explicitly requests a different treatment.

When `audio_mode = SPOKEN_ON_CAMERA`, the creator visibly speaks the exact Stage 08 canonical dialogue with synchronized mouth movement, line timing, natural conversational cadence, and intentional pauses. Gaze primarily holds the lens; brief gaze breaks, blinks, breathing, small head movements, posture adjustments, and purposeful hand gestures must be motivated and restrained. Expressions evolve in response to the spoken idea rather than cycling randomly. Preserve the same creator, wardrobe, setting, and framing logic across references. If `VOICE_OVER` or `NO_SPOKEN_VOICE` is explicitly selected, do not force lip-sync, but retain the direct-to-camera visual composition unless the user explicitly requests a different visual treatment.

## Motion and Editorial Causality

Every scene prompt must implement the storyboard's ordered action beats and reference trajectory. Explain trigger → intention → action → physical/emotional consequence → target state. Include motivated body movement, hand motion where relevant, gaze, restrained expression changes, bounded micro-motion, and camera response. “Move naturally” is never sufficient.

Do not add a new event, quote, personal confession, threat, reconciliation, or emotional conclusion that is absent from the storyboard. Do not turn coercion or abuse into a harmless communication misunderstanding. On-screen text must follow storyboard timing and remain readable; no unrequested text should appear.

Bridge references are immutable. A segment's start and target references must resolve to the same versions as the canonical reference graph. If a reference changes, affected transitions become stale.

## Exact Duration Composition

For `QUOTE_CONTENT` video formats, final duration is fixed at exactly 20 seconds and must use exactly two generation segments: Segment 1 = 10 seconds, Segment 2 = 10 seconds. Supported generation segment durations are `[4, 6, 8, 10]` seconds under `EXACT_SEGMENT_COMPOSITION`. Segment durations must sum to exactly 20 seconds. No rounding, truncation, extension, or filler. If impossible, set `duration_feasibility: BLOCKED` and do not produce a falsely complete video plan.

Generation segments are technical provider requests, not additional scenes or user-facing prompts. The segment plan is validated across the entire run, not independently per scene: it must contain exactly two segments total, each exactly 10 seconds, covering the final timeline `[0, 10]` and `[10, 20]` with no gap or overlap. The sum must be exactly 20 seconds. Each segment must declare its `segment_id`, `source_scene_ids`, final start/end times, start reference, target reference, contained transition IDs, primary action, action causality, timing guidance, camera behavior, and continuity constraints. A segment may cover transitions across scene boundaries when the storyboard timeline requires it; retain one user-facing Video Prompt per Storyboard scene regardless of segment allocation. If the current per-scene segment records cannot represent this run-wide plan unambiguously, block completion rather than silently changing scene count or duration.

## Output Shape

```yaml
stage: 09_VIDEO_PROMPT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT
audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
scenes:
  - scene_id:
    delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD | USER_OVERRIDE
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
        source_scene_ids: []
        final_start_time:
        final_end_time:
        generation_duration: 10
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
  source_freshness: PASS | BLOCKED
  dependency_alignment: PASS | BLOCKED
  format_mechanism: PASS | NEEDS_REFINEMENT | BLOCKED
  scene_prompt_count: PASS | NEEDS_REFINEMENT
  reference_fidelity: PASS | NEEDS_REFINEMENT | BLOCKED
  motion_causality: PASS | NEEDS_REFINEMENT | BLOCKED
  dialogue_sync: PASS | NEEDS_REFINEMENT | NOT_REQUIRED
  timing: PASS | NEEDS_REFINEMENT
  duration_feasibility: PASS | BLOCKED
  run_wide_segment_composition: PASS | BLOCKED
unresolved_requirements: []
source_artifacts: []
provenance: []
source_commit_sha:
```

## Invalidation

Changes to strategy, hook, storyboard, visual references, duration, audio mode, or voice script when required invalidate affected video prompts. `source_freshness` and `dependency_alignment` must both be `PASS` before Stage 09 can be marked `COMPLETED`. Complete and wait for `/next` only after validation.
