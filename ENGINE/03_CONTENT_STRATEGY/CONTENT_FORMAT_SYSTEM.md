# Affilix — Content Format System

## Purpose

Content Format defines **how the UGC experience is packaged as a story or viewing mechanism**.

Content Format is distinct from Content Angle:

- **Content Format:** the structural experience of the content.
- **Content Angle:** the communication angle used to position the product.

Example:

`Beauty Crime Scene + Problem → Solution`

`Product Has a Job + Feature Spotlight`

`One Product, Three Personalities + Lifestyle integration`

Content Format is a Stage 04 creative constraint and must be passed downstream to Hook, Storyboard, Visual Prompt, Video Prompt, and Voice Script.

## Selection Chain

Use this sequence:

```
PRODUCT
  ↓
PRODUCT TYPE
  ↓
PRODUCT BEHAVIOR
  ↓
DEMONSTRATION / PROOF OPPORTUNITY
  ↓
FORMAT ELIGIBILITY
  ↓
CONTENT FORMAT
  ↓
CONTENT ANGLE
  ↓
CORE MESSAGE
  ↓
PROOF STRATEGY
  ↓
STORY ARC
```

Do not select a format solely because it sounds creative.

## Format Contract

Every registered Content Format must define:

- `format_id`
- `name`
- `description`
- `best_for`
- `requires`
- `not_ideal_for`
- `supported_product_behaviors`
- `compatible_product_types`
- `proof_requirements`
- `story_pattern`
- `hook_patterns`
- `action_patterns`
- `claim_constraints`

## Product Behavior Classes

A product may have one or more behavior classes:

### TESTABLE

The product supports an observable test, comparison, inspection, or controlled demonstration when evidence permits it.

Examples:
- foundation
- mascara
- lip products
- sunscreen
- setting spray

Natural formats:
- Beauty Myth Lab
- Product Interrogation
- Beauty Crime Scene
- Silent Beauty Test

### JOB_ORIENTED

The product has a clear task or job that can be represented through a causal action.

Examples:
- concealer
- cleanser
- moisturizer
- hair serum
- brow product

Natural formats:
- Product Has a Job
- Problem-Solution Mission
- Beauty Crime Scene

### MULTI_MODE

The product has multiple legitimate use contexts, looks, intensities, or styling modes.

Examples:
- lip tint
- blush
- eyeshadow
- foundation
- styling products

Natural formats:
- One Product, Three Personalities
- Lifestyle Integration
- Demonstration

### EXPERIENCE_LED

The primary value is sensory, experiential, aesthetic, or lifestyle-oriented rather than objectively testable.

Examples:
- perfume
- body mist
- some bodycare
- lip balm
- some moisturizers

Natural formats:
- Lifestyle Integration
- Silent Beauty Test
- Routine

### PROBLEM_SOLUTION

The product is explicitly associated with a supported problem/use case that can be demonstrated without inventing outcomes.

Examples:
- cleanser
- sunscreen
- concealer
- anti-frizz hair product

Natural formats:
- Beauty Crime Scene
- Product Has a Job
- Problem-Solution Mission

A product may belong to multiple classes. Selection must use the supplied product evidence and campaign objective.

## Format Registry

### 1. BEAUTY_CRIME_SCENE

**Description:** Treat the viewer's problem as a case to investigate. The product becomes the evidence-backed intervention.

**Best for:** recognizable beauty problems with an observable or supportable demonstration path.

**Requires:**
- clear problem/context
- product relevance
- valid evidence or observable demonstration

**Not ideal for:** products whose value is primarily abstract, purely sensory, or unsupported by observable evidence.

**Supported behaviors:** TESTABLE, JOB_ORIENTED, PROBLEM_SOLUTION

**Story pattern:**
Problem → Investigation → Product as evidence/intervention → Test/action → Resulting state → CTA

**Action pattern:** inspect → identify issue → reach for product → apply/use → observe resulting state.

**Claim constraints:** never imply unsupported treatment, cure, guaranteed transformation, clinical proof, or before/after outcome.

### 2. PRODUCT_HAS_A_JOB

**Description:** Give the product one specific mission and show the physical action that performs it.

**Best for:** products with a clear functional role.

**Requires:**
- explicit product job
- physically demonstrable interaction

**Not ideal for:** products where no concrete job can be represented without inventing a claim.

**Supported behaviors:** JOB_ORIENTED, PROBLEM_SOLUTION

