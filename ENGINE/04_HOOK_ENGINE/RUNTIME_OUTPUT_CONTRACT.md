## Canonical Stage Identity

- Canonical workflow stage: Stage 05
- Engine implementation path: `ENGINE/04_HOOK_ENGINE/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Hook Runtime Output Contract

## Stage Gate

Stage 05 executes only after current Stage 04 Content Strategy is current and validated.

## Output

```yaml
stage: 06_HOOK
status: COMPLETED
content_format_constraint:
  format_id:
  format_name:
  format_fit: eligible | conditional
  format_requirements: []
candidates:
  - hook_id:
    hook_type:
    hook_text_or_visual_concept:
    delivery_mode:
    audience_trigger:
    product_connection:
    context_connection:
    strategy_connection:
    content_format_connection:
    required_visual_action: []
    required_proof: []
    claim_risk:
    status: VIABLE
selection:
  content_format_preserved: true
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

The artifact is validated, marked COMPLETED, and waits for `/next` then continue according to the canonical /next progression.

## Invalidation

Any material change to Content Strategy, including Content Format or Content Angle, Creator, Niche Context, or Product invalidates the Hook and all downstream creative artifacts as STALE.
