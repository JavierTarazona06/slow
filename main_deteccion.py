from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from Localizador_ob import *
import time
import pyscreenshot
import Graph as gp

class Grafico_muestra:

    def _init_(self, idvideo, idusuario, idvias, multa):
        self.idVideo= idvideo
        self.idUsuario = idusuario
        self.idVias = idvias
        self.multa = multa

        ventana = Tk()
        Button(ventana, text="Abrir video a detectar", command=self.abrirVideo).pack()
        ventana.mainloop()


    def abrirVideo(self):
        seguimiento = Localizador_ob()
        self.grafic = gp.Graph(self.idVideo, self.idUsuario, self.idVias, self.multa)
        video = filedialog.askopenfilename(title="ABRIR VIDEO PARA DETECCIÓN")  # aqui se guarda el path del video
        print(video)
        lecturaVideo = cv2.VideoCapture(video)

        # fps = 30
        # fps = lecturaVideo.get(cv2.CAP_PROP_FPS)
        delay = 2
        deteccion = cv2.createBackgroundSubtractorMOG2(history=10000,
                                                       varThreshold=15)  # OPEN CV llama un metodo de segmentacion, nuestro objeto queda en negro y lo demas en blanco, historu se refiere al numero de procesamientos, y el umbral mas detecciones se tendra,(depende en donde vayamos a poner los videos o imageenes)

        carI = {}
        car0 = {}

        velocidades = {}
        aux = 0
        while (lecturaVideo.isOpened()):
            ret, vi = lecturaVideo.read()

            alto2 = vi.shape[0]  # (m, n) matriz 2
            ancho2 = vi.shape[1]

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

            # if ret == False:
            # break
            # vi = cv2.resize(vi, (1920, 1080))  # se le baja la calidad al video

            # puros filtros que pasan una imagen mas limpia
            mascara = deteccion.apply(zona)
            # hace un blur
            filtro = cv2.GaussianBlur(mascara, (19, 19), 0)
            # este es el mas importante porque nos bota las cosas a blanco y negro
            _, umbral = cv2.threshold(filtro, 127, 255, cv2.THRESH_BINARY)

            dilatacion = cv2.dilate(umbral, np.ones((5, 5)))

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # matrices de ceros y unos, convoluciones

            cerrar = cv2.morphologyEx(dilatacion, cv2.MORPH_CLOSE, kernel)

            # se esta aplicando a la zona de interes, es decir mps esta enviando la imagen negra
            # _, mascara = cv2.threshold(mascara, 254, 255, cv2.THRESH_BINARY) #¡¡¡¡¡¡
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
                # cv2.putText(zona, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

                vel = 0
                infractor = True

                if vel == 0:
                    color = 0, 255, 255
                cv2.rectangle(vi, (x, y), (x + ancho, y + alto), (color), 2)

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
                            # print(tiempo)

                        if tiempo % 1 != 0:
                            tiempo = tiempo + 1.016
                            # print(tiempo)

                        if id not in car0:
                            car0[id] = tiempo

                        if id in car0:
                            tiempo = car0[id]

                            vel = 24.5 / car0[id]
                            vel *= 3.6
                            if vel > 60:
                                captura_pantalla = True
                                color = 0, 0, 255


                            else:
                                infractor = False
                                color = 0, 255, 0
                            cv2.rectangle(vi, (x, y), (x + ancho, y + alto), (color), 2)

                        if id in velocidades:
                            if velocidades[id][3] == 0:
                                imagen = pyscreenshot.grab()
                                imagen.save(f"Infractor_{str(id)}.png")
                                velocidades[id][3] = f"Infractor_{str(id)}.png"
                                #SEe pasan los datos de la gráfica
                                self.grafic.guardarCarros(grafica)

                        else:
                            #bbox = (x, y, x + ancho, y + alto)
                            grafica = [id, vel, infractor, 0]
                            velocidades[id] = grafica

                        cv2.rectangle(vi, (x, y - 10), (x + 100, y - 50), (0, 0, 0), -1)
                        cv2.putText(vi, str(int(vel)) + " KM / H", (x, y - 35), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
                        # print(id)
                        # print(vel)

                    cv2.putText(vi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

            # print(informacion_objeto_detectado)
            # cv2.imshow("Zona de interes", zona)
            # cv2.imshow("calle", filtro)

            cv2.imshow("calle", vi)
            #cv2.imshow("cerrar", cerrar)
            # cv2.imshow("zona donde se hara la detección", zona)
            if cv2.waitKey(1) & 0xFF == 27:
                break

            # time.sleep(delay)

        lecturaVideo.release()
        cv2.destroyAllWindows()

    def envento_boton(self):
        self.grafic.graficarYMostrar()
        self.grafic = gp.Graph(self.grafic)

Grafico_muestra(1, 2, 3 ,4)