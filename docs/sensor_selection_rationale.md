# Sensor Selection Rationale

## Design Philosophy
The CautaLabs Food Model emphasizes:
- Non-contact sensing
- Multi-modal data fusion
- Compact and low-cost design
- On-device intelligence

## Selected Sensors and Rationale

### BME690
Provides environmental context (VOC, temperature, humidity, pressure) critical for spoilage analysis.

### AS7343
Captures wavelength-resolved spectral data beyond RGB imaging, enabling chemical and surface insights.

### VL53L8CX
Provides dense depth information unavailable from cameras or ultrasonic sensors.

### MLX90614
Enables non-contact temperature measurement of food surfaces.

### Dual NoIR Cameras
Enable controlled illumination imaging across NIR bands for texture and reflectance analysis.

## Why Not Ultrasonic or Single-Sensor Systems
- Ultrasonic sensors lack spatial resolution
- Single-modality systems fail under real-world variability
- Sensor fusion improves robustness and explainability