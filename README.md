# Affilix

**ChatGPT-native UGC Affiliate production system**

Affilix turns a product brief, creator identity, references, and campaign constraints into a structured UGC package. The repository is the source of truth for runtime behavior, creator identity, product facts, niche context, production rules, QC, and regression tests.

## Start Here

1. [SKILL.md](SKILL.md) — runtime entry point and governing behavior
2. [ENGINE/WORKFLOW.md](ENGINE/WORKFLOW.md) — dependency, invalidation, reclassification, and revision contract
3. [ENGINE/NICHE_CONTEXT_LOADER/README.md](ENGINE/NICHE_CONTEXT_LOADER/README.md) — canonical runtime context
4. [ENGINE/FINAL_UGC_PACKAGE_CONTRACT.md](ENGINE/FINAL_UGC_PACKAGE_CONTRACT.md) — final delivery contract
5. [ENGINE/09_QUALITY_CONTROL/README.md](ENGINE/09_QUALITY_CONTROL/README.md) — production-readiness gate
6. [EXAMPLES/SKILL_RUNTIME_REGRESSION_MATRIX.md](EXAMPLES/SKILL_RUNTIME_REGRESSION_MATRIX.md) — runtime regression coverage
7. [ENGINE/AFFILIX_ENTRY_POINT/INTERFACE_ADAPTER_CONTRACT.md](ENGINE/AFFILIX_ENTRY_POINT/INTERFACE_ADAPTER_CONTRACT.md) — ChatGPT/Telegram adapter boundary

## Repository Map

| Path | Responsibility |
|---|---|
| SKILL.md | Runtime entry point and top-level execution rules |
| ENGINE/ | Universal production engines and runtime contracts |
| ENGINE/01_BRIEF_ANALYZER/ | Normalize and classify incoming briefs |
| ENGINE/NICHE_CONTEXT_LOADER/ | Resolve one canonical niche/product context per run |
| ENGINE/02_CREATOR_SELECTOR/ | Select and load creator identity |
| ENGINE/03_CONTENT_STRATEGY/ | Define campaign strategy and message |
| ENGINE/04_HOOK_ENGINE/ | Generate hooks from approved strategy |
| ENGINE/05_STORYBOARD_ENGINE/ | Build the canonical temporal scene sequence |
| ENGINE/06_VISUAL_PROMPT_ENGINE/ | Build image/keyframe prompts |
| ENGINE/07_VIDEO_PROMPT_ENGINE/ | Build temporal motion prompts |
| ENGINE/08_VOICE_SCRIPT_ENGINE/ | Build spoken dialogue and delivery specs |
| ENGINE/09_QUALITY_CONTROL/ | Validate production readiness |
| ENGINE/WORKFLOW.md | Canonical dependency and state-transition contract |
| ENGINE/AFFILIX_ENTRY_POINT/ | User-facing `/Affilix` entry command and interface contracts |
| ENGINE/FINAL_UGC_PACKAGE_CONTRACT.md | Defines the final UGC package and readiness states |
| CREATOR_LIBRARY/ | Persistent creator identities and references |
| PRODUCT_LIBRARY/ | Product facts, claims, niche context, and product-type rules |
| PRODUCT_LIBRARY/NICHE_SYSTEM/ | Niche registry and shared context schemas |
| PRODUCT_LIBRARY/NICHES/ | Niche-specific rules and product-type behavior |
| EXAMPLES/ | Fixtures, test matrices, E2E tests, and contract tests |
| REPOSITORY_ARCHITECTURE_AUDIT.md | Latest architecture audit and maintenance findings |
| SKILL_PACKAGING_RELEASE_AUDIT.md | v1 packaging and release audit |

## Runtime Flow

Affilix executes one isolated production run:

`/Affilix` → Product Intake → Brief Analysis → Niche Context → Creator → Product → Strategy → Hook → Storyboard → Visual/Video/Voice → QC → Final Package

The canonical context is created before creative decisions. A material upstream change invalidates dependent downstream state. A final package is production-ready only after QC passes.

### Runtime Invariants

