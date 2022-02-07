from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import VentanaMadre
import ConexionBaseDeDatosSlow as bD
from tkinter import filedialog
import Imagenes
from tkinter import messagebox
from PIL import Image,ImageTk

class VentanaRegistro(VentanaMadre.VentanaMadre):
    
    def __init__(self):
        super().__init__()

        self.ventana.title("SLOW - Crear Cuenta")
        self.crearWidgets()
 
    def crearWidgets(self):
        self.crearLogoSlow()
        self.crearElementos()

    def crearElementos(self):
        
        self.devolverImg = PhotoImage(file=self.recursosGraficos["DEVOLVER"])
        self.devolverImg = self.devolverImg.subsample(11)
        self.botonDevolver = Button(self.base,image=self.devolverImg,bg="white", cursor="hand2", bd=0, command=self.devolver)
        self.botonDevolver.place(relx=0.02, rely=0.02)
        self.botonDevolver.bind("<Enter>",self.enBotonDevolver)
        self.botonDevolver.bind("<Leave>",self.fueraBotonDevolver)

        self.tituloCrearCuenta = Label(self.base, text="CREAR UNA CUENTA", bg="white", font=("",20,"bold"))
        self.tituloCrearCuenta.place(relx=0.409, rely=0.1944)

        self.xCol1, self.yCol1 = 0.0375, 0.3
        self.xCol1b, self.yCol1b = 0.146, 0.305
        self.xCol2, self.yCol2 = 0.383, 0.3
        self.xCol2b, self.yCol2b = 0.4925, 0.305
        self.xCol3, self.yCol3 = 0.6975, 0.3
        self.xCol3b, self.yCol3b = 0.806, 0.305
        self.altura = 0.088

        self.usuarioText = Label(self.base, text="Usuario:", bg="white", font=("",17,"bold"))
        self.usuarioText.place(relx=self.xCol1, rely=self.yCol1)
        self.usuarioEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.usuarioEntrada.place(relx=self.xCol1b, rely=self.yCol1b)

        self.contrasenaText = Label(self.base, text="Contraseña:", bg="white", font=("",17,"bold"))
        self.contrasenaText.place(relx=self.xCol1, rely=self.yCol1+self.altura)
        self.contrasenaEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3, show="*")
        self.contrasenaEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura)
        self.contrasenaNota = Label(self.base, text="*De 10 carácteres mínimo e incluya números.", bg="white", fg="red", font=("",8,""), justify="left")
        self.contrasenaNota.place(relx=self.xCol1b, rely=self.yCol1b+self.altura+0.03)

        self.ojoClaveAbiertoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVEABIERTO"])
        self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
        self.ojoClaveBoton = Button(self.base, image=self.ojoClaveAbiertoImg, command=self.abrirOjo,bg="white", border=1, relief="raised", cursor="hand2", bd=0)
        self.ojoClaveBoton.place(relx=self.xCol1b+0.153, rely=self.yCol1b+0.083)
        self.ojoClaveBoton.bind("<Enter>",self.enOjoClaveBoton)
        self.ojoClaveBoton.bind("<Leave>",self.fueraOjoClaveBoton)

        self.nombreText = Label(self.base, text="Nombre:", bg="white", font=("",17,"bold"))
        self.nombreText.place(relx=self.xCol1, rely=self.yCol1+self.altura*2)
        self.nombreEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.nombreEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*2)

        self.apellidoText = Label(self.base, text="Apellido:", bg="white", font=("",17,"bold"))
        self.apellidoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*3)
        self.apellidoEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.apellidoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*3)

        self.tipoDocumentoText = Label(self.base, text="Tipo de\nDocumento:", bg="white", font=("",17,"bold"), justify="left")
        self.tipoDocumentoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*4-0.011)
        self.tipoDocumentoEntrada = ttk.Combobox(self.base, state="readonly")
        self.tipoDocumentoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*4)
        self.tipoDocumentoEntrada["values"] = ["C.C", "C.E", "T.P"]
        self.tipoDocumentoEntrada.current(0)

        self.numeroDocumentoText = Label(self.base, text="Número de\nDocumento:", bg="white", font=("",17,"bold"), justify="left")
        self.numeroDocumentoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*5-0.011)
        self.numeroDocumentoEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.numeroDocumentoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*5)

        self.imagenPerfilText = Label(self.base, text="Imagen de\nPerfil:", bg="white", font=("",17,"bold"), justify="left")
        self.imagenPerfilText.place(relx=self.xCol1, rely=self.yCol1+self.altura*6-0.011)
        self.imgPrlBoton = Button(self.base,text="Subir Imagen",bg="black",fg="white", cursor="hand2", font=(40), bd=4, command=self.abrirArchivo)
        self.imgPrlBoton.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*6)
        self.imgPrlBoton.bind("<Enter>",self.enBotonImagenPerfil)
        self.imgPrlBoton.bind("<Leave>",self.fueraBotonImagenPerfil)
        self.confirmacionImagenCargada = Label(self.base, text="No se ha cargado la imagen opcional", bg="white", font=(5), fg="red")
        self.confirmacionImagenCargada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*6+0.044)
        self.imagenPerfilEntrada = ""

        self.tipoSangreText = Label(self.base, text="Tipo de\nSangre:", bg="white", font=("",17,"bold"), justify="left")
        self.tipoSangreText.place(relx=self.xCol2, rely=self.yCol2-0.011)
        self.tipoSangreEntrada = ttk.Combobox(self.base, state="readonly")
        self.tipoSangreEntrada.place(relx=self.xCol2b, rely=self.yCol2b)
        self.tipoSangreEntrada["values"] = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
        self.tipoSangreEntrada.current(6)

        self.jefeText = Label(self.base, text="ID Jefe:", bg="white", font=("",17,"bold"), justify="left")
        self.jefeText.place(relx=self.xCol2, rely=self.yCol2+self.altura)
        self.jefeDisplay = StringVar()
        self.jefeEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3, textvariable=self.jefeDisplay)
        self.jefeEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura)
        self.jefeTextNota = Label(self.base, text="*Sí es policía, indique el ID de su jefe\nde la app Slow.", bg="white", fg="red", font=("",8,""), justify="left")
        self.jefeTextNota.place(relx=self.xCol2b, rely=self.yCol2b+self.altura+0.029)

        self.policiasAsignadosText = Label(self.base, text="Policías\nAsignados:", bg="white", font=("",17,"bold"), justify="left")
        self.policiasAsignadosText.place(relx=self.xCol2, rely=self.yCol2+self.altura*2-0.011)
        self.policiasAsignadosDisplay = StringVar()
        self.policiasAsignadosEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3, textvariable=self.policiasAsignadosDisplay)
        self.policiasAsignadosEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*2)
        self.policiasAsignadosTextNota = Label(self.base, text="*Sí es jefe de policía, indique el ID de sus\npolicías asignados separados por comas.", bg="white", fg="red", font=("",8,""), justify="left")
        self.policiasAsignadosTextNota.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*2+0.029)

        self.asignacionText = Label(self.base, text="Asignación:", bg="white", font=("",17,"bold"), justify="left")
        self.asignacionText.place(relx=self.xCol2, rely=self.yCol2+self.altura*3)
        self.asignacionEntrada = ttk.Combobox(self.base, state="readonly")
        self.asignacionEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*3)
        self.asignacionEntrada["values"] = ["TRÁNSITO"]
        self.asignacionEntrada.current(0)

        self.rolText = Label(self.base, text="Rol:", bg="white", font=("",17,"bold"), justify="left")
        self.rolText.place(relx=self.xCol2, rely=self.yCol2+self.altura*4)
        self.rolEntrada = ttk.Combobox(self.base, state="readonly")
        self.rolEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*4)
        self.rolEntrada["values"] = ["POLICÍA","JEFE"]
        self.rolEntrada.current(0)

        self.numeroCuadranteText = Label(self.base, text="Número de\nCuadrante:", bg="white", font=("",17,"bold"), justify="left")
        self.numeroCuadranteText.place(relx=self.xCol2, rely=self.yCol2+self.altura*5-0.011)
        self.numeroCuadranteEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.numeroCuadranteEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*5)

        self.cuadranteText = Label(self.base, text="Cuadrante:", bg="white", font=("",17,"bold"), justify="left")
        self.cuadranteText.place(relx=self.xCol2, rely=self.yCol2+self.altura*6)
        self.cuadranteEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.cuadranteEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*6)

        self.ciudadText = Label(self.base, text="Ciudad:", bg="white", font=("",17,"bold"), justify="left")
        self.ciudadText.place(relx=self.xCol3, rely=self.yCol3)
        self.ciudadEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.ciudadEntrada.place(relx=self.xCol3b, rely=self.yCol3b)

        self.departamentoText = Label(self.base, text="Departamento:", bg="white", font=("",17,"bold"), justify="left")
        self.departamentoText.place(relx=self.xCol3, rely=self.yCol3+self.altura)
        self.departamentoEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.departamentoEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura)

        self.horarioText = Label(self.base, text="Horario:", bg="white", font=("",17,"bold"), justify="left")
        self.horarioText.place(relx=self.xCol3, rely=self.yCol3+self.altura*2)
        self.horarioTextNota = Label(self.base, text="*En formato: 7:00-12:00 / 14:00-18:00", bg="white", fg="red", font=("",8,""), justify="left")
        self.horarioTextNota.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2+0.055)
        self.listaHoras = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
        self.listaMinutos = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
            "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
        self.hora1Entrada = ttk.Combobox(self.base, state="readonly")
        self.hora1Entrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2, width=35)
        self.hora1Entrada["values"] = self.listaHoras
        self.hora1Entrada.current(0)
        self.sep1 = Label(self.base, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.021875, rely=self.yCol3b+self.altura*2)
        self.minuto1Entrada = ttk.Combobox(self.base, state="readonly")
        self.minuto1Entrada.place(relx=self.xCol3b+0.028125, rely=self.yCol3b+self.altura*2, width=35)
        self.minuto1Entrada["values"] = self.listaMinutos
        self.minuto1Entrada.current(0)
        self.sep2 = Label(self.base, text="-", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.05, rely=self.yCol3b+self.altura*2)
        self.hora2Entrada = ttk.Combobox(self.base, state="readonly")
        self.hora2Entrada.place(relx=self.xCol3b+0.05625, rely=self.yCol3b+self.altura*2, width=35)
        self.hora2Entrada["values"] = self.listaHoras
        self.hora2Entrada.current(0)
        self.sep3 = Label(self.base, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.078125, rely=self.yCol3b+self.altura*2)
        self.minuto2Entrada = ttk.Combobox(self.base, state="readonly")
        self.minuto2Entrada.place(relx=self.xCol3b+0.084375, rely=self.yCol3b+self.altura*2, width=35)
        self.minuto2Entrada["values"] = self.listaMinutos
        self.minuto2Entrada.current(0)
        self.sep4 = Label(self.base, text=" / ", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.109375, rely=self.yCol3b+self.altura*2)
        self.hora3Entrada = ttk.Combobox(self.base, state="readonly")
        self.hora3Entrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2+0.029, width=35)
        self.hora3Entrada["values"] = self.listaHoras
        self.hora3Entrada.current(0)
        self.sep5 = Label(self.base, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.021875, rely=self.yCol3b+self.altura*2+0.029)
        self.minuto3Entrada = ttk.Combobox(self.base, state="readonly")
        self.minuto3Entrada.place(relx=self.xCol3b+0.028125, rely=self.yCol3b+self.altura*2+0.029, width=35)
        self.minuto3Entrada["values"] = self.listaMinutos
        self.minuto3Entrada.current(0)
        self.sep6 = Label(self.base, text="-", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.05, rely=self.yCol3b+self.altura*2+0.029)
        self.hora4Entrada = ttk.Combobox(self.base, state="readonly")
        self.hora4Entrada.place(relx=self.xCol3b+0.05625, rely=self.yCol3b+self.altura*2+0.029, width=35)
        self.hora4Entrada["values"] = self.listaHoras
        self.hora4Entrada.current(0)
        self.sep7 = Label(self.base, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.078125, rely=self.yCol3b+self.altura*2+0.029)
        self.minuto4Entrada = ttk.Combobox(self.base, state="readonly")
        self.minuto4Entrada.place(relx=self.xCol3b+0.084375, rely=self.yCol3b+self.altura*2+0.029, width=35)
        self.minuto4Entrada["values"] = self.listaMinutos
        self.minuto4Entrada.current(0)

        self.direccionText = Label(self.base, text="Dirección:", bg="white", font=("",17,"bold"), justify="left")
        self.direccionText.place(relx=self.xCol3, rely=self.yCol3+self.altura*3)
        self.direccionEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.direccionEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*3)
        self.direccionTextNota = Label(self.base, text="*En formato: CRA 70 A No. 4242 BRR\nFELICIDAD CASA 2 BOGOTÁ", bg="white", fg="red", font=("",8,""), justify="left")
        self.direccionTextNota.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*3+0.029)

        self.celularText = Label(self.base, text="Celular:", bg="white", font=("",17,"bold"), justify="left")
        self.celularText.place(relx=self.xCol3, rely=self.yCol3+self.altura*4)
        self.celularEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.celularEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*4)

        self.correoText = Label(self.base, text="Correo:", bg="white", font=("",17,"bold"), justify="left")
        self.correoText.place(relx=self.xCol3, rely=self.yCol3+self.altura*5)
        self.correoEntrada = Entry(self.base,bg="white",fg="black", justify="left", font=(16), width=25, border=3)
        self.correoEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*5)

        self.guardarBoton = Button(self.base,text="Guardar y Crear Cuenta",bg="black",fg="white", cursor="hand2", font=(40), command=self.guardarYCrearCuenta, bd=4)
        self.guardarBoton.place(relx=self.xCol3b-0.040625, rely=self.yCol3b+self.altura*6)
        self.guardarBoton.bind("<Enter>",self.enBotonGuardar)
        self.guardarBoton.bind("<Leave>",self.fueraBotonGuardar)

    def enBotonDevolver(self, event):
        self.devolverImg = PhotoImage(file=self.recursosGraficos["DEVOLVER"])
        self.devolverImg = self.devolverImg.subsample(10)
        self.botonDevolver.config(image = self.devolverImg)

    def fueraBotonDevolver(self, event):
        self.devolverImg = PhotoImage(file=self.recursosGraficos["DEVOLVER"])
        self.devolverImg = self.devolverImg.subsample(11)
        self.botonDevolver.config(image = self.devolverImg)

    def devolver(self):
        self.ventana.destroy()
        from InicioSesion import VentanaInicioSesion
        ventanaInicioSesion = VentanaInicioSesion()
        ventanaInicioSesion.ventana.mainloop()

    def enOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=2)

    def fueraOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=0)

    def abrirOjo(self):
        self.ojoClaveCerradoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVECERRADO"])
        self.ojoClaveCerradoImg = self.ojoClaveCerradoImg.subsample(15)
        self.ojoClaveBoton.config(image=self.ojoClaveCerradoImg, command=self.cerrarOjo)
        self.contrasenaEntrada.config(show="")

    def cerrarOjo(self):
        self.ojoClaveAbiertoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVEABIERTO"])
        self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
        self.ojoClaveBoton.config(image=self.ojoClaveAbiertoImg, command=self.abrirOjo)
        self.contrasenaEntrada.config(show="*")

    def enBotonImagenPerfil(self, event):
        self.imgPrlBoton.config(bd=6)

    def fueraBotonImagenPerfil(self, event):
        self.imgPrlBoton.config(bd=4)

    def abrirArchivo(self):
        self.imagenPerfilEntrada = str(filedialog.askopenfile(title="Abrir Archivo Foto de Perfil",initialdir="C:/",
            filetypes=(("PNG Image","*.png"),("JPG Image","*.jpg"))))
        startPath = self.imagenPerfilEntrada.find("'")
        endPath = self.imagenPerfilEntrada.find("'",startPath+1)
        self.imagenPerfilEntrada = self.imagenPerfilEntrada[startPath+1:endPath]
        if self.imagenPerfilEntrada != "Non":
            self.confirmacionImagenCargada.config(text="Imagen Cargada", fg="green")

    def enBotonGuardar(self, event):
        self.guardarBoton.config(bd=6)

    def fueraBotonGuardar(self, event):
        self.guardarBoton.config(bd=4)

    def guardarYCrearCuenta(self):
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        messageBoxTit, messageBoxContent = "Error al Crear Cuenta", "Todos los campos son requeridos.\nFavor registre: "
        usuario = str(self.usuarioEntrada.get())
        if usuario == "":
            return messagebox.showerror(messageBoxTit, messageBoxContent+"Usuario")
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE USUARIO='{usuario}'")
        usuarioEncontrado = conexionSlow.cursorSlow.fetchall()
        if len(usuarioEncontrado)>0:
            return messagebox.showerror(messageBoxTit, "Usuario ya existe. Inicie sesión o registre uno nuevo.")
        clave = str(self.contrasenaEntrada.get())
        if clave == "":
            return messagebox.showerror(messageBoxTit, messageBoxContent+"Contraseña")
        if (len(clave)<10)or((clave.find("0")==-1)and(clave.find("1")==-1)and(clave.find("2")==-1)and(clave.find("3")==-1)and(clave.find("4")==-1)and(clave.find("5")==-1)and(clave.find("6")==-1)and(clave.find("7")==-1)and(clave.find("8")==-1)and(clave.find("9")==-1)):
            return messagebox.showerror(messageBoxTit, "Clave digitada de forma Incorrecta.")
        nombre = str(self.nombreEntrada.get())
        if nombre == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Nombre")
        apellido = str(self.apellidoEntrada.get())
        if apellido == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Apellido")
        tipoDocumento = str(self.tipoDocumentoEntrada.get())
        if tipoDocumento == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Tipo de Documento")
        numeroDocumento = str(self.numeroDocumentoEntrada.get())
        if numeroDocumento == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Número de Documento")
        else:
            try:
                numeroDocumento = int(numeroDocumento)
            except ValueError:
                return messagebox.showerror(messageBoxTit,"El Número de Documento debe ser un Número.")
            if numeroDocumento <= 99999:
                return messagebox.showerror(messageBoxTit,"El Número de Documento debe ser un Número mayor a 99999")
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE NUMERODOCUMENTO='{numeroDocumento}'")
        numeroDocumentoEncontrado = conexionSlow.cursorSlow.fetchall()
        if len(numeroDocumentoEncontrado)>0:
            return messagebox.showerror(messageBoxTit, "Número de documento ya existe.")
        imagenPerfilPath = str(self.imagenPerfilEntrada)
        if imagenPerfilPath == "Non" or imagenPerfilPath=="":
            imagenPerfilPath = str(self.recursosGraficos["PERFILDEFECTO"])
        imagenPerfilObjeto = Imagenes.Imagen(imagenPerfilPath)
        imagenPerfil = imagenPerfilObjeto.aHexaDecimalStr()
        tipoSangre = str(self.tipoSangreEntrada.get())
        if tipoSangre == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Tipo de Sangre")
        rol = str(self.rolEntrada.get())
        if rol=="JEFE":
            idJefe = 0
            self.jefeDisplay.set("0")
            policiasAsignados = str(self.policiasAsignadosEntrada.get())
            if policiasAsignados == "":
                policiasAsignados = "0"
                self.policiasAsignadosDisplay.set("0")
            listaPoliciasAsignados = policiasAsignados.split(sep=",")
            if (not listaPoliciasAsignados[0]=="0") and len(listaPoliciasAsignados)==1:
                for i in listaPoliciasAsignados:
                    try:
                        idPolicia = int(i)
                    except ValueError:
                        return messagebox.showerror(messageBoxTit,"Recuerde ingresar solo los ID válidos de Slow para\nlos policías asignados separados por comas")
                    conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idPolicia}' AND ROL='POLICIA'")
                    policiaEncontrado = conexionSlow.cursorSlow.fetchall()
                    if len(policiaEncontrado)==0:
                        return messagebox.showerror(messageBoxTit, f"No existe el ID del policía {idPolicia}. Ingresar uno existente o crear uno nuevo")
        else:
            idJefe = str(self.jefeDisplay.get())
            if idJefe == "":
                return messagebox.showerror(messageBoxTit,messageBoxContent+"ID de Jefe")
            else:
                try:
                    idJefe = int(idJefe)
                except ValueError:
                    return messagebox.showerror(messageBoxTit,"El ID de Jefe debe ser un Número.")
                if idJefe <= 0:
                    return messagebox.showerror(messageBoxTit,"ID de Jefe incorrecto.")
            conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idJefe}' AND ROL='JEFE'")
            jefeEncontrado = conexionSlow.cursorSlow.fetchall()
            if len(jefeEncontrado)==0:
                return messagebox.showerror(messageBoxTit, "No existe ese jefe. Ingresar uno existente o crear uno nuevo")
            policiasAsignados = "0"
            self.policiasAsignadosDisplay.set("0")
        numeroCuadrante = self.numeroCuadranteEntrada.get()
        if numeroCuadrante == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Número de Cuadrante")
        else:
            try:
                numeroCuadrante = int(numeroCuadrante)
            except ValueError:
                return messagebox.showerror(messageBoxTit,"El Número de Cuadrante debe ser un Número.")
            if numeroCuadrante <= 0:
                return messagebox.showerror(messageBoxTit,"El Número de Cuadrante debe ser un Número mayor a 0.")
        cuadrante = str(self.cuadranteEntrada.get())
        if cuadrante == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Cuadrante")
        ciudad = str(self.ciudadEntrada.get())
        if ciudad == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Ciudad")
        departamento = str(self.departamentoEntrada.get())
        if departamento == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Departamento")
        if (int(self.hora1Entrada.get())>int(self.hora2Entrada.get())) or (int(self.hora2Entrada.get())>int(self.hora3Entrada.get())) or (int(self.hora3Entrada.get())>int(self.hora4Entrada.get())) or (self.hora1Entrada.get()=="0" and self.hora2Entrada.get()=="0"):
            return messagebox.showerror(messageBoxTit,"El horario se digitó Incorrectamente.")
        self.horarioEntrada = f"{self.hora1Entrada.get()}:{self.minuto1Entrada.get()}-{self.hora2Entrada.get()}:{self.minuto2Entrada.get()} / {self.hora3Entrada.get()}:{self.minuto3Entrada.get()}-{self.hora4Entrada.get()}:{self.minuto4Entrada.get()}"
        horario = str(self.horarioEntrada)
        if horario == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Horario")
        direccion = str(self.direccionEntrada.get())
        if direccion == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Dirección")
        celular = self.celularEntrada.get()
        if celular == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Celular")
        else:
            try:
                celular = int(celular)
            except ValueError:
                return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número.")
            if celular <= 0:
                return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número mayor a 0.")
        correo = str(self.correoEntrada.get())
        if correo == "":
            return messagebox.showerror(messageBoxTit,messageBoxContent+"Correo")
        if (correo.find("@policia.gov.co")==-1):
            return messagebox.showerror(messageBoxTit,"El correo electrónico debe terminar en @policia.gov.co")
        conexionSlow.cursorSlow.execute(f'''INSERT INTO USUARIOS (
            USUARIO,CLAVE,NOMBRE,APELLIDO,TIPODOCUMENTO,NUMERODOCUMENTO,
            IMAGENPERFIL,TIPOSANGRE,JEFE,POLICIASASIGNADOS,ASIGNACION,ROL,
            NUMEROCUADRANTE,CUADRANTE,CIUDAD,DEPARTAMENTO,HORARIO,ESTADO,
            DIRECCION,CELULAR,CORREO,FONDO
        ) VALUES (
            '{usuario}',AES_ENCRYPT('{clave}','clave'),'{nombre}','{apellido}','{tipoDocumento}',{numeroDocumento},
            '{imagenPerfil}','{tipoSangre}',{idJefe},'{policiasAsignados}','TRÁNSITO','{rol}',
            {numeroCuadrante},'{cuadrante}','{ciudad}','{departamento}','{horario}','ACTIVO',
            '{direccion}',{celular},'{correo}','CLARO'
        )''')
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE USUARIO='{usuario}'")
        usuarioEncontrado = conexionSlow.cursorSlow.fetchall()
        if len(usuarioEncontrado)>0:
            messagebox.showinfo("Información Slow", "Información Guardada Exitosamente.\nRegrese al módulo de iniciar sesión e inicie sesión")
        else:
            messagebox.showerror(messageBoxTit,"No se guardaron los datos. Inténtelo nuevamente o reporte el problema para una solución")
        conexionSlow.cerrarBaseDeDatosSlow()