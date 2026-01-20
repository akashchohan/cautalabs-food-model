# NIR LED Illumination System (730 nm, 850 nm, 940 nm)

## Purpose
The Near-Infrared (NIR) LED illumination system provides controlled, wavelength-specific lighting for food sample analysis. It is designed to enable reflectance-based imaging and spectroscopy using NoIR cameras and spectral sensors.

By sequentially illuminating food samples at different NIR wavelengths, the system captures complementary information related to surface texture, moisture content, fat composition, and early spoilage indicators.

## LED Specifications
Three high-power LEDs are used:

| Wavelength | Power | Forward Voltage | Rated Current |
|-----------|-------|-----------------|---------------|
| 730 nm    | 3 W   | 1.8–2.2 V       | 600–700 mA   |
| 850 nm    | 3 W   | 1.6–1.8 V       | 600–700 mA   |
| 940 nm    | 3 W   | 1.6–1.8 V       | 600–700 mA   |

Each LED is mounted on a 20 mm aluminum PCB for thermal dissipation.

## Optical Setup
- 60° collimator lenses are mounted above each LED
- LEDs are positioned to uniformly illuminate the food sample area
- Narrow illumination angle improves signal-to-noise ratio and repeatability
- LEDs are never activated simultaneously to avoid spectral cross-talk

## Power and Control Architecture
Each LED channel consists of:
- LM2596 CC/CV buck converter (constant-current configuration)
- Logic-level MOSFET trigger module
- Raspberry Pi GPIO control

### Power Flow
Raspberry Pi 5V
└── LM2596 (CC mode, current-limited)
└── LED (+ / −)
└── MOSFET (low-side switching)
└── GND

### Control Logic
- MOSFET trigger pin connected to Raspberry Pi GPIO
- GPIO HIGH → LED ON
- GPIO LOW → LED OFF
- LEDs are activated for short, controlled durations (typically < 2 s)

## GPIO Assignment
| LED Wavelength | GPIO Pin |
|---------------|----------|
| 730 nm        | GPIO 17  |
| 850 nm        | GPIO 27  |
| 940 nm        | GPIO 22  |

(GPIO numbers use BCM numbering)

## Safety Considerations
- LEDs are current-limited to prevent thermal runaway
- MOSFET isolation protects Raspberry Pi GPIOs
- LEDs are never viewed directly during operation
- Short duty cycles reduce heating and improve consistency

## Verification and Testing
- Each LED was individually tested via GPIO control
- Sequential activation confirmed correct wiring
- No cross-activation or unintended illumination observed
- Voltage and current verified under load

## Role in Sensor Fusion
The NIR LED system enables:
- Controlled reflectance imaging with NoIR cameras
- Spectral consistency for AS7343 measurements
- Improved robustness of AI-based food analysis models
- Repeatable, lab-grade illumination conditions

## Status
✔ Fully assembled  
✔ Electrically tested  
✔ GPIO-controlled  
✔ Integrated with camera capture workflow  
✔ Ready for dataset acquisition
