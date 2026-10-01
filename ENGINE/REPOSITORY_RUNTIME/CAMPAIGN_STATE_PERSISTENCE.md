# Affilix Campaign State Persistence

## Purpose

Affilix needs durable campaign state so ChatGPT, Telegram, and future interfaces can operate on the same production run without maintaining separate copies of state.

The persistence layer stores runtime state only. GitHub remains the source of truth for Affilix rules, engines, schemas, and libraries.

## Responsibilities

The persistence layer stores:

- campaign/run identity
- interface user identity
- run status
- current stage and stage status
- pinned repository commit
- repository access metadata
- normalized campaign/product/niche state
- approval state
- decision queue
- references to production artifacts

It does not store an alternative copy of engine rules.

## Canonical Separation

```
GitHub
  = implementation + rules + libraries

Persistence
  = runtime state + campaign progress + approvals

Interface
  = input/output adapter
```

## Campaign Record

Minimum persisted record:

```yaml
id:
user_id:
status:
entry_command: /Affilix

repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:

campaign_state:
  brief:
  product:
  niche_context:
  creator:
  strategy:
  hook:
  storyboard:
  visual_prompt:
  video_prompt:
  voice_script:
  qc:
  final_package:

current_stage:
current_stage_status:

approval_state:
decision_queue:

created_at:
updated_at:
```

## Repository Pinning

At run initialization, the runtime resolves the current `main` commit and persists the SHA.

All repository-backed reads for that run must use the pinned commit.

A new run resolves the current `main` head again.

Repository updates therefore affect subsequent runs without requiring changes to interface prompts.

## Interface Independence

Telegram and ChatGPT must address campaigns through the same persisted campaign ID.

Neither interface may assume that conversation history is the authoritative campaign state.

A reconnect, device change, or interface change must not lose the campaign.

## Security Boundary

Campaign ownership must be enforced by the persistence layer.

The client must never receive database service credentials.

Any exposed table must use RLS appropriate to the actual authentication model. Do not rely on an authenticated role alone as an ownership check.

## Current Implementation Target

The first persistence table is:

`public.affilix_campaigns`

The initial implementation uses JSONB for evolving campaign state while the runtime contract stabilizes. Frequently queried identity/status fields remain typed columns.

As the contract stabilizes, high-value entities can be normalized into dedicated tables without changing the external runtime contract.
