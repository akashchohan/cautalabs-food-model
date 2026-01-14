# Manual Trigger Interface

## Purpose
Provides a physical trigger to initiate controlled data acquisition,
useful for repeatable experiments and demonstrations.

## Electrical Design
- Momentary push button (normally open)
- One contact connected to GPIO 23
- One contact connected to GND
- Internal pull-up resistor used (software)

## Logic
- Button released → GPIO HIGH (idle)
- Button pressed → GPIO LOW (trigger)

## Notes
- LED ring not used in initial prototype
- LED feedback planned for future firmware revision
