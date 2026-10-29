# Unlock, ignition, and the Android service boundary

The initial dash POC replaces the stock HMI client UI while retaining Ola's
background services. This explains where a user action enters the protocol.

## Normal owner workflow

1. The handlebar power button wakes the system and requests the passcode screen.
2. The UI submits the existing six-digit PIN to the stock profile service using
   `challengeUnlockByPasscode(pin, false)`.
3. That service checks the PIN and remaining attempts, selects the matching
   profile, and requests authenticated unlock through the vehicle parser.
4. The application waits for actual vehicle state; PIN acceptance alone is not
   proof of physical unlock, PARK, or DRIVE.
5. The owner's next physical power-button action enters DRIVE through the
   scooter's existing controls and interlocks. Mode changes remain handlebar actions.

Static lower-layer findings include the `PASSCODE_AUTH` entry in the versioned
HMI enum, the command-ACK parser, lock-state feedback on `0x144`, and the
passcode-window signal on `0x6AE`. Command ACK means acknowledgment; lock state
and vehicle mode provide different feedback.

`Ride_Now` and `Lock_Now` are responses in the stock side-stand override path.
Their existence is not evidence that normal start requires either command, or
that a touchscreen start command should replace the physical procedure.

## What worked in the POC

On 2026-10-30, the owner reported using the replacement keypad to unlock the
scooter. Application logs subsequently showed PIN accepted, BCM unlocked,
vehicle `DRIVE`, reported mode `NORMAL`, and active host keep-alive.

The published [sanitized observation](../observations/gen1/2026-10-30-unlock-drive.json)
contains a callback-level summary, not a raw-CAN capture or a PIN. This validates
the service/UI integration on that scooter. It does not validate every signal
layout, riding behavior, range estimate, fault condition, or firmware version.

## Host responsibilities

`IVehicleService` exposes parser and commander binders. Parser subscriptions
cover motor, battery, display, vehicle modes, alerts, and other domains. The
replacement dash reads these decoded callbacks and sends a touch/activity report
through `sendTouchEvent` for its testing keep-alive behavior.

The captured source constructs touch/activity frames on `0x643`. Stock touch
activity and the POC's unlocked-state keep-alive policy are different application
policies; the frame's boolean layout alone does not prescribe a wake policy.

Repeated SLEEP, lock-state, and passcode-window snapshots were seen while testing.
The POC needed idempotent handling so repeated reports did not erase a partial
PIN or reopen an in-flight verification. No new signal edge should be inferred
from an identical repeated callback.
