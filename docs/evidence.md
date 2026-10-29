# Evidence and confidence

The seed is based on the HVDP APK identified by SHA256 in the profile. Its Java
decompilation was inspected with JADX 1.5.3. Every source reference includes a
portable path and a SHA256 of that particular decompiled file. Line numbers can
change with another decompiler; use the symbol and hashes alongside the line.

## Keep these claims separate

| Claim | What supports it | What it does not establish |
|---|---|---|
| `static_source` signal | Recovered parser or constructor expression | Actual wire values, intended units, vehicle acceptance |
| `inferred` signal | A stated interpretation and its supporting evidence | A verified decode |
| `runtime_correlated` signal | Relevant raw frames correlated with an observed value/action | Other firmware versions or operating conditions |
| `decompile_gap` payload | Dispatch exists, method body recovery failed | Byte or bit offsets hidden in that body |
| `not_curated` payload | ID and method are inventoried | A complete field review |
| `partial` payload | At least some fields are curated | Meaning of every remaining byte |
| `constant_only` direction | ID constant exists | Actual use in this app's receive/write paths |

`raw_runtime_validation` belongs to the frame record and starts `unverified`.
The seed's live unlock/DRIVE callback observation does not change this flag:
no redacted raw frame trace establishing those bit layouts is published here.

## Preserve the unknowns

Signal `confidence` describes numeric extraction and affine conversion.
`unit_confidence` separately describes the physical unit. Most metric labels in
the seed remain `inferred`; parser names/math alone do not establish them.
The odometer's meters callback and motor-RPM callback name are explicit source
labels. Null units remain `unknown`.

The offline decoder applies the documented affine math using decimal factors;
it is not an emulator of vendor floating-point rounding, clamping, or exceptions.

The parser can call a value "distance" without establishing whether it is
meters, kilometers, a trip increment, or a rolling counter. A field called
`DCDC_VOLTAGE` can in fact deliver power-button status. A Java `float` variable
can hold a converted integer rather than IEEE754 payload bits. Names are clues;
the expression and controlled observations provide the evidence.

The seed mirrors the Java helper's signed 32-bit accumulator for four-byte
integer fields. This is a parser-behavior fact, not a guarantee that a physical
odometer or sensor was intended to use signed wire values. Its intended range,
rollover, and physical units should be independently checked.

Likewise, repeated Android callbacks at approximately 100 ms intervals do not
establish a guaranteed CAN frame period. Consumers must distinguish repeated
snapshots from state transitions.
