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

## Duration-Bound Spoken Word Budget

For Quote Content video formats, Stage 01 must supply a requested final duration of exactly 18, 28, or 30 seconds. The selected duration is the source of truth for the spoken script; do not substitute a provider segment duration for the final video duration.

Use these initial target ranges for all spoken words combined across narration and character dialogue:
- 18 seconds: 35–42 words.
- 28 seconds: 55–65 words.
- 30 seconds: 60–70 words.

These ranges assume conversational delivery around 130–140 words per minute and are drafting targets, not a timing guarantee. Validate the actual script against measured/read-aloud pace, pauses, speaker changes, emotional beats, and storyboard dialogue anchors. The spoken script must fit within the exact final duration without rushed delivery, arbitrary silence, filler, or omitted lines.

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
      dialogue_anchor:
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
  provenance_and_non_fabrication: PASS | BLOCKED
  sensitivity: PASS | NEEDS_REFINEMENT | BLOCKED
  timing: PASS | NEEDS_REFINEMENT
unresolved_requirements: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Validation and Invalidation

For video formats, validate the selected duration is exactly 18, 28, or 30 seconds and check the combined spoken-word count against the corresponding initial target range, unless a documented delivery rationale justifies a different count. Spoken text must fit the storyboard's timing and dialogue anchors. Mark `NEEDS_REFINEMENT` when wording or timing can be corrected without changing the strategy/storyboard. Mark `BLOCKED` if duration is unsupported or coherent dialogue requires fabricated lived experience, unsupported factual claims, unsafe framing, or incompatible story changes.

Changes to topic, audience, strategy, hook, storyboard, speaker, audio mode, or delivery constraints invalidate affected voice assets. Mark completed and wait for `/next`.
