#!/usr/bin/env python3

import subprocess
from pathlib import Path

script_dir = Path(__file__).parent
project_dir = script_dir.parent
font_dir = project_dir / "fonts"

source_path = project_dir / "tests" / "thumbnail" / "test.typ"
thumbnail_path = project_dir / "thumbnail.png"

subprocess.run(
    [
        "typst",
        "compile",
        "--root",
        str(project_dir),
        "--ignore-system-fonts",
        "--font-path",
        str(font_dir),
        "--ppi",
        "250",
        str(source_path),
        str(thumbnail_path),
    ]
)

subprocess.run(["oxipng", "-o", "max", str(thumbnail_path)])
