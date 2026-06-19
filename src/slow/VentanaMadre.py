import _tkinter as Tk
from tkinter import *
from .paths import resource_path_string
from .window_icon import set_window_icon

class VentanaMadre():
    def __init__(self):

        self.recursosGraficos = {"LOGOSLOW": resource_path_string("Logo_Slow.png"),
        "DEVOLVER": resource_path_string("DEVOLVER.png"),
        "MENU": resource_path_string("MENU.png"),
        "RECARGAR": resource_path_string("RECARGAR.png"),
        "ELIMINAR": resource_path_string("ELIMINAR.png"),
        "MULTA": resource_path_string("MULTA.png"),
        "AVATAR": resource_path_string("AVATAR.png"),
        "CANDADO": resource_path_string("CANDADO.png"),
        "OJOCLAVECERRADO": resource_path_string("OJOCLAVECERRADO.png"),
        "OJOCLAVEABIERTO": resource_path_string("OJOCLAVEABIERTO.png"),
        "TARJETADOCUMENTO": resource_path_string("TARJETADOCUMENTO.png"),
        "CORREO": resource_path_string("CORREO.png"),
        "ROL": resource_path_string("ROL.png"),
        "CLAVE": resource_path_string("CLAVE.png"),
        "POLICIA":'POLICIA NACIONAL',
        "ESCUDOPOLICIA": resource_path_string("ESCUDOPOLICIA.png"),
        "PAIS":'REPÚBLICA DE COLOMBIA',
        "BANDERAPAIS": resource_path_string("BANDERAPAIS.png"),
        "INFORMACION": resource_path_string("INFORMACION.png"),
        "ACTUALIZARDATOS": resource_path_string("ACTUALIZARDATOS.png"),
        "REGISTRARVIDEOS": resource_path_string("REGISTRARVIDEOS.png"),
        "VEHICULOSVIAS": resource_path_string("VEHICULOSVIAS.png"),
        "HISTORICO": resource_path_string("HISTORICO.png"),
        "PERFILDEFECTO": resource_path_string("PERFILDEFECTO.png"),
        "VIADEFECTO": resource_path_string("VIADEFECTO.png")}

        #Root------------

        self.ventana = Tk()

        self.ancho = self.ventana.winfo_screenwidth()
        self.alto = self.ventana.winfo_screenheight()

        self.ventana.title("SLOW")
        #self.ventana.title("SLOW - Inicio de Sesión")
        set_window_icon(self.ventana)
        self.ventana.config(bg="white")
        self.ventana.geometry(f"{self.ancho}x{self.alto}+0+0")
        self.ventana.resizable(False,False)

        #Base------------

        self.base = Frame(self.ventana, bg="white").pack()

    def crearWidgets(self):
        self.crearLogoSlow()
        self.crearLogoEscudoPolicia()
        self.crearLogoPais()

    def crearLogoSlow(self):
        self.logoSlowImg = PhotoImage(file=self.recursosGraficos["LOGOSLOW"])
        self.logoSlowImg = self.logoSlowImg.subsample(2)
        self.logoSlow = Label(self.base, image=self.logoSlowImg, bg="white").place(relx=0.409,rely=0.01)

    def crearLogoEscudoPolicia(self):
        self.logoEscudoPoliciaImg = PhotoImage(file=self.recursosGraficos["ESCUDOPOLICIA"])
        self.logoEscudoPoliciaImg = self.logoEscudoPoliciaImg.subsample(16)
        self.logoEscudoPolicia = Label(self.base, image=self.logoEscudoPoliciaImg, bg="white").place(relx=0.025, rely=0.0125)
        self.policiaNacional = Label(self.base, text="POLICIA NACIONAL", bg="white").place(relx=0.0171, rely=0.1125)

    def crearLogoPais(self):
        self.paisImg = PhotoImage(file=self.recursosGraficos["BANDERAPAIS"])
        self.paisImg  = self.paisImg.subsample(9)
        self.pais = Label(self.base, image=self.paisImg , bg="white").place(relx=0.906, rely=0.025)
        self.paisText = Label(self.base, text="REPÚBLICA DE COLOMBIA", bg="white").place(relx=0.89, rely=0.1125)
