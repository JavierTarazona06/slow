# SLOW

SLOW is a Python/Tkinter desktop application for vehicle-speed detection, record keeping, and graph visualization.

## Run

From the project root:

```bash
pip install -r requirements.txt
```

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

This app expects a local MySQL database named `slow` and GUI support with Tkinter installed.
