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

## Quote Content Narrative and Performance Beats

For direct-to-camera quote videos, plan the spoken thought as a coherent progression rather than a stack of unrelated inspirational sentences. Use these narrative functions when they fit the selected format and message:

1. **HOOK / RECOGNITION** — continue the selected Stage 05 hook and establish the relatable thought or tension.
2. **DEVELOPMENT** — make the situation, contradiction, or emotional reality specific enough to feel recognizable.
3. **CORE INSIGHT** — deliver the central quote or point with clear semantic emphasis.
4. **PAYOFF / RESONANCE** — land a grounded reframe, consequence, or memorable final thought.

These are narrative functions, not mandatory beat or scene counts. One beat may serve more than one function, and the functions may be combined when the dialogue is short. Never pad the script just to fill a template. Preserve the selected format mechanism and the actual meaning of the Stage 05 hook.

For each dialogue-bearing beat, storyboard the delivery intention and timing: the semantic point, phrase or word to emphasize, intended pace, meaningful pause, and the visible action that supports the line. Stage 06 defines semantic anchors and performance timing; it MUST NOT author or silently replace the final spoken wording owned by Stage 08. Dialogue-bearing beats must leave enough time for plausible speech and any story-critical pause or reaction. Avoid assigning a new gesture to every sentence.

Emotional progression must follow the meaning of the line. Define the starting expression, motivated change, and resulting expression where material. Keep gestures purposeful and restrained; maintain direct lens gaze by default, allowing brief gaze breaks only when motivated. Bound micro-motion to plausible breathing, blinking, small posture/weight shifts, and minor hand or clothing adjustments. The creator remains visibly speaking on camera when `audio_mode = SPOKEN_ON_CAMERA`; do not require lip-sync for `VOICE_OVER` or `NO_SPOKEN_VOICE`.

Storyboard validation for Quote Content must explicitly check narrative progression, hook continuity, dialogue-to-action alignment, emotional plausibility, direct-to-camera treatment, and absence of filler or unrelated cutaways.

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

Every video scene MUST declare a complete, ordered Reference Plan and Reference Trajectory before Stage 06 can be marked `COMPLETED`. Do not leave reference metadata for Stage 07 to infer or invent.

Every declared reference state MUST include:
- `source_scene_id`: the canonical owning scene ID for this state. It must resolve to an existing scene in this exact storyboard artifact. A shared bridge may be referenced at both scene boundaries, but remains one canonical state identity/version with explicit boundary mapping; do not create a second independent state.
- `reference_id`: unique, stable ID within the active storyboard run (for example `R01`).
- `reference_version`: explicit version, initialized to `v1` for a new state.
- `sequence_index`: unique, contiguous order within the scene, starting at 1.
- `reference_role`: `START`, `INTERMEDIATE`, `END`, or `BRIDGE`.
- `source_beat_id`: an existing beat ID from the same scene that causes or establishes this state.
- `state_summary`: one concrete frozen visual state, not a motion sequence.
- `continuity_invariants`: the identity, framing, wardrobe/environment inheritance, and other attributes that must remain unchanged.
- `critical_state`: whether the state is required to preserve a material action or continuity change.

Every scene MUST also include `reference_trajectory.ordered_reference_ids` in the same order as its Reference Plan, plus explicit transition records connecting each adjacent state. Each transition records a `transition_id`, `from_reference_id`, `to_reference_id`, `source_beat_id`, the causal action, allowed changes, invariants, and resulting state. Every `action_graph.beats[].reference_after` must resolve to a declared reference in that scene. No dangling IDs, duplicate sequence indices, missing beat references, or unordered trajectories are allowed.

A shared scene-boundary bridge MUST resolve to the exact same `reference_id` and `reference_version` at the end of Scene N and start of Scene N+1. For example, if Scene 01 ends at `R03@v1`, Scene 02 MUST start at `R03@v1`; it is invalid to label the same bridge `R03` in one scene and `R04` in the next, or to create two independent state records that merely look alike. The shared bridge is one canonical state, referenced by both scenes. Its source beat must be traceable to the beat that establishes the boundary state; scene-local beat mapping must explicitly resolve to that shared state. Do not duplicate or independently regenerate the bridge state. Revising a bridge version invalidates all transitions that touch it and all dependent downstream artifacts.

Reference states are frozen visual checkpoints, not generation segments. One scene can have multiple reference states and multiple technical generation segments, but it remains one scene. Reference count is driven by meaningful action complexity, not a fixed quota; high-complexity scenes may target six states when justified.

## Duration

For `QUOTE_CONTENT` video formats, the requested final duration MUST be one of `18`, `28`, or `30` seconds. The requested duration is the source of truth and must not be silently changed. Compose provider generation segments using only `4`, `6`, `8`, or `10` seconds, with exact total duration: `18 = 8 + 10`, `28 = 10 + 10 + 8`, and `30 = 10 + 10 + 10`. Creative scene durations must also sum exactly to the requested duration. Segment boundaries belong to the downstream Video Prompt implementation plan; they must follow meaningful action/narrative boundaries and must not force unnecessary scene changes. No rounding, truncation, extension, or filler. If the requested duration is outside the supported set or exact composition is impossible, set `duration_feasibility: BLOCKED` and report the reason; do not substitute another duration.

