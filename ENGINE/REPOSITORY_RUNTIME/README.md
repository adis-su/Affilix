# Affilix — Repository Runtime Layer

## Purpose

This layer defines how Affilix uses `adis-su/Affilix` as its canonical implementation source.

## Source-of-Truth Order

1. Latest explicit user instruction
2. Campaign requirements
3. Current Product Library facts and constraints
4. Current Creator Library identity constraints
5. Current canonical Niche Context
6. Current product-type rules
7. Current repository engine specifications
8. Platform requirements
9. Current validated Content Strategy
10. Creative interpretation

Repository rules never authorize invention.

## Canonical Stage Resolution

Use `ENGINE/WORKFLOW.md` as the sole stage registry. The registry maps canonical Stage IDs to implementation paths. Engine directory prefixes are not stage IDs and MUST NOT be used for ordering or dependency inference. If a runtime artifact conflicts with the registry, reject the conflicting stage resolution instead of guessing.

## Repository Loading Contract

At the start of an Affilix run:

1. Read `SKILL.md`.
2. Read `ENGINE/WORKFLOW.md`.
3. Read `ENGINE/AFFILIX_ENTRY_POINT/README.md`.
4. Load only the Creator Library, Product Library, Niche Context, and engine files relevant to the current stage.
5. Load the current engine specification immediately before executing that engine when its rules materially affect output.
6. Load `ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md` before final output assembly.

Do not load or depend on obsolete QC/final-package contracts.

## Progressive Loading

```text
SKILL.md
→ WORKFLOW.md
→ Entry / Brief Contract
→ Relevant Creator + Product + Niche Context
→ Current Engine Specification
→ Downstream Specifications
→ Production Output Template
```

Typical mapping:
- Intake: SKILL + WORKFLOW + Entry + Brief Analyzer
- Creator: Creator Selector + Creator Library
- Product/Niche: Product Library + Niche Context Loader + applicable niche rules
- Strategy/Hook/Storyboard: engines 03, 04, 05
- Image: engine 06 + current storyboard/reference states
- Video: engine 07 + current storyboard + visual specification when applicable
- Voice: engine 08 + current storyboard
- Production Output: UGC Production Output Template + all required current upstream artifacts

## Runtime State Separation

Repository state and production-run state are separate. A repository update does not rewrite an active run. If a current repository rule materially affects an existing asset, mark that asset STALE and regenerate according to `ENGINE/WORKFLOW.md`.

## Evidence and Unknowns

If the repository does not define a fact, do not invent it. Preserve UNKNOWN where needed and ask only when the missing information materially blocks safe execution.

## Engine Execution

Before executing an engine:
1. identify the relevant engine,
2. load its current repository specification,
3. load declared inputs and upstream canonical state,
4. generate within those constraints,
5. validate the output,
6. pass the current result to the next dependency,
7. invalidate affected downstream assets when upstream canonical inputs change.

## Traceability

Production assets should be traceable to:
- current run,
- source storyboard scene when applicable,
- canonical creator,
- canonical product,
- canonical niche context when applicable,
- current engine specification,
- repository commit SHA.

## Failure / Fallback

If a required repository file cannot be accessed:
1. do not invent its contents,
2. use available higher-level rules only if sufficient,
3. preserve affected fields as UNKNOWN where appropriate,
4. ask only if the missing rule materially prevents safe execution,
5. do not claim the repository was consulted.

## Completion

A run is repository-compliant when relevant current rules were loaded, required library/context data was loaded, downstream assets follow current engine specifications, no unsupported facts were introduced, cross-run state remained isolated, material source changes triggered regeneration, and the final Production Output is current.

## Live Repository Runtime

For every new `/Affilix` run:
1. resolve `adis-su/Affilix` on `main`,
2. read the current branch head,
3. record `repository.commit_sha`,
4. pin that commit for the run,
5. load relevant files from the pinned commit,
6. record repository access status and load time.

Never silently mix files from different repository commits.

## Runtime State

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
```

## Interface Boundary

ChatGPT Project is the only user-facing runtime host for the Affilix Skill. It displays outputs, accepts `/next`, accepts revisions, and does not maintain competing workflow logic.

## Repository Freshness Failure

If the current repository head cannot be resolved or required files cannot be loaded:
- do not claim the latest repository was loaded,
- do not invent missing rules,
- preserve affected values as UNKNOWN,
- continue only when available rules are sufficient,
- otherwise block the affected operation.

A cached snapshot must never be presented as the current `main` branch.
