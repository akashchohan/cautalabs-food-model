```md
# Camera Subsystem

## Purpose
The CautaLabs Food Model uses two Raspberry Pi Camera Module 3 NoIR cameras to capture high-resolution images of food samples under controlled illumination.

The dual-camera setup allows:
- Redundant capture
- Multi-angle imaging
- Parallel experiments
- Future stereo or differential analysis

## Camera Details
- Model: Raspberry Pi Camera Module 3 NoIR
- Sensor: IMX708
- Resolution: 12 MP
- Interface: CSI-2
- IR sensitivity: Enabled (NoIR variant)

## Detection and Verification
Detected using:
```bash
rpicam-hello --list-cameras

0: imx708
1: imx708 NoIR

Live Preview Test

Camera 0:

rpicam-hello --camera 0 -t 0


Camera 1:

rpicam-hello --camera 1 -t 0

Image Capture Test
rpicam-jpeg -o cam0_test.jpg --camera 0
rpicam-jpeg -o cam1_test.jpg --camera 1
