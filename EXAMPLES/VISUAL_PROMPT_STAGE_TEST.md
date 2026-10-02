# Affilix Visual Prompt Stage Regression Test

## Purpose

Validate that Stage 08 generates one static image prompt per required Storyboard reference state rather than one prompt per scene.

## Reference-State Cardinality

Given:

    Scene 01
    R01 → R02 → R03

Expected output:

    Prompt 01 → R01
    Prompt 02 → R02
    Prompt 03 → R03

Expected prompt count: 3.

## Acceptance Criteria

1. Prompt count equals the number of required renderable reference states.
2. Each prompt targets exactly one reference ID.
3. A prompt must not use a collapsed target such as R01/R02/R03.
4. Each prompt describes one frozen static visual state only.
5. Prompt metadata identifies the scene and its single reference ID.
6. R02 remains the immutable canonical bridge state when reused downstream.
7. The engine must not collapse multiple reference states into one prompt merely because they belong to the same scene.

## Failure Example

Invalid:

    Prompt 01
    Scene: 01
    Reference: R01/R02/R03
    Prompt Type: Image

This represents three distinct static states as one image prompt.

## Required Result

Valid:

    Prompt 01
    Scene: 01
    Reference: R01

    Prompt 02
    Scene: 01
    Reference: R02

    Prompt 03
    Scene: 01
    Reference: R03

## Validation Formula

    required_reference_states = [R01, R02, R03]
    generated_prompts = [P01, P02, P03]

    assert len(generated_prompts) == len(required_reference_states)
    assert generated_prompts[i].reference_id == required_reference_states[i]

A scene with N required reference states must produce exactly N static image prompts.
