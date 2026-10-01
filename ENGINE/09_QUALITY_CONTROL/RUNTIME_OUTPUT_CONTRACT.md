# Affilix — Quality Control Runtime Output Contract

## Stage Gate

QC runs only after the required production-spec artifacts exist. It validates the current run's canonical context and all applicable downstream assets. It must never silently repair creative content.

## Output

```yaml
stage: 09_QUALITY_CONTROL
status: REVIEW
qc_id:
campaign_id:
overall_status: PASS | REVISION REQUIRED | BLOCKED
critical_issue_count: 0
major_issue_count: 0
minor_issue_count: 0
validation_coverage: []
issues:
  - issue_id:
    severity: Critical | Major | Minor
    category:
    scene_id:
    asset_id:
    problem:
    evidence:
    impact:
    required_correction:
    status: OPEN | RESOLVED
passed_checks: []
required_actions: []
revalidation_scope: []
production_readiness: READY | NOT_READY | BLOCKED
provenance: []
source_commit_sha:
```

## Status Rules

- PASS: no Critical/Major issues, mandatory requirements satisfied.
- REVISION REQUIRED: correction is needed but no blocking Critical condition exists.
- BLOCKED: any Critical issue or missing evidence for a mandatory factual claim.

Unavailable non-critical product appearance details remain UNKNOWN and are not automatically blockers.

## Validation Order

Brief → canonical niche context → creator → product → claims → strategy → hook → storyboard → visual → video → voice → CTA → production feasibility → reclassification integrity → cross-run isolation.

## Cross-Asset Rule

Upstream sources remain authoritative. Downstream assets cannot silently override approved campaign requirements, creator identity, product facts, canonical context, strategy, hook, or storyboard sequence.

## Revision Rule

Return the smallest affected asset and exact correction. Revalidate dependent downstream assets. Never rewrite the entire package merely to hide one defect.

## Runtime Integrity

QC must preserve UNKNOWN values, surface conflicts, detect stale context/assets, and reject cross-run leakage. It must not infer missing evidence from aesthetics or niche labels.

## Handoff

PASS permits Final UGC Package assembly. REVISION REQUIRED returns affected assets to their owning engine. BLOCKED stops production until the minimum blocking requirement is resolved.
