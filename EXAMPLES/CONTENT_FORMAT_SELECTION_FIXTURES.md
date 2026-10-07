# Affilix — Content Format Selection Fixtures v1

## Purpose

Deterministic fixtures for validating the Stage 04 Content Format selection algorithm against realistic beauty campaigns.

The fixtures validate eligibility, proof constraints, product behavior classification, scoring, and downstream traceability. They are regression inputs, not production campaigns.

## Scoring

Use the registered weights from `ENGINE/03_CONTENT_STRATEGY/CONTENT_FORMAT_SYSTEM.md`:

- Product behavior fit: 30
- Proof opportunity fit: 25
- Campaign objective fit: 15
- Creator fit: 10
- Platform fit: 10
- Action clarity / physical demonstrability: 10

Each signal is scored from 0 to 1.

`format_score = Σ(signal_score × weight)`

## Fixture F001 — Sunscreen Demonstration

### Input

- Product type: sunscreen
- Product behavior: TESTABLE + PROBLEM_SOLUTION
- Evidence: application is observable; product identity and approved usage facts available
- Objective: demonstrate practical use
- Creator: beauty creator comfortable with close-up application
- Platform: short-form vertical video
- Proof opportunity: visible application and routine context

### Expected

- Primary format: `BEAUTY_CRIME_SCENE`
- Fit: eligible
- Rationale: the product can be introduced through an observable sunscreen-use problem and resolved through physical application.
- Must not invent SPF performance, protection percentages, clinical proof, or personal results.

## Fixture F002 — Foundation Multi-Look

### Input

- Product type: foundation
- Product behavior: TESTABLE + MULTI_MODE
- Evidence: shade/finish information and application behavior available
- Objective: demonstrate different looks or use cases
- Creator: beauty/fashion creator
- Platform: short-form vertical video
- Proof opportunity: visible changes in styling/application context without unsupported transformation claims

### Expected

- Primary format: `ONE_PRODUCT_THREE_PERSONALITIES`
- Fit: eligible
- Rationale: foundation supports multiple clearly differentiated use contexts while preserving one product identity.
- Must not claim unsupported coverage, wear duration, or before/after performance.

## Fixture F003 — Concealer Job-Oriented

### Input

- Product type: concealer
- Product behavior: JOB_ORIENTED + PROBLEM_SOLUTION
- Evidence: approved product function and supported use case available
- Objective: solve a clearly defined makeup problem
- Creator: beauty creator
- Platform: short-form vertical video
- Proof opportunity: targeted application on the relevant area

### Expected

- Primary format: `PRODUCT_HAS_A_JOB`
- Fit: eligible
- Rationale: the product has a concrete, demonstrable task and the action naturally expresses that task.
- Must not invent treatment, healing, or guaranteed correction.

## Fixture F004 — Perfume Lifestyle

### Input

- Product type: perfume
- Product behavior: EXPERIENCE_LED
- Evidence: validated scent description and product identity available; no supplied personal experience
- Objective: lifestyle association
- Creator: lifestyle creator
- Platform: short-form vertical video
- Proof opportunity: ritual/contextual use rather than measurable product performance

### Expected

- Primary format: `LIFESTYLE_INTEGRATION`
- Fit: eligible
- Rationale: the value is communicated through context and ritual, not fabricated measurable proof.
- Must not invent longevity, projection, social reactions, or personal experience.

## Fixture F005 — Unsupported Proof Must Block

### Input

- Product type: foundation
- Product behavior: TESTABLE
- Evidence: product identity only; no supported wear-test, coverage proof, or supplied creator experience
- Objective: "prove it lasts all day"
- Creator: beauty creator
- Platform: short-form vertical video
- Proof opportunity: unavailable

### Expected

- `BEAUTY_MYTH_LAB`: INELIGIBLE
- `SILENT_BEAUTY_TEST`: INELIGIBLE
- Any format requiring unsupported wear/performance proof: INELIGIBLE
- Selection must not fabricate evidence.
- If no remaining eligible format satisfies the objective, return:
  `selection_status: BLOCKED`

## Fixture F006 — Conditional Format

### Input

- Product type: lip tint
- Product behavior: MULTI_MODE
- Evidence: product identity, shades, and supported usage available
- Objective: show different styling contexts
- Creator: lifestyle/beauty creator
- Platform: short-form vertical video
- Proof opportunity: visible shade/context variation

### Expected

- `ONE_PRODUCT_THREE_PERSONALITIES`: eligible
- Alternative formats may be conditional only when their explicit requirements are satisfiable.
- Conditional selection must record the condition in `content_format_requirements`.

## Validation Rules

1. The highest-scoring eligible format wins.
2. An ineligible format can never win because of a higher raw score.
3. Conditional formats require explicit satisfiable conditions.
4. Ties prefer stronger proof opportunity and clearer physical action.
5. Product-specific evidence outranks generic product-type tendencies.
6. No format selection may create unsupported claims or invented experience.
7. The selected format must propagate unchanged through Hook, Storyboard, Visual Prompt, Video Prompt, Voice Script when required, and Production Output.
