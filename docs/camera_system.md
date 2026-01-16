```md
# Camera System Architecture

## Overview
The Cautalabs Food Model uses a dual-camera architecture to support multi-modal imaging. Two Raspberry Pi Camera Module 3 NoIR units are operated simultaneously to enable flexible capture strategies such as reference imaging, spectral imaging support, and redundancy.

## Hardware Configuration
- Camera model: Raspberry Pi Camera Module 3 NoIR and Raspberry Pi Camera Module 3
- Sensor: Sony IMX708
- Interfaces:
  - Camera 0 → CSI port CAM0
  - Camera 1 → CSI port CAM1

## Software Stack
- OS: Raspbian GNU/Linux 13 (trixie)
- Camera framework: rpicam-apps (successor to libcamera-apps)

## Detection and Enumeration
Both cameras are enumerated automatically by the OS when `camera_auto_detect=1` is enabled.

Detection command:
```bash
rpicam-hello --list-cameras