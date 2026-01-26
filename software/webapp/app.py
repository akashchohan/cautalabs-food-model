import sys
import os
import asyncio
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from gpiozero import OutputDevice

# --- PATH SETUP ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- DRIVER IMPORTS ---
from drivers.illumination import LightEngine 
from drivers.display import StatusDisplay
from drivers.user_interface import PhysicalUI
from drivers.camera import CameraSystem

app = FastAPI()

# Mount data folder
os.makedirs("captured_data", exist_ok=True)
app.mount("/data", StaticFiles(directory="captured_data"), name="data")

templates = Jinja2Templates(directory="software/webapp/templates")

# --- HARDWARE INITIALIZATION ---
lights = LightEngine()
screen = StatusDisplay()
ui = PhysicalUI()
cam = CameraSystem(data_dir="captured_data")
fan = OutputDevice(24)

SYSTEM_STATE = "BOOT" 
# We now store TWO images (Cam 0 and Cam 1)
LAST_IMAGES = {"cam0": None, "cam1": None}

async def wait_for_network():
    """
    Fixes the 'No Network' issue by retrying for 30 seconds.
    """
    print("Waiting for Network...")
    for _ in range(30):
        ip = screen.get_ip_address()
        if ip != "No Network" and ip != "127.0.0.1":
            screen.show_status(line1="IP Address:", line2=ip)
            return
        await asyncio.sleep(1)
    
    # If still no network, show error
    screen.show_status(line1="Error:", line2="No Wi-Fi Found")

async def run_scan_sequence():
    """
    Main Scan: Now supports DUAL CAMERAS
    """
    global SYSTEM_STATE, LAST_IMAGES
    SYSTEM_STATE = "SCANNING"
    ui.set_state("SCANNING")
    
    print("--- STARTING DUAL-CAM SCAN ---")
    
    # 1. Environment
    screen.show_status("Environment", "Fan: ON")
    fan.on()
    await asyncio.sleep(2)
    fan.off()

    # 2. Capture Sequence (Dark -> 730 -> 850 -> 940)
    wavelengths = [730, 850, 940]
    
    for wl in wavelengths:
        # A. Lights On
        screen.show_status("Capturing", f"{wl}nm Band")
        lights.set_wavelength(wl)
        await asyncio.sleep(0.5) 
        
        # B. Capture BOTH Cameras
        loop = asyncio.get_running_loop()
        
        # Camera 0
        file0 = await loop.run_in_executor(None, cam.capture, f"scan_{wl}nm", 0)
        if file0: LAST_IMAGES["cam0"] = os.path.basename(file0)
        
        # Camera 1 (Sequential capture to prevent USB overload)
        file1 = await loop.run_in_executor(None, cam.capture, f"scan_{wl}nm", 1)
        if file1: LAST_IMAGES["cam1"] = os.path.basename(file1)
            
    lights.all_off()
    
    # 3. Finish
    screen.show_status("Scan Complete", "Saved.")
    await asyncio.sleep(2)
    SYSTEM_STATE = "READY"
    ui.set_state("READY")
    screen.show_status("CautaLabs", "Ready")

def handle_button_press():
    global SYSTEM_STATE
    if SYSTEM_STATE == "BOOT":
        SYSTEM_STATE = "READY"
        ui.set_state("READY")
        screen.show_status("CautaLabs", "Ready")
    elif SYSTEM_STATE == "READY":
        loop = asyncio.get_event_loop()
        loop.create_task(run_scan_sequence())

ui.set_callback(handle_button_press)

@app.on_event("startup")
async def startup_event():
    global SYSTEM_STATE
    SYSTEM_STATE = "BOOT"
    ui.set_state("BOOT")
    screen.show_status("Booting...", "Please Wait")
    # Start the network checker in background
    asyncio.create_task(wait_for_network())

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "status": SYSTEM_STATE,
        "images": LAST_IMAGES
    })

@app.get("/api/preview/{cam_idx}")
async def get_preview_frame(cam_idx: int):
    """
    Takes a quick photo and tells the browser what file to load.
    """
    # Run the camera in a thread to keep server fast
    loop = asyncio.get_running_loop()
    filename = await loop.run_in_executor(None, cam.get_preview, cam_idx)
    
    if filename:
        return {"status": "ok", "image": filename}
    else:
        return {"status": "error"}

@app.get("/api/start")
async def api_start_scan(background_tasks: BackgroundTasks):
    """
    Allows the Mac Web App to trigger the scan.
    """
    global SYSTEM_STATE
    if SYSTEM_STATE == "READY" or SYSTEM_STATE == "BOOT":
        # Run the scan in the background so the web server doesn't freeze
        background_tasks.add_task(run_scan_sequence)
        return {"message": "Scan Started"}
    else:
        return {"message": "System Busy"}

# ------------------------------------------------

# --- NEW EMERGENCY STOP ---
@app.get("/api/stop")
async def stop_system():
    global SYSTEM_STATE
    print("EMERGENCY STOP TRIGGERED")
    lights.all_off()
    fan.off()
    SYSTEM_STATE = "READY"
    ui.set_state("OFF")
    screen.show_status("System Stopped", "Manual Reset")
    return {"message": "System Stopped"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#  ~/cautalabs-food-model/software/app.py akashchohan@192.168.2.3:~/cautalabs_project/software/webapp/app.py