"""Verify that built distributions preserve all package source files and assets."""

import tarfile
import tomllib
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
project = tomllib.loads((root / "pyproject.toml").read_text())["project"]
stem = project["name"].replace("-", "_") + "-" + project["version"]
wheel_path = root / "dist" / (stem + "-py3-none-any.whl")
sdist_path = root / "dist" / (stem + ".tar.gz")
files = [path for path in (root / "src/compas_blender").rglob("*") if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}]
with zipfile.ZipFile(wheel_path) as wheel, tarfile.open(sdist_path) as sdist:
    for path in files:
        expected = path.read_bytes()
        wheel_name = path.relative_to(root / "src").as_posix()
        sdist_name = stem + "/" + path.relative_to(root).as_posix()
        if wheel.read(wheel_name) != expected:
            raise SystemExit(f"Wheel content differs: {wheel_name}")
        stream = sdist.extractfile(sdist_name)
        if stream is None or stream.read() != expected:
            raise SystemExit(f"Sdist content differs: {sdist_name}")
print(f"Verified {len(files)} source files and assets in both distributions.")