**Story pattern:**
Need → Mission → Product takes the job → Action → Resulting state → CTA

**Action pattern:** trigger → product pickup → deliberate application/use → inspect/adjust → resulting state.

**Claim constraints:** result must remain within supported benefits and observable facts.

### 3. BEAUTY_MYTH_LAB

**Description:** A controlled mini-experiment that tests a beauty assumption or product behavior.

**Best for:** products with a legitimate, observable test.

**Requires:**
- testable proposition
- evidence or observable comparison method
- controlled setup

**Not ideal for:** products whose claimed value cannot be tested visually or physically.

**Supported behaviors:** TESTABLE

**Story pattern:**
Question → Setup → Test → Observation → Interpretation

**Action pattern:** establish baseline → apply/use consistently → perform test → inspect comparison.

**Claim constraints:** no fabricated scientific, clinical, percentage, superiority, or universal claims.

### 4. PRODUCT_INTERROGATION

**Description:** The product is treated as a suspect whose relevant properties must be demonstrated.

**Best for:** products with a small number of specific, supportable properties.

**Requires:**
- clear property/question
- evidence-backed answer path

**Not ideal for:** experience-led products with no concrete property to inspect.

**Supported behaviors:** TESTABLE

**Story pattern:**
Question → Product on trial → Evidence/action → Finding → CTA

**Action pattern:** present product → inspect/open → apply/test → observe → conclude.

**Claim constraints:** only answer questions supported by product evidence.

### 5. ONE_PRODUCT_THREE_PERSONALITIES

**Description:** One product is used across three distinct legitimate contexts or styling modes.

**Best for:** versatile products with multiple modes or contexts.

**Requires:**
- at least three legitimate contexts/modes
- enough product evidence to distinguish them

**Not ideal for:** single-purpose products.

**Supported behaviors:** MULTI_MODE

**Story pattern:**
Product → Mode 1 → Mode 2 → Mode 3 → takeaway → CTA

**Action pattern:** context change → product use → styling/application adjustment → resulting visual state.

**Claim constraints:** do not invent versatility that the product evidence does not support.

### 6. SILENT_BEAUTY_TEST

**Description:** Visual proof carries the content with minimal or no voiceover.

**Best for:** products whose interaction and observable result can be understood visually.

**Requires:**
- visually legible action
- clear product interaction
- sufficient visual proof

**Not ideal for:** claims requiring explanation that cannot be conveyed honestly through visuals.

**Supported behaviors:** TESTABLE, EXPERIENCE_LED, JOB_ORIENTED

**Story pattern:**
Context → Product → Action → Observation → CTA

**Action pattern:** gaze, gesture, application, inspection, restrained reaction, camera reframing.

**Claim constraints:** text/on-screen statements remain subject to the same evidence rules as spoken claims.

### 7. BEAUTY_ROUTINE_UNDER_PRESSURE

**Description:** The product solves or supports a beauty task under a realistic time or situational constraint.

**Best for:** routine products with a practical use context.

**Requires:**
- legitimate scenario constraint
- product relevance to the routine

**Not ideal for:** products with no meaningful role in the scenario.

**Supported behaviors:** JOB_ORIENTED, EXPERIENCE_LED, PROBLEM_SOLUTION

**Story pattern:**
Constraint → Need → Product action → Completion → CTA

**Action pattern:** time/context trigger → rapid but controlled product interaction → transition → resulting state.

**Claim constraints:** time pressure is a storytelling device, not evidence of guaranteed speed or performance.

### 8. ANTI_TUTORIAL

**Description:** Frame the content around when the product is not the right choice, who should be cautious, or what it does not solve.

**Best for:** products with meaningful limitations or audience-fit distinctions.

**Requires:**
- truthful limitation or qualification
- enough product evidence to support the qualification

**Not ideal for:** products with insufficient information to make a responsible qualification.

**Supported behaviors:** all, when evidence supports the framing

**Story pattern:**
Expectation → Qualification → Product reality → Best-fit use case → CTA

**Action pattern:** demonstrate relevant use → reveal limitation/context → reposition expectation.

**Claim constraints:** never manufacture flaws or negative claims merely for engagement.

### 9. LIFESTYLE_INTEGRATION

**Description:** The product is embedded in a believable daily, social, work, travel, or personal routine.

**Best for:** experience-led and context-sensitive products.

