import cv2
import numpy as np
from .ArchivosYCarpetas import Carpeta
from .Imagenes import Imagen
from .Localizador_ob import *
import time
import pyscreenshot
from . import Graph as gp
from . import ConexionBaseDeDatosSlow as bD
from .paths import CAPTURES_DIR, VIDEOS_DIR, capture_path, path_string, project_relative_string, resolve_path_string, video_path

class Grafico_muestra:

    def __init__ (self,idusuario, idvia, multa, ciudad, direccion, path):
        self.idVideo = 0
        self.idUsuario = idusuario
        self.idVias = idvia
        self.multa = multa
        self.ciudad = ciudad
        self.direccion = direccion
        self.video = path
        self.carrosDetectados = []
        self.cancelarProcesamiento = False
        self.procesando = False
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f'''INSERT INTO DETECCIONYVIDEOS (IDUSUARIO,VIDEO,IDVIA,CIUDAD,DIRECCION,FECHA)
        VALUES ({self.idUsuario},'CAMBIO',{self.idVias},'{self.ciudad}','{self.direccion}',CURDATE())''')
        conexionSlow.cursorSlow.execute("SELECT IDVIDEO FROM DETECCIONYVIDEOS WHERE VIDEO='CAMBIO'")
        self.idVideo = conexionSlow.cursorSlow.fetchone()[0]
        carpetaVideos = Carpeta(VIDEOS_DIR)
        if not carpetaVideos.existeCarpeta:
            carpetaVideos.crearCarpeta()
        self.videoN = f"video-{self.idVideo}.mp4"
        carpetaVideos.copiarArchivo(self.video,self.videoN)
        conexionSlow.cursorSlow.execute(f"UPDATE DETECCIONYVIDEOS SET VIDEO='{project_relative_string(video_path(self.videoN))}' WHERE IDVIDEO={self.idVideo}")
        conexionSlow.cursorSlow.execute(f"SELECT LIMITEVELOCIDAD FROM VIAS WHERE IDVIA={self.idVias}")
        self.limiteVelocidad = float(conexionSlow.cursorSlow.fetchone()[0])

        carpetaCapturas = Carpeta(CAPTURES_DIR)
        if not carpetaCapturas.existeCarpeta:
            carpetaCapturas.crearCarpeta()

        conexionSlow.cerrarBaseDeDatosSlow()

    def abrirVideo(self):
        self.cancelarProcesamiento = False
        self.procesando = True
        self.carrosDetectados = []
        seguimiento = Localizador_ob()
        lecturaVideo = cv2.VideoCapture(resolve_path_string(self.video))
        if not lecturaVideo.isOpened():
            self.procesando = False
            return

        deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=15)
        carI = {}
        car0 = {}
        velocidades = {}
        nombreVentana = "Road"
        cv2.namedWindow(nombreVentana, cv2.WINDOW_NORMAL)

        try:
            while lecturaVideo.isOpened() and not self.cancelarProcesamiento:
                ret, vi = lecturaVideo.read()
                if not ret or vi is None:
                    break

                alto2, ancho2 = vi.shape[:2]
                mascara2 = np.zeros((alto2, ancho2), dtype=np.uint8)  # zeros rellenar matriz
                puntos = np.array([[[746, 293], [980, 293], [1142, 792], [476, 792]]])  # 2
                cv2.fillPoly(mascara2, puntos, 255)  # 2
                zona = cv2.bitwise_and(vi, vi, mask=mascara2)  # 2

                area_grande = [(746, 293), (980, 293), (1142, 792), (476, 792)]
                area_1 = [(1142, 792), (476, 792), (590, 590), (1070, 590)]
                area_2 = [(1070, 590), (590, 590), (675, 430), (1022, 430)]
                area_3 = [(746, 293), (980, 293), (1022, 430), (675, 430)]

                cv2.polylines(vi, [np.array(area_grande, np.int32)], True, (255, 255, 255), 2)
                cv2.polylines(vi, [np.array(area_3, np.int32)], True, (255, 255, 255), 2)
                cv2.polylines(vi, [np.array(area_2, np.int32)], True, (255, 255, 255), 2)
                cv2.polylines(vi, [np.array(area_1, np.int32)], True, (255, 255, 255), 2)

                mascara = deteccion.apply(zona)
                filtro = cv2.GaussianBlur(mascara, (19, 19), 0)
                _, umbral = cv2.threshold(filtro, 127, 255, cv2.THRESH_BINARY)
                dilatacion = cv2.dilate(umbral, np.ones((5, 5)))
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # matrices de ceros y unos, convoluciones
                cerrar = cv2.morphologyEx(dilatacion, cv2.MORPH_CLOSE, kernel)
                contornos, _ = cv2.findContours(cerrar, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                detecciones = []

                for i_contorno in contornos:
                    area_objeto = cv2.contourArea(i_contorno)
                    if area_objeto > 3000:  # se refiere a pixeles, esta sigue limpiando la imagen, hay puntitos blancos diminutos
                        x, y, ancho, alto = cv2.boundingRect(i_contorno)
                        # cv2.rectangle(zona, (x, y), (x + ancho, y + alto), (255, 255, 0), 3)
                        detecciones.append([x, y, ancho, alto])

                informacion_objeto_detectado = seguimiento.localizar(detecciones)
                for i_informacion in informacion_objeto_detectado:
                    x, y, ancho, alto, id = i_informacion
                    vel = 0
                    infractor = True
                    color = 0, 255, 255
                    cv2.rectangle(vi, (x, y), (x + ancho, y + alto), color, 2)

                    punto_centralx = int(x + ancho / 2)
                    punto_centraly = int(y + alto / 2)

                    seccion2 = cv2.pointPolygonTest(np.array(area_2, np.int32), (punto_centralx, punto_centraly), False)
                    if seccion2 >= 0:
                        carI[id] = time.process_time()

                    if id in carI:
                        cv2.circle(vi, (punto_centralx, punto_centraly), 3, (0, 0, 255), -1)
                        seccion3 = cv2.pointPolygonTest(np.array(area_3, np.int32), (punto_centralx, punto_centraly), False)

                        if seccion3 >= 0:
                            tiempo = time.process_time() - carI[id]
                            if tiempo % 1 == 0:
                                tiempo = tiempo + 0.3234
                            if tiempo % 1 != 0:
                                tiempo = tiempo + 1.016

                            if id not in car0:
                                car0[id] = tiempo

                            vel = 24.5 / car0[id]
                            vel *= 3.6
                            if vel > self.limiteVelocidad:
                                color = 0, 0, 255
                            else:
                                infractor = False
                                color = 0, 255, 0
                            cv2.rectangle(vi, (x, y), (x + ancho, y + alto), color, 2)

                            if id in velocidades:
                                velocidades[id][1] = vel
                                velocidades[id][2] = infractor
                                if velocidades[id][3] == 0:
                                    imagen = pyscreenshot.grab()
                                    captura_path = path_string(capture_path(f"Infractor_{str(id)}.png"))
                                    imagen.save(captura_path)
                                    velocidades[id][3] = captura_path
                                    self.guardarCarroDetectado(velocidades[id])
                                    if velocidades[id][2]:
                                        capturaImagen = Imagen(captura_path)
                                        capturaBinaria = capturaImagen.aHexaDecimalStr()
                                        conexionSlow = bD.ConexionBaseDeDatosSlow()
                                        conexionSlow.cursorSlow.execute(f'''INSERT INTO VEHICULOS 
                                        (IDVIDEO,CAPTURA,TIPOVEHICULO,PLACA,
                                        VELOCIDAD,IDVIA,VELOCIDADEXCEDIDA,MULTA,IDUSUARIO) 
                                        VALUES ({self.idVideo},'{capturaBinaria}','POR DEFINIR','POR DEFI',{velocidades[id][1]},
                                        {self.idVias},{velocidades[id][2]},{self.multa},{self.idUsuario})''')
                                        conexionSlow.cerrarBaseDeDatosSlow()
                            else:
                                velocidades[id] = [id, vel, infractor, 0]

                            cv2.rectangle(vi, (x, y - 10), (x + 100, y - 50), (0, 0, 0), -1)
                            cv2.putText(vi, str(int(vel)) + " KM / H", (x, y - 35), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

                    cv2.putText(vi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

                cv2.imshow(nombreVentana, vi)
                tecla = cv2.waitKey(1) & 0xFF
                if tecla == 27 or cv2.getWindowProperty(nombreVentana, cv2.WND_PROP_VISIBLE) < 1:
                    break

        finally:
            self.procesando = False
            lecturaVideo.release()
            cv2.destroyAllWindows()

    def detener(self):
        self.cancelarProcesamiento = True
        cv2.destroyAllWindows()

    def guardarCarroDetectado(self, datos):
        carro = [datos[0], float(datos[1]), bool(datos[2])]
        if carro[0] in [item[0] for item in self.carrosDetectados]:
            return
        self.carrosDetectados.append(carro)

    def evento_boton(self):
        self.grafic = gp.Graph(self.idVideo)
        self.grafic.limiteVelocidad = self.limiteVelocidad
        for carro in list(self.carrosDetectados):
            self.grafic.guardarCarros(carro)
        self.grafic.ventana.deiconify()
        self.grafic.graficarYMostrar()
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"UPDATE DETECCIONYVIDEOS SET GRAFICA='{project_relative_string(self.grafic.pathToSaveGraphs)}' WHERE IDVIDEO={self.idVideo}")
        conexionSlow.cerrarBaseDeDatosSlow()