- one canonical runtime context per run
- no cross-run context leakage
- no stale assets in a production-ready package
- creator identity remains locked
- product identity remains locked
- unsupported claims remain forbidden
- UNKNOWN remains UNKNOWN without evidence
- explicit facts outrank contextual labels
- reclassification replaces the canonical context and invalidates dependents

## Source-of-Truth Hierarchy

1. latest explicit user instruction
2. campaign requirements
3. approved Product Library facts and constraints
4. approved Creator Library identity constraints
5. canonical Niche Context
6. product-type rules
7. platform requirements
8. approved content strategy
9. creative interpretation

Never use a downstream creative asset to silently redefine an upstream fact.

## Creator Library

Current creator library:

- Rositasari/ — canonical creator identity, profile, visual references, wardrobe, expressions, and poses

Creator attributes that are not supplied by the library remain unknown. Creative styling may change without changing the canonical creator identity.

## Product Library

The Product Library is responsible for product identity, supported selling points, claims rules, niche classification, product-type rules, context dimensions, and evidence boundaries.

Do not invent product specifications, performance, reviews, testimonials, discounts, scarcity, guarantees, certifications, or personal experience.

## Niche System

Affilix currently registers ten niches.

### Active

- Fashion
- Beauty
- Food & Beverage
- Home & Living

### Planned

- Electronics
- Lifestyle
- Baby & Kids
- Pet
- Sports & Outdoor
- Automotive

PLANNED means the niche is registered for architecture and future expansion, not that detailed niche-specific behavior is available. Do not fabricate missing rules.

The context model is:

Niche → Sub-Niche → Product Type → Use Case → Style/Aesthetic → Audience Context

Not every dimension must be known for every run. Unknown fields remain unknown unless supported by evidence.

## Universal Engines vs Niche Rules

The production engines are universal.

Niche and product-type rules are runtime context. They influence applicable hooks, settings, styling, demonstrations, pacing, and other behavior without creating separate engine implementations for every niche.

This separation prevents the repository from becoming a graveyard of nearly identical prompt engines with slightly different nouns.

## Interface Adapters

Interfaces are thin adapters to the canonical runtime.

- ChatGPT: user-facing `/Affilix` entry
- Telegram: `affilix-telegram-adapter` Edge Function
- Canonical lifecycle: `affilix-runtime-lifecycle`

Telegram maps a Telegram chat to an isolated runtime `user_id` and forwards messages/approvals to the lifecycle. Telegram credentials remain server-side. See `ENGINE/AFFILIX_ENTRY_POINT/INTERFACE_ADAPTER_CONTRACT.md`.

The Telegram adapter is deployed but remains **DEPLOYED_NOT_CONNECTED** until a bot token, webhook secret, and Telegram webhook are configured.

## Regression and Testing

EXAMPLES/ contains validation at several scopes:

- niche context matrices
- universal runtime matrices
- E2E runtime tests
- skill runtime regression matrix
- failure/stale validation
- live smoke-test plan/result
- niche/product-type fixtures
- final package golden fixture
- final package contract test

Use the narrowest relevant test when changing a component, then run broader regression coverage for material runtime changes.

### Regression Naming Convention

Use:

- *_MATRIX.md for test matrices
- *_FIXTURE.md for test inputs
- *_RESULT.md for test results
- *_CONTRACT_TEST.md for contract validation

Do not rename existing artifacts only for cosmetic consistency.

## Production Readiness

A run is deliverable only when:

QC = PASS → PRODUCTION_READY → READY

REVISION REQUIRED and BLOCKED produce NOT_READY.

A production-ready package must contain one current runtime and no stale downstream asset.

## Change Protocol

When adding or modifying a major rule:

1. identify the source of truth
2. update the relevant schema or registry
3. update affected runtime dependencies
4. add or update regression coverage
5. validate final package compatibility
6. update this repository map if the structure changes
7. run QC or the appropriate contract test

For niche or product-type changes, update the canonical context system before modifying downstream creative behavior.

## Current Architecture Status

The latest repository architecture audit is recorded in REPOSITORY_ARCHITECTURE_AUDIT.md.

Current status: **PASS**

No destructive cleanup is currently recommended.
