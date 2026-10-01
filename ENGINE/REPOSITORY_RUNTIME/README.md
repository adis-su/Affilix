# Affilix — Repository Runtime Layer

## Purpose

This layer defines how Affilix uses `adis-su/Affilix` as its canonical implementation source. The repository is active runtime knowledge, not merely documentation.

When repository access is available, Affilix must read the current relevant files before executing rules that depend on them.

## Source-of-Truth Order

1. Latest explicit user instruction
2. Campaign requirements
3. Current approved Product Library facts and constraints
4. Current approved Creator Library identity constraints
5. Current canonical Niche Context
6. Current product-type rules
7. Current repository engine specifications
8. Platform requirements
9. Approved content strategy
10. Creative interpretation

Repository rules never authorize invention.

## Repository Loading Contract

At the start of an Affilix run:

1. Read `SKILL.md`.
2. Read `ENGINE/WORKFLOW.md`.
3. Read `ENGINE/AFFILIX_ENTRY_POINT/README.md` for `/Affilix` intake.
4. Load only the Creator Library, Product Library, Niche Context, and engine files relevant to the current stage.
5. Load the current engine specification immediately before executing that engine when its rules materially affect output.
6. Load QC and final-package contracts before final delivery.

Never claim repository consultation when the repository could not actually be accessed.

## Progressive Loading

Do not load the entire repository for every request.

Use:

```text
SKILL.md
→ WORKFLOW.md
→ Entry / Brief Contract
→ Relevant Creator + Product + Niche Context
→ Current Engine Specification
→ Downstream Specifications
→ QC + Final Package Contracts
```

Typical stage mapping:

- Intake: `SKILL.md`, `ENGINE/WORKFLOW.md`, `ENGINE/AFFILIX_ENTRY_POINT/README.md`, `ENGINE/01_BRIEF_ANALYZER/README.md`
- Creator: `ENGINE/02_CREATOR_SELECTOR/README.md` + relevant `CREATOR_LIBRARY/`
- Product/Niche: relevant `PRODUCT_LIBRARY/` + `ENGINE/NICHE_CONTEXT_LOADER/README.md` + applicable niche rules
- Strategy/Hook/Storyboard: engines 03, 04, 05
- Image: engine 06 + current storyboard scene + relevant visual references
- Video: engine 07 + current storyboard + current visual specification when applicable
- Voice: engine 08 + current storyboard
- QC/Delivery: engine 09 + `FINAL_UGC_PACKAGE_CONTRACT.md` + `UGC_PRODUCTION_OUTPUT_TEMPLATE.md`

## Current-Version Rule

Prefer the current repository file over remembered or stale content. Do not silently merge conflicting rules. Resolve conflicts through the source-of-truth hierarchy and flag material conflicts for QC.

## Runtime State Separation

Repository state and production-run state are separate.

A repository update does not automatically rewrite existing production assets. If a current repository rule materially affects an existing asset, mark that dependent asset STALE and regenerate according to `ENGINE/WORKFLOW.md`.

Every new `/Affilix` run starts fresh production state, even though it may load the same canonical repository definitions.

## Evidence and Unknowns

If the repository does not define a fact, do not invent it. Preserve UNKNOWN internally where needed and ask only when the missing information materially prevents safe or accurate production.

Incomplete visual product detail alone does not require blocking production when available information is sufficient.

## Engine Execution

Before executing an engine:

1. Identify the relevant engine.
2. Load its current repository specification.
3. Load its declared inputs and upstream canonical state.
4. Generate only within those constraints.
5. Pass the result to the next dependency.
6. Invalidate and regenerate downstream assets when an upstream canonical input changes.

## Traceability

Production assets should be traceable to the current run, source storyboard scene when applicable, canonical creator, canonical product, canonical niche context when applicable, and current engine specification.

For image prompts:

```text
Repository Rules
→ Current Storyboard
→ Scene Data
→ Visual Prompt Engine
→ Final Image Prompt
```

## Failure / Fallback

If a required repository file cannot be accessed:

1. Do not invent its contents.
2. Use available higher-level rules only if sufficient.
3. Preserve affected fields as UNKNOWN where appropriate.
4. Ask only if the missing rule materially prevents safe execution.
5. Do not claim the repository was consulted.

## Completion

A run is repository-compliant when relevant current rules were loaded, required library/context data was loaded, downstream assets follow current engine specifications, no unsupported facts were introduced, cross-run state remained isolated, material source changes triggered regeneration, and QC passes.


## Live Repository Runtime

The repository is a live runtime dependency, not a static prompt source.

For every new `/Affilix` run:

1. Resolve `adis-su/Affilix` on canonical branch `main`.
2. Read the current branch head.
3. Record the commit SHA as the run's `repository.commit_sha`.
4. Pin that commit for the entire run.
5. Load relevant repository files from the pinned commit.
6. Record repository access status and load time.

A run must never silently mix files from different repository commits.

A repository update after run initialization applies automatically to the next new run. The active run remains pinned to its initialized commit unless the user explicitly requests a repository-version change and the workflow revalidates affected state.

See `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md` for the canonical runtime state and interface contract.

## Runtime State

Repository state and production state must remain separate.

At minimum, the runtime tracks:

```yaml
repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:

run:
  id:
  status:

stages:
  <stage>:
    status:
    output:

progression:
  command: /next
  required_between_completed_stages: true

decision_queue:
  - field:
    reason:
    blocking_stage:
    status:
```

Every material production artifact should retain the run ID, source repository commit SHA, stage, and relevant upstream dependencies.

## Interface Boundary

ChatGPT Project is the only interface/runtime host for the Affilix Skill.

It must not maintain competing workflow logic. It displays outputs, accepts `/next` to advance after a completed stage, accepts revision instructions, and presents relevant decision-queue items.

Changing the repository changes the implementation used by subsequent runs without requiring interface-specific prompt copies.

## Repository Freshness Failure

If the current repository head cannot be resolved or required files cannot be loaded:

- do not claim the latest repository was loaded,
- do not invent missing rules,
- preserve affected values as UNKNOWN,
- continue only when available rules are sufficient,
- otherwise block the affected operation.

A cached snapshot must never be presented as the current `main` branch.
