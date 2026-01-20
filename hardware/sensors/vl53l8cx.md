# VL53L8CX Time-of-Flight Sensor

## Purpose
The VL53L8CX is a multi-zone (8×8) time-of-flight (ToF) depth sensor used in the CautaLabs Food Model to capture spatial structure, surface unevenness, and volumetric characteristics of food samples.

Unlike ultrasonic sensors, the VL53L8CX provides dense depth information at millimeter-scale resolution, enabling non-contact structural assessment of food items.

## Key Specifications
- Sensor type: Multi-zone ToF (8×8 zones)
- Wavelength: 940 nm (VCSEL)
- Interface: I2C
- Typical I2C address: `0x29`
- Operating voltage: 3.3 V

## Wiring (I2C mode)
| VL53L8CX Pin | Raspberry Pi 5 |
|-------------|----------------|
| VIN         | 3.3V           |
| GND         | GND            |
| SDA         | SDA (GPIO 2)   |
| SCL         | SCL (GPIO 3)   |
| LPn / XSHUT | Not connected  |
| INT         | Not connected  |
| SPI pins    | Not connected  |

Note: The breakout board used includes an internal pull-up on LPn, allowing automatic startup in I2C mode.

## Bring-up Verification
- Detected using:
  ```bash
  i2cdetect -y 1
  Successfully observed at address 0x29