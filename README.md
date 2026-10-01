# Affilix

**ChatGPT-native UGC Affiliate production system**

Affilix turns a product brief, creator identity, references, and campaign constraints into structured UGC production outputs. The repository is the source of truth for runtime behavior, creator identity, product facts, niche context, production rules, and regression tests.

## Start Here

1. [SKILL.md](SKILL.md) — runtime entry point and governing behavior
2. [ENGINE/WORKFLOW.md](ENGINE/WORKFLOW.md) — dependency, invalidation, reclassification, and revision contract
3. [ENGINE/NICHE_CONTEXT_LOADER/README.md](ENGINE/NICHE_CONTEXT_LOADER/README.md) — canonical runtime context
4. [ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md](ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md) — final production output contract
5. [EXAMPLES/SKILL_RUNTIME_REGRESSION_MATRIX.md](EXAMPLES/SKILL_RUNTIME_REGRESSION_MATRIX.md) — runtime regression coverage
6. [ENGINE/AFFILIX_ENTRY_POINT/INTERFACE_ADAPTER_CONTRACT.md](ENGINE/AFFILIX_ENTRY_POINT/INTERFACE_ADAPTER_CONTRACT.md) — ChatGPT Project interface boundary

## Repository Map

| Path | Responsibility |
|---|---|
| SKILL.md | Runtime entry point and top-level execution rules |
| ENGINE/ | Universal production engines and runtime contracts |
| ENGINE/01_BRIEF_ANALYZER/ | Normalize and classify incoming briefs |
| ENGINE/NICHE_CONTEXT_LOADER/ | Resolve one canonical niche/product context per run |
| ENGINE/02_CREATOR_SELECTOR/ | Select and load creator identity |
| ENGINE/03_CONTENT_STRATEGY/ | Define campaign strategy and message |
| ENGINE/04_HOOK_ENGINE/ | Generate hooks from strategy |
| ENGINE/05_STORYBOARD_ENGINE/ | Build the canonical temporal scene sequence |
| ENGINE/06_VISUAL_PROMPT_ENGINE/ | Build image/keyframe prompts |
| ENGINE/07_VIDEO_PROMPT_ENGINE/ | Build temporal motion prompts |
| ENGINE/08_VOICE_SCRIPT_ENGINE/ | Build spoken dialogue and delivery specs |
| ENGINE/WORKFLOW.md | Canonical dependency and state-transition contract |
| ENGINE/AFFILIX_ENTRY_POINT/ | User-facing `/Affilix` entry command and interface contracts |
| ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md | Defines the final consolidated production output |
| CREATOR_LIBRARY/ | Persistent creator identities and references |
| PRODUCT_LIBRARY/ | Product facts, claims, niche context, and product-type rules |
| PRODUCT_LIBRARY/NICHE_SYSTEM/ | Niche registry and shared context schemas |
| PRODUCT_LIBRARY/NICHES/ | Niche-specific rules and product-type behavior |
| EXAMPLES/ | Fixtures, test matrices, E2E tests, and contract tests |
| REPOSITORY_ARCHITECTURE_AUDIT.md | Latest architecture audit and maintenance findings |
| SKILL_PACKAGING_RELEASE_AUDIT.md | v1 packaging and release audit |

## Runtime Flow

`/Affilix` → Product Intake → Brief Analysis → Niche Context → Creator → Strategy → Hook → Storyboard → Visual/Video/Voice → Production Output

The canonical context is created before creative decisions. A material upstream change invalidates dependent downstream state.

## Runtime Invariants

- one canonical runtime context per run
- no cross-run context leakage
- creator identity remains locked
- product identity remains locked
- unsupported claims remain forbidden
- UNKNOWN remains UNKNOWN without evidence
- explicit facts outrank contextual labels
- reclassification replaces the canonical context and invalidates dependents

## Interface Adapters

Interfaces are thin adapters to the canonical runtime.

- ChatGPT Project: user-facing `/Affilix` entry
- GitHub `adis-su/Affilix` (`main`): canonical implementation source

Affilix runs inside the ChatGPT Project. The repository is loaded as the implementation source for each new run. No Telegram adapter, Supabase runtime, or external campaign database is required.

## Regression and Testing

EXAMPLES/ contains validation at several scopes:

- niche context matrices
- universal runtime matrices
- E2E runtime tests
- skill runtime regression matrix
- failure/stale validation
- live smoke-test plan/result
- niche/product-type fixtures
- production output golden example
- production output contract test

Use the narrowest relevant test when changing a component, then run broader regression coverage for material runtime changes.

## Change Protocol

When adding or modifying a major rule:

1. identify the source of truth
2. update the relevant schema or registry
3. update affected runtime dependencies
4. add or update regression coverage
5. validate production output compatibility
6. update this repository map if the structure changes

For niche or product-type changes, update the canonical context system before modifying downstream creative behavior.

## Current Architecture Status

The latest repository architecture audit is recorded in REPOSITORY_ARCHITECTURE_AUDIT.md.

Current status: **PASS**
