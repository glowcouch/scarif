#!/usr/bin/env python3

import subprocess
from pathlib import Path

script_dir = Path(__file__).parent
project_dir = script_dir.parent
examples_dir = project_dir / "examples"
font_dir = project_dir / "fonts"

examples = sorted(examples_dir.glob("*.typ"))

for example in examples:
    output = example.with_suffix(".svg")
    subprocess.run(
        [
            "typst",
            "compile",
            "--root",
            str(project_dir),
            "--ignore-system-fonts",
            "--font-path",
            str(font_dir),
            str(example),
            str(output),
        ]
    )
