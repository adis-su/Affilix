# GitHub Runtime Adapter

## Purpose

The GitHub Runtime Adapter resolves the canonical Affilix repository version for a production run and loads runtime rules from the pinned commit. It provides repository access only; it is not a campaign-state database or an alternative workflow runtime.

Canonical repository:

- repository: `adis-su/Affilix`
- ref: `main`

## Initialization Contract

For every new campaign run:

1. Resolve `main` head.
2. Record the exact commit SHA.
3. Use that SHA as the immutable repository version for the run.
4. Load runtime-critical files from that SHA.
5. Return the commit SHA and repository access status to the ChatGPT Project runtime state.
6. Never mix files from a later commit into the active run.

Runtime-critical bootstrap files:

- `SKILL.md`
- `ENGINE/WORKFLOW.md`
- `ENGINE/AFFILIX_ENTRY_POINT/README.md`
- `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md`

## Access Model

The current repository is public, so repository resolution uses GitHub's public REST endpoints and loads raw file content pinned to the resolved commit SHA.

The canonical runtime host is the ChatGPT Project / Affilix Skill. Active campaign state and stage progression remain in the Project's run context as defined by `CAMPAIGN_STATE_PERSISTENCE.md` and `RUNTIME_CONTRACT.md`.

This adapter MUST NOT require or introduce Supabase, an external campaign database, a Supabase Edge Function, Telegram, or another service as the canonical runtime or persistence layer. Any future architecture change requires an explicit update to the canonical architecture contracts before implementation.

## Failure Behavior

If GitHub cannot be reached or the expected files cannot be loaded:

- do not claim that the latest repository was loaded,
- return the repository access failure to the Project runtime,
- do not invent repository rules,
- block only the operations that require the unavailable runtime rules,
- use `REPOSITORY_SYNC_FAILURE` when an atomic `/next` synchronization cannot complete.

Do not persist campaign state to an external service as a fallback.

## State Traceability

The active Project run state should retain:

- repository
- repository ref
- repository commit SHA
- repository loaded timestamp
- repository access status

The commit SHA is the authoritative link between a production run and the repository rules used by that run. The adapter supplies repository metadata; it does not own the campaign state.
