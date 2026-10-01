# Affilix — Hook Runtime Output Contract

## Stage Gate

Stage 05 executes only after current Stage 04 Content Strategy is APPROVED.

## Output

```yaml
stage: 05_HOOK
status: REVIEW
candidates:
  - hook_id:
    hook_type:
    hook_text_or_visual_concept:
    delivery_mode:
    audience_trigger:
    product_connection:
    context_connection:
    strategy_connection:
    required_visual_action: []
    required_proof: []
    claim_risk:
    status: VIABLE
selection:
  selected_hook_id:
  rationale:
unresolved_requirements: []
decision_queue: []
provenance: []
source_artifacts: []
source_commit_sha:
```

## Rules

Return viable candidates with factual rationale. Do not rank candidates as best/worst or assign subjective scores.

Hooks must align with approved strategy, creator, product facts, niche context, platform constraints, and available evidence. Unsupported superlatives, guarantees, performance numbers, testimonials, urgency, scarcity, discounts, comparisons, or personal experience are prohibited.

The selected hook must be physically executable and specify the opening visual state, creator action, product visibility, framing, viewer-facing action, context cues, and transition.

The artifact enters REVIEW and waits for approval before Storyboard execution.

## Invalidation

Any material change to Strategy, Creator, Niche Context, or Product invalidates the Hook and all downstream creative artifacts as STALE.
