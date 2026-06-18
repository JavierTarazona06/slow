"""Initialize the MySQL schema required by the SLOW application."""

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
    """Create the database tables used by SLOW."""
    print("Initializing SLOW database schema...", flush=True)
    add_src_to_python_path()

    try:
        from slow.ConexionBaseDeDatosSlow import initialize_schema

        initialize_schema()
    except ModuleNotFoundError as exc:
        missing_module = exc.name or "unknown"
        print(f"Database initialization failed: missing module '{missing_module}'.", file=sys.stderr)
        print("Install dependencies with: pip install -r requirements.txt", file=sys.stderr)
        return 1
    except Exception as exc:
        if _looks_like_mysql_connection_error(exc):
            print("Database initialization failed: could not connect to MySQL.", file=sys.stderr)
            print("Quick start with Docker:", file=sys.stderr)
            print("  docker compose up -d mysql", file=sys.stderr)
            print("  python3 scripts/init_database.py", file=sys.stderr)
            return 1
        print("Database initialization failed.", file=sys.stderr)
        print("Make sure MySQL is running and config/database.txt is correct.", file=sys.stderr)
        traceback.print_exc()
        return 1

    print("SLOW database schema is ready.")
    return 0


def _looks_like_mysql_connection_error(exc: Exception) -> bool:
    """Return True when an exception appears to be a PyMySQL connection failure."""
    return exc.__class__.__name__ == "OperationalError" and "MySQL" in str(exc)


if __name__ == "__main__":
    raise SystemExit(main())
