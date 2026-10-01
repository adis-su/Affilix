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
    duration:
    aspect_ratio:
    mandatory_requirements:
    restrictions:

  creator:
    id:
    name:
    identity_reference:
    wardrobe:
    expression:
    pose:
    references:

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

## Package Rules

1. The package must represent one current run only.
2. Every canonical field must come from its designated source of truth.
3. UNKNOWN values must remain explicit when evidence is absent.
4. No final package may contain stale context or stale downstream assets.
5. Creator identity must match the current Creator Library selection.
6. Product identity and claims must match the current Product Library evidence.
7. Niche context must match the canonical Niche Context Loader output.
8. Storyboard is the canonical temporal source for downstream visual, video, and voice specifications.
9. QC must be PASS for a production-ready package.
10. A package with BLOCKED or REVISION REQUIRED status is not production-ready.
11. Do not add unsupported claims during final synthesis.
12. Do not silently resolve conflicts during final synthesis.

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
- creator and product identity are validated
- canonical context is synchronized
- claims are supported
- all required scenes/assets exist
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
