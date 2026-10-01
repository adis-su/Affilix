# Rositasari — Visual Reference System

## Purpose

This directory defines how visual references for Rositasari are organized, prioritized, and interpreted by Affilix.

Visual references are evidence for creator identity. They are not automatically interchangeable.

## Reference Hierarchy

When multiple references are available, use this priority order:

1. Explicitly approved canonical reference
2. Latest approved creator identity reference
3. Dedicated reference for the requested attribute
4. Scene-specific reference supplied for the current campaign
5. Older supporting references

A scene-specific reference may change clothing, pose, environment, or styling without changing the canonical creator identity unless the user explicitly requests an identity change.

## Reference Types

### Face Reference

Used primarily for:

- Facial identity
- Facial proportions
- Eyes
- Eyebrows
- Nose
- Lips
- Jawline
- Skin details
- Makeup baseline

### Full-Body Reference

Used primarily for:

- Body proportions
- Height presentation
- Posture
- Silhouette
- Full-body styling

### Style Reference

Used primarily for:

- Fashion aesthetic
- Outfit direction
- Accessories
- Hair styling
- Makeup direction
- Overall visual mood

## Identity Preservation

References must be interpreted as constraints, not as permission to copy unrelated attributes.

For example:

- A new outfit reference changes the outfit, not the face.
- A new pose reference changes the pose, not the body identity.
- A new background reference changes the environment, not the creator.
- A new hairstyle reference changes the hairstyle only when compatible with the canonical identity or explicitly requested.

## Reference Conflict Resolution

If references conflict:

1. Follow explicit user instructions.
2. Follow the most recently approved canonical reference.
3. Apply the dedicated reference only to the attribute it is intended to control.
4. Preserve all unrelated canonical attributes.

## Reference Naming

Use descriptive filenames.

Recommended format:

<creator>_<reference_type>_<version>.<extension>

Examples:

- rositasari_face_v01.jpg
- rositasari_fullbody_v01.jpg
- rositasari_style_v02.jpg

## Reference Approval

A reference becomes canonical only when:

- The user explicitly identifies it as the main/canonical reference, or
- It has been explicitly approved as the source of truth.

Unapproved references are supporting references only.

## Prompt Integration

When generating prompts, Affilix should conceptually separate:

- Identity reference
- Product reference
- Outfit/style reference
- Pose reference
- Environment reference
- Lighting reference

Do not collapse all references into one undifferentiated identity description.

## Missing Reference Rule

If an attribute cannot be established from approved information or references, leave it undefined.

Never fabricate a visual attribute and label it as canonical.
