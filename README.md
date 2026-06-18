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

Run the app:

```bash
python3 scripts/run_app.py
```

The launcher adds `src/` to `PYTHONPATH` and starts `slow.main`.

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

This app expects a local MySQL database named `slow`.
