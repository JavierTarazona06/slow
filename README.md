# SLOW

SLOW is a Python desktop application for vehicle-speed detection, evidence capture, record management, and graph visualization. It uses Tkinter for the interface, OpenCV for video processing, Matplotlib for graphs, and MySQL for persistent data.

## Main Features

- User login and account management.
- Vehicle-speed detection from uploaded videos.
- Evidence capture for detected infractions.
- Vehicle and road record management.
- Historical video and graph visualization.
- MySQL-backed data storage.
- PyInstaller-based executable generation.

## Requirements

- Python 3.10 or newer.
- Tkinter system package.
- MySQL server, or Docker for the included MySQL service.
- Pip packages listed in `requirements.txt`.
- For executable builds: packages listed in `requirements-dev.txt`.

Tkinter is not installed with `pip`. On Ubuntu/Debian, install it with:

```bash
sudo apt install python3-tk
```

## Installation

From the project root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install runtime dependencies:

```bash
pip install -r requirements.txt
```

Start the included MySQL service:

```bash
docker compose up -d mysql
```

Initialize the database schema:

```bash
python3 scripts/init_database.py
```

## Run From Source

Run the application with:

```bash
python3 scripts/run_app.py
```

The launcher prepares the local `src/` import path and starts `slow.main`.

## Generate The Executable

Install build dependencies:

```bash
pip install -r requirements-dev.txt
```

Build the executable:

```bash
python3 scripts/build_executable.py
```

The executable is generated in `dist/`. Temporary PyInstaller files are generated in `build/pyinstaller/`. Both folders are ignored by Git.

## Run The Executable

Make sure MySQL is running first:

```bash
docker compose up -d mysql
```

Then run the generated executable from `dist/`.

On Linux:

```bash
./dist/slow
```

On Windows, run:

```powershell
.\dist\slow.exe
```

If you use custom database settings, place a local `config/database.txt` next to the project during development, or set these environment variables before launching the executable:

- `SLOW_DB_HOST`
- `SLOW_DB_PORT`
- `SLOW_DB_USER`
- `SLOW_DB_PASSWORD`
- `SLOW_DB_NAME`

## Project Structure

```text
.
├── assets/              # Bundled images, icons, and sample videos
├── config/              # Local config templates and PyInstaller spec
├── docs/                # Documentation
├── outputs/             # Runtime-generated files
├── scripts/             # Entry-point, setup, and build scripts
├── src/slow/            # Application source code
├── docker-compose.yml   # MySQL service for local development
├── requirements.txt     # Runtime Python dependencies
└── requirements-dev.txt # Build/development dependencies
```

## Notes And Troubleshooting

### MySQL Connection Refused

If you see an error like `Can't connect to MySQL server on 'localhost'`, start MySQL and initialize the schema:

```bash
docker compose up -d mysql
python3 scripts/init_database.py
```

### Missing Tkinter

If Python cannot import `tkinter`, install the system package:

```bash
sudo apt install python3-tk
```

### Missing PyInstaller

If executable generation fails because PyInstaller is missing, install build dependencies:

```bash
pip install -r requirements-dev.txt
```

### Generated Files

Runtime outputs, build artifacts, virtual environments, local database credentials, and OS metadata are ignored by Git through `.gitignore`.