## Output Shape

```yaml
stage: 06_STORYBOARD
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT
metadata:
  storyboard_id: required stable ID for this storyboard artifact
  storyboard_version: required explicit version, initialized to v1 and incremented on material revision
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
          time_window:
            start_time:
            end_time:
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
          dialogue_anchor:
            semantic_intent:
            action_window:
              start_time:
              end_time:
            target_reference:
          text_or_dialogue_anchor:
          reference_after:
    reference_plan:
      reference_density: LOW | MEDIUM | HIGH | VERY_HIGH
      target_reference_count:
      rationale:
      states:
        - reference_id:
          reference_version: v1
          source_scene_id: required; must equal the owning scene_id, including explicit bridge mapping
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

## Beat Timing and Dialogue Anchor Contract

For every video beat, `time_window.start_time` and `time_window.end_time` are required numeric seconds relative to the start of the requested final video. Require `0 <= start_time < end_time <= metadata.requested_duration`, where the requested duration is exactly `18`, `28`, or `30` seconds. Beat windows must be chronologically ordered; overlap is allowed only when the beat explicitly identifies concurrent motion channels and the causal order remains clear. Scene durations must sum exactly to `metadata.requested_duration`, and each beat window must fit wholly inside its owning scene window.

When spoken dialogue is required, each dialogue-bearing beat MUST declare `dialogue_anchor.semantic_intent`, `dialogue_anchor.action_window.start_time`, `dialogue_anchor.action_window.end_time`, and `dialogue_anchor.target_reference`. The action window must be non-empty, fall within the owning beat and scene windows, and point to a declared reference state established by that beat or its explicitly declared transition. `target_reference` must resolve to the exact `reference_id@reference_version`; no guessed or nearest-state fallback is allowed. Beats without spoken dialogue may omit `dialogue_anchor` or set it to `null`.

Stage 08 must bind each dialogue line to a storyboard `scene_id` and `dialogue_anchor`, preserve the anchor's semantic intent, and keep the line's `start_time`/`end_time` inside the anchor action window. A line may reference an anchor only if that anchor exists in the current Stage 06 artifact. Dialogue may overlap a beat only when it does not obscure a required silent pause, critical reaction, or visually dependent action. If dialogue timing cannot fit, Stage 08 must revise wording/delivery or mark `NEEDS_REFINEMENT`; it must not move the storyboard window or change the final duration. If the anchor cannot be resolved without inventing creative intent, block the affected output.

## Artifact Identity and Provenance

Every non-skipped video storyboard artifact MUST expose a stable, non-empty `metadata.storyboard_id` and explicit `metadata.storyboard_version`. Initialize a new artifact at `v1`; increment the version when any material storyboard content or reference graph changes. The pair `(storyboard_id, storyboard_version)` identifies the exact artifact version. `source_commit_sha` identifies repository source, not the storyboard artifact, and MUST NOT be used as a substitute for artifact identity. Every scene/state source reference must resolve within this exact artifact. Record upstream `source_artifacts` with artifact IDs and versions where available. `QUOTE_IMAGE` remains `SKIPPED` and does not require a temporal storyboard artifact.

## Reference Graph Cardinality and Canonicalization

For each scene with `n` ordered reference states, `reference_trajectory.ordered_reference_ids` MUST contain exactly those `n` states in the same order as `reference_plan.states`; the scene must contain exactly `max(0, n - 1)` internal transition records, one for each adjacent pair and no duplicate pair. Every transition's `from_reference_id` and `to_reference_id` must match the corresponding adjacent IDs. Every beat's `reference_after` must resolve to a state ID and explicit version in the same storyboard artifact; use a structured reference `{ reference_id, reference_version }` where supported, otherwise require a documented unambiguous ID-to-version resolution. A bridge is a single canonical `(reference_id, reference_version)` reused at the preceding scene's END and following scene's START; the boundary mapping must not create two independently versioned states. `source_scene_id` and `source_beat_id` must resolve to the owning scene and an existing beat, respectively.

## Validation and Invalidation

Complete only when the format mechanism, causal story progression, sensitivity, timing, and reference graph pass. Reference-graph validation MUST verify that every reference has a non-empty ID/version/source beat/state summary and continuity invariants, sequence indices are unique and contiguous within each scene, every source beat exists in the same scene and establishes the stated state, the ordered trajectory exactly matches the Reference Plan, each adjacent state pair has exactly one resolvable transition, every transition has an ID/source beat/causal action/allowed changes/invariants/resulting state, every beat's `reference_after` resolves to a declared state in that same scene, and bridge ID/version pairs match across scene boundaries. The shared bridge must be represented as one canonical reference identity/version, not two independent references with equivalent summaries. If the story is feasible but these fields can be generated from existing storyboard beats, generate them during Stage 06 before validation. Do not defer metadata creation to Stage 07. Mark `NEEDS_REFINEMENT` for a feasible but underspecified story; mark `BLOCKED` only when a required state/transition cannot be established without inventing creative facts, continuity is impossible, a critical dependency is missing, or exact duration is infeasible.

Changes to brief, editorial context, strategy, hook, creator identity when used, duration, or a reference state invalidate affected storyboard elements and all dependent downstream artifacts. After validation, mark the stage complete and wait for `/next`.
