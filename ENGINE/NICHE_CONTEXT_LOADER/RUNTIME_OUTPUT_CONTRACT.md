## Canonical Stage Identity

- Canonical workflow stage: Stage 02
- Engine implementation path: `ENGINE/NICHE_CONTEXT_LOADER/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.



## Runtime Output Contract

Stage 02 consumes the approved Stage 01 artifact and produces exactly one canonical context object for the active mode. It must not silently invent unresolved dimensions.

For `UGC_AFFILIATE`, recommended persisted shape:

```yaml
stage: 02_NICHE_CONTEXT
content_mode: UGC_AFFILIATE
status: COMPLETED | BLOCKED
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

For `QUOTE_CONTENT`, use the editorial output shape defined in `ENGINE/NICHE_CONTEXT_LOADER/README.md` under **Quote Content Runtime Output Shape**. Product-specific fields must be `NOT_APPLICABLE`, not fabricated values.

### Gate

Stage 02 may run only from a current and validated Stage 01 artifact. Its output is validated and marked COMPLETED when valid, then waits for `/next`.