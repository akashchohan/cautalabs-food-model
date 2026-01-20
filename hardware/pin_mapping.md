# GPIO Pin Mapping (Planned)

## I2C Bus
- SDA / SCL:
  - OLED display
  - AS7343 spectral sensor
  - MLX90614 thermal sensor
  - VL53L8CX ToF sensor

## Camera Interfaces
- CSI-0: NoIR Camera
- CSI-1: RGB Camera

## GPIO Outputs
- GPIO17: 730 nm LED (via MOSFET)
- GPIO27: 850 nm LED (via MOSFET)
- GPIO22: 940 nm LED (via MOSFET)
- GPIO23: White LED (via MOSFET)

## Actuators
- GPIO24: VOC chamber fan

## User Input
- GPIO25: Manual capture button

## Sensor-Specific Allocation

### BME690
- Interface: I2C (shared)
- Power: 3.3 V
- Fan: GPIO24 (via MOSFET)

### MLX90614
- Interface: I2C
- Power: 3.3 V
- Address: 0x5A

## NIR Illumination System (Low-side MOSFET Switching)

| Function | Component | Raspberry Pi Pin | BCM GPIO | Notes |
|--------|----------|------------------|----------|-------|
| 730 nm LED control | MOSFET TRIG | Pin 11 | GPIO 17 | 1 s pulse tested |
| 850 nm LED control | MOSFET TRIG | Pin 13 | GPIO 27 | Reserved |
| 940 nm LED control | MOSFET TRIG | Pin 15 | GPIO 22 | Reserved |
| MOSFET power | VIN+ | Pin 2 | 5V | Shared 5V rail |
| MOSFET ground | GND | Pin 6 | GND | Common ground |

## LED Driver (LM2596 – Constant Current Mode)

- VIN+ → Raspberry Pi 5V
- VIN− → Raspberry Pi GND
- OUT+ → LED Anode (+)
- OUT− → Not used directly (low-side switching via MOSFET)

**Configured per LED:**
- Output voltage: 2.2–2.5 V
- Current limit: 500–600 mA
- Operation mode: pulsed only (<100 ms recommended)

## Camera Interfaces

| Device | Interface | Notes |
|------|----------|------|
| Camera Module 3 NoIR | CSI CAM0 | Primary imaging |
| Camera Module 3 NoIR | CSI CAM1 | Secondary / reference |

## User Interface

| Component | Pin | Raspberry Pi GPIO | Notes |
|--------|----|------------------|------|
| Button (switch) | SW | GPIO 23 | Pull-up enabled |
| Button LED | LED | GPIO 16 | Status indicator |

## Optional / Reserved Pins
- AS7343: I, G (not connected)
- VL53L8CX: INT (reserved), MISO (SPI only)

## User Interface

| Component | Function | GPIO | Notes |
|--------|--------|------|------|
| Button | Input (momentary) | GPIO 23 | Pull-up enabled |
| Button LED | Status indicator | GPIO 16 | 330–470 Ω resistor |


## Notes
This mapping may evolve slightly during integration,
but GPIO roles are kept stable once sensors are validated.
- MOSFET module is low-side switching (VIN+ internally tied to OUT+)
- Ground is switched, not 5V
- Only one NIR LED is enabled at a time

Sensor	Typical Address
BME690	0x76 or 0x77
OLED SSD1306	0x3C
MLX90614	0x5A
AS7343	0x39
VL53L8CX	0x29

python3 mlx90614_test.py
