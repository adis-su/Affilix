# Affilix — Continuous Production Contract v3

## Purpose

Affilix runs as a stage-by-stage production workflow. Each stage is processed and validated, then the run pauses at the completed stage. The user advances with `/next`. `/next` is a progression command, not an approval action.

Each stage follows:

**INPUT → PROCESS → OUTPUT → VALIDATE → WAIT FOR `/next` → NEXT STAGE**

## Canonical Stages

1. Brief & Product
2. Campaign Intake
3. Niche & Context
4. Creator
5. Content Strategy
6. Hook
7. Storyboard
8. Visual Prompt
9. Voice Script
10. Video Prompt
11. Production Output

A stage may be skipped only when its output is genuinely not required for the requested deliverable.

## Stage State

Each stage has one of:
- `NOT_STARTED`
- `DRAFT`
- `REVIEW`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

## `/next` Progression Contract

After producing a stage output:
1. persist the artifact
2. validate the stage and prerequisites
3. mark the stage `COMPLETED` when validation passes
4. present the completed stage output
5. wait for `/next`
6. on `/next`, execute the next dependency-satisfied stage

`/next` does not mean approve, accept, or endorse the output.

If the user requests a revision, revise the affected stage. After the revision is validated, wait for `/next` again.

STALE prevents stale artifacts from being consumed downstream.

## Runtime State Shape

```yaml
run:
  status: ACTIVE
  current_stage: BRIEF_PRODUCT

campaign:
  requested_duration:
  creative_duration:
  duration_status:

provider:
  id:
  model_id:
  supported_durations: []
  capability_status:

generation_segments: []

stages:
  brief_product:
    status: COMPLETED
  campaign_intake:
    status: NOT_STARTED
  niche_context:
    status: NOT_STARTED
  creator:
    status: NOT_STARTED
  strategy:
    status: NOT_STARTED
  hook:
    status: NOT_STARTED
  storyboard:
    status: NOT_STARTED
  visual_prompt:
    status: NOT_STARTED
  video_prompt:
    status: NOT_STARTED
  voice_script:
    status: NOT_STARTED
  production_output:
    status: NOT_STARTED
```

## Stage Contracts

### 01 — Brief & Product
Input: product name and product link/reference only.
Output: researched, normalized brief and canonical product facts from the supplied product reference when accessible.

Stage 01 product-research rule:
- A supplied product link/reference is an evidence source that must be actively inspected.
- Extract materially useful product facts before declaring them UNKNOWN.
- Preserve source provenance and distinguish factual product data from unsupported marketing claims.
- Stage 01 may present the resulting product research summary to the user.

Stage 01 user-facing output isolation:
- Render only Product Intake information.
- Do not render Campaign Intake fields, campaign summaries, or campaign UNKNOWN placeholders.
- Internal campaign state may be initialized as UNKNOWN, but remains non-user-facing until Stage 02 is active.
- Any generic state/status renderer must filter fields by the active stage before presenting output.

### 02 — Campaign Intake
Input: validated Brief & Product.
Output: structured platform, exact requested video duration, content objective, AI-derived or user-corrected target audience, requested creator from the current Creator Library, and CTA.

Stage 02 controlled choices:

**Platform**
- TikTok
- Instagram Reels
- Facebook
- Shopee Video

**Duration**
- 18 seconds by default
- Custom exact duration

The requested duration is authoritative. Provider generation durations remain technical constraints and must be handled later by exact segment composition. The default 18-second duration is provider-feasible as `8 + 10`. A Custom duration that cannot be composed exactly must be marked `duration_feasibility: BLOCKED`; never silently round, truncate, extend, or replace it.

**Content objective**
Available objectives include:
- Product awareness
- Product education
- Problem-solution
- Product demonstration
- Benefit explanation
- Feature highlight
- Social proof
- Trust building
- Consideration
- Conversion / sales
- Direct response
- Traffic / click-through
- Engagement
- Community building
- Launch / new product
- Promotion / offer
- Retargeting

Persist a primary objective and any explicitly requested secondary objectives.

**Target audience**
Derive the initial target audience from validated Stage 01 product research and the supplied product reference. Use source-supported product category, benefits, use cases, positioning, and purchase signals. Mark derived attributes as `INFERRED`. Do not invent sensitive personal attributes or unsupported demographic facts. Allow the user to correct or replace the AI-derived audience before completion.

