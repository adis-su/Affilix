## Canonical Stage Identity

- Canonical workflow stage: Stage 08
- Engine implementation path: `ENGINE/08_VOICE_SCRIPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Voice Script Runtime Output Contract

## Stage Gate

Stage 08 executes when spoken dialogue is required, including `NO_SPOKEN_VOICE` with `dialogue.enabled=true` and `dialogue.delivery=EXTERNAL_PROVIDER`, and only after current Stage 06 Storyboard is current and validated.

When `audio_mode` is `NO_SPOKEN_VOICE` and external dialogue is disabled, Stage 08 must not generate a placeholder or invented script. Its valid runtime state is `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE`. Visual Prompt is a parallel Storyboard descendant and is not a prerequisite for Voice Script.

## Output

```yaml
stage: 08_VOICE_SCRIPT
status: COMPLETED
content_format_constraint:
  format_id:
  format_name:
  format_fit: eligible | conditional
  format_requirements: []
metadata:
  audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER | NO_SPOKEN_VOICE
  dialogue_enabled: true | false
  dialogue_delivery: NATIVE_PROVIDER | EXTERNAL_PROVIDER | NONE
  script_id:
  creator_id:
  campaign_id:
  language:
  language_mix:
  delivery_style:
  overall_tone:
  approximate_speaking_pace:
  total_spoken_duration:
scenes:
  - scene_id:
    dialogue_type: Spoken | Voice-over | None
    exact_dialogue:
    delivery_intent:
    emotion:
    pace:
    emphasis: []
    pause_points: []
    pronunciation_notes: []
    lip_sync_priority:
validation:
  content_format: PASS | NEEDS_REFINEMENT | BLOCKED
  accuracy: PASS | NEEDS_REFINEMENT
  creator: PASS | NEEDS_REFINEMENT
  timing: PASS | NEEDS_REFINEMENT
  narrative: PASS | NEEDS_REFINEMENT
content_format_validation:
  format_mechanism_present: true | false
  product_role_preserved: true | false
  proof_language_supported: true | false
  action_dialogue_aligned: true | false
  format_preserved: true | false
  validation_status: PASS | NEEDS_REFINEMENT | BLOCKED
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Storyboard Authority

Stage 06 Storyboard is the canonical source for scene sequence, action meaning, timing, dialogue anchors, proof mechanism, and resulting states. Voice Script may elaborate spoken wording and delivery only. It MUST NOT invent actions, proof, product outcomes, or incompatible scene meaning. A material mismatch requires Storyboard revision or marks this artifact STALE.

See `ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md`.

## Content Format Validation

For SPOKEN_ON_CAMERA and VOICE_OVER, the selected Stage 04 Content Format is a required narrative constraint, not metadata decoration.

The Voice Script passes Content Format validation only when dialogue materially supports the selected format mechanism, preserves the product role, uses only supported proof language, remains aligned with storyboard action, and does not imply another format.

The following failures are NEEDS_REFINEMENT:
- generic dialogue that could belong to any format,
- format-specific mechanism present only in metadata,
- dialogue that describes a product role different from the selected format,
- dialogue that talks about proof the storyboard does not demonstrate,
- CTA or product reveal that substitutes a different format mechanism.

The result is BLOCKED when the selected format cannot be expressed in spoken content without inventing unsupported claims, personal experience, or unavailable proof.

For NO_SPOKEN_VOICE with external dialogue enabled, Stage 08 validates the dialogue because it remains the canonical dialogue/timing source. For NO_SPOKEN_VOICE without dialogue, Stage 08 is SKIPPED and Content Format voice validation is NOT_REQUIRED.

## Rules

Spoken claims require evidence. First-person experience requires explicit supplied experience. Do not invent testimonials, results, guarantees, promotions, urgency, scarcity, or creator speaking habits.

Dialogue must fit the approved scene duration. When timing is uncertain, shorten rather than assume implausible speaking speed.

The storyboard remains the canonical scene sequence. Voice Script owns spoken language and delivery direction only.

The artifact is validated, marked COMPLETED, and waits for `/next` then continue according to the canonical /next progression.

## Invalidation

Changes to Content Format, Storyboard, Strategy, Hook, Creator, Product, or campaign language requirements invalidate the Voice Script as STALE.


## Mode-Specific Schema Dispatch

For `content_mode = QUOTE_CONTENT`, use `QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md` as the authoritative output schema and skip rules. Do not require product claims or product proof. Preserve exact wording, provenance, dialogue timing, and non-fabrication checks. For `UGC_AFFILIATE`, retain this contract unchanged.
