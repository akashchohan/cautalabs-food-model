from gpiozero import Button, PWMLED
import asyncio

class PhysicalUI:
    def __init__(self):
        # HARDWARE MAPPING
        # Button on GPIO 23 (Switch)
        # LED on GPIO 16 (Status Indicator)
        
        # Pull_up=True means the switch connects to Ground when pressed
        self.btn = Button(23, pull_up=True, bounce_time=0.1)
        
        # PWMLED allows for "breathing" effects
        self.status_led = PWMLED(16)
        
    def set_callback(self, func):
        """Tells the button what function to run when pressed"""
        self.btn.when_pressed = func

    def set_state(self, state):
        """Visual feedback based on system state"""
        if state == "BOOT":
            # Fast Blink: System is loading
            self.status_led.blink(on_time=0.1, off_time=0.1)
            
        elif state == "READY":
            # Breathing/Pulse: Waiting for user
            self.status_led.pulse(fade_in_time=1, fade_out_time=1)
            
        elif state == "SCANNING":
            # Solid ON: Busy capturing data
            self.status_led.on()
            
        elif state == "ERROR":
            # Slow Blink: Something is wrong
            self.status_led.blink(on_time=0.5, off_time=0.5)
            
        elif state == "OFF":
            self.status_led.off()

    def cleanup(self):
        self.status_led.close()
        self.btn.close()
