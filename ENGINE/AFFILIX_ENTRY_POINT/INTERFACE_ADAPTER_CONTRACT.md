# Affilix Interface Adapter Contract

## Purpose

ChatGPT Project is the Affilix interface and runtime host for this Skill.

An adapter may:

- accept user input
- normalize transport-specific metadata
- call the canonical runtime
- present runtime output
- collect `/next` progression commands or revision instructions
- preserve the active run state

An adapter must not:

- implement stage logic
- maintain competing campaign state
- turn `/next` into an approval decision
- regenerate stale assets
- bypass QC or Final Package
- treat transport metadata as product evidence

## Runtime Boundary

The ChatGPT Project hosts the Affilix Skill and executes the canonical workflow using the GitHub repository as source of truth.

The interface may:

- accept `/Affilix` and campaign input
- present the current stage output
- accept `/next` to advance the run
- accept direct revision instructions
- preserve the active run state within the current Project conversation

The interface must not:

- implement competing stage logic
- maintain a second canonical product or creator state
- interpret `/next` as approval
- bypass QC or Final Package
- invent missing repository rules

## Repository Runtime

For a new `/Affilix` run:

1. Resolve `adis-su/Affilix` on `main`.
2. Record the current commit SHA.
3. Load the relevant Skill, workflow, library, and engine files.
4. Keep the active run tied to that repository version for traceability.

No Telegram adapter, Supabase lifecycle endpoint, or external campaign database is part of the canonical Affilix runtime.
