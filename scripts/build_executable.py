"""Build a standalone SLOW executable with PyInstaller.

The script wraps the project PyInstaller spec so contributors can build from
the repository root without remembering output paths or spec-file details.
Generated files are written to `dist/` and `build/pyinstaller/`.
"""

from __future__ import annotations

from pathlib import Path
import importlib.util
import subprocess
import sys


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
SPEC_FILE: Path = PROJECT_ROOT / "config" / "pyinstaller" / "main.spec"
DIST_DIR: Path = PROJECT_ROOT / "dist"
WORK_DIR: Path = PROJECT_ROOT / "build" / "pyinstaller"


def main() -> int:
    """Build the SLOW executable and return a shell-friendly exit code."""
    print("Building SLOW executable with PyInstaller...", flush=True)

    if not SPEC_FILE.exists():
        print(f"Build failed: missing spec file at {SPEC_FILE}", file=sys.stderr)
        return 1

    if importlib.util.find_spec("PyInstaller") is None:
        print("Build failed: PyInstaller is not installed.", file=sys.stderr)
        print("Install build dependencies with: pip install -r requirements-dev.txt", file=sys.stderr)
        return 1

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--distpath",
        str(DIST_DIR),
        "--workpath",
        str(WORK_DIR),
        str(SPEC_FILE),
    ]

    try:
        subprocess.run(command, cwd=PROJECT_ROOT, check=True)
    except subprocess.CalledProcessError as exc:
        print(f"Build failed: PyInstaller exited with code {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1

    print(f"Build complete. Executable output is in: {DIST_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
