# Affilix Campaign Intake Stage Regression Test

## Test ID
INTAKE-002

## Purpose
Validate that /Affilix opens at Stage 01 and /next after Product Intake exposes Campaign Intake as the explicit Stage 02.

## Stage 01
Expected opening:

STAGE 01 — Product Intake
Silakan isi:
Nama Produk:
Link Produk:

No bootstrap diagnostics, commit SHA, or internal runtime text may appear.

## Stage 02
After Stage 01 is completed and the user sends /next, expected intake:

STAGE 02 — Campaign Intake

Silakan isi:
Platform:
Durasi video:
Tujuan konten:
Target audience:
Creator:
CTA:

## Validation
Stage 02 must persist:
- platform
- requested video duration
- content objective
- target audience
- requested creator
- CTA

The requested creator is campaign input. Canonical creator identity is resolved and validated later by Stage 04 Creator.

Requested duration is authoritative campaign input and must remain unchanged by downstream provider segmentation.

## Acceptance
PASS only when:
1. Stage 01 remains the Product Intake entry.
2. Stage 02 is Campaign Intake.
3. All six Stage 02 fields are exposed exactly as specified.
4. /next progresses from Stage 01 to Stage 02.
5. Stage 02 completion progresses to Stage 03 Niche & Context.
6. No approval gate, QC stage, or hidden bootstrap diagnostics are introduced.


## Stage 01 Output Isolation Regression

Stage 01 must not render Campaign Intake fields before Stage 02 is active.

The Stage 01 user-facing response/output must NOT contain:
- Platform
- Durasi video
- Tujuan konten
- Objective
- Target audience
- Creator
- CTA
- campaign status summaries showing these fields as UNKNOWN or "Belum diberikan"

It is valid for these fields to exist internally as UNKNOWN in isolated runtime state. Internal state initialization must not leak into the Stage 01 user-facing output.

## Renderer Contract

Any generic runtime/status renderer must apply the active-stage output scope before presentation. Stage 01 scope is Product Intake only. Stage 02 scope is Campaign Intake only. A regression passes only when later-stage fields remain hidden until their owning stage becomes active.


## Stage 01 Product Research Regression

When Stage 01 receives a product link, it must attempt active product-reference research before presenting the completed stage. A compliant Stage 01 result includes:
- researched product identity
- available brand/category/product-type information
- materially useful product facts, variants, usage, ingredients/materials, benefits/selling points, or other source-supported details when present
- source/provenance distinction
- explicit UNKNOWN only for information that remains genuinely unavailable

The output must not merely state that the link was received or is a reference source.
