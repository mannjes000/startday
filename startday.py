import subprocess
import sys
from pathlib import Path

# edit these to match what you actually use
MODES = {
    "work": {
        "apps": ["Microsoft Outlook", "zoom.us"],
        "sites": ["https://dppsupport.zendesk.com", "https://dpripro.com/links"],
    },
}

mode = sys.argv[1] if len(sys.argv) > 1 else "work"

if mode not in MODES:
    print(f"Unknown mode {mode!r}. Options: {', '.join(MODES)}")
    sys.exit(1)

plan = MODES[mode]

for app in plan["apps"]:
    subprocess.run(["open", "-a", app])

for site in plan["sites"]:
    subprocess.run(["open", site])

print(f"Started '{mode}' setup.")