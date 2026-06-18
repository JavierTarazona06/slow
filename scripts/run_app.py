"""Run the complete SLOW desktop application.

This script is the main project entry point for local development. It prepares
the `src/` import path, creates runtime output folders through `slow.main`, and
starts the Tkinter application workflow.
"""

from __future__ import annotations

from pathlib import Path
import sys
import traceback


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
SRC_DIR: Path = PROJECT_ROOT / "src"


def add_src_to_python_path(src_dir: Path = SRC_DIR) -> None:
    """Make the local `src/` package layout importable without installation."""
    src_dir_text = str(src_dir)
    if src_dir_text not in sys.path:
        sys.path.insert(0, src_dir_text)


def main() -> int:
    """Start the SLOW application and return a shell-friendly exit code."""
    print("Starting SLOW application...", flush=True)
    add_src_to_python_path()

    try:
        from slow.main import main as run_slow_app

        run_slow_app()
    except ModuleNotFoundError as exc:
        missing_module = exc.name or "unknown"
        print(f"Startup failed: missing Python module '{missing_module}'.", file=sys.stderr)
        if missing_module == "tkinter":
            print(
                "Tkinter is a system dependency. On Ubuntu/Debian, install it with: "
                "sudo apt install python3-tk",
                file=sys.stderr,
            )
        else:
            print("Install pip dependencies with: pip install -r requirements.txt", file=sys.stderr)
        return 1
    except Exception as exc:
        if _looks_like_mysql_connection_error(exc):
            print("Startup failed: SLOW could not connect to MySQL.", file=sys.stderr)
            print("Quick start with Docker:", file=sys.stderr)
            print("  docker compose up -d mysql", file=sys.stderr)
            print("  python3 scripts/init_database.py", file=sys.stderr)
            print("  python3 scripts/run_app.py", file=sys.stderr)
            return 1
        print("SLOW application stopped because of an unexpected error.", file=sys.stderr)
        traceback.print_exc()
        return 1
    except KeyboardInterrupt:
        print("\nSLOW application interrupted by user.")
        return 130

    print("SLOW application closed.")
    return 0


def _looks_like_mysql_connection_error(exc: Exception) -> bool:
    """Return True when an exception appears to be a PyMySQL connection failure."""
    return exc.__class__.__name__ == "OperationalError" and "MySQL" in str(exc)


if __name__ == "__main__":
    raise SystemExit(main())
