from tkinter import *
import ConexionBaseDeDatosSlow as bD
from tkinter import messagebox
import VentanaMadre

class VentanaInicioSesion(VentanaMadre.VentanaMadre):
    
    def __init__(self):
        super().__init__()

        self.ventana.title("SLOW - Inicio de Sesión")
        self.crearWidgets()

    def crearWidgets(self):
        self.crearLogoSlow()
        self.crearElementos()

    def crearLogoSlow(self):
        self.logoSlowImg = PhotoImage(file=self.recursosGraficos["LOGOSLOW"])
        self.logoSlow = Label(self.base, image=self.logoSlowImg, bg="white").place(relx=0.324, rely=0.1)

    def crearElementos(self):
        self.avatarImg = PhotoImage(file=self.recursosGraficos["AVATAR"])
        self.avatarImg = self.avatarImg.subsample(15)
        self.avatar = Label(self.base, image=self.avatarImg, bg="white").place(relx=0.406, rely=0.42)

        self.usuarioEntrada = Entry(self.base,bg="white",fg="grey", justify="left", font=(30), width=25, border=3)
        self.usuarioEntrada.place(relx=0.4375, rely=0.43)
        self.usuarioEntrada.insert(0,'Usuario')
        self.usuarioEntrada.bind("<FocusIn>",self.defaultUsuario)
        self.usuarioEntrada.bind("<FocusOut>",self.defaultUsuario)
        self.usuarioEntrada.bind("<Return>",self.iniciarSesionE)

        self.candadoImg = PhotoImage(file=self.recursosGraficos["CANDADO"])
        self.candadoImg = self.candadoImg.subsample(15)
        self.candado = Label(self.base, image=self.candadoImg, bg="white").place(relx=0.406, rely=0.485)

        self.contrasenaEntrada = Entry(self.base,bg="white",fg="grey", justify="left", font=(30), width=25, border=3)
        self.contrasenaEntrada.place(relx=0.4375, rely=0.495)
        self.contrasenaEntrada.insert(0,'Contraseña')
        self.contrasenaEntrada.bind("<FocusIn>",self.defaultContrasena)
        self.contrasenaEntrada.bind("<FocusOut>",self.defaultContrasena)
        self.contrasenaEntrada.bind("<Return>",self.iniciarSesionE)

        self.ojoClaveAbiertoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVEABIERTO"])
        self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
        self.ojoClaveBoton = Button(self.base, image=self.ojoClaveAbiertoImg, command=self.abrirOjo,bg="white", border=1, relief="raised", cursor="hand2", bd=0)
        self.ojoClaveBoton.place(relx=0.5875, rely=0.49)
        self.ojoClaveBoton.bind("<Enter>",self.enOjoClaveBoton)
        self.ojoClaveBoton.bind("<Leave>",self.fueraOjoClaveBoton)

        self.iniciarSesionBoton = Button(self.base,text="Iniciar Sesión",bg="black",fg="white", cursor="hand2", font=(40), command=self.iniciarSesion, bd=4)
        self.iniciarSesionBoton.place(relx=0.46875, rely=0.585)
        self.iniciarSesionBoton.bind("<Enter>",self.enBotonIniciarSesion)
        self.iniciarSesionBoton.bind("<Leave>",self.fueraBotonIniciarSesion)

        self.crearCuentaBoton = Button(self.base,text="Crear Cuenta",bg="black",fg="white", cursor="hand2" ,font=(40), bd=4, command=self.crearCuenta)
        self.crearCuentaBoton.place(relx=0.468, rely=0.654)
        self.crearCuentaBoton.bind("<Enter>",self.enBotoCrearCuenta)
        self.crearCuentaBoton.bind("<Leave>",self.fueraBotoCrearCuenta)

        self.firmaUniversidad = Label(self.base, text="Universidad Nacional De Colombia", bg="white", font=(25)).place(relx=0.428125, rely=0.775)
        self.firmaPOO = Label(self.base, text="Proyecto Programación Orientada a Objetos", bg="white", font=(25)).place(relx=0.40625, rely=0.805)
        self.firmaAno = Label(self.base, text="2021", bg="white", font=(25)).place(relx=0.49,rely=0.835)

    def defaultUsuario(self,event):
        texto = self.usuarioEntrada.get()
        if texto == "Usuario":
            self.usuarioEntrada.delete(0,END)
            self.usuarioEntrada.config(fg="black")
        elif texto == "":
            self.usuarioEntrada.insert(0,"Usuario")
            self.usuarioEntrada.config(fg="grey")

    def defaultContrasena(self, event):
        texto = self.contrasenaEntrada.get()
        if texto == "Contraseña":
            self.contrasenaEntrada.delete(0,END)
            self.contrasenaEntrada.config(fg="black", show="*")
        elif texto == "":
            self.contrasenaEntrada.insert(0,"Contraseña")
            self.contrasenaEntrada.config(fg="grey", show="")

    def enOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=2)

    def fueraOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=0)

    def abrirOjo(self):
        texto = self.contrasenaEntrada.get()
        if texto != "Contraseña":
            self.ojoClaveCerradoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVECERRADO"])
            self.ojoClaveCerradoImg = self.ojoClaveCerradoImg.subsample(15)
            self.ojoClaveBoton.config(image=self.ojoClaveCerradoImg, command=self.cerrarOjo)
            self.contrasenaEntrada.config(show="")

    def cerrarOjo(self):
        texto = self.contrasenaEntrada.get()
        if texto != "Contraseña":
            self.ojoClaveAbiertoImg = PhotoImage(file=self.recursosGraficos["OJOCLAVEABIERTO"])
            self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
            self.ojoClaveBoton.config(image=self.ojoClaveAbiertoImg, command=self.abrirOjo)
            self.contrasenaEntrada.config(show="*")

    def enBotonIniciarSesion(self, event):
        self.iniciarSesionBoton.config(bd=6)

    def fueraBotonIniciarSesion(self, event):
        self.iniciarSesionBoton.config(bd=4)

    def enBotoCrearCuenta(self, event):
        self.crearCuentaBoton.config(bd=6)

    def fueraBotoCrearCuenta(self, event):
        self.crearCuentaBoton.config(bd=4)

    def iniciarSesionE(self,event):
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        usuario = self.usuarioEntrada.get()
        contrasena = self.contrasenaEntrada.get()
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO,USUARIO,AES_DECRYPT(CLAVE,'clave') FROM USUARIOS WHERE USUARIO='{usuario}' AND ESTADO='ACTIVO'")
        posiblesUsuarios = conexionSlow.cursorSlow.fetchall()
        iniciar = False
        for i in posiblesUsuarios:
            if (str(i[1])==usuario) and (str(i[2])=="b'"+contrasena+"'"):
                idUsuario = i[0]
                iniciar = True
        if (usuario=="Usuario" and contrasena=="Contraseña") or (usuario=="" and contrasena==""): iniciar= False
        if iniciar:
            self.ventana.destroy()
            import Slow as slowApp
            slowApp.elUsuario(idUsuario)
        else:
            messagebox.showerror('Error en Inicio de Sesión', 'Usuario o Clave Incorrecta\nFavor verifique e inténtelo nuevamente.')
        conexionSlow.cerrarBaseDeDatosSlow()

    def iniciarSesion(self):
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        usuario = self.usuarioEntrada.get()
        contrasena = self.contrasenaEntrada.get()
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO,USUARIO,AES_DECRYPT(CLAVE,'clave') FROM USUARIOS WHERE USUARIO='{usuario}'")
        posiblesUsuarios = conexionSlow.cursorSlow.fetchall()
        iniciar = False
        for i in posiblesUsuarios:
            if (str(i[1])==usuario) and (str(i[2])=="b'"+contrasena+"'"):
                idUsuario = i[0]
                iniciar = True
        if (usuario=="Usuario" and contrasena=="Contraseña") or (usuario=="" and contrasena==""): iniciar= False
        if iniciar:
            self.ventana.destroy()
            import Slow as slowApp
            slowApp.elUsuario(idUsuario)
        else:
            messagebox.showerror('Error en Inicio de Sesión', 'Usuario o Clave Incorrecta\nFavor verifique e inténtelo nuevamente.')
        conexionSlow.cerrarBaseDeDatosSlow()

    def crearCuenta(self):
        self.ventana.destroy()
        from CrearCuenta import VentanaRegistro
        ventanaRegistro = VentanaRegistro()
        ventanaRegistro.ventana.mainloop()