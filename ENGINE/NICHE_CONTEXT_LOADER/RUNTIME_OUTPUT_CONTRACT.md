## Canonical Stage Identity

- Canonical workflow stage: Stage 03
- Engine implementation path: `ENGINE/NICHE_CONTEXT_LOADER/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.



## Runtime Output Contract

Stage 02 consumes the approved Stage 01 artifact and produces exactly one canonical context object. It must not silently invent unresolved dimensions.

Recommended persisted shape:

```yaml
stage: 03_NICHE_CONTEXT
status: COMPLETED
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

Stage 02 may run only from an current and validated Stage 01 artifact. Its output must enter `REVIEW` and wait for approval then continue according to the canonical /next progression.