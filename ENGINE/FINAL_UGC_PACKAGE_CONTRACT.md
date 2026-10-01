# Affilix — Final UGC Package Contract v1

## Purpose

Define one stable output contract for every production-ready Affilix run.

The final package is the only user-facing synthesis layer. Individual engines may produce intermediate artifacts, but delivery must conform to this contract.

## Required Package

```yaml
package:
  package_id:
  status:
  version:
  campaign:
    objective:
    audience:
    platform:
    format:
    requested_duration:
    creative_duration:
    final_duration:
    aspect_ratio:
    mandatory_requirements:
    restrictions:
    duration_status:

  creator:
    id:
    name:
    identity_reference:
    wardrobe:
    expression:
    pose:
    references

  product:
    id:
    name:
    niche:
    sub_niche:
    product_type:
    identity:
    supported_features:
    selling_points:
    claims_allowed:
    claims_forbidden:
    evidence:

  niche_context:
    niche:
    sub_niche:
    product_type:
    use_case:
    style_aesthetic:
    audience_context:
    status:
    confidence:
    evidence:
    unresolved:
    conflict_flags:

  strategy:
    primary_objective:
    content_angle:
    core_message:
    supporting_messages:
    proof_strategy:
    emotional_strategy:
    story_arc:
    cta_strategy:

  hook:
    concept:
    spoken:
    visual:
    delivery:

  storyboard:
    total_duration:
    scenes: []

  visual_prompts: []

  video_prompts: []
  video_generation_segments: []

  voice_script:
    scenes: []

  qc:
    status:
    critical_issues:
    major_issues:
    minor_issues:
    passed_checks:
    required_revisions:
    revalidation_scope:
    delivery_readiness:
```

## Duration Contract

The final package distinguishes:

- `requested_duration`: explicit user/campaign requirement.
- `creative_duration`: approved storyboard duration.
- `final_duration`: assembled production duration.
- `video_generation_segments`: technical provider generations used to produce the final video.

Unless the user explicitly approves a change:

`requested_duration = creative_duration = final_duration`

Provider limitations must not silently alter these values.

If a provider supports only discrete generation durations, multiple segments may be assembled to satisfy the approved final duration.

Example:

`18s final = 4s + 6s + 8s`

or another provider-supported segmentation that follows natural storyboard boundaries.

## Video Generation Segment Contract

Each entry in `video_generation_segments` should contain:

- segment_id
- source_scene_id
- final_start_time
- final_end_time
- creative_duration
- generation_duration
- provider_id
- model_id when relevant
- assembly_order
- start_visual_state
- end_visual_state
- continuity_anchor
- status

Generation duration is a technical property. It must not replace the storyboard's creative duration.

## Package Rules

1. The package must represent one current run only.
2. Every canonical field must come from its designated source of truth.
3. UNKNOWN values must remain explicit when evidence is absent.
4. No final package may contain stale context or stale downstream assets.
5. Creator identity must match the current Creator Library selection.
6. Product identity and claims must match the current Product Library evidence.
7. Niche context must match the canonical Niche Context Loader output.
8. Storyboard is the canonical creative temporal source for downstream visual, video, and voice specifications.
9. Provider capability constraints may affect technical video segmentation but may not silently change approved campaign duration.
10. QC must be PASS for a production-ready package.
11. A package with BLOCKED or REVISION REQUIRED status is not production-ready.
12. Do not add unsupported claims during final synthesis.
13. Do not silently resolve conflicts during final synthesis.

## Scene Contract

Every storyboard scene should contain, when applicable:

- scene_id
- timecode
- duration
- story_purpose
- narrative_beat
- environment
- shot
- creator_state
- product_state
- interaction
- wardrobe
- hijab
- lighting
- dialogue_intent
- on_screen_text
- sound
- transition
- continuity
- context_requirements
- references

Visual, video, and voice assets must reference the corresponding scene IDs.

## Traceability

The package must preserve traceability from:

User Brief → Brief Analyzer → Niche Context → Creator/Product Sources → Strategy → Hook → Storyboard → Visual/Video/Voice → QC.

Every material final decision must be attributable to an upstream source or explicit creative interpretation.

## Production Readiness

A package is production-ready only if:

- required campaign fields are satisfied
- requested duration is preserved
- creative duration matches requested duration
- final assembled duration matches requested duration
- creator and product identity are validated
- canonical context is synchronized
- claims are supported
- all required scenes/assets exist
- video generation segments are provider-compatible when video is required
- segment durations sum to the approved final duration
- scene IDs are synchronized across downstream assets
- no stale state remains
- QC status is PASS
- delivery readiness is explicitly marked READY

## Final Synthesis Rules

The final package assembler may:

- normalize formatting
- remove internal duplication
- organize validated assets
- summarize validated strategy and QC
- preserve UNKNOWN and conflict flags

The final package assembler may not:

- invent facts
- invent claims
- change creator/product identity
- reclassify niche context
- alter approved storyboard meaning
- silently change requested duration
- hide duration feasibility issues
- hide QC issues
- convert UNKNOWN into a concrete value
- introduce new creative claims

## Versioning

Use semantic package versions:

- v1.x: structural or formatting changes without changing source-of-truth semantics
- v2.x: contract changes that alter required fields or runtime behavior

A package version change does not permit silent changes to product or creator facts.

## Handoff

If QC = PASS:

- package status = PRODUCTION_READY
- delivery_readiness = READY

If QC = REVISION REQUIRED:

- package status = REVISION_REQUIRED
- delivery_readiness = NOT_READY

If QC = BLOCKED:

- package status = BLOCKED
- delivery_readiness = NOT_READY
