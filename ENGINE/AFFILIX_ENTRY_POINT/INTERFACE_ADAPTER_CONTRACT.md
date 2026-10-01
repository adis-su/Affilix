# Affilix Interface Adapter Contract

## Purpose

ChatGPT, Telegram, and future clients are interface adapters to the same Affilix runtime.

An adapter may:

- accept user input
- normalize transport-specific metadata
- call the canonical runtime
- present runtime output
- collect approval or revision
- preserve the runtime campaign ID

An adapter must not:

- implement stage logic
- maintain competing campaign state
- decide approval independently
- regenerate stale assets
- bypass QC or Final Package
- treat transport metadata as product evidence

## Canonical Runtime

The canonical lifecycle endpoint is the Supabase Edge Function:

`affilix-runtime-lifecycle`

The adapter sends:

- `user_id`
- `campaign_id` when continuing a run
- `command`
- `stage` when explicitly targeting a stage
- `input` or `message`
- transport metadata only when useful for traceability

The runtime remains the source of truth for:

- repository commit pinning
- campaign state
- stage status
- approvals
- revisions
- stale propagation
- dependency rules
- QC
- final readiness

## Telegram Mapping

Telegram `chat.id` is the transport identity used as `user_id`.

A Telegram message containing `/Affilix` starts a new campaign.

A subsequent message is routed to the current campaign for that Telegram chat.

Approval phrases are passed through unchanged and normalized by the runtime.

## Security

The Telegram adapter must verify Telegram's webhook secret token when configured.

The bot token is stored only as a server-side Supabase secret.

The Telegram adapter must never expose:

- `SUPABASE_SERVICE_ROLE_KEY`
- `TELEGRAM_BOT_TOKEN`

No Telegram credential is stored in Git.

## Activation

Deployment of the adapter is separate from Telegram webhook registration.

The adapter can be deployed without a live bot token, but webhook activation requires:

1. `TELEGRAM_BOT_TOKEN` Supabase secret
2. deployed adapter URL
3. Telegram `setWebhook` configuration
4. optional `TELEGRAM_WEBHOOK_SECRET`

Until those are configured, Telegram integration remains `DEPLOYED_NOT_CONNECTED`.
