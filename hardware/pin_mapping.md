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


## Notes
This mapping may evolve slightly during integration,
but GPIO roles are kept stable once sensors are validated.