**Requires:**
- credible use context
- product role that naturally fits the scene

**Not ideal for:** products that require a specific demonstration to communicate their main value.

**Supported behaviors:** EXPERIENCE_LED, MULTI_MODE, JOB_ORIENTED

**Story pattern:**
Context → Need/moment → Product interaction → Lifestyle payoff → CTA

**Action pattern:** enter context → notice need → retrieve product → use → continue activity.

**Claim constraints:** lifestyle context must not become an unsupported product claim.

### 10. PROBLEM_SOLUTION_MISSION

**Description:** A focused mission turns a product benefit into a concrete sequence of actions.

**Best for:** clear problem/use-case products where the action itself can carry the story.

**Requires:**
- defined problem
- defined product role
- causal action path

**Not ideal for:** products without a meaningful problem/use-case relationship.

**Supported behaviors:** JOB_ORIENTED, PROBLEM_SOLUTION

**Story pattern:**
Problem → Mission → Action → Check → Resulting state → CTA

**Action pattern:** trigger → intention → product interaction → adjustment → inspection → resulting state.

**Claim constraints:** resulting state must be visually and evidentially defensible.

## Eligibility Decision Rules

1. Start from product truth, not format novelty.
2. Prefer the format with the strongest combination of:
   - product fit
   - proof fit
   - creator fit
   - platform fit
   - action clarity
3. Reject formats whose required proof cannot be supplied.
4. Do not select a test format merely because a comparison looks entertaining.
5. Do not select a transformation format when transformation evidence is absent.
6. A format may be marked `eligible`, `conditional`, or `ineligible`.
7. `conditional` requires an explicit condition in the strategy artifact.
8. If no format is eligible, preserve the blocker rather than forcing a creative concept.

## Output Fields

Stage 04 should record:

- `content_format`
- `content_format_fit`
- `content_format_rationale`
- `content_format_requirements`
- `product_behavior`
- `proof_opportunity`

These fields become downstream constraints.

## Downstream Constraint

Once Content Format is selected:

```
CONTENT FORMAT
  ↓
HOOK
  ↓
STORYBOARD
  ↓
VISUAL PROMPT
  ↓
VIDEO PROMPT
  ↓
VOICE SCRIPT
```

Downstream stages MUST preserve the selected format unless Stage 04 is revised.

If product evidence, product type, or selected format changes, the affected downstream artifacts become stale and must be revalidated.


## Operational Selection Algorithm

Stage 04 MUST resolve format selection deterministically from the current validated inputs.

### Candidate Generation

1. Load all registered formats.
2. Determine product behavior classes from product type, supplied product evidence, use case, and demonstration opportunity.
3. Generate candidates whose `supported_product_behaviors` intersect the resolved product behavior.
4. Remove candidates whose `requires` conditions cannot be satisfied.
5. Mark candidates with unresolved but non-critical requirements as `conditional`.

### Candidate Scoring

For each remaining candidate, evaluate:

| Signal | Weight |
|---|---:|
| Product behavior fit | 30 |
| Proof opportunity fit | 25 |
| Campaign objective fit | 15 |
| Creator fit | 10 |
| Platform fit | 10 |
| Action clarity / physical demonstrability | 10 |

Score each signal from 0–1, then calculate:

`format_score = Σ(signal_score × weight)`

The score ranks eligible candidates. It does not override hard claim or evidence constraints.

### Selection

- Select the highest-scoring `eligible` candidate.
- A `conditional` candidate may be selected only when its condition is explicitly satisfiable and recorded.
- If multiple candidates are materially tied, resolve the tie deterministically in this order: (1) stronger proof opportunity score, (2) stronger action clarity score, (3) simpler story mechanism, (4) stronger campaign-objective fit. If all four remain equal, preserve registry order and record the tie-break rationale in provenance.
- Never select an `ineligible` candidate.
- If no candidate is eligible or conditionally satisfiable, set `format_selection_status: BLOCKED` and preserve the unresolved requirement. Do not invent a format.

### Output Traceability

The selected strategy must preserve enough information to explain the decision:

```yaml
content_format:
  id:
  name:
  fit: eligible | conditional
  score:
  rationale:
  requirements: []
content_format_selection:
  product_behavior: []
  proof_opportunity:
  candidate_scores: []
  selection_status: SELECTED | BLOCKED
```

The candidate score list is diagnostic strategy provenance, not a downstream creative instruction.
