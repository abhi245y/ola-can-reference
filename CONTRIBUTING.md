# Contributing

Start with the closest versioned profile in `catalog/`. JSON is canonical;
`docs/generated/` is generated and must not be edited by hand.

## A useful report

Include:

- Scooter generation/model and the relevant firmware or app version.
- CAN ID in hex and decimal, standard/extended format, direction relative to
  your capture point, and actual payload length if known.
- Byte/bit offsets, byte order, signedness, scale, offset, unit, and enum values.
  Write **unknown** when a property has not been established.
- Evidence: a decompiled class/method and line, source-file hash, APK hash when
  available, or a short redacted raw frame window with observation notes.
- Conditions: parked/riding/charging, button or other physical action, repeat
  count, and what changed. Passive captures are sufficient for contributions;
  transmit testing is not required.

Capture only hardware you own or are authorized to study. Private captures can
contain PINs, VINs, location, BLE addresses, or profile data. Submit a minimal
reviewed excerpt instead of an entire session. Preserve unknown/redacted bytes
as unknowns; do not substitute zero and then infer a field from it.

## Catalog conventions

- IDs use `0x354`-style uppercase hex with three digits; `decimal_id` must agree.
- Bit numbering is **LSB0**: bit 0 is the least-significant bit of payload byte 0.
- Seed fields are little endian. A big-endian proposal also needs decoder and
  validator support; do not relabel the order to make it pass.
- `unit: null` means not established, not dimensionless. Enum labels preserve
  source spelling so versions can be compared.
- Keep `unit_confidence` separate from numeric-layout `confidence`: a verified
  bit offset and scale do not prove a km/h, km, A, V, or degC interpretation.
- A frame may have multiple transmit layouts. Put these in `transmit_variants`;
  do not combine incompatible fields into one apparently complete decoder.
- Unused zero bytes in a constructed transmit frame do not prove the same
  bytes are reserved in every firmware or every direction.
- Evidence paths are relative to the named artifact's decompiled root. Do not
  publish absolute private filesystem paths or paste proprietary method bodies.
- Do not mark a raw frame `correlated` based solely on UI or Binder callbacks.
  Link a published `raw_frame_observation` under `observations/` matching the
  profile and ID. The seed's callback-only POC observation is intentionally weaker.

## Add or correct a record

Use `templates/frame.json` for a frame or `templates/observation.json` for raw
runtime evidence. Templates are examples outside the catalog, not discoveries.
New evidence IDs must be unique within the profile. An enum's final value before
the semicolon counts too; see the early-note corrections before importing tables.

Keep unknown fields out of `signals`. Describe partial hypotheses in `notes`
with their limits. Leave `payload_status` as `partial` until all payload fields
and reserved areas have actually been accounted for.

```sh
python3 tools/validate.py
python3 tools/render.py
python3 tools/render.py --check
python3 -m unittest discover -s tests -v
```

CI runs these checks. The validator checks catalog structure and semantics;
`schemas/catalog.schema.json` additionally supports editors and schema tools.
Automated checks cannot establish whether a physical interpretation is true.

## Review

Maintainers check version attribution, evidence, unknowns, privacy, and decoder
fixtures. Conflicting findings should remain visible under separate profiles or
explicit hypotheses until evidence resolves them. A reproducible correction is
more useful than an unqualified claim of support for every Ola scooter.

Contributions to original repository content are accepted under the repository's
MIT license. Do not include third-party APKs, application source, or artwork.
