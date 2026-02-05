#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

script_dir = Path(__file__).parent
project_dir = script_dir.parent
font_dir = project_dir / "fonts"

args = ["tt", "--root", str(project_dir), "--font-path", str(font_dir)]

if len(sys.argv) > 1:
    args += sys.argv[1:]
else:
    args += ["run", "--no-fail-fast"]

subprocess.run(args)
