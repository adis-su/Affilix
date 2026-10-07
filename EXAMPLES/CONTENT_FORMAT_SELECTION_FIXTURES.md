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

## Numeric Ranking Checks

The fixtures below make the ranking behavior explicit. Scores use the registered weights and are shown as weighted totals out of 100.

### F001 Ranking

Expected candidate scores:

| Format | Eligibility | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BEAUTY_CRIME_SCENE | eligible | 1.0 | 0.9 | 0.9 | 0.9 | 1.0 | 1.0 | 95.0 |
| PRODUCT_HAS_A_JOB | eligible | 0.9 | 0.8 | 0.8 | 0.9 | 1.0 | 1.0 | 85.5 |
| LIFESTYLE_INTEGRATION | eligible | 0.3 | 0.6 | 0.4 | 0.9 | 1.0 | 0.7 | 52.0 |

Expected winner: `BEAUTY_CRIME_SCENE`.

### F002 Ranking

Expected candidate scores:

| Format | Eligibility | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| ONE_PRODUCT_THREE_PERSONALITIES | eligible | 1.0 | 1.0 | 1.0 | 0.9 | 1.0 | 1.0 | 99.0 |
| BEAUTY_MYTH_LAB | eligible | 0.8 | 0.5 | 0.4 | 0.9 | 1.0 | 0.8 | 67.0 |
| PRODUCT_INTERROGATION | eligible | 0.7 | 0.5 | 0.3 | 0.9 | 1.0 | 0.8 | 61.5 |

Expected winner: `ONE_PRODUCT_THREE_PERSONALITIES`.

### F003 Ranking

Expected candidate scores:

| Format | Eligibility | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| PRODUCT_HAS_A_JOB | eligible | 1.0 | 1.0 | 1.0 | 0.9 | 1.0 | 1.0 | 99.0 |
| BEAUTY_CRIME_SCENE | eligible | 0.9 | 0.8 | 0.8 | 0.9 | 1.0 | 0.9 | 84.5 |
| BEAUTY_ROUTINE_UNDER_PRESSURE | eligible | 0.7 | 0.6 | 0.5 | 0.9 | 1.0 | 0.8 | 68.0 |

Expected winner: `PRODUCT_HAS_A_JOB`.

### F004 Ranking

Expected candidate scores:

| Format | Eligibility | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| LIFESTYLE_INTEGRATION | eligible | 1.0 | 0.9 | 1.0 | 1.0 | 1.0 | 0.8 | 95.5 |
| SILENT_BEAUTY_TEST | eligible | 0.6 | 0.4 | 0.5 | 0.9 | 1.0 | 0.7 | 61.5 |

Expected winner: `LIFESTYLE_INTEGRATION`.

### F005 Hard Eligibility Check

No numeric score may rescue a format whose proof requirement is unsatisfied.

Expected result:

`selection_status: BLOCKED`

### F006 Ranking

Expected candidate scores:

| Format | Eligibility | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| ONE_PRODUCT_THREE_PERSONALITIES | eligible | 1.0 | 1.0 | 1.0 | 0.9 | 1.0 | 1.0 | 99.0 |
| LIFESTYLE_INTEGRATION | eligible | 0.7 | 0.9 | 0.7 | 0.9 | 1.0 | 0.8 | 81.0 |

Expected winner: `ONE_PRODUCT_THREE_PERSONALITIES`.

## Validation Rules

1. The highest-scoring eligible format wins.
2. An ineligible format can never win because of a higher raw score.
3. Conditional formats require explicit satisfiable conditions.
4. Ties prefer stronger proof opportunity and clearer physical action.
5. Product-specific evidence outranks generic product-type tendencies.
6. No format selection may create unsupported claims or invented experience.
7. The selected format must propagate unchanged through Hook, Storyboard, Visual Prompt, Video Prompt, Voice Script when required, and Production Output.


### F007 — Near Tie, Proof Wins

Two eligible formats receive the same total score.

