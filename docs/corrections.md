# Corrections to the early research notes

The seed was rebuilt from constants, dispatches, constructors, and enum bodies.
It deliberately does not reproduce conflicting handwritten summaries.

| Earlier summary | Source-backed correction |
|---|---|
| IMU Z at `0x65D` | Decimal 1613 is **`0x64D`**. `0x65D` is magnetometer X/Y transmit; Z transmit is `0x66D`. |
| IMU payload described as little-endian float | Parser converts a **little-endian Java integer**, adds **−2000**, then stores a float. It does not decode IEEE754 payload bytes. Physical units remain unknown. |
| `0x153` described as DC-DC voltage/status | Source name is `DCDC_VOLTAGE`, but **byte 1 is PowerButtonStatus** and produces `isPowerButtonPressed`. |
| HMI/App/voice command tables had 106/21/13 entries | Correct counts are **107/22/14**. The old import omitted the final semicolon-terminated entry. |
| Vehicle-command enum had 216 values | Source has **217**, numbered 0..216. |
| Missing final entries | HMI `DIY_mode_Disable`=106; App `FMB_SPEAKER_ENABLE`=21; voice `TURN_ON_ECO_MODE`=13. |
| Side-stand disable/enable described as 91/92 | They are **90/91** in this source profile. |
| HVDP write inventory described as 18 IDs | `MasterCommander` has **20 distinct literal transmit IDs** across 26 construction sites. This is not a whole-scooter inventory. |
| Unlock response flag described as cleared on success | Command ACK stops retry/count and **sets `responseReceived=true`**. |
| Proximity command value placed in byte 1 | `0x690` proximity layout uses command in byte 0, **zero in byte 1, value in byte 2**. Party mode uses a different layout on the same ID. |
| Every transmit payload described as zero-padded | Only unused bytes are zero in each constructor. Magnetometer X/Y uses all eight bytes. |

Exact source locations and hashes are retained in the canonical profile.
The epoch-time constructor also contains an undefined decompiler variable `r1`;
its source-variable binding remains an explicit recovery limitation.
