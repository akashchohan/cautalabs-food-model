# Dual Camera System Validation

Date: 2025-01-16
Author: Akash Chohan

## Objective
Validate simultaneous operation of two Raspberry Pi Camera Module 3 NoIR units for multi-modal food sensing.

## Hardware
- Raspberry Pi 5 (8GB)
- AI HAT (26 TOPS)
- 1 × Raspberry Pi Camera Module 3 NoIR (IMX708)
- 1 × Raspberry Pi Camera Module 3  (IMX708)
- CSI interfaces: CAM0 and CAM1

## Test Procedure

### 1. Camera Detection
Verified that the operating system correctly detects both cameras.

Command used:
```bash
rpicam-hello --list-cameras
