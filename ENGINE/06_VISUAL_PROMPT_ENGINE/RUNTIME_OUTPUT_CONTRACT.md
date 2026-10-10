## Canonical Stage Identity

- Canonical workflow stage: Stage 07
- Engine implementation path: `ENGINE/06_VISUAL_PROMPT_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Visual Prompt Runtime Output Contract

## Stage Gate

Stage 07 executes only after current Stage 06 Storyboard is COMPLETED and valid.

## Output

```yaml
stage: 07_VISUAL_PROMPT
status: COMPLETED
content_format_constraint:
  format_id:
  format_name:
  format_fit: eligible | conditional
  format_requirements: []
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
    content_format_connection:
  mechanism_preserved: true
static_qc:
      single_frame: PASS | NEEDS_REFINEMENT
      no_motion: PASS | NEEDS_REFINEMENT
      no_temporal_instruction: PASS | NEEDS_REFINEMENT
      identity_lock: PASS | NEEDS_REFINEMENT
      product_lock: PASS | NEEDS_REFINEMENT
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Storyboard Authority

Stage 06 Storyboard is the canonical creative production blueprint. This stage may elaborate the frozen visual implementation of the current Storyboard reference, but MUST NOT introduce new actions, product states, reference transitions, Content Format mechanisms, or creative decisions. Any material mismatch requires Storyboard revision or marks this artifact STALE.

See `ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md`.

## Static Invariant

Each final prompt describes exactly one frozen visual state. Camera movement, duration instructions, temporal sequences, and next-scene directions are prohibited in the generation prompt.

## Rules

Storyboard remains the canonical scene and timing source. Creator and product identity remain locked. Reference roles remain separated. UNKNOWN is preserved internally. CTA/UI is not baked into the image unless explicitly requested; reserve negative space when needed.

The artifact is validated, marked COMPLETED when valid, then waits for /next before downstream progression.

## Invalidation

Changes to Content Format, Storyboard, Creator, Product, Context, or visual references invalidate Visual Prompts as STALE.


## Reference-State Output

Each prompt must map to exactly one Storyboard reference:

```yaml
reference_id:
reference_role: START | INTERMEDIATE | END | BRIDGE
reference_version:
source_scene_id: required source scene ID
source_beat_id: required source beat ID
sequence_index: required scene-local order
source_storyboard_id: required exact storyboard artifact ID
source_storyboard_version: required exact storyboard artifact version
continuity_lock: PASS | NEEDS_REFINEMENT
```

A scene may therefore contain multiple prompts. Visual Prompt output count is driven by the Storyboard Reference Plan, not by scene count. Every declared canonical reference state must produce exactly one static image prompt across the active storyboard artifact. A shared bridge is one canonical state and must not produce duplicate prompts merely because two scenes reference it. A bridge prompt must use the same reference version used by both adjacent scenes.

### Reference Density Invariant

For each Storyboard scene:

```
reference_prompt_count = declared_reference_state_count
```

High-complexity scenes should normally target six meaningful reference states when the action graph justifies that density. This is a planning target, not a blind quota. Fewer references are valid for simpler scenes when no additional meaningful state exists.

Visual Prompt must preserve the Storyboard reference order, role, source beat, critical-state designation, and state semantics. It may not invent intermediate references or collapse declared states.

Stage completion: process, validate, mark `COMPLETED`, then wait for `/next`. A revision invalidates only affected prompts and dependent transitions.


## Mode-Specific Schema Dispatch

For `content_mode = QUOTE_CONTENT`, use `QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md` as the authoritative output schema, including the static `QUOTE_IMAGE` path and one prompt per declared video reference state. For `UGC_AFFILIATE`, retain this contract unchanged.


## Exact Storyboard Source and Reference Graph Gate

For video-mode Quote Content, Stage 07 MUST require `metadata.storyboard_id`, `metadata.storyboard_version`, and `source_commit_sha` from the current completed Stage 06 artifact. Record the exact artifact ID/version in `source_artifacts`; every prompt must carry source scene, source beat, sequence index, reference ID/version, and the same source storyboard ID/version. Validate all states before generation: non-empty required metadata, scene/beat resolution, contiguous unique sequence indices, trajectory/Reference Plan equality, exactly n−1 adjacent transitions per scene, valid `reference_after` links, and identical bridge ID/version at both boundaries. Generate one prompt per unique canonical state in source order. Missing or inconsistent data returns `NEEDS_REFINEMENT` with exact scene/field details; never fabricate metadata or mark Stage 07 completed. Do not change the UGC-specific behavior except where the universal exact-source identity requirement applies.

## Quote Content Exact-Value Validation Gate

For `content_mode = QUOTE_CONTENT`, the fixed section values below are a blocking invariant, not advisory prompt guidance. Generic creator defaults (including hijab/clothing descriptions), environment examples, naturalism requirements, and editorial scene descriptions must not append text to either section.

The runtime must validate the parsed full section bodies, not merely check whether the required sentence appears somewhere in the prompt. If either section contains extra words, English paraphrases, or scene descriptions, repair the prompt and rerun validation. If exact equality still fails, do not return it as a completed Stage 07 artifact.

## Fixed Wardrobe and Environment Output

Every final image-generation prompt must use these exact section values, without appended description or paraphrase:

```text
WARDROBE
Sesuai referensi gambar yang diupload user.

ENVIRONMENT
Sesuai referensi gambar yang diupload user.
```

"Gambar yang diupload user" refers to an image uploaded by the user directly to the external AI image-generation provider, not to the Affilix repository. The user must attach that image separately using the provider's reference-image interface. Affilix only emits the prompt instruction and does not host, access, inspect, or verify that image. Validate exact-string equality for both sections before marking Stage 07 COMPLETED.
