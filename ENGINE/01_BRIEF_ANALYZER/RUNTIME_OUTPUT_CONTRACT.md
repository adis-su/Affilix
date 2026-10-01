

## Runtime Output Contract

The analyzer output is a structured stage artifact, not only prose. The runtime should persist it under `stages.brief_product.output` and preserve field provenance.

Recommended shape:

```yaml
stage: 01_BRIEF_PRODUCT
status: REVIEW
campaign: {}
product: {}
audience: {}
messaging: {}
creator: {}
creative_direction: {}
constraints: {}
references: {}
missing_information: []
decision_queue: []
provenance:
  - field:
    value:
    classification: EXPLICIT | REFERENCE | SUPPORTED | INFERRED | UNKNOWN
    source:
```

### Progressive Intake

Do not require every schema field before producing Stage 01. Normalize what is known, retain UNKNOWN values, and create decision-queue items only for missing information that materially blocks the next stage.

A Stage 01 artifact is ready for review when product identity is sufficiently clear for downstream handling and no unresolved blocker prevents safe progression.