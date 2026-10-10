# Affilix Quote Content Voice Script Contract

## Canonical Identity

- Canonical workflow stage: Stage 08 — Voice Script
- Content mode: `QUOTE_CONTENT`
- Universal implementation: `ENGINE/08_VOICE_SCRIPT_ENGINE/`

## Applicability

Stage 08 is conditional. Run it when the selected Quote Content format and audio mode require authored spoken dialogue or an external dialogue asset. If the brief explicitly selects no spoken voice and the format remains understandable without speech, mark Stage 08 `SKIPPED` with reason `NO_SPOKEN_VOICE_REQUIRED`. Static `QUOTE_IMAGE` always skips with `STATIC_IMAGE_FORMAT`.

Never manufacture a creator's personal testimony or imply a real first-person event. A clearly labeled fictional/illustrative narrator may speak in first person only when the brief explicitly establishes that framing.

## Required Inputs

Current Stage 01 editorial brief, Stage 02 context, Stage 04 strategy, Stage 05 hook when applicable, and Stage 06 storyboard for video formats. Stage 03 Creator is required only if an identified on-screen speaker is part of the brief. No product or product facts are required.

## Ownership

Voice Script owns exact spoken wording, speaker identity/role, pronunciation notes, delivery, timing, pauses, and voice performance plan. Video Prompt may synchronize the canonical script but must not rewrite it. The script must support the selected pillar, format, primary message, and takeaway without introducing a new narrative claim.

## Deterministic Storyboard Handoff

Stage 08 consumes only the current, validated Stage 06 artifact for the active campaign and repository snapshot. Record the storyboard artifact ID/version (or canonical source artifact reference) in `source_artifacts`; preserve its `source_commit_sha`. Do not use a stale storyboard or silently mix artifacts generated from different source commits.

Each dialogue line MUST bind to an existing storyboard `scene_id` and `dialogue_anchor` from a specific Stage 06 beat. The line's `dialogue_anchor` object must identify that anchor unambiguously using `beat_id` and, when a beat contains multiple anchors, `anchor_id`. Preserve the anchor's `semantic_intent`. Require numeric `start_time` and `end_time` in seconds on the final-video timeline, with `0 <= start_time < end_time <= 20`. The line interval must fit entirely inside the anchor's `action_window` and its owning scene window. The referenced `target_reference` must resolve to the exact declared `reference_id@reference_version` in Stage 06. No nearest-reference, missing-anchor, inferred-timing, or stale-artifact fallback is permitted.

Validate line-level intervals as well as total duration. Reject or refine any line that overlaps a storyboard-declared protected pause, critical reaction, or visually dependent action. Concurrent speech is allowed only when the storyboard explicitly permits it and it does not contradict the action's semantic intent. If a line cannot fit, first shorten or re-deliver the wording while preserving meaning; if that cannot satisfy the anchor, return `NEEDS_REFINEMENT` or `BLOCKED` as appropriate rather than editing Storyboard timing from Stage 08.

## Duration-Bound Spoken Word Budget

For Quote Content video formats, the final duration is fixed at exactly 20 seconds by the mode contract. Stage 01 must not ask the user to select a duration. The canonical generation composition is exactly two 10-second segments; do not substitute a provider segment duration for the final video duration.

Use an initial target of **38–44 spoken words total** across all narration and character dialogue for the 20-second video. As a drafting guide, distribute roughly 19–22 words into each 10-second segment, but allocate by meaning and action rather than forcing an exact per-segment quota. These are drafting targets, not a timing guarantee. Validate the complete script against measured/read-aloud pace, pauses, speaker changes, emotional beats, and storyboard dialogue anchors. The spoken script must fit within exactly 20 seconds without rushed delivery, arbitrary silence, filler, or omitted lines.

If the script falls outside its target range, revise wording and/or pause timing while preserving the strategy and storyboard. If a deliberate slower delivery or pause-heavy style warrants a different word count, record the rationale and validate that the complete spoken performance still fits the requested duration. Do not alter the requested duration to accommodate the script.

