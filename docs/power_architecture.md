```md
# Power Architecture

## Overview
The CautaLabs Food Model is powered from a single 5V USB-C supply connected to the Raspberry Pi 5. All subsystems derive regulated power from this source.

## Power Sources
- Input: USB-C power adapter (5V, up to 5A)
- Raspberry Pi 5 acts as the central power distribution node

## Power Domains
| Component            | Voltage |
|---------------------|---------|
| Raspberry Pi 5      | 5V      |
| Sensors (I2C)       | 3.3V    |
| Cameras             | CSI bus |
| NIR LEDs            | Buck-regulated CC/CV |
| Fan (VOC chamber)   | 5V      |

## LED Power Regulation
- Each NIR LED is driven via:
  - LM2596 CC/CV buck converter
  - Logic-level MOSFET for GPIO control
- Current-limited operation protects LEDs and ensures repeatability

## Safety Considerations
- No direct LED connection to Raspberry Pi GPIO
- MOSFET isolation prevents backfeeding
- All grounds are common