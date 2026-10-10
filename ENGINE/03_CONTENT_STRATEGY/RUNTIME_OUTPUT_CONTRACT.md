## Canonical Stage Identity

- Canonical workflow stage: Stage 04
- Engine implementation path: `ENGINE/03_CONTENT_STRATEGY/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Content Strategy Runtime Output Contract

## Stage Gate

Stage 04 Content Strategy executes only from current, validated artifacts for Stage 01 Brief & Product, Stage 02 Niche & Context, and Stage 03 Creator.

## Output

```yaml
stage: 04_CONTENT_STRATEGY
status: COMPLETED
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
content_format:
  id:
  name:
  fit:
  score:
  rationale:
  requirements: []
content_format_selection:
  product_behavior: []
  proof_opportunity:
  candidate_scores: []
  selection_status: SELECTED | BLOCKED
content_angle:
core_message:
supporting_messages: []
proof_strategy:
emotional_strategy:
story_arc: []
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

The artifact is validated, marked COMPLETED, and waits for `/next` then continues according to the canonical /next progression. Content Format and Content Angle are both required creative constraints for downstream stages.

## Quote Content Output Contract

When `content_mode = QUOTE_CONTENT`, use `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_STRATEGY_CONTRACT.md` and persist the following mode-specific artifact rather than filling product-only fields:

```yaml
stage: 04_CONTENT_STRATEGY
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED
campaign_objective:
  primary:
  secondary:
  desired_audience_action:
platform:
pillar:
  id:
  name:
  rationale:
secondary_pillar:
format:
  id:
  name:
  output_type:
  requirements: []
  rationale:
audience:
  target:
  context:
  core_need:
  awareness_level:
editorial_topic:
primary_message:
takeaway:
emotional_strategy:
  intended_response:
  emotional_movement: []
story_arc: []
hook_direction:
caption_direction:
cta_strategy:
source_provenance: []
unresolved_requirements: []
decision_queue: []
source_artifacts: []
source_commit_sha:
```

For this branch, product role, product behavior, proof opportunity, and product claim scoring are `NOT_APPLICABLE`. A static `QUOTE_IMAGE` may record downstream video/story stages as `SKIPPED` only according to the strategy contract.

## Invalidation

Changes to any upstream product, niche/context, or creator artifact invalidate UGC Strategy and its downstream creative artifacts as STALE. For `QUOTE_CONTENT`, changes to editorial topic, audience, platform when format-sensitive, pillar, format, primary message, or takeaway invalidate the strategy and all dependent downstream artifacts as STALE.
