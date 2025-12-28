# Phase 1 – Core System Bring-up

Date: 2025-01-XX  
Author: Akash

## Hardware connected
- Raspberry Pi 5 (8GB)
- AI HAT (26 TOPS)
- Raspberry Pi Camera Module 3 NoIR
- 0.96" OLED display (I2C)
- RTC battery module

## Steps performed
1. Installed Raspberry Pi OS
2. Attached AI HAT and verified boot
3. Connected NoIR camera and tested with libcamera
4. Connected OLED display via I2C and verified output
5. Verified RTC time persistence across reboot

## Observations
- System booted normally with AI HAT attached
- Camera detected successfully
- OLED display working correctly
- RTC functioning as expected

## Notes
This phase establishes the base compute and I/O platform for all further sensing modules.
