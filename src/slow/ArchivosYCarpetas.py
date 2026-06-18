import os
import shutil

from .paths import resolve_path

class Carpeta():
    def __init__(self, path):
        self.carpetaPath = resolve_path(path)
        self.existeCarpeta = self.carpetaPath.is_dir()

    def crearCarpeta(self):
        self.existeCarpeta = self.carpetaPath.is_dir()
        if not self.existeCarpeta:
            self.carpetaPath.mkdir(parents=True, exist_ok=True)
            print("Carpeta Creada")
        self.existeCarpeta = self.carpetaPath.is_dir()

    def eliminarCarpeta(self):
        self.existeCarpeta = self.carpetaPath.is_dir()
        if self.existeCarpeta:
            os.rmdir(self.carpetaPath)
            print("Carpeta Eliminada")
        self.existeCarpeta = self.carpetaPath.is_dir()

    def copiarArchivo(self,pathArchivo,nombreArchivo):
        destino = self.carpetaPath / nombreArchivo
        shutil.copy(resolve_path(pathArchivo), destino)
        print(f"{nombreArchivo} copiado")

    def eliminarArchivo(self,pathArchivo):
        os.unlink(resolve_path(pathArchivo))
        print(f"{pathArchivo} eliminado")
