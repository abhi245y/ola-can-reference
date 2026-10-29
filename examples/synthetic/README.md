# Synthetic decoder examples

These values are deliberately invented test vectors, not scooter captures.
Unit interpretations keep the confidence recorded in the catalog and output.

| ID | Payload | Expected result |
|---|---|---|
| `0x354` | `2F00000000000000` | Displayed speed 47 km/h |
| `0x352` | `4600000000000000` | Displayed SOC 70% |
| `0x144` | `0100000000000000` | Lock-state enum `Vehicle_Unlocked` |
| `0x153` | `0001000000000000` | Power-button enum `Normal_Press` |
| `0x15B` | `0200000000000000` | Drive-mode enum `NORMAL` |

The unit tests cover additional boundary cases and the terminal command-enum
entries omitted by an early table generator. None of these examples transmits
a frame or proves physical behavior.
