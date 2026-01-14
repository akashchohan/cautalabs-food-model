## Phase 2 – BME690 VOC Sensor Integration

- BME690 connected via I2C (address confirmed)
- Temperature, humidity, pressure, and gas resistance validated
- VOC response observed to human breath
- 5V fan integrated via MOSFET on GPIO24
- Fan successfully used for purge cycles

This establishes the environmental and chemical sensing baseline for the system.

- I2C scan performed using `i2cdetect -y 1`
- BME690 detected at address 0x76
- No other I2C devices present at this stage
- Confirms clean I2C bus and correct wiring

## Phase 3 – MLX90614 Thermal Sensor (PASS 1)

- MLX90614 connected via shared I2C bus
- Sensor detected at address 0x5A
- Coexists correctly with BME690 (0x76)
- No I2C conflicts observed

## PASS 1 Summary

- Multi-device I2C bus validated with four active devices:
  - BME690 (0x76)
  - MLX90614 (0x5A)
  - AS7343 (0x39)
  - OLED (0x3C)
- Bus stability confirmed under real load
- Sensors validated using both probe-based and functional read methods
