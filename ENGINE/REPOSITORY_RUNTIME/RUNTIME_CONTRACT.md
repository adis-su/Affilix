# Affilix Runtime Contract

## Purpose

This contract defines the state boundary between Affilix interfaces (ChatGPT, Telegram, or future clients) and the canonical Affilix production runtime.

Interfaces are adapters. They must not become independent sources of workflow logic, production state, or repository rules.

## Runtime Architecture

```
Client Interface
    ↓
Affilix Runtime
    ├── Repository Runtime
    ├── Campaign State
    ├── Stage Manager
    ├── Approval / Revision Manager
    └── Production Artifacts
```

The same runtime contract must be usable by ChatGPT, Telegram, and future interfaces.

## Run Initialization

Every new production run must:

1. Resolve the canonical repository: `adis-su/Affilix`.
2. Resolve the canonical branch: `main`.
3. Read the current branch head.
4. Record the resolved commit SHA as `repository.commit_sha`.
5. Pin that commit for the lifetime of the production run.
6. Load repository rules from the pinned commit, not from an unversioned or mixed snapshot.
7. Create an isolated campaign state.
8. Start the stage-gated workflow.

A new run uses the latest available `main` commit at initialization.

## Mid-Run Repository Updates

A repository update after run initialization must not silently change the rules used by the active run.

The active run remains pinned to its recorded commit.

A later run resolves the newer `main` head automatically.

If a runtime explicitly detects a newer repository head during an active run, it may report that a newer version exists, but it must not mix commits inside the current run.

If the user requests adoption of the newer repository version, treat that as a repository-version change and apply normal stale-state and revalidation rules.

## Runtime State Contract

Minimum state:

```yaml
run:
  id:
  entry_command:
  status:
  created_at:

repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:

campaign:
  platform:
  format:
  duration:
  aspect_ratio:
  objective:
  audience:
  creator:
  cta:
  key_message:
  talking_points:
  references:
  restrictions:

product:
  identity:
  facts:
  selling_points:
  claims:
  evidence:
  unknowns:

niche_context:
  status:
  niche:
  sub_niche:
  product_type:
  use_case:
  style:
  audience_context:
  confidence:
  evidence:
  unresolved_fields:
  conflict_flags:

stages:
  brief_product:
    status:
    output:
  niche_context:
    status:
    output:
  creator:
    status:
    output:
  content_strategy:
    status:
    output:
  hook:
    status:
    output:
  storyboard:
    status:
    output:
  visual_prompt:
    status:
    output:
  video_prompt:
    status:
    output:
  voice_script:
    status:
    output:
  quality_control:
    status:
    output:
  final_package:
    status:
    output:

approval:
  required:
  status:
  requested_at:
  resolved_at:
  revision_request:

decision_queue:
  - id:
    field:
    reason:
    blocking_stage:
    status:

artifacts:
  - id:
    type:
    stage:
    status:
    source_commit_sha:
    source_inputs:
```

Optional implementation fields may be added without changing the semantic contract.

## State Semantics

Repository state and production state are separate.

A production run owns its campaign state and downstream artifacts.

A stage output is valid only when:

- its stage is current,
- its required upstream inputs are current,
- its source repository commit matches the run commit,
- it is not STALE,
- and its approval requirements are satisfied.

When an upstream canonical input changes:

1. identify affected dependents,
2. mark them STALE,
3. regenerate the smallest affected dependency chain,
4. require approval again where the stage contract requires it.

## Evidence and Unknowns

Campaign and product fields must retain provenance.

Use these information classes where applicable:

- EXPLICIT
- REFERENCE
- SUPPORTED
- INFERRED
- UNKNOWN

Only EXPLICIT, REFERENCE, and SUPPORTED information may become authoritative campaign or product requirements.

INFERRED information may guide internal reasoning but must not silently become an authoritative requirement.

UNKNOWN remains UNKNOWN until supported.

## Decision Queue

Missing information must not automatically become a blocking questionnaire.

Create a decision-queue item only when a missing field materially affects a required stage.

Each item records:

- the missing field,
- why it matters,
- the first stage that is blocked,
- whether a safe default exists,
- and its current resolution status.

Interfaces should present only the decisions relevant to the current user interaction.

## Approval Contract

The runtime owns approval state.

An interface may express approval or revision in natural language or UI controls, but the runtime must normalize it into:

- APPROVED
- REVISION_REQUESTED
- WAITING_FOR_APPROVAL

An approval applies only to the current stage output and current repository commit.

## Interface Rules

ChatGPT, Telegram, and other interfaces must:

- send user input to the runtime,
- display runtime outputs,
- display relevant decision requests,
- collect approval or revision,
- never maintain a competing copy of canonical production state,
- never embed independent engine logic,
- never silently modify repository rules.

## Repository Access Failure

If the canonical repository cannot be accessed:

- do not claim that the latest repository was loaded,
- do not invent missing repository rules,
- preserve affected fields as UNKNOWN,
- continue only when available higher-level rules are sufficient,
- otherwise block the affected operation with a clear runtime status.

A stale cached repository snapshot is not equivalent to the current `main` branch and must be labeled accordingly.

## Runtime Traceability

Every material production artifact should record:

- run ID,
- stage,
- source repository commit SHA,
- relevant upstream artifact IDs,
- relevant creator/product/niche sources,
- generation status.

This allows the runtime to explain which repository version produced an output.

## Completion

A production run is complete only when:

- the run has one pinned repository commit,
- all required stages are current,
- required approvals are satisfied,
- no required artifact is STALE,
- QC is PASS,
- and the final package is traceable to the run and pinned repository commit.
