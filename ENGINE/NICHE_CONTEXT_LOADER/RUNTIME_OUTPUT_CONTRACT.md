

## Runtime Output Contract

Stage 02 consumes the approved Stage 01 artifact and produces exactly one canonical context object. It must not silently invent unresolved dimensions.

Recommended persisted shape:

```yaml
stage: 02_NICHE_CONTEXT
status: REVIEW
context:
  niche:
  sub_niche:
  product_type:
  use_case:
  style:
  audience_context:
confidence:
evidence: []
unresolved_fields: []
conflict_flags: []
loaded_rule_layers: []
decision_queue: []
source_stage: 01_BRIEF_PRODUCT
source_artifact_id:
source_commit_sha:
```

### Gate

Stage 02 may run only from an approved, current Stage 01 artifact. Its output must enter `REVIEW` and wait for approval before Creator selection begins.