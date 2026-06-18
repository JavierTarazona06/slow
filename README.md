# SLOW

SLOW is a Python/Tkinter desktop application for vehicle-speed detection, record keeping, and graph visualization.

## Run

From the project root:

Tkinter is required for the desktop UI. It is a system package, not a pip dependency, so it is intentionally not listed in `requirements.txt`.

On Ubuntu/Debian:

```bash
sudo apt install python3-tk
```

Then install the pip dependencies:

```bash
pip install -r requirements.txt
```

Start MySQL with Docker:

```bash
docker compose up -d mysql
```

Initialize the database tables:

```bash
python3 scripts/init_database.py
```

Run the app:

```bash
python3 scripts/run_app.py
```

The launcher adds `src/` to `PYTHONPATH` and starts `slow.main`.

## Build Executable

Install the build dependencies:

```bash
pip install -r requirements-dev.txt
```

Build the executable with PyInstaller:

```bash
python3 scripts/build_executable.py
```

The generated executable is written to `dist/`. Temporary PyInstaller files are written to `build/pyinstaller/`. Both locations are ignored by Git.

## Project Layout

- `src/slow/` - application source code
- `scripts/` - runnable scripts, including `scripts/run_app.py`
- `assets/` - bundled static images, icons, and sample videos
- `config/` - configuration and build specs
- `outputs/` - generated/runtime files such as uploaded videos, captures, graphs, and extracted DB images
- `build/` - generated build artifacts
- `docs/` - project documentation
- `archive/` - legacy or preserved files that are not part of the active runtime

## Notes

This app expects a local MySQL database named `slow`. The fastest setup is the included Docker Compose service, which exposes MySQL on `localhost:3306` with user `root`, password `root`, and database `slow`.

Local database credentials can be customized with `config/database.txt` or these environment variables:

- `SLOW_DB_HOST`
- `SLOW_DB_PORT`
- `SLOW_DB_USER`
- `SLOW_DB_PASSWORD`
- `SLOW_DB_NAME`
