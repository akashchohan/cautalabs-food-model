# NIR LED + MOSFET Validation Test

Date: 2025-01-16  
Author: Akash Chohan

## Objective
Validate low-side MOSFET switching of NIR LEDs using GPIO control.

## Hardware
- Raspberry Pi 5
- LM2596 (CC mode)
- MOSFET Trigger Module
- 3W 730 nm LED

## Procedure
1. Powered system with LED disconnected
2. Verified LED remains OFF at boot
3. Connected 730 nm LED
4. Triggered GPIO 17 HIGH for 1 second via Python
5. Observed LED response

## Result
- LED turns ON only when GPIO HIGH
- Turns OFF immediately when GPIO LOW
- No flicker, no overheating
- Current stable (~500 mA)

## Conclusion
MOSFET low-side switching confirmed operational and safe.
