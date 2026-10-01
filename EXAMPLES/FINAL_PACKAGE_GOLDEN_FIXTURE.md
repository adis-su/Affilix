# Affilix Final Package Golden Fixture

## Test ID
E2E-GOLDEN-001

## Purpose

Provide a stable reference output for validating that a completed Affilix run conforms to the Final UGC Package Contract v1.

This fixture is intentionally factual and minimal. Missing product attributes remain UNKNOWN rather than being filled creatively.

## Package

### Metadata

- package_id: E2E-GOLDEN-001
- status: PRODUCTION_READY
- version: v1.0
- delivery_readiness: READY

### Campaign

- objective: Product showcase + styling
- audience: UNKNOWN
- platform: TikTok
- format: UGC short-form video
- duration: 20 seconds
- aspect_ratio: 9:16
- mandatory_requirements: none beyond supplied brief
- restrictions: no unsupported claims

### Creator

- id: rositasari
- name: Rositasari
- identity_reference: CREATOR_LIBRARY/Rositasari
- wardrobe: modest, context-appropriate
- expression: approachable, natural
- pose: context-appropriate
- references: Creator Library canonical references

### Product

- id: minimal_modest_dress_e2e_fixture
- name: Minimal Modest Dress - E2E Fixture
- niche: Fashion
- sub_niche: Modest Fashion
- product_type: Dress
- identity:
  - color: black
  - sleeves: long
  - silhouette: ankle-length
  - material: UNKNOWN
  - dimensions: UNKNOWN
  - branding: UNKNOWN
- supported_features:
  - black color
  - long sleeves
  - ankle-length silhouette
- selling_points: UNKNOWN
- claims_allowed:
  - observable product attributes above
- claims_forbidden:
  - unsupported material claims
  - fit/comfort claims
  - durability claims
  - performance claims
  - workplace suitability claims
  - discounts/scarcity/guarantees
- evidence: supplied fixture brief

### Niche Context

- niche: Fashion
- sub_niche: Modest Fashion
- product_type: Dress
- use_case: Work
- style_aesthetic: Minimalist
- audience_context: UNKNOWN
- status: ACTIVE
- confidence: supported
- evidence: supplied brief + active Fashion context registry
- unresolved:
  - audience_context
  - product material
  - product dimensions
  - branding
- conflict_flags: none

### Strategy

- primary_objective: Product showcase + styling
- content_angle: Demonstrate the supplied dress in a modest work-context styling frame
- core_message: Visual showcase of the supplied dress and styling
- supporting_messages: supplied product attributes only
- proof_strategy: visual demonstration
- emotional_strategy: natural, approachable
- story_arc: hook → context → product → styling demonstration → reaction → CTA
- cta_strategy: View product details

### Hook

- concept: Quick visual introduction to the dress in a modest work-context setup
- spoken: No unsupported product claim
- visual: Creator enters/appears in frame wearing the supplied dress
- delivery: natural and concise

### Storyboard

- total_duration: 20 seconds
- scenes:
  - scene_id: S01
    timecode: 00:00-00:03
    story_purpose: Hook
  - scene_id: S02
    timecode: 00:03-00:07
    story_purpose: Context
  - scene_id: S03
    timecode: 00:07-00:12
    story_purpose: Product showcase
  - scene_id: S04
    timecode: 00:12-00:17
    story_purpose: Styling demonstration
  - scene_id: S05
    timecode: 00:17-00:20
    story_purpose: CTA

### Visual Prompts

- S01: Rositasari canonical identity, canonical hijab, black long-sleeve ankle-length dress, modest work-context framing, consistent lighting and environment.
- S02: Same creator, same outfit and product identity, contextual work-oriented composition.
- S03: Same creator and product, clear product visibility and stable garment attributes.
- S04: Same creator and product, simple modest styling interaction without adding unsupported garment attributes.
- S05: Same creator, same outfit and product, clean CTA composition.

### Video Prompts

- S01: natural entrance or opening movement, stable identity.
- S02: subtle body/camera movement establishing context.
- S03: controlled product-facing movement.
- S04: natural styling gesture with continuity.
- S05: stable end state for CTA.

### Voice Script

- S01: concise hook without unsupported claims.
- S02: context framing without invented workplace details.
- S03: identify the supplied dress attributes only.
- S04: describe the visible styling action only.
- S05: "View product details" CTA intent.

### QC

- status: PASS
- critical_issues: 0
- major_issues: 0
- minor_issues: 0
- passed_checks:
  - brief
  - canonical context
  - creator identity
  - product identity
  - claims
  - strategy
  - hook
  - storyboard
  - visual
  - video
  - voice
  - CTA
  - feasibility
  - reclassification integrity
  - cross-run isolation
- required_revisions: none
- revalidation_scope: none
- delivery_readiness: READY

## Golden Invariants

1. No unsupported product attribute is introduced.
2. Rositasari identity remains stable.
3. Canonical hijab remains stable.
4. Fashion → Modest Fashion → Dress → Work → Minimalist remains synchronized.
5. Scene IDs remain synchronized across storyboard, visual, video, and voice.
6. QC PASS is required for production readiness.
7. Any material context change invalidates dependent outputs before delivery.
