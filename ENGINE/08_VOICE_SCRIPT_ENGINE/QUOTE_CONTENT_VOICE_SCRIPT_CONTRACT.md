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

## Format and Editorial Rules

- `CINEMATIC_QUOTE_REELS`: speech is optional; if present, it supports the core statement and does not compete with on-screen text.
- `RELATABLE_STORY_REELS`: dialogue may establish the situation and emotional turn, but may not claim it happened to the user unless the user said so.
- `POV_RELATIONSHIP_REELS`: dialogue clarifies perspective and communication insight without caricature or false universal claims.
- `MINI_STORYTELLING_REELS`: spoken beats follow the storyboard trigger, consequential action, and resulting state.
- `QUOTE_IMAGE`: no voice script.

Avoid universal claims about all spouses, fabricated quotation attribution, fake testimonials, unsupported diagnoses, guaranteed healing, and engagement bait that distorts the message. Abuse, coercion, threats, and fear must not be normalized as ordinary relationship conflict.

## Output Shape

```yaml
stage: 08_VOICE_SCRIPT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason: null | STATIC_IMAGE_FORMAT | NO_SPOKEN_VOICE_REQUIRED
audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
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

Spoken text must fit the storyboard's timing and dialogue anchors. Mark `NEEDS_REFINEMENT` when wording or timing can be corrected without changing the strategy/storyboard. Mark `BLOCKED` if coherent dialogue requires fabricated lived experience, unsupported factual claims, unsafe framing, or incompatible story changes.

Changes to topic, audience, strategy, hook, storyboard, speaker, audio mode, or delivery constraints invalidate affected voice assets. Mark completed and wait for `/next`.
