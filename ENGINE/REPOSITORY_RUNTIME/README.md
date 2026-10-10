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
3. Read `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`.
4. Read `ENGINE/AFFILIX_ENTRY_POINT/README.md`.
5. Load only the Creator Library, Product Library, mode-appropriate Niche/Editorial Context, and engine files relevant to the current stage.
5. Load the current engine specification immediately before executing that engine when its rules materially affect output.
6. For `UGC_AFFILIATE`, load `ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md` before final output assembly. For `QUOTE_CONTENT`, load `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`; block final assembly if a required dependency is missing, stale, or invalid.

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
- Mode selection/intake: SKILL + WORKFLOW + Content Mode Routing + Entry + Brief Analyzer
- `UGC_AFFILIATE`: existing product-centered engine contracts and libraries
- `QUOTE_CONTENT`: editorial context loader + `QUOTE_CONTENT_STRATEGY_CONTRACT.md` + `QUOTE_CONTENT_HOOK_CONTRACT.md`; then load `QUOTE_CONTENT_STORYBOARD_CONTRACT.md`, `QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md`, conditional `QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md`, `QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md`, and `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md` according to the selected format/audio mode
- Creator: Creator Selector + Creator Library
- Product/Niche: Product Library + Niche Context Loader + applicable niche rules
- Strategy/Hook/Storyboard: engines 03, 04, 05; load the Quote Content strategy/hook contracts when `content_mode = QUOTE_CONTENT`
- Image: engine 06 + current storyboard/reference states
- Video: engine 07 + current storyboard + visual specification when applicable
- Voice: engine 08 + current storyboard
- Production Output (`UGC_AFFILIATE`): UGC Production Output Template + all required current upstream artifacts
- Production Output (`QUOTE_CONTENT`): `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`; block with `QUOTE_CONTENT_OUTPUT_DEPENDENCY_BLOCKED` when a required artifact is missing, stale, or invalid

## Runtime State Separation

Repository state and production-run state are separate. A repository update does not rewrite an active run. If a current repository rule materially affects an existing asset, mark that asset STALE and regenerate according to `ENGINE/WORKFLOW.md`.

## Evidence and Unknowns

If the repository does not define a fact, do not invent it. Preserve UNKNOWN where needed and ask only when the missing information materially blocks safe execution.

## Engine Resolution and Execution

Before executing an engine:
1. resolve the canonical Stage ID from `ENGINE/WORKFLOW.md`,
2. resolve the canonical Stage Name from that registry entry,
3. resolve the implementation path from the same registry entry,
4. verify that the implementation path exists in the pinned repository snapshot,
5. load the engine's current repository specification from that exact path,
6. load declared inputs and upstream canonical state,
7. generate within those constraints,
8. validate the output,
9. pass the current result to the next dependency,
10. invalidate affected downstream assets when upstream canonical inputs change.

A runtime must never synthesize an engine path from a stage number or directory prefix. For Stage 08 the required lookup is exactly `08 → Voice Script → ENGINE/08_VOICE_SCRIPT_ENGINE/`; for Stage 09 it is exactly `09 → Video Prompt → ENGINE/07_VIDEO_PROMPT_ENGINE/`.

If the canonical implementation path is present in the pinned snapshot but cannot be loaded, classify the failure as `ENGINE_FILE_ACCESS_FAILURE`, not `ENGINE_NOT_FOUND`. Only report `ENGINE_NOT_FOUND` when the exact canonical path is verified absent from the pinned snapshot. Do not fall back to an assumed alternate path.

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
5. load `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`,
6. resolve and persist one `run.content_mode`,
7. load only that mode's applicable files from the pinned commit,
8. record repository access status, load time, and content mode.

Never silently mix files from different repository commits.


## Atomic /next Synchronization Boundary

`/next` is a repository synchronization boundary for an active run. Before any next-stage engine is resolved, the runtime MUST resolve the current `main` HEAD and compare it with the active run's pinned SHA.

If the SHA is unchanged, continue on the existing pinned snapshot. If it changed, the runtime MUST synchronize the run to the new SHA before loading any engine or stage-specific file. The synchronized snapshot becomes the only repository source for that `/next` execution.

Required transaction:

1. resolve current `main` HEAD,
2. compare with active pin,
3. synchronize the active pin when different,
4. reload runtime contracts from the synchronized snapshot,
5. revalidate prerequisites and mark only affected artifacts `STALE`,
6. resolve the next canonical stage path,
7. load that stage engine from the synchronized snapshot,
8. execute and validate the stage.

Never resolve a stage engine from `main` and then execute it against an older pinned snapshot. Never mix commits within one stage execution. If synchronization fails, use `REPOSITORY_SYNC_FAILURE`; do not misclassify the condition as `ENGINE_NOT_FOUND` or silently continue with the stale pin.

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


## Quote Content Production Contracts

The following mode-specific contracts are active and must be loaded only for `content_mode = QUOTE_CONTENT`:

- Stage 06: `ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md`
- Stage 07: `ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md`
- Stage 08: `ENGINE/08_VOICE_SCRIPT_ENGINE/QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md`
- Stage 09: `ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md`
- Stage 10: `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`

Do not load the UGC Production Output Template for Quote Content. Stage skips must record the canonical stage ID and precise reason. A skip is not a generated artifact.
