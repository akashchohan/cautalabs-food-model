import subprocess
import os
import time

class CameraSystem:
    def __init__(self, data_dir="captured_data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        
    def capture(self, filename_prefix, cam_idx=0):
        """
        Takes a photo using rpicam-jpeg (Verified Working).
        """
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{filename_prefix}_cam{cam_idx}_{timestamp}.jpg"
        filepath = os.path.join(self.data_dir, filename)
        
        # EXACT command from your successful test
        cmd = [
            "rpicam-jpeg",
            "-o", filepath,
            "--camera", str(cam_idx),
            "-t", "500",      # 500ms timeout for exposure
            "--nopreview"     # No HDMI preview
        ]
        
        print(f"CAMERA: Capturing Cam {cam_idx}...")
        
    def get_preview(self, cam_idx=0):
        """
        Takes a FAST, Low-Res photo for the web dashboard.
        Overwrites 'preview.jpg' constantly.
        """
        filename = f"preview_cam{cam_idx}.jpg"
        filepath = os.path.join(self.data_dir, filename)
        
        cmd = [
            "rpicam-jpeg",
            "-o", filepath,
            "--camera", str(cam_idx),
            "-t", "100",           # Super fast timeout (100ms)
            "--width", "640",      # Low resolution for speed
            "--height", "480",
            "--nopreview"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            return filename
        except Exception:
            return None
