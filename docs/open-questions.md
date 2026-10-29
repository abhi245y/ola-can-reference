# Open research

These are scoped gaps, not evidence that a feature or message does not exist.

| Area | Current boundary | Useful next evidence |
|---|---|---|
| `0x143` vehicle modes | Dispatch known; method body recovery failed | Recover byte/bit map and correlate raw frames with PARK/DRIVE callbacks. Lead: byte 1 went 0x24 -> 0x54 on entering reverse ([2026-10-30 drive-mode observation](../observations/gen1/2026-10-30-drive-modes.json)) |
| `0x353` telltales | Dispatch and callback family known | Recover individual indicator, lamp, side-stand, and fault fields. Lead: byte 6 went 0x04 -> 0x64 on entering reverse ([2026-10-30 drive-mode observation](../observations/gen1/2026-10-30-drive-modes.json)) |
| `0x660` feature availability | Dispatch known; decompile gap | Recover feature-bit map with exact app version |
| `0x6AD` handlebar D-pad | Dispatch known; decompile gap | Decode button fields and press/release/repeat behavior |
| `0x223` trip byte | Byte position known | Establish units, counter semantics, rollover, and reset behavior. Note: the decoded `onDistanceCovered` callback stayed 0 during a short ride on 2026-10-30 while the odometer advanced |
| IMU values | LE integer conversion plus offset known | Establish units, axes, valid ranges, signedness/rollover intent |
| Raw frame timing | No guaranteed periods in the seed | Short synchronized passive traces across sleep/wake/park/drive |
| Source attribution | Android interface is `vcan0` | Establish bridge topology, physical bus bitrate, and originating ECUs |
| Additional battery/cell frames | Not decoded in this HVDP surface | Versioned evidence from other services or passive traces |
| `0x273`, `0x6DF` | Constants present, no dispatch here | Find actual consumers or evidence these are unused in this version |
| New generations | Gen 1 seed only | Separate Gen 2/3/other profiles with artifact identity and observations |

Repository issues can hold unexplained IDs or competing interpretations before
they are mature enough for a curated decoder. Include negative search boundaries
so the next contributor can avoid repeating the same work.

Drive-mode naming: the stock HMI shows `DriveModes.LIMPHOME` as **Eco** (rider-confirmed on one Gen 1 scooter), and Easy Park reverse reports `PARK_ASSIST`. Whether plain reverse reports `REVERSE` is still open. See the [2026-10-30 drive-mode observation](../observations/gen1/2026-10-30-drive-modes.json).
