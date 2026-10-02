## Canonical Stage Identity

- Canonical workflow stage: Stage 04
- Engine implementation path: `ENGINE/02_CREATOR_SELECTOR/`
- Engine directory numbering is an implementation identifier only and MUST NOT be used to infer workflow order, prerequisites, or downstream dependencies.
- Workflow order and dependencies are defined exclusively by `ENGINE/WORKFLOW.md`.

# Affilix — Creator Selector Runtime Output Contract

## Stage Gate

Stage 04 may execute only after current Stage 03 Niche & Context is current and validated.

## Output

```yaml
stage: 04_CREATOR
status: COMPLETED
selected_creator:
  creator_id:
  creator_name:
  selection_status: Selected | Needs Clarification | No Match
  match_rationale:
  loaded_identity_sources: []
  loaded_style_sources: []
  required_references: []
creator_constraints:
  identity_locks: []
  appearance_locks: []
  body_locks: []
  hijab_headwear_requirements: []
  style_constraints: []
  speaking_persona_constraints: []
  campaign_constraints: []
unresolved_requirements: []
decision_queue: []
source_stage: 02_NICHE_CONTEXT
source_artifact_id:
source_commit_sha:
```

## Rules

Selection must use approved Creator Library data. It may select an existing creator but never create or silently redesign one.

Use Needs Clarification when mandatory requirements leave multiple valid creators and the brief does not resolve the choice. Use No Match when no approved creator satisfies a mandatory requirement.

Every selected identity constraint must remain traceable to loaded creator assets. [DEFINE], missing, or unknown attributes remain UNKNOWN.

The artifact enters REVIEW and downstream creative stages remain blocked until approval.

## Invalidation

Changes to Stage 01 product identity, Stage 02 context, or Stage 04 creator selection invalidate dependent Content Strategy, Hook, Storyboard, Visual Prompt, Video Prompt, Voice Script, and Final UGC artifacts as STALE.
