# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_DIR = PROJECT_ROOT / "assets"
DATABASE_EXAMPLE = PROJECT_ROOT / "config" / "database.example.txt"
ICON_PATH = ASSETS_DIR / "graphics" / "resources" / "Logo_Slow_Icon_Map.ico"


block_cipher = None


a = Analysis(
    [str(PROJECT_ROOT / "scripts" / "run_app.py")],
    pathex=[str(SRC_DIR)],
    binaries=[],
    datas=[
        (str(ASSETS_DIR), "assets"),
        (str(DATABASE_EXAMPLE), "config"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="slow",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(ICON_PATH),
)
