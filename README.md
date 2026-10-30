# Ola CAN Reference

An independent, community-maintained reference for Ola scooter CAN messages,
signals, command vocabularies, and the Android services that expose them.

Initial coverage is **Gen 1**, pinned to the captured **HVDP 5.0.0** APK.
Other generations and firmware versions need separate profiles and evidence.

> **Unofficial.** This project is not affiliated with, endorsed by, sponsored by, or
> supported by Ola Electric. "Ola" and "S1" are trademarks of Ola Electric, used only
> to describe compatibility. Use it only with a scooter you own; changing your
> scooter's software may affect its warranty, and you do so at your own risk.

## Start here

- [Frame catalog](docs/generated/gen1-hvdp-5.0.0-frames.md): 99 known IDs,
  including 77 receive dispatches and 20 distinct transmit IDs.
- [Enum tables](docs/generated/gen1-hvdp-5.0.0-enums.md): 20 enums and 527 values.
- [Canonical JSON](catalog/gen1/hvdp-5.0.0.json): 52 curated signal fields,
  source locations, file hashes, and explicit coverage gaps.
- [Working unlock/drive integration](docs/operations.md): what the dash POC
  demonstrated and what it did not prove about raw CAN.
- [Corrections to early notes](docs/corrections.md): enum tails, hex IDs,
  power-button semantics, and IMU encoding.
- [Open research](docs/open-questions.md): useful starting points for contributors.

The catalog is a starting inventory, not a complete scooter CAN specification.
Known IDs without curated fields are still useful: each names its parser or
transmit method and gives the next researcher a reproducible source location.

## Decode a supplied frame

Python 3.10+; no third-party packages required:

```sh
python3 tools/decode.py --id 0x354 --data 2F00000000000000
```

This synthetic example decodes displayed speed as 47, with the catalog's inferred
km/h unit label. Numeric-layout confidence and unit confidence are separate.
The tool reads only
the hex you supply; it does not connect to the scooter or transmit CAN frames.
Its output retains the profile's raw-runtime validation status.

## Contribute a finding

1. Choose the exact generation and firmware/profile. If these differ from the
   seed, add a new profile rather than changing old ordinals in place.
2. Open a **New signal / frame** or **Correction** issue, or use the
   [frame template](templates/frame.json) in a pull request.
3. Supply the CAN ID, byte/bit layout, units or explicit unknowns, and source
   or short redacted capture evidence. Separate observation from interpretation.
4. Update canonical JSON, regenerate tables, and run the checks below.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the evidence format and review rules.
Documentation, corrections, unexplained IDs, and negative results all help.

```sh
python3 tools/validate.py
python3 tools/render.py
python3 tools/render.py --check
python3 -m unittest discover -s tests -v
```

## Evidence boundaries

Directions are **relative to the Android head unit**, not a claim about which
physical ECU originated a message. `vcan0` is the observed Android interface;
the physical bus topology and bitrate remain unresolved here.

Source recovery proves what a particular app parses or constructs. It does not
by itself prove vehicle acceptance, physical effects, wire timing, units, or
compatibility with another firmware. A successful Android callback is not a
raw-CAN capture. [Validation levels](docs/evidence.md) explain these distinctions.

This repository contains independently written descriptions, protocol facts,
small offline tools, and synthetic examples. APKs, decompiled application code,
identifiers, credentials, and complete private logs are not included.

## Related projects

- [Ola Dash SDK](https://github.com/abhi245y/ola-dash-sdk) (GPL-3.0-or-later):
  an open dash platform for the S1 Pro Gen 1 with runtime themes, plugins and a
  clean-room vehicle-service interface. It reads the same vehicle data this
  catalog describes.
- [Ola Dev Skill](https://github.com/abhi245y/ola-dev-skill) (MIT): an AI-agent
  skill (Claude Code, Codex, Gemini CLI, Cursor) that packages this catalog and
  the SDK for building themes, plugins and analysis tools. It re-syncs and
  releases automatically when this repository changes.

Original repository content is available under the [MIT license](LICENSE).
