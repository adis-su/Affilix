# Rositasari — Face Reference Controller

## Purpose

Defines how Affilix uses face references to preserve Rositasari's facial identity.

## Controls

Primary controls:

- Face shape
- Facial proportions
- Eyes
- Eyebrows
- Nose
- Lips
- Jawline
- Cheek structure
- Skin details
- Makeup baseline

## Priority

Use an approved canonical face reference before supporting references.

A scene-specific image must not replace the canonical face identity unless the user explicitly requests a new canonical identity.

## Prompt Rule

Describe the face from the approved reference and preserve identity across scenes.

Do not invent facial attributes that are not supported by the reference.

## Do Not Change

Unless explicitly requested:

- Apparent age
- Core facial structure
- Recognizable facial proportions
- Core skin characteristics
- Core identity

## Allowed Variation

- Expression
- Eye direction
- Makeup intensity when requested
- Lighting
- Camera angle
- Natural hair framing

## QC

Reject or revise a generated result when the face becomes noticeably inconsistent with the approved reference.
