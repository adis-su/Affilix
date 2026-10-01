# Affilix — Production Release Audit

## Audit Date

2026-10-01

## Scope

Runtime lifecycle, Stage 01–11 functions, interface boundary, failure/stale semantics, security posture, and live-test readiness.

## Deployment Inventory

| Component | Status |
|---|---|
| affilix-runtime | ACTIVE |
| affilix-runtime-v2 | ACTIVE |
| affilix-runtime-lifecycle | ACTIVE v3 |
| affilix-stage-01 | ACTIVE v2 |
| affilix-stage-02 | ACTIVE v2 |
| affilix-stage-03 | ACTIVE v2 |
| affilix-stage-04 | ACTIVE v2 |
| affilix-stage-05 | ACTIVE v2 |
| affilix-stage-06 | ACTIVE v2 |
| affilix-stage-07 | ACTIVE v2 |
| affilix-video-prompt | ACTIVE v2 |
| affilix-stage-08 | ACTIVE v2 |
| affilix-quality-control | ACTIVE v2 |
| affilix-final-package | ACTIVE v2 |
| affilix-telegram-adapter | ACTIVE v2 |

## Contract Checks

- Stage 01–06 prerequisite gates use per-stage runtime state rather than `current_stage`.
- Storyboard is the gate for downstream production branches.
- Visual, Video, and Voice branches have independent approval state.
- Video continuity can require Visual Prompt approval.
- Revision propagates STALE state through declared dependents.
- STALE stages cannot be approved.
- QC gates Final Package.
- Final Package rejects missing, stale, or unapproved required artifacts.
- Repository commit pinning is part of run initialization.
- UNKNOWN is preserved when evidence is unavailable.
- Interface adapters do not define creative workflow logic.

## Security Checks

- Core Affilix runtime functions retain JWT verification.
- Telegram webhook is intentionally public at the HTTP layer because Telegram cannot attach a Supabase JWT.
- Telegram adapter therefore requires `TELEGRAM_WEBHOOK_SECRET` before processing requests.
- Telegram bot credentials are expected only as server-side Supabase secrets.
- Service-role credentials are never placed in Git or returned to clients.

## Live Validation

Live HTTP execution remains pending because the available Supabase tool surface does not expose an Edge Function invocation operation.

The deployment state is therefore verified, but end-to-end runtime execution is not claimed as PASS.

## Telegram Status

The Telegram adapter is deployed and hardened, but it is **DEPLOYED_NOT_CONNECTED**.

Connection requires external Telegram configuration:

1. store `TELEGRAM_BOT_TOKEN` as a Supabase secret
2. store `TELEGRAM_WEBHOOK_SECRET` as a Supabase secret
3. register the adapter URL with Telegram using `setWebhook` and the same secret
4. send a real Telegram message
5. validate campaign creation, continuation, approval, revision, and reply delivery

## Release Decision

**CONDITIONAL RELEASE**

The repository and deployed runtime are structurally ready for integration testing. Production release is not marked fully verified until live HTTP execution and Telegram webhook integration have been exercised successfully.
