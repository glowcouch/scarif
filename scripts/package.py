#!/usr/bin/env python3

import shutil
import tomllib
from pathlib import Path

script_dir = Path(__file__).parent
project_dir = script_dir.parent

with open(project_dir / "typst.toml", "rb") as f:
    config = tomllib.load(f)
    version = config["package"]["version"]

package_dir = project_dir / "scarif" / version
package_dir.mkdir(parents=True, exist_ok=True)

shutil.copytree(project_dir / "src", package_dir / "src", dirs_exist_ok=True)
shutil.copytree(project_dir / "template", package_dir / "template", dirs_exist_ok=True)
shutil.copytree(project_dir / "examples", package_dir / "examples", ignore=shutil.ignore_patterns("*.typ"), dirs_exist_ok=True)
shutil.copy2(project_dir / "LICENSE-MIT", package_dir / "LICENSE-MIT")
shutil.copy2(project_dir / "LICENSE-APACHE", package_dir / "LICENSE-APACHE")
shutil.copy2(project_dir / "README.md", package_dir / "README.md")
shutil.copy2(project_dir / "typst.toml", package_dir / "typst.toml")
shutil.copy2(project_dir / "thumbnail.png", package_dir / "thumbnail.png")
