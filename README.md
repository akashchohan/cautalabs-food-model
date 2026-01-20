# CautaLabs Food Model  
### A Multi-Modal, AI-Ready Food Safety and Quality Sensing Device

## Overview
The **CautaLabs Food Model** is a compact, low-cost, multi-modal sensing platform designed to assess food quality, safety, and early spoilage indicators using **sensor fusion** and **on-device intelligence**.

The system integrates optical, spectral, thermal, structural, and environmental sensing into a single experimental prototype. It is built to support reproducible data collection, explainable analysis, and future AI-driven inference directly at the edge.

This repository documents the complete hardware bring-up, system design, and measurement methodology of the prototype.

---

## What the System Measures
The device captures complementary information from multiple physical domains:

- **Optical texture & reflectance** (dual NoIR cameras)
- **Spectral response** (AS7343 multispectral sensor)
- **Surface temperature** (MLX90614 IR sensor)
- **Environmental context** (BME690: VOC, temperature, humidity, pressure)
- **3D surface structure** (VL53L8CX multi-zone ToF)
- **Controlled illumination** (730 nm, 850 nm, 940 nm NIR LEDs)

These signals are synchronized and logged to form a structured dataset suitable for statistical analysis and AI model training.

---

## Why This Project Exists (Motivation)
This project emerged from direct, first-hand exposure to real-world food handling environments rather than from purely academic assumptions.

During my first months in the UK, I worked as a **chef with no prior professional kitchen experience**. In that role, I observed how food quality and expiry are often judged by **visual inspection, estimation, or routine**, rather than by any measurable or verifiable process.

Later, while working as a **Catering Assistant and Barista (Costa Coffee) at Freedom Leisure, Guildford Spectrum**, I saw similar patterns at scale:  
large food throughput, reliance on manual checks, and limited objective verification of freshness or spoilage.

These experiences highlighted a clear gap:
> Food safety decisions are often made without sensing, data, or traceability.

The CautaLabs Food Model is a technical response to that gap.

---

## Design Philosophy
The system is designed around the following principles:

- **Non-contact sensing**  
- **Explainable measurements (not black-box only)**  
- **Sensor fusion over single-sensor dependency**  
- **Edge-first computation**  
- **Compact, affordable, reproducible hardware**

The goal is not to replace existing standards, but to explore how **low-cost sensing + AI** can augment food safety practices.

---

## Hardware Platform
- Raspberry Pi 5 (8 GB)
- AI HAT (26 TOPS)
- Dual Raspberry Pi Camera Module 3 NoIR
- AS7343 spectral sensor
- VL53L8CX 8×8 ToF sensor
- MLX90614 IR temperature sensor
- BME690 environmental sensor
- 730 nm / 850 nm / 940 nm NIR LEDs
- LM2596 CC/CV LED drivers
- MOSFET GPIO switching
- OLED status display
- User input button
- VOC chamber fan

All hardware components are documented with wiring, rationale, and validation logs.

---

## Repository Structure (Can be different or updated)
cautalabs-food-model/
├── docs/ # System-level documentation
├── hardware/ # Sensors, wiring, power, optics
├── software/ # Control, acquisition, utilities
├── experiments/ # Measurement trials
├── data_schema/ # Dataset format definitions
├── build_logs/ # Step-by-step bring-up logs
└── media/ # Photos and videos of the prototype


---

## Current Status
✔ Hardware bring-up complete  
✔ All sensors validated individually  
✔ GPIO, LEDs, cameras, and user input tested  
✔ System ready for software integration and dataset acquisition  

---

## Intended Use
This prototype is intended for:
- Research and experimentation
- Dataset generation
- Edge AI development
- Academic publication groundwork
- PhD and research lab evaluation

It is **not** a commercial product and is not intended for deployment in food service environments.

---

## Author
**Akash Chohan**  
MSc Data Science  
University of Surrey, England  

Background spanning:
- Embedded systems & sensing
- Experimental physics (ODMR, quantum sensing)
- Edge AI and data science
- Hands-on food service experience informing real-world constraints

---

## License
This project is released for research and educational purposes.  
All designs, documentation, and data structures are original unless otherwise stated.
