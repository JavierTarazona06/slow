from .InicioSesion import VentanaInicioSesion
from .paths import ensure_runtime_directories


def main():
    ensure_runtime_directories()
    ventana_inicio_sesion = VentanaInicioSesion()
    ventana_inicio_sesion.ventana.mainloop()


if __name__ == "__main__":
    main()
