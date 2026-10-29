"""Shared, offline-only helpers for the community reference."""
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_unique_object)


def profiles():
    return sorted((ROOT / "catalog").glob("**/*.json"))


def frame_by_id(profile, number):
    return next((frame for frame in profile["frames"] if frame["decimal_id"] == number), None)


def decode(profile, number, payload):
    if not 0 <= number <= 0x7FF:
        raise ValueError("Only standard 11-bit CAN IDs are supported")
    if not 0 < len(payload) <= 8:
        raise ValueError("Supply 1..8 bytes of classic CAN payload")
    frame = frame_by_id(profile, number)
    if frame is None:
        raise ValueError(f"ID 0x{number:03X} is not in this profile")
    if frame["payload_bytes"] is not None and len(payload) != frame["payload_bytes"]:
        raise ValueError(f"ID 0x{number:03X} has a documented payload length of {frame['payload_bytes']} bytes")
    if not frame["signals"]:
        raise ValueError(f"ID 0x{number:03X} has no curated signal decoder yet")
    required_bits = max(s["start_bit"] + s["bit_length"] for s in frame["signals"])
    if len(payload) * 8 < required_bits:
        raise ValueError(f"ID 0x{number:03X} needs at least {(required_bits + 7) // 8} bytes for its curated fields")
    raw_frame = int.from_bytes(payload, "little")
    output = []
    for signal in frame["signals"]:
        width = signal["bit_length"]
        raw = (raw_frame >> signal["start_bit"]) & ((1 << width) - 1)
        if signal["signed"] and raw & (1 << (width - 1)):
            raw -= 1 << width
        scaled = Decimal(raw) * Decimal(str(signal["scale"])) + Decimal(str(signal["offset"]))
        value = int(scaled) if scaled == scaled.to_integral_value() else float(scaled)
        result = {"name": signal["name"], "raw": raw, "value": value, "unit": signal["unit"],
                  "unit_confidence": signal["unit_confidence"], "confidence": signal["confidence"]}
        if "enum" in signal:
            values = profile["enums"][signal["enum"]]["values"]
            result["enum"] = signal["enum"]
            result["label"] = next((item["name"] for item in values if item["value"] == raw), None)
        output.append(result)
    return {"profile": profile["profile"], "id": frame["id"], "payload": payload.hex().upper(),
            "raw_runtime_validation": frame["raw_runtime_validation"], "signals": output}
