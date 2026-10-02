## Canonical Stage Identity

- Canonical workflow stage: Stage 09
- Engine implementation path: `ENGINE/08_VOICE_SCRIPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Voice Script Runtime Output Contract

## Stage Gate

Stage 09 executes only after current Stage 07 Storyboard is current and validated. Visual Prompt approval is not required because audio and visual production specifications are parallel storyboard descendants.

## Output

```yaml
stage: 09_VOICE_SCRIPT
status: COMPLETED
metadata:
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
  accuracy: PASS | REVIEW
  creator: PASS | REVIEW
  timing: PASS | REVIEW
  narrative: PASS | REVIEW
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
