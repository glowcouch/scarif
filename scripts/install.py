#!/usr/bin/env python3

import os
import platform
import shutil
import subprocess
import tomllib
from pathlib import Path

script_dir = Path(__file__).parent
project_dir = script_dir.parent

subprocess.run([str(script_dir / "package.py")])

# Read version from typst.toml
with open(project_dir / "typst.toml", "rb") as f:
    config = tomllib.load(f)
    version = config["package"]["version"]

system = platform.system()
if system == "Linux":
    data_dir = Path(os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share"))
elif system == "Darwin":
    data_dir = Path.home() / "Library" / "Application Support"
elif system == "Windows":
    data_dir = Path(os.getenv("APPDATA"))
else:
    raise RuntimeError(f"Unsupported platform: {system}")

typst_packages_dir = data_dir / "typst" / "packages" / "local"
typst_packages_dir.mkdir(parents=True, exist_ok=True)

package_dst = typst_packages_dir / "scarif"

if package_dst.exists():
    shutil.rmtree(package_dst)

shutil.copytree(project_dir / "scarif", package_dst)

template_file = package_dst / version / "template" / "main.typ"
if template_file.exists():
    content = template_file.read_text()
    content = content.replace("preview", "local")
    template_file.write_text(content)
