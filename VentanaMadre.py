import _tkinter as Tk
from tkinter import *

class VentanaMadre():
    def __init__(self):

        self.recursosGraficos = {"LOGOSLOWICO":"RecursosGraficos\\Logo_Slow_Icon_Map.ico",
        "LOGOSLOW":'RecursosGraficos\\\Logo_Slow.png',
        "DEVOLVER":'RecursosGraficos\\\DEVOLVER.png',
        "MENU":'RecursosGraficos\\\MENU.png',
        "RECARGAR":'RecursosGraficos\\\RECARGAR.png',
        "ELIMINAR":'RecursosGraficos\\\ELIMINAR.png',
        "MULTA":'RecursosGraficos\\\MULTA.png',
        "AVATAR":'RecursosGraficos\\\AVATAR.png',
        "CANDADO":'RecursosGraficos\\\CANDADO.png',
        "OJOCLAVECERRADO":'RecursosGraficos\\\OJOCLAVECERRADO.png',
        "OJOCLAVEABIERTO":'RecursosGraficos\\\OJOCLAVEABIERTO.png',
        "TARJETADOCUMENTO":'RecursosGraficos\\\TARJETADOCUMENTO.png',
        "CORREO":'RecursosGraficos\\\CORREO.png',
        "ROL":'RecursosGraficos\\\ROL.png',
        "CLAVE":'RecursosGraficos\\\CLAVE.png',
        "POLICIA":'POLICIA NACIONAL',
        "ESCUDOPOLICIA":'RecursosGraficos\\\ESCUDOPOLICIA.png',
        "PAIS":'REPÚBLICA DE COLOMBIA',
        "BANDERAPAIS":'RecursosGraficos\\\BANDERAPAIS.png',
        "INFORMACION":'RecursosGraficos\\\INFORMACION.png',
        "ACTUALIZARDATOS":'RecursosGraficos\\\ACTUALIZARDATOS.png',
        "REGISTRARVIDEOS":'RecursosGraficos\\\REGISTRARVIDEOS.png',
        "VEHICULOSVIAS":'RecursosGraficos\\\VEHICULOSVIAS.png',
        "HISTORICO":'RecursosGraficos\\\HISTORICO.png',
        "PERFILDEFECTO":'RecursosGraficos\\\PERFILDEFECTO.png',
        "VIADEFECTO":'RecursosGraficos\\\VIADEFECTO.png'}

        #Root------------

        self.ventana = Tk()

        self.ancho = self.ventana.winfo_screenwidth()
        self.alto = self.ventana.winfo_screenheight()

        self.ventana.title("SLOW")
        #self.ventana.title("SLOW - Inicio de Sesión")
        self.ventana.iconbitmap(self.recursosGraficos["LOGOSLOWICO"])
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