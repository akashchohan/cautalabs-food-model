## Python Environment

The project uses a Python virtual environment to comply with Debian PEP 668 package management rules.

Setup:
```bash
python3 -m venv cautalabs-env
source cautalabs-env/bin/activate
pip install -r requirements.txt


### Raspberry Pi 5 GPIO backend

On Raspberry Pi 5, Adafruit Blinka requires the lgpio backend.

Install via:
```bash
sudo apt install python3-lgpio

### Python Environment (Raspberry Pi 5)

On Raspberry Pi 5, the Adafruit Blinka GPIO backend relies on the system
package `python3-lgpio`. To allow Blinka access to this backend, the
virtual environment is created with system site packages enabled:

```bash
python3 -m venv cautalabs-env --system-site-packages


