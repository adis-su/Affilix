#!/usr/bin/env python3
"""Static contract checks for Affilix.

These checks verify repository wiring and critical documented invariants.
They do not execute the conversational Skill runtime or external media providers.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "ENGINE/WORKFLOW.md",
    "ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md",
    "ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md",
    "ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md",
    "ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md",
    "ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md",
    "EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md",
]

errors = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if condition:
        print(f"PASS: {message}")
    else:
        errors.append(message)
        print(f"FAIL: {message}")


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


for relative in REQUIRED_FILES:
    check((ROOT / relative).is_file(), f"required contract exists: {relative}")

workflow = read("ENGINE/WORKFLOW.md")
routing = read("ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md")
skill = read("SKILL.md")
storyboard = read("ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md")
visual = read("ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md")
video = read("ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md")
output = read("ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md")
matrix = read("EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md")

# Canonical registry identity and the non-numeric engine-to-stage mappings.
stage_rows = re.findall(r"^\|\s*(\d{2})\s*\|", workflow, flags=re.MULTILINE)
check(stage_rows[:10] == [f"{i:02d}" for i in range(1, 11)],
      "canonical workflow registry lists stages 01–10 in order")
check("08 | Voice Script" in workflow and "ENGINE/08_VOICE_SCRIPT_ENGINE/" in workflow,
      "Stage 08 maps to the Voice Script engine")
check("09 | Video Prompt" in workflow and "ENGINE/07_VIDEO_PROMPT_ENGINE/" in workflow,
      "Stage 09 maps to the Video Prompt engine")
check("No QC stage, Final UGC Package stage, or approval gate exists." in workflow,
      "canonical workflow excludes QC, Final UGC Package, and approval gate")
check("engine directory prefixes" in skill.lower() and "must not" in skill.lower(),
      "Skill documents that engine directory prefixes do not define stage order")

# Mode routing and the static-image branch.
check("UGC_AFFILIATE" in routing and "QUOTE_CONTENT" in routing,
      "both supported content modes are registered")
check("never fall back to UGC template" in routing.lower(),
      "Quote Content cannot silently fall back to the UGC output template")
for relative, content in [
    ("Storyboard", storyboard),
    ("Video Prompt", video),
]:
    check("STATIC_IMAGE_FORMAT" in content and "QUOTE_IMAGE" in content,
          f"{relative} contract defines the static-image skip")
check("Stage 06, 08, and 09 must be `SKIPPED` with `STATIC_IMAGE_FORMAT`" in output,
      "Production Output enforces Quote Image skip states")

# Reference-state coverage and prompt/scene cardinality.
check("target_reference_count" in storyboard and "reference_version" in storyboard,
      "Storyboard declares reference counts and versioned reference states")
check("one image prompt for each Storyboard-declared reference state" in visual,
      "Visual Prompt requires one image prompt per declared reference state")
check("video_prompt_count = storyboard_scene_count" in video,
      "Video Prompt count equals Storyboard scene count")
check("immutable" in storyboard.lower() and "same reference ID and version" in storyboard,
      "Storyboard protects immutable bridge references")

# Exact duration and honest regression reporting.
for content, label in [(storyboard, "Storyboard"), (video, "Video Prompt"), (output, "Production Output")]:
    check(all(token in content for token in ("4", "6", "8", "10")) and
          "sum exactly" in content and "duration_feasibility: BLOCKED" in content,
          f"{label} contract preserves exact segment duration and infeasible-duration blocking")
check("NOT RUN as an end-to-end runtime suite" in matrix,
      "regression matrix clearly distinguishes test specifications from runtime execution")
check(all(f"QCR-{i:03d}" in matrix for i in range(1, 19)),
      "Quote Content regression matrix includes QCR-001 through QCR-018")

print(f"\nStatic contract checks: {checks - len(errors)}/{checks} passed.")
if errors:
    print(f"Failures: {len(errors)}")
    sys.exit(1)
print("Scope note: static contract consistency only; no end-to-end runtime test was executed.")
