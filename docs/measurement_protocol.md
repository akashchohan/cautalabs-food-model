# Measurement Protocol

## Step 1: System Initialization
- Power Raspberry Pi
- Verify I2C bus stability
- Confirm sensor detection

## Step 2: Environmental Baseline
- Record temperature, humidity, pressure, VOC
- Stabilize chamber airflow

## Step 3: Optical Capture
- Activate selected NIR LED
- Capture camera image(s)
- Deactivate LED

## Step 4: Spectral Measurement
- Read AS7343 spectral channels
- Store timestamped values

## Step 5: Structural Measurement
- Trigger VL53L8CX ranging
- Capture multi-zone depth map

## Step 6: Thermal Measurement
- Read MLX90614 object temperature

## Step 7: Data Logging
- Save all measurements with timestamps
- Associate with sample ID and capture conditions