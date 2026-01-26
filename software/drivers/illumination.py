from gpiozero import OutputDevice

class LightEngine:
    def __init__(self):
        # Hardware Mapping based on your schematic
        # GPIO 17 = 730nm (Red/NIR)
        # GPIO 27 = 850nm (NIR 1)
        # GPIO 22 = 940nm (NIR 2)
        self.led_730 = OutputDevice(17, active_high=True, initial_value=False)
        self.led_850 = OutputDevice(27, active_high=True, initial_value=False)
        self.led_940 = OutputDevice(22, active_high=True, initial_value=False)

    def all_off(self):
        """Safety kill switch for all illumination."""
        self.led_730.off()
        self.led_850.off()
        self.led_940.off()

    def set_wavelength(self, wl):
        """
        Activates a specific wavelength.
        Ensures strict mutual exclusivity (only one ON at a time).
        """
        self.all_off() # Turn others off first
        
        if wl == 730:
            print(f"LIGHTS: Switching to {wl}nm")
            self.led_730.on()
        elif wl == 850:
            print(f"LIGHTS: Switching to {wl}nm")
            self.led_850.on()
        elif wl == 940:
            print(f"LIGHTS: Switching to {wl}nm")
            self.led_940.on()
        else:
            print(f"[WARN] Unknown wavelength {wl} requested.")

    def cleanup(self):
        self.all_off()
        self.led_730.close()
        self.led_850.close()
        self.led_940.close()