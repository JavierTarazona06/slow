import os
import shutil

class Carpeta():
    def __init__(self, path):
        self.carpetaPath = f"{path}"
        self.existeCarpeta = os.path.isdir(self.carpetaPath)

    def crearCarpeta(self):
        self.existeCarpeta = os.path.isdir(self.carpetaPath)
        if not self.existeCarpeta:
            os.makedirs(self.carpetaPath)
            print("Carpeta Creada")
        self.existeCarpeta = os.path.isdir(self.carpetaPath)

    def eliminarCarpeta(self):
        self.existeCarpeta = os.path.isdir(self.carpetaPath)
        if self.existeCarpeta:
            os.rmdir(self.carpetaPath)
            print("Carpeta Eliminada")
        self.existeCarpeta = os.path.isdir(self.carpetaPath)

    def copiarArchivo(self,pathArchivo,nombreArchivo):
        shutil.copy(f"{pathArchivo}",f"{self.carpetaPath}\\{nombreArchivo}")
        print(f"{nombreArchivo} copiado")

    def eliminarArchivo(self,pathArchivo):
        os.unlink(f"{pathArchivo}")
        print(f"{pathArchivo} eliminado")
'''' 
def main():
    carpetaVideos = Carpeta("S:\Videos")
    carpetaVideos.crearCarpeta()
    carpetaVideos.copiarArchivo("H:\Mi unidad\\2. Semester\Object Oriented Programming (OOP)\Exercises and Works\Proyecto POO\Slow\Programación de SLOW\RecursosGraficos\INFORMACION.png","INFORMACION.png")
    #carpetaVideos.eliminarArchivo("S:\Videos\INFORMACION.png")
    #carpetaVideos.eliminarCarpeta()

main()
'''