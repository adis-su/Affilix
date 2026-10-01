# Affilix — Live Smoke Test Result

## Status

**NOT EXECUTED**

The available Supabase tool surface provides Edge Function deployment, inspection, listing, and logs, but no direct Edge Function HTTP invocation operation.

## Required live scenarios

1. Create a new /Affilix run.
2. Confirm repository HEAD is resolved and pinned.
3. Submit product input.
4. Approve Stage 01 through Stage 06 sequentially.
5. Confirm Visual, Video, and Voice branches activate independently.
6. Approve branches independently.
7. Run QC and confirm PASS.
8. Build Final Package and confirm PRODUCTION_READY.
9. Repeat with a revision and verify stale propagation.
10. Verify a stale artifact cannot reach Final Package.

## Evidence currently available

- All Affilix Edge Functions are deployed and ACTIVE.
- Stage 01–06 are v2.
- Lifecycle is v3.
- Visual Prompt and Voice Script do not use shared current_stage as their execution gate.
- Runtime contracts define the required failure and stale semantics.

## Acceptance

This remains **PENDING LIVE HTTP TEST** until an invocation-capable client or tool is available.
