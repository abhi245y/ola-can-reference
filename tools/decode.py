#!/usr/bin/env python3
"""Decode supplied hex only. Does not connect to or transmit on a CAN bus."""
import argparse
import json
from pathlib import Path
from catalog import ROOT, decode, load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=ROOT / "catalog/gen1/hvdp-5.0.0.json")
    parser.add_argument("--id", required=True, type=lambda value: int(value, 0), help="CAN ID, e.g. 0x354")
    parser.add_argument("--data", required=True, help="Hex payload; quoted spaces are accepted")
    args = parser.parse_args()
    try:
        result = decode(load(args.profile), args.id, bytes.fromhex(args.data))
    except (ValueError, KeyError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
