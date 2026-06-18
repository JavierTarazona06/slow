# Project Structure

The repository now follows a `src` layout:

```text
.
├── archive/
├── assets/
│   ├── graphics/
│   │   ├── resources/
│   │   └── ui/
│   └── videos/
│       └── samples/
├── build/
├── config/
│   └── pyinstaller/
├── docs/
├── outputs/
│   ├── captures/
│   ├── debug/
│   ├── graphs/
│   ├── images/
│   └── videos/
├── scripts/
│   ├── experiments/
│   └── run_app.py
└── src/
    └── slow/
```

`src/slow/paths.py` centralizes filesystem locations and maps legacy values such as `Videos\\video-1.mp4` and `RecursosGraficos\\...` to the reorganized folders.
