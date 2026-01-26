from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import socket

class StatusDisplay:
    def __init__(self):
        # Initialize I2C (Address 0x3C as per your hardware list)
        serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(serial)
        # Load default font
        self.font = ImageFont.load_default()

    def get_ip_address(self):
        """Finds the current WiFi IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0)
            # Doesn't actually connect, just determines route
            s.connect(('8.8.8.8', 1)) 
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "No Network"

    def show_status(self, line1="System Ready", line2=""):
        """Updates the OLED screen"""
        ip = self.get_ip_address()
        
        with canvas(self.device) as draw:
            # Top Bar: IP Address
            draw.text((0, 0), f"IP: {ip}", font=self.font, fill="white")
            # Separator Line
            draw.line((0, 12, 127, 12), fill="white")
            # Status Lines
            draw.text((0, 15), line1, font=self.font, fill="white")
            draw.text((0, 28), line2, font=self.font, fill="white")

    def clear(self):
        self.device.clear()
