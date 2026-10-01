# GitHub Runtime Adapter

## Purpose

The GitHub Runtime Adapter resolves the canonical Affilix repository version for a production run and loads runtime rules from the pinned commit.

Canonical repository:

- repository: `adis-su/Affilix`
- ref: `main`

## Initialization Contract

For every new campaign run:

1. Resolve `main` head.
2. Record the exact commit SHA.
3. Use that SHA as the immutable repository version for the run.
4. Load runtime-critical files from that SHA.
5. Persist the SHA and repository access status in `public.affilix_campaigns`.
6. Never mix files from a later commit into the active run.

Runtime-critical bootstrap files:

- `SKILL.md`
- `ENGINE/WORKFLOW.md`
- `ENGINE/AFFILIX_ENTRY_POINT/README.md`
- `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md`

## Access Model

The current repository is public, so the first runtime implementation uses GitHub's public REST endpoint to resolve the branch head and raw file URLs to load pinned content.

For higher production reliability and API-rate capacity, a GitHub credential may later be added as a Supabase Edge Function secret. The runtime must keep the same commit-pinning semantics regardless of authentication method.

## Failure Behavior

If GitHub cannot be reached or the expected files cannot be loaded:

- do not claim that the latest repository was loaded,
- persist the repository access failure,
- do not invent repository rules,
- block only the operations that require the unavailable runtime rules.

## State Traceability

A campaign row must retain:

- repository
- repository ref
- repository commit SHA
- repository loaded timestamp
- repository access status

The commit SHA is the authoritative link between a production run and the repository rules used by that run.
