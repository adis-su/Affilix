# Affilix — Visual Prompt Runtime Output Contract

## Stage Gate

Stage 07 executes only after current Stage 06 Storyboard is COMPLETED and valid.

## Output

```yaml
stage: 07_VISUAL_PROMPT
status: REVIEW
prompts:
  - prompt_id:
    scene_id:
    prompt_type: Image
    metadata: {}
    final_prompt:
    creator_references: []
    product_references: []
    wardrobe_references: []
    pose_expression_references: []
    environment_references: []
    style_references: []
    static_qc:
      single_frame: PASS | REVIEW
      no_motion: PASS | REVIEW
      no_temporal_instruction: PASS | REVIEW
      identity_lock: PASS | REVIEW
      product_lock: PASS | REVIEW
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Static Invariant

Each final prompt describes exactly one frozen visual state. Camera movement, duration instructions, temporal sequences, and next-scene directions are prohibited in the generation prompt.

## Rules

Storyboard remains the canonical scene and timing source. Creator and product identity remain locked. Reference roles remain separated. UNKNOWN is preserved internally. CTA/UI is not baked into the image unless explicitly requested; reserve negative space when needed.

The artifact is validated, marked COMPLETED when valid, then waits for /next before downstream progression.

## Invalidation

Changes to Storyboard, Creator, Product, Context, or visual references invalidate Visual Prompts as STALE.


## Reference-State Output

Each prompt must map to exactly one Storyboard reference:

```yaml
reference_id:
reference_role: START | INTERMEDIATE | END | BRIDGE
reference_version:
continuity_lock: PASS | REVIEW
```

A scene may therefore contain multiple prompts. A bridge prompt must use the same reference version used by both adjacent scenes.

Stage completion: process, validate, mark `COMPLETED`, then wait for `/next`. A revision invalidates only affected prompts and dependent transitions.