For `TEXT_ONLY` or other explicitly no-spoken-voice output, spoken-word targets do not apply. Validate on-screen text for legibility and available reading time instead. Static `QUOTE_IMAGE` has no video duration or voice script.

## Format and Editorial Rules

For every Quote Content video format, default to `delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD`. When `audio_mode = SPOKEN_ON_CAMERA`, write the script as words the on-screen creator says directly to the lens, in a conversational first- or second-person address as appropriate. It must sound like a person talking to a viewer, not like formal narration intended to sit over B-roll. Include restrained delivery cues and beat-level pauses; do not add filler merely to fill time. Stage 09 must preserve the exact canonical wording and synchronize visible mouth movement with each line's timing anchors.

- `CINEMATIC_QUOTE_REELS`: the creator speaks the central reflection directly to camera by default; on-screen text may emphasize the key phrase but must not compete with the spoken line.

- `RELATABLE_STORY_REELS`: the creator recounts the situation directly to camera, establishing the trigger and emotional turn without claiming it happened to the user unless the user said so.
- `POV_RELATIONSHIP_REELS`: the creator explains the perspective and communication insight directly to camera without caricature or false universal claims.
- `MINI_STORYTELLING_REELS`: the creator tells the story directly to camera; spoken beats follow the storyboard trigger, consequential action, and resulting state.
- `QUOTE_IMAGE`: no voice script.

Avoid universal claims about all spouses, fabricated quotation attribution, fake testimonials, unsupported diagnoses, guaranteed healing, and engagement bait that distorts the message. Abuse, coercion, threats, and fear must not be normalized as ordinary relationship conflict.

## Output Shape

```yaml
stage: 08_VOICE_SCRIPT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT | NO_SPOKEN_VOICE_REQUIRED
audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD | USER_OVERRIDE
dialogue:
  enabled: true | false
  delivery: NATIVE_PROVIDER | EXTERNAL_PROVIDER | NONE
  lines:
    - line_id:
      scene_id:
      source_beat_id:
      dialogue_anchor:
        beat_id:
        anchor_id: null | string
      speaker_role:
      exact_text:
      intended_meaning:
      start_time:
      end_time:
      delivery:
      pause_points: []
      pronunciation_notes: []
voice_performance_plan:
  pace:
  energy:
  emotional_range:
  restraint_notes:
validation:
  strategy_alignment: PASS | NEEDS_REFINEMENT
  storyboard_alignment: PASS | NEEDS_REFINEMENT
  anchor_resolution: PASS | NEEDS_REFINEMENT | BLOCKED
  source_freshness: PASS | BLOCKED
  provenance_and_non_fabrication: PASS | BLOCKED
  sensitivity: PASS | NEEDS_REFINEMENT | BLOCKED
  timing: PASS | NEEDS_REFINEMENT
unresolved_requirements: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Validation and Invalidation

For video formats, validate that final duration is exactly 20 seconds and generation composition is exactly `10 + 10` seconds. Check the combined spoken-word count against the initial 38–44 word target, unless a documented delivery rationale justifies a different count. Spoken text must fit the storyboard's timing and dialogue anchors. For every line, validate scene and source beat existence, exact anchor resolution, semantic-intent alignment, target reference ID/version resolution, numeric interval bounds, containment within the anchor action window and scene window, and absence of conflicts with protected pauses or critical visual actions. `anchor_resolution` and `source_freshness` must both be `PASS` before Stage 08 can be marked `COMPLETED`. Missing, stale, or contradictory dependencies must never be silently repaired by inventing a new anchor. Mark `NEEDS_REFINEMENT` when wording or timing can be corrected without changing the strategy/storyboard. Mark `BLOCKED` if duration is unsupported or coherent dialogue requires fabricated lived experience, unsupported factual claims, unsafe framing, or incompatible story changes.

Changes to topic, audience, strategy, hook, storyboard, speaker, audio mode, or delivery constraints invalidate affected voice assets. Mark completed and wait for `/next`.
