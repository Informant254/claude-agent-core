# security_hardening.py - Additional Fortress Layer

import os
import signal
import psutil

def enable_fortress_mode():
    """Extra runtime protections."""
    print("[FORTRESS] Extra hardening enabled.")
    # Disable dangerous signals if possible
    try:
        signal.signal(signal.SIGTERM, lambda s, f: sys.exit(1))
    except:
        pass

def detect_debugger():
    """Basic anti-debug."""
    if 'pdb' in sys.modules or os.getenv('DEBUG'):
        print("[!] Debugger detected - fortress lockdown.")
        os._exit(1)
