# Manual Trigger Interface

## Purpose
Provides a physical trigger to initiate controlled data acquisition,
useful for repeatable experiments and demonstrations.

## Electrical Design
- Momentary push button (normally open)
- One contact connected to GPIO 23
- One contact connected to GND
- Internal pull-up resistor used (software)

## User Interface

| Component | Function | GPIO | Notes |
|--------|--------|------|------|
| Button | Input (momentary) | GPIO 23 | Pull-up enabled |
| Button LED | Status indicator | GPIO 16 | 330–470 Ω resistor |

## Logic
- Button released → GPIO HIGH (idle)
- Button pressed → GPIO LOW (trigger)

## Notes
- LED ring not used in initial prototype
- LED feedback planned for future firmware revision