| Format | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---:|---:|---:|---:|---:|---:|---:|
| BEAUTY_CRIME_SCENE | 0.9 | 1.0 | 0.8 | 0.9 | 1.0 | 0.8 | 91.5 |
| PRODUCT_HAS_A_JOB | 0.9 | 0.9 | 0.9 | 0.9 | 1.0 | 0.9 | 91.5 |

Expected winner: `BEAUTY_CRIME_SCENE`.

Reason: proof opportunity is the first tie-break signal and is stronger.

### F008 — Full Tie, Action Wins

Two eligible formats receive the same total score and equal proof opportunity.

| Format | PB | Proof | Objective | Creator | Platform | Action | Score |
|---|---:|---:|---:|---:|---:|---:|---:|
| BEAUTY_CRIME_SCENE | 0.9 | 0.9 | 0.8 | 0.9 | 1.0 | 0.9 | 89.5 |
| PRODUCT_HAS_A_JOB | 0.9 | 0.9 | 0.9 | 0.9 | 1.0 | 0.8 | 89.5 |

Expected winner: `BEAUTY_CRIME_SCENE`.

Reason: action clarity is the second tie-break signal.

### F009 — Full Tie Through Objective

Two eligible formats remain tied after proof and action clarity.

Expected tie-break order:
1. proof opportunity
2. action clarity
3. simpler story mechanism
4. campaign-objective fit

The runtime must record which criterion resolved the tie. It must not choose based on arbitrary runtime ordering.

### F010 — Unresolved Final Tie

If proof, action clarity, story simplicity, and objective fit are all equal, the runtime may preserve registered format order, but must record:

`tie_break: registry_order`

and the candidate set that was tied.



## Hook Propagation Regression

### F011 — Format Metadata Alone Must Not Pass

Given selected format `PRODUCT_HAS_A_JOB` for a concealer campaign:

- Invalid hook: generic curiosity hook that mentions the concealer but establishes no concrete job or need.
- Valid hook: opens on the specific makeup need, then physically frames the concealer as the product taking that job.

Expected:
- invalid hook: `NEEDS_REFINEMENT`
- valid hook: `VIABLE`
- `content_format_preserved: true`

### F012 — Beauty Crime Scene Mechanism Must Survive the Hook

Given selected format `BEAUTY_CRIME_SCENE`:

- The hook must establish a recognizable beauty problem/case and an investigation/intervention path.
- A generic product reveal without the case mechanism is not sufficient.

Expected:
- mechanism-preserving hook: `VIABLE`
- generic product reveal: `NEEDS_REFINEMENT`

### F013 — Format Revision Invalidates Hook

Given a completed Hook generated under `LIFESTYLE_INTEGRATION`, changing Stage 04 Content Format to `ONE_PRODUCT_THREE_PERSONALITIES` makes the Hook `STALE`.

The system must not silently relabel the old Hook with the new format.


## Storyboard Propagation Regression

### F014 — Product Has a Job Must Become a Job-Centered Scene

Given `PRODUCT_HAS_A_JOB`:

- Invalid storyboard: generic creator/product introduction with no concrete task.
- Valid storyboard: a defined makeup need triggers the product action, and the resulting state reflects completion of that task.

Expected:
- invalid storyboard: `NEEDS_REFINEMENT`
- valid storyboard: `PASS`
- metadata alone cannot satisfy format validation.

### F015 — One Product, Three Personalities Must Produce Distinct Modes

Given `ONE_PRODUCT_THREE_PERSONALITIES`:

- The storyboard must preserve one product identity while staging distinct context/mode beats.
- Three arbitrary poses or cosmetic close-ups without distinct mode purpose do not satisfy the format.

Expected:
- mode-driven storyboard: `PASS`
- generic multi-shot product montage: `NEEDS_REFINEMENT`

### F016 — Format Revision Invalidates Storyboard

Given a completed Storyboard under `PRODUCT_HAS_A_JOB`, changing Stage 04 Content Format makes the Storyboard `STALE`.

The old scene sequence must not be silently relabeled with the new format.
