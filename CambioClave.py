import VentanaMadre
from tkinter import*
import ConexionBaseDeDatosSlow as bD
from tkinter import messagebox

class CambioClave(VentanaMadre.VentanaMadre):
    def __init__(self,idUsuario):
        super().__init__()
        self.ventana.title("SLOW - Cambiar Clave")
        self.ventana.geometry("680x400")
        self.ventana.resizable(False,False)
        self.idUsuario = idUsuario
        self.crearWidgets()

    def crearWidgets(self):
        self.crearElementos()

    def crearElementos(self):
        self.tituloCambioClave = Label(self.base, text="Para cambiar la clave ingrese la contraseña anterior", bg="white", font=("",17,"bold"))
        self.tituloCambioClave.place(relx=0.05, rely=0.05)

        self.campContrasenaAnterior = CampoContrasena(self.base,"Contraseña Anterior:",0.1,0.3)
        self.campContrasenaAnteriorConf = CampoContrasena(self.base,"Confirma Contraseña\nAnterior:",0.1,0.5)
        self.campContrasenaNueva = CampoContrasena(self.base,"Nueva Contraseña:",0.1,0.7)

        self.verificarBoton = Button(self.base,text="Verificar",bg="black",fg="white", cursor="hand2", font=(40), command=self.verificar, bd=4)
        self.verificarBoton.place(relx=0.5, rely=0.85)
        self.verificarBoton.bind("<Enter>",self.enBotonVerificar)
        self.verificarBoton.bind("<Leave>",self.fueraBotonVerificar)

    def enBotonVerificar(self, event):
        self.verificarBoton.config(bd=6)

    def fueraBotonVerificar(self, event):
        self.verificarBoton.config(bd=4)

    def verificar(self):
        contrAnt = self.campContrasenaAnterior.contrasenaTexto.get()
        contrAntConf = self.campContrasenaAnteriorConf.contrasenaTexto.get()
        if not contrAnt==contrAntConf:
            return messagebox.showerror("SLOW - Error al Verificar Clave","Las claves no coinciden")
        if contrAnt=="":
            return messagebox.showerror("SLOW - Error al Verificar Clave","La clave no puede quedar en blanco")

class CampoContrasena():
    def __init__(self,base,textoContrasena,posx,posy):
        self.base = base
        self.contrasenaText = Label(self.base, text=f"{textoContrasena}", bg="white", font=("",15,"bold"))
        self.contrasenaText.place(relx=posx, rely=posy)
        self.contrasenaTexto = StringVar()
        self.contrasenaEntrada = Entry(self.base,bg="white",textvariable=self.contrasenaTexto,fg="black", justify="left", font=(16), width=25, border=3, show="*")
        self.contrasenaEntrada.place(relx=posx+0.4, rely=posy)
        self.contrasenaNota = Label(self.base, text="*De 10 carácteres mínimo e incluya números.", bg="white", fg="red", font=("",8,""), justify="left")
        self.contrasenaNota.place(relx=posx+0.4, rely=posy+0.1)
        self.contrasenaTexto.set("")

        self.ojoClaveAbiertoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVEABIERTO.png")
        self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
        self.ojoClaveBoton = Button(self.base, image=self.ojoClaveAbiertoImg, command=self.abrirOjo,bg="white", border=1, relief="raised", cursor="hand2", bd=0)
        self.ojoClaveBoton.place(relx=0.863, rely=posy-0.02)
        self.ojoClaveBoton.bind("<Enter>",self.enOjoClaveBoton)
        self.ojoClaveBoton.bind("<Leave>",self.fueraOjoClaveBoton)

    def enOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=2)

    def fueraOjoClaveBoton(self, event):
        self.ojoClaveBoton.config(bd=0)

    def abrirOjo(self):
        self.ojoClaveCerradoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVECERRADO.png")
        self.ojoClaveCerradoImg = self.ojoClaveCerradoImg.subsample(15)
        self.ojoClaveBoton.config(image=self.ojoClaveCerradoImg, command=self.cerrarOjo)
        self.contrasenaEntrada.config(show="")

    def cerrarOjo(self):
        self.ojoClaveAbiertoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVEABIERTO.png")
        self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
        self.ojoClaveBoton.config(image=self.ojoClaveAbiertoImg, command=self.abrirOjo)
        self.contrasenaEntrada.config(show="*")

def cambio(id):
    global ventana
    ventana = CambioClave(id)
    ventana.ventana.mainloop()
def destruir():
    ventana.ventana.destroy()