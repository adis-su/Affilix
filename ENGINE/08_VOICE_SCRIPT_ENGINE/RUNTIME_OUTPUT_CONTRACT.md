## Canonical Stage Identity

- Canonical workflow stage: Stage 09
- Engine implementation path: `ENGINE/08_VOICE_SCRIPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Voice Script Runtime Output Contract

## Stage Gate

Stage 09 executes only when Campaign Intake `audio_mode` is `SPOKEN_ON_CAMERA` or `VOICE_OVER`, and only after current Stage 07 Storyboard is current and validated.

When `audio_mode` is `NO_SPOKEN_VOICE`, Stage 09 must not generate a placeholder or invented script. Its valid runtime state is `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE`. Visual Prompt is a parallel Storyboard descendant and is not a prerequisite for Voice Script.

## Output

```yaml
stage: 09_VOICE_SCRIPT
status: COMPLETED
metadata:
  audio_mode: SPOKEN_ON_CAMERA | VOICE_OVER
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
    cta_role:
validation:
  accuracy: PASS | NEEDS_REFINEMENT
  creator: PASS | NEEDS_REFINEMENT
  timing: PASS | NEEDS_REFINEMENT
  narrative: PASS | NEEDS_REFINEMENT
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Rules

Spoken claims require evidence. First-person experience requires explicit supplied experience. Do not invent testimonials, results, guarantees, promotions, urgency, scarcity, or creator speaking habits.

Dialogue must fit the approved scene duration. When timing is uncertain, shorten rather than assume implausible speaking speed.

The storyboard remains the canonical scene sequence. Voice Script owns spoken language and delivery direction only.

The artifact is validated, marked COMPLETED, and waits for `/next` then continue according to the canonical /next progression.

## Invalidation

Changes to Storyboard, Strategy, Hook, Creator, Product, or campaign language requirements invalidate the Voice Script as STALE.