**Creator**
Enumerate the current pinned repository's `CREATOR_LIBRARY/` records dynamically. Stage 02 must show only creators that actually exist in that library. Do not hard-code creator names into the campaign contract. The selected creator is a requested campaign input; Stage 04 resolves and validates the canonical creator identity.

**CTA**
Available CTA options include:
- Shop now
- Buy now
- Add to cart
- Check the product
- Learn more
- See details
- Try it
- Discover more
- Visit the product page
- Click the link
- Tap the link
- Follow for more
- Save this video
- Share this video
- Comment your thoughts
- Send this to someone
- DM for details
- Use the product
- Consider it for your routine
- Custom CTA

When `Custom CTA` is selected, require the user-provided CTA text.

Stage 02 validation requires one supported platform, one exact duration, one primary objective, one resolved audience profile, one current-library creator selection, and one CTA. Do not use `UNKNOWN` to bypass a choice that can be safely derived or presented.

### 03 — Niche & Context
Input: validated Brief & Product plus Campaign Intake.
Output: one canonical niche context.

### 04 — Creator
Input: validated context plus the requested creator from Campaign Intake.
Output: selected creator identity and relevant creator references.

### 05 — Content Strategy
Input: validated Brief, Campaign Intake, Context, Creator.
Output: objective, audience, angle, core message, story arc, proof strategy, CTA strategy.

### 06 — Hook
Input: validated Strategy.
Output: validated hook direction/copy and delivery direction.

### 07 — Storyboard
Input: validated Hook and all upstream completed state.
Output: canonical scene sequence, creative timing, and duration/segment planning intent.

The storyboard is the source of truth for the requested creative duration. Provider limits are technical constraints and must not silently redefine campaign duration.

### 08 — Visual Prompt
Input: validated Storyboard and upstream completed state.
Output: one production-ready image prompt per required visual scene.

### 09 — Voice Script
Input: validated Storyboard, Content Strategy, Hook, Creator, Product facts, and declared platform/campaign constraints.
Output: scene-by-scene canonical dialogue and delivery instructions.

Voice Script is the canonical source of exact spoken wording, speaker, delivery, and speech timing. It must be completed before Video Prompt when spoken content is required.

### 10 — Video Prompt
Input: validated Storyboard, completed Visual Prompt where relevant, completed Voice Script when spoken content exists, and provider capability profile when video generation is required.
Output: motion specification plus provider-compatible generation segment mapping, including synchronized dialogue instructions when applicable.

Video Prompt must consume the current Voice Script rather than inventing or independently rewriting dialogue. If Voice Script changes, affected Video Prompt artifacts become STALE and must be revalidated.

### 11 — Production Output
Input: all required current upstream production assets.
Output: consolidated production output containing the current campaign brief, creator, product, niche context, strategy, hook, storyboard, and applicable visual/video/voice specifications.

This stage does not perform a separate approval or readiness gate. It is the final output assembly step.

## Revision Contract

A revision must identify the smallest affected component.

Examples:
- Hook wording change → revise Hook and affected opening storyboard dependencies.
- Storyboard Scene 3 change → revise Scene 3 and dependent Visual/Video/Voice assets.
- Visual composition change → revise Visual Prompt and dependent Video Prompt when motion/state is affected.
- Requested duration change → revise Storyboard timing and all duration-sensitive downstream assets.
- Provider capability change → re-evaluate Video Prompt segmentation without silently changing campaign duration.

Do not rebuild unrelated completed stages.

## Completion

The run is complete when all required stages are current and validated, with `COMPLETED` or `SKIPPED` used as internal lifecycle states, and the final Production Output is generated.

There is no QC stage and no Final UGC Package stage.


## Action-Choreography Stage Contract

Stage 07 Storyboard now produces three canonical layers: action choreography, reference graph, and creative timing.

Stage 08 renders reference states. Stage 09 creates canonical spoken content. Stage 10 converts reference-to-reference transitions into provider-compatible generation segments and synchronizes the canonical Voice Script.

A stage is processed, validated, marked `COMPLETED`, then paused for `/next`. No approval gate is implied.
