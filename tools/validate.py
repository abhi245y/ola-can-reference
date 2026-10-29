#!/usr/bin/env python3
"""Dependency-free structural and semantic checks for reference catalogs."""
import math
import re
from pathlib import PurePosixPath
from catalog import ROOT, load, profiles


def validate(profile):
    errors = []
    if not isinstance(profile, dict):
        return ["catalog must be a JSON object"]

    def check(condition, message):
        if not condition:
            errors.append(message)

    check(profile.get("schema_version") == 1, "schema_version must be 1")
    check(bool(re.fullmatch(r"[a-z0-9][a-z0-9.-]+", profile.get("profile", ""))), "profile must be a stable lowercase identifier")
    evidence = profile.get("evidence", {})
    if not isinstance(evidence, dict) or not isinstance(profile.get("enums", {}), dict) or not isinstance(profile.get("frames", []), list):
        return ["evidence/enums must be objects and frames must be an array"]
    check(bool(evidence), "source evidence is required")
    for ident, source in evidence.items():
        if not isinstance(source, dict):
            errors.append(f"{ident}: evidence must be an object")
            continue
        if source.get("kind") == "runtime_frame_capture":
            relative = source.get("observation", "")
            safe = isinstance(relative, str) and relative.startswith("observations/") and ".." not in PurePosixPath(relative).parts
            check(safe, f"{ident}: runtime evidence must link under observations/")
            if safe:
                try:
                    observation = load(ROOT / relative)
                    check(observation.get("kind") == "raw_frame_observation" and observation.get("profile") == profile["profile"]
                          and bool(observation.get("samples")), f"{ident}: matching raw observation required")
                except (ValueError, OSError, AttributeError):
                    errors.append(f"{ident}: unreadable raw observation")
            continue
        check(source.get("kind") == "static_decompilation", f"{ident}: unsupported evidence kind")
        path = source.get("path", "")
        check(bool(path) and not PurePosixPath(path).is_absolute() and ".." not in PurePosixPath(path).parts,
              f"{ident}: source path must be portable and relative")
        check(bool(re.fullmatch(r"[a-f0-9]{64}", source.get("source_sha256", ""))), f"{ident}: source SHA256 required")
        check(type(source.get("line")) is int and source["line"] > 0, f"{ident}: positive source line required")
        check(source.get("artifact") in profile.get("artifacts", {}), f"{ident}: unknown artifact")
    enums = profile.get("enums", {})
    for name, enumeration in enums.items():
        if not isinstance(enumeration, dict) or not isinstance(enumeration.get("values"), list) or not all(isinstance(v, dict) for v in enumeration.get("values", [])):
            errors.append(f"{name}: invalid enum structure")
            continue
        values = enumeration.get("values", [])
        check(enumeration.get("evidence") in evidence, f"{name}: unknown enum evidence")
        encoding = enumeration.get("encoding")
        check(encoding in {"ordinal", "explicit"}, f"{name}: unsupported enum encoding")
        numbers = [v.get("value") for v in values]
        check(bool(values) and all(type(v) is int for v in numbers) and len(numbers) == len(set(numbers)), f"{name}: integer enum values must be unique")
        if encoding == "ordinal":
            check(numbers == list(range(len(values))), f"{name}: ordinal list must start at zero with no gaps")
        names = [v.get("name") for v in values]
        check(all(isinstance(n, str) and n for n in names) and len(names) == len(set(names)), f"{name}: invalid/duplicate enum name")
    seen = set()
    for frame in profile.get("frames", []):
        if not isinstance(frame, dict):
            errors.append("frame must be an object")
            continue
        ident, number = frame.get("id", ""), frame.get("decimal_id")
        numeric = type(number) is int and 0 <= number <= 0x7FF
        check(numeric and ident == f"0x{number:03X}", f"{ident}: canonical hex and decimal ID must agree")
        check(ident not in seen, f"{ident}: duplicate frame")
        seen.add(ident)
        check(frame.get("frame_format") == "classic_standard", f"{ident}: unsupported frame format")
        check(frame.get("payload_bytes") is None or type(frame.get("payload_bytes")) is int and 0 <= frame["payload_bytes"] <= 8,
              f"{ident}: invalid payload_bytes")
        check(bool(frame.get("names")) and all(isinstance(n, str) and n for n in frame["names"]), f"{ident}: names required")
        check(bool(frame.get("directions")) and set(frame["directions"]) <= {"headunit_rx", "headunit_tx", "constant_only"}, f"{ident}: direction required")
        check(frame.get("raw_runtime_validation") in {"unverified", "correlated"}, f"{ident}: raw runtime status required")
        if frame.get("raw_runtime_validation") == "correlated":
            check(bool(frame.get("runtime_observations")), f"{ident}: correlated frames need published observation links")
            for relative in frame.get("runtime_observations", []):
                safe = isinstance(relative, str) and relative.startswith("observations/") and ".." not in PurePosixPath(relative).parts
                check(safe, f"{ident}: observation path must stay under observations/")
                if safe:
                    try:
                        observation = load(ROOT / relative)
                        check(observation.get("kind") == "raw_frame_observation" and observation.get("profile") == profile["profile"]
                              and observation.get("frame_id") == ident and bool(observation.get("samples")),
                              f"{ident}: observation must contain matching raw-frame evidence, not callback-only evidence")
                    except (ValueError, OSError, AttributeError):
                        errors.append(f"{ident}: unreadable observation {relative}")
        refs = frame.get("evidence", [])
        check(bool(refs) and all(ref in evidence for ref in refs), f"{ident}: valid frame evidence required")
        for item in frame.get("parsers", []) + frame.get("transmit_variants", []):
            check(item.get("evidence") in evidence, f"{ident}: method evidence required")
        used, signal_names = set(), set()
        for signal in frame.get("signals", []):
            if not isinstance(signal, dict):
                errors.append(f"{ident}: signal must be an object")
                continue
            name = signal.get("name", "")
            check(bool(re.fullmatch(r"[a-z][a-z0-9_]*", name)) and name not in signal_names, f"{ident}: invalid/duplicate signal name {name}")
            signal_names.add(name)
            start, width = signal.get("start_bit"), signal.get("bit_length")
            valid_range = type(start) is int and type(width) is int and start >= 0 and 1 <= width <= 64 and start + width <= 64
            check(valid_range, f"{ident}/{name}: bits must fit a classic CAN payload")
            if valid_range:
                bits = set(range(start, start + width))
                check(not used.intersection(bits), f"{ident}/{name}: overlapping signals; model alternate layouts as variants")
                used.update(bits)
                if frame.get("payload_bytes") is not None:
                    check(start + width <= frame["payload_bytes"] * 8, f"{ident}/{name}: field exceeds declared DLC")
            check(signal.get("byte_order") == "little_endian", f"{ident}/{name}: seed decoder supports little endian only")
            check(type(signal.get("signed")) is bool, f"{ident}/{name}: explicit signedness required")
            check(signal.get("unit") is None or isinstance(signal.get("unit"), str), f"{ident}/{name}: unit must be a string or null")
            check(signal.get("unit_confidence") in {"static_source", "inferred", "runtime_correlated", "unknown"},
                  f"{ident}/{name}: separate unit_confidence required")
            check(signal.get("unit") is not None or signal.get("unit_confidence") == "unknown", f"{ident}/{name}: null units must remain unknown")
            for field in ("scale", "offset"):
                value = signal.get(field)
                check(type(value) in (int, float) and math.isfinite(value), f"{ident}/{name}: finite {field} required")
            check(signal.get("scale") != 0, f"{ident}/{name}: scale must not be zero")
            check(signal.get("confidence") in {"static_source", "inferred", "runtime_correlated"}, f"{ident}/{name}: confidence required")
            check(bool(signal.get("evidence")) and all(ref in evidence for ref in signal["evidence"]), f"{ident}/{name}: signal evidence required")
            kinds = {evidence[ref].get("kind") for ref in signal.get("evidence", []) if ref in evidence}
            if signal.get("confidence") == "static_source":
                check("static_decompilation" in kinds, f"{ident}/{name}: static_source needs source evidence")
            if signal.get("confidence") == "runtime_correlated":
                check("runtime_frame_capture" in kinds, f"{ident}/{name}: runtime_correlated needs raw capture evidence")
            if "enum" in signal:
                check(signal["enum"] in enums, f"{ident}/{name}: unknown enum")
        check(frame.get("payload_status") in {"not_curated", "decompile_gap", "partial", "complete"}, f"{ident}: payload status required")
    check(bool(seen), "at least one frame is required")
    return errors


def main():
    failed = False
    paths = profiles()
    if not paths:
        raise SystemExit("No catalogs found")
    for path in paths:
        try:
            profile = load(path)
            errors = validate(profile)
        except (ValueError, KeyError, TypeError, OSError) as error:
            errors = [str(error)]
        if errors:
            failed = True
            print(path)
            for error in errors:
                print("  " + error)
        else:
            print(f"OK {profile['profile']}: {len(profile['frames'])} frames, {len(profile['enums'])} enums")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
