# Affilix — Content Strategy Runtime Output Contract

## Stage Gate

Stage 04 executes only from current APPROVED artifacts for Stage 01 Brief & Product, Stage 02 Niche Context, and Stage 03 Creator.

## Output

```yaml
stage: 04_CONTENT_STRATEGY
status: REVIEW
campaign_objective:
  primary:
  secondary:
  desired_audience_action:
audience:
  target:
  context:
  core_need:
  objection:
  awareness_level:
product_role:
  function:
  verified_feature:
  supported_benefit:
  demonstration_opportunity:
  evidence: []
content_angle:
core_message:
supporting_messages: []
proof_strategy:
emotional_strategy:
story_arc: []
cta_strategy:
strategy_confidence:
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Rules

One primary message only. All product facts and benefits require traceable evidence. Experience, transformation, comparison, superiority, urgency, scarcity, discount, guarantee, and certification claims must not be invented.

UNKNOWN is preserved when evidence is absent. A missing non-critical field does not automatically block strategy.

The artifact enters REVIEW and waits for approval before Hook execution.

## Invalidation

Changes to any upstream product, niche/context, or creator artifact invalidate Strategy and all downstream creative artifacts as STALE.
