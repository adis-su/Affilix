#!/usr/bin/env python3
"""Validate Quote Content Stage 06–10 bundles using the repository's canonical YAML shapes.

The input is JSON serialized with the same field layout as the YAML output contracts.
This checks artifacts; it does not execute the conversational Skill or a media provider.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def _source_identity(sources: Any, artifact_type: str) -> dict[str, Any] | None:
    if isinstance(sources, dict):
        value = sources.get(artifact_type.lower()) or sources.get(artifact_type)
        return value if isinstance(value, dict) else None
    if isinstance(sources, list):
        for item in sources:
            if isinstance(item, dict) and item.get("artifact_type", item.get("stage")) in (artifact_type, artifact_type.lower()):
                return item
    return None


def _artifact_id_version(artifact: dict[str, Any], kind: str) -> tuple[Any, Any]:
    metadata = artifact.get("metadata", {})
    if kind == "STORYBOARD":
        return metadata.get("storyboard_id"), metadata.get("storyboard_version")
    return artifact.get("artifact_id", metadata.get("artifact_id")), artifact.get("artifact_version", metadata.get("artifact_version"))


def validate_bundle(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("storyboard", "visual_prompt", "voice_script", "video_prompt", "production_output")
    for name in required:
        if not isinstance(bundle.get(name), dict):
            errors.append(f"missing_or_invalid_artifact:{name}")
    if errors:
        return errors

    sb, vp, vs, video, output = (bundle[k] for k in required)
    sb_id, sb_version = _artifact_id_version(sb, "STORYBOARD")
    sb_commit = sb.get("metadata", {}).get("source_commit_sha", sb.get("source_commit_sha"))
    if not sb_id or not sb_version or not sb_commit:
        errors.append("storyboard_identity_incomplete")

    scenes = sb.get("scenes", [])
    scene_ids = [s.get("scene_id") for s in scenes]
    states: dict[tuple[Any, Any], dict[str, Any]] = {}
    transitions: dict[Any, dict[str, Any]] = {}
    beats_by_scene: dict[Any, dict[Any, dict[str, Any]]] = {}
    scene_windows: dict[Any, tuple[float, float]] = {}

    if not scenes or any(not sid for sid in scene_ids) or len(set(scene_ids)) != len(scene_ids):
        errors.append("storyboard_scene_ids_missing_or_duplicate")

    for scene in scenes:
        sid = scene.get("scene_id")
        try:
            scene_windows[sid] = (float(scene["time_window"]["start_time"]), float(scene["time_window"]["end_time"]))
        except (KeyError, TypeError, ValueError):
            # Scene-level duration can exist in older contract-shaped fixtures; still require beat timing.
            scene_windows[sid] = (float("nan"), float("nan"))
        plan = scene.get("reference_plan", {})
        trajectory = scene.get("reference_trajectory", {})
        scene_states = plan.get("states", [])
        ordered = trajectory.get("ordered_reference_ids", [])
        state_ids = [x.get("reference_id") for x in scene_states]
        if ordered != state_ids:
            errors.append("storyboard_reference_trajectory_order_mismatch")
        if len(trajectory.get("transitions", [])) != max(0, len(scene_states) - 1):
            errors.append("storyboard_transition_cardinality_mismatch")
        for i, state in enumerate(scene_states):
            rid, version = state.get("reference_id"), state.get("reference_version")
            key = (rid, version)
            if not rid or not version or not state.get("source_beat_id") or not state.get("state_summary") or not state.get("continuity_invariants"):
                errors.append("storyboard_reference_state_incomplete")
            if key in states and states[key] != state:
                # Reused bridge identity must refer to one canonical immutable state.
                if state.get("reference_role") != "BRIDGE" and states[key].get("reference_role") != "BRIDGE":
                    errors.append("storyboard_reference_identity_collision")
            states[key] = state
            if state.get("sequence_index") is not None and state.get("sequence_index") != i:
                errors.append("storyboard_reference_sequence_index_invalid")
        for transition in trajectory.get("transitions", []):
            tid = transition.get("transition_id")
            if not tid or not transition.get("causal_action") or not transition.get("resulting_state"):
                errors.append("storyboard_transition_incomplete")
            if tid in transitions:
                errors.append("storyboard_transition_id_duplicate")
            transitions[tid] = transition
        beats = scene.get("action_graph", {}).get("beats", [])
        beats_by_scene[sid] = {b.get("beat_id"): b for b in beats}
        for beat in beats:
            ref_after = beat.get("reference_after", {})
            if isinstance(ref_after, str):
                if not any(key[0] == ref_after for key in states):
                    errors.append("storyboard_beat_reference_after_unresolved")
            elif (ref_after.get("reference_id"), ref_after.get("reference_version")) not in states:
                errors.append("storyboard_beat_reference_after_unresolved")
            try:
                start, end = float(beat["time_window"]["start_time"]), float(beat["time_window"]["end_time"])
                if not (0 <= start < end <= 20):
                    errors.append("storyboard_beat_timing_invalid")
                if sid in scene_windows and scene_windows[sid][0] == scene_windows[sid][0]:
                    if not (scene_windows[sid][0] <= start < end <= scene_windows[sid][1]):
                        errors.append("storyboard_beat_outside_scene_window")
            except (KeyError, TypeError, ValueError):
                errors.append("storyboard_beat_timing_missing")

    state_keys = set(states)
    if not state_keys:
        errors.append("storyboard_reference_states_missing")

    def source_matches(artifact: dict[str, Any], artifact_name: str) -> None:
        sources = artifact.get("source_artifacts", [])
        src = _source_identity(sources, "STORYBOARD")
        if src is None:
            # Canonical Stage 07 also records the exact storyboard identity on each prompt.
            prompts = artifact.get("prompts", [])
            matching_prompt = any(p.get("source_storyboard_id") == sb_id and
                                  p.get("source_storyboard_version") == sb_version for p in prompts)
            if not matching_prompt:
                errors.append(f"{artifact_name}_storyboard_lineage_missing")
        else:
            sid = src.get("artifact_id", src.get("storyboard_id"))
            version = src.get("artifact_version", src.get("storyboard_version"))
            commit = src.get("source_commit_sha", sb_commit)
            if (sid, version, commit) != (sb_id, sb_version, sb_commit):
                errors.append(f"{artifact_name}_storyboard_lineage_mismatch")
        if artifact.get("status") == "STALE":
            errors.append(f"{artifact_name}_is_stale")

    for artifact, name in ((vp, "visual_prompt"), (vs, "voice_script"), (video, "video_prompt"), (output, "production_output")):
        source_matches(artifact, name)

    # Stage 07: one prompt per unique canonical state, in storyboard order.
    prompts = vp.get("prompts", [])
    prompt_keys = [(p.get("reference_id"), p.get("reference_version")) for p in prompts]
    if set(prompt_keys) != state_keys or len(prompt_keys) != len(state_keys) or len(set(prompt_keys)) != len(prompt_keys):
        errors.append("visual_prompt_reference_coverage_mismatch")
    for prompt in prompts:
        if prompt.get("source_storyboard_id") not in (None, sb_id) or prompt.get("source_storyboard_version") not in (None, sb_version):
            errors.append("visual_prompt_prompt_storyboard_lineage_mismatch")
        key = (prompt.get("reference_id"), prompt.get("reference_version"))
        state = states.get(key)
        if state and prompt.get("source_scene_id") not in (None, state.get("source_scene_id")):
            errors.append("visual_prompt_source_scene_mismatch")
        if state and prompt.get("source_beat_id") not in (None, state.get("source_beat_id")):
            errors.append("visual_prompt_source_beat_mismatch")

    # Stage 08 canonical lines live under dialogue.lines and carry dialogue_anchor.beat_id.
    lines = vs.get("dialogue", {}).get("lines", vs.get("lines", []))
    for line in lines:
        sid, beat_id = line.get("scene_id"), line.get("source_beat_id", line.get("dialogue_anchor", {}).get("beat_id"))
        if sid not in beats_by_scene or beat_id not in beats_by_scene.get(sid, {}):
            errors.append("voice_line_anchor_unresolved")
            continue
        beat = beats_by_scene[sid][beat_id]
        anchor = beat.get("dialogue_anchor") or {}
        line_anchor = line.get("dialogue_anchor") or {}
        if line_anchor.get("beat_id", beat_id) != beat_id:
            errors.append("voice_line_anchor_mismatch")
        if line_anchor.get("anchor_id") not in (None, anchor.get("anchor_id")):
            errors.append("voice_line_anchor_mismatch")
        if line.get("intended_meaning") not in (None, anchor.get("semantic_intent")):
            errors.append("voice_line_semantic_intent_mismatch")
        target = anchor.get("target_reference", {})
        if isinstance(target, str):
            target_key = next((k for k in state_keys if k[0] == target), None)
        else:
            target_key = (target.get("reference_id"), target.get("reference_version"))
        if target_key not in state_keys:
            errors.append("voice_line_reference_anchor_mismatch")
        try:
            start, end = float(line["start_time"]), float(line["end_time"])
            aw = anchor["action_window"]
            astart, aend = float(aw["start_time"]), float(aw["end_time"])
            sstart, send = scene_windows[sid]
            if not (0 <= start < end <= 20 and astart <= start < end <= aend and sstart <= start < end <= send):
                errors.append("voice_line_timing_outside_scene_or_anchor")
        except (KeyError, TypeError, ValueError):
            errors.append("voice_line_timing_missing_or_invalid")

    # Stage 09 canonical run-wide segments may be declared under each scene.
    video_scenes = video.get("scenes", [])
    video_scene_ids = [s.get("scene_id") for s in video_scenes]
    if video_scene_ids != scene_ids:
        errors.append("video_prompt_scene_count_or_order_mismatch")
    segments = video.get("generation_segments", [])
    if not segments:
        for scene in video_scenes:
            segments.extend(scene.get("generation_segments", []))
    # Segment records are run-wide: identical IDs appearing in multiple scene wrappers count once.
    deduped: dict[Any, dict[str, Any]] = {}
    for segment in segments:
        deduped.setdefault(segment.get("segment_id"), segment)
    segments = list(deduped.values())
    if len(segments) != 2:
        errors.append("generation_segment_count_not_two")
    expected = [(0.0, 10.0, 10.0), (10.0, 20.0, 10.0)]
    actual = []
    for segment in segments:
        try:
            start, end, duration = float(segment["final_start_time"]), float(segment["final_end_time"]), float(segment["generation_duration"])
            actual.append((start, end, duration))
            if duration != end - start:
                errors.append("generation_segment_duration_window_mismatch")
            source_scenes = segment.get("source_scene_ids", [])
            if not source_scenes or any(sid not in scene_ids for sid in source_scenes):
                errors.append("generation_segment_scene_mapping_invalid")
            if not segment.get("start_reference_id") or not segment.get("target_reference_id"):
                errors.append("generation_segment_reference_metadata_missing")
            for field in ("start_reference_version", "target_reference_version"):
                if not segment.get(field):
                    errors.append("generation_segment_reference_metadata_missing")
            for field in ("start_reference_id", "target_reference_version"):
                pass
            start_key = (segment.get("start_reference_id"), segment.get("start_reference_version"))
            target_key = (segment.get("target_reference_id"), segment.get("target_reference_version"))
            if start_key not in state_keys or target_key not in state_keys:
                errors.append("generation_segment_reference_unresolved")
            for tid in segment.get("transition_ids", []):
                if tid not in transitions:
                    errors.append("generation_segment_transition_unresolved")
        except (KeyError, TypeError, ValueError):
            errors.append("generation_segment_timing_invalid")
    if actual != expected:
        errors.append("generation_segment_composition_not_exact_10_plus_10")

    # Stage 10 canonical source_artifacts is keyed by stage; verify IDs/versions when present.
    expected_sources = {
        "stage_06": (sb_id, sb_version),
        "stage_07": _artifact_id_version(vp, "VISUAL_PROMPT"),
        "stage_08": _artifact_id_version(vs, "VOICE_SCRIPT"),
        "stage_09": _artifact_id_version(video, "VIDEO_PROMPT"),
    }
    output_sources = output.get("source_artifacts", {})
    for key, identity in expected_sources.items():
        src = output_sources.get(key) if isinstance(output_sources, dict) else _source_identity(output_sources, key.upper())
        if src is None:
            errors.append(f"production_output_{key}_lineage_missing")
            continue
        got = (src.get("artifact_id", src.get("storyboard_id")), src.get("artifact_version", src.get("storyboard_version")))
        if got != identity:
            errors.append(f"production_output_{key}_lineage_mismatch")
    validation = output.get("validation", {})
    if validation.get("reference_coverage") != "PASS":
        errors.append("production_output_reference_coverage_not_pass")
    if validation.get("duration_integrity") != "PASS":
        errors.append("production_output_duration_integrity_not_pass")

    return sorted(set(errors))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_quote_content_artifacts.py path/to/bundle.json", file=sys.stderr)
        return 2
    try:
        bundle = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read JSON bundle: {exc}", file=sys.stderr)
        return 2
    errors = validate_bundle(bundle)
    if errors:
        print("BLOCKED: Quote Content artifact bundle failed validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: Quote Content artifact bundle satisfies Stage 06–10 integration invariants")
    print("Scope note: validates serialized artifacts; does not execute the conversational Skill or video provider.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
