from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
SRC_DIR = PACKAGE_DIR.parent
PROJECT_ROOT = SRC_DIR.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
UI_ASSETS_DIR = ASSETS_DIR / "graphics" / "ui"
RESOURCE_ASSETS_DIR = ASSETS_DIR / "graphics" / "resources"
SAMPLE_VIDEOS_DIR = ASSETS_DIR / "videos" / "samples"

CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
CAPTURES_DIR = OUTPUTS_DIR / "captures"
GRAPHS_DIR = OUTPUTS_DIR / "graphs"
VIDEOS_DIR = OUTPUTS_DIR / "videos"
DEBUG_OUTPUT_DIR = OUTPUTS_DIR / "debug"
OUTPUT_IMAGES_DIR = OUTPUTS_DIR / "images"
ROAD_IMAGES_DIR = OUTPUT_IMAGES_DIR / "roads"
VEHICLE_IMAGES_DIR = OUTPUT_IMAGES_DIR / "vehicles"
PROFILE_IMAGES_DIR = OUTPUT_IMAGES_DIR / "profiles"


def ensure_runtime_directories():
    for path in (
        CAPTURES_DIR,
        GRAPHS_DIR,
        VIDEOS_DIR,
        DEBUG_OUTPUT_DIR,
        ROAD_IMAGES_DIR,
        VEHICLE_IMAGES_DIR,
        PROFILE_IMAGES_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)


def path_string(path):
    return str(Path(path))


def project_relative_string(path):
    resolved_path = Path(path).resolve()
    try:
        return resolved_path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def _clean_legacy_path(path):
    return str(path).replace("\\", "/")


def resolve_path(path):
    raw_path = Path(str(path))
    if raw_path.is_absolute():
        return raw_path

    clean_path = _clean_legacy_path(path)
    clean = Path(clean_path)

    legacy_roots = {
        "RecursosGraficos": RESOURCE_ASSETS_DIR,
        "Capturas": CAPTURES_DIR,
        "Graficas": GRAPHS_DIR,
        "Videos": VIDEOS_DIR,
    }

    parts = clean.parts
    legacy_resource_outputs = {
        ("RecursosGraficos", "ImgVias"): ROAD_IMAGES_DIR,
        ("RecursosGraficos", "ImgVehiculos"): VEHICLE_IMAGES_DIR,
        ("RecursosGraficos", "ImagenesPerfil"): PROFILE_IMAGES_DIR,
        ("RecursosGraficos", "Grafica"): GRAPHS_DIR / "resources",
    }

    if len(parts) >= 2 and parts[:2] in legacy_resource_outputs:
        return legacy_resource_outputs[parts[:2]].joinpath(*parts[2:])

    if parts and parts[0] in {"assets", "config", "outputs"}:
        return PROJECT_ROOT / clean

    if parts and parts[0] in legacy_roots:
        return legacy_roots[parts[0]].joinpath(*parts[1:])

    candidates = (
        UI_ASSETS_DIR / clean,
        RESOURCE_ASSETS_DIR / clean,
        SAMPLE_VIDEOS_DIR / clean,
        OUTPUTS_DIR / clean,
        PROJECT_ROOT / clean,
    )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return UI_ASSETS_DIR / clean


def resolve_path_string(path):
    return path_string(resolve_path(path))


def resource_path(*parts):
    return RESOURCE_ASSETS_DIR.joinpath(*parts)


def resource_path_string(*parts):
    return path_string(resource_path(*parts))


def ui_asset_path(*parts):
    return UI_ASSETS_DIR.joinpath(*parts)


def ui_asset_path_string(*parts):
    return path_string(ui_asset_path(*parts))


def capture_path(filename):
    CAPTURES_DIR.mkdir(parents=True, exist_ok=True)
    return CAPTURES_DIR / filename


def graph_path(filename):
    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    return GRAPHS_DIR / filename


def video_path(filename):
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    return VIDEOS_DIR / filename


def debug_output_path(filename):
    DEBUG_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return DEBUG_OUTPUT_DIR / filename


def road_image_path(filename):
    ROAD_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    return ROAD_IMAGES_DIR / filename


def vehicle_image_path(filename):
    VEHICLE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    return VEHICLE_IMAGES_DIR / filename


def profile_image_path(filename):
    PROFILE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    return PROFILE_IMAGES_DIR / filename


def legacy_output_path(path):
    clean_path = _clean_legacy_path(path)
    first_part = Path(clean_path).parts[0]
    if first_part == "Capturas":
        return str(Path("outputs") / "captures" / Path(clean_path).name)
    if first_part == "Graficas":
        return str(Path("outputs") / "graphs" / Path(clean_path).name)
    if first_part == "Videos":
        return str(Path("outputs") / "videos" / Path(clean_path).name)
    return str(Path(clean_path))
