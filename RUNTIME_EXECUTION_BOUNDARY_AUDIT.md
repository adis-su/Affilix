# Runtime Execution Boundary Audit

## Date
2026-10-10

## Repository
`adis-su/Affilix`, branch `main`.

## Scope
Audited the current Skill entry point, canonical workflow registry, runtime contract, GitHub adapter, campaign state model, and Storyboard downstream authority contract for three behaviors:

1. repository commit pinning and synchronization on `/next`;
2. stage progression holds and dependency checks;
3. downstream artifact invalidation after revisions.

## Findings

### R01 — Commit pinning
**Contract: DEFINED. Executable orchestration: NOT PRESENT IN THE REPOSITORY.**

The repository specifies resolving `main`, pinning its SHA, loading all runtime files from that snapshot, and synchronizing at the next explicit progression/revision boundary. The GitHub adapter is repository-access-only. No standalone runtime executor or persistent state machine was found in the repository tree during this audit.

### R02 — `/next` progression
**Contract: DEFINED. End-to-end runtime behavior: NOT VERIFIED.**

`SKILL.md`, `ENGINE/WORKFLOW.md`, and `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md` describe a completed-stage hold, repository synchronization, prerequisite validation, one-stage progression, and a return to `WAITING_FOR_NEXT`. These are Skill/runtime instructions, not evidence that a separate program enforces the transition.

### R03 — Dependency invalidation
**Contract: DEFINED. Artifact-level validation: PARTIAL.**

The Storyboard authority contract defines cross-stage lineage and invalidation. The Quote Content artifact validator tests stale/mismatched serialized artifacts for Stages 06–10. Those tests validate artifact bundles; they do not execute a live revision event and prove that the conversational runtime marks dependent artifacts stale.

### R04 — CI coverage
**Before this audit: PARTIAL.** Existing CI checked static contracts and Quote Content artifact bundles but did not explicitly guard the repository-pinning, `/next` synchronization, revision-hold, and invalidation wording as a separate test target.

## Changes in this audit

- Added `scripts/validate_runtime_contract.py` to assert key pinning, synchronization, progression, invalidation, lineage, and architecture-boundary invariants remain present.
- Wired the new validator into the existing GitHub Actions workflow.
- This is contract-drift protection, **not** a claim that the Skill runtime is now an executable state machine.

## Remaining limitation

A genuine end-to-end orchestration test requires an executable runtime/state-transition layer or an observable Skill runtime harness that can run commands against an active state. Do not report `/next`, commit synchronization, or live invalidation as end-to-end tested solely because the static validator passes.

## Acceptance status

- Repository contracts present: **PASS**
- Contract drift checks: **PASS only if CI succeeds**
- Live `/next` synchronization: **NOT RUN**
- Live revision invalidation: **NOT RUN**
- External image/video provider execution: **NOT RUN**
